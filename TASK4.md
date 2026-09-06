# TASK 4 — Exact Evaluation of the Support-2 Fourier Sector

## Objective

The support-2 sector has now been reduced to the exact absolutely convergent sum

$$
F_{ij}
=
\sum_{\substack{r,s\in\mathbb Z\\
rv_i+sv_j\equiv0\pmod{qW}\\
rs\neq0}}
(-1)^{r+s}g_q(r)g_q(s),
$$

where

$$
g_q(n)
=
\left(
\frac{\sin\left(\pi(q-2)n/(2q)\right)}
{\pi(q-2)n/(2q)}
\right)^2,
\qquad
g_q(0)=1.
$$

The previous finite-radius experiments produced negative truncated values, but this does NOT establish that the infinite series is negative.

The purpose of this task is to determine the exact sign and structure of the FULL support-2 contribution.

Do not proceed to BSG, Freiman, Gowers norms, or high-order additive combinatorics.

The immediate goal is:

$$
\boxed{
\text{replace finite truncation by an exact or rigorously controlled
evaluation of }F_{ij}.
}
$$

---

# 1. Audit the previous support-2 results

Read:

* `01_dual_lattice.md`
* `02_poisson_certificate.md`
* `research/axis_obstruction.md`
* `research/support2/theorem.md`

Verify every formula involving:

$$
D_{ij},
$$

the congruence

$$
rv_i+sv_j\equiv0\pmod{qW},
$$

and the Fourier weight.

Do not assume the previous parametrization is optimal.

---

# 2. Put the support-2 relation set into lattice form

For fixed \(i<j\), define

$$
L_{ij}
=
\left\{
(r,s)\in\mathbb Z^2:
rv_i+sv_j\equiv0\pmod{qW}
\right\}.
$$

This is a full-rank sublattice of \(\mathbb Z^2\).

Compute:

1. an explicit basis for \(L_{ij}\);
2. its determinant/index;
3. its Smith normal form;
4. a canonical basis with parameters expressed in gcd data.

Do not rely only on the one-variable CRT parametrization.

The lattice formulation should be suitable for applying 2-dimensional Poisson summation or finite Fourier analysis.

---

# 3. Extend the pair contribution to include the origin and axes

Define the complete rank-two sum

$$
T_{ij}
=
\sum_{(r,s)\in L_{ij}}
(-1)^{r+s}g_q(r)g_q(s).
$$

Then decompose it exactly into:

$$
T_{ij}
=
1
+
T_i^{(ij)}
+
T_j^{(ij)}
+
F_{ij},
$$

where the first term is \((r,s)=(0,0)\), the next two are axis contributions, and

$$
F_{ij}
$$

is the exact-support-2 contribution.

This may be easier to evaluate than \(F_{ij}\) directly.

Determine the relationship between \(T_{ij}\) and the already computed global axis contribution.

---

# 4. Exploit the special form of \(g_q\)

Introduce

$$
\alpha_q=\frac{q-2}{2q}.
$$

Then

$$
g_q(n)
=
\left(
\frac{\sin(\pi\alpha_q n)}
{\pi\alpha_q n}
\right)^2.
$$

Investigate every exact representation of \(g_q\), including:

$$
g_q(n)
=
\int_{-\alpha_q}^{\alpha_q}
K_q(x)e^{2\pi i n x}\,dx
$$

for the appropriate triangular kernel \(K_q\).

Derive the exact kernel.

The aim is to convert

$$
T_{ij}
$$

from a weighted lattice sum into an integral involving a finite/lattice
character sum.

---

# 5. Apply 2-dimensional Poisson summation

Using the lattice

$$
L_{ij}\subset\mathbb Z^2,
$$

derive an exact formula for

$$
T_{ij}.
$$

Prefer a formula in which the rapidly decaying sinc-squared factors are
replaced by compactly supported triangular kernels.

Investigate whether the dual lattice is simple enough that only finitely many
dual points contribute because of compact support.

