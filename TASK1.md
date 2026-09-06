# TASK: Execute the Next Mathematical Research Step

You are working inside a mathematical research repository whose overall goal is to investigate a possible proof of the Lonely Runner Conjecture.

The repository contains:

* `AGENTS.md`
* `01_dual_lattice.md`
* `02_poisson_certificate.md`
* `03_2adic_parity.md`
* `04_relation_energy.md`
* `05_structure_pseudorandomness.md`
* `06_structured_branch.md`
* `07_global_proof.md`

The repository deliberately distinguishes between PROVED, VERIFIED, CONJECTURED, HEURISTIC, OPEN, and DISPROVED statements.

## Your role

Act as a mathematical research agent, not as a text editor.

Do not merely restate the research program.

Do not stop because the Lonely Runner Conjecture is open.

Do not attempt to prove the entire conjecture in one step.

Your task is to make genuine mathematical progress on the next unresolved lemma.

---

# Immediate objective

Investigate the proposed 2-adic parity mechanism for dual relations.

The central unresolved question is:

> For a relation
>
> $$
> a\in\mathbb Z^N,
> \qquad
> \sum_i a_i v_i\equiv0\pmod{qW},
> \qquad q=N+1,
> $$
>
> what restrictions does
>
> $$
> \sum_i a_i\equiv1\pmod2
> $$
>
> impose on the 2-adic structure of \(a\)?

The goal is NOT to assume that the proposed parity theorem is true.

The goal is to determine whether a rigorous theorem of this type is actually true, and if so to discover and prove the strongest useful version.

---

# Phase 1 — Audit the existing formulation

Before attempting a proof:

1. Read `01_dual_lattice.md`.
2. Read `02_poisson_certificate.md`.
3. Read `03_2adic_parity.md`.
4. Independently verify the exact relation space

   $$
   D=
   \left\{
   a\in\mathbb Z^N:
   \sum_i a_iv_i\equiv0\pmod{qW}
   \right\}.
   $$
5. Verify the phase

   $$
   e^{2\pi i\langle c,\xi_a\rangle}
   =
   (-1)^{\sum_i a_i}.
   $$
6. Identify any mathematical error in these documents.

If an error exists, fix the mathematical statement first and record exactly what changed.

Do not preserve a false statement merely because it is part of the existing research plan.

---

# Phase 2 — Build a computational laboratory

Create a reproducible Python research script/package under:

```
research/2adic/
```

It should be able to accept a finite set

```
V = [v1, ..., vN]
```

and compute:

* q,
* W,
* b_i,
* the modulus qW,
* the relation lattice D modulo the coordinate periods q b_i,
* representatives of dual relations,
* parity

  $$
  \sum_i a_i\bmod2,
  $$
* the valuation profile

  $$
  \nu_2(v_i),
  $$
* the quantities

  $$
  B_s(a)=\sum_{i\in I_s}a_i u_i,
  $$
* exact carry data through the 2-adic filtration.

Do NOT enumerate an infinite relation lattice directly.

Work with canonical representatives modulo

$$
a_i\sim a_i+qb_i m_i.
$$

Explicitly verify that all quantities used by the program are invariant under this quotient, or document which quantities are representative-dependent.

---

# Phase 3 — Exhaustive small-case search

For small N, perform an exhaustive search over many configurations V.

At minimum investigate:

* N = 2,...,8
* all distinct positive v_i below a reasonable bound
* random configurations at larger scales
* arithmetic progressions
* odd configurations
* powers of two
* mixed 2-adic valuation layers
* configurations with many common divisors
* configurations normalized by gcd(V)=1

For each configuration enumerate all sufficiently short relation representatives a.

Record:

1. support size,
2. l1 norm,
3. l_infinity norm,
4. parity of sum a_i,
5. number of active 2-adic layers,
6. carry depth,
7. number of nontrivial carries,
8. the full carry profile,
9. whether the relation is genuinely distinct modulo the dual-lattice quotient.

The purpose is to search for the strongest empirical invariant satisfied by every odd relation.

