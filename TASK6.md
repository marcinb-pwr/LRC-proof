# TASK 6 — Global Aggregation of the Exact Pair Dual Formula

## Objective

The rank-2 support sector has now been dualized exactly.

For every pair \(i<j\),

$$
T_{ij}
=
\sum_{(r,s)\in L_{ij}}
(-1)^{r+s}g_q(r)g_q(s)
$$

has the finite nonnegative representation

$$
T_{ij}
=
\frac1{\det L_{ij}}
\sum_{\eta\in\mathcal Q_{ij}}
\widehat G_q(\eta-h),
$$

where

$$
\mathcal Q_{ij}
=
L_{ij}^*
\cap
[1/q,1-1/q]^2,
$$

$$
L_{ij}^*
=
\mathbb Z^2+
\mathbb Z
\left(
\frac{v_i}{qW},
\frac{v_j}{qW}
\right),
$$

and

$$
h=(1/2,1/2).
$$

Thus

$$
T_{ij}\ge0
$$

is proved, but the exact-support contribution

$$
F_{ij}
$$

may be negative after subtracting the axis terms.

The next objective is to understand the finite dual set
\(\mathcal Q_{ij}\) arithmetically and then determine whether the **aggregate
support-\(\le2\) contribution**

$$
F_{\le2}(V)
=
F_{\rm axis}(V)+F_2(V)
$$

can be controlled globally for \(N\ge4\).

Do not move to support 3 or to general additive combinatorics until this task is
completed.

---

# 1. Derive the canonical one-parameter finite formula

Start from

$$
L_{ij}^*
=
\mathbb Z^2+
\mathbb Z
\left(
\frac{v_i}{M},
\frac{v_j}{M}
\right),
\qquad M=qW.
$$

Let

$$
d_{ij}=\gcd(v_i,v_j,M)
$$

and

$$
D_{ij}=\frac{M}{d_{ij}}
=
\det L_{ij}.
$$

Prove that every dual point modulo \(\mathbb Z^2\) has the form

$$
\eta_k
=
\left(
\left\{\frac{k v_i}{M}\right\},
\left\{\frac{k v_j}{M}\right\}
\right),
\qquad
k=0,\ldots,D_{ij}-1,
$$

after an appropriate choice of residues.

Prove that the relevant finite set \(\mathcal Q_{ij}\) is determined by

$$
\frac1q
\le
\left\{\frac{k v_i}{M}\right\}
\le
1-\frac1q
$$

and

$$
\frac1q
\le
\left\{\frac{k v_j}{M}\right\}
\le
1-\frac1q.
$$

Be extremely careful with the distinction between:

* a point in \(L_{ij}^*\),
* its class modulo \(\mathbb Z^2\),
* and the unique representative inside
  \([1/q,1-1/q]^2\).

---

# 2. Prove the "at most one lift" property

Because

$$
1-\frac2q<1,
$$

prove rigorously that for each residue class modulo \(\mathbb Z^2\), there is at most one representative in

$$
[1/q,1-1/q]^2.
$$

Therefore \(\mathcal Q_{ij}\) can be indexed directly by those \(k\) satisfying the two
fractional-part inequalities above.

This should eliminate unnecessary enumeration over \(\mathbb Z^2\).

---

# 3. Simplify the weight

For

$$
\eta_k=(x_k,y_k)
$$

inside the admissible square, derive

$$
\widehat G_q(\eta_k-h)
=
\frac1{\alpha_q^2}
\left(
1-\frac{|x_k-1/2|}{\alpha_q}
\right)
\left(
1-\frac{|y_k-1/2|}{\alpha_q}
\right).
$$

Rewrite each factor directly in terms of

$$
\{kv_i/M\},
\qquad
\{kv_j/M\}.
$$

Obtain a completely explicit formula

$$
T_{ij}
=
\frac1{D_{ij}}
\sum_{k\in K_{ij}}
H_q
\left(
\left\{\frac{kv_i}{M}\right\},
\left\{\frac{kv_j}{M}\right\}
\right).
$$

Prefer a formula involving distances to \(0\) and \(1\) on the circle.

---