This is especially important because

$$
\alpha_q=\frac{q-2}{2q}<\frac12.
$$

Determine exactly how the support interval interacts with the dual lattice.

---

# 6. Alternative finite-Fourier formulation

Because \(g_q\) arises from a compactly supported triangle, investigate whether

$$
T_{ij}
$$

can be represented as a finite sum over residue classes modulo \(qW\).

In particular, derive a formula of the schematic form

$$
T_{ij}
=
\frac{1}{M}
\sum_{k\pmod M}
C_{ij}(k)\,H_q(k),
$$

or another finite expression, where

$$
M=qW.
$$

Do not assume such a formula exists; derive it or disprove its usefulness.

---

# 7. Exact sign of a single pair

For every pair \(i,j\), attempt to prove one of the following:

### Strong outcome

$$
F_{ij}\ge0.
$$

### Moderate outcome

$$
F_{ij}\ge -H(i,j)
$$

for an explicit arithmetic function \(H\).

### Structural outcome

The sign of \(F_{ij}\) is determined exactly by a finite set of residue/parity
data.

### Negative outcome

Construct an infinite-series example with

$$
F_{ij}<0.
$$

The last outcome is still valuable because it identifies the true obstruction.

---

# 8. Never infer the infinite sign from truncations

For every numerical calculation, distinguish:

$$
F_{ij}^{(R)}
=
\sum_{\substack{(r,s)\in L_{ij}\\
|r|,|s|\le R\\rs\ne0}}
(-1)^{r+s}g_q(r)g_q(s)
$$

from the actual

$$
F_{ij}.
$$

If numerical evidence is used, provide a rigorous tail bound.

A valid tail estimate must have the form

$$
|F_{ij}-F_{ij}^{(R)}|
\le E_{ij}(R)
$$

with an explicit \(E_{ij}(R)\to0\).

Only then may a numerical sign be claimed.

---

# 9. Derive a universal tail bound

Using

$$
g_q(n)\ll_q n^{-2},
$$

derive a uniform bound for the omitted lattice points.

Prefer a bound independent of the detailed arithmetic structure of \(V\),
for example

$$
\sum_{\substack{|r|>R\ \text{or}\ |s|>R}}
g_q(r)g_q(s)
\le
E_q(R).
$$

Make the constants explicit.

This will determine how large numerical searches must be before signs become
rigorously certifiable.

---

# 10. Investigate parity analytically

The factor

$$
(-1)^{r+s}
$$

should be treated structurally rather than as random cancellation.

Study the four parity classes

$$
(r,s)\pmod2.
$$

Determine which parity classes are actually present in

$$
L_{ij}.
$$

Classify according to

$$
\nu_2(v_i),\qquad
\nu_2(v_j),\qquad
\nu_2(qW).
$$

The central question is:

> Is the signed lattice sum \(T_{ij}\) equivalent to a difference of two
> positive sublattice sums with explicitly related indices?

If yes, derive that representation.

---

# 11. Study the ratio \(v_i/v_j\) rather than only valuations

Support-2 relations depend on more than 2-adic valuations.

Normalize:

$$
g=\gcd(v_i,v_j),
\qquad
v_i=gx,\qquad
v_j=gy,
\qquad
\gcd(x,y)=1.
$$

Rewrite the relation

$$
rx+sy\equiv0\pmod{qW/g}.
$$

Determine whether \(F_{ij}\) depends essentially on:

* \(x\),
* \(y\),
* \(q\),
* and the modulus \(qW/g\),

or whether it collapses to a simpler invariant.

Search for exact formulas in terms of:

$$
\gcd(v_i,v_j),\qquad
\operatorname{lcm}(v_i,v_j),\qquad
q.
$$

---

# 12. Search for monotonicity or extremality

Investigate whether the worst possible pair contribution occurs for a simple
arithmetic family.

Test systematically:

$$
(v_i,v_j)=(1,m),
$$

