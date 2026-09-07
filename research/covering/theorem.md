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

---

# TASK 15 audit: the two-direction quotient

## Definition 28 (canonical second label) — **PROVED well-defined under a covered word**

Assume the one-direction word is covered. Call a noncentral runner *active* when its bad set in $\mathbb Z/(qv_*)\mathbb Z$ is nonempty. Among the active labels choose the numerically least divisor $b_i=W/v_i$ (equivalently, the largest active velocity), and call it $b^\dagger=W/v^\dagger$. This rule uses the labelled divisor poset and the already known word; it never examines a two-direction safe point.

There is an active noncentral label: the central runner is safe at every $h\not\equiv0\pmod q$, so it cannot cover a covered word alone. Thus the definition is well-defined. The least numerical element is in particular minimal in the divisibility order (although that order can have incomparable minimal elements).

## Theorem 29 (period lattice and Smith form) — **PROVED**

Put $M=qW$, $d=\gcd(b_*,b^\dagger)$, and $L=M/d$. The exact period lattice of

$$
 (h,k)\longmapsto W+h b_*+k b^\dagger\pmod M
$$

is

$$
 K_2=\{(h,k)\in\mathbb Z^2:M\mid h b_*+k b^\dagger\}. \tag{33}
$$

Moreover

$$
 \boxed{\mathbb Z^2/K_2\cong\mathbb Z/L\mathbb Z,\qquad
 \operatorname{SNF}(K_2\hookrightarrow\mathbb Z^2)=\operatorname{diag}(1,L)}. \tag{34}
$$

Writing $\ell=\operatorname{lcm}(v_*,v^\dagger)$, one has $d=W/\ell$, $L=q\ell$, and the apparent two-dimensional torus is the cyclic orbit

$$
 \boxed{x_z=W+zd\pmod M,\quad z\in\mathbb Z/L\mathbb Z}. \tag{35}
$$

**Proof.** Equation (33) is the kernel definition. Bézout gives $\langle b_*,b^\dagger\rangle=d\mathbb Z$, so the image modulo $M$ is $d\mathbb Z/M\mathbb Z$, of order $L$. The first isomorphism theorem proves (34); a rank-two sublattice with cyclic quotient of order $L$ has Smith invariants $1,L$. Finally $\gcd(W/a,W/b)=W/\operatorname{lcm}(a,b)$ for $a,b\mid W$. □

This rank collapse is the precise higher-dimensional obstruction exposed by TASK 15: scalar directions in one residue circle never create a genuine rank-two quotient.

## Theorem 30 (exact affine modular strips) — **PROVED**

For runner $i$, put $m_i=qb_i$, $g_i=\gcd(d,m_i)$, and $H_i=m_i/g_i$. Its bad strip is

$$
 \mathcal A_i=\{(h,k)+K_2:\operatorname{dist}_{\mathbb Z/m_i\mathbb Z}
 (W+h b_*+k b^\dagger,0)\le b_i-1\}. \tag{36}
$$

Under (35), this is the lift to $\mathbb Z/L\mathbb Z$ of

$$
 A_i=\{z\bmod H_i:zd\equiv-W+u\pmod {m_i},\ |u|\le b_i-1\}. \tag{37}
$$

**Proof.** Badness is membership in the centered closed residue arc of radius $b_i-1$. Multiplication by $d$ modulo $m_i$ has kernel period $H_i$, giving (37); (35) gives the identification. □

## Theorem 31 (labelled union and gcd-intersection certificates) — **PROVED**

Let $\widetilde A_i$ lift (37) to $\mathbb Z/L\mathbb Z$. An uncovered point exists iff $\bigcup_i\widetilde A_i\ne\mathbb Z/L\mathbb Z$. For two labels,

$$
 |\widetilde A_i\cap\widetilde A_j|
 ={L\over\operatorname{lcm}(H_i,H_j)}
 \#\{(a,b)\in A_i\times A_j:a\equiv b\pmod{\gcd(H_i,H_j)}\}. \tag{38}
$$

For every spanning tree $T$ on the labels,

$$
 \boxed{\sum_i |A_i|{L\over H_i}
 -\sum_{ij\in E(T)}|\widetilde A_i\cap\widetilde A_j|<L} \tag{39}
$$

certifies a safe point and hence LRC.

**Proof.** Generalized CRT gives the compatibility condition in (38), after which there are $L/\operatorname{lcm}(H_i,H_j)$ lifts. To prove (39), root $T$ and add its sets one vertex at a time. The increase in the union is at most the size of the new set minus its intersection with its parent. Strict inequality leaves a class uncovered. □

## Proposition 32 (exact strip Fourier transform) — **PROVED**

With $\widehat f(n)=L^{-1}\sum_{z\bmod L}f(z)e^{-2\pi inz/L}$ and $f_i=1_{\widetilde A_i}$,

$$
 \widehat f_i(n)=0\quad\text{unless }n={L\over H_i}s,
$$

and then

$$
 \boxed{\widehat f_i((L/H_i)s)
 ={1\over H_i}\sum_{a\in A_i}e^{-2\pi isa/H_i}.} \tag{40}
$$

**Proof.** Write every lift as $a+rH_i$ and sum the geometric progression in $r$. □

The phase is linear: no inverse phase or Kloosterman sum appears.

## Computational audit — **VERIFIED**

The canonical rule resolves all 19 TASK 14 full-period obstructions. A separate exhaustive audit of all 18,969 gcd-one subsets of $\{1,\ldots,15\}$ whose centre $W$ is covered found no covered canonical two-direction quotient. Hence there is **no smallest covered configuration in that finite scope**. This is not a universal theorem. The scripts use periods $q\operatorname{lcm}(v_*,v^\dagger)$, never scan $M=qW$, and independently check (35) and (38) on seeded random inputs.

## TASK 15 outcome and narrow barrier

The second label clears every known TASK 14 obstruction. But Theorem 29 disproves the premise that it creates a genuinely two-dimensional torus. The narrow open question is

$$
 \boxed{\textbf{OPEN: }\text{must the canonical two-label lcm grid contain a safe class?}} \tag{41}
$$

Neither (39) nor computation proves (41). A counterexample or a proof using the exact gcd intersections is required before adding further labels.

---

# TASK 16 audit: optimized intersection certificates

## Theorem 33 (optimal tree certificate) — **PROVED**

For the lifted bad sets $B_i=\widetilde A_i\subseteq\mathbb Z/L\mathbb Z$, assign the complete labelled graph the weights

$$
 w_{ij}=|B_i\cap B_j|,
$$

computed exactly by (38). If $T_{\max}$ is a maximum-weight spanning tree, then

$$
 \boxed{|\bigcup_iB_i|\le U_T:=\sum_i|B_i|-\sum_{ij\in T_{\max}}w_{ij}.} \tag{42}
$$

Moreover $U_T$ is the smallest upper bound obtainable from (39) by choosing a spanning tree. Thus $U_T<L$ is the optimal certificate in this precisely delimited pairwise-tree class.

**Proof.** The proof of (39) applies to every tree. Its vertex term is independent of the tree, so minimizing the right side is exactly maximizing the sum of edge weights. Kruskal's algorithm returns a maximum-weight spanning tree: when it accepts an edge joining two current components, any spanning tree must cross that cut, and the standard exchange replaces such a crossing edge by the no-lighter greedy edge without destroying a spanning tree. Iteration proves optimality. □

This is an optimization only within the tree certificates; it is not claimed optimal among every inequality using pairwise data.

## Theorem 34 (arbitrary labelled intersections and third Bonferroni bound) — **PROVED**

For a nonempty label set $J$, let $H_J=\operatorname{lcm}_{j\in J}H_j$. Then

