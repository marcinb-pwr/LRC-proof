# TASK 8 — Find a Genuine New Theorem from the Finite Dual Reformulation

## Current state

The full-dimensional Poisson calculation has been rigorously established.

Let

$$
q=N+1,\qquad M=qW,
$$

and define

$$
R=
\left\{
a\in\mathbb Z^N:
\sum_i a_iv_i\equiv0\pmod M
\right\}.
$$

Its dual lattice is

$$
R^*
=
\mathbb Z^N+
\mathbb Z
\left(
\frac{v_1}{M},\ldots,\frac{v_N}{M}
\right).
$$

The Fourier certificate is

$$
F(V)
=
\frac1{\det R}
\sum_{\eta\in R^*}
\widehat G_q(\eta-h),
\qquad
h=(1/2,\ldots,1/2),
$$

with nonnegative summands.

Therefore

$$
F(V)\ge0
$$

is automatic.

Moreover,

$$
F(V)>0
\iff
R^*\cap(1/q,1-1/q)^N\neq\varnothing,
$$

and this is equivalent to the finite LRC condition.

Therefore the Poisson reformulation is currently an exact reformulation,
not yet a proof.

The purpose of this task is to extract a genuinely new theorem from the
finite cyclic structure.

Do NOT return to support-by-support decomposition.

Do NOT invoke BSG/Freiman/Gowers yet.

---

# 1. Normalize the finite dual problem

Assume

$$
\gcd(v_1,\ldots,v_N)=1.
$$

Verify that this implies

$$
\gcd(M,v_1,\ldots,v_N)=1
$$

and hence

$$
\det R=M.
$$

Then the dual classes modulo \(\mathbb Z^N\) are exactly

$$
x_k=
\left(
\left\{\frac{k v_1}{M}\right\},
\ldots,
\left\{\frac{k v_N}{M}\right\}
\right),
\qquad
k=0,\ldots,M-1.
$$

Prove this carefully.

The LRC problem is therefore:

$$
\boxed{
\exists k\in\{0,\ldots,M-1\}
\quad
\forall i,\quad
\left\|
\frac{k v_i}{M}
\right\|
\ge\frac1q.
}
$$

---

# 2. Reinterpret failure of LRC as a covering problem

Assume LRC fails.

Then for every

$$
k\in\mathbb Z/M\mathbb Z
$$

there exists at least one \(i\) such that

$$
\left\|
\frac{k v_i}{M}
\right\|
<
\frac1q
$$

or equality is handled separately according to the exact endpoint convention.

Define the bad sets

$$
B_i
=
\left\{
k\in\mathbb Z/M\mathbb Z:
\left\|
\frac{k v_i}{M}
\right\|
<
\frac1q
\right\}.
$$

Then a counterexample implies

$$
\boxed{
\mathbb Z/M\mathbb Z
=
\bigcup_{i=1}^N B_i
}
$$

for the appropriate strict/closed version.

Study the sizes and overlaps of the \(B_i\).

---

# 3. Compute the exact cardinality of each bad set

For each \(i\), determine exactly

$$
|B_i|.
$$

Because \(v_i\mid W\), there are strong arithmetic regularities.

Determine the exact formula in terms of

$$
q,\qquad
W,\qquad
v_i.
$$

Pay attention to:

* endpoint inclusion,
* whether \(q\) is odd/even,
* divisibility of \(M\) by \(qv_i\),
* whether the number of admissible residues per period is exactly
  \(2W/(qv_i)\) or a nearby integer.

Do not use asymptotic estimates if an exact count is possible.

---

# 4. First-moment covering test

Compute

$$
\sum_i |B_i|.
$$

Determine whether the trivial union bound

$$
\left|\bigcup_i B_i\right|
\le
\sum_i|B_i|
$$

is ever strong enough to prove that the bad sets cannot cover all of
\(\mathbb Z/M\mathbb Z\).

If it fails, quantify the deficit:

$$
\Delta
=
\sum_i|B_i|-M.
$$

The size of \(\Delta\) measures how much overlap is required for a hypothetical
counterexample.

This quantity should become a central parameter.

---

# 5. Inclusion-exclusion and pair intersections

Compute exactly

$$
|B_i\cap B_j|.
$$

Relate these quantities to the pairwise Fourier analysis already obtained.

Investigate whether

$$
\sum_{i<j}|B_i\cap B_j|
$$

has a simple arithmetic interpretation.

Then use

$$
\left|\bigcup_iB_i\right|
=
\sum_i|B_i|
-
\sum_{i<j}|B_i\cap B_j|
+
\sum_{i<j<k}|B_i\cap B_j\cap B_k|
-\cdots.
$$

The key question is whether a hypothetical cover forces an impossible amount
of pairwise or higher-order overlap.

---

