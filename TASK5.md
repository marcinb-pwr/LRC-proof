# TASK 5 — Dualize the Rank-2 Support Sector

## Objective

The support-2 contribution is currently represented by

$$
F_{ij}
=
\sum_{\substack{(r,s)\in L_{ij}\\rs\neq0}}
(-1)^{r+s}g_q(r)g_q(s),
$$

where

$$
L_{ij}
=
\{(r,s)\in\mathbb Z^2:
rv_i+sv_j\equiv0\pmod{qW}\},
$$

and

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

The previous task established absolute convergence but no useful sign theorem.

The key new idea is to exploit the fact that \(g_q\) is a squared sinc function.

The main objective is:

$$
\boxed{
\text{apply Poisson summation to the rank-2 lattice sum and
derive an exact FINITE dual formula.}
}
$$

Do NOT proceed to BSG/Freiman/Gowers.

Do NOT use numerical truncation as the main method.

---

# 1. Fourier transform of \(g_q\)

Fix the convention

$$
\widehat f(x)
=
\int_{\mathbb R}
f(t)e^{-2\pi ixt}\,dt.
$$

Set

$$
\alpha=\alpha_q.
$$

Starting from

$$
g_q(n)
=
\left(
\frac{\sin(\pi\alpha n)}
{\pi\alpha n}
\right)^2,
$$

derive its exact continuous Fourier transform.

Prove the identity

$$
\widehat{g_q}(x)
=
\frac1\alpha
\left(1-\frac{|x|}{2\alpha}\right)_+
$$

or determine the exact normalization if this formula differs under the chosen
Fourier convention.

Verify the result symbolically.

Do not rely only on a known transform table.

---

# 2. Tensor-product transform

Define

$$
G_q(r,s)=g_q(r)g_q(s).
$$

Compute

$$
\widehat{G_q}(x,y).
$$

The expected form is a product of two triangular functions:

$$
\widehat{G_q}(x,y)
=
\widehat{g_q}(x)\widehat{g_q}(y).
$$

Determine its exact support:

$$
\operatorname{supp}\widehat{G_q}
=
[-2\alpha,2\alpha]^2.
$$

Since

$$
2\alpha
=
\frac{q-2}{q}
=
1-\frac2q,
$$

record this identity explicitly.

---

# 3. Encode the parity character as a frequency shift

The signed sum is

$$
\sum_{(r,s)\in L_{ij}}
G_q(r,s)(-1)^{r+s}.
$$

Write

$$
(-1)^{r+s}
=
e^{2\pi i\langle h,(r,s)\rangle},
\qquad
h=\left(\frac12,\frac12\right).
$$

Thus the full rank-2 sum becomes

$$
T_{ij}
=
\sum_{\lambda\in L_{ij}}
G_q(\lambda)
e^{2\pi i\langle h,\lambda\rangle}.
$$

Prove carefully that this is exactly the quantity used in the support-2
analysis.

---

# 4. Apply Poisson summation with the character shift

Let \(L=L_{ij}\).

Derive the exact formula

$$
T_{ij}
=
\frac1{\det L}
\sum_{\eta\in L^\ast}
\widehat{G_q}(\eta-h)
$$

or the equivalent formula dictated by the Fourier convention.

Check the sign of the shift carefully.

Do not assume the formula.

Derive it from ordinary lattice Poisson summation.

---

# 5. Crucial support reduction

Because

$$
\widehat{G_q}(x,y)
$$

has compact support

$$
[-2\alpha,2\alpha]^2,
$$

the dual Poisson sum contains only

$$
\eta\in L^\ast
$$

such that

$$
\eta-h
\in
[-2\alpha,2\alpha]^2.
$$

Since

$$
h=\left(\frac12,\frac12\right),
$$

this is equivalent coordinatewise to

$$
\eta_k
\in
\left[
\frac12-2\alpha,
\frac12+2\alpha
\right].
$$

Compute these endpoints exactly.

Determine whether the resulting interval can be simplified using

$$
2\alpha=1-\frac2q.
$$

This is a critical step.

---

# 6. Determine whether the dual sum is finite

Prove that

$$
\left(
h+[-2\alpha,2\alpha]^2
\right)
\cap L^\ast
$$

contains only finitely many points.

Give an explicit bound on the number of possible points in terms of:

* \(q\),
* \(W\),
* \(\gcd(v_i,v_j,qW)\),
* or \(\det L\).

Do not merely state "compact support implies finite".

The dual lattice is discrete, so finite intersection is automatic, but the
important question is to obtain an explicit description and count.

---

# 7. Compute \(L_{ij}^\ast\) exactly

The previous task computed \(L_{ij}\).

Now compute its dual lattice explicitly.

If

$$
L_{ij}
=
\operatorname{span}_{\mathbb Z}
\{u_1,u_2\},
$$

then

$$
L_{ij}^\ast
=
\{x\in\mathbb R^2:
\langle x,u_1\rangle,\langle x,u_2\rangle\in\mathbb Z\}.
$$

Derive an explicit basis.

Express the answer using the arithmetic data

$$
v_i,\quad v_j,\quad qW.
$$

Cross-check the result symbolically against the rank-two lattice determinant.

---

# 8. Obtain a finite exact formula

Substitute the explicit triangular transform.

The target is a formula of the form

$$
\boxed{
T_{ij}
=
\frac{1}{\det L_{ij}}
\sum_{\eta\in\mathcal Q_{ij}}
H_q(\eta_1,\eta_2),
}
$$

