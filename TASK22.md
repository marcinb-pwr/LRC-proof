# TASK 22 — Restricted Incidence on a Triple-Safe Set

## Starting point

TASK 21 proves quantitative lower bounds for the set $S_T$ safe for three
labels, including positivity for divisor-aligned triples when $q\ge7$. Other
runners can still cover $S_T$.

## Objective

Prove the strict restricted-multiplicity inequality

$$
\sum_{r\notin T}|A_r\cap S_T|<|S_T|
$$

for a canonically chosen triple, under an explicit LRC-derived hypothesis, or
find a canonical system disproving the proposed hypothesis.

## Required work

1. Express every $|A_r\cap S_T|$ by labelled generalized-CRT data, without
   scanning $qW$.
2. Choose $T$ by a rule independent of knowledge of a safe point.
3. Seek a bound using the divisor relations among $(H_p,a_p,c_p,\rho_p)$;
   do not substitute arbitrary modular subsets.
4. Separate unconditional inequalities, conditional theorems, and exact
   enumeration identities.
5. Test $(1,3,4,5)$, all TASK 14 obstructions, and every applicable required
   family.
6. Search adversarially on the lcm grid for failure of each proposed strict
   inequality and store a compact labelled CRT certificate for the first
   failure.
7. Determine whether averaging over triples yields a strictly stronger
   multiplicity statement; prove the averaging weights and endpoint cases.
8. Update global status and create `TASK23.md` only after obtaining a theorem,
   a counterexample, or a sharply isolated obstruction.
