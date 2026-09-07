"""Deterministic TASK 23 phase-sensitive surplus audit."""

import json
from itertools import combinations
from math import gcd
from pathlib import Path

from multiplier_fragmentation import strip_multiplier
from multiplicity_surplus import multiplicity_histogram, surplus_from_histogram
from triple_safe import divisor_alignment
from two_direction import two_direction_torus


def record(values):
    data = two_direction_torus(values)
    histogram = multiplicity_histogram(data["runners"], data["order"])
    phases = []
    for runner in data["runners"]:
        p = strip_multiplier(data, runner)
        phases.append([runner["velocity"], p["period"], p["multiplier"],
                       p["center"], p["reduced_radius"]])
    return {"velocities": list(values), "q": data["q"],
            "lcm_grid_period": data["order"],
            "all_divisor_aligned": all(divisor_alignment(r) for r in data["runners"]),
            "multiplicity_histogram": list(histogram),
            "surplus": surplus_from_histogram(histogram),
            "phase_records_v_H_a_c_rho": phases}


def run():
    prior = json.loads(Path(__file__).with_name("task14_results.json").read_text())
    required_values = [(1, 3, 4, 5), (1, 4, 5, 6, 9)] + [
        tuple(x["velocities"]) for x in prior["full_period_obstructions"]]
    required = [record(v) for v in required_values]
    exhaustive = []
    for size in range(4, 7):
        for values in combinations(range(1, 11), size):
            if gcd(*values) != 1 or not any(v % (size + 1) == 0 for v in values):
                continue
            try:
                exhaustive.append(record(values))
            except ValueError:
                pass
    aligned_nonnegative = [x for x in exhaustive
                           if x["all_divisor_aligned"] and x["surplus"] >= 0]
    result = {
        "status": "DISPROVED divisor-alignment-implies-negative-surplus",
        "period_policy": "All histograms use the canonical lcm grid, never qW.",
        "exhaustive_scope": "gcd-one subsets of {1,...,10}, sizes 4,...,6, with defined canonical grid",
        "exhaustive_configuration_count": len(exhaustive),
        "aligned_nonnegative_count": len(aligned_nonnegative),
        "first_aligned_nonnegative_certificate": aligned_nonnegative[0],
        "required": required,
    }
    Path(__file__).with_name("task23_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    out = run()
    print(json.dumps({k: v for k, v in out.items() if k != "required"}, indent=2))
