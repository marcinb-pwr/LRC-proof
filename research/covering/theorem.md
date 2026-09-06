# Exact periodic covering audit

## Status and outcome

This note achieves **Outcome B** of `TASK8.md`: it gives exact cardinality and
intersection formulae and reduces any counterexample to a sharp finite
arithmetic inequality.  It does **not** prove LRC.

## Theorem 1 (finite normalization) — `PROVED`

Let the distinct positive integers (v_1,\ldots,v_N) have gcd one, put
(q=N+1), (W=\operatorname{lcm}(v_i)), and (M=qW).  For

\[
R=\{a\in\mathbb Z^N:\sum_i a_iv_i\equiv0\pmod M\}
\]

one has ([\mathbb Z^N:R]=M),

\[
R^*=\mathbb Z^N+\mathbb Z(v_1/M,\ldots,v_N/M),
\]

and its classes modulo (\mathbb Z^N) are, without repetition,

\[
x_k=(\{kv_1/M\},\ldots,\{kv_N/M\}),\qquad 0\le k<M.
\]

**Proof.** Since (v_i\mid W\mid M),
(\gcd(M,v_1,\ldots,v_N)=\gcd(v_1,\ldots,v_N)=1).  The image of
(a\mapsto\sum a_iv_i\pmod M) is therefore all of (\mathbb Z/M\mathbb Z),
so its kernel (R) has index (M).  The displayed fractional vector
annihilates (R), and its class has order (M): if (M\mid kv_i) for every
(i), Bezout's identity gives (M\mid k).  Its (M) classes exhaust
(R^*/\mathbb Z^N), whose order is ([\mathbb Z^N:R]=M).  This also proves
the asserted parametrization and absence of repetition. \(\square\)

The endpoint convention is important.  LRC fails exactly when the **strict**
bad sets

\[
B_i=\{k\pmod M:\|kv_i/M\|<1/q\}
\]

cover (\mathbb Z/M\mathbb Z). Equality is safe and hence is not in (B_i).

## Theorem 2 (period and exact size) — `PROVED`

Put (b_i=W/v_i).  Membership in (B_i) has exact period (qb_i=M/v_i)
(as a function on the integers), and in one period its residues are

\[
A_i=\{0,1,\ldots,b_i-1\}\cup
\{qb_i-b_i+1,\ldots,qb_i-1\}.
\]

Consequently

\[
\boxed{|B_i|=v_i(2b_i-1)=2W-v_i.}
\]

**Proof.** Write (r=k\bmod qb_i).  Cancelling (v_i) from
(kv_i/(qW)=k/(qb_i)), strict badness says
(\min(r,qb_i-r)<b_i), which gives exactly the two displayed blocks and
(2b_i-1) residues.  The block repeats (v_i) times modulo (M).
The least period is (qb_i): the zero set's initial run has the stated
endpoints, so no proper translation stabilizes it (the trivial one-point
case is immediate). \(\square\)

Thus, with (S=\sum_i|B_i|),

\[
S=2NW-\sum_i v_i,\qquad
\boxed{\Delta=S-M=(N-1)W-\sum_i v_i.}
\]

If (\Delta<0), the union bound proves LRC.  This is a valid sufficient
criterion, though experiments show it is usually weak.

## Theorem 3 (exact pair CRT/block formula) — `PROVED`

For a pair (i,j), let (p_i=qb_i,p_j=qb_j),
(L_{ij}=\operatorname{lcm}(p_i,p_j)), and let (A_i,A_j) be the blocks in
Theorem 2. Then

\[
\boxed{
|B_i\cap B_j|={M\over L_{ij}}
\sum_{r=0}^{L_{ij}-1}
1_{A_i}(r\bmod p_i)1_{A_j}(r\bmod p_j).
}
\]

**Proof.** Both indicators have common period (L_{ij}\mid M). Count in
one common period and repeat (M/L_{ij}) times. This is also an exact CRT
algorithm: a pair (a\in A_i,b\in A_j) contributes precisely when
(a\equiv b\pmod{\gcd(p_i,p_j)}), in which case it determines one residue
modulo (L_{ij}). \(\square\)

This shows why a formula depending only on a single gcd is generally too
coarse: the locations and lengths of both endpoint blocks remain relevant.

## Theorem 4 (sharp excess-overlap obstruction) — `PROVED`

Let (m(k)=\sum_i1_{B_i}(k)), and put

\[
P=\sum_{i<j}|B_i\cap B_j|=\sum_k\binom{m(k)}2.
\]

If the bad sets cover, then

\[
\boxed{P\ge\Delta.}
\]

More exactly,

\[
\boxed{P-\Delta=\sum_k\binom{m(k)-1}{2}\ge0.}
\]

**Proof.** Under a cover (m(k)\ge1). Pointwise,
(\binom m2-(m-1)=\binom{m-1}2\). Summing and using
(\sum_k(m(k)-1)=S-M=\Delta) proves both claims. Equality holds precisely
when every multiplicity is one or two, so the inequality is sharp among
arbitrary set systems. \(\square\)

Equivalently, the second power moment obeys

\[
\sum_km(k)^2=S+2P\ge M+3\Delta
\]

when (0\le\Delta\) and a cover exists.  Therefore the concrete new
finite-arithmetic target is

\[
\boxed{
\sum_{i<j}|B_i\cap B_j|<(N-1)W-\sum_i v_i
\quad\Longrightarrow\quad\text{LRC}.
}
\]

The left side is exactly computable by Theorem 3. This implication is new
information rather than another Poisson equivalence, but a universal proof of
its premise is **OPEN** (and the premise is not expected to hold for every
configuration without refinement).

## Computational audit — `VERIFIED`

`experiments.py` checks the constructions and identities on the required
consecutive, odd, powers-of-two, translated, and deterministic random
families for (2\le N\le7).  It also records moments through order four.
These checks are evidence against implementation errors, not proofs.

## Barrier — `PROVED`

No argument using only the values (M,S) and an unrestricted second moment
can improve Theorem 4: for every integer (0\le\Delta\le M), a multiplicity
sequence with (M-\Delta) ones and (\Delta) twos attains equality. Any
successful moment route must therefore exploit the arithmetic pair formula,
higher intersections, or pointwise restrictions peculiar to these periodic
blocks. This sharply identifies the next step.
