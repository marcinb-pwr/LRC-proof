# Certified support-2 evaluation

This directory separates exact lattice arithmetic from floating-point
evaluation. A truncated value is never called a sign certificate unless the
explicit tail bound in `exact_pair.py` proves
\[
|F_{ij}-F_{ij}^{(R)}|<|F_{ij}^{(R)}|.
\]

Run:

```bash
python3 research/support2_exact/experiments.py
```

The current experiments use a symmetric coefficient radius and certify only
signs that pass the displayed inequality.
