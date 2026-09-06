# Dualized support-2 theorem

## Status

The transform, character-shifted Poisson formula, dual lattice, and finite
formula below are **PROVED**. The example comparisons are **VERIFIED**.

## 1. Correct transform

With \(\alpha=(q-2)/(2q)\),
\[
\widehat g_q(x)=\frac1\alpha(1-|x|/\alpha)_+.
\]
Thus the support is \([-\alpha,\alpha]\). This corrects the proposed
\([-2\alpha,2\alpha]\) support.

## 2. Character-shifted Poisson formula

Let \(h=(1/2,1/2)\). Since
\((-1)^{r+s}=e^{2\pi i\langle h,(r,s)\rangle}\),
ordinary lattice Poisson summation gives
\[
T_{ij}=\frac1{\det L_{ij}}
\sum_{\eta\in L_{ij}^*}\widehat G_q(\eta-h).                 \tag{1}
\]
The sign is fixed by
\(\widehat{e^{2\pi i\langle h,\cdot\rangle}G}(\xi)
=\widehat G(\xi-h)\).

The support condition is
\[
\eta_k\in\left[\frac12-\alpha,\frac12+\alpha\right]
=\left[\frac1q,1-\frac1q\right].                             \tag{2}
\]
Hence the dual sum is finite and every summand is nonnegative.

## 3. Explicit dual lattice and formula

The basis in `dual_lattice.py` is
\[
u_1=(n_1,0),\qquad u_2=(r_0,a),
\]
where
\[
h=\gcd(v_i,v_j),\quad n=\frac{qW}{\gcd(h,qW)},\quad
x=v_i/h,\quad y=v_j/h,
\]
\[
a=\gcd(x,n),\quad n_1=n/a,\quad
r_0\equiv-y(x/a)^{-1}\pmod{n_1}.
\]
Its determinant is \(n\). If \(U=[u_1\ u_2]\), then
\[
L_{ij}^*=U^{-T}\mathbb Z^2.
\]
This is **PROVED**.

There is also a direct arithmetic description:
\[
L_{ij}^*=\mathbb Z^2+
\mathbb Z\left(\frac{v_i}{qW},\frac{v_j}{qW}\right).             \tag{3}
\]
Indeed, the displayed generator pairs integrally with every element of
\(L_{ij}\), and the quotient \(L_{ij}^*/\mathbb Z^2\) has order
\(\det L_{ij}\). Thus the finite dual set can be enumerated exactly by
\(k=0,\ldots,\det L_{ij}-1\), reducing both coordinates modulo \(qW\).

Define
\[
\mathcal Q_{ij}=L_{ij}^*\cap[1/q,1-1/q]^2.
\]
Then the exact finite formula is
\[
\boxed{
T_{ij}=\frac1{\det L_{ij}}
\sum_{\eta\in\mathcal Q_{ij}}
\frac1{\alpha^2}
\left(1-\frac{|\eta_1-1/2|}{\alpha}\right)
\left(1-\frac{|\eta_2-1/2|}{\alpha}\right).
}                                                               \tag{3}
\]
Every term is nonnegative, so \(T_{ij}\ge0\) is **PROVED**.

Finally,
\[
F_{ij}=T_{ij}-
\bigl(T_i^{(ij)}+T_j^{(ij)}-1\bigr),                           \tag{4}
\]
where
\[
T_i^{(ij)}=\text{axis\_line}(q,b_i),\quad
T_j^{(ij)}=\text{axis\_line}(q,b_j),
\]
and each `axis_line` includes its origin term. Formula (4) is
**PROVED**.

## 4. Examples and remaining issue

`results.json` contains exact rational values and independent direct
summations for \(V=(1,2),(1,3),(1,4),(2,3),(2,5)\), and several \(N=3,4\)
configurations. The full pair sums
are nonnegative by (3), but this does not prove
\[
F_{\rm axis}+F_2>0.
\]
The remaining global support-2 question is **OPEN**.
