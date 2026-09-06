# TASK 12 — Labelled Endpoint Pairing and the Divisibility Poset

## Starting point

TASK 11 derived the exact ordered endpoint word, reflection antisymmetry, and the runner-labelled congruences and paired spacings. It proved LRC for the infinite normalized class with no velocity divisible by \(q=N+1\), but disproved naive alternation, unit-change, and minimum-spacing conjectures. The remaining information is not merely the unlabelled word: it is the association of endpoint pairs to divisors \(b_i\mid W\).

## Objective

Determine whether the labelled pairing and the divisibility poset force a zero prefix when one or more velocities are divisible by \(q\). Produce a theorem for a genuinely new infinite normalized class, a counterexample to a precise labelled-pair conjecture, or a finite-state obstruction that cannot be expressed by the unlabelled word alone.

## Required work

1. Encode every event with its runner, period, mate, clipping status, and residue class; preserve coincident events rather than retaining only their net change.
2. Derive all implications of \(b_i\mid W\), including the gcd/lcm poset of periods and compatibility of coincidences between two labelled pairs.
3. Split at \(x=W\). Classify exactly which runners cover \(W\) (equivalently \(q\mid v_i\)) and determine the first labelled events on either side.
4. Test a precise descent conjecture: if \(W\) is covered, does the innermost covering pair force a safe segment, or reduce to the subconfiguration \(q\mid v_i\)? Record the smallest counterexample to every version.
5. Exhaust all gcd-one subsets of \(\{1,\ldots,L\}\) for the largest feasible \(L\), and include standard, divisor, and families containing multiples of \(q\). Use exact integer arithmetic and do not scan \(M\).
6. Prove a new infinite normalized class not contained in Theorem 15, or state the exact labelled obstruction that prevents it.
7. Update `research/covering/` with reproducible code, deterministic results, proofs, and explicit claim statuses.

Do not discard runner labels by passing to a moment, sign histogram, or gap multiset. Computation remains verification unless its finite scope is part of a proved exhaustive argument.
