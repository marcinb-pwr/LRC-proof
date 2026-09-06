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
## TASK 15 covering update

The central-covering route now has an exact canonical two-label quotient. Its
period lattice has Smith form $\operatorname{diag}(1,q\operatorname{lcm}(v_*,v^\dagger))$;
therefore the nominal two-dimensional torus collapses to a cyclic lcm grid.
Exact modular-strip, pairwise-gcd intersection, spanning-tree union, and
Fourier formulae are **PROVED** in `research/covering/theorem.md`.

All 19 one-direction obstructions from TASK 14 acquire a safe point after the
canonical second direction, and an exhaustive 18,969-input audit through
velocity 15 finds no two-label obstruction (**VERIFIED**, not a theorem).
Universal success of this grid remains **OPEN**. Consequently the status of
LRC itself is unchanged: the repository provides exact reductions and new
infinite certified families, but neither universal strict Fourier positivity
nor a universal covering argument.

## TASK 16 certificate update

The optimal pairwise spanning-tree certificate and exact arbitrary labelled
intersection formula are now **PROVED**, together with a third-order
Bonferroni certificate. They do not settle the canonical two-label grid:
$(1,3,4,5)$ has safe classes but defeats both low-order bounds. Exhaustive
verification through velocity 12 and a seeded sample through velocity 40 find
no covered grid, but universal grid success and LRC remain **OPEN**.

## TASK 17 scaling and component update

Common multiplication of every velocity is **PROVED** to be exactly neutral:
it only repeats the same primitive bad blocks, so the apparent increase in
lattice points supplies no new density or existence information. An exact
interval-sensitive component recursion is now available. However, two explicit
systems of centered cyclic arcs have identical first three intersection moments
and different coverage, proving that those aggregate moments cannot decide the
problem. The remaining canonical-grid and global LRC assertions are **OPEN**.

## TASK 18 fragmentation update

Every bad strip on the canonical grid is now **PROVED** to be an arithmetic
progression obtained from one centered arc by an explicit reduced unit. Its
ordinary cyclic component count has an exact formula in terms of that unit,
the reduced radius, and the period. Tests verify the formula across required
families within the central-cover hypothesis and find no covered grid in a
seeded audit through velocity 50. Cross-label alignment of these fragmented
strips, universal canonical-grid success, and LRC remain **OPEN**.

## TASK 19 pairwise-alignment update

Exact labelled $4\times4$ joint transition tables for every pair of bad strips
are now **PROVED**, together with a formula for the number of components left
by a pair. This strictly refines pair-intersection counts. Aggregate pairwise
transition summaries are **DISPROVED** as a coverage criterion by two centered-
arc systems on $\mathbb Z/8\mathbb Z$ with identical summaries and different
coverage. Whether complete labelled pair data plus LRC divisor phases forces a
gap remains **OPEN**, as do the canonical-grid assertion and LRC.

## TASK 20 triple-alignment update

The full labelled $8\times8$ transition table for every triple and the exact
change in safe-component count after inserting a third strip are **PROVED**.
The labelled phase records reconstruct all strips and hence all higher tables,
but this finite reconstruction does not provide a uniform inequality forcing a
gap. Tests cover the required applicable families and all TASK 14 obstructions;
no triple covers the canonical grid there. Universal grid success and LRC
remain **OPEN**.
