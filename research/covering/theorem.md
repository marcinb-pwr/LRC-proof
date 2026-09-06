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

---

# TASK 11 audit: the ordered endpoint word

Keep the notation of Theorem 9 and write \(H=M-\beta+1\), so the integer domain \(D\) is the half-open interval \([\beta,H)\cap\mathbb Z\).

## Theorem 13 (exact realizable word) — `PROVED`

For each \(i\), set \(p_i=qb_i\) and \(r_i=b_i-1\). Reduce each cyclic interval \[jp_i-r_i,jp_i+r_i]+M\mathbb Z\) to its one or two inclusive components \(I=[a,c]\subseteq[0,M-1]\). For every nonempty clipped component \(I\cap D=[\ell,u]\), form the labelled half-open events

\[
 (\ell,+1),\qquad (u+1,-1). \tag{12}
\] Add the zero sentinels \((\beta,0),(H,0)\), combine equal coordinates by adding their signs, and sort. The result is precisely the coalesced word \(\mathcal W=((x_0,\delta_0),\ldots,(x_s,\delta_s))\). Conversely, a word arises from the normalized CRT construction **if and only if** there are distinct positive integers \(v_i\) of gcd one, with

\[
 q=N+1,\quad W=\operatorname {lcm}(v_i),\quad b_i=W/v_i,\quad b_i\mid W,
\]

for which (12), coalescing, and the two sentinels produce that word. This is an exact finite characterization, not a claim that the restrictions below alone are sufficient.

**Proof.** Equation (10) gives the inclusive block \([jp_i-r_i,jp_i+r_i]\), with its possible split at zero. Reducing modulo \(M\) and intersecting its components with \(D\) gives the intervals used in (12). An inclusive interval changes its indicator by \(+1\) at its left endpoint and by \(-1\) one after its right endpoint. Indicator addition proves the forward statement. The reverse direction is immediate from the displayed construction and Theorem 9. □

This description is implemented directly; it never visits the \(M\) residues. Before coalescing it has at most \(2\sum_i(v_i+1)+2\) events.

## Proposition 14 (word restrictions) — `PROVED`

Every realizable word has all of the following properties.

1. \(x_j\in\mathbb Z\), \(\beta=x_0<x_1<\cdots<x_s=H\), and consecutive spacings are positive integers.
2. Its prefix multiplicities \(h_j=\sum_{k\le j}\delta_k\) on \([x_j,x_{j+1})\) are integers in \([0,N]\); the total signed change is zero. A safe integer exists exactly when some \(h_j=0\).
3. Reflection is exact: \(\delta(M+1-x)=-\delta(x)\). Hence zero segments occur in reflected pairs, except for a possible self-reflected central segment.
4. An unclipped event belonging to runner \(i\) is respectively
   \[
   x=b_i(qj-1)+1\equiv1-b_i\pmod{qb_i},\qquad
   x=b_i(qj+1)\equiv b_i\pmod{qb_i}. \tag{13}
   \]
   Its paired endpoints differ by \(2b_i-1\); the gap from its right event to the next left event of that runner is \(b_i(q-2)+1\).
5. At the left boundary, runner \(i\) contributes the clipped interval \([\beta,b_i-1]\) exactly when \(b_i>\beta\); reflection gives its right boundary mate.

Items 1–2 hold for arbitrary finite interval systems (with \(N\) interval families); reflection additionally needs reflection invariance. The divisibility, residue, exact two-spacing pattern (13), boundary rule, and shared \(q,W\) are the genuinely CRT-forced restrictions.

**Proof.** Prefix sums add interval indicators, proving 1–2. Reflection sends an inclusive interval \([a,b]\) to \([M-b,M-a]\), and therefore sends its \(+1\) event at \(a\) to the \(-1\) event at \(M+1-a\); this proves the symmetry, including after coalescing. Substitution of \(p_i=qb_i,r_i=b_i-1\) proves (13) and both differences. Finally the centered block is \([-(b_i-1),b_i-1]\) modulo \(M\), so clipping it to \(D\) gives precisely the boundary rule. □

## Natural order conjectures — `DISPROVED`

The claims that (i) nonzero net signs strictly alternate and (ii) every coalesced change has absolute value one both fail already for \(V=(1,4)\): at \(M=12\) a coincident event has change \(2\) (and its reflection has change \(-2\)). The claim that every consecutive event gap is at least \(\beta\) fails for \(V=(2,3)\): here \(\beta=2\), but unit gaps occur. Thus congruences and endpoint pairing do not imply the most natural interlacing theorem. These are explicit exact counterexamples, not merely failed searches.

