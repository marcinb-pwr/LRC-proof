"""Exact lattice data and certified support-2 truncation bounds."""

from __future__ import annotations

import math
from fractions import Fraction


def lcm(a: int, b: int) -> int:
    return abs(a // math.gcd(a, b) * b)


def setup(v: tuple[int, ...], i: int, j: int):
    q = len(v) + 1
    W = 1
    for x in v:
        W = lcm(W, x)
    M = q * W
    vi, vj = v[i], v[j]
    b_i, b_j = W // vi, W // vj
    return q, W, M, vi, vj, b_i, b_j


def lattice_basis(vi: int, vj: int, M: int):
    """Return a basis [(r,s), ...] for {(r,s): r vi+s vj=0 mod M}."""
    h = math.gcd(vi, vj)
    n = M // math.gcd(h, M)
    x, y = vi // h, vj // h
    a = math.gcd(x, n)
    n1 = n // a
    if n1 == 1:
        r0 = 0
    else:
        inv = pow((x // a) % n1, -1, n1)
        r0 = (-y * inv) % n1
    basis = ((n1, 0), (r0, a))
    assert (basis[0][0] * vi + basis[0][1] * vj) % M == 0
    assert (basis[1][0] * vi + basis[1][1] * vj) % M == 0
    assert abs(basis[0][0] * basis[1][1]
               - basis[0][1] * basis[1][0]) == n
    return basis, n


def smith_invariants(vi: int, vj: int, M: int):
    """Smith invariants of the homomorphism (r,s)->r vi+s vj mod M."""
    h = math.gcd(math.gcd(vi, vj), M)
    return h, M // h


def relation_s_residue(vi: int, vj: int, M: int, r: int):
    """Return the least nonnegative s residue, or None if unsolvable."""
    d = math.gcd(vj, M)
    if (r * vi) % d:
        return None
    modulus = M // d
    if modulus == 1:
        return 0
    inverse = pow((vj // d) % modulus, -1, modulus)
    return (-(r * vi // d) * inverse) % modulus


def g_q(q: int, n: int) -> float:
    if n == 0:
        return 1.0
    alpha = (q - 2) / (2 * q)
    x = math.pi * alpha * n
    return (math.sin(x) / x) ** 2


def exact_axis(v: tuple[int, ...]) -> Fraction:
    q = len(v) + 1
    W = 1
    for x in v:
        W = lcm(W, x)
    b = [W // x for x in v]
    if q % 2 == 0:
        return Fraction(1)
    return Fraction(1) - sum(
        (Fraction(1, (q - 2) ** 2 * x * x) for x in b if x % 2),
        Fraction(0),
    )


def tail_bound(q: int, R: int) -> float:
    """Uniform bound for |F_ij-F_ij^(R)| with |r|,|s|<=R truncation."""
    # g_q(n) <= C_q/n^2 for n != 0.
    C = 4 * q * q / (math.pi**2 * (q - 2)**2)
    # Sum_{|n|>R} 1/n^2 <= 2/R and
    # sum_{n != 0} 1/n^2 = pi^2/3. The omitted grid is the union of
    # {|r|>R} and {|s|>R}, with both coordinates nonzero.
    return 4 * C * C * math.pi**2 / (3 * R)


def pair_truncation(v: tuple[int, ...], i: int, j: int, R: int):
    q, W, M, vi, vj, bi, bj = setup(v, i, j)
    total = 0.0
    points = 0
    for r in range(-R, R + 1):
        s0 = relation_s_residue(vi, vj, M, r)
        if s0 is None:
            continue
        modulus = M // math.gcd(vj, M)
        for s in range(s0, R + 1, modulus):
            if s < -R:
                continue
            if r == 0 or s == 0:
                continue
            total += (-1.0) ** (r + s) * g_q(q, r) * g_q(q, s)
            points += 1
        # Include negative representatives congruent to s0.
        start = s0 - ((s0 + R) // modulus) * modulus
        for s in range(start, -R - 1, -modulus):
            if s < -R or s > R or s == 0:
                continue
            total += (-1.0) ** (r + s) * g_q(q, r) * g_q(q, s)
            points += 1
    # The two loops can overlap at s0 when it is in range.
    # Recompute through a set to guarantee no duplicate points.
    vals = set()
    for r in range(-R, R + 1):
        s0 = relation_s_residue(vi, vj, M, r)
        if s0 is None:
            continue
        modulus = M // math.gcd(vj, M)
        for k in range(-R - 1, R + 2):
            s = s0 + k * modulus
            if -R <= s <= R and r != 0 and s != 0:
                vals.add((r, s))
    total = sum(
        (-1.0) ** (r + s) * g_q(q, r) * g_q(q, s)
        for r, s in vals
    )
    return {
        "q": q,
        "M": M,
        "basis": lattice_basis(vi, vj, M)[0],
        "determinant": lattice_basis(vi, vj, M)[1],
        "smith_invariants": smith_invariants(vi, vj, M),
        "R": R,
        "value": total,
        "points": len(vals),
        "tail_bound": tail_bound(q, R),
        "certified_sign": abs(total) > tail_bound(q, R),
    }
