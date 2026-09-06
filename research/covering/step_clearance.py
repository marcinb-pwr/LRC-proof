"""Exact periodic clearance words in the integer step parameter h."""

from math import gcd, lcm

from bad_sets import parameters
from central_fringe import cyclic_distance


def runner_forbidden_residues(velocity, q, w, b_star, sign=1):
    """Compact affine modular-arc description of one runner's bad steps."""
    b = w // velocity
    modulus = q * b
    g = gcd(b_star, modulus)
    period = modulus // g
    return {"velocity": velocity, "b": b, "modulus": modulus,
            "coefficient": sign * b_star, "constant": w,
            "radius": b - 1, "period": period}


def clearance_word(raw_velocities, sign=1):
    """Return exact forbidden h classes and their common natural period."""
    velocities, q, w, modulus = parameters(tuple(raw_velocities))
    central = tuple(v for v in velocities if v % q == 0)
    if not central:
        raise ValueError("W is not covered: no q-divisible velocity")
    v_star = max(central)
    b_star = w // v_star
    runners = []
    period = 1
    for v in velocities:
        runner = runner_forbidden_residues(v, q, w, b_star, sign)
        period = lcm(period, runner["period"])
        runners.append(runner)
    # The point x=W+h*b_star itself has exact period q*v_star modulo qW.
    point_period = q * v_star
    assert point_period % period == 0
    return {"velocities": velocities, "q": q, "W": w, "M": modulus,
            "v_star": v_star, "b_star": b_star, "sign": sign,
            "word_period": period, "point_period": point_period,
            "runners": tuple(runners)}


def safe_steps(raw_velocities, stop=None, sign=1):
    """Enumerate safe h in a requested finite range, never scanning M."""
    data = clearance_word(raw_velocities, sign)
    stop = data["point_period"] if stop is None else stop
    safe = []
    for h in range(1, stop):
        if all(cyclic_distance(runner["constant"] + h * runner["coefficient"],
                               runner["modulus"]) > runner["radius"]
               for runner in data["runners"]):
            safe.append(h)
    return data, tuple(safe)


def direct_clearance(raw_velocities, h, sign=1):
    """Minimum signed clearance, for independent testing of residue classes."""
    velocities, q, w, _ = parameters(tuple(raw_velocities))
    central = tuple(v for v in velocities if v % q == 0)
    if not central:
        raise ValueError("W is not covered: no q-divisible velocity")
    b_star = w // max(central)
    x = w + sign * h * b_star
    return min(cyclic_distance(x, q * (w // v)) - (w // v - 1)
               for v in velocities)