$$
 \boxed{|\bigcap_{j\in J}B_j|={L\over H_J}
 \#\{z\bmod H_J:z\bmod H_j\in A_j\ \forall j\in J\}.} \tag{43}
$$

In particular, writing $S_r=\sum_{|J|=r}|\bigcap_{j\in J}B_j|$, the third Bonferroni inequality gives

$$
 \boxed{|\bigcup_iB_i|\le U_3:=S_1-S_2+S_3.} \tag{44}
$$

Hence $U_3<L$ certifies a safe class.

**Proof.** All periods divide $L$. A compatible class modulo their lcm has exactly $L/H_J$ lifts, proving (43). Pointwise, if a point belongs to $r$ sets, its contribution to the right side of (44) is
$r-\binom r2+\binom r3=1+\binom{r-1}{3}\ge1$ (with the binomial interpreted as zero for $r<4$). Summing proves (44). □

## Finite obstruction to low-order certificates — **DISPROVED**

Neither optimized pairwise trees nor the third Bonferroni truncation universally certify even the tested safe grids. For $V=(1,2,3,5)$, $L=75$, the exact union has six safe classes, but $U_T=77\ge75$; the third-order bound succeeds with $U_3=74$. More sharply, for

$$
 \boxed{V=(1,3,4,5),\quad L=100,}
$$

the exact safe classes include $24,25,35,36$, while

$$
 U_T=108,\qquad U_3=103.
$$

Thus the statements “the optimized tree bound always proves (41)” and “the third Bonferroni bound always proves (41)” are **DISPROVED**. This does not disprove (41).

## Computational audit — **VERIFIED**

Among all 2,432 gcd-one subsets of $\{1,\ldots,12\}$ for which $W$ is covered, the optimized tree certifies 196 and the third Bonferroni bound certifies 685; every canonical two-label grid nevertheless has a safe class. A separate seeded sample checked 324 admissible configurations with velocities at most 40 and found no covered grid. Exact tests compare all implemented pair/triple intersections and both upper bounds with direct sets on 64 random inputs. These finite results are not promoted to a theorem.

## TASK 16 outcome and narrow barrier

Assertion (41) remains **OPEN**. TASK 16 proves the best bound in the tree class and a rigorously signed higher-order extension, then supplies the smallest failures in the audited ordering. Full inclusion-exclusion would merely compute the already finite union and offers no uniform argument.

The narrow missing statement is now an interval-sensitive intersection theorem: exploit that every $A_i$ is the inverse image of one centered modular arc, rather than an arbitrary periodic set, to bound the uncovered complement after the third-order estimate fails. Any such theorem must distinguish $(1,3,4,5)$ from a genuine cover and cannot depend only on $S_1,S_2,S_3$ through (44).

---

# TASK 17 audit: scaling and interval-sensitive components

## Theorem 35 (common scaling is exactly neutral) — **PROVED**

For every positive integer $c$,

$$
 V=(v_1,\ldots,v_N)\text{ satisfies LRC}
 \iff cV=(cv_1,\ldots,cv_N)\text{ satisfies LRC}. \tag{45}
$$

More precisely, $t$ for $V$ corresponds to $t/c$ for $cV$. If $W'=cW$, then

$$
 b_i'={W'\over cv_i}=b_i,
$$

so every primitive bad period $qb_i$, every centered arc, and every normalized lattice problem is unchanged. In the unnormalized residue circle $qW'=cqW$, all blocks are merely repeated $c$ times. The absolute number of integer representatives grows by $c$, but their density and the existence of a safe class do not change.

This statement needs a careful distinction concerning “resolution.”  The two
sets of **time coordinates**

$$
 \left\{{x\over qW}:0\le x<qW\right\},\qquad
 \left\{{x\over qcW}:0\le x<qcW\right\}              \tag{45a}
$$

are not equal; the second really has $c$ times as many real numbers.  What is
unchanged is their image in runner phase space.  At the $x$th point of the
second grid,

$$
 \left({x\over qcW}cv_i\pmod1\right)_{i=1}^N
 =\left({xv_i\over qW}\pmod1\right)_{i=1}^N.          \tag{45b}
$$

The right side has period $qW$ in $x$ when $V$ is gcd-normalized.  Hence, as
$0\le x<cqW$, every old phase vector occurs exactly $c$ times; no intermediate
phase vector is added.  Thus it would be inaccurate to say that the raw set
of time points is unchanged.  The correct assertion is that the set of
**simultaneous runner positions**, and therefore safe-point existence, is
unchanged.

For example, for $V=(1,3)$ one has $qW=9$. Scaling by $2$ produces the 18
time coordinates $x/18$, but the positions of the scaled runners $(2,6)$ are

$$
 (2x/18,6x/18)=(x/9,x/3)\pmod1.
$$

The entries for $x=9,\ldots,17$ repeat those for $x=0,\ldots,8$. By contrast,
refining the denominator while **not** scaling the velocities would indeed
insert new phase vectors; that is a different operation from common scaling.

**Proof.** The identity $\|(t/c)(cv_i)\|=\|tv_i\|$ proves (45) including the exact threshold. The displayed equality of the $b_i$ proves invariance of the finite periods.  Equation (45b) proves the stronger phase-image statement directly.  Finally,
$\operatorname{lcm}_i(qb_i)=q\operatorname{lcm}_i(W/v_i)=qW$ because
$\gcd_i(v_i)=1$, so this phase word has precisely the asserted common period.
Equivalently, gcd normalization sends $cV$ back to $V$. □

The same distinction applies to the canonical two-direction grid.  Its raw
ambient length changes from $L=qW/d$ to $cL$, while $b_i$ and $d$ do not
change.  Membership is periodic with period $L$, and the change of base point
from $W$ to $cW$ translates the $z$-word by $(c-1)W/d$ (an integer because
$d\mid W$).  The enlarged canonical grid therefore consists of $c$ translated
copies of the original membership word, not a finer phase-space sampling.

Thus multiplying all velocities to “create more lattice points” cannot strengthen the attack: it creates $c$ copies of the same quotient information. Multiplying only selected velocities is not this invariance; it changes the LRC instance and needs a separate reduction, which is presently unavailable.

## Proposition 35a (refining time with fixed velocities) — **PROVED**

There is a different operation that does create new phase vectors: keep $V$
fixed and refine the finite time mesh to

$$
 G_c=\left\{{x\over cqW}:0\le x<cqW\right\}.          \tag{45c}
$$

Nevertheless, for every positive integer $c$,

$$
 \boxed{G_c\text{ contains an LRC-safe time}
 \iff G_1\text{ contains an LRC-safe time}.}           \tag{45d}
$$

**Proof.** Since $G_1\subseteq G_c$ via $x/(qW)=(cx)/(cqW)$, the reverse-to-
forward implication is immediate. Conversely, a safe point of $G_c$ is a
safe real time. For fixed $i$, the feasible set
$\{t:\|tv_i\|\ge1/q\}$ is closed and has endpoints

$$
 {qk+1\over qv_i},\qquad {qk+q-1\over qv_i}.
$$

Because $v_i\mid W$, all these endpoints lie in $G_1$. The common feasible
set is a finite union of closed intervals and isolated points whose endpoints
come from those individual endpoint sets. If it is nonempty, it therefore
contains a point of $G_1$ (and if it is the whole circle, any point of $G_1$
does). Thus a safe refined-grid point cannot be the first existential witness
missed by $G_1$. □

So time refinement may still be useful as an **analytic or computational
device**: it can sample the interiors of safe/bad components, approximate
their measures, or provide averaged inequalities. It gives no stronger
existence statement, because the endpoint grid $G_1$ is already complete.
Likewise, the continuous reparametrization $t\mapsto ct$ is surjective on
$\mathbb R/\mathbb Z$ and by itself cannot change existence. Any proposed
benefit from a finer mesh must therefore be quantitative (for example, a
uniform margin or measure bound), not merely “a new point appeared.”

## Theorem 35b (quantitative margin approximation) — **PROVED**

This is precisely where time refinement can help. Define the LRC margin

$$
 \mu_V(t)=\min_i\|tv_i\|-{1\over q},qquad
 \Delta(V)=\max_{t\in\mathbb R/\mathbb Z}\mu_V(t),      \tag{45e}
$$

and let $\Delta_c(V)=\max_{t\in G_c}\mu_V(t)$. If
$v_{\max}=\max_i v_i$, then

$$
 \boxed{\Delta(V)-{v_{\max}\over2cqW}
 \le\Delta_c(V)\le\Delta(V).}                         \tag{45f}
$$

Consequently, a positive value computed on any refined grid is a rigorous
positive-margin LRC certificate. Conversely, if $\Delta(V)=\delta>0$, every
integer

$$
 c>{v_{\max}\over2qW\delta}                            \tag{45g}
$$

guarantees $\Delta_c(V)>0$.

