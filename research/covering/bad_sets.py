"""Exact bad sets for the finite Lonely Runner covering problem."""

from math import gcd, lcm


def lcm_many(values):
    out = 1
    for value in values:
        out = lcm(out, value)
    return out


def normalize(velocities):
    common = 0
    for value in velocities:
        common = gcd(common, value)
    return tuple(value // common for value in velocities)


def parameters(velocities):
    velocities = normalize(velocities)
    n = len(velocities)
    q = n + 1
    w = lcm_many(velocities)
    return velocities, q, w, q * w


def bad_set(velocity, q, w):
    """Return B_v with the strict endpoint convention, as residues mod qW."""
    modulus = q * w
    # Integer arithmetic avoids floating-point endpoint errors.
    return {k for k in range(modulus)
            if min((k * velocity) % modulus,
                   (-k * velocity) % modulus) * q < modulus}


def bad_set_by_period(velocity, q, w):
    """Construct B_v from its primitive block and repeat it v times."""
    b = w // velocity
    period = q * b
    block = set(range(b)) | set(range(period - b + 1, period))
    return {r + j * period for r in block for j in range(velocity)}


def exact_size(velocity, w):
    """The proved formula |B_v| = 2W-v."""
    return 2 * w - velocity
