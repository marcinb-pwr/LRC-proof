"""Quantitative all-safe bounds for three canonical-grid strips (TASK 21)."""

from itertools import combinations
from math import gcd, lcm


def lifted_size(runner, common_order):
    """Cardinality of one bad strip after lifting to the common cyclic grid."""
    if common_order % runner["period"]:
        raise ValueError("runner period must divide the common order")
    return len(runner["bad_residues"]) * (common_order // runner["period"])


def intersection_size(runners, common_order):
    """Exact generalized-CRT intersection cardinality (no common-order scan)."""
    if not runners:
        return common_order
    joint_period = lcm(*(runner["period"] for runner in runners))
    if common_order % joint_period:
        raise ValueError("runner periods must divide the common order")
    # Scan only the true lcm quotient.  This is often much smaller than the
    # Cartesian product and, crucially, is never the ambient qW modulus.
    bad = tuple(frozenset(runner["bad_residues"]) for runner in runners)
    compatible = sum(all(z % runner["period"] in residues
                         for runner, residues in zip(runners, bad))
                     for z in range(joint_period))
    return compatible * (common_order // joint_period)


def triple_safe_certificate(runners, common_order):
    """Exact triple-safe mass and two quantitative lower bounds.

    ``union_bound`` uses only the three one-strip cardinalities.  The
    ``pair_corrected_bound`` is the second Bonferroni lower bound for the
    complement and uses pair CRT intersections, but not the triple cell.
    """
    if len(runners) != 3:
        raise ValueError("exactly three runners are required")
    singles = tuple(lifted_size(runner, common_order) for runner in runners)
    pairs = tuple(intersection_size((runners[i], runners[j]), common_order)
                  for i, j in combinations(range(3), 2))
    triple = intersection_size(runners, common_order)
    exact = common_order - sum(singles) + sum(pairs) - triple
    return {
        "single_bad_masses": singles,
        "pair_bad_intersections": pairs,
        "triple_bad_intersection": triple,
        "all_safe_mass": exact,
        "union_bound": max(0, common_order - sum(singles)),
        # Since |A1 union A2 union A3| <= sum |Ai|-sum |AiAj|+min |AiAj|.
        "pair_corrected_bound": max(
            0, common_order - sum(singles) + sum(pairs) - min(pairs)),
    }


def divisor_alignment(runner):
    """Test g_i | b_i from Theorem 38 using stored period data."""
    g_i = runner["modulus"] // runner["period"]
    return runner["b"] % g_i == 0


def aligned_density_numerator(runner):
    """Return q|A_i|-2H_i, negative under divisor alignment and nonemptiness."""
    q = runner["modulus"] // runner["b"]
    return q * len(runner["bad_residues"]) - 2 * runner["period"]
