"""Restricted bad-strip incidences on a triple-safe set (TASK 22)."""

from itertools import combinations

from triple_safe import intersection_size, lifted_size, triple_safe_certificate


def canonical_mass_triple(runners, common_order):
    """Choose the three largest bad masses, with label order as the tie-break."""
    if len(runners) < 3:
        raise ValueError("at least three runners are required")
    ranked = sorted(range(len(runners)),
                    key=lambda i: (-lifted_size(runners[i], common_order), i))
    return tuple(sorted(ranked[:3]))


def restricted_single_incidence(runners, triple, outside, common_order):
    """Compute |A_outside intersect S_triple| by four-set CRT inclusion-exclusion."""
    selected = tuple(runners[i] for i in triple)
    outer = runners[outside]
    total = lifted_size(outer, common_order)
    for degree in range(1, 4):
        sign = -1 if degree % 2 else 1
        total += sign * sum(
            intersection_size((outer,) + tuple(selected[j] for j in ids),
                              common_order)
            for ids in combinations(range(3), degree))
    return total


def restricted_certificate(runners, common_order, triple=None):
    """Return exact restricted incidences and the strict first-moment test."""
    if triple is None:
        triple = canonical_mass_triple(runners, common_order)
    triple = tuple(triple)
    if len(triple) != 3 or len(set(triple)) != 3:
        raise ValueError("triple must contain three distinct indices")
    safe_mass = triple_safe_certificate(
        tuple(runners[i] for i in triple), common_order)["all_safe_mass"]
    outside = tuple(i for i in range(len(runners)) if i not in triple)
    incidences = tuple(restricted_single_incidence(
        runners, triple, i, common_order) for i in outside)
    return {"triple": triple, "outside": outside, "safe_mass": safe_mass,
            "incidences": incidences, "incidence_sum": sum(incidences),
            "strict_certificate": sum(incidences) < safe_mass}


def pointwise_averaging_totals(runners, common_order):
    """Directly evaluate the two sides of the exact all-triples identity."""
    bad = tuple(frozenset(r["bad_residues"]) for r in runners)
    safe_triple_total = 0
    restricted_total = 0
    for z in range(common_order):
        multiplicity = sum(z % r["period"] in values
                           for r, values in zip(runners, bad))
        safe_labels = len(runners) - multiplicity
        count = 0 if safe_labels < 3 else (
            safe_labels * (safe_labels - 1) * (safe_labels - 2) // 6)
        safe_triple_total += count
        restricted_total += multiplicity * count
    return safe_triple_total, restricted_total
