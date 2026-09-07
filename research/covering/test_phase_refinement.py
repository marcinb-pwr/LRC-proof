"""Independent tests for TASK 25 bounded phase refinements."""

import random
import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from localized_certificate import coarse_phase_bin_certificate, multi_anchor_transition_certificate, short_word_certificate
from multiplier_fragmentation import strip_multiplier
from two_direction import safe_classes, two_direction_torus


def main():
    rng = random.Random(2501)
    inputs = [(1, 3, 4, 5), (1, 4, 5, 6, 9),
              (1, 2, 3, 4, 5, 7), (1, 3, 4, 5, 7, 18)]
    while len(inputs) < 45:
        size = rng.randint(3, 8)
        q = size + 1
        values = set(rng.sample(range(1, 38), size - 1))
        values.add(q * rng.randint(1, 37 // q))
        values = tuple(sorted(values))
        if len(values) != size or gcd(*values) != 1:
            continue
        try:
            two_direction_torus(values)
        except ValueError:
            continue
        inputs.append(values)
    for values in inputs:
        data = two_direction_torus(values)
        phases = tuple(strip_multiplier(data, runner) for runner in data["runners"])
        candidates = [short_word_certificate(data["runners"], data["order"], 1),
                      coarse_phase_bin_certificate(data["runners"], data["order"], phases, 4)]
        candidates += [multi_anchor_transition_certificate(
            data["runners"], data["order"], k)
            for k in range(1, min(4, len(values)) + 1)]
        for candidate in candidates:
            assert candidate["realized_fibers"] <= candidate["fiber_bound"]
            if candidate["certified"]:
                assert safe_classes(values)[1]
    critical = two_direction_torus((1, 3, 4, 5))
    assert not multi_anchor_transition_certificate(
        critical["runners"], critical["order"], 1)["certified"]
    assert multi_anchor_transition_certificate(
        critical["runners"], critical["order"], 2)["certified"]
    print(f"phase-refinement checks passed ({len(inputs)} inputs)")


if __name__ == "__main__":
    main()