**Proof.** Distance to the nearest integer is 1-Lipschitz on the circle, so
$t\mapsto\|tv_i\|$ is $v_i$-Lipschitz and their pointwise minimum is
$v_{\max}$-Lipschitz. Choose a maximizer $t_*$, which exists by compactness,
and a nearest point $s\in G_c$. Its circular distance from $t_*$ is at most
$1/(2cqW)$. Hence
$\mu_V(s)\ge\mu_V(t_*)-v_{\max}/(2cqW)$, proving the lower bound. The upper
bound follows from $G_c\subset\mathbb R/\mathbb Z$, and (45g) makes the lower
bound positive. □

This yields a valid research route: seek a uniform or structure-dependent
lower bound for $\Delta(V)$, then choose a certified finite resolution using
(45g). There is, however, a sharp obstruction to a universally **positive**
margin theorem. For $V=(1,2)$, $q=3$, one has

$$
 \max_t\min(\|t\|,\|2t\|)=1/3,qquad\Delta(1,2)=0.     \tag{45h}
$$

Indeed, on $[0,1/2]$, the first distance is $t$, while the second is
$\min(2t,1-2t)$; their minimum is at most $1/3$, with equality at $t=1/3$.
Thus a margin strategy for all configurations must allow the equality case
and either classify zero-margin extremizers or prove a dichotomy
$\Delta(V)>0$ versus an explicitly solvable rigid family. A claim of a
universal bound $\Delta(V)\ge\delta_N>0$ is already **DISPROVED** for $N=2$.

## Corollary 35c (refinement never makes the $(1,2)$ margin positive) —
**PROVED**

For $V=(1,2)$ one has $W=2$, $q=3$, and for every integer $c\ge1$,

$$
 \boxed{\Delta_c(1,2)=0.}                              \tag{45i}
$$

In particular, arbitrarily fine grids do not merely fail to guarantee a
positive margin eventually: this fixed configuration has exactly zero best
margin at **every** refinement.

**Proof.** By symmetry it suffices to take $0\le t\le1/2$. For
$0\le t\le1/4$,

$$
 \min(\|t\|,\|2t\|)=\min(t,2t)=t\le1/4.
$$

For $1/4\le t\le1/2$ it equals $\min(t,1-2t)$, whose maximum is attained when
$t=1-2t$, namely at $t=1/3$, with value $1/3$. Hence
$\mu_{(1,2)}(t)\le0$ for every real $t$. On the other hand,

$$
 {1\over3}={2c\over6c}\in G_c
$$

because $cqW=6c$, and its margin is zero. Therefore
$0\le\Delta_c(1,2)\le0$. □

This also clarifies the role of the approximation error in (45f). That error
is an upper bound on how much a grid can miss a **pre-existing positive**
continuous margin; it is not a mechanism that creates margin. Refinement can
make $\Delta_c(V)$ approach $\Delta(V)$ from below, but it can never exceed
$\Delta(V)$. Thus no choice of $c$ can turn a zero-margin configuration into
a positive-margin one.

## Theorem 36 (exact cyclic-component recursion) — **PROVED**

For $C\subseteq\mathbb Z/L\mathbb Z$, define its canonical components by their starts

$$
 \partial^-C=\{z\in C:z-1\notin C\} \tag{46}
$$

and, for each start $s$, the unique maximal length $\lambda_s$ such that
$s,s+1,\ldots,s+\lambda_s-1\in C$. The empty and full-circle cases are treated separately. These pairs $(s,\lambda_s)$ uniquely and disjointly encode $C$.

Choose two labelled strips $B_i,B_j$ and initialize

$$
 C_2=(\mathbb Z/L\mathbb Z)\setminus(B_i\cup B_j). \tag{47}
$$

After adding runner $r$, the exact update is

$$
 C_{m+1}=C_m\setminus B_r,\qquad
 \partial^-C_{m+1}=\{z\in C_m:z\notin B_r, z-1\notin C_m\setminus B_r\}. \tag{48}
$$

On a component $(s,\lambda_s)$ its surviving endpoints are therefore exactly the transitions of

$$
 1_{C_m}(s+a)\bigl(1-1_{A_r}((s+a)\bmod H_r)\bigr),\quad 0\le a<\lambda_s. \tag{49}
$$

Equations (37) and (49) are the requested endpoint formula: the second factor is not arbitrary, but the inverse image of the single centered arc
$zd\equiv-W+[-(b_r-1),b_r-1]\pmod{qb_r}$.

**Proof.** Every nonempty proper cyclic subset has a unique predecessor gap before each maximal consecutive run, proving (46). Set subtraction gives (48), and restricting its indicator to a run gives (49). Induction retains every runner label and ends with exactly the safe set. □

This is an exact M-free decision procedure on $L=q\operatorname{lcm}(v_*,v^\dagger)$, not by itself a uniform LRC proof. A crucial obstruction is that multiplication by the unit induced by $d$ can permute a centered arc into many separated positions in the $z$ ordering; ordinary interval connectedness is not preserved by the quotient parametrization.

## Proposition 37 (three intersection moments cannot decide arc coverage) — **DISPROVED criterion**

Even for four genuine centered cyclic arcs, $(S_1,S_2,S_3)$ does not determine coverage. On $\mathbb Z/8\mathbb Z$, consider

$$
 \begin{aligned}
 \mathcal C&=(\{0\},\{5,6,7,0,1,2,3\},\{5,6,7\},\{4,5,6,7,0\}),\\
 \mathcal U&=(\{0\},\{0,1,2\},\{4,5,6,7,0\},\{4,5,6,7,0,1,2\}).
 \end{aligned} \tag{50}
$$

Both have

$$
 (S_1,S_2,S_3)=(16,12,4), \tag{51}
$$

but $\bigcup\mathcal C=\mathbb Z/8\mathbb Z$, whereas $3\notin\bigcup\mathcal U$.

**Proof.** Every displayed set is a centered cyclic arc (with the displayed center and radius respectively $(0,0),(0,3),(6,1),(6,2)$ and $(0,0),(1,1),(6,2),(7,3)$). Direct finite intersection counting gives (51), and the two union assertions are visible from (50). This is a complete finite proof, not sampling. □

Therefore no theorem depending only on the first three aggregate intersection moments can settle coverage, even before the extra LRC arithmetic constraints are imposed.

## Computational audit — **VERIFIED**

The component recursion reproduces the four safe classes $24,25,35,36$ for $(1,3,4,5)$ and nonempty safe components for all 19 TASK 14 obstructions. Independent tests compare its expanded output with direct safe classes and verify common-scale invariance on 53 seeded admissible configurations. The exact arc pair (50) is stored and rechecked computationally. These checks support the implementation; Theorems 35–37 have independent proofs.

## TASK 17 outcome and narrow barrier

The suggested common-scaling mechanism is conclusively neutral, while the component recursion supplies an exact interval-sensitive algorithm. Proposition 37 shows why the first three aggregate moments cannot be upgraded into a universal criterion. The canonical two-label assertion and LRC remain **OPEN**.

The narrow next barrier is to control the ordering produced by the modular multiplier in (49) using the special divisibility relations $b_i=W/v_i$. One needs either a uniform bound on the fragmentation of the surviving components that forces a gap, or an exact covered canonical grid. Arbitrary cyclic-arc inequalities are now known to be insufficient unless they retain this labelled multiplier/divisor information.

---

# TASK 18 audit: modular-multiplier fragmentation

## Theorem 38 (reduced labelled multiplier) — **PROVED**

Retain the canonical grid $x=W+zd$ of (35). For runner $i$ set

$$
 m_i=qb_i,\qquad g_i=\gcd(d,m_i),qquad H_i=m_i/g_i,qquad
 a_i=d/g_i. \tag{52}
$$

Then $\gcd(a_i,H_i)=1$, and with

$$
 \rho_i=\left\lfloor{b_i-1\over g_i}\right\rfloor,qquad
 c_i=-{W\over g_i}a_i^{-1}\pmod {H_i}, \tag{53}
$$

the bad strip is exactly the modular arithmetic progression

$$
 \boxed{A_i=\{c_i+a_i^{-1}y\pmod {H_i}:-\rho_i\le y\le\rho_i\}.} \tag{54}
$$

Its cardinality is $s_i=\min(H_i,2\rho_i+1)$. Thus the relevant permutation multiplier is $a_i^{-1}\pmod {H_i}$; its multiplicative order and the Euclidean continued fraction of $a_i/H_i$ are exact finite invariants of the labelled strip.

