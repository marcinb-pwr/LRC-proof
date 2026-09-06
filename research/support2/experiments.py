"""Exact support-2 relation and Fourier experiments."""

from __future__ import annotations

import itertools
import json
import math
import random
from fractions import Fraction
from pathlib import Path


def lcm(a, b):
    return abs(a // math.gcd(a, b) * b)


def setup(v):
    q = len(v) + 1
    W = 1
    for x in v:
        W = lcm(W, x)
    b = tuple(W // x for x in v)
    return q, W, b


def relation(vi, vj, r, s, q, W):
    return (r * vi + s * vj) % (q * W) == 0


def gq(q, n):
    if n == 0:
        return 1.0
    x = (q - 2) * n / (2 * q)
    return (math.sin(math.pi * x) / (math.pi * x)) ** 2


def axis_exact(v):
    q, _, b = setup(v)
    if q % 2 == 0:
        return Fraction(1)
    return Fraction(1) - sum(
        (Fraction(1, (q - 2) ** 2 * bi * bi) for bi in b if bi % 2),
        Fraction(0),
    )


def support2_short(v, i, j, radius=8):
    q, W, _ = setup(v)
    vi, vj = v[i], v[j]
    out = []
    for r, s in itertools.product(range(-radius, radius + 1), repeat=2):
        if not r or not s or not relation(vi, vj, r, s, q, W):
            continue
        if (r + s) % 2 == 1:
            out.append((abs(r) + abs(s), r, s))
    return sorted(out)


def pair_exact_box(v, i, j, cap=100_000):
    q, W, b = setup(v)
    periods = (q * b[i], q * b[j])
    states = periods[0] * periods[1]
    if states > cap:
        return {"enumerated": False, "states": states}
    vi, vj = v[i], v[j]
    rows = []
    for r, s in itertools.product(range(periods[0]), range(periods[1])):
        if not r or not s or not relation(vi, vj, r, s, q, W):
            continue
        rows.append({
            "r": r,
            "s": s,
            "parity": (r + s) % 2,
            "l1": r + s,
        })
    return {"enumerated": True, "states": states, "relations": rows}


def pair_short_sum(v, i, j, radius=8):
    q, W, _ = setup(v)
    vi, vj = v[i], v[j]
    signed = 0.0
    odd_mass = 0.0
    even_mass = 0.0
    rows = support2_short(v, i, j, radius)
    for _, r, s in rows:
        w = gq(q, r) * gq(q, s)
        signed += (-1.0) ** (r + s) * w
        if (r + s) % 2:
            odd_mass += w
        else:
            even_mass += w
    return {
        "short_signed": signed,
        "short_odd_mass": odd_mass,
        "short_even_mass": even_mass,
        "min_odd_l1": rows[0][0] if rows else None,
        "odd_short_count": len(rows),
    }


def cases():
    out = []
    for n in range(2, 9):
        out.extend([
            ("consecutive", tuple(range(1, n + 1))),
            ("odd", tuple(2 * k + 1 for k in range(n))),
            ("powers_two", tuple(2 ** k for k in range(n))),
            ("translated", tuple(range(7, 7 + n))),
        ])
    random.seed(2)
    for n in range(2, 9):
        for _ in range(3):
            out.append(("random", tuple(sorted(random.sample(range(1, 80), n)))))
    return out


def analyze(name, v):
    q, W, b = setup(v)
    pairs = []
    total_signed = 0.0
    total_odd = 0.0
    min_l1 = None
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            short = pair_short_sum(v, i, j)
            box = pair_exact_box(v, i, j)
            total_signed += short["short_signed"]
            total_odd += short["short_odd_mass"]
            if short["min_odd_l1"] is not None:
                min_l1 = min(min_l1 or short["min_odd_l1"],
                             short["min_odd_l1"])
            pairs.append({"i": i, "j": j, **short, "box": box})
    return {
        "family": name,
        "V": list(v),
        "q": q,
        "W": W,
        "b": list(b),
        "axis_exact": str(axis_exact(v)),
        "support2_short_signed": total_signed,
        "support2_short_odd_mass": total_odd,
        "axis_plus_support2_short": float(axis_exact(v)) + total_signed,
        "min_odd_l1": min_l1,
        "pairs": pairs,
    }


def main():
    rows = [analyze(name, v) for name, v in cases()]
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(rows, indent=2) + "\n")
    print(f"wrote {path} ({len(rows)} cases)")
    negatives = [r for r in rows if r["axis_plus_support2_short"] < 0]
    print(f"negative truncated axis+support2 cases: {len(negatives)}")


if __name__ == "__main__":
    main()
