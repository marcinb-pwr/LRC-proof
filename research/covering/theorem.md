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

---

# TASK 9 audit: closed overlaps, localization, and the moment barrier

## Theorem 5 (closed centered pair formula) — `PROVED`

Put (b_i=W/v_i, b_j=W/v_j), (d=gcd(b_i,b_j)), (Q=qd),
(A=b_i-1), and (B=b_j-1).  Then

\[
 \boxed{|B_i\cap B_j|={W\over\operatorname{lcm}(b_i,b_j)}
 \sum_{t=-\lfloor(A+B)/Q\rfloor}^{\lfloor(A+B)/Q\rfloor}
 \bigl(\min(A,B+tQ)-\max(-A,-B+tQ)+1\bigr)_+.}       \tag{4}
\]

This removes the scan through a common period in Theorem 3.  Equivalently,
with (J=[-B,B]\cap\mathbb Z), its inner count can be written with floors as

\[
 \sum_{u=-A}^{A}\left(
 \left\lfloor{B-u\over Q}\right\rfloor-
 \left\lceil{-B-u\over Q}\right\rceil+1\right).       \tag{5}
\]

**Proof.**  Represent the first endpoint block by (0,1,\ldots,b_i-1)
and the second, without duplicating zero, by
(-b_i+1,\ldots,-1); together these are exactly ([-A,A]).  Do the
same for (j).  The four left-left, left-right, right-left, and right-right
block pairs are therefore the four sign choices for ((u,v)), with the zero
assigned only to the nonnegative block.  CRT says that ((u,v)) gives one
class modulo (q\operatorname{lcm}(b_i,b_j)) exactly when
(u\equiv v\pmod{qd}).  Writing (u-v=tQ), the allowed (u)'s form
([-A,A]\cap[-B+tQ,B+tQ]), whose integer cardinality is the summand in
(4).  Only the displayed range of (t) can intersect.  Finally the common
period repeats (W/\operatorname{lcm}(b_i,b_j)) times modulo (qW).
This proves (4), all four block counts, and (5). □

Thus (d) alone does **not** determine the answer: after writing
(b_i=dr,b_j=ds), the coprime lengths (r,s), and the lift multiplicity
(W/(drs)), remain necessary.  For example, (4) changes when either (r)
or (s) changes with (d=1).

## Corollary 6 (normalized estimate) — `PROVED`

For (b_i=dr,b_j=ds), (gcd(r,s)=1), let (C_q(d;r,s)) denote the sum
in (4).  Then

\[
 \left|C_q(d;r,s)-{(2dr-1)(2ds-1)\over qd}\right|
 <\min(2dr-1,2ds-1).                                  \tag{6}
\]

Consequently (6), multiplied by (W/(drs)), bounds the global
intersection.  The primitive error is independent of (W).

**Proof.**  For each fixed integer (u\in[-A,A]), the number of integers
(v\in[-B,B]) in one specified class modulo (Q) differs from
((2B+1)/Q) by less than one.  Sum over (u).  Interchanging (i,j) and
taking the better estimate proves (6).  Strict endpoints are already encoded
by (A=b_i-1,B=b_j-1); no endpoint correction is suppressed. □

This coarse estimate does not identify universal extremizers; that
optimization remains `OPEN`.  Formula (4), rather than a claimed false
extremal statement, is implemented in `intersections.py` and checked against
the common-period count.

## Theorem 7 (triple identity and its exact limitation) — `PROVED`

For

\[
 T=\sum_{i<j<\ell}|B_i\cap B_j\cap B_\ell|
   =\sum_k\binom{m(k)}3,
\]

a common-period formula is obtained exactly as in Theorem 3: use period
(q\operatorname{lcm}(b_i,b_j,b_\ell)), test the three endpoint blocks,
and multiply by (W/\operatorname{lcm}(b_i,b_j,b_\ell)).
If the sets cover and (E=P-\Delta), then

\[
 \boxed{{3\over N}T\le E\le T,\qquad E=0\Longleftrightarrow T=0.} \tag{7}
\]

**Proof.**  Under a cover, Theorem 4 gives
(E=\sum_k\binom{m(k)-1}{2}).  For (m\ge3),
(\binom{m-1}{2}=3\binom m3/m), while both sides vanish for (m<3).
Since (3\le m\le N), summation proves (7). □

Hence (P>\Delta) forces a triple point, but the third moment supplies no
contradiction by itself: its exact pointwise relation to the pair slack is
already (7).  No stronger periodic lower bound was established; such a bound
is `OPEN`.

## Theorem 8 (canonical forced core) — `PROVED`

Let β= \(\min_i b_i\) and

