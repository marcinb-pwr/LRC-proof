"""Certified support-2 experiments."""

from __future__ import annotations

import json
import random
from pathlib import Path

from exact_pair import exact_axis, pair_truncation


def cases():
    out = []
    for n in range(2, 9):
        out.extend([
            ("consecutive", tuple(range(1, n + 1))),
            ("odd", tuple(2 * k + 1 for k in range(n))),
            ("powers_two", tuple(2 ** k for k in range(n))),
            ("translated", tuple(range(7, 7 + n))),
        ])
    random.seed(3)
    for n in range(2, 9):
        for _ in range(3):
            out.append(("random", tuple(sorted(random.sample(range(1, 80), n)))))
    return out


def main():
    rows = []
    for name, v in cases():
        pairs = []
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                pairs.append({
                    "i": i,
                    "j": j,
                    "R8": pair_truncation(v, i, j, 8),
                    "R32": pair_truncation(v, i, j, 32),
                })
        rows.append({
            "family": name,
            "V": list(v),
            "axis_exact": str(exact_axis(v)),
            "pairs": pairs,
        })
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(rows, indent=2) + "\n")
    certified = [
        (r["V"], p["i"], p["j"], p["R32"]["value"],
         p["R32"]["tail_bound"])
        for r in rows for p in r["pairs"] if p["R32"]["certified_sign"]
    ]
    negative = [x for x in certified if x[3] < 0]
    print(f"wrote {path} ({len(rows)} cases)")
    print(f"certified pair signs at R=32: {len(certified)}")
    print(f"certified negative pair signs: {len(negative)}")


if __name__ == "__main__":
    main()
