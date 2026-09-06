"""Exact CRT/block counts for intersections of bad sets."""

from itertools import combinations
from math import gcd, lcm


def primitive_block(velocity, q, w):
    b = w // velocity
    period = q * b
    return period, set(range(b)) | set(range(period - b + 1, period))


def pair_intersection_size(vi, vj, q, w):
    """Count via one common period, then lift to Z/(qW)."""
    pi, ai = primitive_block(vi, q, w)
    pj, aj = primitive_block(vj, q, w)
    common_period = lcm(pi, pj)
    primitive_count = sum(k % pi in ai and k % pj in aj
                          for k in range(common_period))
    return primitive_count * (q * w // common_period)


def centered_pair_count(bi, bj, q):
    """Count compatible signed endpoint representatives in one common period.

    The representatives are u in [-(bi-1),bi-1] and similarly for v.  CRT
    compatibility is exactly u == v (mod q*gcd(bi,bj)).  This difference-sum
    implementation is independent of the (potentially large) common period.
    """
    d = gcd(bi, bj)
    step = q * d
    a, b = bi - 1, bj - 1
    lower = -((a + b) // step)
    upper = (a + b) // step
    total = 0
    for t in range(lower, upper + 1):
        shift = t * step  # u-v
        lo = max(-a, -b + shift)
        hi = min(a, b + shift)
        total += max(0, hi - lo + 1)
    return total


def pair_intersection_closed(vi, vj, q, w):
    """The proved centered-CRT formula for |B_i intersect B_j|."""
    bi, bj = w // vi, w // vj
    return (w // lcm(bi, bj)) * centered_pair_count(bi, bj, q)


def triple_intersection_size(vi, vj, vk, q, w):
    """Exact common-period count for a triple, lifted to Z/(qW)."""
    data = [primitive_block(v, q, w) for v in (vi, vj, vk)]
    common_period = lcm(*(period for period, _ in data))
    count = sum(all(x % period in block for period, block in data)
                for x in range(common_period))
    return count * (q * w // common_period)


def all_pair_intersections(velocities, q, w):
    return {f"{i},{j}": pair_intersection_closed(velocities[i], velocities[j], q, w)
            for i, j in combinations(range(len(velocities)), 2)}
