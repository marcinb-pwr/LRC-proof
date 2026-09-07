"""Independent validation of the TASK 26 counterexample."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from localized_certificate import multi_anchor_transition_certificate, quadratic_value
from task26_experiments import COUNTEREXAMPLE
from two_direction import safe_classes


def main():
    data, safe = safe_classes(COUNTEREXAMPLE)
    result = multi_anchor_transition_certificate(data["runners"], data["order"], 4)
    assert safe
    assert not result["certified"]
    assert max(result["quadratics"].values()) == 0
    assert result["realized_fibers"] == len(result["histograms"])
    assert sum(sum(hist) for hist in result["histograms"].values()) == data["order"]
    for key, histogram in result["histograms"].items():
        assert quadratic_value(histogram) == result["quadratics"][key]
    # Directly verify every stored safe class has multiplicity zero.
    for z in safe:
        assert all(z % runner["period"] not in runner["bad_residues"]
                   for runner in data["runners"])
    print("four-anchor counterexample checks passed")


if __name__ == "__main__":
    main()
