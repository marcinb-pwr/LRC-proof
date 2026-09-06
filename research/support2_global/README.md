# Global aggregation of the rank-2 dual sector

This directory implements the exact \(k\)-parameter aggregation of the finite
dual formulas. All congruences and weights are evaluated with exact integer
and rational arithmetic.

For
\[
z_i(k)=\left\{\frac{k v_i}{qW}\right\},
\]
define
\[
h_q(z)=\frac1{\alpha_q}
\left(1-\frac{|z-1/2|}{\alpha_q}\right)_+.
\]
Then
\[
\sum_{i<j}T_{ij}
=\frac1{qW}\sum_{k=0}^{qW-1}
\sum_{i<j}h_q(z_i(k))h_q(z_j(k)).
\]

Run:

```bash
python3 research/support2_global/experiments.py
```