\[
 C=\{0,1,\ldots,\beta-1\}\cup
   \{M-\beta+1,\ldots,M-1\}.
\]

Then (C\subseteq B_i) for every (i),  \(|C|=2\beta-1\), and

\[
 P=\binom N2(2\beta-1)+P_{\rm off},
 \quad
 P_{\rm off}=\sum_{i<j}|(B_i\cap B_j)\setminus C|.       \tag{8}
\]

**Proof.**  If (0\le k<\beta\le b_i), then (k/(qb_i)<1/q); the negative
residues are identical by symmetry.  The two ranges meet only at zero.
Every core point has multiplicity (N), yielding (8). □

This isolates a major defect in raw (P): it always includes
(\binom N2(2\beta-1)), overlap forced at residues that are already bad for
every runner.  Any useful pair obstruction must subtract or otherwise use
this localization.

## Exhaustive audit — `VERIFIED`; universal pair premise — `DISPROVED`

`experiments.py` checks the centered formula against the independent
common-period algorithm, checks the forced core, and records triple and
off-core statistics.  It also exhausts all normalized subsets of
\(\{1,\ldots,10\}\) of sizes 2 through 6 having (M\le200000): 806
configurations.  Among them, 797 satisfy (\Delta\ge0\) and (P\ge\Delta\).
The lexicographically first is

\[
 V=(2,3),\quad q=3,\quad W=6,\quad P=5,\quad\Delta=1.
\]

Yet its bad sets do not cover (direct exact enumeration finds safe residues).
Thus both implications

\[
 \text{LRC}\Longrightarrow P<\Delta,
 \qquad P\ge\Delta\Longrightarrow\text{cover}
\]

are `DISPROVED`.  The maximal recorded slack is 10711 for
(V=(4,5,7,8,9,10)).  These are finite exact computations, not proofs beyond
the stated finite range.

## TASK 9 outcome and narrow barrier

TASK 9 achieves outcomes 4 and 5.  Raw pair overlap is not merely
occasionally too weak: it passes its necessary-cover threshold in 797/806
of the audited cases.  Triple mass is algebraically coupled to its slack by
(7), and the canonical core (8) explains part of the excess.  Therefore
another unlocalized polynomial in the moments is not justified.  The
narrowest surviving question is whether the **off-core spatial distribution**
of uncovered residues and endpoint-block intersections obeys a new arithmetic
inequality.  This is the subject of `TASK10.md`.

---

# TASK 10 audit: endpoint localization and exact gap geometry

Throughout this section the velocities are gcd-normalized.  Put
\(p_i=qb_i\), \(r_i=b_i-1\), and \(D=(\mathbb Z/M\mathbb Z)\setminus C\).

## Theorem 9 (off-core block decomposition) — `PROVED`

In the standard representatives \(0,\ldots,M-1\), the cyclic core \(C\) is
one cyclic interval and its complement is the single (possibly empty) maximal
interval

\[
 D=[\beta,M-\beta]\cap\mathbb Z.                         \tag{9}
\]

For every \(i\), before clipping to (9),

\[
 B_i=\bigcup_{j=0}^{v_i-1}
 \bigl([jp_i-r_i,jp_i+r_i]+M\mathbb Z\bigr).             \tag{10}
\]

Thus \(B_i\setminus C\) is obtained explicitly by intersecting each
translated block in (10) with \([\beta,M-\beta]\); empty intersections are
discarded.  The surviving linear intervals are disjoint.

**Proof.**  The description of \(C\) in Theorem 8 joins through residue zero,
so deleting it leaves exactly (9), including both endpoints.  Theorem 2 says
that in each period \(p_i\), bad residues are precisely the centered integers
\(-r_i,\ldots,r_i\).  There are \(M/p_i=v_i\) periods, giving (10).  Since
\(2r_i+1=2b_i-1<p_i\) for \(q\ge3\), distinct blocks do not meet.  Clipping
preserves disjointness. \(\square\)

## Definition 10 (exact localized statistics)

Let \(m_D(k)=\sum_i1_{B_i\setminus C}(k)\).  The endpoint sweep partitions
\(D\) into maximal integer intervals on which \(m_D\) is constant.  Define

* \(G\): the greatest length of a segment having multiplicity zero (the
  **longest safe run**);
* \(d_{\min},d_{\max}\): the least and greatest distances between starting
  points of consecutive constant-multiplicity segments (zero when there is
  no pair);
* \(A_D=\sum_{k\in D}m_D(k)\), and
  \(P_D=\sum_{k\in D}\binom{m_D(k)}2\), the off-core membership and overlap.

