# TASK 19 — Pairwise Fragmentation Alignment

## Starting point

TASK 18 gives an exact reduced multiplier and exact component count for every
individual bad strip. Individual fragmentation does not record how components
from different runner labels align.

## Objective

Control shared transitions and gap destruction for two labelled modular
progressions using their gcd/divisor relations.

## Required work

1. Derive exact CRT conditions for a point and its successor to lie in specified combinations of two strips.
2. Express shared boundary/transition counts through $(a_i,H_i)$, $(a_j,H_j)$ and their gcd, retaining centered-arc endpoints.
3. Prove a bound that is stronger than intersection cardinality alone, or give an exact counterexample to each proposed bound.
4. Test first on $(1,3,4,5)$ and all 19 TASK 14 obstructions, then on every required family satisfying the central-cover hypotheses.
5. Determine whether pairwise transition data forces a surviving gap; otherwise exhibit matching transition summaries with different coverage.
6. Continue the M-free covered-grid search and provide a compact exact certificate if one is found.
7. Update global status and create `TASK20.md` only after genuine new progress.
