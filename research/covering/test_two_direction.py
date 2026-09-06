"""Independent checks for the TASK 15 torus formulae."""

import random
import sys
from itertools import combinations
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from central_fringe import cyclic_distance
from two_direction import pair_intersection_count, safe_classes


def main():
    rng = random.Random(1501)
    checked = 0
    for _ in range(80):
        n = rng.randint(2, 7)
        q = n + 1
        values = tuple(sorted(rng.sample(range(1, 31), n)))
        if gcd(*values) != 1 or not any(v % q == 0 for v in values):
            continue
        data, safe = safe_classes(values)
        direct = []
        for z in range(data["order"]):
            x = data["W"] + z * data["gcd_direction"]
            if all(cyclic_distance(x, q * (data["W"] // v)) >
                   data["W"] // v - 1 for v in values):
                direct.append(z)
        assert tuple(direct) == safe
        for left, right in combinations(data["runners"], 2):
            if len(left["bad_residues"]) * len(right["bad_residues"]) > 100_000:
                continue
            left_bad, right_bad = set(left["bad_residues"]), set(right["bad_residues"])
            actual = sum(z % left["period"] in left_bad and
                         z % right["period"] in right_bad
                         for z in range(data["order"]))
            assert pair_intersection_count(left, right, data["order"]) == actual
        checked += 1
    assert checked >= 10
    print(f"two-direction checks passed ({checked} random inputs)")


if __name__ == "__main__":
    main()