# 4. Search for a combinatorial interpretation

The admissibility condition is

$$
\left\|
\frac{kv_i}{M}
\right\|
\ge\frac1q
$$

and

$$
\left\|
\frac{kv_j}{M}
\right\|
\ge\frac1q.
$$

Investigate whether \(K_{ij}\) can be interpreted directly as

$$
\left\{
k:
\left\|
\frac{k v_i}{M}
\right\|\ge\frac1q,
\quad
\left\|
\frac{k v_j}{M}
\right\|\ge\frac1q
\right\}.
$$

If so, formulate \(T_{ij}\) as a weighted count of "simultaneously safe"
residue classes.

Determine whether this connects the exact pair certificate to the original
lonely-runner geometry.

---

# 5. Determine exact cardinality of \(\mathcal Q_{ij}\)

Compute

$$
|\mathcal Q_{ij}|
$$

for many pairs.

Investigate whether it depends only on:

$$
q,\qquad
D_{ij},\qquad
\gcd(v_i,v_j),
$$

or whether finer arithmetic data are required.

Search for exact formulas and sharp lower/upper bounds.

The first target is a statement of the form

$$
|\mathcal Q_{ij}|
\ge
L(q,D_{ij})
$$

or

$$
|\mathcal Q_{ij}|
=
f(q,\text{explicit arithmetic invariants}).
$$

---

# 6. Characterize the zero case

Find an exact criterion for

$$
T_{ij}=0.
$$

Since every term in the finite formula is nonnegative,

$$
T_{ij}=0
$$

if and only if

$$
\mathcal Q_{ij}=\varnothing.
$$

Translate this into a purely arithmetic condition on

$$
(v_i,v_j,q,W).
$$

Do not confuse

$$
T_{ij}=0
$$

with failure of the Lonely Runner Conjecture. They are different statements.

The example

$$
V=(2,3),\quad N=2
$$

already shows that \(T_{ij}=0\) can coexist with LRC.

---

# 7. Find sharp lower bounds when \(T_{ij}>0\)

If

$$
\mathcal Q_{ij}\neq\varnothing,
$$

the individual terms have positive size.

Determine whether one can prove

$$
T_{ij}\ge
\frac{c(q)}{D_{ij}}
$$

or any stronger arithmetic lower bound.

More generally derive

$$
T_{ij}\ge
G(q,D_{ij},\text{arithmetic data}).
$$

The exact dependence on the distance of the dual points from the boundary is important.

---

# 8. Aggregate the pair sums

We have

$$
F_2(V)
=
\sum_{i<j}F_{ij}.
$$

From

$$
T_{ij}
=
1+
(\text{axis}_i^{(ij)})
+
(\text{axis}_j^{(ij)})
+
F_{ij},
$$

derive the exact global identity relating

$$
\sum_{i<j}T_{ij},
\qquad
F_{\rm axis},
\qquad
F_2.
$$

Simplify it symbolically.

The exact identity should be written in a standalone theorem.

Then determine exactly what lower bound on

$$
\sum_{i<j}T_{ij}
$$

would imply

$$
F_{\rm axis}+F_2>0.
$$

This is the key global inequality for the support-\(\le2\) sector.

---

# 9. Reduce the global question to a finite counting problem

Using the canonical \(k\)-parameter representation, write

$$
\sum_{i<j}T_{ij}
$$

as a sum over pairs \((i,j)\) and residues \(k\).

Investigate whether the order of summation can be reversed:

$$
\sum_{i<j}
\sum_k
(\cdots)
=
\sum_k
\sum_{i<j}
(\cdots).
$$

This may reveal global combinatorial structure.

Look for terms involving:

$$
\#\left\{
i:
\left\|
\frac{k v_i}{M}
\right\|\ge\frac1q
\right\}.
$$

If possible, express the pair sum in terms of the number of "safe" coordinates at
each residue \(k\).

This is potentially the most important step of the task.

---

# 10. Investigate a second-moment/counting interpretation

For each residue \(k\), define

$$
S_k
=
\left\{
i:
\left\|
\frac{k v_i}{M}
\right\|\ge\frac1q
\right\}.
$$

