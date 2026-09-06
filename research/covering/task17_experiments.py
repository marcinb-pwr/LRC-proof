"""Reproducible TASK 17 component and low-moment obstruction audit."""

import json
from pathlib import Path

from interval_components import component_certificate
from two_direction import safe_classes


def moments(sets):
    from itertools import combinations
    return [sum(len(set.intersection(*choice))
                for choice in combinations(sets, degree))
            for degree in (1, 2, 3)]


def run():
    prior = json.loads(Path(__file__).with_name("task14_results.json").read_text())
    records = []
    for item in prior["full_period_obstructions"]:
        data, safe = safe_classes(item["velocities"])
        components = component_certificate(data)
        records.append({"velocities": item["velocities"],
                        "safe_count": len(safe),
                        "final_component_count": len(components)})

    # Two systems of genuine centered arcs on Z/8Z.  They have identical
    # first three intersection sums but different coverage.
    circle = set(range(8))
    covered = [{0}, {0, 1, 2, 3, 5, 6, 7}, {5, 6, 7}, {0, 4, 5, 6, 7}]
    uncovered = [{0}, {0, 1, 2}, {0, 4, 5, 6, 7},
                 {0, 1, 2, 4, 5, 6, 7}]
    result = {
        "status": "VERIFIED",
        "task14_records": records,
        "task14_all_resolved_by_components": all(r["safe_count"] > 0 for r in records),
        "critical_configuration": {"velocities": [1, 3, 4, 5],
                                   "safe_classes": [24, 25, 35, 36]},
        "matching_moment_arc_systems": {
            "modulus": 8, "moments": moments(covered),
            "covered_union_size": len(set.union(*covered)),
            "uncovered_union_size": len(set.union(*uncovered)),
            "covered_system": [sorted(x) for x in covered],
            "uncovered_system": [sorted(x) for x in uncovered]},
    }
    assert moments(covered) == moments(uncovered) == [16, 12, 4]
    assert set.union(*covered) == circle and set.union(*uncovered) != circle
    Path(__file__).with_name("task17_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
