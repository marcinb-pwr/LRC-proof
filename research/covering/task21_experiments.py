"""Deterministic TASK 21 all-safe-mass and adversarial audit."""

import json
from itertools import combinations
from math import gcd
from pathlib import Path

from triple_safe import divisor_alignment, triple_safe_certificate
from two_direction import two_direction_torus


def audit(values):
    data = two_direction_torus(values)
    records = []
    for ids in combinations(range(len(values)), 3):
        runners = tuple(data["runners"][i] for i in ids)
        result = triple_safe_certificate(runners, data["order"])
        records.append({
            "labels": [values[i] for i in ids],
            "all_safe_mass": result["all_safe_mass"],
            "union_bound": result["union_bound"],
            "pair_corrected_bound": result["pair_corrected_bound"],
            "all_divisor_aligned": all(divisor_alignment(r) for r in runners),
        })
    return {"velocities": list(values), "q": data["q"],
            "lcm_grid_period": data["order"], "triple_count": len(records),
            "minimum_all_safe_mass": min(r["all_safe_mass"] for r in records),
            "minimum_union_bound": min(r["union_bound"] for r in records),
            "minimum_pair_corrected_bound": min(r["pair_corrected_bound"] for r in records),
            "zero_all_safe_triples": [r for r in records if r["all_safe_mass"] == 0],
            "triples": records}


def run():
    prior = json.loads(Path(__file__).with_name("task14_results.json").read_text())
    required = [(1, 3, 4, 5)] + [tuple(x["velocities"])
                                  for x in prior["full_period_obstructions"]]
    required_records = [audit(values) for values in required]

    # Exhaustive normalized adversarial search in a compact but completely
    # specified range.  Only inputs for which the canonical construction is
    # defined are retained.
    exhaustive = []
    for size in range(3, 7):
        for values in combinations(range(1, 11), size):
            if gcd(*values) != 1 or not any(v % (size + 1) == 0 for v in values):
                continue
            try:
                exhaustive.append(audit(values))
            except ValueError:
                pass
    all_records = required_records + exhaustive
    zero = [(record["velocities"], triple)
            for record in all_records for triple in record["zero_all_safe_triples"]]
    result = {
        "status": "VERIFIED",
        "period_policy": "Every scan and mass is on q*lcm(v_star,v_dagger), never qW.",
        "required_configuration_count": len(required_records),
        "exhaustive_scope": "gcd-one subsets of {1,...,10}, sizes 3,...,6, with a q-divisible velocity and defined canonical second direction",
        "exhaustive_configuration_count": len(exhaustive),
        "zero_all_safe_triple_count": len(zero),
        "zero_all_safe_certificates": zero,
        "minimum_normalized_all_safe_mass": min(
            (r["minimum_all_safe_mass"] / r["lcm_grid_period"] for r in all_records)),
        "required": required_records,
    }
    Path(__file__).with_name("task21_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    summary = run()
    print(json.dumps({k: v for k, v in summary.items() if k != "required"}, indent=2))
