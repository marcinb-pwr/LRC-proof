# TASK: Analyze the Axis-Dual Obstruction and Repair the Fourier Program

The previous 2-adic research task disproved the naive statement that every odd dual relation must involve multiple 2-adic valuation layers.

This is not merely a failed lemma. It reveals an important structural phenomenon:

For every coordinate \(i\),

$$
a=q b_i e_i
$$

is a valid relation because

$$
(qb_i)v_i=qW.
$$

The corresponding dual point is

$$
\xi=e_i.
$$

Its Fourier phase is

$$
e^{2\pi i\langle c,e_i\rangle}
=
(-1)^{q b_i}.
$$

Therefore, whenever \(qb_i\) is odd, there is an explicit negative Fourier contribution coming from a one-coordinate dual point.

The purpose of this task is to understand and isolate this phenomenon rigorously.

---

# 1. Correct the Poisson representation

Read:

* `01_dual_lattice.md`
* `02_poisson_certificate.md`
* `03_2adic_parity.md`

The current statement in `02_poisson_certificate.md` that the coefficient relation set should be quotiented by

$$
a_i\sim a_i+qb_i m_i
$$

must be removed.

The map

$$
a\mapsto
\left(
\frac{a_1}{qb_1},\ldots,
\frac{a_N}{qb_N}
\right)
$$

is injective.

Therefore the Poisson sum must be written as an actual sum over the full relation lattice

$$
D=
\left\{
a\in\mathbb Z^N:
\sum_i a_iv_i\equiv0\pmod{qW}
\right\}.
$$

The correct object is

$$
F(V)=
\sum_{a\in D}
(-1)^{\sum_i a_i}
\widehat\phi(\xi_a),
$$

where

$$
\xi_a=
\left(
\frac{a_1}{qb_1},\ldots,
\frac{a_N}{qb_N}
\right).
$$

Update the documentation accordingly.

---

# 2. Define the axis sublattice

Define

$$
D_{\mathrm{axis}}
=
\left\{
m q b_i e_i:
m\in\mathbb Z,\ 1\le i\le N
\right\}.
$$

Verify carefully:

1. every such element belongs to \(D\);
2. the associated dual point is

   $$
   \xi=me_i;
   $$
3. its parity is

   $$
   (-1)^{m q b_i};
   $$
4. determine exactly when the axis contribution is negative.

Do not call these relations "trivial" unless a precise mathematical reason is established.

---

# 3. Compute the axis Fourier contribution exactly

For the tensor-product triangle test function used in
`02_poisson_certificate.md`, compute

$$
F_{\mathrm{axis}}(V)
$$

exactly.

For

$$
A_i=\frac{q-2}{2}b_i,
$$

the contribution of the \(i\)-th axis is

$$
\sum_{m\in\mathbb Z}
(-1)^{m q b_i}
\left(
\frac{\sin(\pi m A_i)}
{\pi m A_i}
\right)^2.
$$

Derive a closed form whenever possible.

Use exact identities for Fourier series such as

$$
\sum_{m\ge1}\frac{1}{m^2},
\qquad
\sum_{m\ge1}\frac{(-1)^m}{m^2},
$$

and their variants if needed.

Do not use numerical approximation when an exact expression is available.

---

# 4. Determine whether the axis contribution is already positive

Study

$$
F_{\mathrm{axis}}(V).
$$

Determine whether there are configurations for which:

$$
F_{\mathrm{axis}}(V)>0,
$$

$$
F_{\mathrm{axis}}(V)=0,
$$

or

$$
F_{\mathrm{axis}}(V)<0.
$$

Perform both:

* symbolic analysis,
* exhaustive computational experiments for small \(N\).

Determine the dependence on:

$$
q=N+1,
$$

and on the parity of

$$
b_i=W/v_i.
$$

---

# 5. Do not assume that axis/non-axis is the optimal decomposition

Investigate whether the relation lattice admits a more useful decomposition.

Possible alternatives include:

$$
D=D_{\mathrm{axis}}+D_{\mathrm{genuine}},
$$

or decomposition according to support size:

$$
|\operatorname{supp}(a)|=1,\ 2,\ \ge3,
$$

