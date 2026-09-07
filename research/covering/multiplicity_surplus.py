"""Exact multiplicity-surplus identities for TASK 23."""

from itertools import combinations
from math import comb

from triple_safe import intersection_size


def surplus_coefficients(number_of_runners):
    """Binomial-basis coefficients of (m-1)*C(N-m,3)."""
    n = number_of_runners
    f = [((m - 1) * comb(n - m, 3) if n - m >= 3 else 0)
         for m in range(5)]
    return (f[0], f[1] - f[0], f[2] - 2*f[1] + f[0],
            f[3] - 3*f[2] + 3*f[1] - f[0],
            f[4] - 4*f[3] + 6*f[2] - 4*f[1] + f[0])


def intersection_moments(runners, common_order, maximum_order=4):
    """Return sum of all k-fold bad intersections for 0 <= k <= maximum_order."""
    moments = [common_order]
    for degree in range(1, min(maximum_order, len(runners)) + 1):
        moments.append(sum(intersection_size(tuple(runners[i] for i in ids),
                                             common_order)
                           for ids in combinations(range(len(runners)), degree)))
    moments.extend([0] * (maximum_order + 1 - len(moments)))
    return tuple(moments)


def surplus_from_intersections(runners, common_order):
    """Compute Sigma from intersection moments through order four."""
    coefficients = surplus_coefficients(len(runners))
    moments = intersection_moments(runners, common_order)
    return sum(c * moment for c, moment in zip(coefficients, moments))


def multiplicity_histogram(runners, common_order):
    """Compute the exact bad-multiplicity histogram on the lcm grid."""
    histogram = [0] * (len(runners) + 1)
    bad = tuple(frozenset(r["bad_residues"]) for r in runners)
    for z in range(common_order):
        multiplicity = sum(z % r["period"] in values
                           for r, values in zip(runners, bad))
        histogram[multiplicity] += 1
    return tuple(histogram)


def surplus_from_histogram(histogram):
    """Compute Sigma directly from its defining pointwise polynomial."""
    n = len(histogram) - 1
    return sum(count * (m - 1) * comb(n - m, 3)
               for m, count in enumerate(histogram) if n - m >= 3)
