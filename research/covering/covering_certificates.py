"""Exact labelled union certificates for cyclic modular strips."""

from collections import Counter
from itertools import combinations
from math import gcd, lcm


def intersection_count(runners, common_order):
    """Count a lifted intersection by generalized CRT, for any label tuple."""
    if not runners:
        return common_order
    modulus = 1
    classes = {0}
    for runner in runners:
        h = runner["period"]
        new_modulus = lcm(modulus, h)
        merged = set()
        # The periods in this project divide common_order.  Enumerating the
        # current lcm is independent of M=qW and avoids a product of arc sizes.
        bad = frozenset(runner["bad_residues"])
        for z in range(new_modulus):
            if z % modulus in classes and z % h in bad:
                merged.add(z)
        classes, modulus = merged, new_modulus
        if not classes:
            return 0
    return len(classes) * (common_order // modulus)


def pair_intersection_fast(left, right, common_order):
    """Formula (38), evaluated through gcd-residue histograms."""
    hi, hj = left["period"], right["period"]
    g = gcd(hi, hj)
    ca = Counter(a % g for a in left["bad_residues"])
    cb = Counter(b % g for b in right["bad_residues"])
    compatible = sum(count * cb.get(residue, 0)
                     for residue, count in ca.items())
    return compatible * (common_order // lcm(hi, hj))


def maximum_spanning_tree_weight(weights, vertex_count):
    """Kruskal's exact maximum spanning-tree value."""
    parent = list(range(vertex_count))

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    total = used = 0
    for weight, i, j in sorted(weights, reverse=True):
        ri, rj = root(i), root(j)
        if ri != rj:
            parent[ri] = rj
            total += weight
            used += 1
            if used == vertex_count - 1:
                break
    return total


def certificate_bounds(data, triples=False):
    """Return the optimal tree upper bound and optional Bonferroni-3 bound."""
    runners, order = data["runners"], data["order"]
    sizes = [len(r["bad_residues"]) * (order // r["period"])
             for r in runners]
    edges = [(pair_intersection_fast(runners[i], runners[j], order), i, j)
             for i, j in combinations(range(len(runners)), 2)]
    tree = sum(sizes) - maximum_spanning_tree_weight(edges, len(runners))
    result = {"first_moment": sum(sizes), "tree_upper_bound": tree,
              "tree_certifies": tree < order}
    if triples:
        pair_sum = sum(weight for weight, _, _ in edges)
        triple_sum = sum(intersection_count(tuple(runners[i] for i in ids), order)
                         for ids in combinations(range(len(runners)), 3))
        bonferroni3 = sum(sizes) - pair_sum + triple_sum
        result.update({"pair_sum": pair_sum, "triple_sum": triple_sum,
                       "bonferroni3_upper_bound": bonferroni3,
                       "bonferroni3_certifies": bonferroni3 < order})
    return result
