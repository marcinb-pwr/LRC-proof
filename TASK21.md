# TASK 21 — Quantitative Triple All-Safe Bound

## Starting point

TASK 20 exactly computes all 64 cells of a labelled triple transition table.
Full phase data reconstructs the system, but exact reconstruction alone is not
a uniform proof of a surviving gap.

## Objective

Obtain a genuinely quantitative lower bound for triple all-safe mass or find a
covered canonical two-label grid.

## Required work

1. Express the all-safe state and its incoming transitions directly as intersections of three complements of centered multiplier arcs.
2. Use the divisor restrictions on $(H_i,a_i,c_i,\rho_i)$ to seek a lower bound not valid for arbitrary modular subsets.
3. Separate bounds that merely restate exact enumeration from bounds uniform in the velocities.
4. Test every candidate on $(1,3,4,5)$, all TASK 14 obstructions, and every applicable required family.
5. Search adversarially for zero all-safe mass using the lcm period, never $qW$; certify any example by compact CRT residue data.
6. If triple bounds cannot control the union of all runners, state the precise additional multiplicity hypothesis required.
7. Update global status and create `TASK22.md` only after genuine progress.
