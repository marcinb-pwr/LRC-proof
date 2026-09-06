"""Exact rank-2 lattice and finite dual-box arithmetic."""

from __future__ import annotations

import math
from fractions import Fraction


def lcm(a: int, b: int) -> int:
    return abs(a // math.gcd(a, b) * b)


def pair_data(v: tuple[int, ...], i: int, j: int):
    q = len(v) + 1
    W = 1
    for x in v:
        W = lcm(W, x)
    M = q * W
    vi, vj = v[i], v[j]
    h = math.gcd(vi, vj)
    n = M // math.gcd(h, M)
    x, y = vi // h, vj // h
    a = math.gcd(x, n)
    n1 = n // a
    r0 = 0 if n1 == 1 else (-y * pow((x // a) % n1, -1, n1)) % n1
    basis = ((n1, 0), (r0, a))
    dual_basis = (
        (Fraction(basis[1][1], n), Fraction(-basis[1][0], n)),
        (Fraction(0), Fraction(basis[0][0], n)),
    )
    assert abs(basis[0][0] * basis[1][1]
               - basis[0][1] * basis[1][0]) == n
    return {
        "q": q, "W": W, "M": M, "vi": vi, "vj": vj,
        "basis": basis, "det": n, "dual_basis": dual_basis,
    }


def finite_dual_points(data):
    """Enumerate eta in L* with eta-h in [-alpha,alpha]^2 exactly."""
    q = data["q"]
    lo, hi = Fraction(1, q), Fraction(q - 1, q)
    points = set()
    # L* = Z^2 + Z*(vi/M,vj/M). Modulo Z^2 there are det(L) classes.
    for k in range(data["det"]):
        x = Fraction((k * data["vi"]) % data["M"], data["M"])
        y = Fraction((k * data["vj"]) % data["M"], data["M"])
        if lo <= x <= hi and lo <= y <= hi:
            points.add((x, y))
    return sorted(points)


def triangle_factor(q: int, eta: Fraction) -> Fraction:
    alpha = Fraction(q - 2, 2 * q)
    z = abs(eta - Fraction(1, 2))
    if z > alpha:
        return Fraction(0)
    return (Fraction(1, alpha) *
            (1 - z / alpha))
