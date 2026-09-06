# TASK 9 — Arithmetic Pair-Overlap and Higher-Multiplicity Obstructions

## Starting point

`TASK8.md` has produced an exact periodic covering model.  For normalized
(V=\{v_1,\ldots,v_N\}), put (q=N+1), (W=\operatorname{lcm}(V)),
(M=qW), and

\[
B_i=\{k\pmod M:\|kv_i/M\|<1/q\}.
\]

The following statements are **PROVED** in `research/covering/theorem.md`:

\[
|B_i|=2W-v_i,\qquad
\Delta=\sum_i|B_i|-M=(N-1)W-\sum_i v_i,
\]

and every cover must satisfy

\[
P:=\sum_{i<j}|B_i\cap B_j|\ge\Delta,qquad
P-\Delta=\sum_k\binom{m(k)-1}{2}.
\]

Pair intersections have an exact common-period/CRT block formula.  The generic
second-moment inequality is sharp for unrestricted set systems, so another
abstract moment manipulation cannot resolve the problem.

## Objective

Exploit arithmetic restrictions on the endpoint blocks to obtain information
that arbitrary set systems do not have.  Produce one of:

1. a proved upper bound (P<\Delta) for a nontrivial infinite class;
2. a proved structural classification of cases with (P\ge\Delta);
3. a higher-multiplicity inequality specific to the periodic blocks;
4. an explicit counterexample disproving a proposed universal overlap bound;
5. a rigorous obstruction showing which statistics still cannot suffice.

Do **not** claim that (P<\Delta) universally: first test it, since it is an
open candidate and may be false even for many LRC-satisfying configurations.

## 1. Derive a closed pair formula

Replace the finite sum in Theorem 3, where possible, by a formula using

\[
b_i=W/v_i,\quad b_j=W/v_j,\quad d=\gcd(b_i,b_j),
\]

and explicit floor functions.  Split the two endpoint blocks into four pairs
(left-left, left-right, right-left, right-right), handle duplicated zero
correctly, and prove every CRT count.  Determine precisely what information
beyond (d) is necessary.

## 2. Normalize pair parameters

Use (b_i=d r), (b_j=d s), (\gcd(r,s)=1).  Seek upper and lower bounds for
(|B_i\cap B_j|) with explicit errors independent of (W), and identify the
extremizers.  Every bound must be checked at strict endpoints.

## 3. Test the candidate obstruction before proving it

Extend the experiment over:

* all distinct normalized subsets of \(\{1,\ldots,L\}\) for feasible (L);
* divisor sets of highly composite (W);
* consecutive, odd, powers-of-two, and translated families;
* configurations maximizing (P-\Delta).

Record the smallest counterexample to every candidate inequality.  Use exact
integer arithmetic.  Add checkpointing or optimized bitsets if exhaustive
search becomes expensive.

## 4. Study triple multiplicity exactly

Compute

\[
T=\sum_{i<j<\ell}|B_i\cap B_j\cap B_\ell|
 =\sum_k\binom{m(k)}3.
\]

Derive the exact common-period CRT formula and identities involving
(P-\Delta).  In particular, quantify how (P>\Delta) forces points of
multiplicity at least three and determine whether periodicity forces more
triple overlap than an arbitrary integer multiplicity sequence.

## 5. Residue-class localization

The proof must use that every (B_i) consists of two endpoint blocks modulo
(qb_i).  Investigate localization near (k=0), where all sets overlap, and
its translates.  Separate this forced common core from the remaining overlap;
otherwise the pair statistic may be dominated by information irrelevant to
covering the middle residues.

Define and test a renormalized statistic such as

\[
P_{\mathrm{off}}=
\sum_{i<j}|(B_i\cap B_j)\setminus C|,
\]

where (C) is a canonically proved forced core, not an empirically chosen
window.

## 6. Fourier comparison

Write the exact finite Fourier expansion of (1_{B_i}) and derive Parseval's
identity for (P).  Compare this formula term-by-term with the triangular
kernel from the full-dual certificate.  This is useful only if it yields a new
bound or isolates a signed arithmetic term; another equivalent transform is
not an outcome.

## 7. Deliverables

Update `research/covering/` with optimized exact intersection and exhaustive
search code, refreshed deterministic `results.json`, and an expanded
`theorem.md`.  Every central statement must carry a claim status.

The preferred theorem is:

\[
\boxed{
P\ge\Delta
\Longrightarrow
\text{an explicit arithmetic structure among the }b_i
}
\]

with a consequence that advances LRC for a genuine infinite family.  If this
is false, preserve the minimal counterexample and formulate the corrected
statement.  The next task must be selected from the narrowest barrier revealed
by this audit, not predetermined.
