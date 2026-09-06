"""Deterministic exact TASK 11 audit; finite computation is not proof."""

import json
from itertools import combinations
from math import gcd
from pathlib import Path

from endpoint_words import word_statistics


def primitive(values):
    g = 0
    for value in values:
        g = gcd(g, value)
    return g == 1


def compact(raw, family):
    d = word_statistics(raw)
    return {
        "family": family, "velocities": d["velocities"], "N": len(d["velocities"]),
        "M": d["M"], "beta": d["beta"], "event_count": len(d["word"]),
        "zero_segment_count": d["zero_segment_count"],
        "zero_segments": d["zero_segments"],
        "delta_histogram": d["delta_histogram"], "gap_multiset": d["gap_multiset"],
        "strictly_alternating": d["strictly_alternating"],
        "unit_changes": d["unit_changes"],
        "minimum_gap_at_least_beta": d["minimum_gap_at_least_beta"],
    }


def run():
    records = []
    for size in range(2, 17):
        for raw in combinations(range(1, 17), size):
            if primitive(raw):
                records.append(compact(raw, "exhaustive"))
    exhaustive_count = len(records)

    standards = []
    for n in range(2, 13):
        standards.extend((compact(range(1, n + 1), "consecutive"),
                          compact(range(1, 2 * n, 2), "odd"),
                          compact((2 ** i for i in range(n)), "powers2"),
                          compact(range(17, 17 + n), "translated")))
    records.extend(standards)
    for w in (60, 120, 360, 840, 2520):
        divisors = [d for d in range(1, w + 1) if w % d == 0]
        for n in range(2, min(9, len(divisors) + 1)):
            for start in range(len(divisors) - n + 1):
                raw = divisors[start:start + n]
                if primitive(raw):
                    records.append(compact(raw, "divisors"))

    conjectures = ("strictly_alternating", "unit_changes",
                   "minimum_gap_at_least_beta")
    counterexamples = {name: next((r for r in records if not r[name]), None)
                       for name in conjectures}

    # Deliberately unordered finite summary: even all event gaps and net-change
    # multiplicities forgets their association/order.  Hold basic parameters too.
    seen, collision = {}, None
    coarse_seen, coarse_collision = {}, None
    for r in records:
        coarse_key = (r["N"], r["M"], r["beta"], r["event_count"],
                      tuple(map(tuple, r["delta_histogram"])))
        if (coarse_collision is None and coarse_key in coarse_seen and
                coarse_seen[coarse_key]["zero_segment_count"] !=
                r["zero_segment_count"]):
            coarse_collision = {"summary": coarse_key,
                                "first": coarse_seen[coarse_key], "second": r}
        coarse_seen.setdefault(coarse_key, r)
        key = (r["N"], r["M"], r["beta"], r["event_count"],
               tuple(map(tuple, r["delta_histogram"])), tuple(r["gap_multiset"]))
        behavior = r["zero_segment_count"]
        if key in seen and seen[key]["zero_segment_count"] != behavior:
            collision = {"summary": key, "first": seen[key], "second": r}
            break
        seen.setdefault(key, r)

    result = {
        "status": "VERIFIED",
        "exhaustive_scope": "all gcd-one subsets of {1,...,16}, sizes 2..16",
        "exhaustive_count": exhaustive_count,
        "total_count": len(records),
        "covers_found": sum(r["zero_segment_count"] == 0 for r in records),
        "smallest_counterexamples": counterexamples,
        "coarse_unordered_summary_collision": coarse_collision,
        "unordered_summary_collision": collision,
        "standard_families": standards,
    }
    Path(__file__).with_name("task11_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    result = run()
    print(json.dumps({k: v for k, v in result.items()
                      if k != "standard_families"}, indent=2))
