# Support-2 sector theorem status

## 1. Full relation space

For \(i<j\), define
\[
D_{ij}=\{r e_i+s e_j:r v_i+s v_j\equiv0\pmod{qW}\}.
\]
The exact-support sets \(D_{ij}^{(2)}\), obtained by requiring \(rs\ne0\),
are disjoint for different unordered pairs. This is **PROVED**, because the
support of a vector uniquely determines its unordered pair.

The group \(D_{ij}\) is generally rank two. Consequently, a global
one-integer parametrization is impossible. A correct finite canonical
enumeration is
\[
0\le r<qb_i,\qquad0\le s<qb_j,
\]
subject to the congruence. For fixed \(r\), one-coordinate CRT gives a
one-parameter residue class for \(s\): if
\[
M=qW,\quad d=\gcd(v_j,M),
\]
then solvability requires \(d\mid rv_i\), and
\[
s\equiv-\frac{rv_i}{d}(v_j/d)^{-1}\pmod{M/d}.                  \tag{1}
\]
This is **PROVED**.

## 2. Parity

For any relation \(r e_i+s e_j\), odd parity is exactly
\[
r+s\equiv1\pmod2.
\]
Equation (1), together with the chosen integer representative, is an exact
criterion. There is no general requirement that \(\nu_2(v_i)\ne\nu_2(v_j)\).
This is **PROVED**, and the one-layer counterexample \(V=(1,3)\) from the
previous task already demonstrates it.

## 3. Fourier weight

For the tensor triangle function,
\[
w(r e_i+s e_j)=g_q(r)g_q(s),
\qquad
g_q(n)=\left(
\frac{\sin(\pi(q-2)n/(2q))}
{\pi(q-2)n/(2q)}
\right)^2,
\]
with \(g_q(0)=1\). The independence from \(i,j\) is **PROVED**.

## 4. Signed contribution

The exact pair contribution is the absolutely convergent series
\[
F_{ij}=\sum_{\substack{r,s\in\mathbb Z\\
rv_i+sv_j\equiv0\pmod{qW}\\rs\ne0}}
(-1)^{r+s}g_q(r)g_q(s).                                      \tag{2}
\]
Absolute convergence follows from \(g_q(n)=O(n^{-2})\) away from zero.
Equation (2) is **PROVED**. The experiments use finite symmetric truncation
and therefore are **VERIFIED computationally**, not an evaluation of (2).

## 5. Smallest odd support-2 frequency

The exact quantity
\[
L_{ij}=\min\{|r|+|s|:rs\ne0,\ rv_i+sv_j\equiv0\pmod{qW},
r+s\text{ odd}\}
\]
is computed by bounded search in `results.json`. No universal closed formula
or useful lower bound has been proved. That part is **OPEN**.

## 6. Outcome

The strongest results are:

* support-2 pairs are exactly classified by (1);
* their Fourier weights reduce to the universal product \(g_q(r)g_q(s)\);
* the support-2 signed contribution is the exact series (2);
* finite experiments do not prove universal positivity of
  \(F_{\rm axis}+F_2\).

The pairwise sector is therefore reduced to an explicit arithmetic series,
but its global sign remains **OPEN**. No move to higher-order additive
combinatorics is justified by this task alone.
