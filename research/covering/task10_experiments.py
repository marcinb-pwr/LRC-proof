"""Deterministic exact audit for TASK 10; computation is not proof."""

import json
from itertools import combinations
from math import comb, gcd
from pathlib import Path

from bad_sets import parameters
from intersections import pair_intersection_closed
from localization import localized_statistics


def record(raw, family):
    raw = tuple(raw)
    velocities, q, w, modulus = parameters(raw)
    loc = localized_statistics(velocities, q, w)
    total = 2 * len(velocities) * w - sum(velocities)
    pairs = sum(pair_intersection_closed(a, b, q, w)
                for a, b in combinations(velocities, 2))
    core_size = modulus - loc["off_core_size"]
    triples = core_size * comb(len(velocities), 3)
    triples += sum((right - left + 1) * comb(mult, 3)
                   for left, right, mult in loc["segments"])
    loc.pop("segments")
    return {"family": family, "velocities": velocities, "q": q, "W": w,
            "M": modulus, "S": total, "P": pairs, "T": triples, **loc}


def normalized(raw):
    g = 0
    for value in raw:
        g = gcd(g, value)
    return g == 1


def run():
    exhaustive = []
    for n in range(2, 8):
        for raw in combinations(range(1, 13), n):
            if normalized(raw):
                exhaustive.append(record(raw, "exhaustive"))

    standards = []
    for n in range(2, 11):
        standards += [
            record(range(1, n + 1), "consecutive"),
            record(range(1, 2 * n, 2), "odd"),
            record((2 ** i for i in range(n)), "powers2"),
            record(range(11, 11 + n), "translated"),
        ]

    divisors = []
    for w in (60, 120, 360, 840):
        ds = [d for d in range(1, w + 1) if w % d == 0]
        # Deterministic sliding divisor families avoid an enormous powerset.
        for n in range(2, min(8, len(ds) + 1)):
            for start in range(len(ds) - n + 1):
                raw = tuple(ds[start:start + n])
                if normalized(raw):
                    divisors.append(record(raw, "divisors"))

    all_records = exhaustive + standards + divisors
    certified = sum(r["localized_pair_certificate"] for r in all_records)
    assert all(not r["covers"] or not r["localized_pair_certificate"]
               for r in all_records)

    # Locate equal unlocalized summaries whose cyclic gap geometry differs.
    seen, collision = {}, None
    for r in all_records:
        key = (r["M"], r["S"], r["P"], r["T"],
               r["off_core_pair_overlap"])
        geometry = (r["longest_safe_run"], r["change_count"],
                    r["min_change_distance"], r["max_change_distance"])
        if key in seen and seen[key][0] != geometry:
            collision = {"statistics": key, "first": seen[key][1],
                         "second": r}
            break
        seen[key] = (geometry, r)

    # Necessary localized pair condition obtained by applying P>=A-|D| on D.
    false_converse = next((r for r in all_records
        if r["off_core_membership"] >= r["off_core_size"] and
           r["off_core_pair_overlap"] >=
           r["off_core_membership"] - r["off_core_size"] and not r["covers"]),
        None)

    result = {
        "status": "VERIFIED",
        "exhaustive_scope": "all gcd-one subsets of {1,...,12}, sizes 2..7",
        "exhaustive_count": len(exhaustive),
        "standard_family_count": len(standards),
        "highly_composite_divisor_family_count": len(divisors),
        "localized_pair_certificates": certified,
        "covers_found": sum(r["covers"] for r in all_records),
        "smallest_false_converse": false_converse,
        "same_global_statistics_different_geometry": collision,
        "standard_families": standards,
    }
    path = Path(__file__).with_name("task10_results.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    summary = run()
    print(json.dumps({k: v for k, v in summary.items()
                      if k != "standard_families"}, indent=2))
