"""Exact global support-2 aggregation experiments."""

from __future__ import annotations

import json
import random
from fractions import Fraction
from pathlib import Path

from aggregation import check


def cases():
    out = []
    for n in range(2, 9):
        out.extend([
            ("consecutive", tuple(range(1, n + 1))),
            ("odd", tuple(2 * k + 1 for k in range(n))),
            ("powers_two", tuple(2 ** k for k in range(n))),
            ("translated", tuple(range(7, 7 + n))),
        ])
    random.seed(4)
    for n in range(2, 9):
        for _ in range(3):
            out.append(("random", tuple(sorted(random.sample(range(1, 70), n)))))
    return out


def main():
    rows = []
    for name, v in cases():
        result = check(v)
        rows.append({"family": name, "V": list(v), **result})
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(rows, indent=2) + "\n")
    done = [r for r in rows if r["enumerated"]]
    negative = [r for r in done if Fraction(r["F_le2"]) < 0]
    print(f"wrote {path} ({len(rows)} cases)")
    print(f"enumerated: {len(done)}, negative F_le2: {len(negative)}")


if __name__ == "__main__":
    main()