**Proof.** The congruence $dz\equiv-W+u\pmod {m_i}$ is soluble exactly when $g_i\mid u$, because $g_i\mid W$. Write $u=g_iy$ and divide by $g_i$. The resulting coefficient $a_i$ is a unit modulo $H_i$ by the definition of the gcd. Its inverse gives (54), while the allowed integral values of $y$ give (53) and the cardinality. □

Unlike a generic unit model, every quantity in (52)–(54) is constrained by

$$
 d={W\over\operatorname{lcm}(v_*,v^\dagger)},qquad b_i={W\over v_i}. \tag{55}
$$

This is the exact divisor information that must be retained in any structural estimate.

## Theorem 39 (exact fragmentation formula) — **PROVED**

Assume $0<s_i<H_i$, and let $r_i$ be the least residue of $a_i$ in $\{1,\ldots,H_i-1\}$. The number $\kappa_i$ of ordinary consecutive cyclic components of $A_i$ in the $z$ ordering is

$$
 \boxed{\kappa_i=s_i-\max(0,s_i-r_i)-\max(0,s_i-(H_i-r_i)).} \tag{56}
$$

In particular

$$
 1\le\kappa_i\le\min(s_i,H_i-s_i). \tag{57}
$$

The empty and full cases have respectively zero and one component.

**Proof.** Under (54), two bad $z$-classes are consecutive exactly when their arc coordinates differ by $a_i$ modulo $H_i$. A cyclic interval of length $s_i$ overlaps its translate by $r_i$ in

$$
 E_i=\max(0,s_i-r_i)+\max(0,s_i-(H_i-r_i))
$$

points. These are precisely the directed adjacency edges $z\to z+1$ inside $A_i$. A proper subset of a cycle is a disjoint union of paths, so vertices minus internal edges equals its number of components, proving (56). The first bound in (57) is immediate. Applying the same transition count to the complement shows that a proper cyclic binary word has equally many one-runs and zero-runs, whence $\kappa_i\le H_i-s_i$; also $\kappa_i\le s_i$. □

Formula (56) is stronger than a generic component bound: after substitution from (52), it computes fragmentation directly from $W/v_i$, the canonical lcm direction, and their gcd. However, summing the individual $\kappa_i$ and $s_i$ does not presently control how components of different labels align.

## Computational audit — **VERIFIED**

The implementation computes $a_i$, $a_i^{-1}$, its multiplicative order, the Euclidean continued fraction of $a_i/H_i$, and both sides of (56) using integer arithmetic. Independent tests verify (54)–(56) on 116 admissible inputs, including $(1,3,4,5)$, the smallest TASK 14 obstruction, powers of two with $q$-divisible member, consecutive and odd examples when they meet the central-cover hypothesis, translated examples, and seeded random configurations. Consecutive families not containing a multiple of $q=N+1$ are explicitly outside the hypotheses of this central-grid construction, rather than failed tests.

All 19 TASK 14 obstructions again have safe canonical grids. A seeded adversarial audit checks 434 admissible configurations with velocities at most 50 and finds no covered grid. This is `VERIFIED` only; it proves neither universal grid success nor LRC.

## TASK 18 outcome and narrow barrier

TASK 18 completely determines single-strip fragmentation. The hoped-for conclusion “individual fragmentation plus total strip length forces a surviving gap” remains **OPEN**, because (56) contains no cross-label phase/alignment information. No covered canonical grid was found, so there is no counterexample to certify.

The narrow new problem is pairwise fragmentation alignment: derive an exact or useful bound for transitions shared by two progressions (54), using the gcd relations among $(a_i,H_i)$ and $(a_j,H_j)$. This is strictly finer than intersection cardinality and strictly finer than treating the strips as arbitrary arcs.

---

# TASK 19 audit: pairwise fragmentation alignment

## Theorem 40 (local transition classes) — **PROVED**

Let $I_i=[-\rho_i,\rho_i]\subseteq\mathbb Z/H_i\mathbb Z$ be the centered arc from (54), and define

$$
 y_i(z)=a_i z+{W\over g_i}\pmod {H_i}. \tag{58}
$$

For $(\epsilon,\eta)\in\{0,1\}^2$, the exact local transition class is

$$
 \boxed{T_i^{\epsilon\eta}=\{z\bmod H_i:
 1_{I_i}(y_i(z))=\epsilon,
 1_{I_i}(y_i(z)+a_i)=\eta\}.} \tag{59}
$$

The four classes partition $\mathbb Z/H_i\mathbb Z$. In particular,
$T_i^{01}$ and $T_i^{10}$ are respectively the entry and exit boundaries of
the fragmented bad strip in the canonical $z$ ordering.

**Proof.** By the divided congruence in Theorem 38, $z\in A_i$ exactly when
$y_i(z)\in I_i$. Replacing $z$ by $z+1$ adds $a_i$ to $y_i$, proving (59).
The four possible pairs of indicator values are disjoint and exhaustive. □

## Theorem 41 (exact labelled joint-transition table) — **PROVED**

For two labels $i,j$, put $G_{ij}=\gcd(H_i,H_j)$ and
$H_{ij}=\operatorname{lcm}(H_i,H_j)$. For states
$s,t\in\{0,1\}^2$, the number of $z\bmod L$ having transition $s$ for
runner $i$ and transition $t$ for runner $j$ is

$$
 \boxed{Q_{ij}(s,t)={L\over H_{ij}}
 \#\{(u,v)\in T_i^s\times T_j^t:u\equiv v\pmod {G_{ij}}\}.} \tag{60}
$$

Thus the complete $4\times4$ table is computable from centered-arc endpoints,
the reduced multipliers, and one pairwise gcd. It strictly refines ordinary
intersection cardinality: for example
$|B_i\cap B_j|=\sum_{s_0=t_0=1}Q_{ij}(s,t)$, while the other cells retain
entry/exit alignment.

**Proof.** The simultaneous residue conditions $z\equiv u\pmod {H_i}$ and
$z\equiv v\pmod {H_j}$ are compatible precisely under the congruence modulo
$G_{ij}$. Each compatible pair has $L/H_{ij}$ lifts because both periods
divide $L$. Summation proves (60). □

## Corollary 42 (two-strip safe-component count) — **PROVED**

If the complement of $B_i\cup B_j$ is neither empty nor the whole circle, its
number of cyclic components is

$$
 \boxed{K_{ij}=\sum_{\substack{s_0\lor t_0=1\\s_1=t_1=0}}Q_{ij}(s,t).} \tag{61}
$$

The empty and full cases have zero and one component respectively.

**Proof.** A safe component starts at $z+1$ exactly when at least one runner is
bad at $z$ and both are safe at $z+1$. These are precisely the cells summed
in (61). □

This gives exact pairwise fragmentation alignment, not merely a bound. It can
be evaluated by histograms modulo $G_{ij}$ without scanning $qW$.

## Proposition 43 (aggregate pair-transition summaries do not decide coverage) — **DISPROVED criterion**

Even centered arcs with the same aggregate single-label transition counts and
the same aggregate $4\times4$ pair-transition table can have different
coverage. On $\mathbb Z/8\mathbb Z$ take

$$
 \begin{aligned}
 \mathcal U&=(\{0\},\{1\},\{5,6,7\},\{0,1,2,4,5,6,7\}),\\
 \mathcal C&=(\{0\},\{3\},\{2,3,4\},\{1,2,3,4,5,6,7\}).
 \end{aligned} \tag{62}
$$

Both aggregate individual tables, in state order $00,01,10,11$, equal

$$
 (16,4,4,8), \tag{63}
$$

and summing $Q_{ij}(s,t)$ over all six unordered label pairs gives the same
$4\times4$ table for both systems. Nevertheless
$|\bigcup\mathcal U|=7$ and $|\bigcup\mathcal C|=8$.

**Proof.** The four sets in each row of (62) are centered cyclic arcs, with
center-radius data $(0,0),(1,0),(6,1),(7,3)$ and
$(0,0),(3,0),(3,1),(4,3)$. Direct enumeration of the eight possible starts
gives (63), the common pair table stored in `task19_results.json`, and the
displayed union sizes. This is a finite exhaustive proof. □

Proposition 43 concerns **aggregate** pair-transition data. It does not show
that the complete collection of labelled tables $Q_{ij}$ is insufficient;
that stronger question remains open and must not be silently inferred.

## Computational audit — **VERIFIED**

Independent direct-period and gcd-histogram implementations of (60) agree on
106 seeded admissible configurations. Formula (61) agrees with direct cyclic
component decomposition for up to six pairs per input. The audit records all
pairs for $(1,3,4,5)$ and all 19 TASK 14 obstructions, and exactly reproduces
the two systems (62). Required standard families are covered through the
TASK 18 suite whenever the central-cover hypothesis applies; TASK 19 adds no
claim outside that hypothesis.

## TASK 19 outcome and narrow barrier

Pairwise transition alignment is now exact, and is strictly richer than the
intersection counts of TASK 16. Aggregate transition statistics still fail to
decide coverage. No theorem currently converts all labelled tables $Q_{ij}$
into a forced global gap, and no covered canonical two-label grid is known.

The narrow next problem is whether the **complete labelled** pair-transition
tables, together with the divisor-compatible phases (58), control triple gap
destruction. This requires either a reconstruction/inequality theorem or two
valid LRC-derived strip systems with identical labelled pair data and different
coverage. Arbitrary relabelling or aggregation is no longer sufficient.

---

# TASK 20 audit: labelled triple transitions

## Theorem 44 (exact eight-state transition table) — **PROVED**

For three distinct labels $i,j,k$, let a global before-state and after-state be

$$
 u=(u_i,u_j,u_k),\qquad v=(v_i,v_j,v_k)\in\{0,1\}^3. \tag{64}
$$

Thus there are eight states at each endpoint and an $8\times8$ transition
table. Put $H_{ijk}=\operatorname{lcm}(H_i,H_j,H_k)$. Its exact entry is

$$
 \boxed{R_{ijk}(u,v)={L\over H_{ijk}}\#\left\{
 (r_i,r_j,r_k)\in T_i^{u_iv_i}\times T_j^{u_jv_j}\times T_k^{u_kv_k}:
 r_p\equiv r_q\pmod{\gcd(H_p,H_q)}\ \forall p,q
 \right\}.} \tag{65}
