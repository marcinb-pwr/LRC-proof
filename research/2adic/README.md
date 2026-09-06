# 2-adic relation laboratory

This laboratory studies
\[
\sum_i a_i v_i\equiv0\pmod{qW},\qquad q=N+1,
\]
using finite canonical residue boxes and separately enumerated short
relations. It does not enumerate the infinite relation lattice.

For coordinate \(i\), the dual period is \(q b_i\). Canonical residues are
chosen in `range(q * b_i)`. Quantities involving the coefficient sum,
\(\ell^1\)-norm, support, and carry profile are representative-dependent
when a period \(q b_i\) is odd. The script records this fact explicitly.
The actual Fourier phase belongs to the full dual point, not to a quotient
class.

Run:

```bash
python3 research/2adic/experiments.py
```

The output is written to `results.json`.