Then

$$
\binom{|S_k|}{2}
$$

counts the number of pairs simultaneously satisfying the support-2 admissibility
condition.

Investigate whether

$$
\sum_{i<j}T_{ij}
$$

can be expressed or bounded through weighted versions of

$$
\sum_k \binom{|S_k|}{2}.
$$

This is potentially crucial because a counterexample to LRC would mean that
every residue \(k\) fails for at least one coordinate, i.e.

$$
|S_k|\le N-1
$$

for every relevant residue.

Determine whether this global obstruction forces an upper bound on the pair
dual mass that conflicts with the lower bound required by
\(F_{\rm axis}+F_2\le0\).

Do not assume such a contradiction exists.

---

# 11. Investigate the exact relation with the original safe-box problem

Recall that the original LRC condition is equivalent to the existence of a
residue class \(x\) for which every coordinate lies in the safe interval.

The pair dual sets involve exactly the condition that two coordinates are safe.

Therefore investigate whether the support-2 dual sector is measuring the number of
pairs of coordinates that can simultaneously be safe.

Try to formulate a statement of the form:

$$
\text{pair dual mass}
\approx
\text{weighted second moment of the number of safe coordinates}.
$$

If an exact identity exists, prove it.

If only an inequality exists, prove the sharpest possible version.

This is more important than finding an isolated sign bound for \(F_{ij}\).

---

# 12. Test the global identity computationally

Create:

```
research/support2_global/
```

with:

```
aggregation.py
exact_counts.py
experiments.py
results.json
theorem.md
README.md
```

Test:

* \(N=2,\ldots,10\),
* exhaustive bounded configurations where feasible,
* random configurations,
* consecutive integers,
* odd integers,
* powers of two,
* highly composite configurations,
* configurations with repeated 2-adic valuation patterns.

All congruence calculations must use exact integers.

---

# 13. Search for the strongest universal inequality

The preferred target is one of:

### Target A

$$
F_{\rm axis}+F_2>0
\qquad
\forall N\ge4.
$$

### Target B

$$
F_{\rm axis}+F_2
\ge
c_N>0.
$$

### Target C

A lower bound in terms of a global safe-count statistic.

### Target D

A reduction showing that any violation of

$$
F_{\rm axis}+F_2>0
$$

forces a strong structural property of the entire configuration \(V\).

### Target E

A counterexample to universal support-\(\le2\) positivity, with the smallest
possible \(N\) and a structural explanation.

---

# 14. Important conceptual point

Do not treat

$$
T_{ij}\ge0
$$

as the end of the pairwise analysis.

The useful quantity is the relation between the nonnegative \(T_{ij}\) and the
negative exact-support terms obtained after removing the axes.

The central question is:

$$
\boxed{
\text{Can the axis subtraction be absorbed by a global lower bound on }
\sum_{i<j}T_{ij}?
}
$$

This is a global problem, not an individual-pair sign problem.

---

# 15. Do not move to support 3 yet

Only proceed to support 3 if one of the following is established:

1. \(F_{\rm axis}+F_2>0\) universally;
2. a strong global lower bound reduces the remaining problem to support \(\ge3\);
3. support 2 is proved incapable of being controlled by pairwise/global counting,
   with a rigorous obstruction.

The objective is to isolate exactly where genuinely higher-order interaction
first appears.

---

# 16. Required final report

Update:

```
research/support2_global/theorem.md
```

The final report must state:

1. the canonical \(k\)-parameter formula for \(T_{ij}\);
2. exact \(\mathcal Q_{ij}\) characterization;
3. exact zero criterion;
4. sharp lower bounds if available;
5. the global identity relating \(\sum T_{ij}\), \(F_{\rm axis}\), and \(F_2\);
6. any safe-count interpretation;
7. all experimentally tested inequalities;
8. rigorous counterexamples to failed conjectures;
9. the strongest theorem proved;
10. the exact reason support 3 is or is not now justified.

Do not claim that the LRC is proved.

The goal is to determine whether the entire support-\(\le2\) Fourier sector can be
closed by finite arithmetic and global counting alone.

