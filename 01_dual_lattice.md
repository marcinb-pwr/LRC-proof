# 01 — Exact CRT and dual-lattice formulation

## Status

The statements in this document are **PROVED**. No assertion here depends on
the conjectural 2-adic or additive-combinatorial part of the research
program.

Let \(V=\{v_1,\ldots,v_N\}\) be distinct positive integers, put
\[
q=N+1,\qquad W=\operatorname{lcm}(v_1,\ldots,v_N),\qquad b_i=W/v_i.
\]
Thus \(W=b_i v_i\).

## 1. Discretization and residue reformulation

There is a necessary discretization step. It is not true that the residue
of an arbitrary real \(x\) modulo an integer is an integer.

For each \(i\), on the circle \(\mathbb R/\mathbb Z\), the feasible set
\(\{t:\|tv_i\|\ge1/q\}\) is a finite union of closed intervals whose
endpoints are
\[
\frac{k+1/q}{v_i},\qquad \frac{k+1-1/q}{v_i}.
\]
Every such endpoint belongs to \((qW)^{-1}\mathbb Z/\mathbb Z\). The
intersection over \(i\) is again a finite union of closed intervals (and
possibly points). If it is nonempty, one of its components has an endpoint
among the endpoints above, unless it is the whole circle, in which case
\(t=0\) works. Consequently
\[
\exists t\in\mathbb R\ \forall i,\ \|tv_i\|\ge1/q
\iff
\exists x\in\mathbb Z\ \forall i,\
\left\|\frac{x}{qb_i}\right\|\ge1/q.                            \tag{0}
\]
The reverse implication is immediate, and the forward implication is the
grid-endpoint argument. This is the step that permits an integer CRT
calculation.

Set \(x=qWt\). Then
\[
tv_i=\frac{x}{qb_i}.
\]
For the integer \(x\) supplied by (0), let \(r_i\) be the residue of \(x\)
modulo \(qb_i\),
chosen in \(\{0,\ldots,qb_i-1\}\). Since the distance to the nearest
integer is the distance of \(r_i/(qb_i)\) to \(0\) modulo \(1\),
\[
\left\|\frac{x}{qb_i}\right\|\geq\frac1q
\iff
b_i\leq r_i\leq(q-1)b_i.                                      \tag{1}
\]
The endpoints are included. This also proves that no parity convention is
being hidden in the reduction.

Define
\[
A_i=\frac{q-2}{2}b_i,\qquad
c_i=\frac q2b_i,\qquad
K=\prod_i[-A_i,A_i],\qquad c=(c_1,\ldots,c_N).
\]
The interval in (1), after subtracting \(c_i\), is exactly
\([-A_i,A_i]\), including both endpoints.

## 2. The compatibility lattice

Define
\[
\Lambda=\left\{r\in\mathbb Z^N:
r_i\equiv r_j\pmod{q\gcd(b_i,b_j)}
\text{ for every }i,j\right\}.                                \tag{2}
\]

The elementary two-modulus CRT says that the system
\[
x\equiv r_i\pmod{qb_i}\quad(1\leq i\leq N)
\]
has an integer solution if and only if
\[
r_i\equiv r_j\pmod{\gcd(qb_i,qb_j)}
=\pmod{q\gcd(b_i,b_j)}
\]
for every pair. Necessity follows by subtracting two congruences.
Sufficiency follows inductively: if a solution exists for moduli \(m\) and
\(n\), the next congruence \(x\equiv r\pmod n\) is solvable precisely when
\(r\) agrees with the existing residue modulo \(\gcd(m,n)\), and then the
usual two-modulus CRT gives a solution modulo \(\operatorname{lcm}(m,n)\).
Therefore
\[
\Lambda=\{(x\bmod qb_1,\ldots,x\bmod qb_N):x\in\mathbb Z\},       \tag{3}
\]
where the right side is viewed as a set of integer representatives. In
particular, (2) is not an assumed lattice model: it is exactly the image of
the simultaneous residue map.

Let \(L=\operatorname{lcm}(b_1,\ldots,b_N)\). The map in (3), modulo
\(qL\), has image \(\Lambda/(q b_1\mathbb Z\oplus\cdots\oplus q b_N\mathbb Z)\)
of cardinality \(qL\). Hence
\[
\boxed{\det\Lambda=[\mathbb Z^N:\Lambda]
 =\frac{\prod_i(qb_i)}{qL}
 =q^{N-1}\frac{\prod_i b_i}{L}.}                               \tag{4}
\]
The displayed quotient is an integer because it is an index. This also
handles common divisors among the \(b_i\).

