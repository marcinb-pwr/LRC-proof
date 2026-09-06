# TASK 15 — A Two-Direction Clearance Torus

## Starting point

TASK 14 converted the step parameter into exact modular arcs with canonical
period \(qv_*\), disproved universal one-direction coverage using 19 exact
finite obstructions, and proved LRC for the mixed-fringe family
\(\{1,3,4m\}\). The smallest full-period obstruction is
\((1,3,4,5,7,18)\); it is not an LRC counterexample.

## Objective

Choose a second direction from the labelled divisor poset and determine
whether a two-parameter subgroup forces an uncovered point or exposes a
precise higher-dimensional obstruction.

## Required work

1. Define \(b^\dagger\) canonically from the runners that cover the
   one-dimensional step word; do not optimize it after seeing a safe point.
2. Derive the exact period lattice of
   \(x=W+h b_*+k b^\dagger\) and its Smith normal form.
3. Express every runner's bad parameters as an affine modular strip on the
   finite two-dimensional quotient.
4. Test all 19 TASK 14 full-period obstructions first, then exhaust the largest
   feasible normalized input range without scanning \(M\).
5. Prove a strip-union or intersection certificate, preserving runner labels
   and pairwise gcd information.
6. Record the smallest configuration whose entire two-direction torus is
   covered; do not call it an LRC counterexample.
7. State the exact Fourier transform of a modular strip before considering
   cancellation. Do not invoke Weil or Kloosterman bounds unless a nonlinear
   inverse phase actually appears.
8. Prove a new infinite family or isolate the narrowest remaining
   higher-dimensional obstruction; add reproducible artifacts and TASK16.