## Theorem 15 (a genuine infinite normalized class) — `PROVED`

If no velocity is divisible by \(q=N+1\), then the word has a zero prefix on the segment containing \(x=W\), and LRC holds. In particular, for every fixed \(N\ge2\),

\[
 V_m=\{1,2,\ldots,N-1,m\},\qquad m>N,\quad q\nmid m,
\]

is an infinite family of pairwise distinct gcd-normalized configurations certified by the ordered sweep.

**Proof.** At \(x=W\), reduction modulo \(qb_i\) is multiplication by \(b_i\) of \(v_i\bmod q\). Its cyclic distance from zero is \(b_i\min(r,q-r)\ge b_i\), where \(r\in\{1,\ldots,q-1\}\); hence \(W\notin B_i\) for every \(i\). Since \(W\in D\), its constant segment has prefix zero. The displayed family has gcd one, distinct entries, and infinitely many allowable \(m\). □

This theorem uses an arithmetically distinguished coordinate rather than a general prefix principle; it does not resolve configurations containing a multiple of \(q\).

## Computational audit and finite-state obstruction — `VERIFIED` / `OPEN`

`task11_experiments.py` exhausts all 65,242 gcd-one subsets of \(\{1,\ldots,16\}\) of sizes 2 through 16, plus 44 standard and 558 divisor families (65,844 total). No cover occurs. The independent regression test compares segment prefixes with direct modular membership on 250 seeded random configurations and checks reflection antisymmetry.

