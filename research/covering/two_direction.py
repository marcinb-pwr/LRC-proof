"""Exact arithmetic for the TASK 15 two-direction audit."""

from math import gcd, lcm

from bad_sets import parameters
from central_fringe import cyclic_distance
from step_clearance import clearance_word


def _bad(runner, h):
    return cyclic_distance(runner["constant"] + h * runner["coefficient"],
                           runner["modulus"]) <= runner["radius"]


def canonical_second_direction(raw_velocities):
    """Choose the least active divisor (equivalently largest active velocity).

    Activity is measured on the original one-direction word.  The central
    label v_star is excluded.  This rule sees no two-direction safe point.
    """
    word = clearance_word(raw_velocities)
    active = []
    for runner in word["runners"]:
        if runner["velocity"] == word["v_star"]:
            continue
        if any(_bad(runner, h) for h in range(word["point_period"])):
            active.append(runner)
    if not active:
        raise ValueError("the one-direction cover has no noncentral coverer")
    # Since b_i=W/v_i, this is the numerically least labelled divisor b_i.
    chosen = min(active, key=lambda r: (r["b"], -r["velocity"]))
    return word, chosen


def two_direction_torus(raw_velocities):
    """Return the exact quotient and modular-strip data, without scanning qW."""
    velocities, q, w, modulus = parameters(tuple(raw_velocities))
    word, chosen = canonical_second_direction(velocities)
    b_star, b_dagger = word["b_star"], chosen["b"]
    d = gcd(b_star, b_dagger)
    order = modulus // d
    ell = lcm(word["v_star"], chosen["velocity"])
    assert d == w // ell and order == q * ell
    runners = []
    for v in velocities:
        b = w // v
        m = q * b
        g = gcd(d, m)
        period = m // g
        residues = tuple(z for z in range(period)
                         if cyclic_distance(w + z * d, m) <= b - 1)
        runners.append({"velocity": v, "b": b, "modulus": m,
                        "radius": b - 1, "period": period,
                        "bad_residues": residues})
    return {"velocities": velocities, "q": q, "W": w, "M": modulus,
            "v_star": word["v_star"], "v_dagger": chosen["velocity"],
            "b_star": b_star, "b_dagger": b_dagger, "gcd_direction": d,
            "order": order, "snf": (1, order), "runners": tuple(runners)}


def safe_classes(raw_velocities):
    """Safe classes z for x=W+z*gcd(b_star,b_dagger)."""
    data = two_direction_torus(raw_velocities)
    bad_sets = tuple(frozenset(r["bad_residues"]) for r in data["runners"])
    safe = tuple(z for z in range(data["order"])
                 if all(z % r["period"] not in bad
                        for r, bad in zip(data["runners"], bad_sets)))
    return data, safe


def pair_intersection_count(left, right, common_order):
    """Exact lifted intersection size, retaining the pairwise gcd."""
    hi, hj = left["period"], right["period"]
    g = gcd(hi, hj)
    compatible = sum(a % g == b % g for a in left["bad_residues"]
                     for b in right["bad_residues"])
    return compatible * (common_order // lcm(hi, hj))
