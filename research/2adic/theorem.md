# 2-adic parity result

## Outcome B — the naive theorem is disproved

The candidate statement

> Every odd dual relation must involve at least two distinct 2-adic
> valuation layers

is false.

Take
\[
N=2,\qquad q=3,\qquad V=(1,3),\qquad W=3.
\]
Then
\[
qW=9,\qquad (v_1,v_2)=(1,3),
\]
and the coefficient vector
\[
a=(0,3)
\]
satisfies
\[
0\cdot1+3\cdot3=9\equiv0\pmod9.
\]
Its coefficient sum is \(3\), which is odd, while both \(v_1\) and \(v_2\)
have 2-adic valuation \(0\). The relation is supported on only one
valuation layer. Its dual point is
\[
\xi_a=(0,1),
\]
so it is a genuine nonzero point of the full dual lattice.

This is not an artifact that can be removed by quotienting coefficients:
the map \(a\mapsto(a_i/(qb_i))_i\) is injective, and shifting a coefficient
by \(qb_i\) changes the dual point. Moreover, when \(qb_i\) is odd, the
parity of \(\sum_i a_i\) changes under such a shift. Therefore parity,
\(\ell^1\)-norm, and carry statistics are representative-dependent on a
finite quotient and must be interpreted on the full relation lattice when
used in Fourier analysis.

## What remains valid

For a relation \(a\), write
\[
v_i=2^{s_i}u_i,\qquad u_i\text{ odd},\qquad
B_s(a)=\sum_{i:s_i=s}a_i u_i.
\]
If the congruence is divisible by \(2^k\), the exact successive equations
are
\[
B_0\equiv0\pmod2,\qquad
C_{s+1}=\frac{B_s+C_s}{2},\qquad C_0=0,
\]
with \(B_s+C_s\) even at every step. These equations are proved by
successively dividing the congruence by \(2\).

They do not imply a layer-interaction theorem. The strongest result from
this task is therefore the explicit counterexample and the corrected
warning about quotient-dependent statistics. A useful replacement theorem,
if one exists, must include the odd part of the modulus \(qW\), coefficient
size, or a Fourier-weight-dependent complexity.
