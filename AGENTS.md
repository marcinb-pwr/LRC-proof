# AGENTS.md

# Research Program: 2-adic Fourier–Structure Approach to the Lonely Runner Conjecture

## 0. Mission

The goal of this project is to investigate and, if possible, obtain a complete proof of the **Lonely Runner Conjecture (LRC)** for every number of runners.

This is a mathematical research project. Heuristic arguments must never be presented as proofs. Every claim must be classified and treated appropriately:

1. formally stated,
2. checked against boundary cases and small examples,
3. derived from previously established results,
4. or explicitly marked as a conjecture/open lemma.

The central research strategy combines:

* reduction of LRC to a lattice/box problem,
* exact determination of the dual lattice,
* Poisson summation,
* a carefully chosen test function,
* Fourier phase parity,
* 2-adic filtration,
* carry propagation,
* additive energy,
* Structure/Pseudorandomness methods,
* BSG/Freiman/Gowers-type inverse theory,
* and reduction of the structured case to simpler configurations or smaller dimension.

The intended chain is:

$$
\boxed{
\text{counterexample to LRC}
\Longrightarrow
\text{dual Fourier certificate}
\Longrightarrow
\text{negative parity mass}
\Longrightarrow
2\text{-adic structure of relations}
\Longrightarrow
\text{additive structure}
\Longrightarrow
\text{contradiction}.
}
$$

None of these implications should be assumed in advance. The purpose of the project is to determine which are true, prove them when possible, and identify precisely where genuinely new mathematics is required.

---

# 1. Exact formulation of LRC

After the standard normalization, consider distinct positive integers

$$
V=\{v_1,\ldots,v_N\},
\qquad
v_i\in\mathbb Z_{>0}.
$$

The target statement is the existence of

$$
t\in\mathbb R
$$

such that

$$
\boxed{
\|t v_i\|_{\mathbb R/\mathbb Z}
\ge
\frac{1}{N+1}
\qquad
\forall i.
}
$$

Here

$$
\|x\|_{\mathbb R/\mathbb Z}
=
\min_{m\in\mathbb Z}|x-m|.
$$

Do not alter the threshold \(1/(N+1)\) without an explicit justification.

---

# 2. First objective: a completely rigorous lattice reduction

Do not begin with additive combinatorics.

First establish, from first principles, an exact equivalence between LRC and a lattice point in a translated box.

Define

$$
q=N+1,
$$

$$
W=\operatorname{lcm}(v_1,\ldots,v_N),
$$

$$
b_i=\frac{W}{v_i}.
$$

Introduce

$$
x=qWt.
$$

Then

$$
tv_i=\frac{x}{qb_i}.
$$

The condition

$$
\left\|\frac{x}{qb_i}\right\|
\ge
\frac1q
$$

must be converted exactly into a condition on

$$
x\bmod qb_i.
$$

After centering the residue intervals, the expected box is

$$
K=
\prod_{i=1}^{N}
\left[
-\frac{q-2}{2}b_i,
\frac{q-2}{2}b_i
\right]
$$

and the expected shift is

$$
c=
\left(
\frac q2 b_1,\ldots,
\frac q2 b_N
\right).
$$

However, these formulas must be derived rather than assumed.

The proof must explicitly handle all parity and endpoint issues.

## Required result

Prove a precise equivalence

$$
\boxed{
\text{LRC for }V
\iff
(\Lambda-c)\cap K\neq\varnothing
}
$$

for an explicitly and correctly defined lattice \(\Lambda\).

Do not write "this follows from the Chinese Remainder Theorem" without supplying the actual derivation.

---

# 3. Exact construction of the lattice \(\Lambda\)

Derive the lattice induced by compatibility of the residue conditions.

A natural candidate is

$$
\Lambda=
\left\{
r\in\mathbb Z^N:
r_i\equiv r_j
\pmod{q\gcd(b_i,b_j)}
\quad\forall i,j
\right\}.
$$

This definition must not be accepted without proof.

Establish:

1. that \(\Lambda\) is exactly the image of

   $$
   x\mapsto
   (x\bmod qb_1,\ldots,x\bmod qb_N),
   $$
2. the precise CRT compatibility conditions,
3. the index of \(\Lambda\) in \(\mathbb Z^N\),
4. the determinant/covolume of \(\Lambda\),
5. consistency for \(N=1,2,3,\ldots\),
6. consistency when the \(b_i\) have nontrivial common divisors.

