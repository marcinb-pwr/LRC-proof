"""Exact labelled pairwise transition arithmetic for TASK 19."""

from collections import Counter
from math import gcd, lcm


STATES = ((0, 0), (0, 1), (1, 0), (1, 1))


def transition_classes(runner):
    """Partition one local period by (bad(z), bad(z+1))."""
    period = runner["period"]
    bad = frozenset(runner["bad_residues"])
    return {state: tuple(z for z in range(period)
                         if ((z in bad), ((z + 1) % period in bad)) ==
                         tuple(bool(x) for x in state))
            for state in STATES}


def compatible_count(left_classes, right_classes, gcd_periods):
    """Number of CRT-compatible pairs, evaluated by gcd histograms."""
    left = Counter(z % gcd_periods for z in left_classes)
    right = Counter(z % gcd_periods for z in right_classes)
    return sum(count * right.get(residue, 0)
               for residue, count in left.items())


def joint_transition_table(left, right, common_order):
    """Exact 4-by-4 labelled transition table on the common grid."""
    hi, hj = left["period"], right["period"]
    divisor = gcd(hi, hj)
    lifts = common_order // lcm(hi, hj)
    left_states, right_states = transition_classes(left), transition_classes(right)
    return {(s, t): compatible_count(left_states[s], right_states[t], divisor) * lifts
            for s in STATES for t in STATES}


def pair_safe_component_count(left, right, common_order):
    """Components of the complement of two strips from their transition table."""
    table = joint_transition_table(left, right, common_order)
    # A safe run starts at z+1 exactly when z is bad in at least one strip and
    # z+1 is safe in both.  Full/empty exceptional cases are handled directly.
    safe_size = sum(value for (s, t), value in table.items()
                    if s[0] == 0 and t[0] == 0)
    if safe_size == 0:
        return 0
    if safe_size == common_order:
        return 1
    return sum(value for (s, t), value in table.items()
               if (s[0] or t[0]) and s[1] == 0 and t[1] == 0)


def direct_joint_transition_table(left, right, common_order):
    """Independent full-period implementation used only by tests."""
    left_bad, right_bad = set(left["bad_residues"]), set(right["bad_residues"])
    out = Counter()
    for z in range(common_order):
        s = (int(z % left["period"] in left_bad),
             int((z + 1) % left["period"] in left_bad))
        t = (int(z % right["period"] in right_bad),
             int((z + 1) % right["period"] in right_bad))
        out[(s, t)] += 1
    return {key: out[key] for key in ((s, t) for s in STATES for t in STATES)}
