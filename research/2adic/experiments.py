"""Small exact laboratory for parity and 2-adic relation profiles."""

from __future__ import annotations

import itertools
import json
import math
import random
from pathlib import Path


def lcm(a: int, b: int) -> int:
    return abs(a // math.gcd(a, b) * b)


def data_for_v(v: tuple[int, ...]) -> dict:
    q = len(v) + 1
    W = 1
    for x in v:
        W = lcm(W, x)
    b = tuple(W // x for x in v)
    periods = tuple(q * x for x in b)
    valuations = tuple((x & -x).bit_length() - 1 for x in v)
    units = tuple(x >> s for x, s in zip(v, valuations))
    return {
        "q": q,
        "W": W,
        "b": b,
        "periods": periods,
        "valuation_profile": valuations,
        "units": units,
    }


def relation(v: tuple[int, ...], a: tuple[int, ...], q: int, W: int) -> bool:
    return sum(x * y for x, y in zip(a, v)) % (q * W) == 0


def carry_profile(v: tuple[int, ...], a: tuple[int, ...]) -> dict:
    valuation = [(x & -x).bit_length() - 1 for x in v]
    units = [x >> s for x, s in zip(v, valuation)]
    max_layer = max(valuation + [0])
    carries = []
    equations = []
    carry = 0
    for s in range(max_layer + 1):
        B = sum(coef * unit for coef, unit, layer in zip(a, units, valuation)
                 if layer == s)
        total = B + carry
        equations.append({"s": s, "B": B, "carry_in": carry,
                          "divisible_by_2": total % 2 == 0})
        if total % 2:
            return {
                "valid_through_layers": False,
                "equations": equations,
                "carries": carries,
            }
        carry = total // 2
        carries.append(carry)
    return {
        "valid_through_layers": True,
        "equations": equations,
        "carries": carries,
        "terminal_carry": carry,
    }


def profile(v: tuple[int, ...], a: tuple[int, ...]) -> dict:
    info = data_for_v(v)
    cp = carry_profile(v, a)
    return {
        "a": list(a),
        "parity": sum(a) % 2,
        "support_size": sum(x != 0 for x in a),
        "l1": sum(abs(x) for x in a),
        "linf": max(map(abs, a), default=0),
        "active_layers": sorted({
            (x & -x).bit_length() - 1
            for x, coef in zip(v, a) if coef
        }),
        "carry_depth": len(cp["carries"]),
        "nontrivial_carries": sum(x != 0 for x in cp["carries"]),
        "carry_profile": cp,
        "canonical": all(0 <= x < p for x, p in zip(a, info["periods"])),
    }


def canonical_relations(v: tuple[int, ...], state_cap: int = 2_000_000):
    info = data_for_v(v)
    count = math.prod(info["periods"])
    if count > state_cap:
        return [], {"enumerated": False, "state_count": count}
    out = []
    for a in itertools.product(*(range(p) for p in info["periods"])):
        if relation(v, a, info["q"], info["W"]):
            out.append(profile(v, a))
    return out, {"enumerated": True, "state_count": count}


def short_relations(v: tuple[int, ...], radius: int = 8):
    info = data_for_v(v)
    out = []
    for a in itertools.product(range(-radius, radius + 1), repeat=len(v)):
        if a != (0,) * len(v) and relation(v, a, info["q"], info["W"]):
            out.append(profile(v, a))
    return out


def exhaustive_cases(max_n: int = 5, max_v: int = 10, radius: int = 3):
    cases = []
    for n in range(2, max_n + 1):
        for v in itertools.combinations(range(1, max_v + 1), n):
            rels, meta = canonical_relations(v, state_cap=100_000)
            short = short_relations(v, radius=radius)
            odd_short = [x for x in short if x["parity"] == 1]
            cases.append({
                "V": list(v),
                "canonical_meta": meta,
                "canonical_odd_count": sum(x["parity"] == 1 for x in rels),
                "short_odd_count": len(odd_short),
                "short_odd_min_l1": min((x["l1"] for x in odd_short), default=None),
                "short_odd_profiles": odd_short[:20],
            })
    return cases


def targeted_one_layer_counterexample():
    # V={1,3}: qW=9 and a=(0,3) gives 0*1+3*3=9.
    v = (1, 3)
    a = (0, 3)
    info = data_for_v(v)
    assert relation(v, a, info["q"], info["W"])
    p = profile(v, a)
    assert p["parity"] == 1
    assert p["active_layers"] == [0]
    return {"V": list(v), "a": list(a), "profile": p}


def main():
    random.seed(0)
    random_cases = []
    for n in range(6, 9):
        for _ in range(5):
            v = tuple(sorted(random.sample(range(1, 101), n)))
            short = short_relations(v, radius=3)
            odd_short = [x for x in short if x["parity"] == 1]
            random_cases.append({
                "V": list(v),
                "short_odd_count": len(odd_short),
                "short_odd_min_l1": min(
                    (x["l1"] for x in odd_short), default=None
                ),
                "short_odd_profiles": odd_short[:20],
            })
    result = {
        "scope": {
            "exhaustive_n": [2, 5],
            "exhaustive_v_bound": 10,
            "random_n": [6, 8],
            "random_cases_per_n": 5,
            "short_radius": 3,
            "status": "VERIFIED computationally, not a proof",
        },
        "one_layer_counterexample": targeted_one_layer_counterexample(),
        "exhaustive": exhaustive_cases(radius=3),
        "random": random_cases,
    }
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"wrote {path}")
    print("one-layer odd counterexample: V=[1,3], a=[0,3]")


if __name__ == "__main__":
    main()
