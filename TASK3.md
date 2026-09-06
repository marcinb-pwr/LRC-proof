# TASK 3 — Support-2 Dual Sector

## Goal

The axis sector (support 1) has now been classified exactly and its Fourier contribution has been computed.

The next objective is to completely understand the **support-2 sector**

$$
D_2
=
\{a\in D:|\operatorname{supp}(a)|=2\}.
$$

This is the lowest-dimensional genuinely multidimensional part of the dual lattice.

Do NOT move to BSG, Freiman, Gowers norms, or a general Structure/Pseudorandomness theorem yet.

The immediate goal is to determine exactly what the support-2 contribution looks like, whether it can be summed explicitly, and what structural information its negative part contains.

---

# 1. Correct the existing documentation first

Read:

* `01_dual_lattice.md`
* `02_poisson_certificate.md`
* `research/axis_obstruction.md`

Verify that the full Fourier sum is

$$
F(V)
=
\sum_{a\in D}
(-1)^{|a|}
\widehat\phi(\xi_a),
$$

with

$$
D=
\left\{
a\in\mathbb Z^N:
\sum_i a_i v_i\equiv0\pmod{qW}
\right\},
$$

and

$$
\xi_a=
\left(
\frac{a_1}{qb_1},\ldots,
\frac{a_N}{qb_N}
\right).
$$

Do not quotient coefficient vectors.

---

# 2. Define the support-2 sector precisely

For every unordered pair

$$
\{i,j\},
$$

define

$$
D_{ij}
=
\{a\in D:
\operatorname{supp}(a)\subseteq\{i,j\}\}.
$$

Separate the axis vectors from genuine support-2 vectors:

$$
D_{ij}^{(2)}
=
\{a\in D:
\operatorname{supp}(a)=\{i,j\}\}.
$$

Then

$$
D_2
=
\bigcup_{i<j}D_{ij}^{(2)}.
$$

Establish that these sets are disjoint.

---

# 3. Obtain a canonical parametrization

The previous task derived a congruence characterization for

$$
a=r e_i+s e_j.
$$

Now make this representation canonical.

For each pair \(i<j\), derive an explicit parametrization of every support-2 relation in terms of one integer parameter.

The parametrization should make it possible to answer:

* when the relation is primitive,
* when it is an axis relation,
* when its coefficient sum is odd,
* and how large its Fourier frequency is.

Avoid arbitrary choices of integer representatives whenever possible.

---

# 4. Exact parity classification

For every pair \(i,j\), determine exactly when a support-2 relation

$$
a=r e_i+s e_j
$$

satisfies

$$
r+s\equiv1\pmod2.
$$

Express the condition directly in terms of:

$$
v_i,\;v_j,\;q,\;W,
$$

and relevant gcds.

In particular, determine the role of:

$$
\nu_2(v_i),
\qquad
\nu_2(v_j),
\qquad
\nu_2(qW).
$$

Do not assume that odd parity requires distinct 2-adic valuation layers.

Search explicitly for counterexamples.

---

# 5. Exact Fourier weight for support 2

For

$$
a=r e_i+s e_j,
$$

compute

$$
w(a)
=
\widehat\phi(\xi_a)
$$

exactly for the triangle test function.

Since

$$
A_i=\frac{q-2}{2}b_i,
$$

we have

$$
w(a)
=
\left(
\frac{\sin(\pi r A_i/(q b_i))}
{\pi r A_i/(q b_i)}
\right)^2
\left(
\frac{\sin(\pi s A_j/(q b_j))}
{\pi s A_j/(q b_j)}
\right)^2.
$$

Simplify this expression fully.

In particular, observe and exploit that

$$
\frac{A_i}{q b_i}
=
\frac{q-2}{2q},
$$

which is independent of \(i\).

Determine whether this leads to a universal one-dimensional weight

$$
g_q(r)
$$

such that

$$
w(r e_i+s e_j)
=
g_q(r)\,g_q(s).
$$

If so, prove it.

---

# 6. Exact support-2 Fourier contribution

Define

$$
F_2(V)
=
\sum_{a\in D_2}
(-1)^{|a|}w(a).
$$

Decompose

$$
F_2(V)
=
\sum_{i<j}F_{ij}(V).
$$

For each pair, attempt to derive an exact formula or an absolutely convergent one-dimensional series.

Do not settle for a vague bound if an exact expression is possible.

---

# 7. Primitive versus nonprimitive relations

Investigate whether every support-2 relation can be represented as

$$
m a_0
$$

where \(a_0\) is primitive in \(\mathbb Z^2\).

Classify:

* primitive relations,
* multiples of primitive relations,
* their parity,
* their Fourier weights.

Determine whether summing over multiples can be performed analytically.

The preferred outcome is a reduction of \(F_{ij}\) to a finite number of arithmetic classes times a universal rapidly convergent series.

---

# 8. Search for a pairwise obstruction parameter

For every pair \(i,j\), define a numerical parameter

$$
\mathcal P(i,j)
$$

measuring how strongly the pair can generate negative support-2 Fourier mass.

Possible ingredients:

* \(\gcd(v_i,v_j)\),
* \(\gcd(v_i,qW)\),
* \(\gcd(v_j,qW)\),
* \(v_i/gcd(v_i,v_j)\),
* \(v_j/gcd(v_i,v_j)\),
* \(2\)-adic valuations,
* the smallest odd relation,
* the smallest Fourier frequency.