The lattice description should emerge from the arithmetic; it should not be fitted to the desired Poisson formula.

---

# 4. Critical step: compute the dual lattice exactly

This is the first fundamental theorem of the project.

For

$$
\Lambda\subset\mathbb Z^N
$$

define

$$
\Lambda^\ast
=
\left\{
\xi\in\mathbb R^N:
\langle\xi,\lambda\rangle\in\mathbb Z
\quad
\forall\lambda\in\Lambda
\right\}.
$$

Compute \(\Lambda^\ast\) explicitly.

Do not assume that

$$
\Lambda^\ast
=
\left\{
\left(
\frac{a_1}{qb_1},\ldots,
\frac{a_N}{qb_N}
\right):
\sum_i a_iv_i\equiv0\pmod{qW}
\right\}
$$

unless this is actually proved.

## Target

Obtain an exact correspondence between elements of the dual lattice and arithmetic relations of the form

$$
\boxed{
D=
\left\{
a\in\mathbb Z^N:
\sum_i a_i v_i\equiv0\pmod{qW}
\right\}.
}
$$

If the correct parametrization differs, use the correct one.

---

# 5. Poisson summation

After the exact dual lattice is known, choose a test function

$$
\phi:\mathbb R^N\to\mathbb R_{\ge0}
$$

with as many as possible of the following properties.

### P1 — Support

$$
\operatorname{supp}\phi\subseteq K.
$$

### P2 — Nontriviality

$$
\phi\not\equiv0.
$$

### P3 — Fourier positivity

Preferably,

$$
\widehat\phi(\xi)\ge0
\qquad
\forall\xi.
$$

### P4 — Normalization

Preferably,

$$
\widehat\phi(0)=1.
$$

Potential function classes:

* tensor-product B-splines,
* Beurling/Selberg-type majorants,
* Fejér-type kernels,
* compactly supported positive-definite functions,
* squares/convolutions of compactly supported functions,
* other functions with strong Fourier decay and manageable support.

If P1–P4 cannot be achieved simultaneously, document the obstruction and modify the function class.

---

# 6. Exact Poisson formula

For

$$
S(c)=
\sum_{\lambda\in\Lambda}\phi(c-\lambda)
$$

derive

$$
S(c)
=
\frac{1}{\operatorname{covol}(\Lambda)}
\sum_{\xi\in\Lambda^\ast}
\widehat\phi(\xi)
e^{2\pi i\langle c,\xi\rangle}.
$$

All conventions must be explicit:

* Fourier-transform convention,
* \(2\pi\) normalization,
* determinant/covolume factors,
* signs,
* regularity assumptions on \(\phi\),
* decay assumptions needed for Poisson summation.

---

# 7. The parity phase theorem

This is the central structural feature of the method.

For a dual point \(\xi_a\) corresponding to a relation \(a\), calculate

$$
e^{2\pi i\langle c,\xi_a\rangle}
$$

exactly.

The desired identity is

$$
\boxed{
e^{2\pi i\langle c,\xi_a\rangle}
=
(-1)^{\sum_i a_i}.
}
$$

If this is not exactly correct, determine the true phase function.

If

$$
w(a)=\widehat\phi(\xi_a)\ge0,
$$

the Fourier certificate becomes

$$
F(V)
=
\sum_{a\in D}
(-1)^{|a|}
w(a),
$$

where

$$
|a|=\sum_i a_i.
$$

Hence

$$
F(V)
=
\sum_{\substack{a\in D\\ |a|\text{ even}}}
w(a)
-
\sum_{\substack{a\in D\\ |a|\text{ odd}}}
w(a).
$$

---

# 8. Fundamental certificate

Prove rigorously:

$$
\boxed{
F(V)>0
\Longrightarrow
\text{LRC for }V.
}
$$

Indeed,

$$
F(V)>0
\Longrightarrow
S(c)>0,
$$

so there exists

$$
\lambda\in\Lambda
$$

such that

$$
\phi(c-\lambda)>0.
$$

The support condition then implies

$$
c-\lambda\in K.
$$

The lattice reduction then gives LRC.

Thus the entire problem can be reduced to proving

$$
\boxed{
F(V)>0
\quad\text{for every admissible configuration }V.
}
$$

---

# 9. Do not equate "few relations" with pseudorandomness

Do not use informal statements such as:

> "The set has no additive structure, therefore it is pseudorandom."