These quantities are independent of runner ordering and reflection
\(k\mapsto-k\).  Gcd normalization makes them invariant under common scaling
\(V\mapsto hV\): both inputs normalize to the same \(V/\gcd(V)\).  They are
not asserted to be invariant if one deliberately works on a nonprimitive,
repeated modulus; normalization is essential.  These assertions are
`PROVED`, directly from (9), (10), and uniqueness of the maximal constant
segments.

## Theorem 11 (endpoint decision algorithm) — `PROVED`

Create events \(+1\) at every clipped block's left endpoint and \(-1\) one
past its right endpoint, combine coincident events, sort, and take prefix
sums.  Then the bad sets cover precisely when every emitted segment has
positive prefix sum.  This decides covering without visiting all \(M\)
residues and simultaneously computes Definition 10.

If \(E\le2\sum_i(v_i+1)+2\) is the number of events before coalescing (the
extra block per runner allows its centered block to split at residue zero), the
algorithm uses \(O(E\log E)\) comparisons and \(O(E)\) storage.  On a bit
model where all inputs and endpoints have \(O(\log M)\) bits, its bit cost is
\(O(E\log E\log M)\) with standard comparison/addition bounds, apart from the
cost of computing \(W\).  Iterated gcd/lcm computes \(W\) in polynomial bit
time in the input lengths.  Correctness follows because an interval indicator
changes only at its two events, and the prefix sum is exactly \(m_D\) between
successive event coordinates. \(\square\)

## Theorem 12 (localized pair certificate) — `PROVED`

Let \(n_D=|D|=M-2\beta+1\).  Then

\[
 \boxed{N A_D-2P_D<Nn_D\quad\Longrightarrow\quad G>0,}   \tag{11}
\]

so (11) proves LRC.  This is genuinely off-core: all forced
\(\binom N2|C|\) pair mass has disappeared.

**Proof.**  Write \(R_D=\sum_{k\in D}(m_D(k)-1)_+\).  Pointwise, for
\(0\le m\le N\),

\[
 \binom m2={m\over2}(m-1)\le {N\over2}(m-1)_+.
\]

Hence \(R_D\ge2P_D/N\).  The covered portion of \(D\) has exact size
\(A_D-R_D\), and therefore at most \(A_D-2P_D/N\).  Inequality (11) makes
this less than \(n_D\), leaving a safe residue. \(\square\)

The criterion is nonvacuous beyond the ordinary union bound.  For
\(V=(2,5)\), one has \((M,n_D,A_D,P_D)=(30,27,27,6)\).  Thus \(S=33>M\),
so the union bound says nothing, while (11) gives \(42<54\).  By the proved
scaling invariance, the same certificate applies to every velocity family
\((2h,5h)\), \(h\ge1\), an infinite class.  This does not claim these are
arithmetically inequivalent after normalization.

The weaker necessary-cover condition \(P_D\ge A_D-n_D\) has no converse.
The smallest audited nontrivial example is again \((2,5)\): it satisfies
\(A_D=n_D\) and \(P_D=6\), but has a safe run of length three.  Thus that
candidate converse is `DISPROVED`.

## Exact collision and limitation — `VERIFIED`

The configurations \((1,4,12)\) and \((2,3,12)\) have the same

\[
 (M,S,P,T,P_D)=(48,55,18,1,15),
\]

but their endpoint partitions have respectively 28 and 20 changes, and
maximum change distances 3 and 4.  Both have longest safe run 3 and neither
covers.  This exact finite collision proves that those five global statistics
do not determine the localized geometry; it does **not** provide different
covering behavior (none was found and claiming one here would amount to a
small LRC counterexample).

## Computational audit — `VERIFIED`

`task10_experiments.py` exhausts all 3,221 gcd-one subsets of
\(\{1,\ldots,12\}\) of sizes 2 through 7.  It also checks 36 standard
consecutive, odd, powers-of-two, and translated families through \(N=10\),
and 289 deterministic sliding subsets of the divisors of
\(60,120,360,840\).  Exactly 315 audited records satisfy (11), no audited
cover occurs, and the collision above is reproduced.  `test_localization.py`
independently compares endpoint output with residue-by-residue construction on
180 seeded random cases.  These finite claims are evidence against coding
errors, not general proofs.

## TASK 10 outcome and narrow barrier

The sweep gives an exact sublinear-in-\(M\) decision procedure, and (11) is a
proved localized sufficient inequality covering a scalable class missed by
the union bound.  However, it certifies only 315 of 3,546 audited records.
The collision shows that \((M,S,P,T,P_D)\) cannot recover even endpoint
geometry.  The narrowest remaining barrier is to use the **ordered signed
endpoint word** itself—rather than finitely many aggregate moments—to force a
zero prefix sum.  This is posed in `TASK11.md`.
