"""Exact full relation lattice and its finite dual classes."""

from __future__ import annotations

import math
from fractions import Fraction


def lcm(a: int, b: int) -> int:
    return abs(a // math.gcd(a, b) * b)


def setup(v: tuple[int, ...]):
    q = len(v) + 1
    W = 1
    for x in v:
        W = lcm(W, x)
    M = q * W
    d = math.gcd(M, *v)
    det = M // d
    return q, W, M, d, det


def relation_lattice_basis_description(v: tuple[int, ...]):
    q, W, M, d, det = setup(v)
    return {
        "q": q,
        "W": W,
        "M": M,
        "gcd": d,
        "det_relation_lattice": det,
        "dual": "Z^N + Z*(v_1/M,...,v_N/M)",
    }


def dual_class_points(v: tuple[int, ...], delta: Fraction):
    """Return dual classes whose unique [delta,1-delta]^N lift exists."""
    q, W, M, d, det = setup(v)
    points = []
    for k in range(det):
        coords = tuple(Fraction((k * x) % M, M) for x in v)
        if all(delta <= z <= 1 - delta for z in coords):
            points.append((k, coords))
    return points