Do not assume the final form.

Use computation to discover the right invariant.

---

# 9. Determine the smallest negative support-2 frequency

For every pair \(i,j\), define

$$
L_{ij}
=
\min\{
|r|+|s|:
r e_i+s e_j\in D_2,\ r+s\text{ odd}
\},
$$

with \(L_{ij}=\infty\) if no such relation exists.

Compute \(L_{ij}\) exactly for many configurations.

Investigate whether there is a simple arithmetic formula or lower bound for \(L_{ij}\).

This is potentially more useful than the false statement about 2-adic valuation layers.

---

# 10. Test the hypothesis of pairwise control

Investigate whether the total negative support-2 mass satisfies a bound of the form

$$
M_{2,\mathrm{odd}}
=
\sum_{\substack{a\in D_2\\|a|\text{ odd}}}w(a)
\le
\sum_{i<j}H(\mathcal P(i,j)),
$$

for an explicit function \(H\).

Then search for a universal upper bound depending only on \(N\).

The ideal outcome would be something like

$$
M_{2,\mathrm{odd}}
<
c_N
$$

with

$$
c_N<1
$$

or, better, a bound that can be compared directly with the positive zero-frequency and axis contributions.

---

# 11. Compare support 2 against the axis sector

Define

$$
F_{\le2}
=
F_{\rm axis}+F_2.
$$

Determine computationally and symbolically whether

$$
F_{\le2}>0
$$

holds universally for:

$$
N\ge4.
$$

Test all configurations within feasible small bounds and large random samples.

This is not a proof.

The objective is to determine whether the next genuine obstruction begins at support 2 or support 3.

---

# 12. Search for exact cancellation

Do not only look at absolute values.

The signed sum may exhibit systematic cancellation.

Study:

$$
F_{ij}
=
\sum_{a\in D_{ij}^{(2)}}
(-1)^{|a|}w(a).
$$

Determine whether there are pairwise identities causing:

$$
F_{ij}\ge0,
$$

or perhaps stronger:

$$
F_{ij}>-C_{ij}
$$

with a small explicit \(C_{ij}\).

Pay particular attention to parity patterns where the relation set is invariant under

$$
(r,s)\mapsto(-r,-s).
$$

---

# 13. 2-adic analysis: only after exact pair classification

After obtaining the exact support-2 parametrization, investigate its 2-adic consequences.

Ask the precise question:

> Does odd parity of a support-2 relation force a lower bound on its Fourier frequency?

The desired form is something such as

$$
r+s\equiv1\pmod2
\Longrightarrow
|r|+|s|
\ge
L(q,v_i,v_j).
$$

This would replace the false multi-layer theorem by a statement directly relevant to Fourier decay.

If false, search for the correct invariant.

---

# 14. Computational requirements

Create:

```
research/support2/
```

with:

```
experiments.py
results.json
theorem.md
README.md
```

The program must support:

* exhaustive search for small \(N\),
* exhaustive bounded search over \(V\),
* enumeration of support-2 relations,
* exact parity,
* exact valuation data,
* exact smallest odd relation,
* numerical Fourier weights,
* pairwise signed contributions,
* comparison with the axis sector.

Use exact integer arithmetic for all congruences.

Use high precision only for Fourier evaluations.

---

# 15. Required theorem status

At the end, classify every major conclusion as one of:

* PROVED
* VERIFIED
* CONJECTURED
* HEURISTIC
* OPEN
* DISPROVED

Do not upgrade empirical observations to theorems.

---

# 16. Desired mathematical outcomes

The strongest useful outcomes, in descending order, are:

### Outcome A

Prove a universal lower bound on the frequency of every odd support-2 relation.

### Outcome B

Compute \(F_2(V)\) exactly and prove

$$
F_{\rm axis}(V)+F_2(V)>0
$$

for all \(N\ge4\).

### Outcome C

Prove a strong uniform upper bound on the negative support-2 mass.

### Outcome D

Find a new arithmetic invariant controlling support-2 negativity.

### Outcome E

Find a counterexample showing support 2 is already too strong to control by pairwise methods.

Any of these is a useful research result.

---

# 17. Do NOT proceed yet to general additive combinatorics

Do not start:

* BSG,
* Freiman,
* Gowers inverse theorems,
* generalized arithmetic progressions,
* high-order additive energy,

until the support-2 sector has been fully analyzed.

The research hierarchy should now be:

$$
\boxed{
\text{support 1}
\rightarrow
\text{support 2}
\rightarrow
\text{support 3}
\rightarrow
\cdots
\rightarrow
\text{global structure}.
}
$$

The purpose is to discover the smallest support at which genuinely new
combinatorial structure becomes unavoidable.

---

# 18. Final report

At completion, update the research tree with:

```
research/support2/theorem.md
```

and append a section to the main research notes explaining:

1. the exact support-2 classification;
2. the exact parity criterion;
3. the Fourier weight;
4. the size of the negative sector;
5. whether \(F_{\rm axis}+F_2\) is always positive in tested ranges;
6. the strongest proved theorem;
7. any counterexamples;
8. the precise remaining obstruction.

Do not claim progress toward a full LRC proof unless a new rigorous theorem has actually been proved.

