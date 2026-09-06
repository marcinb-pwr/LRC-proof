"""Exact finite formula for the complete signed rank-2 sum."""

from __future__ import annotations

from fractions import Fraction

from dual_lattice import finite_dual_points, pair_data, triangle_factor


def axis_line(q: int, b: int) -> Fraction:
    if q % 2 == 0 or b % 2 == 0:
        return Fraction(1)
    return Fraction(1) - Fraction(1, (q - 2) ** 2 * b * b)


def complete_sum(v: tuple[int, ...], i: int, j: int):
    data = pair_data(v, i, j)
    points = finite_dual_points(data)
    total = Fraction(0)
    for x, y in points:
        total += triangle_factor(data["q"], x) * triangle_factor(data["q"], y)
    return total / data["det"], points, data


def exact_support2(v: tuple[int, ...], i: int, j: int):
    total, points, data = complete_sum(v, i, j)
    W, q = data["W"], data["q"]
    axis = axis_line(q, W // v[i]) + axis_line(q, W // v[j]) - 1
    return total - axis, total, points, data
