"""Phase-fiber quadratic low-multiplicity certificate (TASK 24)."""

from pairwise_alignment import STATES, transition_classes
from triple_safe import lifted_size


def canonical_anchor(runners, common_order):
    """Largest lifted bad mass, with input label order as deterministic tie-break."""
    return min(range(len(runners)),
               key=lambda i: (-lifted_size(runners[i], common_order), i))


def transition_fiber_histograms(runners, common_order, anchor=None):
    """Multiplicity histograms on the four transition fibers of one label."""
    if anchor is None:
        anchor = canonical_anchor(runners, common_order)
    local = transition_classes(runners[anchor])
    bad = tuple(frozenset(r["bad_residues"]) for r in runners)
    histograms = {}
    for state in STATES:
        residues = local[state]
        histogram = [0] * (len(runners) + 1)
        for z in range(common_order):
            if z % runners[anchor]["period"] not in residues:
                continue
            multiplicity = sum(z % r["period"] in values
                               for r, values in zip(runners, bad))
            histogram[multiplicity] += 1
        histograms[state] = tuple(histogram)
    return anchor, histograms


def quadratic_value(histogram):
    """Sum (1-m)(N-m); positivity rigorously forces multiplicity zero."""
    n = len(histogram) - 1
    return sum(count * (1 - m) * (n - m)
               for m, count in enumerate(histogram))


def quadratic_from_moments(histogram):
    """Independent degree-two moment form N|E|-N M1(E)+2M2(E)."""
    n = len(histogram) - 1
    size = sum(histogram)
    first = sum(m * count for m, count in enumerate(histogram))
    second = sum((m * (m - 1) // 2) * count
                 for m, count in enumerate(histogram))
    return n * size - n * first + 2 * second


def localized_certificate(runners, common_order, anchor=None):
    """Evaluate the phase-fiber criterion chosen without inspecting safe points."""
    anchor, histograms = transition_fiber_histograms(
        runners, common_order, anchor)
    fibers = {"".join(map(str, state)): {
        "size": sum(histograms[state]),
        "histogram": histograms[state],
        "quadratic": quadratic_value(histograms[state]),
    } for state in STATES}
    return {"anchor": anchor, "fibers": fibers,
            "certified": any(x["quadratic"] > 0 for x in fibers.values())}


def canonical_anchors(runners, common_order, count):
    """Select a fixed number of largest-mass anchors before seeing safe points."""
    if count < 1 or count > len(runners):
        raise ValueError("anchor count must lie between one and runner count")
    return tuple(sorted(range(len(runners)),
                        key=lambda i: (-lifted_size(runners[i], common_order), i))[:count])


def _histograms_from_key(runners, common_order, key_function):
    bad = tuple(frozenset(r["bad_residues"]) for r in runners)
    histograms = {}
    for z in range(common_order):
        key = key_function(z)
        multiplicity = sum(z % r["period"] in values
                           for r, values in zip(runners, bad))
        histogram = histograms.setdefault(key, [0] * (len(runners) + 1))
        histogram[multiplicity] += 1
    return {key: tuple(value) for key, value in histograms.items()}


def multi_anchor_transition_certificate(runners, common_order, anchor_count):
    """Refine by the before/after states of k canonical anchors (<=4**k fibers)."""
    anchors = canonical_anchors(runners, common_order, anchor_count)
    bad = tuple(frozenset(r["bad_residues"]) for r in runners)
    histograms = _histograms_from_key(
        runners, common_order,
        lambda z: tuple((int(z % runners[i]["period"] in bad[i]),
                         int((z + 1) % runners[i]["period"] in bad[i]))
                        for i in anchors))
    values = {repr(key): quadratic_value(hist) for key, hist in histograms.items()}
    return {"anchors": anchors, "fiber_bound": 4 ** anchor_count,
            "realized_fibers": len(histograms), "quadratics": values,
            "histograms": {repr(key): hist for key, hist in histograms.items()},
            "certified": any(value > 0 for value in values.values())}


def short_word_certificate(runners, common_order, radius=1):
    """Refine by one anchor's membership word on offsets [-radius,radius]."""
    if radius < 0:
        raise ValueError("radius must be nonnegative")
    anchor = canonical_anchors(runners, common_order, 1)[0]
    residues = frozenset(runners[anchor]["bad_residues"])
    period = runners[anchor]["period"]
    histograms = _histograms_from_key(
        runners, common_order,
        lambda z: tuple(int((z + offset) % period in residues)
                        for offset in range(-radius, radius + 1)))
    values = {repr(key): quadratic_value(hist) for key, hist in histograms.items()}
    return {"anchor": anchor, "radius": radius,
            "fiber_bound": 2 ** (2 * radius + 1),
            "realized_fibers": len(histograms), "quadratics": values,
            "certified": any(value > 0 for value in values.values())}


def coarse_phase_bin_certificate(runners, common_order, phases, bins=4):
    """Partition by one anchor's reduced affine arc coordinate in fixed bins."""
    if bins < 2:
        raise ValueError("at least two bins are required")
    anchor = canonical_anchors(runners, common_order, 1)[0]
    phase = phases[anchor]
    period, multiplier, center = phase["period"], phase["multiplier"], phase["center"]
    histograms = _histograms_from_key(
        runners, common_order,
        lambda z: bins * (multiplier * (z - center) % period) // period)
    values = {str(key): quadratic_value(hist) for key, hist in histograms.items()}
    return {"anchor": anchor, "bins": bins, "fiber_bound": bins,
            "realized_fibers": len(histograms), "quadratics": values,
            "certified": any(value > 0 for value in values.values())}
