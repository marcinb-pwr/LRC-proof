"""Exact axis formulas and finite genuine-relation experiments."""

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
    W = math.prod(v)
    for x in v:
        W = lcm(W, x)
    b = tuple(W // x for x in v)
    return q, W, b


def axis_exact(v):
    q, W, b = setup(v)
    if q % 2 == 0:
        value = Fraction(1)
    else:
        value = Fraction(1)
        for bi in b:
            if bi % 2:
                value -= Fraction(1, (q - 2) ** 2 * bi * bi)
    return value


def sinc_sq(x):
    if x == 0:
        return 1.0
    return (math.sin(math.pi * x) / (math.pi * x)) ** 2


def relation(v, a, q, W):
    return sum(x * y for x, y in zip(a, v)) % (q * W) == 0


def finite_split(v, radius=3):
    q, W, b = setup(v)
    axis = 0.0
    genuine = 0.0
    counts = {"axis": 0, "genuine": 0, "odd_genuine": 0}
    for a in itertools.product(range(-radius, radius + 1), repeat=len(v)):
        if not relation(v, a, q, W):
            continue
        x = 1.0
        for ai in a:
            x *= sinc_sq((q - 2) * ai / (2 * q))
        signed = (-1.0) ** sum(a)
        if sum(x != 0 for x in a) <= 1:
            axis += signed * x
            counts["axis"] += 1
        else:
            genuine += signed * x
            counts["genuine"] += 1
            counts["odd_genuine"] += sum(a) % 2
    return {
        "axis_truncated": axis,
        "genuine_truncated": genuine,
        "counts": counts,
        "axis_exact": str(axis_exact(v)),
    }


def families():
    out = []
    for n in range(2, 9):
        out.extend([
            ("consecutive", tuple(range(1, n + 1))),
            ("odd", tuple(2 * i + 1 for i in range(n))),
            ("powers_two", tuple(2 ** i for i in range(n))),
            ("translated", tuple(range(7, 7 + n))),
        ])
    random.seed(1)
    for n in range(2, 9):
        for _ in range(3):
            out.append(("random", tuple(sorted(random.sample(range(1, 80), n)))))
    return out


def main():
    rows = []
    for name, v in families():
        row = {"family": name, "V": list(v)}
        row.update(finite_split(v))
        rows.append(row)
    path = Path(__file__).with_name("axis_results.json")
    path.write_text(json.dumps(rows, indent=2) + "\n")
    print(f"wrote {path} ({len(rows)} cases)")
    print("V=(1,3):", axis_exact((1, 3)))
    print("V=(1,2):", axis_exact((1, 2)))


if __name__ == "__main__":
    main()
