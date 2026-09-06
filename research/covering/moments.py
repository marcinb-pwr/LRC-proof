"""Multiplicity and exact integer moments."""

from math import comb


def multiplicities(bad_sets, modulus):
    return [sum(k in bad for bad in bad_sets) for k in range(modulus)]


def power_moment(values, exponent):
    return sum(value ** exponent for value in values)


def binomial_moment(values, order):
    return sum(comb(value, order) for value in values)


def cover_obstruction(values):
    """Statistics in the proved excess-overlap inequality P >= S-M."""
    modulus = len(values)
    total = sum(values)
    excess = total - modulus
    pairs = binomial_moment(values, 2)
    return {
        "covers": min(values) >= 1,
        "total_membership": total,
        "excess": excess,
        "pair_overlap": pairs,
        "pair_slack": pairs - excess,
    }
