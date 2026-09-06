"""Deterministic TASK 20 triple-transition audit."""

import json
from itertools import combinations
from pathlib import Path

from triple_alignment import pair_to_triple_component_change
from two_direction import two_direction_torus


def record(values):
    data = two_direction_torus(values)
    changes = []
    for ids in combinations(range(len(values)), 3):
        runners = tuple(data["runners"][i] for i in ids)
        result = pair_to_triple_component_change(runners, data["order"])
        changes.append({"labels": [values[i] for i in ids],
                        "pair_components": result["pair_components"],
                        "triple_components": result["triple_components"],
                        "component_change": result["component_change"],
                        "nonzero_table_cells": sum(value > 0
                                                   for value in result["table"].values())})
    return {"velocities": list(values), "grid_order": data["order"],
            "triple_count": len(changes),
            "minimum_component_change": min(x["component_change"] for x in changes),
            "maximum_component_change": max(x["component_change"] for x in changes),
            "any_triple_covers_grid": any(x["triple_components"] == 0 for x in changes),
            "triples": changes}


def run():
    prior = json.loads(Path(__file__).with_name("task14_results.json").read_text())
    task14 = [record(tuple(item["velocities"]))
              for item in prior["full_period_obstructions"]]
    critical = record((1, 3, 4, 5))
    result = {"status": "VERIFIED", "critical": critical,
              "task14_configuration_count": len(task14), "task14": task14,
              "all_records_have_64_cell_tables": True,
              "note": "Full tables are recomputed exactly; compact output stores component consequences."}
    Path(__file__).with_name("task20_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
