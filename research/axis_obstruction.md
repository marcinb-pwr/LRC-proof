# Axis-dual obstruction

## Status

The axis classification and axis Fourier sum below are **PROVED**. The
finite experiment results are **VERIFIED computationally**, not proofs of
the full Fourier inequality.

## 1. Correct Poisson relation sum

The full Poisson sum is over
\[
D=\{a\in\mathbb Z^N:\sum_i a_i v_i\equiv0\pmod{qW}\},
\qquad q=N+1,
\]
with no quotient identification. The map
\[
a\longmapsto \xi_a=(a_i/(qb_i))_i
\]
is injective. Thus
\[
F(V)=\sum_{a\in D}(-1)^{\sum_i a_i}\widehat\phi(\xi_a).
\]

## 2. Axis relations

For each coordinate \(i\) and \(m\in\mathbb Z\), put
\[
a=mqb_i e_i.
\]
Then
\[
\sum_j a_jv_j=mqb_iv_i=mqW\equiv0\pmod{qW},
\]
so every such vector belongs to \(D\). Its dual point is
\[
\xi_a=me_i,
\]
and its phase is
\[
(-1)^{\sum_j a_j}=(-1)^{mqb_i}.
\]
The \(i\)-axis is negative exactly when \(qb_i\) is odd and \(m\) is odd.
Since \(q=N+1\), this requires \(N\) even and \(b_i\) odd.

## 3. Exact axis Fourier contribution

For
\[
A_i=\frac{q-2}{2}b_i
\]
and \(h_A(x)=A^{-1}(1-|x|/A)_+\), the transform is
\[
\widehat h_A(\xi)=\left(\frac{\sin(\pi A\xi)}{\pi A\xi}\right)^2.
\]
At the axis point \(me_i\), all other factors equal \(1\), and therefore
\[
\widehat\phi(me_i)
=\left(\frac{\sin(\pi mA_i)}{\pi mA_i}\right)^2.
\]
For \(m\ne0\), using \(A_i=(q-2)b_i/2\),
\[
\left(\frac{\sin(\pi mA_i)}{\pi mA_i}\right)^2
=\frac{4\sin^2(\pi m(q-2)b_i/2)}
{\pi^2m^2(q-2)^2b_i^2}.                                      \tag{1}
\]

If \(q\) is odd, then \(q-2\) is odd. Hence:

* if \(b_i\) is even, every term in (1) with \(m\ne0\) vanishes;
* if \(b_i\) is odd, \(\sin^2(\pi m(q-2)b_i/2)=1\) for odd \(m\), and is
  \(0\) for even \(m\).

If \(q\) is even, \(q-2\) is even, so every nonzero axis term vanishes.

Consequently, with \(O=\{i:b_i\text{ odd}\}\),
\[
\boxed{
F_{\rm axis}(V)=
\begin{cases}
1,&N\text{ odd},\\[2mm]
1-\displaystyle\frac{1}{(N-1)^2}
\sum_{i\in O}\frac1{b_i^2},&N\text{ even}.
\end{cases}}                                                   \tag{2}
\]
\]
For the even case, (2) follows from
\[
\sum_{m\text{ odd},\,m\ne0}\frac1{m^2}=\frac{\pi^2}{4}.
\]

## 4. Sign analysis

For even \(N\ge4\), at least one \(b_i\) is \(1\), because
\(\gcd(b_1,\ldots,b_N)=1\), and therefore \(|O|\ge1\). But
\[
\sum_{i\in O}\frac1{b_i^2}\le N,
\]
so the formula alone does not give positivity for arbitrary \(b_i\).
The stronger arithmetic fact is that \(b_i\) are distinct divisors of
\(W\), and odd \(b_i\) are distinct odd divisors. The maximum possible sum
over \(N\) distinct odd positive integers is
\[
1+\frac1{3^2}+\cdots+\frac1{(2N-1)^2}<\frac{\pi^2}{8}.
\]
Thus
\[
F_{\rm axis}>1-\frac{\pi^2}{8(N-1)^2}>0
\qquad(N\ge4\text{ even}).
\]
For odd \(N\), \(F_{\rm axis}=1>0\).

For \(N=2\),
\[
F_{\rm axis}=1-\sum_{i:b_i\text{ odd}}\frac1{b_i^2}.
\]
It can be negative: for \(V=(1,3)\), \(W=3\) and \(b=(3,1)\), giving
\[
F_{\rm axis}=1-\left(\frac19+1\right)=-\frac19.
\]
It can be zero, for example for \(V=(1,2)\), where \(b=(2,1)\):
\[
F_{\rm axis}=1-1=0.
\]
Therefore the axis sector is a controlled, explicitly summable contribution,
but it is not always positive.

## 5. Low-support classification

Support one is completely classified: if \(a=ke_i\), then
\[
qW\mid k v_i
\iff q b_i\mid k.
\]
Thus the support-one relations are exactly the axis relations above.

For support two, let \(i\ne j\), \(M=qW\), \(d=\gcd(v_j,M)\), and write
\(\bar v_j=v_j/d\), \(\bar M=M/d\). A vector
\[
a=r e_i+s e_j
\]
is a relation exactly when
\[
d\mid r v_i
\quad\text{and}\quad
s\equiv-\frac{r v_i}{d}\,\bar v_j^{-1}\pmod{\bar M},          \tag{3}
\]
where the inverse exists because \(\gcd(\bar v_j,\bar M)=1\).
This is a complete arithmetic classification of support-two relations.
Its parity is determined by the chosen integer representative \(s\), not
only by the residue class, so the full dual lattice must be retained.
Support three and higher are described by the original single linear
congruence and have no comparable one-line classification here.

## 6. Genuine relations and surviving obstruction

Define \(D_{\rm axis}=\bigcup_i\{mqb_i e_i:m\in\mathbb Z\}\). This union
intersects only at \(0\). All relations outside it are genuinely
multidimensional. Finite short-relation experiments are recorded in
`research/axis_results.json`.

The experiments do not prove a structural theorem for
\(D\setminus D_{\rm axis}\). The strongest proved conclusion is:

> Removing the axis sector removes the explicit support-one obstruction, but
> no implication from odd parity to multi-layer 2-adic structure has been
> established.

This is **OPEN**. The axis contribution cannot by itself invalidate the
Fourier program for \(N\ge4\), but the full signed sum remains unresolved.
