import random
import unittest

from labelled_pairs import center_data, labelled_endpoint_word


class LabelledPairTests(unittest.TestCase):
    def test_mates_and_prefixes(self):
        rng = random.Random(1202026)
        for _ in range(250):
            raw = rng.sample(range(1, 25), rng.randint(2, 8))
            data = labelled_endpoint_word(raw)
            by_pair = {}
            for event in data["events"]:
                by_pair.setdefault(event["pair"], []).append(event)
            self.assertTrue(all(len(pair) == 2 for pair in by_pair.values()))
            for pair in by_pair.values():
                self.assertEqual(pair[0]["x"], pair[1]["mate"])
                self.assertEqual(pair[1]["x"], pair[0]["mate"])
            for item in data["word"][:-1]:
                if item["next_x"] > item["x"]:
                    x = item["x"]
                    direct = sum(min((x * v) % data["M"],
                                     (-x * v) % data["M"]) * data["q"]
                                 < data["M"] for v in data["velocities"])
                    self.assertEqual(item["prefix"], direct)

    def test_center_classification(self):
        for raw in ((1, 3), (1, 4), (2, 3, 12), (1, 2, 3, 20)):
            data = center_data(raw)
            expected = {v for v in data["velocities"] if v % data["q"] == 0}
            observed = {item["velocity"] for item in data["center_covering"]}
            self.assertEqual(observed, expected)


if __name__ == "__main__":
    unittest.main()
