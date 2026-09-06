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