$$

**Proof.** The generalized CRT for three congruences is soluble exactly when
every pair is compatible modulo the gcd of its moduli. Every compatible triple
then determines one class modulo $H_{ijk}$ and hence $L/H_{ijk}$ classes
modulo $L$. The transition restrictions are exactly those defining the three
local sets $T_p^{u_pv_p}$. □

Formula (65) retains all 64 before/after cells; calling it merely an
“eight-state count” must not collapse the two endpoints.

## Theorem 45 (exact triple gap-destruction identity) — **PROVED**

Let $0=(0,0,0)$. If the set safe for all three labels is a nonempty proper
subset of the cyclic grid, its component count is

$$
 \boxed{K_{ijk}=\sum_{u\ne0}R_{ijk}(u,0).} \tag{66}
$$

Consequently, outside the separately handled empty/full cases, inserting
runner $k$ after the pair $(i,j)$ changes the number of surviving components
by the exact signed quantity

$$
 \boxed{\Delta K=\sum_{u\ne0}R_{ijk}(u,0)-K_{ij}.} \tag{67}
$$

This identity includes both destruction of whole pairwise gaps and splitting
of a pairwise gap into several smaller gaps.

**Proof.** A safe component starts at $z+1$ precisely when the before-state is
not all-safe and the after-state is all-safe. Summing exactly those cells gives
(66). Subtract Corollary 42 to obtain (67). □

## Proposition 46 (phase data reconstructs the full system) — **PROVED / limitation identified**

The complete labelled phase records

$$
 (H_i,a_i,c_i,\rho_i)_{i=1}^N \tag{68}
$$

already determine every bad set by (54), hence determine their union, every
higher transition table, and coverage exactly. Therefore the complete labelled
pair tables together with (68) do control triple gap destruction—constructively
through (59) and (65).

**Proof.** Substitute each record into (54) to reconstruct $A_i$, lift it to
$L$, and apply set union or (65). No choices remain. □

This resolves a logical ambiguity in TASK 20. It is impossible to produce two
systems with identical records (68) but different coverage: they are the same
labelled subsets. On the other hand, reconstruction is an exact finite
algorithm, not a uniform inequality proving that the reconstructed union is
proper. Complete labelled pair tables *without* (68) may still lose higher
correlations; no claim of sufficiency is made for that reduced data.

## Computational audit — **VERIFIED**

An implementation of (65) over $H_{ijk}$ is independently compared with a
direct scan over the canonical period $L$, never $qW$. All 64 cells agree on
92 admissible inputs: 87 seeded cases plus the critical configuration, a
TASK 14 obstruction, powers of two, odd integers, and a consecutive/translated
interval satisfying the central-cover hypothesis. Formulae (66)–(67) agree
with direct cyclic-component decomposition.

For $(1,3,4,5)$ the four triples have component changes $1,0,0,0$ and none
covers the grid. Across all 19 TASK 14 obstructions, no three-label subset
covers its canonical grid; observed component changes range from $0$ to $14$.
These are finite `VERIFIED` statements, not universal bounds.

## TASK 20 outcome and narrow barrier

Triple gap destruction is now exactly dualized by generalized CRT. The phase
records trivially-but-rigorously reconstruct all higher data, while no
nontrivial inequality extracted from pair tables is known to force a gap.
Neither a covered canonical grid nor an LRC-derived collision of reduced
labelled pair summaries was found. Universal canonical-grid success and LRC
remain **OPEN**.

The narrow next task is no longer another exact table. It is to compress (65)
without losing the sign relevant to $R_{ijk}(u,0)$: prove a quantitative bound
on triple all-safe entries from the divisor-compatible centered arcs, or find
a concrete canonical grid where all-safe mass vanishes.

---

# TASK 21 audit: quantitative triple all-safe mass

## Theorem 47 (complements of three centered multiplier arcs) — **PROVED**

For three labels $i,j,k$, write

$$
 I_p=[-\rho_p,\rho_p]\pmod {H_p},\qquad
 y_p(z)=a_p(z-c_p)\pmod {H_p}.                         \tag{69}
$$

The all-safe set on the canonical cyclic grid $\mathbb Z/L\mathbb Z$ is
exactly

$$
 \boxed{S_{ijk}=\bigcap_{p\in\{i,j,k\}}
 \{z:y_p(z)\notin I_p\}.}                             \tag{70}
$$

If $s_p=\min(H_p,2\rho_p+1)$ and $J_{pq}=|A_p\cap A_q|$, then

$$
 |S_{ijk}|=L-L\sum_p{s_p\over H_p}
              +J_{ij}+J_{ik}+J_{jk}-J_{ijk},           \tag{71}
$$

where every intersection is given by the pairwise-compatible generalized
CRT conditions in (65). In particular the following bounds require no
triple-cell enumeration:

$$
 \boxed{|S_{ijk}|\ge
 \max\left(0,L-L\sum_p{s_p\over H_p}\right),}          \tag{72}
$$

and

$$
 \boxed{|S_{ijk}|\ge\max\left(0,L-L\sum_p{s_p\over H_p}
 +\sum_{p<r}J_{pr}-\min_{p<r}J_{pr}\right).}           \tag{73}
$$

**Proof.** Theorem 38 says $z\in A_p$ exactly when $y_p(z)\in I_p$;
taking three complements proves (70). Inclusion--exclusion proves (71).
The union bound gives (72). For (73), note that
$J_{ijk}\le\min(J_{ij},J_{ik},J_{jk})$ in (71). All lifts use the lcm
period because $H_p\mid L$; $qW$ is not involved. □

Formula (71) is exact enumeration rewritten. Bounds (72)--(73), by contrast,
are uniform inequalities: (72) uses only one-strip masses and (73) only
one- and two-strip masses.

## Corollary 48 (a divisor-aligned positive range) — **PROVED**

Suppose $g_p=\gcd(d,qb_p)$ divides $b_p$ for each of three selected labels.
Then

$$
 {s_p\over H_p}={2(b_p/g_p)-1\over q(b_p/g_p)}<{2\over q}. \tag{74}
$$

Consequently, if $q\ge7$,

$$
 \boxed{|S_{ijk}|>L(1-6/q)\ge L/7>0.}                 \tag{75}
$$

**Proof.** Put $B_p=b_p/g_p\in\mathbb Z_{>0}$. Equations (52)--(53) give
$H_p=qB_p$ and $\rho_p=B_p-1$, hence $s_p=2B_p-1<H_p$ and (74). Sum the
three strict inequalities in (72). □

