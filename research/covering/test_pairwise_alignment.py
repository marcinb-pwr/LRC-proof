"""Independent exact tests for TASK 19 transition tables."""

import random
import sys
from itertools import combinations
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from interval_components import pair_complement_components
from pairwise_alignment import direct_joint_transition_table, joint_transition_table, pair_safe_component_count
from two_direction import two_direction_torus


def main():
    rng = random.Random(1901)
    checked = 0
    for _ in range(130):
        size = rng.randint(2, 8)
        q = size + 1
        values = set(rng.sample(range(1, 35), size - 1))
        values.add(q * rng.randint(1, 34 // q))
        values = tuple(sorted(values))
        if len(values) != size or gcd(*values) != 1:
            continue
        data = two_direction_torus(values)
        for i, j in list(combinations(range(size), 2))[:6]:
            left, right = data["runners"][i], data["runners"][j]
            assert joint_transition_table(left, right, data["order"]) == \
                   direct_joint_transition_table(left, right, data["order"])
            assert pair_safe_component_count(left, right, data["order"]) == \
                   len(pair_complement_components(data, i, j))
        checked += 1
    assert checked >= 90
    print(f"pairwise-alignment checks passed ({checked} inputs)")


if __name__ == "__main__":
    main()