## 3. Exact equivalence with LRC

By the discretization lemma, it suffices to consider integer \(x\), and
conversely every integer \(x\) gives \(t=x/(qW)\). The residues of \(x\)
form an element \(\lambda\in\Lambda\). By (1), all LRC inequalities hold exactly when
\[
\lambda-c\in K.
\]
Since \(K=-K\), this is equivalent to \(c-\lambda\in K\), and therefore
\[
\boxed{\text{LRC for }V\iff(\Lambda-c)\cap K\ne\varnothing.}    \tag{5}
\]
Replacing integer \(x\) by its residue modulo \(qL\) leaves every residue
unchanged.

## 4. The dual lattice

Let
\[
\Lambda^*=\{\xi\in\mathbb R^N:\langle\xi,\lambda\rangle\in\mathbb Z
\text{ for every }\lambda\in\Lambda\}.
\]
First, \(qb_i e_i\in\Lambda\), so every \(\xi\in\Lambda^*\) satisfies
\(\xi_i=a_i/(qb_i)\) for some \(a_i\in\mathbb Z\).

Conversely, for such a vector and \(\lambda\) arising from \(x\), choose
integers \(k_i\) with \(\lambda_i=x-qb_i k_i\). Then
\[
\langle\xi,\lambda\rangle
=\frac{x}{q}\sum_i\frac{a_i}{b_i}-\sum_i a_i k_i
=\frac{x}{qW}\sum_i a_i v_i-\sum_i a_i k_i.                    \tag{6}
\]
The first term is integral for every integer \(x\) if and only if
\[
\sum_i a_i v_i\equiv0\pmod{qW}.                                \tag{7}
\]
This proves both directions, because taking \(x=1\) in (6) proves necessity.
Thus the exact parametrization is
\[
\boxed{\Lambda^*=
\left\{\left(\frac{a_1}{qb_1},\ldots,\frac{a_N}{qb_N}\right):
a\in\mathbb Z^N,\ \sum_i a_i v_i\equiv0\pmod{qW}\right\}.}      \tag{8}
\]
The parametrization in (8) is one-to-one: equality of two displayed
vectors forces equality of every integer coordinate \(a_i\). In particular,
replacing \(a_i\) by \(a_i+qb_i m_i\) produces a different dual point, not
the same point. This distinction matters when summing over the full dual
lattice.

## 5. Worked examples

### \(N=2\), \(V=\{1,2\}\)

\[
q=3,\quad W=2,\quad(b_1,b_2)=(2,1).
\]
Thus
\[
\Lambda=\{(r_1,r_2):r_1\equiv r_2\pmod3\},\qquad \det\Lambda=3.
\]
The dual relation is
\[
a_1+2a_2\equiv0\pmod6,\qquad
\xi=(a_1/6,a_2/3).
\]

### \(N=3\), \(V=\{1,2,3\}\)

\[
q=4,\quad W=6,\quad(b_1,b_2,b_3)=(6,3,2).
\]
The congruences are
\[
r_1\equiv r_2\pmod{12},\quad
r_1\equiv r_3\pmod8,\quad
r_2\equiv r_3\pmod4,
\]
and \(\det\Lambda=4^2(6\cdot3\cdot2)/6=96\).
The dual relation is
\[
a_1+2a_2+3a_3\equiv0\pmod{24},\qquad
\xi=(a_1/24,a_2/12,a_3/8).
\]

### \(N=4\), \(V=\{1,2,3,4\}\)

\[
q=5,\quad W=12,\quad(b_1,b_2,b_3,b_4)=(12,6,4,3).
\]
The pairwise moduli \(5\gcd(b_i,b_j)\) are respectively
\[
30,20,15,10,15,5
\]
in the order \(12,13,14,23,24,34\). The determinant is
\[
5^3\frac{12\cdot6\cdot4\cdot3}{12}=9000.
\]
The dual relation is
\[
a_1+2a_2+3a_3+4a_4\equiv0\pmod{60},
\]
with coordinates \((a_1/60,a_2/30,a_3/20,a_4/15)\).

## 6. Phase consequence

For a relation \(a\) in (8),
\[
\langle c,\xi_a\rangle
=\sum_i\frac q2b_i\frac{a_i}{qb_i}
=\frac12\sum_i a_i,
\]
so
\[
\boxed{e^{2\pi i\langle c,\xi_a\rangle}=(-1)^{\sum_i a_i}.}    \tag{9}
\]
The case \(N=1\) is elementary separately; the nondegenerate box/phase
construction begins at \(N=2\).
