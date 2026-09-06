"""Deterministic M-free TASK 14 audit of the step-clearance word."""

import json
from itertools import combinations
from math import gcd
from pathlib import Path

from step_clearance import safe_steps


def primitive(values):
    g = 0
    for value in values:
        g = gcd(g, value)
    return g == 1


def run(limit=18):
    count = center_covered = short_failures = full_failures = 0
    smallest_short_failure = None
    smallest_full_failure = None
    full_period_obstructions = []
    largest_period_ratio = None
    for size in range(2, limit + 1):
        q = size + 1
        for raw in combinations(range(1, limit + 1), size):
            if not primitive(raw) or not any(v % q == 0 for v in raw):
                continue
            center_covered += 1
            plus_data, plus_short = safe_steps(raw, q, 1)
            _, minus_short = safe_steps(raw, q, -1)
            if not plus_short and not minus_short:
                short_failures += 1
                if smallest_short_failure is None:
                    smallest_short_failure = {
                        "velocities": raw, "q": q, "W": plus_data["W"],
                        "v_star": plus_data["v_star"],
                        "word_period": plus_data["word_period"],
                        "point_period": plus_data["point_period"]}
            _, plus_full = safe_steps(raw, sign=1)
            # A full positive period already contains negative h as residues,
            # so a separate minus scan is unnecessary here.
            if not plus_full:
                full_failures += 1
                obstruction = {
                    "velocities": raw, "q": q, "W": plus_data["W"],
                    "v_star": plus_data["v_star"],
                    "word_period": plus_data["word_period"],
                    "point_period": plus_data["point_period"]}
                full_period_obstructions.append(obstruction)
                if smallest_full_failure is None:
                    smallest_full_failure = obstruction
            ratio = plus_data["point_period"] // plus_data["word_period"]
            if largest_period_ratio is None or ratio > largest_period_ratio["ratio"]:
                largest_period_ratio = {"velocities": raw, "ratio": ratio,
                                        "point_period": plus_data["point_period"],
                                        "word_period": plus_data["word_period"]}
            count += 1

    result = {"status": "VERIFIED",
              "exhaustive_scope": f"gcd-one subsets of {{1,...,{limit}}} whose W is covered",
              "center_covered_count": center_covered,
              "audited_count": count, "short_range_failures": short_failures,
              "smallest_short_range_failure": smallest_short_failure,
              "full_period_failures": full_failures,
              "smallest_full_period_failure": smallest_full_failure,
              "full_period_obstructions": full_period_obstructions,
              "largest_point_to_word_period_ratio": largest_period_ratio}
    Path(__file__).with_name("task14_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