# 6. Translate overlaps into congruence geometry

For

$$
B_i\cap B_j,
$$

the condition is

$$
\left\|
\frac{k v_i}{M}
\right\|<\frac1q
$$

and

$$
\left\|
\frac{k v_j}{M}
\right\|<\frac1q.
$$

Interpret this as a simultaneous congruence interval.

Compute the exact number of solutions using gcd/CRT methods.

Look for a formula depending on

$$
\gcd(v_i,v_j,M).
$$

Derive sharp upper and lower bounds.

---

# 7. Investigate whether the cover has a forced multiplicity

Define the covering multiplicity

$$
m(k)
=
\#\{i:k\in B_i\}.
$$

A counterexample means

$$
m(k)\ge1
\qquad
\forall k.
$$

The average multiplicity is

$$
\frac1M\sum_km(k)
=
\frac1M\sum_i|B_i|.
$$

Determine whether this average is strictly less than \(1\).

If not, determine how far above \(1\) it can be.

Then study the variance

$$
\operatorname{Var}(m)
=
\frac1M\sum_k
\left(
m(k)-\bar m
\right)^2.
$$

A potential strategy is:

$$
m(k)\ge1\;\forall k
\quad\Longrightarrow\quad
\operatorname{Var}(m)
\text{ satisfies a strong lower bound}.
$$

Try to contradict this with an arithmetic upper bound.

---

# 8. Express the second moment using Fourier analysis

Compute

$$
\sum_k m(k)^2.
$$

Expand:

$$
\sum_km(k)^2
=
\sum_i|B_i|
+
2\sum_{i<j}|B_i\cap B_j|.
$$

Investigate whether the exact finite dual formulas for the rank-2 sector
give a natural expression for this second moment.

In particular determine whether

$$
T_{ij}
$$

is a smoothed version of the normalized pair intersection count.

If possible, derive an exact comparison:

$$
T_{ij}
\approx
C_q\frac{|B_i\cap B_j|}{M}
+
E_{ij},
$$

with an explicit error.

Prefer an exact identity.

---

# 9. Search for a general moment inequality

For a covering,

$$
m(k)\ge1.
$$

Therefore for every convex function \(\Phi\),

$$
\frac1M\sum_k\Phi(m(k))
\ge
\Phi(1).
$$

Study this for:

$$
\Phi(x)=x^2,
\qquad
x^3,
\qquad
x(x-1),
$$

and other useful polynomial functions.

Determine whether the arithmetic structure of the \(B_i\) yields an upper
bound contradicting one of these moment inequalities.

This is the main new combinatorial direction.

---

# 10. Use the exact fact that there are only N = q-1 bad sets

The threshold is tied exactly to

$$
q=N+1.
$$

Exploit this numerology.

For each fixed \(k\), failure of LRC means at least one of the \(N=q-1\)
coordinates is bad.

Try to obtain inequalities that are sharp specifically for \(q-1\) sets whose
individual bad-set density is approximately \(2/q\).

This may lead to a pigeonhole or extremal-covering argument impossible for
arbitrary numbers of sets.

---

# 11. Analyze the geometry of each B_i

The set

$$
B_i
=
\left\{
k:
\left\|
\frac{k v_i}{M}
\right\|<1/q
\right\}
$$

is periodic.

Determine its period exactly.

Because

$$
v_i\mid W,
$$

the period should have a particularly simple form.

Represent \(B_i\) as a union of equally spaced intervals/residue blocks.

Study:

* spacing,
* block size,
* period,
* pairwise relative shifts.

The objective is to characterize which families of such periodic sets can cover
the entire cyclic group.

---

# 12. Reformulate as a covering by periodic Bohr sets

Write

$$
B_i
=
\{k:\|k\alpha_i\|<1/q\},
\qquad
\alpha_i=v_i/M.
$$

This is a one-dimensional Bohr set.

The problem becomes:

> Can \(q-1\) specific periodic Bohr sets, with frequencies
> \(v_i/M\), cover the entire cyclic group?

Investigate whether a known or newly provable covering theorem applies.

If a standard theorem is used, state it exactly and verify all hypotheses.

---

# 13. Search for a sharp weighted covering inequality

The natural triangular weight is

$$
h_q(x)
=
\frac1{\alpha_q}
\left(
1-\frac{|x-1/2|}{\alpha_q}
\right)_+.
$$

The Fourier analysis naturally assigns a weight to the complementary safe
region.

Define the corresponding bad weight

$$
b_q(x)=C-h_q(x)
$$

with a suitable constant \(C\).

Search for a pointwise inequality of the form

$$
\sum_i b_q(z_i(k))
<
1
$$

for at least one \(k\), or a global average inequality implying such a point.

The exact constants matter.

---

# 14. Try nonlinear averaging rather than linear averaging

