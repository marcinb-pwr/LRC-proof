# TASK 18 — Modular-Multiplier Fragmentation

## Starting point

TASK 17 proved common-scale invariance, constructed an exact component
recursion, and disproved every coverage criterion depending only on the first
three aggregate intersection moments, even for centered cyclic arcs.

## Objective

Use the labelled divisor constraints of LRC to control how the modular
multipliers fragment centered arcs in the canonical lcm-grid ordering.

## Required work

1. Derive the multiplier acting on each centered arc after division by
   $\gcd(d,qb_i)$ and record its exact order and continued-fraction data.
2. Prove a nontrivial upper or lower bound on component fragmentation that uses
   $b_i=W/v_i$, not an arbitrary unit modulo $H_i$.
3. Test every claim on $(1,3,4,5)$, all TASK 14 obstructions, powers of two,
   consecutive integers, odd integers, translated intervals, and seeded random inputs.
4. Determine whether fragmentation plus total strip length forces a surviving
   gap; otherwise find and certify a covered canonical two-label grid.
5. Do not use common scaling as progress: Theorem 35 proves it is neutral.
6. Update global status and create `TASK19.md` only after a new theorem,
   counterexample, or sharply stated obstruction.
