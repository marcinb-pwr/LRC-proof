"""Exact pointwise polynomial certificates on integer multiplicities."""

from fractions import Fraction
from math import comb


def binomial_certificate_values(maximum):
    """Values of C(m,2)-(m-1), the sharp degree-two cover certificate."""
    return [Fraction(comb(m, 2) - (m - 1)) for m in range(1, maximum + 1)]


def verify_degree_two_certificate(maximum):
    return all(value >= 0 for value in binomial_certificate_values(maximum))
