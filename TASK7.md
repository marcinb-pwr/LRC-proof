# TASK 7 — Full-Dimensional Dualization

## Objective

The rank-2 support sector has been exactly dualized.

The following phenomenon now requires an immediate full-dimensional audit.

For a relation lattice of the form

$$
D_S
=
\left\{
a\in\mathbb Z^S:
\sum_{i\in S}a_iv_i\equiv0\pmod M
\right\},
\qquad M=qW,
$$

the rank-2 analysis suggests that the signed sinc-squared sum

$$
T_S
=
\sum_{a\in D_S}
(-1)^{\sum_{i\in S}a_i}
\prod_{i\in S}g_q(a_i)
$$

may admit a finite nonnegative dual representation.

The purpose of this task is NOT to assume that this generalization is correct.

The purpose is to determine rigorously whether the same construction works in arbitrary
dimension.

This is potentially the most important step of the entire project.

---

# 1. Start from the FULL relation lattice

Do not begin with support 3.

Set

$$
D=
\left\{
a\in\mathbb Z^N:
\sum_{i=1}^N a_iv_i\equiv0\pmod M
\right\},
\qquad
M=qW.
$$

This is a full-rank sublattice of \(\mathbb Z^N\).

The original Fourier certificate is

$$
F(V)
=
\sum_{a\in D}
(-1)^{\sum_i a_i}
\prod_{i=1}^N g_q(a_i),
$$

where

$$
g_q(n)
=
\left(
\frac{\sin(\pi\alpha_q n)}
{\pi\alpha_q n}
\right)^2,
\qquad
\alpha_q=\frac{q-2}{2q}.
$$

First independently verify this identity from the exact Poisson formulation.

---

# 2. Compute the full dual lattice

Prove or disprove

$$
\boxed{
D^\ast
=
\mathbb Z^N+
\mathbb Z
\left(
\frac{v_1}{M},
\ldots,
\frac{v_N}{M}
\right).
}
$$

Do not infer this from the rank-2 case.

Prove both inclusions.

Compute

$$
\det D
$$

and independently verify

$$
[D^\ast:\mathbb Z^N]=\det D.
$$

Determine whether

$$
\det D=
\frac{M}{\gcd(v_1,\ldots,v_N,M)}.
$$

If this formula is false, derive the correct one.

---

# 3. Apply N-dimensional Poisson summation

Define

$$
G_q(x_1,\ldots,x_N)
=
\prod_{i=1}^N g_q(x_i).
$$

Define

$$
h=\left(\frac12,\ldots,\frac12\right).
$$

Since

$$
(-1)^{\sum_i a_i}
=
e^{2\pi i\langle h,a\rangle},
$$

the full Fourier certificate is

$$
F(V)
=
\sum_{a\in D}
G_q(a)e^{2\pi i\langle h,a\rangle}.
$$

Apply lattice Poisson summation directly to this expression.

Derive the exact formula

$$
F(V)
=
\frac1{\det D}
\sum_{\eta\in D^\ast}
\widehat G_q(\eta-h),
$$

or determine the correct normalization/sign if this formula is not exact.

This formula must be independently checked.

---

# 4. Compute the continuous Fourier transform

Prove

$$
\widehat g_q(x)
=
\frac1{\alpha_q}
\left(
1-\frac{|x|}{\alpha_q}
\right)_+.
$$

Then prove

$$
\widehat G_q(x_1,\ldots,x_N)
=
\prod_{i=1}^N
\frac1{\alpha_q}
\left(
1-\frac{|x_i|}{\alpha_q}
\right)_+.
$$

Hence

$$
\operatorname{supp}\widehat G_q
=
[-\alpha_q,\alpha_q]^N.
$$

Because

$$
\alpha_q
=
\frac12-\frac1q,
$$

show that

$$
h+[-\alpha_q,\alpha_q]
=
\left[\frac1q,1-\frac1q\right].
$$

Therefore the Poisson sum reduces formally to

$$
\boxed{
F(V)
=
\frac1{\det D}
\sum_{\eta\in
D^\ast\cap[1/q,1-1/q]^N}
\widehat G_q(\eta-h).
}
$$

---

# 5. CRITICAL AUDIT — try to break the argument

This is the most important requirement of the task.

The conclusion

$$
F(V)\ge0
$$

would appear to follow immediately.

Before accepting it, attempt aggressively to find the flaw.

Check independently:

1. Is \(D\) really the lattice appearing in the original Poisson sum?
2. Is the parameter \(a\) exactly the original dual coordinate?
3. Is \(G_q(a)\) exactly \(\widehat\phi(\xi_a)\)?
4. Is the map between the original dual lattice and \(D\) genuinely bijective?
5. Are all determinant factors correct?
6. Is the character exactly

   $$
   (-1)^{\sum_i a_i}?
   $$