---

# Phase 4 — Falsify the naive parity lemma

Explicitly test the following candidate statement:

> Every dual relation with
>
> $$
> \sum_i a_i\equiv1\pmod2
> $$
>
> must involve at least two distinct 2-adic valuation layers.

Do NOT assume this is true.

Search for the smallest counterexample.

If the statement is false, determine the correct weakened statement.

Examples of possible corrected forms:

* an odd relation supported inside one layer is possible only under a specific divisibility condition;
* odd parity forces a carry at a specified depth;
* odd parity forces a minimum support size;
* odd parity forces a lower bound on a weighted 2-adic complexity;
* odd parity forces interaction between one layer and the modulus qW.

The goal is to discover the exact structural invariant, not to defend the original formulation.

---

# Phase 5 — Prove the strongest valid 2-adic theorem

Once computational evidence identifies a candidate statement, attempt a formal proof from

$$
\sum_i a_i2^{s_i}u_i\equiv0\pmod{qW}.
$$

Use exact congruence manipulations.

Potential tools:

* reduction modulo successive powers of 2,
* valuation arguments,
* induction over the valuation layers,
* carry recurrences,
* parity of odd units,
* quotienting by the highest common 2-power.

Do not invoke additive combinatorics yet.

The output should be a theorem whose hypotheses and conclusion are completely explicit.

For example:

## Candidate format

There exists a function C_2(a,V) such that

$$
\sum_i a_i\equiv1\pmod2
\quad\Longrightarrow\quad
C_2(a,V)\ge L(V,N).
$$

The exact definition of C_2 must be discovered and justified.

---

# Phase 6 — Connect 2-adic complexity to Fourier weight

After proving a genuine parity/2-adic lemma, return to the Fourier weight in
`02_poisson_certificate.md`.

For the chosen test function,

$$
w(a)=\widehat\phi(\xi_a).
$$

Derive the strongest possible explicit bound in terms of the relation complexity.

For example, investigate whether one can prove a bound of the form

$$
w(a)
\le
G(C_2(a,V),\|a\|_1)
$$

for an explicitly summable function G.

Then determine whether the parity theorem implies a nontrivial global bound on

$$
M_{\rm odd}
=
\sum_{\substack{a\in D_0\\\sum_i a_i\text{ odd}}}
w(a).
$$

Do not assume that it does.

---

# Phase 7 — Research deliverables

At the end of this task, produce the following files:

```
research/2adic/README.md
research/2adic/experiments.py
research/2adic/results.json
research/2adic/theorem.md
```

`theorem.md` must contain exactly one of:

### Outcome A — Theorem proved

A rigorous new theorem is proved, with full proof.

### Outcome B — Original theorem disproved

Give the smallest counterexample found and explain exactly which statement fails.

### Outcome C — Original theorem false, stronger/corrected theorem discovered

State the corrected theorem and give evidence plus as much proof as possible.

### Outcome D — No useful theorem yet

State precisely what was tested, what remains unresolved, and what the strongest experimentally supported conjecture is.

Do not manufacture a proof.

---

# Phase 8 — Do not move prematurely to BSG/Freiman

Do NOT start `05_structure_pseudorandomness.md` yet.

The immediate research bottleneck is to establish whether the 2-adic parity mechanism actually gives a rigorous restriction on negative Fourier terms.

Only after obtaining a nontrivial theorem here should the project move to:

$$
\text{odd dual mass}
\rightarrow
\text{additive energy}
\rightarrow
\text{structure}.
$$

---

# Definition of success

This task is successful even if LRC is not proved.

A successful result is any rigorous theorem that strengthens our understanding of

$$
\sum_i a_iv_i\equiv0\pmod{qW}
$$

under

$$
\sum_i a_i\equiv1\pmod2.
$$

The agent must finish this task with a mathematically useful result, a counterexample, or a precisely characterized obstruction.

Do not respond with a general discussion of how hard LRC is.

Perform the mathematics.
Run the experiments.
Attempt the proof.
Write the results to the repository.