The search also held fixed the finite unordered summary \((N,M,\beta,\#\mathcal W,\{\!\{\delta\}\!\},\{\!\{x_{j+1}-x_j\}\!\})\). It found no pair with different numbers of zero-prefix segments. The weaker summary omitting the gap multiset likewise had no such collision in this scope. This is `VERIFIED` finite evidence only: neither summary has been proved sufficient, and no collision has been proved impossible.

The narrow obstruction is now precise. General interval constraints give only a nonnegative bridge \(h_j\) with antisymmetric event increments; such bridges can stay strictly positive. CRT adds the simultaneous congruences (13), but the simplest spacing and interlacing consequences are disproved above. A universal theorem must exploit the **association** of each paired gap \(2b_i-1\) with its residue class and with the common divisibility system \(b_i\mid W\); unordered endpoint data have not supplied it. Establishing such a labelled-word theorem is `OPEN`.

---

# TASK 12 audit: labelled pairs and the divisor poset

## Theorem 16 (lossless labelled sweep) — `PROVED`

Give each clipped component in (12) a pair identifier and attach to both of its events

\[
(i,v_i,b_i,p_i,j,\text{centre},\text{mate},\text{wrapped},
 \text{clipped},x\bmod p_i).
\]

Sorting these records by coordinate, without combining records at a coincident coordinate, is lossless: grouping at coordinate \(x\), summing the signs, and taking prefixes recovers exactly \(m_D\). Each pair has one \(+1\) and one \(-1\) record, and the two mate fields are reciprocal. The number of records is at most \(2\sum_i(v_i+1)\), independent of \(M\).

**Proof.** The construction retains both half-open boundary events of every component used in Theorem 13. Thus no interval datum is discarded. At a point \(x\), the sum of all records with that coordinate is exactly the change of the sum of the interval indicators. Induction through the sorted groups proves the prefix assertion. Component splitting can add at most one component for each runner, giving the bound. □

`labelled_pairs.py` implements this construction. In particular, coincident opposite signs are retained even when their net contribution to the old coalesced word is zero.

## Theorem 17 (divisor-poset and coincidence laws) — `PROVED`

For every nonempty index set \(I\),

\[
 \gcd_{i\in I}(b_i)=\frac{W}{\operatorname{lcm}_{i\in I}(v_i)},
 \qquad
 \operatorname{lcm}_{i\in I}(b_i)=\frac{W}{\gcd_{i\in I}(v_i)}. \tag{14}
\]

Consequently \(\operatorname{lcm}_i b_i=W\) after gcd normalization, and

\[
 \gcd(p_i,p_k)=q\gcd(b_i,b_k),\qquad
 \operatorname{lcm}(p_i,p_k)=q\operatorname{lcm}(b_i,b_k). \tag{15}
\]

For unclipped interior events, same-sign coincidences occur exactly when

\[
 b_i(qj\mp1)=b_k(q\ell\mp1),                            \tag{16}
\]

with the upper choice for left events and lower choice for right events. An opposite-sign coincidence occurs exactly when

\[
 b_i(qj-1)+1=b_k(q\ell+1),                              \tag{17}
\]

or with \(i,k\) exchanged. In particular, (17) forces
\(\gcd(b_i,b_k)=1\). Boundary-clipped events are explicit exceptions and must not be subjected to (16)–(17).

**Proof.** Apply each prime valuation to \(b_i=W/v_i\): the minimum of \(\nu(W)-\nu(v_i)\) is \(\nu(W)\) minus the maximum valuation, and the maximum is \(\nu(W)\) minus the minimum. This proves (14), including the normalized conclusion. Equation (15) follows by factoring out the common \(q\). Substituting the two interior coordinates from (13) gives (16) and (17). In (17), every term except the final \(1\) is divisible by \(\gcd(b_i,b_k)\), so that gcd divides one. □

Thus the labelled word carries substantially more than a sign sequence: opposite-sign cancellation in the interior is possible only between coprime nodes of the \(b\)-divisibility system.

## Theorem 18 (exact central classification) — `PROVED`

At \(x=W\), runner \(i\) is bad if and only if \(q\mid v_i\). If \(v_i=qa_i\), the unique block of runner \(i\) containing \(W\) is centred there and has labelled events

\[
 W-b_i+1\quad(+1),\qquad W+b_i\quad(-1).                \tag{18}
\]

Hence the central covering intervals are nested by reverse velocity order. If \(v_*\) is the largest velocity divisible by \(q\), its interval is the innermost, with \(b_*=W/v_*\); the first event of a central covering runner met on either side of \(W\) is the corresponding event of this innermost pair (allowing coincidences).

**Proof.** Modulo \(qb_i\), \(W=v_i b_i\). Its cyclic distance from zero is \(b_i\|v_i\|_{\mathbb Z/q\mathbb Z}\), which is strictly below \(b_i\) exactly when it is zero, namely \(q\mid v_i\). In that case the centre index is \(a_i=v_i/q\), and substitution in the block formula gives (18). Since \(b_i=W/v_i\), increasing velocity decreases the radius and proves nesting. □

## Innermost-pair descent — `DISPROVED`

Two natural precise versions fail.

* “Both exterior boundary points \(W-b_*\) and \(W+b_*\) are safe” already fails for \(V=(1,3)\): the two points are \(2,4\), and only \(4\) is safe.
* “At least one of those two points is safe” fails for \(V=(3,4)\): \(q=3,W=12,b_*=4\), and neither \(8\) nor \(16\) is safe, although the full word has two other zero segments.

Restricting to the runners divisible by \(q\) is not an LRC descent: if their number is \(m<N\), their own conjectural threshold is \(1/(m+1)\), whereas the inherited covering problem uses \(1/(N+1)\). No implication in the required direction follows merely by deletion. Thus the tested innermost pair neither locates a safe point universally nor supplies a smaller LRC instance.

## Theorem 19 (new central-boundary family) — `PROVED`

Suppose exactly one velocity \(v_*\) is divisible by \(q\), it is the largest velocity, and every other velocity satisfies

\[
 v_i\bmod q\in\{1,2,\ldots,q-2\}.                       \tag{19}
\]

Then \(x=W+\beta\), where \(\beta=W/v_*\), is safe for every runner. In particular, for each fixed \(N\ge2\),

\[
 \boxed{V_m=\{1,2,\ldots,N-1,(N+1)m\}},\qquad m\ge1,   \tag{20}
\]

is an infinite gcd-normalized family. It is not covered by Theorem 15 because its last velocity is divisible by \(q\).

**Proof.** For \(v_*\), (18) ends immediately before \(W+\beta\), so strict badness fails there. For another runner put \(s=\beta/b_i=v_i/v_*\), so \(0<s<1\). In units of \(b_i\), the residue of \(W+\beta\) modulo \(qb_i\) is \(r+s\), with \(r=v_i\bmod q\). Under (19), \(r+s>1\), while \(q-(r+s)\ge2-s>1\), with equality in the first inequality when \(r=q-2\). Thus the cyclic distance is at least one unit \(b_i\), so the point is not bad. Family (20) satisfies (19), has only its last member divisible by \(q\), has gcd one, and has unbounded, distinct normalized members. □

(The displayed estimate deliberately excludes residue \(q-1\), for which the right boundary can be bad. Reflection gives the analogous theorem using \(W-\beta\) when residues lie in \(\{2,\ldots,q-1\}\).)

## Computational audit — `VERIFIED`

`task12_experiments.py` exhausts all 65,242 gcd-one subsets of \(\{1,\ldots,16\}\). Of these, 39,506 cover \(W\), while none covers the whole residue circle. It reproduces the two smallest boundary failures above and finds the first configuration with multiple central coverers at \((1,4,8)\). It additionally checks 602 standard, divisor, and Theorem 19 families. `test_labelled_pairs.py` checks mate reciprocity, labelled-prefix equality against direct modular membership on 250 seeded random inputs, and the central classification. These finite facts are verification, not proofs beyond their stated scope.

## Weil/Kloosterman feasibility audit — `KNOWN` / `OPEN`

The classical Weil bound controls complete Kloosterman sums

\[
 S(a,b;p)=\sum_{x\in\mathbb F_p^\times}e_p(ax+b x^{-1}),
 \qquad |S(a,b;p)|\le2\sqrt p
\]

when \(p\) is prime and \(ab\ne0\); composite-modulus variants include divisor and gcd factors. Kloosterman paths concern normalized partial sums of this same inverse-phase sequence. These are `KNOWN` results, but **they do not apply directly to the present endpoint word**. Equations (12)–(18) contain affine phases and divisibility conditions over the generally composite modulus \(qW\), not a complete finite-field sum with an inverse phase. Fourier-expanding an interval indicator produces ordinary geometric (Dirichlet-kernel) sums; calling those Kloosterman sums would be incorrect.

A possible future route is therefore conditional and `OPEN`: first derive an averaging or prime-modulus reduction in which the varying velocities produce a genuine phase \(av+bv^{-1}\pmod p\), with all velocities units and with truncation errors controlled strongly enough to imply a sign or covering statement. Only after that reduction would Weil bounds or Kloosterman-path estimates have verified hypotheses. No such reduction is established here, so no cancellation theorem is invoked by name as a substitute for an argument.

## TASK 12 outcome and narrow barrier

The labelled audit yields a new infinite class and exact coincidence restrictions, while the smallest descent conjectures fail. The surviving local problem is asymmetric: when \(W\) is covered, noncentral runners with residues \(1\) and \(q-1\) can cover opposite exterior boundaries of the innermost pair. A useful next theorem must control those two fringe populations jointly, using their labelled event distances rather than deleting them or appealing prematurely to exponential-sum cancellation.

**Literature reference for the `KNOWN` input.** A. Weil, “On some exponential sums,” *Proceedings of the National Academy of Sciences* **34** (1948), 204–207, proves the Riemann-hypothesis-over-finite-fields estimate underlying the displayed prime-modulus Kloosterman bound. This audit uses only the stated classical consequence and, as explained above, does not apply it to an LRC sum.

---

# TASK 13 audit: exact central fringes and exponential-sum obstruction

## Theorem 20 (exact signed fringe distance) — **PROVED**

Assume \(W\) is covered, let \(v_*=\max\{v_i:q\mid v_i\}\), and put \(b_*=W/v_*\). For an integer \(h\) and either sign, define

\[
 x_h^\pm=W\pm h b_*.
\]

For runner \(i\), the cyclic distance of \(x_h^\pm\) from the closest centre modulo \(qb_i\) is exactly

\[
 d_i^\pm(h)=b_i\,\operatorname{dist}_{\mathbb R/q\mathbb Z}
 \left(v_i\pm h\,{v_i\over v_*},0\right).               \tag{21}
\]

The signed integer clearance from its closed bad block is

\[
 \boxed{c_i^\pm(h)=d_i^\pm(h)-(b_i-1)}.                 \tag{22}
\]

Thus \(x_h^\pm\) is safe for all runners if and only if
\(\min_i c_i^\pm(h)>0\). Formula (22) is an exact labelled two-sided fringe criterion, not a moment bound.

**Proof.** Since \(W=v_i b_i\) and \(b_*/b_i=v_i/v_*\), division of \(x_h^\pm\) by \(b_i\) gives the argument in (21). Multiplication by \(b_i\) converts distance modulo \(q\) to distance modulo \(qb_i\). The bad integers around a centre have radius \(b_i-1\), so subtracting that radius gives (22). All quantities are integers although (21) is written in scaled rational form. □

*central_fringe.py* evaluates the equivalent integer modular formula and does not scan \(M\).

## Theorem 21 (complete first-fringe classification) — **PROVED**

Suppose \(v_*\) is the unique velocity divisible by \(q\) and is also the largest velocity. Then

\[
 \begin{aligned}
 W+b_*\text{ is bad for a noncentral }v_i
   &\iff v_i\equiv-1\pmod q,\\
 W-b_*\text{ is bad for a noncentral }v_i
   &\iff v_i\equiv 1\pmod q.                            \tag{23}
 \end{aligned}
\]

The central runner itself is safe at both points. Consequently, absence of the \(-1\) fringe certifies \(W+b_*\), absence of the \(+1\) fringe certifies \(W-b_*\), and if both fringe populations are present then both first-boundary candidates are bad.

**Proof.** For a noncentral runner write \(r=v_i\bmod q\) and \(s=v_i/v_*\). The hypotheses give \(r\in\{1,\ldots,q-1\}\) and \(0<s<1\). At the plus point, the scaled residue is \(r+s\). Its distance from \(q\mathbb Z\) is below one exactly for \(r=q-1\): for \(r\le q-2\), both \(r+s>1\) and \(q-r-s\ge2-s>1\). At the minus point the scaled residue is \(r-s\), whose distance is below one exactly for \(r=1\); the other cases follow by the same inequalities. For \(v_*\), the points lie exactly one radius unit from its centre and strict badness fails. □

The smallest mixed-fringe example is \(V=(1,3,4)\): its minus boundary is blocked by velocity \(1\), and its plus boundary by velocity \(3\). This is not an LRC counterexample; for this particular configuration \(W+3b_*\) is safe.

## Corollary 22 (an infinite \(-1\)-fringe family) — **PROVED**

For every \(N\ge3\), \(q=N+1\), and \(m\ge1\),

\[
 \boxed{V_m=\{2,3,\ldots,N,qm\}}                       \tag{24}
\]

is gcd-normalized and is certified at \(x=W-b_*\). For \(N=2\), the same conclusion holds for \(V_m=\{2,3m\}\) whenever \(m\) is odd. These families contain a \(q-1\) residue and a \(q\)-divisible velocity, so they are outside Theorem 15 and are the reflected complement of the family in (20).

**Proof.** The noncentral residues in (24) are \(2,\ldots,q-1\), so residue \(1\) is absent and Theorem 21 applies. For \(N\ge3\), the set contains consecutive integers \(2,3\), hence has gcd one; \(qm>N\), so its entries are distinct. For \(N=2\), \(\gcd(2,3m)=1\) exactly when \(m\) is odd. □

## Proposition 23 (obstruction to a direct Kloosterman reduction) — **PROVED**

The natural Fourier expansion of the labelled endpoint system does not produce a Kloosterman sum. For a fixed runner, summing over its centre index \(j\) gives phases affine in \(j\), hence a finite geometric sum. Summing over the selected velocities gives an arbitrary finite subset, not a complete multiplicative group. Rewriting \(v_i=W/b_i\) introduces a formal inverse in \(b_i\), but does not repair either defect:

1. if the finite-field prime \(p\mid W\), then \(W/b\) is not represented by multiplication by \(b^{-1}\) modulo \(p\), and some relevant \(b\)'s are nonunits;
2. if \(p\nmid W\), the values \(\{b_i\}\) are still a freely selected sparse subset of the divisors of \(W\), not all of \(\mathbb F_p^\times\), and carry nonuniform interval weights.

Therefore the hypotheses of the complete Weil bound displayed above are absent. Completion of an arbitrary weighted subset introduces its full Fourier coefficients; without a separate norm estimate, the triangle inequality loses the desired square-root saving. This proves an obstruction to the **direct** Weil/Kloosterman route, not to every possible future transformation of LRC.

**Proof.** Interior endpoints have the affine forms \(b_i(qj-1)+1\) and \(b_i(qj+1)\), so an additive character in the endpoint coordinate is geometric as \(j\) varies. The LRC input permits an arbitrary distinct set of velocities, so it supplies neither completeness nor uniform weights in the \(i\)-variable. The two cases for \(p\) establish the stated inverse-parametrization obstruction. The standard completion identity expresses a weighted incomplete sum as a linear combination of complete twisted sums; bounding each by Weil and then taking absolute values necessarily introduces the \(\ell^1\)-norm of the completion coefficients, for which the current theory provides no saving. □

Thus Weil bounds and Kloosterman paths should not presently be inserted into the proof. A legitimate future use requires a new theorem that first creates a complete or quantitatively controlled incomplete inverse-phase sum.

## Computational audit — **VERIFIED**

*task13_experiments.py* exhausts all 261,565 gcd-one subsets of \(\{1,\ldots,18\}\). Exactly 17,329 have a unique \(q\)-divisible velocity that is globally largest; all satisfy (23). The first configuration containing both fringe populations is \((1,3,4)\). The independent randomized test checks (21)–(23) against direct modular badness on 300 inputs and over 100 admissible unique-central inputs. These results test the implementation and theorem boundaries; the proofs above do not depend on them.

## TASK 13 outcome and narrow barrier

The first fringe is now completely classified and yields the new family (24). Mixed \(+1/-1\) fringes defeat both immediate boundary points, while \((1,3,4)\) shows that a more distant \(h\)-boundary can still succeed. The narrow next problem is to understand the finite word in the step parameter \(h\): determine whether the exact clearances (22), for \(1\le h<q\) or a rigorously enlarged range, force a common positive column. This is a finite simultaneous-avoidance problem before it is an exponential-sum problem.


---

# TASK 14 audit: the step-parameter clearance word

## Theorem 24 (exact modular-arc word) — **PROVED**

Assume \(W\) is covered and retain \(v_*,b_*\) from Theorem 20. For a runner \(i\) and a choice \(\epsilon\in\{-1,+1\}\), put

\[
 m_i=qb_i,\qquad g_i=\gcd(b_*,m_i),\qquad H_i={m_i\over g_i}.
\]

Its bad steps are exactly the following union of residue classes:

\[
 A_i^\epsilon=
 \left\{h\bmod H_i:
 \epsilon h b_*\equiv-W+u\pmod {m_i}
 \text{ for some }-(b_i-1)\le u\le b_i-1\right\}.       \tag{25}
\]

Equivalently, they are the inverse image under the affine map
\(h\mapsto W+\epsilon h b_*\pmod {m_i}\) of the centered modular interval
\([-(b_i-1),b_i-1]\). In particular,

\[
 c_i^\epsilon(h)>0\iff h\bmod H_i\notin A_i^\epsilon.   \tag{26}
\]

This is an exact union-of-residue-classes description. It is usually more compact to store the affine map, modulus, and target arc than to enumerate the classes.

**Proof.** Runner \(i\) is bad precisely when the residue of
\(W+\epsilon h b_*\) modulo \(m_i\) has a representative \(u\) in the displayed centered interval. Rearranging gives (25). The kernel period of multiplication by \(b_*\) modulo \(m_i\) is \(m_i/\gcd(b_*,m_i)=H_i\), proving both periodicity and (26). □

## Theorem 25 (least natural common period) — **PROVED**

The labelled residue motion of runner \(i\) has period

\[
 H_i={qv_*\over\gcd(qv_*,v_i)},                          \tag{27}
\]

and its common period over all runners is exactly

\[
 \boxed{H=\operatorname{lcm}_iH_i=qv_*}.                \tag{28}
\]

Thus \(1\le h<H\) is the least common-period range justified solely by the normalized arithmetic. The shorter range \(1\le h<q\) has no analogous periodic completeness property.

**Proof.** The condition that \(h\) be a period is
\(qb_i\mid hb_*\). Substituting \(b_i=W/v_i\) and \(b_*=W/v_*\), and clearing denominators, gives \(qv_*\mid hv_i\); its least positive solution is (27). For a fixed integer \(L\),
\[
 \operatorname{lcm}_i {L\over\gcd(L,v_i)}
 ={L\over\gcd(L,\gcd_i v_i)}.
\]
This follows prime by prime. Taking \(L=qv_*\) and using
\(\gcd_i v_i=1\) proves (28). □

The full badness vector can accidentally have a smaller period because interval indicators may identify different residues, but \(H\) is the exact common period of the underlying labelled residue motions and is therefore the canonical unconditional range.

## Theorem 26 (finite covering criterion and union certificate) — **PROVED**

Lift every \(A_i^+\subseteq\mathbb Z/H_i\mathbb Z\) to
\(\widetilde A_i\subseteq\mathbb Z/H\mathbb Z\). Then a safe step in one full period exists exactly when

\[
 \bigcup_i\widetilde A_i\ne\mathbb Z/H\mathbb Z.         \tag{29}
\]

In particular, the quantitative certificate

\[
 \boxed{\sum_i |A_i^+|\,{H\over H_i}<H}                 \tag{30}
\]

implies a safe step and hence LRC. Intersections may be retained through exact inclusion-exclusion on the lifted sets; (30) is only the first, deliberately labelled union bound.

**Proof.** Equations (26) and (28) say that a step is safe exactly when it belongs to none of the lifted bad sets, proving (29). Each class modulo \(H_i\) has \(H/H_i\) lifts modulo \(H\). The union bound then proves (30). □

The additive characters arising from (25) are linear in \(h\). Fourier inversion on \(\mathbb Z/H\mathbb Z\) is exact, but it produces ordinary cyclic Fourier coefficients of modular intervals. There is no inverse phase and hence no Kloosterman sum at this stage.

## Short-range and full-period obstructions — **DISPROVED** / **VERIFIED**

The conjecture that some \(W\pm hb_*\) with \(1\le h<q\) is always safe is **DISPROVED** by

\[
 V=(1,3,8),\qquad q=4.
\]

Direct use of (25) shows that all six signed candidates are bad. This is not an LRC counterexample; it only defeats the proposed step range.

Even the full canonical period need not contain a safe point. The finite audit finds the smallest example

\[
 V=(1,3,4,5,7,18),\qquad q=7,\quad v_*=7,\quad H=49,    \tag{31}
\]

for which every point \(W+h b_*\), \(h\in\mathbb Z/H\mathbb Z\), is bad for at least one runner. This statement is **VERIFIED** by exact enumeration of the 49 step classes, not promoted to a general theorem and not claimed to be an LRC counterexample. Reflection means that a separate negative-\(h\) full-period scan adds nothing.

## Theorem 27 (an infinite mixed-fringe family) — **PROVED**

For every \(m\ge1\), the normalized three-runner configuration

\[
 \boxed{V_m=\{1,3,4m\}}                                 \tag{32}
\]

satisfies LRC. It contains both fringe residues \(1\) and \(-1\bmod4\), as well as the central velocity \(4m\). Define

\[
 h_m=\begin{cases}
 3m+1,&4\mid m,\\
 3m,&4\nmid m.
 \end{cases}
\]

Then \(x=W+h_m b_*\) is safe.

**Proof.** In time coordinates the proposed point is
\[
 t={x\over4W}={1\over4}+{h_m\over16m}.
\]
For velocity \(4m\), its fractional position is \(h_m/4\); by construction
\(4\nmid h_m\), so its distance from an integer is at least \(1/4\).
If \(h_m=3m\), then
\[
 t={7\over16},\qquad 3t={21\over16}\equiv{5\over16}\pmod1.
\]
If \(4\mid m\) and \(h_m=3m+1\), then
\[
 t={7\over16}+{1\over16m},\qquad
 3t\equiv{5\over16}+{3\over16m}\pmod1.
\]
Here \(m\ge4\), so both displayed distances lie in \([1/4,3/4]\).
Thus all three runners meet the exact threshold \(1/4\). The set has gcd one and its members are distinct, proving the claim for an infinite normalized family. □

## Computational audit — **VERIFIED**

*task14_experiments.py* exhausts the 159,062 gcd-one subsets of
\(\{1,\ldots,18\}\) for which \(W\) is covered. It finds 14,136 failures of
the short range \(1\le h<q\), beginning with \((1,3,8)\), and 19 failures of
the full labelled-motion period, beginning with (31). The modular-arc
implementation is independently compared with direct clearance calculations
on more than 500 signed random records, and (32) is checked for
\(1\le m\le100\). These computations validate the implementation and locate
finite obstructions; they are not evidence of an LRC counterexample.

## TASK 14 outcome and narrow barrier

The step word is now an exact finite covering problem on
\(\mathbb Z/(qv_*)\mathbb Z\). It proves the mixed-fringe family (32), but the
19 full-period obstructions show that this one-dimensional subgroup cannot
settle LRC universally. The narrowest next problem is to add a second
arithmetically natural direction \(x=W+h b_*+k b^\dagger\), where
\(b^\dagger\) must be chosen from the labelled divisor poset, and determine
whether the resulting two-dimensional finite torus has an uncovered point.
