"""Tests for TASK 22 restricted-incidence identities."""

import random
import sys
from itertools import combinations
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from restricted_incidence import pointwise_averaging_totals, restricted_certificate
from two_direction import two_direction_torus


def direct(data, triple):
    runners, order = data["runners"], data["order"]
    safe = {z for z in range(order) if all(
        z % runners[i]["period"] not in runners[i]["bad_residues"]
        for i in triple)}
    values = tuple(sum(z % runners[i]["period"] in runners[i]["bad_residues"]
                       for z in safe)
                   for i in range(len(runners)) if i not in triple)
    return len(safe), values


def main():
    rng = random.Random(2201)
    checked = 0
    for values in ((1, 3, 4, 5), (1, 3, 4, 5, 7, 18),
                   (1, 2, 4), (1, 3, 5, 7), (2, 3, 4, 5)):
        data = two_direction_torus(values)
        certificates = []
        for triple in combinations(range(len(values)), 3):
            result = restricted_certificate(data["runners"], data["order"], triple)
            safe, incidences = direct(data, triple)
            assert (result["safe_mass"], result["incidences"]) == (safe, incidences)
            certificates.append(result)
            checked += 1
        assert sum(x["safe_mass"] for x in certificates) == \
               pointwise_averaging_totals(data["runners"], data["order"])[0]
        assert sum(x["incidence_sum"] for x in certificates) == \
               pointwise_averaging_totals(data["runners"], data["order"])[1]
    for _ in range(35):
        size = rng.randint(3, 7)
        q = size + 1
        values = set(rng.sample(range(1, 35), size - 1))
        values.add(q * rng.randint(1, 34 // q))
        values = tuple(sorted(values))
        if len(values) != size or gcd(*values) != 1:
            continue
        data = two_direction_torus(values)
        result = restricted_certificate(data["runners"], data["order"])
        assert (result["safe_mass"], result["incidences"]) == direct(data, result["triple"])
        checked += 1
    assert checked >= 35
    print(f"restricted-incidence checks passed ({checked} cases)")


if __name__ == "__main__":
    main()
