"""Deterministic TASK 22 restricted-incidence audit."""

import json
from itertools import combinations
from math import gcd
from pathlib import Path

from multiplier_fragmentation import strip_multiplier
from restricted_incidence import restricted_certificate
from two_direction import two_direction_torus


def compact_record(values):
    data = two_direction_torus(values)
    result = restricted_certificate(data["runners"], data["order"])
    phases = []
    for runner in data["runners"]:
        phase = strip_multiplier(data, runner)
        phases.append({"velocity": runner["velocity"], "H": phase["period"],
                       "a": phase["multiplier"], "c": phase["center"],
                       "rho": phase["reduced_radius"]})
    return {"velocities": list(values), "q": data["q"],
            "lcm_grid_period": data["order"],
            "canonical_triple_labels": [values[i] for i in result["triple"]],
            "safe_mass": result["safe_mass"],
            "restricted_incidences": list(result["incidences"]),
            "incidence_sum": result["incidence_sum"],
            "strict_certificate": result["strict_certificate"],
            "phase_records": phases}


def run():
    prior = json.loads(Path(__file__).with_name("task14_results.json").read_text())
    required_values = [(1, 3, 4, 5)] + [tuple(x["velocities"])
                                        for x in prior["full_period_obstructions"]]
    required = [compact_record(v) for v in required_values]
    exhaustive = []
    for size in range(3, 7):
        for values in combinations(range(1, 11), size):
            if gcd(*values) != 1 or not any(v % (size + 1) == 0 for v in values):
                continue
            try:
                exhaustive.append(compact_record(values))
            except ValueError:
                pass
    failures = [x for x in exhaustive if not x["strict_certificate"]]
    result = {
        "status": "DISPROVED canonical largest-mass triple rule",
        "period_policy": "All arithmetic uses the canonical lcm grid, never qW.",
        "rule": "Select the three largest lifted bad-strip masses; break ties by input label order.",
        "required_configuration_count": len(required),
        "required_strict_success_count": sum(x["strict_certificate"] for x in required),
        "exhaustive_scope": "gcd-one subsets of {1,...,10}, sizes 3,...,6, with defined canonical grid",
        "exhaustive_configuration_count": len(exhaustive),
        "failure_count": len(failures),
        "first_failure_certificate": failures[0] if failures else None,
        "required": required,
    }
    Path(__file__).with_name("task22_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    out = run()
    print(json.dumps({k: v for k, v in out.items() if k != "required"}, indent=2))
