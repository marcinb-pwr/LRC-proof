"""Exact CRT/block counts for intersections of bad sets."""

from itertools import combinations
from math import lcm


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


def all_pair_intersections(velocities, q, w):
    return {f"{i},{j}": pair_intersection_size(velocities[i], velocities[j], q, w)
            for i, j in combinations(range(len(velocities)), 2)}
