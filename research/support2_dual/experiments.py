"""Exact dual-box experiments and independent direct-sum checks."""

from __future__ import annotations

import json
import math
from pathlib import Path

from exact_formula import exact_support2
from dual_lattice import triangle_factor


def direct_g(q, n):
    if n == 0:
        return 1.0
    x = math.pi * (q - 2) * n / (2 * q)
    return (math.sin(x) / x) ** 2


def direct_pair(v, i, j, radius=4000):
    q = len(v) + 1
    W = math.lcm(*v)
    M = q * W
    total = 0.0
    for r in range(-radius, radius + 1):
        for s in range(-radius, radius + 1):
            if r and s and (r * v[i] + s * v[j]) % M == 0:
                total += (-1.0) ** (r + s) * direct_g(q, r) * direct_g(q, s)
    return total


def main():
    examples = [
        (1, 2), (1, 3), (1, 4), (2, 3), (2, 5),
        (1, 2, 3), (1, 3, 5), (1, 2, 3, 4), (1, 2, 4, 8),
    ]
    rows = []
    for v in examples:
        for i, j in [(0, 1)]:
            exact, complete, points, data = exact_support2(v, i, j)
            rows.append({
                "V": list(v),
                "pair": [i, j],
                "basis": data["basis"],
                "dual_basis": [[str(x) for x in b] for b in data["dual_basis"]],
                "finite_dual_points": [[str(x), str(y)] for x, y in points],
                "T_exact": str(complete),
                "F2_exact": str(exact),
                "F2_direct_R4000": direct_pair(v, i, j),
            })
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(rows, indent=2) + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
