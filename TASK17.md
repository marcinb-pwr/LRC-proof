# TASK 17 — Interval-Sensitive Intersection Theorem

## Starting point

TASK 16 optimized all spanning-tree certificates and added exact triple
intersections. Both methods fail on the safe configuration $(1,3,4,5)$, while
no covered canonical two-label grid has been found.

## Objective

Prove or disprove an interval-sensitive inequality that can decide the
canonical grid beyond the first three intersection moments.

## Required work

1. Use the fact that each bad set is the inverse image of a single centered modular arc; do not replace it by an arbitrary subset of its period.
2. Classify the connected components after lifting two strips to their lcm and prove exact endpoint formulas for adding a third strip.
3. Test every proposed inequality first on $(1,3,4,5)$ and on all TASK 14 obstructions.
4. Determine whether a bounded-order intersection theorem can force an uncovered class; if not, give two exact systems with matching proposed summaries but different coverage.
5. Continue an M-free adversarial search for a covered canonical two-label grid and provide a compact CRT certificate for any example found.
6. State the narrowest surviving theorem or counterexample, update global status, and create `TASK18.md` only for genuinely new progress.
