"""Cyclic component decomposition for TASK 17 modular strips."""


def cyclic_components(points, modulus):
    """Return disjoint cyclic components as (start, length), canonically."""
    points = frozenset(points)
    if not points:
        return ()
    if len(points) == modulus:
        return ((0, modulus),)
    starts = sorted(z for z in points if (z - 1) % modulus not in points)
    answer = []
    for start in starts:
        length = 1
        while (start + length) % modulus in points:
            length += 1
        answer.append((start, length))
    return tuple(answer)


def pair_complement_components(data, left, right):
    """Components left after two labelled bad strips are installed."""
    order = data["order"]
    runners = data["runners"]
    bad_left = frozenset(runners[left]["bad_residues"])
    bad_right = frozenset(runners[right]["bad_residues"])
    complement = (z for z in range(order)
                  if z % runners[left]["period"] not in bad_left
                  and z % runners[right]["period"] not in bad_right)
    return cyclic_components(complement, order)


def subtract_runner(components, runner, modulus):
    """Exact endpoint update after adding one modular strip."""
    bad = frozenset(runner["bad_residues"])
    survivors = set()
    for start, length in components:
        for offset in range(length):
            z = (start + offset) % modulus
            if z % runner["period"] not in bad:
                survivors.add(z)
    return cyclic_components(survivors, modulus)


def component_certificate(data, anchor=(0, 1)):
    """Apply the exact pair-component recursion, retaining all labels."""
    components = pair_complement_components(data, *anchor)
    for index, runner in enumerate(data["runners"]):
        if index not in anchor:
            components = subtract_runner(components, runner, data["order"])
    return components
