# Support-2 dual sector

This directory studies dual relations with exactly two nonzero
coordinates. The full sector \(D_{ij}\) is a rank-two lattice; therefore no
single integer parameter can enumerate all of it. A canonical finite
enumeration uses
\[
0\le r<qb_i,\qquad 0\le s<qb_j
\]
and tests the defining congruence. Short signed relations are then searched
in a symmetric box separately.

Run:

```bash
python3 research/support2/experiments.py
```

All congruences and minimum-frequency calculations use integer arithmetic.
Floating point is used only for the triangle Fourier weights.
