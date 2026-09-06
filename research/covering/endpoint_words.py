"""Ordered off-core endpoint words, using no scan of the ambient modulus."""

from collections import Counter, defaultdict

from bad_sets import parameters
from localization import clipped_off_core_blocks


def endpoint_word(raw_velocities):
    """Return the coalesced half-open event word and its prefix segments.

    The two zero-delta sentinels delimit D.  An item (x, delta) means that
    the multiplicity changes by delta immediately before integer x.
    """
    velocities, q, w, modulus = parameters(tuple(raw_velocities))
    b_values = tuple(w // v for v in velocities)
    beta = min(b_values)
    left, stop = beta, modulus - beta + 1
    events = defaultdict(int)
    events[left] += 0
    events[stop] += 0
    labelled = []
    for index, v in enumerate(velocities):
        for lo, hi in clipped_off_core_blocks(v, q, w, beta):
            events[lo] += 1
            events[hi + 1] -= 1
            labelled.append((lo, 1, index, hi + 1))
            labelled.append((hi + 1, -1, index, lo))
    word = tuple(sorted(events.items()))
    prefix = 0
    segments = []
    for (x, delta), (y, _) in zip(word, word[1:]):
        prefix += delta
        if x < y:
            segments.append((x, y - 1, prefix))
    assert prefix + word[-1][1] == 0
    return {
        "velocities": velocities, "q": q, "W": w, "M": modulus,
        "beta": beta, "word": word, "labelled_events": tuple(labelled),
        "segments": tuple(segments),
    }


def word_statistics(raw_velocities):
    data = endpoint_word(raw_velocities)
    word = data["word"]
    interior = tuple((x, d) for x, d in word if d)
    gaps = tuple(word[i + 1][0] - word[i][0]
                 for i in range(len(word) - 1))
    zero_segments = tuple((a, b) for a, b, m in data["segments"] if m == 0)
    signs = tuple(1 if d > 0 else -1 for _, d in interior)
    data.update({
        "zero_segments": zero_segments,
        "zero_segment_count": len(zero_segments),
        "delta_histogram": tuple(sorted(Counter(d for _, d in interior).items())),
        "gap_multiset": tuple(sorted(gaps)),
        "strictly_alternating": all(a != b for a, b in zip(signs, signs[1:])),
        "unit_changes": all(abs(d) == 1 for _, d in interior),
        "minimum_gap_at_least_beta": all(g >= data["beta"] for g in gaps),
    })
    return data
