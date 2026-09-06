"""Reduced modular multipliers and exact strip fragmentation (TASK 18)."""

from math import gcd


def continued_fraction(numerator, denominator):
    """Euclidean continued fraction of numerator/denominator, exactly."""
    out = []
    while denominator:
        quotient, remainder = divmod(numerator, denominator)
        out.append(quotient)
        numerator, denominator = denominator, remainder
    return tuple(out)


def multiplicative_order(unit, modulus):
    """Multiplicative order of a unit; modulus one has the trivial order one."""
    if modulus == 1:
        return 1
    if gcd(unit, modulus) != 1:
        raise ValueError("multiplier is not a unit")
    value = unit % modulus
    order = 1
    while value != 1:
        value = value * unit % modulus
        order += 1
    return order


def strip_multiplier(data, runner):
    """Return the divided congruence and its exact arithmetic invariants."""
    d, w = data["gcd_direction"], data["W"]
    modulus = runner["modulus"]
    divisor = gcd(d, modulus)
    period = modulus // divisor
    multiplier = (d // divisor) % period if period > 1 else 0
    inverse = pow(multiplier, -1, period) if period > 1 else 0
    radius = runner["radius"] // divisor
    center = (-(w // divisor) * inverse) % period if period > 1 else 0
    size = min(period, 2 * radius + 1)
    return {"divisor": divisor, "period": period,
            "multiplier": multiplier, "inverse_multiplier": inverse,
            "multiplicative_order": multiplicative_order(multiplier, period),
            "continued_fraction": continued_fraction(multiplier, period),
            "reduced_radius": radius, "center": center, "size": size}


def predicted_component_count(period, size, inverse_multiplier):
    """Exact number of ordinary cyclic components of a permuted proper arc."""
    if size == 0:
        return 0
    if size == period:
        return 1
    # Consecutive z-points correspond to arc coordinates differing by the
    # original multiplier a, not its inverse.
    multiplier = pow(inverse_multiplier, -1, period)
    shift = multiplier % period
    adjacent_edges = max(0, size - shift) + max(0, size - (period - shift))
    return size - adjacent_edges


def actual_component_count(residues, period):
    """Independent component count from predecessor transitions."""
    residues = frozenset(residues)
    if not residues:
        return 0
    if len(residues) == period:
        return 1
    return sum((z - 1) % period not in residues for z in residues)
