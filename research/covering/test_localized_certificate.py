"""Checks for TASK 24 localized quadratic certificate."""

import random
import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from localized_certificate import localized_certificate, quadratic_from_moments, quadratic_value
from two_direction import safe_classes, two_direction_torus


def main():
    rng = random.Random(2401)
    inputs = [(1, 3, 4, 5), (1, 4, 5, 6, 9),
              (1, 2, 3, 4, 5, 7), (1, 3, 4, 5, 7, 18)]
    while len(inputs) < 45:
        size = rng.randint(3, 7)
        q = size + 1
        values = set(rng.sample(range(1, 36), size - 1))
        values.add(q * rng.randint(1, 35 // q))
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
        result = localized_certificate(data["runners"], data["order"])
        assert sum(x["size"] for x in result["fibers"].values()) == data["order"]
        for fiber in result["fibers"].values():
            assert quadratic_value(fiber["histogram"]) == \
                   quadratic_from_moments(fiber["histogram"])
            if fiber["quadratic"] > 0:
                assert fiber["histogram"][0] > 0
        if result["certified"]:
            assert safe_classes(values)[1]
    print(f"localized-certificate checks passed ({len(inputs)} inputs)")


if __name__ == "__main__":
    main()