Introduce quantitative parameters.

Possible quantities include:

* ordinary additive energy,
* higher additive energies,
* weighted relation counts,
* short-relation counts,
* Gowers norms,
* Fourier mass,
* higher-order correlation parameters.

The exact parameter must be chosen to control the signed dual Fourier sum.

---

# 10. Additive energy

For suitable \(k\), study

$$
E_k(V)
=
\#\left\{
(x_1,\ldots,x_k,y_1,\ldots,y_k)\in V^{2k}:
\sum_{j=1}^k x_j
=
\sum_{j=1}^k y_j
\right\}.
$$

Also investigate weighted versions naturally associated with the dual relation set \(D\).

Do not assume that ordinary \(E(V)\) is necessarily the correct quantity.

The research goal is to discover a relation between

$$
M_{\rm odd}(V)
=
\sum_{\substack{a\in D\\|a|\text{ odd}}}
w(a)
$$

and some appropriate additive-energy parameter.

---

# 11. 2-adic decomposition

Write

$$
v_i=2^{s_i}u_i,
\qquad
u_i\text{ odd}.
$$

Define the 2-adic layers

$$
I_s=
\{i:\nu_2(v_i)=s\}.
$$

Study the relation

$$
\sum_i a_iv_i\equiv0\pmod{qW}
$$

successively modulo

$$
2,\;4,\;8,\ldots,2^k.
$$

For each layer define

$$
B_s(a)
=
\sum_{i\in I_s}a_i u_i.
$$

Derive the exact carry equations.

A schematic form may be

$$
C_{s+1}
=
\frac{C_s+B_s(a)}2,
$$

but this formula must be derived with the correct normalization of the congruence.

---

# 12. Main 2-adic objective

Formulate and prove a genuine:

## 2-adic Parity Theorem

For every

$$
a\in D
$$

with

$$
|a|\equiv1\pmod2,
$$

the relation must have some forced 2-adic complexity.

The desired shape is

$$
\boxed{
\mathcal C_2(a)
\ge
L(N,\text{parameters of }V),
}
$$

where \(\mathcal C_2(a)\) measures one or more of:

* number of active 2-adic layers,
* number of carries,
* carry depth,
* support size,
* 2-adic span,
* or another structurally meaningful quantity.

The key working hypothesis is:

> A non-even dual relation cannot be simultaneously very short and 2-adically simple.

This must be tested aggressively. A small counterexample should cause immediate revision of the statement.

---

# 13. Define a relation complexity

Introduce a complexity measure

$$
\mathcal C(a)
$$

combining:

$$
\|a\|_1,
$$

support information, and 2-adic structure.

For example, one may investigate

$$
\mathcal C(a)
=
\alpha\|a\|_1
+
\beta T_2(a)
+
\gamma R_2(a),
$$

where:

* \(T_2(a)\) is the number of carries,
* \(R_2(a)\) is a measure of 2-adic depth/span.

This is only a research template. The final definition should be the one for which both the parity theorem and Fourier decay can be proved.

---

# 14. Fourier weight decay

Establish an inequality of the form

$$
w(a)
\le
G(\mathcal C(a))
$$

for a rapidly decaying function \(G\).

Desired examples are:

$$
w(a)
\ll_M
(1+\mathcal C(a))^{-M}
$$

for arbitrary \(M\), or

$$
w(a)\le e^{-c\mathcal C(a)}.
$$

The eventual target is a dominance relation such as

$$
\sum_{\substack{a\in D\\|a|\text{ odd}}}w(a)
<
w(0)
+
\sum_{\substack{a\in D\\|a|\text{ even},\,a\ne0}}
w(a).
$$

This gives

$$
F(V)>0.
$$

---

# 15. The Structure/Pseudorandomness theorem

Do not assume a qualitative dichotomy.

Construct a quantitative theorem.

## Structure/Pseudorandomness Theorem

For an appropriately defined parameter \(\mathcal R(V)\), one of the following must hold.

### Branch P — pseudorandom

$$
\mathcal R(V)\le\varepsilon.
$$

Then prove directly that

$$
\boxed{
M_{\rm odd}(V)<M_{\rm even}(V)
}
$$

and hence

$$
F(V)>0.
$$

A stronger target would be

$$
\sum_{\substack{a\in D\\a\neq0}}
w(a)
<
w(0).
$$

### Branch S — structured

$$
\mathcal R(V)>\varepsilon.
$$

