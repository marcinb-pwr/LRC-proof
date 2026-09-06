# TASK 20 — Labelled Pair Data and Triple Gap Destruction

## Starting point

TASK 19 derives exact labelled joint-transition tables and pair-complement
component counts. Aggregating these tables loses decisive coverage information.

## Objective

Determine whether complete labelled pair tables, together with the LRC-derived
multiplier phases, control how a third strip destroys pairwise gaps.

## Required work

1. Derive exact three-label transition tables by generalized CRT, retaining all eight before/after states.
2. Relate those tables to the change in component count when a third labelled strip is inserted.
3. Seek a rigorous inequality reconstructing a surviving component from complete labelled pair data plus the phases in (58).
4. If such reconstruction fails, find two exact LRC-derived systems—not arbitrary arcs—with matching labelled pair summaries and different coverage.
5. Test $(1,3,4,5)$, all TASK 14 obstructions, and all applicable required families before broad random search.
6. Keep all searches M-free and provide a compact CRT certificate for any covered canonical grid.
7. Update global status and create `TASK21.md` only after genuine progress.
