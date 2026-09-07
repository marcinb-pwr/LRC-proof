# Finite covering experiments

Run from the repository root:

```bash
python3 research/covering/experiments.py
```

The code uses integer arithmetic throughout. It constructs strict bad sets,
checks their periodic blocks and sizes, compares the centered closed pair
formula against an independent common-period scan, checks the canonical forced
core, computes pair/triple/off-core moments, and writes deterministic output
to `results.json`.

The exhaustive component covers normalized subsets of `{1,...,10}` of sizes
2 through 6 when `M <= 200000`. Computations are labelled `VERIFIED`, never
`PROVED`; proofs and exact scope statements are in `theorem.md`.

For the TASK 10 endpoint-localization audit, run:

```bash
python3 -m unittest research/covering/test_localization.py
python3 research/covering/task10_experiments.py
```

`localization.py` constructs translated off-core blocks and sweeps their
endpoints without scanning all `M` residues.  The deterministic TASK 10 output
is `task10_results.json`; its exhaustive scope is every gcd-one subset of
`{1,...,12}` of sizes 2 through 7, plus the documented standard and highly
composite divisor families.

For the TASK 11 ordered-word audit, run:

```bash
python3 research/covering/test_endpoint_words.py
python3 research/covering/task11_experiments.py
```

`endpoint_words.py` retains coalesced signed endpoints and prefix segments without scanning the modulus. `task11_results.json` records the exhaustive scope, smallest counterexamples to three natural order conjectures, and the finite-summary collision search.

For the TASK 12 labelled-pair audit, run:

```bash
python3 research/covering/test_labelled_pairs.py
python3 research/covering/task12_experiments.py
```

`labelled_pairs.py` preserves the runner, period, mate, clipping state, and residue of every event. `task12_results.json` records the exhaustive central-cover and innermost-boundary audit.

For the TASK 13 central-fringe audit, run:

```bash
python3 research/covering/test_central_fringe.py
python3 research/covering/task13_experiments.py
```

`central_fringe.py` computes exact signed clearances at `W +/- h*b_star`
without scanning the modulus. The experiment verifies the complete first-fringe
residue classification through all gcd-one subsets of `{1,...,18}`.

For the TASK 14 step-clearance audit, run:

```bash
python3 research/covering/test_step_clearance.py
python3 research/covering/task14_experiments.py
```

`step_clearance.py` stores every bad-step condition as a compact affine
modular arc and derives the canonical period `q*v_star`. The deterministic
output is `task14_results.json`.

For TASK 15, run:

```bash
python3 research/covering/test_two_direction.py
python3 research/covering/task15_experiments.py
```

`two_direction.py` selects the canonical active second label, computes the period lattice/SNF invariants and modular strips, and evaluates exact labelled gcd intersections. `task15_results.json` checks all 19 TASK 14 obstructions and the exhaustive normalized range `{1,...,15}` without scanning `M=qW`.

For TASK 16, run:

```bash
python3 research/covering/test_covering_certificates.py
python3 research/covering/task16_experiments.py
```

`covering_certificates.py` computes generalized-CRT intersections, the exact maximum-spanning-tree bound, and the third Bonferroni bound. The deterministic `task16_results.json` separates theorem status from exhaustive and seeded verification.

For TASK 17, run:

```bash
python3 research/covering/test_interval_components.py
python3 research/covering/task17_experiments.py
```

`interval_components.py` performs the exact labelled endpoint recursion on the cyclic lcm grid. The audit also checks common-scale invariance and records two centered-arc systems with equal first three intersection moments but different coverage.

The resolution distinction in Theorem 35 has an additional raw,
non-normalizing regression check:

```bash
python3 research/covering/test_scale_invariance.py
```

It verifies separately that scaling creates more real time coordinates while
repeating, rather than refining, the simultaneous runner-phase word. It also
holds the velocities fixed and genuinely refines the time mesh, checking that
the refined and exact endpoint grids have equivalent safe-point existence.
It also computes the best margin exactly as a rational number and checks the
monotone nested-grid approximation at refinements 1, 2, and 4. The sharp
configuration `(1, 2)` is checked through refinement 100: its optimum remains
exactly zero on every grid.

For TASK 18, run:

```bash
python3 research/covering/test_multiplier_fragmentation.py
python3 research/covering/task18_experiments.py
```

`multiplier_fragmentation.py` derives the reduced unit, inverse multiplier, multiplicative order, Euclidean continued fraction, and exact component count of every labelled strip. The experiment audits all TASK 14 obstructions and seeded configurations without scanning `qW`.

For TASK 19, run:

```bash
python3 research/covering/test_pairwise_alignment.py
python3 research/covering/task19_experiments.py
```

`pairwise_alignment.py` computes exact four-state local transitions, labelled joint transition tables by CRT/gcd histograms, and two-strip safe-component counts. The audit preserves the distinction between complete labelled tables and insufficient aggregate summaries.

For TASK 20, run:

```bash
python3 research/covering/test_triple_alignment.py
python3 research/covering/task20_experiments.py
```

`triple_alignment.py` constructs the full 8-by-8 before/after table for three labels by generalized CRT and computes the exact component change when the third strip is inserted. The phase-reconstruction result is distinguished from the still-open uniform gap inequality.

For TASK 21, run:

```bash
python3 research/covering/test_triple_safe.py
python3 research/covering/task21_experiments.py
```

`triple_safe.py` computes exact all-safe mass on the lcm quotient and the
one-strip and pair-corrected quantitative lower bounds. The experiment tests
all TASK 14 obstructions and an exhaustive normalized range without scanning
`qW`.

For TASK 22, run:

```bash
python3 research/covering/test_restricted_incidence.py
python3 research/covering/task22_experiments.py
```

`restricted_incidence.py` expands restricted incidences into CRT
intersections of order at most four and implements the exact all-triples
multiplicity identity. The audit records a compact counterexample to the
largest-mass triple rule.

For TASK 23, run:

```bash
python3 research/covering/test_multiplicity_surplus.py
python3 research/covering/task23_experiments.py
```

`multiplicity_surplus.py` evaluates the surplus both from its pointwise
histogram and from intersection moments through order four. The audit records
the divisor-aligned counterexample to surplus negativity.

For TASK 24, run:

```bash
python3 research/covering/test_localized_certificate.py
python3 research/covering/task24_experiments.py
```

`localized_certificate.py` partitions the lcm grid into four transition
fibers of a canonically selected anchor and evaluates the quadratic
low-multiplicity certificate in histogram and moment forms.

For TASK 25, run:

```bash
python3 research/covering/test_phase_refinement.py
python3 research/covering/task25_experiments.py
```

The refinement audit distinguishes joint transition fibers of up to four
anchors, one-anchor short transition words, and coarse reduced-coordinate
bins. Fiber counts are bounded independently of the lcm period.

For TASK 26, run:

```bash
python3 research/covering/test_four_anchor.py
python3 research/covering/task26_experiments.py
```

The audit reconstructs the complete four-anchor fiber histogram of the
13-label counterexample on its canonical lcm period and stores all phase
records and quadratic values.
