# TASK 25 — Bounded-Complexity Phase Refinement

## Starting point

TASK 24 proves a localized quadratic certificate, but the four transition
fibers of one anchor mix safe and multiply covered points. Singleton fibers
would merely reconstruct the answer and are not an acceptable bound.

## Objective

Find a uniformly bounded-complexity, phase-defined refinement on which the
quadratic or another rigorous low-multiplicity statistic forces a safe class,
or prove that every refinement in a precisely specified bounded class can
fail.

## Required work

1. Define the partition solely from a fixed number of labelled phases and
   transition boundaries, before inspecting global safe points.
2. Quantify its number of fibers independently of $L$; singleton or full
   residue reconstruction is excluded.
3. Prove the sign implication for the chosen localized statistic and derive
   its exact CRT intersection order.
4. Test refinements by two anchors, short transition words, and coarse arc
   coordinate bins; distinguish each candidate formally.
5. Determine the least refinement that handles $(1,3,4,5)$ and whether it
   also handles the TASK 22--23 certificates.
6. Test all TASK 14 obstructions and applicable required families, using only
   the lcm grid.
7. Store compact phase/fiber certificates for the first failure of each
   candidate class.
8. Update global status and create `TASK26.md` only after genuine progress.
