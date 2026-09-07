"""Deterministic TASK 26 four-anchor counterexample certificate."""

import json
from pathlib import Path

from localized_certificate import multi_anchor_transition_certificate
from multiplier_fragmentation import strip_multiplier
from two_direction import safe_classes


COUNTEREXAMPLE = (1, 5, 6, 7, 8, 11, 13)


def record(values):
    data, safe = safe_classes(values)
    certificate = multi_anchor_transition_certificate(
        data["runners"], data["order"], 4)
    phases = []
    for runner in data["runners"]:
        phase = strip_multiplier(data, runner)
        phases.append([runner["velocity"], phase["period"], phase["multiplier"],
                       phase["center"], phase["reduced_radius"]])
    return {"velocities": list(values), "q": data["q"],
            "lcm_grid_period": data["order"], "safe_class_count": len(safe),
            "anchor_labels": [values[i] for i in certificate["anchors"]],
            "phase_records_v_H_a_c_rho": phases,
            "realized_fibers": certificate["realized_fibers"],
            "maximum_quadratic": max(certificate["quadratics"].values()),
            "fiber_histograms": certificate["histograms"],
            "fiber_quadratics": certificate["quadratics"],
            "certified": certificate["certified"]}


def run():
    decisive = record(COUNTEREXAMPLE)
    assert decisive["safe_class_count"] > 0
    assert not decisive["certified"]
    deletion_audit = []
    for removed in COUNTEREXAMPLE:
        reduced = tuple(v for v in COUNTEREXAMPLE if v != removed)
        # The canonical central-cover construction requires a q-divisible label.
        q = len(reduced) + 1
        if not any(v % q == 0 for v in reduced):
            deletion_audit.append({"removed": removed, "status": "outside canonical hypothesis"})
            continue
        item = record(reduced)
        deletion_audit.append({"removed": removed, "status": "audited",
                               "certified": item["certified"],
                               "safe_class_count": item["safe_class_count"]})
    prior = json.loads(Path(__file__).with_name("task14_results.json").read_text())
    required_values = [(1, 3, 4, 5), (1, 4, 5, 6, 9),
                       (1, 2, 3, 4, 5, 7)] + [
        tuple(x["velocities"]) for x in prior["full_period_obstructions"]]
    required = [record(values) for values in required_values]
    result = {"status": "DISPROVED universal four-anchor certificate",
              "period_policy": "All data use the canonical lcm grid, never qW.",
              "counterexample": decisive,
              "required_configuration_count": len(required),
              "required_certified_count": sum(x["certified"] for x in required),
              "single_deletion_audit": deletion_audit}
    Path(__file__).with_name("task26_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    out = run()
    print(json.dumps({"status": out["status"],
                      "velocities": out["counterexample"]["velocities"],
                      "safe_class_count": out["counterexample"]["safe_class_count"],
                      "maximum_quadratic": out["counterexample"]["maximum_quadratic"]},
                     indent=2))