7. Is Poisson being applied to the correct lattice?
8. Are the regularity and summability hypotheses satisfied?
9. Does the continuous transform have exactly the stated normalization?
10. Are there hidden boundary terms?
11. Does the finite-support argument remain valid in dimension \(N\)?
12. Does the full-dimensional formula reproduce direct calculations for small
    \(N\)?

Do not accept the apparent positivity until all of these have passed.

---

# 6. If positivity survives, prove it formally

If the audit succeeds, establish:

## Theorem 7.1 — Nonnegative full Fourier certificate

For every configuration \(V\),

$$
\boxed{
F(V)\ge0.
}
$$

This theorem must be proved independently of LRC.

Do not interpret nonnegativity as a proof of LRC.

Immediately compare this with direct calculations for:

$$
N=2,3,4.
$$

---

# 7. Investigate strict positivity

The entire problem then becomes:

$$
F(V)>0?
$$

Since every summand in the finite dual expression is nonnegative,

$$
F(V)>0
$$

is equivalent to the existence of

$$
\eta\in D^\ast
$$

such that

$$
\eta\in
(1/q,1-1/q)^N.
$$

Carefully distinguish:

$$
[1/q,1-1/q]^N
$$

from

$$
(1/q,1-1/q)^N.
$$

The triangular weight vanishes on the boundary.

Prove the exact equivalence

$$
\boxed{
F(V)>0
\iff
D^\ast
\cap
(1/q,1-1/q)^N
\neq\varnothing.
}
$$

Then determine what

$$
F(V)=0
$$

means geometrically.

---

# 8. Compare the strict positivity condition with LRC

The original lattice reduction gives

$$
\text{LRC}
\iff
(\Lambda-c)\cap K\ne\varnothing.
$$

The new dual formulation may give

$$
F(V)>0
\iff
D^\ast
\cap
(1/q,1-1/q)^N
\ne\varnothing.
$$

Determine exactly how these two geometric statements are related.

In particular investigate:

* whether the strict-interior condition is equivalent to an LRC statement
  with a slightly stronger threshold;
* whether boundary-only LRC solutions are possible;
* whether compactness can be used by taking a sequence of relaxed thresholds;
* whether the finite arithmetic nature of the lattices forces an interior
  solution whenever an endpoint solution exists.

Do not assume any of these.

---

# 9. Introduce a relaxed threshold

For

$$
0<\varepsilon<1/q,
$$

define

$$
\delta_\varepsilon
=
\frac1q-\varepsilon.
$$

Repeat the construction with

$$
\alpha_\varepsilon
=
\frac12-\delta_\varepsilon.
$$

The shifted Fourier-support interval becomes

$$
[\delta_\varepsilon,1-\delta_\varepsilon].
$$

Determine whether one can prove

$$
F_\varepsilon(V)>0
$$

for every \(\varepsilon>0\).

If so, compactness of \(\mathbb R/\mathbb Z\) may imply the original LRC threshold by taking a convergent subsequence of corresponding times.

This is a key possible route.

Do not assume positivity for relaxed thresholds; prove or disprove it.

---

# 10. Search for a purely finite dual criterion

Because

$$
D^\ast
=
\mathbb Z^N+
\mathbb Z(v_1/M,\ldots,v_N/M),
$$

the existence of an interior point is equivalent to the existence of an integer
\(k\) satisfying

$$
\frac1q
<
\left\{
\frac{k v_i}{M}
\right\}
<
1-\frac1q
\qquad
\forall i.
$$

Investigate this condition carefully.

Compare it with the original discretized LRC condition.

Determine whether the dual criterion is actually equivalent to a known finite
version of LRC.

---

# 11. Important possibility: self-duality

Investigate whether the full dual condition is simply the original LRC
condition after replacing the original configuration by another finite
configuration.

In particular, study the map

$$
V
\longrightarrow
\left(
\frac{v_1}{M},\ldots,\frac{v_N}{M}
\right).
$$

Determine whether the dual residue problem has the same combinatorial
difficulty as the original problem.

If the dual problem is equivalent to LRC itself, document this explicitly.

If it is genuinely different, identify the distinction.

---

# 12. Boundary analysis

A potential obstruction is:

$$
D^\ast
\cap
[1/q,1-1/q]^N
\neq\varnothing
$$

but

$$
D^\ast
\cap
(1/q,1-1/q)^N
=
\varnothing.
$$

Construct explicit examples if they exist.

Determine whether such examples satisfy LRC via boundary points.

This distinction is critical.

---

# 13. Test families

Test the full formula on:

$$
V=(1,2),
$$

