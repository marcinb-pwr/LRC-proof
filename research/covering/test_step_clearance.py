import random
import unittest

from step_clearance import direct_clearance, safe_steps
from bad_sets import parameters


class StepClearanceTests(unittest.TestCase):
    def test_residue_word_matches_direct_clearance(self):
        rng = random.Random(1402026)
        checked = 0
        for _ in range(400):
            n = rng.randint(2, 9)
            q = n + 1
            raw = rng.sample(range(1, 45), n - 1) + [q * rng.randint(1, 10)]
            if len(set(raw)) != n:
                continue
            normalized, normalized_q, _, _ = parameters(raw)
            if not any(v % normalized_q == 0 for v in normalized):
                continue
            for sign in (-1, 1):
                data, safe = safe_steps(raw, sign=sign)
                predicted = set(safe)
                direct = {h for h in range(1, data["point_period"])
                          if direct_clearance(raw, h, sign) > 0}
                self.assertEqual(predicted, direct)
                checked += 1
        self.assertGreater(checked, 500)

    def test_mixed_fringe_family(self):
        for m in range(1, 101):
            h = 3 * m + (1 if m % 4 == 0 else 0)
            self.assertGreater(direct_clearance((1, 3, 4 * m), h), 0)


if __name__ == "__main__":
    unittest.main()
