# 02 — Poisson certificate

## Status

The lattice identity, phase identity, and implication
\(F(V)>0\Rightarrow\mathrm{LRC}\) below are **PROVED**. Positivity of
\(F(V)\) for every \(V\) is **OPEN**.

Assume \(N\ge2\), and use the notation of `01_dual_lattice.md`. Put
\[
A_i=\frac{q-2}{2}b_i>0,\qquad
h_A(x)=\frac1A(1-|x|/A)_+.
\]
Define
\[
\phi(x)=\prod_{i=1}^N h_{A_i}(x_i).
\]
Then \(\phi\ge0\), \(\operatorname{supp}\phi\subseteq K\), and
\(\phi\not\equiv0\).

Use the Fourier convention
\[
\widehat f(\xi)=\int_{\mathbb R^N}f(x)e^{-2\pi i\langle x,\xi\rangle}\,dx.
\]
The one-dimensional transform is
\[
\widehat h_A(\xi)
=\left(\frac{\sin(\pi A\xi)}{\pi A\xi}\right)^2,
\]
with value \(1\) at \(\xi=0\). Consequently
\[
\widehat\phi(\xi)
=\prod_i\left(\frac{\sin(\pi A_i\xi_i)}
{\pi A_i\xi_i}\right)^2\ge0,\qquad
\widehat\phi(0)=1.                                             \tag{1}
\]

The triangle function is compactly supported and piecewise \(C^1\); its
transform has quadratic coordinate decay. The standard Poisson summation
theorem for a full-rank lattice therefore applies to this tensor product
(alternatively, approximate each triangle uniformly in the Wiener norm by
smooth compactly supported functions and pass to the limit). With
\[
S(c)=\sum_{\lambda\in\Lambda}\phi(c-\lambda),
\]
it gives
\[
S(c)=\frac1{\det\Lambda}
\sum_{\xi\in\Lambda^*}\widehat\phi(\xi)
e^{2\pi i\langle c,\xi\rangle}.                                \tag{2}
\]
The determinant factor is the covolume from (4) of the first document.

For \(a\in\mathbb Z^N\) satisfying
\(\sum_i a_iv_i\equiv0\pmod{qW}\), let
\[
\xi_a=\left(\frac{a_1}{qb_1},\ldots,\frac{a_N}{qb_N}\right).
\]
By (9),
\[
e^{2\pi i\langle c,\xi_a\rangle}=(-1)^{\sum_i a_i}.             \tag{3}
\]
The map \(a\mapsto\xi_a\) is injective, and the Poisson sum is over the full
infinite relation set
\[
D=\{a\in\mathbb Z^N:\sum_i a_i v_i\equiv0\pmod{qW}\}.
\]
For a finite computational experiment one may choose canonical residue
representatives modulo \(qb_i\), but that computes only a finite quotient
sample and is not the full Poisson sum. Define formally:
\[
F(V)=\sum_{a\in D}(-1)^{\sum_i a_i}\widehat\phi(\xi_a).           \tag{4}
\]
Then
\[
\boxed{S(c)=\frac{F(V)}{\det\Lambda}.}                           \tag{5}
\]

Finally, if \(F(V)>0\), then \(S(c)>0\). Since every summand is
nonnegative, there is a \(\lambda\in\Lambda\) with
\(\phi(c-\lambda)>0\). Hence \(c-\lambda\in K\), and (5) of the first
document gives LRC.

\[
\boxed{F(V)>0\Longrightarrow\text{LRC for }V.}
\]

The unresolved problem is the universal strict positivity of (4). The
nonzero terms have nonnegative weights but alternating phases, so Fourier
positivity alone does not prove it.
