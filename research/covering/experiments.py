"""Reproducible small experiment suite; output is evidence, not proof."""

import json
import random
from itertools import combinations
from pathlib import Path

from bad_sets import bad_set, bad_set_by_period, exact_size, parameters
from intersections import (all_pair_intersections, pair_intersection_closed,
                           pair_intersection_size)
from moments import (cover_obstruction, forced_core, multiplicities,
                     power_moment)
from optimization import verify_degree_two_certificate


def families():
    out = []
    for n in range(2, 8):
        out.extend([
            ("consecutive", tuple(range(1, n + 1))),
            ("odd", tuple(range(1, 2 * n, 2))),
            ("powers2", tuple(2 ** i for i in range(n))),
            ("translated", tuple(range(5, 5 + n))),
        ])
    rng = random.Random(20260906)
    # Keep M small enough that the deliberately transparent set construction
    # remains a fast regression test.  Larger searches belong in TASK 9's
    # optimized bitset implementation.
    for n in range(2, 8):
        for _ in range(8):
            out.append(("random", tuple(sorted(rng.sample(range(1, 13), n)))))
    return out


def run():
    records = []
    for family, raw in families():
        velocities, q, w, modulus = parameters(raw)
        sets = [bad_set(v, q, w) for v in velocities]
        assert all(sets[i] == bad_set_by_period(v, q, w)
                   for i, v in enumerate(velocities))
        assert all(len(sets[i]) == exact_size(v, w)
                   for i, v in enumerate(velocities))
        values = multiplicities(sets, modulus)
        pair_counts = all_pair_intersections(velocities, q, w)
        assert all(pair_intersection_closed(velocities[i], velocities[j], q, w)
                   == pair_intersection_size(velocities[i], velocities[j], q, w)
                   for i, j in combinations(range(len(velocities)), 2))
        assert sum(pair_counts.values()) == sum(m * (m - 1) // 2 for m in values)
        stats = cover_obstruction(values)
        core = forced_core([w // v for v in velocities], modulus)
        assert all(core <= bad for bad in sets)
        off_pair = sum(sum(k in sets[i] and k in sets[j] and k not in core
                           for k in range(modulus))
                       for i, j in combinations(range(len(velocities)), 2))
        records.append({
            "family": family, "velocities": velocities, "q": q,
            "W": w, "M": modulus, **stats,
            "moments": {str(r): power_moment(values, r) for r in range(1, 5)},
            "forced_core_size": len(core), "off_core_pair_overlap": off_pair,
        })

    # Exhaust all normalized subsets of [1,10].  A modulus cap makes this a
    # deterministic regression search rather than an accidental stress test.
    exhaustive = []
    for n in range(2, 7):
        for raw in combinations(range(1, 11), n):
            velocities, q, w, modulus = parameters(raw)
            if velocities != raw or modulus > 200_000:
                continue
            pair = sum(all_pair_intersections(velocities, q, w).values())
            delta = (n - 1) * w - sum(velocities)
            if delta >= 0 and pair >= delta:
                covers = all(any(min((k * v) % modulus,
                                     (-k * v) % modulus) * q < modulus
                                 for v in velocities)
                             for k in range(modulus))
                exhaustive.append({"velocities": velocities, "P": pair,
                                   "Delta": delta, "slack": pair - delta,
                                   "covers": covers})
    assert verify_degree_two_certificate(20)
    summary = {
        "claim_status": "VERIFIED (finite test suite only)",
        "configurations": len(records),
        "covers_found": sum(record["covers"] for record in records),
        "minimum_multiplicity_seen": min(
            0 if not record["covers"] else 1 for record in records),
        "records": records,
        "exhaustive_normalized_subsets": sum(
            1 for n in range(2, 7) for raw in combinations(range(1, 11), n)
            if parameters(raw)[0] == raw and parameters(raw)[3] <= 200_000),
        "P_ge_Delta_count": len(exhaustive),
        "covers_among_P_ge_Delta": sum(x["covers"] for x in exhaustive),
        "smallest_P_ge_Delta": exhaustive[0] if exhaustive else None,
        "maximum_P_minus_Delta": max(exhaustive, key=lambda x: x["slack"])
        if exhaustive else None,
    }
    Path(__file__).with_name("results.json").write_text(
        json.dumps(summary, indent=2) + "\n")


if __name__ == "__main__":
    run()
