"""Deterministic TASK 24 phase-fiber audit."""

import json
from itertools import combinations
from math import gcd
from pathlib import Path

from localized_certificate import localized_certificate
from multiplier_fragmentation import strip_multiplier
from two_direction import safe_classes, two_direction_torus


def record(values):
    data = two_direction_torus(values)
    result = localized_certificate(data["runners"], data["order"])
    _, safe = safe_classes(values)
    anchor = result["anchor"]
    phase = strip_multiplier(data, data["runners"][anchor])
    return {"velocities": list(values), "q": data["q"],
            "lcm_grid_period": data["order"],
            "anchor_velocity": values[anchor],
            "anchor_phase_v_H_a_c_rho": [values[anchor], phase["period"],
                phase["multiplier"], phase["center"], phase["reduced_radius"]],
            "safe_class_count": len(safe), "certified": result["certified"],
            "fibers": result["fibers"]}


def run():
    prior = json.loads(Path(__file__).with_name("task14_results.json").read_text())
    required_values = [(1, 3, 4, 5), (1, 4, 5, 6, 9),
                       (1, 2, 3, 4, 5, 7)] + [
        tuple(x["velocities"]) for x in prior["full_period_obstructions"]]
    required = [record(v) for v in required_values]
    exhaustive = []
    for size in range(3, 7):
        for values in combinations(range(1, 11), size):
            if gcd(*values) != 1 or not any(v % (size + 1) == 0 for v in values):
                continue
            try:
                exhaustive.append(record(values))
            except ValueError:
                pass
    missed_safe = [x for x in exhaustive
                   if x["safe_class_count"] > 0 and not x["certified"]]
    result = {
        "status": "DISPROVED universal largest-mass transition-fiber quadratic certificate",
        "period_policy": "All fibers use the canonical lcm grid, never qW.",
        "exhaustive_scope": "gcd-one subsets of {1,...,10}, sizes 3,...,6, with defined canonical grid",
        "exhaustive_configuration_count": len(exhaustive),
        "certified_count": sum(x["certified"] for x in exhaustive),
        "missed_safe_count": len(missed_safe),
        "first_missed_safe_certificate": missed_safe[0],
        "required": required,
    }
    Path(__file__).with_name("task24_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    out = run()
    print(json.dumps({k: v for k, v in out.items() if k != "required"}, indent=2))
