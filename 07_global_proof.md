# 07 — Global proof status

## Status: INCOMPLETE / OPEN

Documents 01 and 02 prove the exact CRT/lattice reduction, the dual
congruence description, the Poisson identity for the stated test function,
the parity phase, and the certificate
\[
F(V)>0\Longrightarrow\mathrm{LRC}.
\]

The required universal inequality \(F(V)>0\) has not been proved. The
2-adic parity theorem, relation-energy implication,
structure/pseudorandomness dichotomy, and structured-branch reduction remain
**OPEN**. Therefore this repository does not contain a proof of the Lonely
Runner Conjecture, and no such conclusion is claimed.


## Support-2 update

The support-2 sector is now reduced to the exact absolutely convergent
pairwise series described in `research/support2/theorem.md`. Its triangle
Fourier weight is the universal product
\[
g_q(r)g_q(s),\qquad
g_q(n)=\left(
\frac{\sin(\pi(q-2)n/(2q))}
{\pi(q-2)n/(2q)}
\right)^2.
\]
Finite computations show that support two can contribute negatively even when
the axis contribution is zero: for \(V=(1,2)\), the radius-8 symmetric
truncation gives approximately \(-1.736\). This is **VERIFIED
computationally**, but the rigorous tail bound does not certify its sign and
it is not a statement about the untruncated series. Universal positivity of
\(F_{\rm axis}+F_2\) is therefore still **OPEN**.

## Exact dualization of the rank-2 sector

The rank-2 support sector has an exact finite dual representation in
`research/support2_dual/theorem.md`. The squared-sinc transform is supported
on \([-\alpha_q,\alpha_q]\), where
\(\alpha_q=(q-2)/(2q)\), so the parity shift restricts the dual lattice to
\([1/q,1-1/q]^2\). Consequently the complete pair sum \(T_{ij}\) is a finite
sum of nonnegative rational terms and
\[
T_{ij}\ge0
\]
is **PROVED**. Subtracting the axis terms can still make \(F_{ij}\) negative,
as the exact example \(V=(2,3)\) gives \(F_{ij}=-8/9\). The global
support-\(\le2\) positivity question is **DISPROVED**: exact aggregation gives
\[
V=(1,2,4),\qquad F_{\rm axis}+F_2=-3/4.
\]
This is a statement about the isolated support-\(\le2\) Fourier sector, not a
counterexample to LRC, because the support-\(\ge3\) contribution is omitted.

## Full-dimensional dual audit

The full relation lattice has the exact dual
\[
R^*=\mathbb Z^N+\mathbb Z(v_1/(qW),\ldots,v_N/(qW)),
\]
and the complete Fourier certificate is a finite sum of nonnegative
triangular weights over
\[
R^*\cap[1/q,1-1/q]^N.
\]
Thus \(F(V)\ge0\) is **PROVED**. However,
\[
F(V)>0
\iff
R^*\cap(1/q,1-1/q)^N\ne\varnothing,
\]
which is equivalent to the original strict finite LRC condition. Exact tests
give \(F(V)=0\) for \(V=(1,2),(1,2,3),(1,2,4)\), while \(V=(1,2,4,8)\)
has \(F(V)=625/2187>0\). Boundary equality is therefore real and cannot be
discarded.