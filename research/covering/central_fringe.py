"""Exact arithmetic at the two boundaries of the innermost central block."""

from bad_sets import parameters


def cyclic_distance(value, modulus):
    residue = value % modulus
    return min(residue, modulus - residue)


def boundary_profile(raw_velocities, step=1):
    """Return exact signed clearances at W +/- step*b_star.

    Clearance is distance to the closest period centre minus (b_i-1), so it
    is positive exactly at a safe integer.  No ambient-modulus scan is used.
    """
    velocities, q, w, modulus = parameters(tuple(raw_velocities))
    central = tuple(v for v in velocities if v % q == 0)
    if not central:
        return {"velocities": velocities, "q": q, "W": w, "M": modulus,
                "central": (), "v_star": None, "b_star": None,
                "minus": (), "plus": ()}
    v_star = max(central)
    b_star = w // v_star
    profiles = {}
    for sign, name in ((-1, "minus"), (1, "plus")):
        x = w + sign * step * b_star
        entries = []
        for v in velocities:
            b = w // v
            distance = cyclic_distance(x, q * b)
            entries.append({"velocity": v, "residue": v % q, "b": b,
                            "distance": distance,
                            "clearance": distance - b + 1,
                            "safe": distance >= b})
        profiles[name] = tuple(entries)
    return {"velocities": velocities, "q": q, "W": w, "M": modulus,
            "central": central, "v_star": v_star, "b_star": b_star,
            **profiles}
