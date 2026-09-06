import random
import unittest

from central_fringe import boundary_profile


class CentralFringeTests(unittest.TestCase):
    def test_clearance_matches_direct_badness(self):
        rng = random.Random(1302026)
        for _ in range(300):
            n = rng.randint(2, 9)
            raw = rng.sample(range(1, 35), n)
            profile = boundary_profile(raw)
            if not profile["central"]:
                continue
            for sign, side in ((-1, "minus"), (1, "plus")):
                x = profile["W"] + sign * profile["b_star"]
                for entry in profile[side]:
                    v = entry["velocity"]
                    distance = min((x * v) % profile["M"],
                                   (-x * v) % profile["M"])
                    direct_safe = distance * profile["q"] >= profile["M"]
                    self.assertEqual(entry["safe"], direct_safe)

    def test_exact_fringe_rule(self):
        rng = random.Random(1313)
        checked = 0
        for _ in range(1000):
            n = rng.randint(2, 9)
            q = n + 1
            v_star = q * rng.randint(2, 8)
            others = rng.sample(range(1, v_star), n - 1)
            if any(v % q == 0 for v in others):
                continue
            profile = boundary_profile(others + [v_star])
            # Normalization does not change these residues only when the gcd
            # is one; restrict the theorem test to its stated hypotheses.
            if profile["v_star"] != v_star:
                continue
            plus_bad = {e["velocity"] for e in profile["plus"] if not e["safe"]}
            minus_bad = {e["velocity"] for e in profile["minus"] if not e["safe"]}
            self.assertEqual(plus_bad,
                             {v for v in profile["velocities"] if v % q == q - 1})
            self.assertEqual(minus_bad,
                             {v for v in profile["velocities"] if v % q == 1})
            checked += 1
        self.assertGreater(checked, 100)


if __name__ == "__main__":
    unittest.main()
