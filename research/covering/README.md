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
