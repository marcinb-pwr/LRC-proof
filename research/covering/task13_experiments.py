"""Deterministic M-free audit of the TASK 13 central fringe theorem."""

import json
from itertools import combinations
from math import gcd
from pathlib import Path

from central_fringe import boundary_profile


def primitive(values):
    g = 0
    for value in values:
        g = gcd(g, value)
    return g == 1


def run(limit=18):
    count = eligible = rule_failures = 0
    first_both_fringes = None
    first_mixed_but_other_safe = None
    for size in range(2, limit + 1):
        q = size + 1
        for raw in combinations(range(1, limit + 1), size):
            if not primitive(raw):
                continue
            count += 1
            profile = boundary_profile(raw)
            central = profile["central"]
            if (len(central) != 1 or profile["v_star"] != max(profile["velocities"])):
                continue
            eligible += 1
            plus_bad = tuple(e["velocity"] for e in profile["plus"] if not e["safe"])
            minus_bad = tuple(e["velocity"] for e in profile["minus"] if not e["safe"])
            expected_plus = tuple(v for v in profile["velocities"] if v % q == q - 1)
            expected_minus = tuple(v for v in profile["velocities"] if v % q == 1)
            if plus_bad != expected_plus or minus_bad != expected_minus:
                rule_failures += 1
            residues = {v % q for v in profile["velocities"]}
            if 1 in residues and q - 1 in residues and first_both_fringes is None:
                first_both_fringes = {"velocities": profile["velocities"], "q": q,
                    "W": profile["W"], "minus_bad": minus_bad, "plus_bad": plus_bad}

            # Check whether mixed fringes nevertheless have a safe h-boundary
            # for 1 <= h < q; this tests the most immediate extension.
            if 1 in residues and q - 1 in residues and first_mixed_but_other_safe is None:
                safe_steps = []
                for h in range(1, q):
                    hp = boundary_profile(raw, h)
                    if all(e["safe"] for e in hp["plus"]):
                        safe_steps.append(h)
                    if all(e["safe"] for e in hp["minus"]):
                        safe_steps.append(-h)
                if safe_steps:
                    first_mixed_but_other_safe = {
                        "velocities": profile["velocities"], "q": q,
                        "W": profile["W"], "safe_steps": tuple(safe_steps)}

    result = {"status": "VERIFIED",
              "exhaustive_scope": f"all gcd-one subsets of {{1,...,{limit}}}, sizes 2..{limit}",
              "exhaustive_count": count, "eligible_unique_max_central": eligible,
              "fringe_rule_failures": rule_failures,
              "smallest_both_fringe_populations": first_both_fringes,
              "smallest_mixed_fringe_with_other_safe_boundary": first_mixed_but_other_safe}
    Path(__file__).with_name("task13_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
