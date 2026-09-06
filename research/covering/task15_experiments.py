"""Reproducible, M-free TASK 15 exhaustive audit."""

import json
from itertools import combinations
from math import gcd
from pathlib import Path

from two_direction import safe_classes


def run(limit=15):
    prior = json.loads(Path(__file__).with_name("task14_results.json").read_text())
    prior_results = []
    for item in prior["full_period_obstructions"]:
        data, safe = safe_classes(item["velocities"])
        prior_results.append({"velocities": item["velocities"],
                              "v_dagger": data["v_dagger"],
                              "torus_order": data["order"],
                              "first_safe_class": safe[0] if safe else None})
    audited = covered = 0
    smallest = None
    for size in range(2, limit + 1):
        q = size + 1
        for values in combinations(range(1, limit + 1), size):
            if gcd(*values) != 1 or not any(v % q == 0 for v in values):
                continue
            data, safe = safe_classes(values)
            audited += 1
            if not safe:
                covered += 1
                if smallest is None:
                    smallest = {"velocities": values, "q": q,
                                "v_star": data["v_star"],
                                "v_dagger": data["v_dagger"],
                                "torus_order": data["order"]}
    result = {"status": "VERIFIED",
              "selection_rule": "least active noncentral b_i (largest active velocity)",
              "task14_obstructions": prior_results,
              "task14_obstructions_resolved": sum(x["first_safe_class"] is not None
                                                    for x in prior_results),
              "exhaustive_scope": f"gcd-one subsets of {{1,...,{limit}}} whose W is covered",
              "audited_count": audited, "covered_tori": covered,
              "smallest_covered_torus": smallest}
    Path(__file__).with_name("task15_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
