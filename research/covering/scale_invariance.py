"""Raw (non-normalizing) checks for common velocity scaling."""

from math import gcd, lcm


def lcm_many(values):
    result = 1
    for value in values:
        result = lcm(result, value)
    return result


def phase_word(velocities):
    """Integer representatives of runner phases on the exact finite grid.

    Coordinate i is stored modulo qW as x*v_i modulo qW, avoiding fractions.
    This function deliberately does not gcd-normalize its input.
    """
    velocities = tuple(velocities)
    q = len(velocities) + 1
    w = lcm_many(velocities)
    modulus = q * w
    return tuple(tuple((x * velocity) % modulus for velocity in velocities)
                 for x in range(modulus))


def scaled_phase_word_in_original_units(velocities, scale):
    """Phases of scale*V, reduced to the original qW numerator units."""
    if scale <= 0:
        raise ValueError("scale must be positive")
    velocities = tuple(velocities)
    q = len(velocities) + 1
    w = lcm_many(velocities)
    scaled_w = lcm_many(tuple(scale * v for v in velocities))
    assert scaled_w == scale * w
    # (x*scale*v)/(q*scale*W) = (x*v)/(qW).
    modulus = q * w
    return tuple(tuple((x * velocity) % modulus for velocity in velocities)
                 for x in range(scale * modulus))


def primitive_phase_period(velocities):
    """Return lcm_i(qW/v_i), equal to qW/gcd(V)."""
    velocities = tuple(velocities)
    q = len(velocities) + 1
    w = lcm_many(velocities)
    periods = tuple(q * (w // v) for v in velocities)
    return lcm_many(periods), q * w // gcd(*velocities)


def safe_indices_on_refined_time_grid(velocities, refinement):
    """Safe x on t=x/(refinement*qW), with velocities held fixed."""
    if refinement <= 0:
        raise ValueError("refinement must be positive")
    velocities = tuple(velocities)
    q = len(velocities) + 1
    denominator = refinement * q * lcm_many(velocities)
    return tuple(x for x in range(denominator)
                 if all(min((x * v) % denominator,
                            (-x * v) % denominator) * q >= denominator
                        for v in velocities))


def best_margin_on_refined_time_grid(velocities, refinement):
    """Return an exact numerator/denominator for the best LRC margin.

    The margin is min_i ||t*v_i|| - 1/q.  At t=x/(c*q*W), its common
    denominator is q*c*q*W; the returned numerator may be zero or negative.
    """
    if refinement <= 0:
        raise ValueError("refinement must be positive")
    velocities = tuple(velocities)
    q = len(velocities) + 1
    time_denominator = refinement * q * lcm_many(velocities)
    best_numerator = None
    best_index = None
    for x in range(time_denominator):
        distance = min(min((x * v) % time_denominator,
                           (-x * v) % time_denominator)
                       for v in velocities)
        numerator = q * distance - time_denominator
        if best_numerator is None or numerator > best_numerator:
            best_numerator, best_index = numerator, x
    return {"index": best_index, "time_denominator": time_denominator,
            "margin_numerator": best_numerator,
            "margin_denominator": q * time_denominator}
