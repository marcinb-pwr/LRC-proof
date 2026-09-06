# Full-dimensional dualization

This directory audits the full relation lattice, without decomposing by
support. The exact result is
\[
F(V)=\frac1{\det R}
\sum_{\eta\in R^*\cap[1/q,1-1/q]^N}
\prod_i \frac1{\alpha_q}
\left(1-\frac{|\eta_i-1/2|}{\alpha_q}\right),
\]
where
\[
R=\{a\in\mathbb Z^N:\sum_i a_i v_i\equiv0\pmod{qW}\}.
\]
The sum is finite and nonnegative. Strict positivity is equivalent to the
existence of an interior dual point, which is equivalent to LRC itself.

Run:

```bash
python3 research/full_dual/experiments.py
```
