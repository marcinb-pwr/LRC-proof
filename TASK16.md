# TASK 16 — Decide the Canonical Two-Label Grid

## Starting point

TASK 15 proved that the apparent two-direction torus is cyclic of order
$q\operatorname{lcm}(v_*,v^\dagger)$, resolved all 19 TASK 14 obstructions,
and found no covered quotient among 18,969 normalized inputs. It did **not**
prove that the canonical two-label grid always succeeds.

## Objective

Decide open assertion (41), rather than introducing another equivalent
parameterization of the same cyclic subgroup.

## Required work

1. Attempt to prove (41) using the exact labelled strips and formula (38).
2. Optimize the spanning-tree certificate (39) exactly and prove every reduction used.
3. If it fails, retain triple intersections via generalized CRT and derive a rigorously signed certificate.
4. Search beyond velocity 15 using systematic and seeded adversarial families, without scanning $qW$.
5. If a counterexample appears, prove its finite coverage compactly and define a canonical third-label rule before testing it.
6. If none appears, do not infer a theorem from computation; isolate the exact gcd-intersection inequality needed.
7. Update global status, add reproducible artifacts, and create `TASK17.md` only after a genuinely new theorem or obstruction.
