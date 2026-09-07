"""Independent checks of TASK 23 intersection and histogram formulae."""

import random
import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from multiplicity_surplus import multiplicity_histogram, surplus_from_histogram, surplus_from_intersections
from two_direction import two_direction_torus


def main():
    rng = random.Random(2301)
    inputs = [(1, 3, 4, 5), (1, 4, 5, 6, 9),
              (1, 2, 3, 4, 5, 7), (1, 3, 4, 5, 7, 18)]
    while len(inputs) < 35:
        size = rng.randint(4, 7)
        q = size + 1
        values = set(rng.sample(range(1, 34), size - 1))
        values.add(q * rng.randint(1, 33 // q))
        values = tuple(sorted(values))
        if len(values) == size and gcd(*values) == 1:
            try:
                two_direction_torus(values)
            except ValueError:
                continue
            inputs.append(values)
    for values in inputs:
        data = two_direction_torus(values)
        histogram = multiplicity_histogram(data["runners"], data["order"])
        assert sum(histogram) == data["order"]
        assert surplus_from_histogram(histogram) == \
               surplus_from_intersections(data["runners"], data["order"])
    print(f"multiplicity-surplus checks passed ({len(inputs)} inputs)")


if __name__ == "__main__":
    main()