Then prove the existence of

$$
V'\subseteq V
$$

with

$$
|V'|\ge\delta(N)|V|
$$

such that \(V'\) lies in a low-rank generalized arithmetic progression

$$
P=
\left\{
n_1d_1+\cdots+n_rd_r:
|n_j|\le L_j
\right\},
$$

with

$$
r\le R(N).
$$

---

# 16. Standard BSG/Freiman output is not sufficient

If the structured branch only yields an ordinary GAP, preserve additional 2-adic information.

The desired result is something like

$$
\boxed{
V'\subseteq P
\quad\text{and}\quad
P\text{ satisfies a strong 2-adic alignment condition}.
}
$$

Possible conditions to investigate include constraints such as

$$
\nu_2(d_i-d_j)\ge h(N),
$$

or conditions on the valuations of generators, differences, or internal additive relations.

Do not assume this is the correct form. Discover the appropriate condition from the relation structure.

---

# 17. Central new theorem

The primary structural target is:

## Theorem X — 2-adic Structure/Pseudorandomness Dichotomy

For every admissible configuration \(V\), one of the following holds.

### X-P: pseudorandom branch

The odd dual mass satisfies

$$
M_{\rm odd}(V)
<
M_{\rm even}(V),
$$

hence

$$
F(V)>0.
$$

### X-S: structured branch

There exists a large subset

$$
V'\subseteq V
$$

contained in a low-rank GAP whose structure is sufficiently 2-adically controlled to permit either:

$$
F(V)>0,
$$

or a reduction to a strictly smaller LRC instance.

This theorem is a major research objective, not an assumption.

---

# 18. Pseudorandom branch

In the pseudorandom regime, obtain a direct estimate for the nonzero dual contribution.

Do not invoke "Weil bounds", "Kloosterman cancellation", or "square-root cancellation" automatically.

The actual sum is

$$
\sum_{a\in D}
(-1)^{|a|}w(a),
$$

which is a weighted sum over a dual lattice/relation set.

First identify the correct analytic object.

Potential tools include:

* Gowers norms,
* additive energy,
* inverse theorems,
* large sieve methods,
* geometry of numbers,
* lattice-point estimates,
* Fourier restriction estimates,
* concentration inequalities,
* Poisson summation,
* decoupling,
* harmonic-analysis estimates.

Every tool must be applied with its exact hypotheses verified.

---

# 19. Structured branch

If \(V\) has additive structure, do not assume that LRC becomes automatic.

Prove a separate:

## Structured LRC Theorem

A configuration satisfying the structural and 2-adic conditions must either:

1. satisfy LRC directly,
2. yield positive Fourier certificate \(F(V)>0\),
3. or reduce to a strictly smaller LRC instance.

Possible mechanisms:

* explicit construction of \(t\),
* dimension reduction,
* reduction in the number of independent generators,
* induction on \(N\),
* reduction to an already solved configuration,
* classification of extremal GAPs.

---

# 20. Minimal counterexample principle

Assume a counterexample exists.

Choose one minimal under a rigorously defined order, for example

$$
(N,\sum_i v_i,\max_i v_i),
$$

or a better well-ordering discovered during the project.

Attempt to prove:

$$
\boxed{
\text{every minimal counterexample must be structured}.
}
$$

Then prove:

$$
\boxed{
\text{structured minimal counterexample}
\Rightarrow
\text{strictly smaller counterexample}.
}
$$

This contradicts minimality.

---

# 21. Inductive reduction

The ideal structural conclusion is

$$
V\longrightarrow V_{\rm red}
$$

with

$$
|V_{\rm red}|<|V|.
$$

Every such reduction must explicitly control:

* the new number of runners,
* the change in threshold,
* rescaling,
* integrality,
* distinctness,
* and the correspondence between the original and reduced configurations.

Do not use hidden induction that changes the LRC threshold without proof.

---

# 22. Alternative endpoint: direct positivity in the structured regime

If the structural branch cannot be reduced inductively, try to prove directly

$$
\boxed{
F(V)>0.
}
$$

For a structured configuration, the desired mechanism is

$$
\text{GAP structure}
\Rightarrow
\text{controlled parity bias}
$$

and hence

$$
M_{\rm even}-M_{\rm odd}>0.
$$

A successful argument of this type may be stronger and cleaner than an inductive reduction.

---

# 23. Central coupling: 2-adic structure ↔ additive energy

The most important research hypothesis is:

$$
\boxed{
\text{large odd dual mass}
\Rightarrow
\text{strong 2-adic structure}
\Rightarrow
\text{large additive energy}.
}
$$

The desired form is a theorem such as

$$
M_{\rm odd}(V)\ge\eta
$$

implying

$$
E_k(V)\ge c(\eta,N)|V|^{2k-1}
$$

for a suitable \(k\).

Then apply an inverse theorem:

$$
E_k(V)\text{ large}
\Rightarrow
V'\subseteq\text{low-rank GAP}.
$$

This implication is a central candidate for the genuinely new mathematical ingredient.

---

# 24. Computational research program

Before attempting the general theorem, build computational experiments.

For

$$
N=2,\ldots,14
$$

and broad families of \(V\):

1. compute \(W\),
2. construct \(\Lambda\),
3. compute \(\Lambda^\ast\),
4. enumerate short elements of \(D\),
5. classify relations by

   $$
   |a|\pmod2,
   $$
6. compute \(\nu_2(v_i)\),
7. record carry profiles,
8. measure \(\|a\|_1\),
9. estimate \(M_{\rm odd}\),
10. calculate additive energies,
11. measure correlations between odd Fourier mass and additive energy,
12. test every proposed lemma.

Computational evidence is not a proof. Its purpose is to discover the correct theorem and locate counterexamples quickly.

---

# 25. Test families

Every new lemma must be tested against at least the following families.

### A. Consecutive integers

$$
V=\{1,2,\ldots,N\}.
$$

### B. Odd integers

$$
V=\{1,3,5,\ldots,2N-1\}.
$$

### C. Powers of two

$$
V=\{1,2,4,\ldots,2^{N-1}\}.
$$

### D. Translated intervals

$$
V=\{m,m+1,\ldots,m+N-1\}.
$$

### E. Random configurations

At multiple scales.

### F. High-energy configurations.

### G. Low-energy configurations.

### H. Configurations close to known extremal or computationally difficult cases.

Any counterexample to an intermediate lemma takes priority over developing the next stage of the proof.

---

# 26. Minimal collection of theorems required for a complete proof

The final argument should be decomposed into independent results.

## P1 — Geometric/CRT Equivalence

$$
\text{LRC}
\iff
(\Lambda-c)\cap K\neq\varnothing.
$$

## P2 — Dual-Lattice Theorem

Exact identification of

$$
\Lambda^\ast
$$

with the arithmetic relation space.

## P3 — Poisson Certificate

$$
S(c)=C\,F(V).
$$

## P4 — Parity Phase Theorem

$$
e^{2\pi i\langle c,\xi_a\rangle}
=
(-1)^{|a|}
$$

or the exact corrected formula.

## P5 — 2-adic Parity Theorem

Every odd relation has forced 2-adic complexity.

## P6 — Fourier Weight Decay

$$
w(a)\le G(\mathcal C(a)).
$$

## P7 — Additive Inverse Theorem for Bad Relations

Large odd dual mass implies high additive energy.

## P8 — 2-adic Structure Theorem

High energy together with parity information implies a suitably 2-adically structured GAP.

## P9 — Pseudorandom Branch

Pseudorandomness implies

$$
F(V)>0.
$$

## P10 — Structured Branch

Structured configurations imply

$$
F(V)>0
$$

or reduce to a smaller LRC instance.

## P11 — Minimal Counterexample Reduction

A hypothetical minimal counterexample produces a smaller counterexample.

## P12 — Final LRC

From P1–P11:

$$
\boxed{
\text{LRC holds for every }N.
}
$$

---

# 27. Risk hierarchy

The principal risks are:

### R1

The proposed parametrization of \(\Lambda^\ast\) may be incorrect.

### R2

The Fourier phase may not provide the exact parity structure required.

### R3

Odd relations may exist that are short and 2-adically simple, invalidating the intended parity theorem.

### R4

Large additive energy may give a GAP, but the resulting GAP may not preserve enough 2-adic information.

### R5

The structured branch may contain genuinely new extremal configurations that cannot be reduced.

### R6

The Fourier tail may be too large for relation counting alone to prove \(F(V)>0\).

Any such failure must be recorded explicitly rather than hidden by increasingly informal estimates.

---

# 28. No "proof by terminology"

The presence of names such as

* Balog–Szemerédi–Gowers,
* Freiman,
* Gowers,
* Weil,
* Kloosterman,
* large sieve,
* Poisson summation,
* inverse theorem,

does not constitute an argument.

For every external theorem used, record:

1. the exact statement,
2. all hypotheses,
3. the object to which it is applied,
4. the parameter correspondence,
5. the precise conclusion obtained,
6. all dependencies on \(N\) and other parameters.

If any of these are missing, mark the result as heuristic or incomplete.

---

# 29. Claim-status discipline

Every important mathematical statement must receive one of the statuses:

* `PROVED` — complete proof established,
* `VERIFIED` — formally/algorithmically verified,
* `KNOWN` — established result from the literature,
* `CONJECTURED` — project hypothesis,
* `HEURISTIC` — intuition only,
* `OPEN` — unresolved step,
* `DISPROVED` — explicit counterexample found.

Never silently promote

`HEURISTIC → PROVED`

or

`COMPUTATIONAL EVIDENCE → THEOREM`.

---

# 30. Minimal-progress principle

Every research stage should produce at least one of:

1. a complete proof of a lemma,
2. a counterexample,
3. a stronger or more natural reformulation,
4. a rigorous reduction to a known problem,
5. a precisely identified unresolved barrier.

Avoid producing long documents that merely restate intuition without reducing uncertainty.

---

# 31. Research order

The preferred order is

$$
\boxed{
P1\rightarrow P2\rightarrow P3\rightarrow P4
}
$$

then

$$
\boxed{
P5\rightarrow P6
}
$$

then

$$
\boxed{
P7\rightarrow P8
}
$$

and only after that

$$
\boxed{
P9/P10\rightarrow P11\rightarrow P12.
}
$$

Do not begin large-scale BSG/GAP arguments before the exact dual lattice and Poisson certificate are established.

---

# 32. First milestone

Create:

## `01_dual_lattice.md`

It must contain a complete proof of

$$
\text{LRC}
\iff
(\Lambda-c)\cap K\neq\varnothing
$$

and an explicit derivation of

$$
\boxed{
\Lambda^\ast
=
\text{exact relation lattice}.
}
$$

Include fully worked examples for

$$
N=2,3,4.
$$

If the initially conjectured form of the dual lattice is wrong, replace it with the correct one.

---

# 33. Second milestone

Create:

## `02_poisson_certificate.md`

It must contain:

1. the choice of \(\phi\),
2. support conditions,
3. the exact Fourier transform,
4. the Poisson formula,
5. the exact phase,
6. the definition of \(F(V)\),
7. a complete proof that

   $$
   F(V)>0\Rightarrow\text{LRC}.
   $$

---

# 34. Third milestone

Create:

## `03_2adic_parity.md`

It must contain:

1. the decomposition

   $$
   v_i=2^{s_i}u_i,
   $$
2. the layers \(I_s\),
3. the exact carry equations,
4. classification of relation types,
5. a precise parity theorem,
6. either a proof or an explicit counterexample.

---

# 35. Fourth milestone

Create:

## `04_relation_energy.md`

Determine an exact relationship of the form

$$
M_{\rm odd}
\longrightarrow
E_k(V).
$$

The first target should be a rigorous implication such as

$$
M_{\rm odd}\ge\eta
\Rightarrow
E_k(V)\ge f(\eta,N).
$$

---

# 36. Fifth milestone

Create:

## `05_structure_pseudorandomness.md`

Construct the complete quantitative dichotomy:

$$
\boxed{
\text{Pseudorandom}
\quad\text{vs.}\quad
\text{Structured}.
}
$$

Both branches must lead to formal mathematical consequences.

---

# 37. Sixth milestone

Create:

## `06_structured_branch.md`

Prove either

$$
\text{2-adic GAP}
\Rightarrow
\text{LRC},
$$

or

$$
\text{2-adic GAP}
\Rightarrow
\text{strictly smaller LRC instance}.
$$

---

# 38. Seventh milestone

Create:

## `07_global_proof.md`

Combine all established results into one proof.

The document must identify explicitly where each previous theorem is used.

---

# 39. Fallback strategy

If the complete proof cannot be closed, maximize mathematical value.

Potential publishable intermediate outcomes include:

### A

A new exact lattice/Fourier formulation of LRC.

### B

A new theorem controlling parity of dual relations.

### C

A new 2-adic additive-structure theorem.

### D

A new relation between signed Fourier mass and additive energy.

### E

A new reduction of LRC to a special class of GAP configurations.

### F

A proof of LRC for a new infinite family of configurations.

A failure to obtain the complete theorem is not a failure if one of these intermediate results is established rigorously.

---

# 40. Target architecture of the final proof

The final argument should have the form

$$
\begin{aligned}
&\text{Assume a counterexample }V.\\
&\Downarrow\\
&\text{CRT/lattice representation}\\
&\Downarrow\\
&(\Lambda-c)\cap K=\varnothing\\
&\Downarrow\\
&\text{Poisson certificate}\\
&\Downarrow\\
&F(V)\le0\\
&\Downarrow\\
&\text{large negative Fourier mass}\\
&\Downarrow\\
&\text{many odd dual relations}\\
&\Downarrow\\
&\text{2-adic parity theorem}\\
&\Downarrow\\
&\text{additive energy}\\
&\Downarrow\\
&\boxed{\text{Structure / Pseudorandomness}}\\
&\swarrow\hspace{45mm}\searrow\\
&\text{Pseudorandom}\hspace{25mm}\text{Structured}\\
&\Downarrow\hspace{45mm}\Downarrow\\
&F(V)>0\hspace{35mm}\text{GAP / reduction}\\
&\hspace{55mm}\Downarrow\\
&\hspace{40mm}\text{smaller counterexample}\\
&\hspace{55mm}\Downarrow\\
&\hspace{45mm}\text{contradiction}\\
&\Downarrow\\
&\boxed{\text{LRC}.}
\end{aligned}
$$

---

# 41. Core research principle

Do not force known theorems into the desired proof.

If a step requires a theorem stronger than currently available mathematics, explicitly label it

$$
\boxed{\text{OPEN LEMMA}}
$$

and investigate that lemma as an independent mathematical problem.

The most important candidate is:

$$
\boxed{
\text{large signed Fourier obstruction}
\Rightarrow
\text{2-adically structured additive configuration}.
}
$$

This implication may contain the main genuinely new difficulty of the program.

---

# 42. Success criterion

The program succeeds completely if it establishes, unconditionally,

$$
\boxed{
F(V)>0
\qquad
\forall N\ge1,\quad
\forall V\subset\mathbb Z_{>0},
\quad |V|=N,
}
$$

and therefore

$$
\boxed{
(\Lambda-c)\cap K\neq\varnothing,
}
$$

which implies

$$
\boxed{
\text{LRC holds for every }N.
}
$$

Every logical step must be independently verifiable.

---

# 43. First task for the research agent

Do **not** immediately attempt to prove LRC.

Proceed in exactly this order:

1. Define \(\Lambda\) rigorously.
2. Prove the equivalence with the original LRC condition.
3. Compute \(\Lambda^\ast\).
4. Verify the dual parametrization.
5. Derive the exact Poisson formula.
6. Compute the shift phase.
7. Verify whether the phase is genuinely

   $$
   (-1)^{\sum_i a_i}.
   $$
8. Verify all formulas symbolically and computationally for small \(N\).
9. Only then begin the 2-adic analysis.
10. Treat every counterexample to an intermediate claim as valuable mathematical information and revise the statement rather than hiding the failure.

**The first objective is not a proof of LRC. The first objective is to obtain an exact, error-free dual formulation of the problem.**

Only after that foundation is secure should the project develop the 2-adic and Structure/Pseudorandomness machinery.


---

# 44. Iterative task protocol

When a numbered `TASKn.md` is present and the user asks to continue the
research program:

1. read the entire current task before changing files;
2. attempt its stated outcomes with the strongest appropriate tools available,
   including exact symbolic derivations, integer-arithmetic computation, and
   reproducible exhaustive/random tests where useful;
3. distinguish `PROVED`, `VERIFIED`, `KNOWN`, `CONJECTURED`, `HEURISTIC`,
   `OPEN`, and `DISPROVED` exactly as required above;
4. save implementation and research artifacts in the task's requested layout;
5. after completing the audit, identify the narrowest unresolved barrier and
   write the next numbered task as `TASK(n+1).md`;
6. ensure that next task requests a genuinely new theorem, counterexample, or
   obstruction rather than merely another equivalent reformulation;
7. run the relevant checks, review the generated evidence, and commit the
   changes before creating the pull request.

“Best tools” never means replacing proof by computation: computer algebra,
exhaustive enumeration, optimization, and literature search are discovery and
verification tools unless a finite exhaustive argument and its scope are
proved explicitly.