$$
V=(1,3),
$$

$$
V=(1,2,3),
$$

$$
V=(1,2,4),
$$

$$
V=(1,2,4,8),
$$

$$
V=(1,2,4,8,16),
$$

and many random configurations.

For each configuration independently compute:

1. the original infinite Fourier relation sum;
2. the finite dual sum;
3. direct numerical minimization of

   $$
   \min_i\|tv_i\|;
   $$
4. the existence/nonexistence of an interior dual point.

All exact arithmetic should be performed symbolically/integer-wise whenever
possible.

---

# 14. If full positivity is false, find the exact flaw

If the apparent proof of

$$
F(V)\ge0
$$

fails, do not merely record "generalization failed".

Identify the exact mathematical reason.

Possible failure modes include:

* incorrect identification of \(D^\ast\);
* non-bijective parameterization;
* incorrect Fourier normalization;
* application of Poisson to the wrong object;
* boundary/distribution issue;
* mismatch between \(G_q\) and the actual dual weight;
* another hidden structural assumption.

Produce the smallest explicit counterexample to the failed step.

---

# 15. If nonnegativity is true, investigate why this does NOT immediately prove LRC

This question is mandatory.

Assume the theorem

$$
F(V)\ge0
$$

has been established.

Explain rigorously why this does or does not already imply LRC.

In particular determine whether:

$$
F(V)=0
$$

can occur for an actual LRC configuration, and whether every LRC configuration
must instead satisfy

$$
F(V)>0.
$$

Do not use informal arguments.

---

# 16. Potential endpoint argument

Investigate whether the following strategy is valid:

1. For every \(\varepsilon>0\), prove LRC with threshold

   $$
   1/q-\varepsilon.
   $$
2. Obtain \(t_\varepsilon\) for each \(\varepsilon\).
3. Use compactness of \(\mathbb R/\mathbb Z\) to choose

   $$
   t_{\varepsilon_j}\to t.
   $$
4. Show

   $$
   \|t v_i\|\ge1/q
   $$

   for every \(i\).

If this works, the remaining theorem required is only the strict positivity of
the relaxed certificate.

Formulate this endpoint argument as a standalone lemma.

---

# 17. Search for the strongest relaxed-threshold theorem

Define the relaxed problem:

$$
\exists t:
\min_i\|tv_i\|
\ge
\frac1q-\varepsilon.
$$

Determine the largest universal class of \(\varepsilon\) for which the dual
finite-sum argument guarantees a positive certificate.

Possible useful outcomes:

### A

$$
F_\varepsilon(V)>0
\quad\forall\varepsilon>0.
$$

This could potentially lead directly to LRC.

### B

There exists an explicit

$$
\varepsilon_N>0
$$

for which the relaxed statement is provable.

### C

The finite dual set can be shown nonempty by a new arithmetic theorem.

### D

A counterexample to strict positivity is found.

---

# 18. Do NOT proceed to support 3

This task supersedes the previous support-by-support hierarchy.

Do not begin a general support-3 program until the full-dimensional calculation has
been audited.

The current priority is:

$$
\boxed{
\text{full relation lattice}
\rightarrow
\text{full dual lattice}
\rightarrow
\text{finite nonnegative certificate}
\rightarrow
\text{strict positivity/boundary problem}.
}
$$

If this works, support decomposition may no longer be necessary.

---

# 19. Required files

Create:

```
research/full_dual/
```

with:

```
full_lattice.py
full_dual.py
poisson_certificate.py
relaxed_threshold.py
experiments.py
results.json
theorem.md
README.md
```

---

# 20. Required final theorem document

`research/full_dual/theorem.md` must contain one of the following outcomes.

## Outcome A — Full nonnegative dual theorem proved

Prove

$$
F(V)\ge0
$$

for all \(V\).

Then identify the exact strict-positivity obstruction.

## Outcome B — Apparent full positivity argument disproved

Give the exact failed step and the smallest counterexample.

## Outcome C — Full positivity plus relaxed-threshold theorem

Prove enough strict positivity to imply LRC by compactness.

## Outcome D — Full positivity reduces exactly to an equivalent finite form of LRC

Document the equivalence precisely.

## Outcome E — Another obstruction discovered

State it as a new standalone mathematical problem.

---

# 21. Absolute priority

The central question of this task is:

$$
\boxed{
\text{Does the same compact-support Poisson mechanism that solved the
rank-2 complete sum actually work in dimension }N?
}
$$

Do not assume that the answer is yes.

But do not abandon it merely because it would have major consequences.

Audit it as if it were a potentially publishable theorem.

If it survives, the problem has been reduced from an oscillatory Fourier sum to a
finite strict-positivity problem on a dual lattice.

That would be the primary result of this task.

