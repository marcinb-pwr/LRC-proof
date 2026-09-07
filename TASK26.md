# TASK 26 — Four-Anchor Certificate: Theorem or Counterexample

## Starting point

TASK 25 proves that four largest-mass transition anchors define at most 256
fibers and require CRT intersections only through order ten. The resulting
quadratic certificate succeeds on every current exhaustive and seeded input,
but this is computational evidence only.

## Objective

Prove that some four-anchor transition fiber has positive quadratic value for
every admissible canonical grid, under explicit LRC divisor constraints, or
find a compact LRC-derived counterexample.

## Required work

1. Express each of the at most 256 quadratic values directly through the
   phase records $(H_i,a_i,c_i,\rho_i)$ and generalized CRT histograms.
2. Use the largest-mass ordering and divisor relations; do not replace the
   anchors by arbitrary cyclic subsets.
3. Derive a uniform inequality stronger than exact reconstruction, or state a
   precise phase hypothesis under which positivity follows.
4. Search adversarially for failures at larger $N$, highly composite lcm
   patterns, valuation-separated families, and near-extremal configurations.
5. Never scan $qW$; use the canonical lcm period and compact fiber histograms.
6. Test all TASK 14 obstructions and the TASK 22--24 decisive records.
7. If a failure is found, minimize it and store all four anchor phase records,
   realized fiber histograms, and quadratic values.
8. Update global status and create `TASK27.md` only after a theorem,
   counterexample, or sharply isolated obstruction.
