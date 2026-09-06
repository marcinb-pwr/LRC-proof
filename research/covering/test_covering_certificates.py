"""Tests for exact TASK 16 tree and triple certificates."""

import random
import sys
from itertools import combinations
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from covering_certificates import certificate_bounds, intersection_count
from two_direction import two_direction_torus


def main():
    rng = random.Random(1601)
    checked = 0
    for _ in range(120):
        n = rng.randint(2, 7)
        q = n + 1
        values = tuple(sorted(rng.sample(range(1, 25), n)))
        if gcd(*values) != 1 or not any(v % q == 0 for v in values):
            continue
        data = two_direction_torus(values)
        sets = [{z for z in range(data["order"])
                 if z % r["period"] in set(r["bad_residues"])}
                for r in data["runners"]]
        for count in (2, 3):
            for ids in list(combinations(range(n), count))[:4]:
                actual = len(set.intersection(*(sets[i] for i in ids)))
                assert intersection_count(tuple(data["runners"][i] for i in ids),
                                          data["order"]) == actual
        union = len(set.union(*sets))
        bounds = certificate_bounds(data, triples=True)
        assert union <= bounds["tree_upper_bound"]
        assert union <= bounds["bonferroni3_upper_bound"]
        checked += 1
    assert checked >= 20
    print(f"covering-certificate checks passed ({checked} inputs)")


if __name__ == "__main__":
    main()
