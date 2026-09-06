"""Statement-level checks for the full character-shifted Poisson formula."""

from __future__ import annotations

from fractions import Fraction


def alpha(q: int) -> Fraction:
    return Fraction(q - 2, 2 * q)


def shifted_support(q: int):
    a = alpha(q)
    return Fraction(1, 2) - a, Fraction(1, 2) + a


def character(a: tuple[int, ...]) -> int:
    return (-1) ** sum(a)


def formula_summary(q: int):
    lo, hi = shifted_support(q)
    return {
        "alpha": str(alpha(q)),
        "shifted_support": (str(lo), str(hi)),
        "character": "(-1)^sum(a)",
        "fourier_transform": "(1/alpha)*(1-|x|/alpha)_+",
    }
