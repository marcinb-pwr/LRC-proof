"""Deterministic TASK 19 shared-transition audit."""

import json
from collections import Counter
from itertools import combinations
from pathlib import Path

from pairwise_alignment import joint_transition_table, pair_safe_component_count
from two_direction import two_direction_torus


def arc_transition_summary(sets, modulus):
    individual, pairs = Counter(), Counter()
    for values in sets:
        for z in range(modulus):
            individual[(int(z in values), int((z + 1) % modulus in values))] += 1
    for left, right in combinations(sets, 2):
        for z in range(modulus):
            s = (int(z in left), int((z + 1) % modulus in left))
            t = (int(z in right), int((z + 1) % modulus in right))
            pairs[(s, t)] += 1
    return {"individual": sorted((str(k), v) for k, v in individual.items()),
            "pairwise": sorted((str(k), v) for k, v in pairs.items())}


def configuration_record(values):
    data = two_direction_torus(values)
    records = []
    for i, j in combinations(range(len(values)), 2):
        table = joint_transition_table(data["runners"][i], data["runners"][j],
                                       data["order"])
        records.append({"labels": [values[i], values[j]],
                        "nonzero_transition_cells": sum(value > 0 for value in table.values()),
                        "safe_components": pair_safe_component_count(
                            data["runners"][i], data["runners"][j], data["order"])})
    return {"velocities": list(values), "grid_order": data["order"], "pairs": records}


def run():
    prior = json.loads(Path(__file__).with_name("task14_results.json").read_text())
    task14 = [configuration_record(tuple(item["velocities"]))
              for item in prior["full_period_obstructions"]]
    uncovered = [{0}, {1}, {5, 6, 7}, {0, 1, 2, 4, 5, 6, 7}]
    covered = [{0}, {3}, {2, 3, 4}, {1, 2, 3, 4, 5, 6, 7}]
    left = arc_transition_summary(uncovered, 8)
    right = arc_transition_summary(covered, 8)
    assert left == right
    result = {"status": "VERIFIED", "critical": configuration_record((1, 3, 4, 5)),
              "task14_configuration_count": len(task14), "task14": task14,
              "matching_aggregate_transition_systems": {
                  "modulus": 8, "summary": left,
                  "uncovered_system": [sorted(x) for x in uncovered],
                  "uncovered_union_size": len(set.union(*uncovered)),
                  "covered_system": [sorted(x) for x in covered],
                  "covered_union_size": len(set.union(*covered))}}
    Path(__file__).with_name("task19_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
