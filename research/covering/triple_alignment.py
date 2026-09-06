"""Exact three-label transition and gap-destruction arithmetic (TASK 20)."""

from itertools import product
from math import lcm

from pairwise_alignment import STATES, transition_classes


TRIPLE_STATES = tuple(product((0, 1), repeat=3))


def triple_transition_table(runners, common_order):
    """Return the exact 8-by-8 transition table for three labelled strips."""
    if len(runners) != 3:
        raise ValueError("exactly three runners are required")
    periods = tuple(runner["period"] for runner in runners)
    joint_period = lcm(*periods)
    if common_order % joint_period:
        raise ValueError("runner periods must divide the common order")
    classes = tuple({state: frozenset(values)
                     for state, values in transition_classes(runner).items()}
                    for runner in runners)
    table = {(before, after): 0
             for before in TRIPLE_STATES for after in TRIPLE_STATES}
    for z in range(joint_period):
        local = []
        for period, partition in zip(periods, classes):
            residue = z % period
            local.append(next(state for state in STATES
                              if residue in partition[state]))
        before = tuple(state[0] for state in local)
        after = tuple(state[1] for state in local)
        table[(before, after)] += common_order // joint_period
    return table


def safe_component_count(table, common_order):
    """Count safe cyclic components from an 8-by-8 transition table."""
    zero = (0, 0, 0)
    safe_size = sum(value for (before, _), value in table.items()
                    if before == zero)
    if safe_size == 0:
        return 0
    if safe_size == common_order:
        return 1
    return sum(value for (before, after), value in table.items()
               if before != zero and after == zero)


def pair_to_triple_component_change(runners, common_order):
    """Exact change when the third strip is inserted after the first pair."""
    from pairwise_alignment import pair_safe_component_count

    pair_components = pair_safe_component_count(runners[0], runners[1], common_order)
    table = triple_transition_table(runners, common_order)
    triple_components = safe_component_count(table, common_order)
    return {"pair_components": pair_components,
            "triple_components": triple_components,
            "component_change": triple_components - pair_components,
            "table": table}


def direct_triple_transition_table(runners, common_order):
    """Independent common-period implementation for tests."""
    bad = tuple(frozenset(runner["bad_residues"]) for runner in runners)
    table = {(before, after): 0
             for before in TRIPLE_STATES for after in TRIPLE_STATES}
    for z in range(common_order):
        before = tuple(int(z % runner["period"] in values)
                       for runner, values in zip(runners, bad))
        after = tuple(int((z + 1) % runner["period"] in values)
                      for runner, values in zip(runners, bad))
        table[(before, after)] += 1
    return table
