"""Exact, deterministic TASK 12 labelled-pair audit."""

import json
from itertools import combinations
from math import gcd
from pathlib import Path

from labelled_pairs import center_data


def primitive(values):
    g = 0
    for value in values:
        g = gcd(g, value)
    return g == 1


def summary(raw, family):
    data = center_data(raw)
    covering = tuple(item["velocity"] for item in data["center_covering"])
    zero_count = sum(item["next_x"] is not None and
                     item["next_x"] > item["x"] and item["prefix"] == 0
                     for item in data["word"])
    return {"family": family, "velocities": data["velocities"],
            "q": data["q"], "W": data["W"], "M": data["M"],
            "center_covering": covering,
            "innermost_boundary_candidates": data["innermost_boundary_candidates"],
            "innermost_boundary_safe": data["innermost_boundary_safe"],
            "zero_segment_count": zero_count,
            "labelled_event_count": len(data["events"])}


def run(limit=16):
    count = covers = center_covered = 0
    first_boundary_failure = None
    first_both_boundary_failure = None
    first_multiple_coverers = None
    for size in range(2, limit + 1):
        for raw in combinations(range(1, limit + 1), size):
            if not primitive(raw):
                continue
            record = summary(raw, "exhaustive")
            count += 1
            covers += record["zero_segment_count"] == 0
            if record["center_covering"]:
                center_covered += 1
                safe = record["innermost_boundary_safe"]
                if first_boundary_failure is None and not all(safe):
                    first_boundary_failure = record
                if first_both_boundary_failure is None and not any(safe):
                    first_both_boundary_failure = record
                if first_multiple_coverers is None and len(record["center_covering"]) > 1:
                    first_multiple_coverers = record

    families = []
    for n in range(2, 13):
        q = n + 1
        families.extend((summary(range(1, n + 1), "consecutive"),
                         summary(range(1, 2 * n, 2), "odd"),
                         summary((2 ** i for i in range(n)), "powers2"),
                         summary(tuple(range(1, n)) + (q * (n + 2),),
                                 "new_theorem_family")))
    for w in (60, 120, 360, 840, 2520):
        divisors = [d for d in range(1, w + 1) if w % d == 0]
        for n in range(2, min(9, len(divisors) + 1)):
            for start in range(len(divisors) - n + 1):
                raw = tuple(divisors[start:start + n])
                if primitive(raw):
                    families.append(summary(raw, "divisors"))

    theorem_failures = [record for record in families
                        if record["family"] == "new_theorem_family" and
                        record["zero_segment_count"] == 0]
    result = {"status": "VERIFIED",
              "exhaustive_scope": f"all gcd-one subsets of {{1,...,{limit}}}, sizes 2..{limit}",
              "exhaustive_count": count, "center_covered_count": center_covered,
              "covers_found": covers,
              "smallest_one_sided_boundary_failure": first_boundary_failure,
              "smallest_two_sided_boundary_failure": first_both_boundary_failure,
              "smallest_multiple_center_coverers": first_multiple_coverers,
              "additional_family_count": len(families),
              "new_theorem_family_failures": theorem_failures}
    Path(__file__).with_name("task12_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
