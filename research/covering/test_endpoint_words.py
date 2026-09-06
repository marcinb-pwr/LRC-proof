import random
import unittest

from bad_sets import parameters
from endpoint_words import endpoint_word


class EndpointWordTests(unittest.TestCase):
    def test_prefixes_equal_direct_multiplicity(self):
        rng = random.Random(1102026)
        for _ in range(250):
            n = rng.randint(2, 7)
            raw = rng.sample(range(1, 22), n)
            data = endpoint_word(raw)
            velocities, q, w, _ = parameters(raw)
            for left, right, multiplicity in data["segments"]:
                for point in {left, right, (left + right) // 2}:
                    direct = sum(min((point * v) % data["M"],
                                     (-point * v) % data["M"]) * q < data["M"]
                                 for v in velocities)
                    self.assertEqual(multiplicity,
                                     direct)

    def test_exact_reflection_antisymmetry(self):
        for raw in ((1, 4, 12), (2, 3, 12), (1, 2, 4, 8), (7, 9)):
            data = endpoint_word(raw)
            events = dict(data["word"])
            for x, delta in data["word"]:
                self.assertEqual(events[data["M"] + 1 - x], -delta)


if __name__ == "__main__":
    unittest.main()
