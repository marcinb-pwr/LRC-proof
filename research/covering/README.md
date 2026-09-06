# Finite covering experiments

Run from this directory:

```bash
python experiments.py
```

The code uses integer arithmetic throughout.  It constructs the strict bad
sets both directly and from their proved periodic blocks, checks the exact
cardinality formula, checks every pair-intersection count against the second
binomial moment, and writes deterministic results to `results.json`.

The computations are labelled `VERIFIED`, never `PROVED`; proofs are in
`theorem.md`.
