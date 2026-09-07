# TASK 27 — Is Anchor Complexity Uniformly Bounded?

## Starting point

TASK 26 disproves four-anchor positivity with the seven-label TASK 14 system
$(1,5,6,7,8,11,13)$.
Five anchors certify that example, but choosing the next constant
experimentally is not a structural theorem.

## Objective

Determine whether there is an absolute $k$ for which the $k$-anchor
transition-fiber quadratic always certifies every admissible canonical grid,
or construct a family whose required anchor count tends to infinity.

## Required work

1. Define the minimum anchor complexity $k_*(V)$ under the deterministic
   largest-mass rule, including configurations never certified.
2. Derive monotonicity under fiber refinement and state why positivity, once
   obtained, persists for refinements.
3. Search for configurations with $k_*(V)\ge6$ using valuation-separated,
   highly composite, interval, odd, power, and seeded adversarial families.
4. Attempt a product/lifting construction that raises $k_*(V)$ while
   preserving the LRC-derived phase constraints and canonical hypothesis.
5. Distinguish an absolute bound, an $N$-dependent bound, and full
   reconstruction; quantify fiber counts and CRT order in each case.
6. Use only canonical lcm periods and store compact phase records for every new
   lower bound on $k_*$.
7. Retest all prior decisive configurations, especially the TASK 26 example.
8. Update global status and create `TASK28.md` only after genuine progress.
