"""Exact finite full-dimensional dual certificate."""

from __future__ import annotations

from fractions import Fraction

from full_lattice import dual_class_points, setup


def h(q: int, delta: Fraction, z: Fraction) -> Fraction:
    alpha = Fraction(1, 2) - delta
    value = (1 / alpha) * (1 - abs(z - Fraction(1, 2)) / alpha)
    return max(Fraction(0), value)


def finite_certificate(
    v: tuple[int, ...],
    delta: Fraction | None = None,
    state_cap: int = 100_000,
):
    q, W, M, d, det = setup(v)
    if delta is None:
        delta = Fraction(1, q)
    if det > state_cap:
        return {
            "q": q, "W": W, "M": M, "gcd": d, "det": det,
            "delta": str(delta), "enumerated": False,
        }
    points = dual_class_points(v, delta)
    total = Fraction(0)
    for _, coords in points:
        weight = Fraction(1)
        for z in coords:
            weight *= h(q, delta, z)
        total += weight
    return {
        "q": q,
        "W": W,
        "M": M,
        "gcd": d,
        "det": det,
        "delta": str(delta),
        "points": [(k, [str(x) for x in coords])
                   for k, coords in points],
        "point_count": len(points),
        "certificate": str(total / det),
        "positive": total > 0,
        "enumerated": True,
    }
