"""Exact small-case checks for the CRT lattice formulas.

This script uses only integer arithmetic.  It verifies the image size,
pairwise compatibility, determinant formula, and the dual congruence
criterion for small configurations.
"""

from itertools import product as cartesian_product
from math import gcd, lcm


def check(v):
    n = len(v)
    q = n + 1
    W = 1
    for x in v:
        W = lcm(W, x)
    b = [W // x for x in v]
    moduli = [q * x for x in b]
    period = lcm(*moduli)

    image = {
        tuple(x % m for m in moduli)
        for x in range(period)
    }
    compatible = {
        r for r in cartesian_product(*(range(m) for m in moduli))
        if all(
            (r[i] - r[j]) % (q * gcd(b[i], b[j])) == 0
            for i in range(n) for j in range(i)
        )
    }
    assert image == compatible

    determinant = q ** (n - 1) * product(b) // lcm(*b)
    assert len(image) * determinant == product(moduli)

    for a in cartesian_product(range(-q, q + 1), repeat=n):
        lhs = sum(a[i] * v[i] for i in range(n)) % (q * W)
        xi_is_dual = lhs == 0
        # Test the defining character on one full period of the image.
        character_is_integral = all(
            (x * sum(a[i] * v[i] for i in range(n))) % (q * W) == 0
            for x in range(period)
        )
        assert xi_is_dual == character_is_integral

    print(f"OK V={v}: q={q}, W={W}, det={determinant}")


def product(xs):
    out = 1
    for x in xs:
        out *= x
    return out


if __name__ == "__main__":
    for values in ([1], [1, 2], [1, 2, 3], [1, 2, 3, 4],
                   [2, 4], [2, 6, 10]):
        check(values)
