# Dualized rank-2 support sector

This directory implements the compact-support Fourier dual of the complete
rank-2 sum
\[
T_{ij}=\sum_{(r,s)\in L_{ij}}(-1)^{r+s}g_q(r)g_q(s).
\]
The correct continuous transform has support
\([-\alpha_q,\alpha_q]\), where \(\alpha_q=(q-2)/(2q)\). After the parity
shift by \(h=(1/2,1/2)\), the finite dual box is
\[
\left[1/q,1-1/q\right]^2.
\]

Run:

```bash
python3 research/support2_dual/experiments.py
```
