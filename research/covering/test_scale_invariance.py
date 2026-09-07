"""Explicit raw-grid tests for the resolution issue in Theorem 35."""

import random
import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from scale_invariance import best_margin_on_refined_time_grid, phase_word, primitive_phase_period, safe_indices_on_refined_time_grid, scaled_phase_word_in_original_units


def main():
    rng = random.Random(3501)
    inputs = [(1, 3, 4, 5), (2, 3), (1, 2, 4)]
    while len(inputs) < 20:
        size = rng.randint(2, 6)
        values = tuple(sorted(rng.sample(range(1, 11), size)))
        if gcd(*values) == 1:
            inputs.append(values)
    for values in inputs:
        original = phase_word(values)
        period, expected = primitive_phase_period(values)
        assert period == expected == len(original)
        for scale in range(2, 5):
            scaled = scaled_phase_word_in_original_units(values, scale)
            assert len(scaled) == scale * len(original)
            assert scaled == original * scale
            # More time coordinates exist, but no new simultaneous phase vector.
            assert set(scaled) == set(original)
            refined_safe = safe_indices_on_refined_time_grid(values, scale)
            base_safe = safe_indices_on_refined_time_grid(values, 1)
            assert bool(refined_safe) == bool(base_safe)
            assert {scale * x for x in base_safe}.issubset(refined_safe)
        margins = [best_margin_on_refined_time_grid(values, scale)
                   for scale in (1, 2, 4)]
        fractions = [x["margin_numerator"] / x["margin_denominator"]
                     for x in margins]
        assert fractions[0] <= fractions[1] <= fractions[2]
    # The sharp two-runner configuration has no positive uniform margin.
    for refinement in range(1, 101):
        sharp = best_margin_on_refined_time_grid((1, 2), refinement)
        assert sharp["margin_numerator"] == 0
        assert sharp["index"] in (2 * refinement, 4 * refinement)
    print(f"raw scale-invariance checks passed ({len(inputs)} inputs)")


if __name__ == "__main__":
    main()
