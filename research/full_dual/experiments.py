"""Small exact full-dual and relaxed-threshold experiments."""

from __future__ import annotations

import json
import random
from fractions import Fraction
from pathlib import Path

from full_dual import finite_certificate
from relaxed_threshold import relaxed_certificate


def cases():
    out = [
        (1, 2), (1, 3), (1, 2, 3), (1, 2, 4),
        (1, 2, 4, 8), (1, 2, 4, 8, 16),
    ]
    random.seed(5)
    for n in range(2, 7):
        for _ in range(5):
            out.append(tuple(sorted(random.sample(range(1, 35), n))))
    return out


def main():
    rows = []
    for v in cases():
        exact = finite_certificate(v)
        relaxed = relaxed_certificate(v, Fraction(1, 100))
        rows.append({
            "V": list(v),
            "exact": exact,
            "relaxed_epsilon_1_100": relaxed,
        })
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(rows, indent=2) + "\n")
    print(f"wrote {path} ({len(rows)} cases)")
    done = [x for x in rows if x["exact"].get("enumerated")]
    print("enumerated cases:", len(done))
    print("exact positive cases:",
          sum(x["exact"]["positive"] for x in done))
    print("exact zero cases:",
          sum(not x["exact"]["positive"] for x in done))


if __name__ == "__main__":
    main()
