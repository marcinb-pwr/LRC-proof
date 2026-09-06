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
