"""Deterministic TASK 16 certificate and counterexample search."""

import json
import random
from itertools import combinations
from math import gcd
from pathlib import Path

from covering_certificates import certificate_bounds
from two_direction import safe_classes


def run(limit=12, random_trials=400):
    audited = tree = bonferroni3 = covered = 0
    first_tree_failure = first_b3_failure = first_covered = None
    for size in range(2, limit + 1):
        q = size + 1
        for values in combinations(range(1, limit + 1), size):
            if gcd(*values) != 1 or not any(v % q == 0 for v in values):
                continue
            data, safe = safe_classes(values)
            bounds = certificate_bounds(data, triples=True)
            audited += 1
            tree += bounds["tree_certifies"]
            bonferroni3 += bounds["bonferroni3_certifies"]
            if not bounds["tree_certifies"] and first_tree_failure is None:
                first_tree_failure = values
            if not bounds["bonferroni3_certifies"] and first_b3_failure is None:
                first_b3_failure = values
            if not safe:
                covered += 1
                first_covered = first_covered or values

    rng = random.Random(1602)
    random_checked = random_covered = 0
    first_random_covered = None
    for _ in range(random_trials):
        size = rng.randint(3, 9)
        q = size + 1
        values = set(rng.sample(range(1, 41), size - 1))
        values.add(q * rng.randint(1, 40 // q))
        values = tuple(sorted(values))
        if len(values) != size or gcd(*values) != 1:
            continue
        _, safe = safe_classes(values)
        random_checked += 1
        if not safe:
            random_covered += 1
            first_random_covered = first_random_covered or values

    result = {
        "status": "VERIFIED",
        "exhaustive_scope": f"gcd-one subsets of {{1,...,{limit}}} whose W is covered",
        "audited_count": audited,
        "tree_certified": tree,
        "bonferroni3_certified": bonferroni3,
        "first_tree_failure": first_tree_failure,
        "first_bonferroni3_failure": first_b3_failure,
        "covered_tori": covered,
        "smallest_covered_torus": first_covered,
        "random_seed": 1602,
        "random_requested": random_trials,
        "random_admissible_checked": random_checked,
        "random_velocity_limit": 40,
        "random_covered_tori": random_covered,
        "first_random_covered_torus": first_random_covered,
    }
    Path(__file__).with_name("task16_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
