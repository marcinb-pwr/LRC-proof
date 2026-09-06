# Full-dimensional dualization

## Outcome D — exact finite reformulation

The full compact-support Poisson calculation is **PROVED**, but strict
positivity is equivalent to the original finite LRC condition. Thus this is
an exact reformulation, not a new proof of LRC.

## 1. Full relation lattice

Let
\[
R=\{a\in\mathbb Z^N:v\cdot a\equiv0\pmod M\},\qquad M=qW.
\]
The homomorphism \(a\mapsto v\cdot a\bmod M\) has image of size
\[
\frac{M}{\gcd(M,v_1,\ldots,v_N)}.
\]
Therefore
\[
\boxed{\det R=\frac{M}{\gcd(M,v_1,\ldots,v_N)}.}
\]
The annihilator calculation gives
\[
\boxed{R^*=\mathbb Z^N+
\mathbb Z\left(\frac{v_1}{M},\ldots,\frac{v_N}{M}\right).}
\]
Indeed, the displayed fractional vector pairs integrally with \(R\), and
the quotient \(R^*/\mathbb Z^N\) has the same finite order as
\(\mathbb Z^N/R\). This proves both inclusions.

## 2. Full Poisson formula

With
\[
G_q(x)=\prod_i g_q(x_i),\qquad
h=(1/2,\ldots,1/2),
\]
the character is
\[
e^{2\pi i\langle h,a\rangle}=(-1)^{\sum_i a_i}.
\]
The one-dimensional transform is
\[
\widehat g_q(x)=\frac1{\alpha_q}
\left(1-\frac{|x|}{\alpha_q}\right)_+,\qquad
\alpha_q=\frac{q-2}{2q}.
\]
Thus \( \widehat G_q \) is a nonnegative product supported on
\([-\alpha_q,\alpha_q]^N\). Lattice Poisson gives
\[
\boxed{
F(V)=\frac1{\det R}
\sum_{\eta\in R^*}
\widehat G_q(\eta-h).
}                                                               \tag{1}
\]
Only points in
\[
R^*\cap[1/q,1-1/q]^N
\]
contribute. Therefore
\[
\boxed{F(V)\ge0}
\]
is **PROVED**.

The regularity issue is harmless: \(G_q\) is continuous, integrable, and
has an integrable compactly supported transform with \(O(|x|^{-2})\)
coordinate decay. The formula also follows by tensor-product smoothing and
an \(L^1\) limit.

## 3. Finite arithmetic form

Modulo \(\mathbb Z^N\), every dual class is
\[
\eta_k=\left(\left\{\frac{k v_i}{M}\right\}\right)_{i=1}^N,
\qquad 0\le k<D,\quad D=\det R.
\]
Because \([1/q,1-1/q]\) has length less than \(1\), each class has at most
one representative in the box. Consequently
\[
F(V)=\frac1D\sum_{\substack{0\le k<D\\
\forall i:\;1/q\le\{kv_i/M\}\le1-1/q}}
\prod_i
\frac1{\alpha_q}
\left(1-\frac{|\{kv_i/M\}-1/2|}{\alpha_q}\right).             \tag{2}
\]
Every term is nonnegative and rational.

## 4. Strict positivity and boundary

Since each factor in (2) is positive exactly in the open interval,
\[
\boxed{
F(V)>0
\iff
R^*\cap(1/q,1-1/q)^N\ne\varnothing.
}                                                               \tag{3}
\]
The boundary-only case gives \(F(V)=0\). This is not a failure of LRC:
the original LRC permits equality at \(1/q\).

Using the discretization lemma from `01_dual_lattice.md`, the existence of
the \(k\) in the closed box in (2) is equivalent to LRC itself. Hence
\[
F(V)>0
\iff \text{the strict finite dual condition},
\]
while \(F(V)\ge0\) alone proves nothing beyond a nonnegative certificate.

## 5. Relaxed thresholds

For \(\delta=1/q-\varepsilon\), the same calculation replaces the box by
\([\delta,1-\delta]^N\). The endpoint lemma is **PROVED**:
if every \(\varepsilon>0\) admits \(t_\varepsilon\) with
\(\min_i\|t_\varepsilon v_i\|\ge1/q-\varepsilon\), compactness of
\(\mathbb R/\mathbb Z\) gives a limit satisfying the endpoint threshold.
However, universal strict positivity of the relaxed finite certificate is
not proved here; it is the same relaxed LRC existence problem.