The divisibility assumption in Corollary 48 is substantive. It is checked,
not presumed, by the implementation; no proof that it holds for every label
of every canonical construction is claimed. Thus (75) is not silently
promoted to an unconditional canonical-grid theorem. For $q\le6$, even three
densities below $2/q$ do not give a positive union bound, although (73) can.

## Why triple mass alone does not control all runners — **PROVED limitation**

Let $T=\{i,j,k\}$ and define on $S_T$ the multiplicity of the remaining bad
strips by

$$
 m_T(z)=\sum_{r\notin T}1_{A_r}(z).                    \tag{76}
$$

The precise extra first-moment hypothesis sufficient to lift a triple gap to
a global gap is

$$
 \boxed{\sum_{z\in S_T}m_T(z)<|S_T|,}                 \tag{77}
$$

equivalently $\sum_{r\notin T}|A_r\cap S_T|<|S_T|$.
Indeed, (77) forces some $z\in S_T$ to have $m_T(z)=0$. Without a restriction
of this kind, positive triple mass alone says nothing: arbitrary additional
sets can cover all of $S_T$. Condition (77) is sufficient rather than claimed
necessary; the exact necessary-and-sufficient condition is
$\min_{z\in S_T}m_T(z)=0$.

## Computational audit — **VERIFIED**

`test_triple_safe.py` independently compares (71) with direct membership and
checks (72)--(75) on 263 triples. The deterministic adversarial audit uses
only $L=q\operatorname{lcm}(v_*,v^\dagger)$, never $qW$. It checks
$(1,3,4,5)$, all 19 TASK 14 obstructions, the applicable powers-of-two, odd,
consecutive and translated families in the unit test, and every defined
canonical construction from gcd-one subsets of $\{1,\ldots,10\}$ of sizes
three through six. Among 442 exhaustive configurations and the 20 required
records, no zero all-safe triple occurs. The smallest observed normalized
triple-safe mass is $1/14$. These are finite verifications, not a proof of
universal positivity.

## TASK 21 outcome and narrow barrier

Triple all-safe mass now has two genuine lower bounds, and the
divisor-aligned range $q\ge7$ forces a surviving triple gap. This still does
not prevent the other $N-3$ runners from covering that gap. The narrow next
problem is to bound the restricted incidences in (77), exploiting the same
divisor-compatible phases rather than replacing them by arbitrary subsets.

---

# TASK 22 audit: restricted incidence on a triple-safe set

## Theorem 49 (four-label CRT formula) — **PROVED**

Fix a triple $T=\{i,j,k\}$ and a label $r\notin T$. For every nonempty set of
labels $U$, let $J_U=|\bigcap_{u\in U}A_u|$, evaluated on the canonical period
$L$ by the pairwise gcd compatibility conditions of the generalized CRT.
Then

$$
 \boxed{|A_r\cap S_T|=J_{\{r\}}-
 \sum_{p\in T}J_{\{r,p\}}+
 \sum_{\{p,s\}\subset T}J_{\{r,p,s\}}-J_{\{r,i,j,k\}}.} \tag{78}
$$

In particular, the left side of (77) is an exact sum of labelled CRT terms of
order at most four and can be computed modulo the lcm of the participating
$H$'s, never modulo $qW$.

**Proof.** Since $S_T=\bigcap_{p\in T}A_p^c$, multiply $1_{A_r}$ by
$\prod_{p\in T}(1-1_{A_p})$, expand, and sum over $z\bmod L$. Each resulting
intersection has the asserted generalized-CRT description by Theorem 44. □

This is an exact identity, not a uniform inequality. It exposes explicitly
that pair and triple data alone omit the final four-label term.

## Theorem 50 (exact averaging over all triples) — **PROVED**

Let $m(z)=\sum_{i=1}^N1_{A_i}(z)$. Summing over all labelled triples gives

$$
 \boxed{\sum_{|T|=3}|S_T|=
 \sum_{z\bmod L}{N-m(z)\choose3},}                    \tag{79}
$$

and

$$
 \boxed{\sum_{|T|=3}\sum_{r\notin T}|A_r\cap S_T|=
 \sum_{z\bmod L}m(z){N-m(z)\choose3}.}                \tag{80}
$$

Here ${h\choose3}=0$ for $h<3$, covering all endpoint cases. Hence averaging
forces at least one triple satisfying (77) whenever

$$
 \sum_z(m(z)-1){N-m(z)\choose3}<0.                    \tag{81}
$$

**Proof.** At a point of bad multiplicity $m$, precisely the
${N-m\choose3}$ triples chosen from its safe labels contain the point in
$S_T$. For each such triple all $m$ bad labels lie outside it, so the point is
counted $m{N-m\choose3}$ times on the left of (80). Summing pointwise proves
both identities and their difference proves the final assertion. □

This averaging is exact but does not by itself overcome coverage. If the full
system covers the grid, then $m(z)\ge1$ everywhere, so every summand in (81)
is nonnegative. A strict averaged inequality therefore already certifies an
uncovered point; it is not a new route to one without an independent
multiplicity estimate.

## Proposition 51 (largest-mass canonical triple) — **DISPROVED**

Consider the phase-blind canonical rule selecting the three labels with
largest lifted bad masses $L|A_i|/H_i$, breaking ties by input label order.
This rule does not always satisfy (77). The smallest failure in the stated
exhaustive audit is

$$
 V=(1,4,5,6,9),\qquad q=6,qquad L=108.               \tag{82}
$$

It selects $T=(1,4,5)$, for which

$$
 |S_T|=24,qquad |A_6\cap S_T|=12,qquad
 |A_9\cap S_T|=12.                                    \tag{83}
$$

Thus the two sides of (77) are equal, not strict. A compact reproducible CRT
certificate consists of the records $(v,H,a,c,\rho)$

$$
 (1,108,1,90,17),\ (4,27,1,9,4),\ (5,108,5,90,17),
 \ (6,18,1,0,2),\ (9,12,1,6,1).                       \tag{84}
$$

**Proof.** Substitution of (84) into (69), followed by (78), gives (83).
These are finite integer computations on $\mathbb Z/108\mathbb Z$ and are
independently checked by direct membership in `test_restricted_incidence.py`.
Equality disproves the proposed strict conclusion. □

This does not assert that (82) is an LRC counterexample, nor even that its
canonical grid is covered. It disproves only this explicitly stated selection
rule and first-moment certificate.

## Computational audit — **VERIFIED**

The exact formula (78) and direct membership agree in 63 test cases, including
all triples of $(1,3,4,5)$, the smallest TASK 14 obstruction, and applicable
powers-of-two, odd, consecutive, and translated families. Identities
(79)--(80) are checked independently. The deterministic audit covers all 20
required configurations and 442 gcd-one subsets of $\{1,\ldots,10\}$ of
sizes three through six with a defined canonical grid. The largest-mass rule
fails on 71 exhaustive inputs and succeeds strictly on only four of the 20
required inputs. These finite counts are **VERIFIED**, not universal claims.

## TASK 22 outcome and narrow barrier

Restricted incidence is now exactly reduced to four-label CRT data, while a
natural phase-blind canonical choice is disproved. All-triple averaging yields
the exact multiplicity weights but becomes nonnegative under hypothetical
coverage. The narrow unresolved issue is therefore not triple selection by
mass: it is whether the divisor-compatible phases force enough
multiplicity-zero or constrain the multiplicity surplus in (81).

---

# TASK 23 audit: phase-sensitive multiplicity surplus

## Theorem 52 (intersection polynomial for the surplus) — **PROVED**

For $0\le k\le4$ define the $k$th intersection moment

$$
 M_k=\sum_{\substack{U\subseteq\{1,\ldots,N\}\\|U|=k}}
 \left|\bigcap_{i\in U}A_i\right|,qquad M_0=L.        \tag{85}
$$

Put $C_h={N-h\choose3}$, with $C_h=0$ when $N-h<3$. Then the surplus in
TASK 23 has the exact expansion

$$
 \boxed{\Sigma=\sum_{k=0}^4\gamma_kM_k,}              \tag{86}
$$

where

$$
 \begin{aligned}
 \gamma_0&=-C_0,&\gamma_1&=C_0,\\
 \gamma_2&=C_2-C_0,&
 \gamma_3&=2C_3-3C_2+C_0,\\
 \gamma_4&=3C_4-8C_3+6C_2-C_0.
 \end{aligned}                                        \tag{87}
$$

