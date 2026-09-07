"""Independent checks for TASK 21 quantitative triple bounds."""

import random
import sys
from itertools import combinations
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from triple_safe import divisor_alignment, triple_safe_certificate
from two_direction import two_direction_torus


def main():
    rng = random.Random(2101)
    checked = 0
    for values in ((1, 2, 4), (1, 3, 5, 7), (2, 3, 4, 5),
                   (1, 3, 4, 5), (1, 3, 4, 5, 7, 18)):
        data = two_direction_torus(values)
        for ids in combinations(range(len(values)), 3):
            runners = tuple(data["runners"][i] for i in ids)
            result = triple_safe_certificate(runners, data["order"])
            direct = sum(all(z % runner["period"] not in runner["bad_residues"]
                             for runner in runners)
                         for z in range(data["order"]))
            assert result["all_safe_mass"] == direct
            assert direct >= result["pair_corrected_bound"] >= result["union_bound"]
            if all(divisor_alignment(runner) for runner in runners) and data["q"] >= 7:
                assert result["union_bound"] > 0
            checked += 1
    for _ in range(80):
        size = rng.randint(3, 8)
        q = size + 1
        values = set(rng.sample(range(1, 45), size - 1))
        values.add(q * rng.randint(1, 44 // q))
        values = tuple(sorted(values))
        if len(values) != size or gcd(*values) != 1:
            continue
        data = two_direction_torus(values)
        for ids in list(combinations(range(size), 3))[:4]:
            runners = tuple(data["runners"][i] for i in ids)
            result = triple_safe_certificate(runners, data["order"])
            assert result["all_safe_mass"] >= result["pair_corrected_bound"]
            checked += 1
    assert checked >= 100
    print(f"triple-safe checks passed ({checked} triples)")


if __name__ == "__main__":
    main()
