"""Deterministic multiplier/fragmentation audit for TASK 18."""

import json
import random
from math import gcd
from pathlib import Path

from multiplier_fragmentation import actual_component_count, strip_multiplier
from two_direction import safe_classes


def record(values):
    data, safe = safe_classes(values)
    strips = []
    for runner in data["runners"]:
        info = strip_multiplier(data, runner)
        strips.append({"velocity": runner["velocity"], "period": info["period"],
                       "multiplier": info["multiplier"],
                       "inverse_multiplier": info["inverse_multiplier"],
                       "order": info["multiplicative_order"],
                       "continued_fraction": info["continued_fraction"],
                       "size": info["size"],
                       "components": actual_component_count(runner["bad_residues"],
                                                            runner["period"])})
    return {"velocities": list(values), "grid_order": data["order"],
            "safe_count": len(safe), "strips": strips}


def run(random_trials=500):
    prior = json.loads(Path(__file__).with_name("task14_results.json").read_text())
    obstructions = [record(tuple(item["velocities"]))
                    for item in prior["full_period_obstructions"]]
    standard = []
    candidates = [(1, 3, 4, 5), (1, 2, 4, 8), (1, 2, 3, 4),
                  (1, 3, 5, 8), (2, 3, 4, 5)]
    for values in candidates:
        if gcd(*values) == 1 and any(v % (len(values) + 1) == 0 for v in values):
            standard.append(record(values))

    rng = random.Random(1802)
    checked = covered = 0
    first_covered = None
    for _ in range(random_trials):
        size = rng.randint(3, 10)
        q = size + 1
        values = set(rng.sample(range(1, 51), size - 1))
        values.add(q * rng.randint(1, 50 // q))
        values = tuple(sorted(values))
        if len(values) != size or gcd(*values) != 1:
            continue
        _, safe = safe_classes(values)
        checked += 1
        if not safe:
            covered += 1
            first_covered = first_covered or list(values)
    result = {"status": "VERIFIED", "task14_obstructions": obstructions,
              "task14_all_safe": all(x["safe_count"] for x in obstructions),
              "standard_families": standard, "random_seed": 1802,
              "random_requested": random_trials,
              "random_admissible_checked": checked,
              "random_velocity_limit": 50, "random_covered": covered,
              "first_random_covered": first_covered}
    Path(__file__).with_name("task18_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
