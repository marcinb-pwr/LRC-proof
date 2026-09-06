"""Regression tests for the independent endpoint sweep."""

import random
import unittest

from bad_sets import bad_set, parameters
from localization import localized_statistics
from moments import forced_core, multiplicities


class LocalizationTests(unittest.TestCase):
    def test_endpoint_sweep_matches_residue_scan(self):
        rng = random.Random(10)
        for n in range(2, 8):
            for _ in range(30):
                raw = tuple(sorted(rng.sample(range(1, 15), n)))
                velocities, q, w, modulus = parameters(raw)
                sets = [bad_set(v, q, w) for v in velocities]
                values = multiplicities(sets, modulus)
                core = forced_core([w // v for v in velocities], modulus)
                outside = [k for k in range(modulus) if k not in core]
                loc = localized_statistics(velocities, q, w)
                self.assertEqual(loc["covers"], all(values[k] for k in outside))
                self.assertEqual(loc["off_core_membership"],
                                 sum(values[k] for k in outside))
                self.assertEqual(loc["off_core_pair_overlap"],
                                 sum(values[k] * (values[k] - 1) // 2
                                     for k in outside))

    def test_common_velocity_scaling_normalizes_identically(self):
        for raw in ((2, 5), (1, 3, 8), (3, 4, 7, 11)):
            base = parameters(raw)
            for scale in (2, 7, 31):
                scaled = parameters(tuple(scale * v for v in raw))
                self.assertEqual(base, scaled)
                self.assertEqual(localized_statistics(*base[:1], base[1], base[2]),
                                 localized_statistics(*scaled[:1], scaled[1], scaled[2]))


if __name__ == "__main__":
    unittest.main()