or decomposition according to:

* primitive dual vectors,
* coordinatewise gcd,
* divisibility by \(qb_i\),
* 2-adic valuation,
* Fourier frequency,
* or shortest-vector structure.

The objective is to identify a decomposition in which the dangerous negative terms can be controlled explicitly.

---

# 6. Search for the actual obstruction

The central question is now:

> What is the simplest possible source of a negative Fourier term?

Classify all relations \(a\in D\) with:

$$
\sum_i a_i\equiv1\pmod2
$$

and small Fourier frequency.

Especially enumerate:

* support \(1\),
* support \(2\),
* support \(3\),
* then general support.

For every class determine which arithmetic conditions on \(V\) permit it.

Produce explicit classification theorems wherever possible.

---

# 7. Revisit the 2-adic mechanism

The previous task established that:

$$
\text{odd parity}
\not\Rightarrow
\text{multiple 2-adic valuation layers}.
$$

Now ask the more precise question:

> After removing the explicitly classifiable one-coordinate relations, does odd parity force additional 2-adic structure?

Formally investigate something like:

$$
a\in D_{\mathrm{genuine}},
\qquad
\sum_i a_i\equiv1\pmod2
$$

implying a nontrivial lower bound on a 2-adic complexity.

Do not assume this is true.

Find counterexamples first.

---

# 8. Search for a corrected theorem

Possible target theorem:

> Every genuinely multidimensional odd dual relation either has sufficiently large Fourier frequency or exhibits a prescribed 2-adic carry structure.

The exact statement must be discovered from the data.

The theorem should preferably imply an estimate of the form

$$
\widehat\phi(\xi_a)
\le
G(\mathcal C_2(a,V))
$$

for odd genuine relations.

---

# 9. Computational experiment

Build or extend:

```
research/2adic/experiments.py
```

to compute separately:

$$
M_{\rm axis}
=
\sum_{a\in D_{\rm axis}}
(-1)^{|a|}w(a)
$$

and

$$
M_{\rm genuine}
=
\sum_{a\in D\setminus D_{\rm axis}}
(-1)^{|a|}w(a).
$$

Study these quantities for:

* \(N=2,\ldots,8\),
* exhaustive bounded configurations when feasible,
* random configurations,
* arithmetic progressions,
* odd configurations,
* powers of two,
* mixed valuation configurations,
* high-energy configurations,
* low-energy configurations.

Determine empirically whether the difficult part is actually concentrated in
support \(\ge2\).

---

# 10. Required final outputs

Create or update:

```
research/axis_obstruction.md
research/axis_experiments.py
research/axis_results.json
```

The main document must contain:

1. the corrected infinite Poisson relation sum;
2. the exact axis relation classification;
3. the exact axis Fourier contribution;
4. symbolic sign analysis;
5. exhaustive computational evidence;
6. the strongest corrected 2-adic statement that survives testing;
7. all counterexamples found.

Classify every result as:

* PROVED,
* VERIFIED,
* CONJECTURED,
* HEURISTIC,
* OPEN,
* or DISPROVED.

---

# 11. Critical research rule

Do not try to rescue the original false 2-adic lemma.

The objective is not:

$$
\text{"make the original proof work"}.
$$

The objective is:

$$
\boxed{
\text{identify the actual structure of the negative dual Fourier mass}.
}
$$

The axis relations may be a harmless explicitly summable contribution, a genuine obstruction, or evidence that the chosen test function needs to be replaced.

Determine which one is true.

---

# 12. Stop condition

Stop this task only after one of the following has been achieved:

### A

A rigorous theorem shows that the entire axis contribution has a controlled sign and magnitude.

### B

A counterexample shows that the axis contribution alone can overwhelm the positive zero-frequency term.

### C

A corrected decomposition identifies a smaller class of genuinely difficult
relations and proves a nontrivial structural property for that class.

### D

No useful decomposition exists, but the precise obstruction is rigorously
characterized.

Do not stop merely because proving LRC remains difficult.

The objective of this task is to convert the failed naive parity lemma into a
more accurate structural theorem about the signed dual Fourier sum.

