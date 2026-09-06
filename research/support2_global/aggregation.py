"""Convenience identity checks for exact support-2 aggregation."""

from __future__ import annotations

from fractions import Fraction

from exact_counts import aggregate


def check(v):
    result = aggregate(v)
    if not result["enumerated"]:
        return result
    assert result["enumerated"]
    f_axis = Fraction(result["F_axis"])
    f2 = Fraction(result["F2"])
    f_le2 = Fraction(result["F_le2"])
    assert f_le2 == f_axis + f2
    return result