$$
(v_i,v_j)=(m,m+1),
$$

$$
(v_i,v_j)=(m,2m+1),
$$

and pairs with extreme gcd/lcm ratios.

The goal is to discover a possible universal extremal principle such as

$$
F_{ij}\ge F_{1,m}
$$

for an appropriate \(m\), or any useful reduction.

Do not assume monotonicity.

---

# 13. Global support-2 sector

Once the pairwise analysis is complete, compute

$$
F_2(V)
=
\sum_{i<j}F_{ij}.
$$

Determine whether there exists a universal bound

$$
F_2(V)\ge -C_N.
$$

Then compare it with

$$
F_{\rm axis}(V).
$$

The central question is:

$$
\boxed{
F_{\rm axis}(V)+F_2(V)>0?
}
$$

for all \(N\ge4\).

Do not claim this unless proved.

---

# 14. Investigate an alternative: pairwise positivity after axis redistribution

It may be that individual \(F_{ij}\) are negative, but that their negative mass can
be absorbed into the axis sector.

Investigate whether one can prove inequalities such as

$$
F_{ij}
\ge
-\alpha_{ij}
$$

with

$$
\sum_{i<j}\alpha_{ij}
<
F_{\rm axis}(V).
$$

This would be sufficient for positivity of the complete support-\(\le2\) sector.

---

# 15. Computational validation

Create:

```
research/support2_exact/
```

with:

```
exact_pair.py
experiments.py
results.json
theorem.md
README.md
```

The computational code must distinguish:

* exact integer/lattice calculations,
* exact symbolic calculations,
* floating-point approximations,
* rigorously bounded numerical signs.

For every numerical result include the truncation radius and rigorous tail bound
when applicable.

---

# 16. Required mathematical outputs

At the end of the task, establish as much as possible of:

### Theorem A

Exact basis/determinant for \(L_{ij}\).

### Theorem B

Exact representation of \(T_{ij}\).

### Theorem C

Exact or rigorously bounded formula for \(F_{ij}\).

### Theorem D

A valid sign/size theorem for \(F_{ij}\), if possible.

### Theorem E

A global support-\(\le2\) bound, if possible.

Each theorem must be marked:

* PROVED,
* VERIFIED,
* CONJECTURED,
* HEURISTIC,
* OPEN,
* DISPROVED.

---

# 17. Important conceptual objective

Determine whether support 2 is fundamentally an additive-combinatorial problem at
all.

There are three possible outcomes:

### Outcome 1

Support 2 is completely summable analytically.

Then the real combinatorial difficulty begins at support 3 or higher.

### Outcome 2

Support 2 has an arithmetic obstruction but admits a strong uniform bound.

Then incorporate that bound into the later Structure/Pseudorandomness argument.

### Outcome 3

Support 2 already contains configurations with arbitrarily difficult signed
cancellation.

Then stop trying to solve the problem pairwise and identify the exact mechanism
responsible for the obstruction.

---

# 18. Do not proceed to BSG/Gowers yet

This task must be completed before invoking:

* Balog–Szemerédi–Gowers,
* Freiman,
* Gowers inverse theorems,
* generalized arithmetic progressions,
* higher-order additive energy.

The purpose of the task is to determine whether the first genuinely difficult
Fourier interactions occur at support 2 or only at higher support.

---

# 19. Final report

Update:

```
research/support2_exact/theorem.md
```

with:

1. exact rank-two lattice structure;
2. exact full pair sum;
3. exact treatment of parity;
4. rigorous tail estimates;
5. all exact sign results;
6. all counterexamples;
7. computational evidence;
8. the strongest surviving theorem;
9. the exact remaining obstruction.

The final report must explicitly state whether the support-2 sector has been:

* solved,
* bounded,
* reduced to a new open lemma,
* or shown to contain a genuine obstruction.

Do not claim progress toward the full LRC unless the corresponding
mathematical implication is actually proved.

