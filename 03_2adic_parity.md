# 03 — 2-adic parity

## Claim status: the naive layer-separation claim is DISPROVED

Write \(v_i=2^{s_i}u_i\), with \(u_i\) odd, and let
\(I_s=\{i:s_i=s\}\). For a dual relation \(a\), the exact congruence is
\[
\sum_i a_i2^{s_i}u_i\equiv0\pmod{qW}.                           \tag{1}
\]
Reducing (1) modulo \(2^k\) gives the exact layer equations
\[
\sum_{s<k}2^s B_s(a)\equiv0\pmod{2^k},\qquad
B_s(a)=\sum_{i\in I_s}a_i u_i.                                  \tag{2}
\]
If \(C_s=\sum_{r<s}2^rB_r(a)/2^s\) is an integer at a stage where the
previous equations hold, the next divisibility condition is
\[
B_s(a)+C_s\equiv0\pmod2,
\]
and the next carry is
\[
C_{s+1}=(B_s(a)+C_s)/2.                                         \tag{3}
\]
These are bookkeeping identities, not a parity theorem.

The proposed statement that every odd \(\sum_i a_i\) must involve at least
two valuation layers is false. For
\[
V=(1,3),\quad q=3,\quad W=3,\quad a=(0,3),
\]
we have
\[
\sum_i a_i v_i=9\equiv0\pmod9,\qquad \sum_i a_i=3\equiv1\pmod2,
\]
but the support lies entirely in the single layer \(s=0\). This is recorded
with computational metadata in `research/2adic/results.json`.

No general lower bound on carries, support, or \(\ell^1\)-length has been
proved. Any corrected theorem must retain the odd part of \(qW\), coefficient
size, or the actual Fourier weight.
