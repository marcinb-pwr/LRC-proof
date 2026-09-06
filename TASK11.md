# TASK 11 — Ordered Endpoint Words and Prefix-Sum Obstructions

## Starting point

TASK 10 proved that every off-core bad set is a disjoint union of explicitly
translated integer intervals and supplied an exact endpoint sweep.  It also
proved the localized certificate

\[
N A_D-2P_D<N|D|\Longrightarrow\text{an uncovered residue}.
\]

This improves the union bound for an infinite scalable class, but certified
only 315 of 3,546 audited records.  Moreover, \((1,4,12)\) and \((2,3,12)\)
have identical \((M,S,P,T,P_D)\) and different endpoint partitions.  Aggregate
moments therefore discard relevant cyclic-order information.

## Objective

Determine whether the arithmetic order of the signed block endpoints forces a
zero prefix sum.  Produce a theorem for a genuine infinite normalized class,
an explicit counterexample to a natural endpoint-order conjecture, or a
precise finite-state obstruction.

## Required work

1. Encode the coalesced off-core sweep as the ordered word
   \((x_j,\delta_j)\), where \(x_j\) is an endpoint coordinate and
   \(\delta_j\) its net signed change.  State exactly which words can arise
   from periods \(qb_i\), radii \(b_i-1\), and \(b_i\mid W\).
2. Derive congruence, spacing, symmetry, and pairing restrictions on this word.
   Separate restrictions valid for arbitrary interval systems from those
   forced by the CRT parameters.
3. Seek a prefix-sum theorem implying that some constant segment has
   multiplicity zero.  Any proposed criterion must be tested before being
   promoted to `PROVED`.
4. Implement the word without scanning \(M\), and exhaust all gcd-one subsets
   of \(\{1,\ldots,L\}\) for the largest feasible \(L\), together with divisor
   and standard families.  Preserve the smallest counterexample to each
   endpoint-spacing or interlacing conjecture.
5. Classify at least one nontrivial infinite normalized family (not merely all
   common scalar multiples of one configuration), or state explicitly why
   the tested word restrictions do not yield such a class.
6. Search for two realizable configurations with the same proposed finite
   endpoint summary but different zero-prefix behavior.  An exact collision
   is an acceptable obstruction; do not claim different cover behavior unless
   an actual LRC counterexample has been independently verified.
7. Update `research/covering/` with exact reproducible code, deterministic
   results, proofs, and claim statuses.

Do not replace the ordered word by another unlocalized moment or Fourier
inversion.  The task is specifically to retain and exploit cyclic endpoint
order.
