"""Exact tests for TASK 17 component endpoints and scale invariance."""

import random
import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from interval_components import component_certificate, cyclic_components
from two_direction import safe_classes


def expand(components, modulus):
    return {((start + offset) % modulus)
            for start, length in components for offset in range(length)}


def main():
    assert cyclic_components({7, 0, 1, 4}, 8) == ((4, 1), (7, 3))
    rng = random.Random(1701)
    checked = 0
    for _ in range(100):
        size = rng.randint(2, 7)
        q = size + 1
        values = tuple(sorted(rng.sample(range(1, 25), size)))
        if gcd(*values) != 1 or not any(v % q == 0 for v in values):
            continue
        data, safe = safe_classes(values)
        components = component_certificate(data)
        assert expand(components, data["order"]) == set(safe)
        scale = rng.randint(2, 9)
        scaled_data, scaled_safe = safe_classes(tuple(scale * v for v in values))
        assert scaled_data["velocities"] == data["velocities"]
        assert scaled_data["order"] == data["order"]
        assert scaled_safe == safe
        checked += 1
    assert checked >= 20
    print(f"interval-component checks passed ({checked} inputs)")


if __name__ == "__main__":
    main()