Thus intersections of order at most four determine $\Sigma$ exactly; no
higher-order table is needed for this statistic.

**Proof.** For every integer $m$, Newton's finite-difference formula expands
$f(m)=(m-1){N-m\choose3}$ as
$\sum_{k=0}^4\Delta^kf(0){m\choose k}$. Its five finite differences are
exactly (87). Pointwise,
${m(z)\choose k}$ counts the $k$-subsets of bad labels at $z$, so
$\sum_z{m(z)\choose k}=M_k$. Summing the Newton expansion proves (86). □

## Corollary 53 (zero mass versus overlap surplus) — **PROVED**

Writing $h_j=|\{z:m(z)=j\}|$, one has

$$
 \boxed{\Sigma=-{N\choose3}h_0+
 \sum_{j=2}^{N-3}(j-1){N-j\choose3}h_j.}              \tag{88}
$$

Multiplicity one contributes exactly zero, multiplicities two through
$N-3$ contribute positively, and larger multiplicities have no safe triple
and hence zero weight. Therefore $\Sigma<0$ is precisely a quantitative
dominance of uncovered classes over the indicated overlap surplus.

**Proof.** Separate the $j=0,1$, $2\le j\le N-3$, and $j>N-3$ terms in the
defining histogram sum. Their signs and zero cases follow immediately. □

This explains the barrier in Theorem 50: even a grid with uncovered points
can have positive $\Sigma$ if overlap multiplicities are sufficiently large.

## Proposition 54 (divisor alignment does not make the surplus negative) —
**DISPROVED criterion**

The condition $g_i\mid b_i$ for every label does not imply $\Sigma<0$. Take

$$
 V=(1,2,3,4,5,7),\quad q=7,\quad L=245.               \tag{89}
$$

All six labels are divisor-aligned. Its exact multiplicity histogram is

$$
 (h_0,h_1,\ldots,h_6)=(6,136,80,6,4,4,9),            \tag{90}
$$

and (88) gives $\Sigma=212>0$. Compact phase records $(v,H,a,c,\rho)$ are

$$
\begin{aligned}
 &(1,245,1,210,34),(2,245,2,210,34),\\
 &(3,245,3,210,34),(4,245,4,210,34),\\
 &(5,49,1,14,6),(7,35,1,0,4).
\end{aligned}                                         \tag{91}
$$

**Proof.** Each corresponding reduced gcd is respectively
$12,6,4,3,12,12$, dividing $b_i=420,210,140,105,84,60$. Substitution of
(91) into (69) on $\mathbb Z/245\mathbb Z$ gives (90); (88) then gives 212.
The independent intersection calculation (86) gives the same integer. □

There are six uncovered classes in (90), so (89) is not an LRC
counterexample. It disproves only the proposed implication from divisor
alignment to negative surplus. In particular, negative surplus is too strong
to be a necessary signature of a successful canonical grid.

## Computational audit — **VERIFIED**

Histogram evaluation and the independent order-four intersection polynomial
agree on 35 inputs. The deterministic audit includes $(1,3,4,5)$, all TASK 14
obstructions, the TASK 22 certificate, and 387 gcd-one subsets of
$\{1,\ldots,10\}$ of sizes four through six with defined canonical grids.
Among these, 38 fully divisor-aligned systems have nonnegative surplus; (89)
is the first in lexicographic exhaustive order. Every computation uses $L$,
never $qW$.

## TASK 23 outcome and narrow barrier

The surplus is completely determined by intersections through order four,
and its multiplicity-zero/overlap decomposition is exact. Plain divisor
alignment cannot force its negativity. A useful next theorem must retain more
than alignment: it must control where low multiplicities occur, or use a
localized/weighted statistic that is not overwhelmed by harmless high-overlap
classes while still forcing $h_0>0$.

---

# TASK 24 audit: localized low-multiplicity certificate

## Theorem 55 (transition-fiber quadratic certificate) — **PROVED**

Choose an anchor label $a$ by largest lifted bad mass, breaking ties by label
order, before inspecting any safe point. Partition $\mathbb Z/L\mathbb Z$
into the four labelled transition fibers

$$
 E_{\epsilon\eta}=\{z:(1_{A_a}(z),1_{A_a}(z+1))
 = (\epsilon,\eta)\},\qquad(\epsilon,\eta)\in\{0,1\}^2. \tag{92}
$$

For any such fiber define

$$
 \boxed{Q(E)=\sum_{z\in E}(1-m(z))(N-m(z)).}           \tag{93}
$$

Then

$$
 \boxed{Q(E)>0\Longrightarrow E\text{ contains a class with }m(z)=0.} \tag{94}
$$

Moreover, with localized moments

$$
 M_1(E)=\sum_i|E\cap A_i|,qquad
 M_2(E)=\sum_{i<j}|E\cap A_i\cap A_j|,
$$

one has the bounded-order formula

$$
 \boxed{Q(E)=N|E|-N M_1(E)+2M_2(E).}                  \tag{95}
$$

After expanding the two anchor conditions defining $E$, (95) uses labelled
shifted-arc CRT intersections of order at most four.

**Proof.** The polynomial $(1-m)(N-m)$ equals $N$ at $m=0$, vanishes at
$m=1,N$, and is negative for $2\le m\le N-1$. Therefore a positive sum
requires a multiplicity-zero point, proving (94). Since
$m^2=m+2{m\choose2}$, pointwise expansion gives
$(1-m)(N-m)=N-Nm+2{m\choose2}$, which sums to (95). Each transition fiber is
an intersection of either an anchor arc or its complement at $z$ and at
$z+1$. Expanding the complements and then the terms of $M_2(E)$ introduces
at most two additional bad arcs, hence at most four simultaneous shifted-arc
congruences. Generalized CRT applies exactly as in Theorem 44. □

The weight in (93) completely suppresses multiplicities one and $N$, rather
than giving every overlap a positive contribution as (88) can. This is a
rigorous sufficient certificate, not a necessary condition for safety.

## Proposition 56 (four transition fibers are too coarse) — **DISPROVED
universal criterion**

The assertion that every safe canonical grid has $Q(E)>0$ on at least one
largest-mass anchor transition fiber is false. The required configuration

$$
 V=(1,3,4,5),\qquad q=5,qquad L=100                 \tag{96}
$$

has four safe classes. The canonical anchor is velocity $1$, with phase
record $(v,H,a,c,\rho)=(1,100,1,80,19)$. In state order
$00,01,10,11$, the fiber sizes, multiplicity histograms, and quadratic values
are

$$
\begin{array}{c|c|c|c}
00&60&(4,38,18,0,0)&-20\\
01&1 &(0,1,0,0,0)&0\\
10&1 &(0,0,1,0,0)&-2\\
11&38&(0,20,9,2,7)&-22.
\end{array}                                           \tag{97}
$$

Thus none of the four fibers certifies the already existing safe classes.

**Proof.** Reconstruct $A_1$ from the displayed phase record and the other
three strips from their LRC data. Direct lcm-period membership gives (97),
while the independent moment formula (95) gives the same four values. Since
all values are nonpositive, (96) disproves the proposed universal criterion. □

This failure also shows that the quadratic downweighting does not rescue the
TASK 23 obstruction as a universal method: it misses both (96) and the safe
TASK 23 example $(1,2,3,4,5,7)$. The implication (94) remains valid.

## Computational audit — **VERIFIED**

The histogram and localized-moment implementations of (95) agree on 45
inputs. The deterministic audit checks $(1,3,4,5)$, all TASK 14 obstructions,
both TASK 22--23 certificates, and 442 gcd-one subsets of
$\{1,\ldots,10\}$ of sizes three through six with a defined canonical grid.
The criterion certifies 289 and misses 153 safe grids. The first missed system
in the exhaustive ordering is (96). All fibers are evaluated on $L$, never
$qW$.

## TASK 24 outcome and narrow barrier

A genuinely phase-defined localized statistic with a rigorous bounded-order
certificate is now available, but the four transition types aggregate safe
and double-covered locations too coarsely. The next narrow problem is to find
a nontrivial bounded-complexity refinement of the phase fibers—strictly
coarser than singleton reconstruction—that separates these populations, or
to prove that every fixed-complexity phase partition can fail.

---

# TASK 25 audit: bounded-complexity phase refinement

## Theorem 57 (fixed-anchor transition refinement) — **PROVED**

