"""Reproducible small experiment suite; output is evidence, not proof."""

import json
import random
from pathlib import Path

from bad_sets import bad_set, bad_set_by_period, exact_size, parameters
from intersections import all_pair_intersections
from moments import cover_obstruction, multiplicities, power_moment
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
        assert sum(pair_counts.values()) == sum(m * (m - 1) // 2 for m in values)
        stats = cover_obstruction(values)
        records.append({
            "family": family, "velocities": velocities, "q": q,
            "W": w, "M": modulus, **stats,
            "moments": {str(r): power_moment(values, r) for r in range(1, 5)},
        })
    assert verify_degree_two_certificate(20)
    summary = {
        "claim_status": "VERIFIED (finite test suite only)",
        "configurations": len(records),
        "covers_found": sum(record["covers"] for record in records),
        "minimum_multiplicity_seen": min(
            0 if not record["covers"] else 1 for record in records),
        "records": records,
    }
    Path(__file__).with_name("results.json").write_text(
        json.dumps(summary, indent=2) + "\n")


if __name__ == "__main__":
    run()
