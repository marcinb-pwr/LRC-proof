"""Independent verification of TASK 20 three-label tables."""

import random
import sys
from itertools import combinations
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from interval_components import cyclic_components
from triple_alignment import direct_triple_transition_table, pair_to_triple_component_change, safe_component_count, triple_transition_table
from two_direction import two_direction_torus


def main():
    rng = random.Random(2001)
    checked = 0
    # Powers, odd integers, consecutive/translated intervals, and the critical
    # configuration, restricted to families satisfying the central hypothesis.
    for values in ((1, 2, 4), (1, 3, 5, 7), (2, 3, 4, 5),
                   (1, 3, 4, 5), (1, 3, 4, 5, 7, 18)):
        data = two_direction_torus(values)
        runners = tuple(data["runners"][i] for i in range(3))
        assert triple_transition_table(runners, data["order"]) == \
               direct_triple_transition_table(runners, data["order"])
        checked += 1
    for _ in range(110):
        size = rng.randint(3, 8)
        q = size + 1
        values = set(rng.sample(range(1, 32), size - 1))
        values.add(q * rng.randint(1, 31 // q))
        values = tuple(sorted(values))
        if len(values) != size or gcd(*values) != 1:
            continue
        data = two_direction_torus(values)
        for ids in list(combinations(range(size), 3))[:3]:
            runners = tuple(data["runners"][i] for i in ids)
            table = triple_transition_table(runners, data["order"])
            assert table == direct_triple_transition_table(runners, data["order"])
            safe = {z for z in range(data["order"])
                    if all(z % runner["period"] not in runner["bad_residues"]
                           for runner in runners)}
            assert safe_component_count(table, data["order"]) == \
                   len(cyclic_components(safe, data["order"]))
            change = pair_to_triple_component_change(runners, data["order"])
            assert change["triple_components"] == len(cyclic_components(
                safe, data["order"]))
        checked += 1
    assert checked >= 75
    print(f"triple-alignment checks passed ({checked} inputs)")


if __name__ == "__main__":
    main()