Fix $k\ge1$ independently of $L$ and choose the $k$ labels of largest lifted
bad mass, breaking ties by label order. For each chosen anchor retain the
before/after pair $(1_{A_i}(z),1_{A_i}(z+1))$. Their joint values partition
$\mathbb Z/L\mathbb Z$ into at most

$$
 \boxed{4^k}                                           \tag{98}
$$

phase-defined fibers. This choice uses no global safe-point information. On
each fiber use the quadratic $Q(E)$ of (93). Positivity still implies a safe
class, and $Q(E)$ is expressible using shifted-arc CRT intersections of order
at most

$$
 \boxed{2k+2.}                                         \tag{99}
$$

**Proof.** Each anchor supplies four possible transition pairs, proving
(98). A fiber fixes membership in $A_i$ at $z$ and $z+1$ for every anchor.
Writing zero conditions as complements expands its indicator into products
of at most $2k$ shifted bad-arc indicators. Formula (95) introduces at most
two further unshifted bad arcs, giving (99). The sign proof of Theorem 55 is
pointwise and is unaffected by refining the fiber. □

Thus $k=4$ gives at most 256 fibers and CRT order at most ten, both uniform in
the possibly enormous lcm period. This is not singleton reconstruction: the
fiber bound does not depend on $L$.

## Proposition 58 (least refinement for the three critical records) —
**VERIFIED / not universal**

Under the deterministic largest-mass anchor rule:

* $(1,3,4,5)$ is not certified for $k=1$ but is certified for $k=2$;
* the TASK 22 record $(1,4,5,6,9)$ is already certified for $k=1$;
* the TASK 23 record $(1,2,3,4,5,7)$ is not certified for
  $k=1,2,3$ but is certified for $k=4$.

These are exact finite evaluations on their canonical lcm grids. They show
that four anchors are genuinely needed by this rule on the named records;
they do not prove that four anchors always suffice.

## Other bounded candidate classes — **PROVED definitions / VERIFIED audit**

Two distinct refinements were audited rather than conflated with (98).

1. A radius-$r$ short-word fiber records one canonical anchor at offsets
   $-r,\ldots,r$. It has at most $2^{2r+1}$ fibers and its quadratic uses CRT
   order at most $2r+3$ after complement expansion.
2. A $B$-bin phase fiber divides the reduced affine coordinate
   $a_i(z-c_i)\bmod H_i$ of one canonical anchor into $B$ fixed consecutive
   bins. It has at most $B$ fibers and its quadratic uses one bin constraint
   together with intersections of at most two bad arcs.

Both definitions are phase-based, fixed before safe points are examined, and
uniformly bounded independently of $L$. Neither candidate is universally
successful on the audited range: radius one and two first miss
$(1,3,4,5)$; four bins first miss $(1,2,3,5)$; and eight bins first miss
$(1,6,7,10)$.

## Computational audit — **VERIFIED**

Independent tests check the fiber bounds and the rigorous sign implication on
45 required/seeded inputs. In the exhaustive 442-input TASK 24 scope, the
one-, two-, and three-anchor rules certify respectively 289, 414, and 440
inputs. The up-to-four-anchor rule (using all labels when $N<4$) certifies all
442. It also certifies all 148 seeded admissible inputs of sizes seven through
nine with velocities below 46. No universal conclusion is drawn: this is
finite evidence, and a larger counterexample may exist. All computations use
the canonical lcm period, never $qW$.

## TASK 25 outcome and narrow barrier

Four transition anchors are the first tested uniformly bounded refinement
that handles every TASK 22--24 critical record and every configuration in the
current exhaustive and seeded audits. TASK 26 must separately recheck all
TASK 14 obstructions. The remaining narrow question is
whether the $k=4$ certificate follows from the LRC divisor/phase constraints,
or whether a larger canonical system defeats it. Exact reconstruction alone
is excluded; a proof must control at most 256 fibers using order-ten CRT data.

---

# TASK 26 audit: four-anchor certificate

## Theorem 59 (direct phase/CRT expression) — **PROVED**

Let $a_1,\ldots,a_4$ be the four largest-mass anchors. For a transition
pattern

$$
 \sigma=(\sigma_{r,s})_{1\le r\le4,\ s\in\{0,1\}}
 \in\{0,1\}^8,
$$

define

$$
 E_\sigma=\{z:1_{A_{a_r}}(z+s)=\sigma_{r,s}
 \text{ for every }r,s\}.                              \tag{100}
$$

Writing $X_i(z)=1_{A_i}(z)$, every fiber quadratic is exactly

$$
 \boxed{Q(E_\sigma)=\sum_{z\bmod L}1_{E_\sigma}(z)
 \left(N-N\sum_iX_i(z)+2\sum_{i<j}X_i(z)X_j(z)\right).} \tag{101}
$$

In (100), each positive condition is the centered phase constraint

$$
 a_{a_r}(z+s-c_{a_r})\in[-\rho_{a_r},\rho_{a_r}]
 \pmod {H_{a_r}},                                      \tag{102}
$$

and each zero condition is its complement. Expanding the complements in
(101) gives a signed sum of generalized-CRT intersections involving at most
the eight shifted anchor arcs and two unshifted arcs. Thus every one of the at
most 256 values is determined directly from $(H_i,a_i,c_i,\rho_i)$ by CRT
histograms of order at most ten.

**Proof.** Formula (101) is (95) written pointwise. Equation (102) is Theorem
38 after replacing $z$ by $z+s$. Expanding the eight binary conditions gives
products of at most eight shifted indicators; the constant, linear, and
quadratic terms in (101) add respectively zero, one, or two indicators.
Generalized CRT applies to every resulting centered modular-arc intersection.
□

This is an exact bounded-order expression, not a positivity inequality.

## Proposition 60 (universal four-anchor positivity) — **DISPROVED**

The four-largest-mass transition rule can fail even on a canonical grid with
many safe classes. A counterexample is

$$
 V=(1,5,6,7,8,11,13),\qquad q=8.                      \tag{103}
$$

Its canonical lcm period is $L=832$. The four anchors are

$$
 (1,5,7,11),                                          \tag{104}
$$

there are 40 realized transition fibers, and

$$
 \boxed{\max_\sigma Q(E_\sigma)=0}                    \tag{105}
$$

although the full system has 14 safe classes. Hence no fiber satisfies the
sufficient positivity condition.

The complete compact phase records $(v,H,a,c,\rho)$ are

$$
\begin{aligned}
&(1,832,1,728,103),(5,832,5,728,103),\\
&(6,416,3,312,51),(7,832,7,728,103),\\
&(8,104,1,0,12),(11,832,11,728,103),\\
&(13,64,1,24,7).
\end{aligned}                                         \tag{106}
$$

**Proof.** Substitution of (106) into (100)--(102) yields the 40 histograms
stored in `task26_results.json`; direct membership independently gives the
same histograms and 14 zero-multiplicity classes. Evaluating (101) on every
histogram gives maximum zero, proving the failure of strict positivity. □

This configuration is not an LRC counterexample—it has 14 safe
classes. It is a counterexample only to the proposed four-anchor certificate.
(103) is already one of the mandatory TASK 14 obstructions; the earlier TASK
25 summary failed to call out this required-family failure and is corrected
above. Every single deletion except removal of velocity 7 retains the
canonical hypothesis and is certified by four anchors; after removing 7 no
$q=7$-divisible velocity remains, so the construction is undefined. This is a
local deletion-minimality certificate, not a claim of globally smallest
possible failure.

For this example, one through four anchors all fail, while five anchors
certify it with maximum quadratic value 51. Thus the obstruction is genuinely
at the proposed fixed level four rather than a failure of the implementation
to detect any refinement.

## Computational audit — **VERIFIED**

An independent test reconstructs all 40 fiber histograms, verifies that they
partition all 832 classes, checks every quadratic from the histogram, and
checks the 14 safe classes directly. The complete mandatory audit finds 21 of
22 TASK 14/TASK 22--24 records certified; (103) is the unique failure. No scan
of $qW$ is used.

## TASK 26 outcome and narrow barrier

The attractive fixed four-anchor conjecture is conclusively false. Increasing
to five repairs the first counterexample but merely shifts the question. The
narrow next problem is whether any absolute anchor count can work, or whether
one can construct LRC-derived failures requiring arbitrarily many phase
anchors. A useful theorem must explain anchor complexity structurally rather
than select the next constant from experiments.
