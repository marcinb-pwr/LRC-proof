# TASK 10 — Off-Core Localization and Gap Geometry

## Starting point

TASK 9 proved the centered CRT pair formula, the triple/slack comparison, and
the canonical forced core

\[
C=\{0,\ldots,\beta-1\}\cup\{M-\beta+1,\ldots,M-1\},
\qquad \beta=\min_i b_i.
\]

It also disproved raw pair overlap as a useful universal discriminator: 797 of
806 audited normalized configurations satisfy the necessary-cover inequality
\(P\ge\Delta\), although the tested bad sets do not cover. Triple mass is
pointwise coupled to \(P-\Delta\), so another unlocalized moment is not a new
route.

## Objective

Determine whether the *locations* of off-core intersections force an
uncovered gap. Produce a theorem, counterexample, or precise obstruction that
uses the cyclic order and endpoint-block geometry, not only global moments.

## Required work

1. Decompose the complement of `C` into maximal cyclic intervals and represent
   every restriction \(B_i\setminus C\) as explicit translated blocks there.
2. Define exact gap statistics: longest safe run, distances between changes of
   multiplicity, and off-core overlap per interval. Prove which are invariant
   under normalization and scaling.
3. Derive a sweep-line or interval-endpoint formula that decides covering
   without iterating all \(M\) residues. State its bit complexity.
4. Test all normalized subsets of `{1,...,L}` for the largest feasible `L`,
   divisor families of highly composite `W`, and the standard test families.
   Preserve the smallest counterexample to every proposed inequality.
5. Seek a sufficient inequality of the form

   \[
   \text{localized off-core overlap or endpoint discrepancy}<\text{explicit threshold}
   \Longrightarrow \text{an uncovered residue}.
   \]

   It must hold for a nontrivial infinite class, or be explicitly disproved.
6. Compare configurations with similar \((M,S,P,T,P_{\rm off})\) but different
   covering behavior. If these statistics cannot determine covering, give an
   exact collision; this is an acceptable rigorous obstruction.
7. Update `research/covering/` with reproducible exact code and results. Label
   every claim `PROVED`, `VERIFIED`, `DISPROVED`, or `OPEN`.

Do not repackage inclusion-exclusion or Fourier inversion as an outcome. The
new information must exploit cyclic localization. After the audit, create
`TASK11.md` from the narrowest barrier actually found.