where

$$
\mathcal Q_{ij}
=
L_{ij}^\ast
\cap
\left(
h+[-2\alpha,2\alpha]^2
\right)
$$

is FINITE, and \(H_q\) is an explicit nonnegative function.

Write \(H_q\) explicitly.

Determine whether every term is nonnegative.

If so, this is potentially a major simplification.

---

# 9. Pay special attention to the fact that \(2\alpha<1\)

Since

$$
2\alpha=1-\frac2q<1,
$$

the relevant shifted box is narrower than length \(1\) in each coordinate.

Investigate whether this implies that the finite dual set

$$
\mathcal Q_{ij}
$$

contains at most one point in each residue class modulo \(\mathbb Z^2\).

Determine whether there can be:

* zero points,
* one point,
* multiple points.

Classify the possibilities.

---

# 10. Try to connect the finite dual condition to the original LRC geometry

The condition

$$
\eta-h\in[-2\alpha,2\alpha]^2
$$

has a strong resemblance to the original "safe box" condition.

Investigate whether the finite dual points have an interpretation directly in terms
of residue classes of \(v_i,v_j\).

Look for a reformulation involving inequalities such as

$$
\frac1q\le \{\eta_k\}\le1-\frac1q.
$$

Do not force an interpretation; derive it if it exists.

---

# 11. Exact treatment of the support decomposition

Remember:

$$
T_{ij}
=
1+T_i^{(ij)}+T_j^{(ij)}+F_{ij}.
$$

Once an exact finite formula for \(T_{ij}\) is obtained, subtract the axis
terms exactly to recover

$$
F_{ij}.
$$

Do not numerically subtract large nearly equal quantities if a symbolic formula
is possible.

---

# 12. Determine the sign of \(T_{ij}\)

Because the triangular transform is nonnegative, investigate whether

$$
T_{ij}\ge0
$$

automatically follows from the finite dual formula.

If yes, this is an important theorem.

Then determine whether this implies a useful bound on \(F_{ij}\):

$$
F_{ij}
\ge
-1-T_i^{(ij)}-T_j^{(ij)}.
$$

Compare this with the global axis contribution.

---

# 13. Stronger possibility: exact combinatorial interpretation

The finite dual formula may simplify further if the triangular weights are evaluated at rational points determined by the lattice.

Investigate whether

$$
H_q(\eta_1,\eta_2)
$$

takes only finitely many rational values.

If so, determine an exact counting formula for

$$
T_{ij}.
$$

A particularly valuable outcome would be:

$$
T_{ij}
=
\frac{\#(\text{explicit finite set})}
{\det L_{ij}}
$$

or a weighted version with simple rational weights.

---

# 14. Test important examples symbolically

Work out complete exact formulas for:

$$
V=(1,2),
$$

$$
V=(1,3),
$$

$$
V=(1,4),
$$

$$
V=(2,3),
$$

$$
V=(2,5),
$$

and several examples for \(N=3,4\).

Do not use decimal approximations unless accompanied by exact expressions.

For each example compare:

1. the original infinite rank-2 series;
2. the finite dual formula;
3. the independently computed Poisson value.

They must agree.

---

# 15. Numerical validation

After deriving the finite formula, create an independent implementation.

Do NOT reuse the original infinite-sum implementation as the only validation.

For each test case compute:

* the finite dual formula;
* a high-precision direct summation;
* a rigorous or very tight tail bound for the latter.

The values must agree to the expected precision.

---

# 16. Search for a new theorem

After obtaining the finite dual formula, investigate the strongest possible statement.

Priority order:

### A

$$
\boxed{T_{ij}\ge0}
$$

for every pair.

### B

$$
\boxed{F_{\rm axis}+F_2>0}
$$

for all \(N\ge4\).

### C

A uniform explicit lower bound

$$
T_{ij}\ge H(q,v_i,v_j).
$$

### D

A structural characterization of when

$$
T_{ij}=0.
$$

### E

A structural characterization of the finite dual set
\(\mathcal Q_{ij}\).

---

# 17. Important interpretation

Do not describe this simply as a better numerical method.

The objective is to determine whether the support-2 sector has an exact
**finite dual combinatorial structure**.

If successful, the research hierarchy changes from

$$
\text{infinite oscillatory support-2 sum}
$$

to

$$
\boxed{
\text{finite arithmetic counting problem}.
}
$$

That would be a substantial simplification.

---

# 18. Required files

Create:

```
research/support2_dual/
```

with:

```
fourier_transform.md
dual_lattice.py
exact_formula.py
experiments.py
results.json
theorem.md
README.md
```

`theorem.md` must contain:

1. exact transform of \(g_q\);
2. exact transform of \(G_q\);
3. character-shifted Poisson formula;
4. exact \(L_{ij}^\ast\);
5. finite dual set;
6. finite formula for \(T_{ij}\);
7. exact formula for \(F_{ij}\);
8. sign results;
9. counterexamples, if any;
10. explicit statement of what remains open.

---

# 19. Do not proceed to higher-order additive combinatorics

Do not move to:

* BSG,
* Freiman,
* Gowers norms,
* higher additive energy,
* generalized arithmetic progressions.

First determine whether rank-two Fourier interactions are already exactly
tractable.

The key research question is now:

$$
\boxed{
\text{Does compact Fourier support turn every support-2 contribution into
a finite arithmetic object?}
}
$$

Answer this rigorously before proceeding.

