"""Exact global k-aggregation for the support-2 finite dual formula."""

from __future__ import annotations

import math
from fractions import Fraction


def lcm(a: int, b: int) -> int:
    return abs(a // math.gcd(a, b) * b)


def setup(v):
    q = len(v) + 1
    W = 1
    for x in v:
        W = lcm(W, x)
    return q, W, q * W


def hq(q: int, z: Fraction) -> Fraction:
    alpha = Fraction(q - 2, 2 * q)
    value = Fraction(1, alpha) * (
        1 - abs(z - Fraction(1, 2)) / alpha
    )
    return max(Fraction(0), value)


def axis_line(q: int, b: int) -> Fraction:
    if q % 2 == 0 or b % 2 == 0:
        return Fraction(1)
    return Fraction(1) - Fraction(1, (q - 2) ** 2 * b * b)


def aggregate(v: tuple[int, ...], state_cap: int = 100_000):
    q, W, M = setup(v)
    if M > state_cap:
        return {"enumerated": False, "M": M}
    sum_pairs = Fraction(0)
    safe_counts = []
    for k in range(M):
        hs = [
            hq(q, Fraction((k * x) % M, M))
            for x in v
        ]
        safe_counts.append(sum(x > 0 for x in hs))
        pair_mass = sum(
            (hs[i] * hs[j] for i in range(len(v))
             for j in range(i + 1, len(v))),
            Fraction(0),
        )
        sum_pairs += pair_mass
    pair_total = sum_pairs / M
    axis_lines = [
        axis_line(q, W // x)
        for x in v
    ]
    axis_global = sum(axis_lines, Fraction(0)) - (len(v) - 1)
    f_le2 = (
        pair_total
        - (len(v) - 2) * axis_global
        - Fraction((len(v) - 1) * (len(v) - 2), 2)
    )
    direct_f2 = pair_total - sum(
        (axis_lines[i] + axis_lines[j] - 1
         for i in range(len(v)) for j in range(i + 1, len(v))),
        Fraction(0),
    )
    assert direct_f2 == f_le2 - axis_global
    return {
        "enumerated": True,
        "q": q,
        "W": W,
        "M": M,
        "sum_T_pairs": str(pair_total),
        "axis_lines": [str(x) for x in axis_lines],
        "F_axis": str(axis_global),
        "F2": str(direct_f2),
        "F_le2": str(f_le2),
        "safe_count_min": min(safe_counts),
        "safe_count_max": max(safe_counts),
        "safe_count_histogram": {
            str(n): safe_counts.count(n)
            for n in sorted(set(safe_counts))
        },
    }
