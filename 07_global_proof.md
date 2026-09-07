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
the raw scaled time grid does contain more real time coordinates, but their
simultaneous runner-phase image only repeats the same primitive bad blocks.
Thus the apparent increase in lattice points supplies no new phase-space
density or existence information. An exact
interval-sensitive component recursion is now available. However, two explicit
systems of centered cyclic arcs have identical first three intersection moments
and different coverage, proving that those aggregate moments cannot decide the
problem. The remaining canonical-grid and global LRC assertions are **OPEN**.

Keeping the velocities fixed while refining the time mesh genuinely adds new
phase vectors, but it is also **PROVED** to be existentially neutral: every
nonempty feasible component has an endpoint on the original $1/(qW)$ mesh.
Such refinement may support measure or averaging estimates, but cannot reveal
a safe configuration that the exact endpoint mesh missed.

For the margin $\Delta(V)=\max_t\min_i\|tv_i\|-1/q$, refinement does give
quantitative information: the best value on the $1/(cqW)$ mesh is within
$v_{\max}/(2cqW)$ of the continuous optimum. Positive computed margin is
therefore rigorous. A universal strictly positive margin is impossible,
because $V=(1,2)$ has optimum exactly zero; a successful margin program must
separate or classify such equality cases. More strongly, its refined-grid
optimum is exactly zero for every refinement $c\ge1$, since $t=1/3$ is always
on the mesh and no real time has positive margin.

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

## TASK 21 quantitative triple update

Triple all-safe mass is now **PROVED** to satisfy explicit one-strip and
pair-corrected lower bounds. If the three reduced gcds divide their labelled
divisors and $q\ge7$, every such triple leaves more than $L(1-6/q)$ canonical
classes safe. An exhaustive audit of 442 normalized inputs, together with
$(1,3,4,5)$ and all 19 TASK 14 obstructions, finds no zero-safe triple. This
does not control coverage by the remaining runners: the missing theorem is a
strict restricted-multiplicity bound on their incidences inside a triple-safe
set. Universal canonical-grid success and LRC remain **OPEN**.

## TASK 22 restricted-incidence update

Every incidence of a fourth bad strip inside a triple-safe set now has an
exact four-label CRT expansion, and summing over all triples gives exact
pointwise weights ${N-m(z)\choose3}$ and $m(z){N-m(z)\choose3}$. The natural
rule selecting the three largest bad masses is **DISPROVED** by
$V=(1,4,5,6,9)$, where the triple $(1,4,5)$ has safe mass 24 and the two
remaining restricted incidences are 12 and 12. The example is not an LRC
counterexample. A phase-sensitive multiplicity-surplus theorem remains
**OPEN**, as do canonical-grid success and LRC.

## TASK 23 multiplicity-surplus update

The all-triple surplus is now **PROVED** to be an explicit linear combination
of bad-strip intersection moments through order four. Its histogram form
separates a negative contribution from multiplicity-zero classes, no
contribution from multiplicity one, and positive low-overlap contributions.
Universal negativity under divisor alignment is **DISPROVED** by
$V=(1,2,3,4,5,7)$, whose histogram is $(6,136,80,6,4,4,9)$ and whose surplus
is 212 despite all reduced gcds dividing their labelled divisors. The example
has six safe classes and is not an LRC counterexample. A phase-sensitive
localized statistic remains **OPEN**, as do canonical-grid success and LRC.

## TASK 24 localized-certificate update

The largest-mass anchor's four transition fibers support a quadratic statistic
$Q(E)=\sum_{z\in E}(1-m(z))(N-m(z))$ whose positivity is **PROVED** to force a
safe class and whose computation needs shifted-arc intersections only through
order four. Universal success of this certificate is **DISPROVED** already by
$V=(1,3,4,5)$: it has four safe classes, but its four values are
$-20,0,-2,-22$. The criterion certifies 289 of 442 exhaustive canonical grids
and misses 153. A bounded-complexity phase refinement remains **OPEN**, as do
canonical-grid success and LRC.

## TASK 25 bounded-refinement update

Joint before/after states of $k$ fixed largest-mass anchors give at most
$4^k$ phase fibers, and the localized quadratic on them has an exact CRT
expansion through order $2k+2$. This is **PROVED**. The up-to-four-anchor rule
is **VERIFIED** on all 442 exhaustive inputs and 148 larger seeded inputs; it
is not a universal theorem. Four anchors are necessary for the audited TASK 23
record under this rule. Short-word and coarse-bin alternatives have explicit
small failures. Universal four-anchor success, canonical-grid success, and
LRC remain **OPEN**.

## TASK 26 four-anchor update

Every four-anchor fiber quadratic now has a direct expansion in shifted
centered-arc CRT intersections through order ten. Universal positivity is
**DISPROVED** already by the seven-label TASK 14 obstruction
$(1,5,6,7,8,11,13)$: it has 14 safe canonical classes, but the maximum
quadratic among its 40 realized four-anchor fibers is zero. Five anchors
certify this example, so the open issue is whether any
absolute anchor bound exists. Canonical-grid success and LRC remain **OPEN**.
