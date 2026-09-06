"""Runner-labelled endpoint pairs for the off-core Lonely Runner sweep."""

from collections import defaultdict

from bad_sets import parameters


def _cyclic_components(center, radius, modulus):
    lo, hi = center - radius, center + radius
    if lo < 0:
        return ((0, hi, True), (modulus + lo, modulus - 1, True))
    if hi >= modulus:
        return ((lo, modulus - 1, True), (0, hi - modulus, True))
    return ((lo, hi, False),)


def labelled_endpoint_word(raw_velocities):
    """Construct paired labelled events without iterating over residues."""
    velocities, q, w, modulus = parameters(tuple(raw_velocities))
    b_values = tuple(w // v for v in velocities)
    beta = min(b_values)
    domain_left, domain_right = beta, modulus - beta
    events = []
    pair_id = 0
    for runner, (v, b) in enumerate(zip(velocities, b_values)):
        period = q * b
        for j in range(v):
            center = j * period
            for lo, hi, wrapped in _cyclic_components(center, b - 1, modulus):
                clipped_lo = max(lo, domain_left)
                clipped_hi = min(hi, domain_right)
                if clipped_lo > clipped_hi:
                    continue
                clipped = clipped_lo != lo or clipped_hi != hi
                left = clipped_lo
                stop = clipped_hi + 1
                common = {
                    "pair": pair_id, "runner": runner, "velocity": v,
                    "b": b, "period": period, "center_index": j,
                    "center": center, "wrapped": wrapped, "clipped": clipped,
                }
                events.append({**common, "x": left, "delta": 1,
                               "mate": stop, "residue": left % period})
                events.append({**common, "x": stop, "delta": -1,
                               "mate": left, "residue": stop % period})
                pair_id += 1
    events.sort(key=lambda event: (event["x"], event["delta"], event["runner"]))
    groups = defaultdict(list)
    for event in events:
        groups[event["x"]].append(event)
    groups[domain_left]  # retain sentinels even when no event occurs there
    groups[domain_right + 1]
    word = []
    prefix = 0
    points = sorted(groups)
    for index, x in enumerate(points):
        group = tuple(groups[x])
        net = sum(event["delta"] for event in group)
        prefix += net
        next_x = points[index + 1] if index + 1 < len(points) else None
        word.append({"x": x, "delta": net, "prefix": prefix,
                     "next_x": next_x, "events": group})
    return {"velocities": velocities, "q": q, "W": w, "M": modulus,
            "beta": beta, "events": tuple(events), "word": tuple(word)}


def center_data(raw_velocities):
    """Classify coverage and nearest paired endpoints around x=W."""
    data = labelled_endpoint_word(raw_velocities)
    q, w = data["q"], data["W"]
    covering = []
    for runner, v in enumerate(data["velocities"]):
        if v % q == 0:
            b = w // v
            covering.append({"runner": runner, "velocity": v, "b": b,
                             "left": w - b + 1, "right_stop": w + b})
    data["center_covering"] = tuple(covering)
    if covering:
        innermost = min(covering, key=lambda item: item["b"])
        candidates = (innermost["left"] - 1, innermost["right_stop"])
        data["innermost_boundary_candidates"] = candidates
        data["innermost_boundary_safe"] = tuple(
            all(min((x * v) % data["M"], (-x * v) % data["M"]) * q
                >= data["M"] for v in data["velocities"])
            for x in candidates)
    else:
        data["innermost_boundary_candidates"] = ()
        data["innermost_boundary_safe"] = ()
    return data
