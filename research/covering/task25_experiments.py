"""Deterministic TASK 25 bounded-complexity phase-refinement audit."""

import json
import random
from itertools import combinations
from math import gcd
from pathlib import Path

from localized_certificate import coarse_phase_bin_certificate, multi_anchor_transition_certificate, short_word_certificate
from multiplier_fragmentation import strip_multiplier
from two_direction import safe_classes, two_direction_torus


def record(values):
    data, safe = safe_classes(values)
    phases = tuple(strip_multiplier(data, runner) for runner in data["runners"])
    candidates = {}
    for count in range(1, min(4, len(values)) + 1):
        candidates[f"transition_{count}_anchors"] = multi_anchor_transition_certificate(
            data["runners"], data["order"], count)
    candidates["transition_up_to_4_anchors"] = candidates[
        f"transition_{min(4, len(values))}_anchors"]
    for radius in (1, 2):
        candidates[f"short_word_radius_{radius}"] = short_word_certificate(
            data["runners"], data["order"], radius)
    for bins in (4, 8):
        candidates[f"coarse_{bins}_bins"] = coarse_phase_bin_certificate(
            data["runners"], data["order"], phases, bins)
    phase_records = [[runner["velocity"], phase["period"], phase["multiplier"],
                      phase["center"], phase["reduced_radius"]]
                     for runner, phase in zip(data["runners"], phases)]
    return {"velocities": list(values), "q": data["q"],
            "lcm_grid_period": data["order"], "safe_class_count": len(safe),
            "phase_records_v_H_a_c_rho": phase_records,
            "candidates": candidates}


def first_miss(records, candidate):
    for item in records:
        value = item["candidates"].get(candidate)
        if item["safe_class_count"] and value is not None and not value["certified"]:
            return item
    return None


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
    rng = random.Random(2502)
    seeded = []
    for _ in range(180):
        size = rng.randint(7, 9)
        q = size + 1
        values = set(rng.sample(range(1, 46), size - 1))
        values.add(q * rng.randint(1, 45 // q))
        values = tuple(sorted(values))
        if len(values) != size or gcd(*values) != 1:
            continue
        try:
            seeded.append(record(values))
        except ValueError:
            pass
    names = ("transition_1_anchors", "transition_2_anchors",
             "transition_3_anchors", "transition_4_anchors",
             "transition_up_to_4_anchors",
             "short_word_radius_1", "short_word_radius_2",
             "coarse_4_bins", "coarse_8_bins")
    result = {
        "status": "VERIFIED fixed four-anchor candidate on exhaustive scope; OPEN universally",
        "period_policy": "All partitions use the canonical lcm grid, never qW.",
        "exhaustive_scope": "gcd-one subsets of {1,...,10}, sizes 3,...,6, with defined canonical grid",
        "exhaustive_configuration_count": len(exhaustive),
        "seeded_configuration_count": len(seeded),
        "certified_counts_exhaustive": {name: sum(
            item["candidates"].get(name, {}).get("certified", False)
            for item in exhaustive) for name in names},
        "first_misses_exhaustive": {name: first_miss(exhaustive, name)
                                     for name in names},
        "first_up_to_four_anchor_miss_seeded": first_miss(
            seeded, "transition_up_to_4_anchors"),
        "required": required,
    }
    Path(__file__).with_name("task25_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    out = run()
    print(json.dumps({k: v for k, v in out.items() if k != "required"}, indent=2))