Linear averaging may be too weak.

Investigate quantities such as

$$
\prod_i b_q(z_i(k)),
$$

$$
\sum_i b_q(z_i(k))^2,
$$

or

$$
\prod_i(1-\lambda h_q(z_i(k))).
$$

The desired mechanism is:

$$
\text{if every }k\text{ is bad}
\Rightarrow
\text{a pointwise inequality},
$$

then averaging over \(k\) contradicts an exact arithmetic identity.

This is potentially more powerful than the first- and second-moment methods.

---

# 15. Search for a polynomial certificate

Because

$$
m(k)\in\{1,\ldots,N\}
$$

under the counterexample assumption, search for a polynomial \(P\) such that

$$
P(m)\ge1
\qquad
(m\ge1)
$$

while the average

$$
\frac1M\sum_kP(m(k))
$$

can be computed or bounded from the arithmetic structure.

A successful certificate would give a finite-dimensional analogue of a
linear-programming bound.

---

# 16. Optimize the test function

The triangular kernel was chosen because it gives a nonnegative Fourier
transform.

Do not assume it is optimal.

Investigate whether there exists a function \(\phi\) satisfying:

1. \(\phi\ge0\),
2. support contained in the closed safe box,
3. \(\widehat\phi\ge0\),
4. \(\phi\) is strictly positive on the boundary,
5. or at least the boundary contribution can be controlled separately.

This is a functional-analytic subproblem.

If such a function exists, it may turn

$$
F(V)\ge0
$$

into

$$
F(V)>0
$$

without solving the original finite LRC problem directly.

Do not assume such a function exists.

Try first to prove impossibility under natural regularity assumptions.

---

# 17. Boundary obstruction theorem

Determine whether

$$
F(V)=0
$$

is equivalent to all contributing dual points lying on the boundary

$$
\{1/q,1-1/q\}^N.
$$

If so, classify the possible boundary points.

Determine whether the arithmetic structure of

$$
R^*
=
\mathbb Z^N+
\mathbb Z(v_1/M,\ldots,v_N/M)
$$

allows a configuration whose only points in the closed safe cube are boundary
points.

This is a finite arithmetic classification problem.

---

# 18. Compactness is NOT enough by itself

The relaxed-threshold argument shows:

If for every \(\varepsilon>0\) there exists a point with

$$
\min_i\|tv_i\|\ge1/q-\varepsilon,
$$

then LRC follows.

Therefore investigate whether the finite covering problem becomes strictly
easier at every relaxed threshold:

$$
\delta<1/q.
$$

The target theorem is:

$$
\boxed{
\forall\delta<1/q,\quad
\exists k\in\mathbb Z/M\mathbb Z:
\forall i,\quad
\delta<\{kv_i/M\}<1-\delta.
}
$$

Do not assume this. Determine the strongest universal \(\delta\) that can be
proved by covering/moment arguments.

---

# 19. Computational search for the new invariant

Create:

```
research/covering/
```

with:

```
bad_sets.py
moments.py
intersections.py
optimization.py
experiments.py
results.json
theorem.md
README.md
```

For each configuration compute:

* all \(B_i\),
* their sizes,
* all pair intersections,
* higher intersections when feasible,
* multiplicity function \(m(k)\),
* all moments

  $$
  \frac1M\sum_km(k)^r,
  $$
* weighted moments using \(h_q\),
* candidate covering inequalities.

Search especially among configurations with:

* consecutive integers,
* powers of two,
* odd integers,
* highly composite \(W\),
* large gcd relationships,
* minimal and maximal valuation diversity.

---

# 20. Required final outcomes

At completion, produce one of:

### Outcome A

A new covering theorem proving that the bad sets cannot cover the cyclic group.

### Outcome B

A new moment inequality that reduces LRC to a specific finite arithmetic
inequality.

### Outcome C

A boundary classification theorem reducing all possible \(F(V)=0\) cases to
a finite/extremal family.

### Outcome D

A new optimal-test-function theorem that gives strict positivity.

### Outcome E

A rigorous obstruction showing why the covering/moment route cannot work.

---

# 21. Important strategic rule

The project has now established that

$$
\boxed{
\text{global nonnegative Fourier certificate}
\neq
\text{proof of LRC}.
}
$$

Do not spend the next iteration deriving more equivalent Poisson formulas.

The next theorem must contain information that is NOT already equivalent to the
existence of a point in the safe cube.

The desired transition is:

$$
\boxed{
\text{exact reformulation}
\rightarrow
\text{new inequality/structure}
\rightarrow
\text{contradiction}.
}
$$

The central question is:

$$
\boxed{
\text{What additional arithmetic property of the }q-1
\text{ periodic bad sets prevents them from covering all }M\text{ residues?}
}
$$

That is the next genuine research problem.

