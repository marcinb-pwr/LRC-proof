# Exact support-2 evaluation

## Status

The lattice basis, Smith invariants, exact pair series, and uniform tail
bound below are **PROVED**. Numerical values are **VERIFIED** only when the
reported tail bound is smaller than the magnitude of the truncation.

## 1. Rank-two lattice

Fix \(i<j\), put \(M=qW\), \(h=\gcd(v_i,v_j)\),
\[
n=\frac{M}{\gcd(h,M)},\qquad x=v_i/h,\qquad y=v_j/h,
\]
\[
a=\gcd(x,n),\qquad n_1=n/a.
\]
Let
\[
r_0\equiv-y(x/a)^{-1}\pmod{n_1},
\]
with \(r_0=0\) if \(n_1=1\). Then
\[
L_{ij}=\{u(n_1,0)+z(r_0,a):u,z\in\mathbb Z\}.                 \tag{1}
\]
This is **PROVED** by solving \(x r+y s\equiv0\pmod n\) and lifting back
through the common gcd. Its determinant is \(n\).

The Smith invariants of the map
\(\mathbb Z^2\to\mathbb Z/M\mathbb Z\), \((r,s)\mapsto rv_i+sv_j\),
are
\[
\gcd(v_i,v_j,M),\qquad \frac{M}{\gcd(v_i,v_j,M)}.               \tag{2}
\]
The kernel index is the second invariant, equal to the determinant in (1).

## 2. Complete pair sum

With
\[
g_q(n)=\left(
\frac{\sin(\pi(q-2)n/(2q))}
{\pi(q-2)n/(2q)}
\right)^2,
\]
the complete sum is
\[
T_{ij}=\sum_{(r,s)\in L_{ij}}(-1)^{r+s}g_q(r)g_q(s).
\]
Separating \((0,0)\), the two coordinate axes, and \(rs\ne0\) gives
\[
T_{ij}=1+T_i^{(ij)}+T_j^{(ij)}+F_{ij}.                        \tag{3}
\]
This is **PROVED** by disjoint partition of \(L_{ij}\).

## 3. Exact support-2 series

\[
F_{ij}=
\sum_{\substack{(r,s)\in L_{ij}\\rs\ne0}}
(-1)^{r+s}g_q(r)g_q(s).                                      \tag{4}
\]
Because \(g_q(n)=O_q(n^{-2})\), (4) is absolutely convergent. This is
**PROVED**.

## 4. Certified truncation

For \(n\ne0\),
\[
g_q(n)\le\frac{C_q}{n^2},\qquad
C_q=\frac{4q^2}{\pi^2(q-2)^2}.
\]
Therefore, truncating to \(|r|,|s|\le R\), even after enlarging the relation
lattice to \(\mathbb Z^2\), gives
\[
|F_{ij}-F_{ij}^{(R)}|
\le E_q(R)
=\frac{4\pi^2C_q^2}{3R}.                                     \tag{5}
\]
Indeed, the omitted union is bounded by
\[
2\left(\sum_{|r|>R}\frac{C_q}{r^2}\right)
\left(\sum_{s\ne0}\frac{C_q}{s^2}\right)
\le\frac{4\pi^2C_q^2}{3R}.
\]
Thus a negative truncation is a mathematical negative sign only when
\[
E_q(R)<|F_{ij}^{(R)}|.
\]
This is **PROVED**.

## 5. Current conclusion

The exact pair sector has been reduced to (4), with an explicit rank-two
basis and certified tails. The experiments in `results.json` determine
which individual signs are certified at \(R=32\). In the current 49-case
experiment, none is certified at \(R=32\). Thus the earlier negative
truncations in `research/support2/results.json` are not mathematical
negative-sign discoveries. No universal sign theorem for \(F_{ij}\), nor a
global positivity theorem for \(F_{\rm axis}+F_2\), has been proved. Those
questions remain **OPEN**.
