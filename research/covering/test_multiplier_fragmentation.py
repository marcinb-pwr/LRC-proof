"""Boundary, family, and random checks for TASK 18."""

import random
import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from multiplier_fragmentation import actual_component_count, predicted_component_count, strip_multiplier
from two_direction import two_direction_torus


def admissible(values):
    q = len(values) + 1
    return gcd(*values) == 1 and any(v % q == 0 for v in values)


def check(values):
    data = two_direction_torus(values)
    for runner in data["runners"]:
        info = strip_multiplier(data, runner)
        assert info["period"] == runner["period"]
        assert info["size"] == len(runner["bad_residues"])
        predicted = predicted_component_count(info["period"], info["size"],
                                              info["inverse_multiplier"])
        assert predicted == actual_component_count(runner["bad_residues"],
                                                   runner["period"])


def main():
    families = [(1, 3, 4, 5), (1, 3, 4, 5, 7, 18),
                (1, 2, 4, 8), (1, 2, 3, 4), (1, 3, 5, 8)]
    checked = 0
    for values in families:
        if admissible(values):
            check(values)
            checked += 1
    rng = random.Random(1801)
    for _ in range(160):
        size = rng.randint(2, 8)
        q = size + 1
        values = set(rng.sample(range(1, 35), size - 1))
        values.add(q * rng.randint(1, 34 // q))
        values = tuple(sorted(values))
        if len(values) == size and admissible(values):
            check(values)
            checked += 1
    assert checked >= 100
    print(f"multiplier-fragmentation checks passed ({checked} inputs)")


if __name__ == "__main__":
    main()
