"""Exact endpoint localization for the strict periodic bad sets.

Intervals are inclusive integer intervals.  Nothing in this module scans the
ambient modulus; the running time depends on the number of endpoint blocks.
"""

from collections import defaultdict
from math import comb


def off_core_interval(b_values, modulus):
    """Return the (possibly empty) linear complement of the cyclic core."""
    beta = min(b_values)
    return None if beta > modulus - beta else (beta, modulus - beta)


def bad_blocks(v, q, w):
    """Disjoint inclusive blocks for B_v in [0,q*w-1]."""
    b = w // v
    period = q * b
    radius = b - 1
    modulus = q * w
    blocks = []
    for j in range(v):
        centre = j * period
        lo, hi = centre - radius, centre + radius
        if lo < 0:
            blocks.append((0, hi))
            blocks.append((modulus + lo, modulus - 1))
        else:
            blocks.append((lo, hi))
    return sorted(blocks)


def clipped_off_core_blocks(v, q, w, beta):
    """Explicit translated blocks outside C, clipped to D=[beta,M-beta]."""
    lo_d, hi_d = beta, q * w - beta
    return [(max(lo, lo_d), min(hi, hi_d))
            for lo, hi in bad_blocks(v, q, w)
            if max(lo, lo_d) <= min(hi, hi_d)]


def endpoint_segments(velocities, q, w):
    """Maximal constant-multiplicity segments in the off-core interval.

    Returns inclusive triples (left, right, multiplicity).  Equal-coordinate
    endpoint events are combined before a segment is emitted.
    """
    modulus = q * w
    b_values = [w // v for v in velocities]
    domain = off_core_interval(b_values, modulus)
    if domain is None:
        return []
    left, right = domain
    events = defaultdict(int)
    events[left] += 0
    events[right + 1] += 0
    for v in velocities:
        for lo, hi in clipped_off_core_blocks(v, q, w, min(b_values)):
            events[lo] += 1
            events[hi + 1] -= 1
    segments, multiplicity = [], 0
    points = sorted(events)
    for index, point in enumerate(points[:-1]):
        multiplicity += events[point]
        next_point = points[index + 1]
        if point < next_point:
            if segments and segments[-1][2] == multiplicity:
                segments[-1] = (segments[-1][0], next_point - 1, multiplicity)
            else:
                segments.append((point, next_point - 1, multiplicity))
    return segments


def localized_statistics(velocities, q, w):
    """Exact gap and overlap statistics computed from endpoint segments."""
    modulus = q * w
    beta = min(w // v for v in velocities)
    segments = endpoint_segments(velocities, q, w)
    lengths = [right - left + 1 for left, right, _ in segments]
    safe = [length for length, segment in zip(lengths, segments)
            if segment[2] == 0]
    changes = [segments[i + 1][0] - segments[i][0]
               for i in range(len(segments) - 1)]
    off_membership = sum(length * segment[2]
                         for length, segment in zip(lengths, segments))
    off_pairs = sum(length * comb(segment[2], 2)
                    for length, segment in zip(lengths, segments))
    domain_size = max(0, modulus - 2 * beta + 1)
    # P <= N R/2, where R=sum (m-1)_+, gives |union|<=A-2P/N.
    localized_certificate = (len(velocities) * off_membership - 2 * off_pairs
                             < len(velocities) * domain_size)
    return {
        "covers": bool(segments) and all(s[2] > 0 for s in segments),
        "off_core_size": domain_size,
        "off_core_membership": off_membership,
        "off_core_pair_overlap": off_pairs,
        "longest_safe_run": max(safe, default=0),
        "change_count": max(0, len(segments) - 1),
        "min_change_distance": min(changes, default=0),
        "max_change_distance": max(changes, default=0),
        "localized_pair_certificate": localized_certificate,
        "segments": segments,
    }
