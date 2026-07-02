# Certificate Frontier Theorems

_Created: 2026-07-01. Scope: finite-residue descent certificates for the shortcut Collatz map._

## Definitions

Let

```text
T(n) = n / 2          if n is even
     = (3n + 1) / 2  if n is odd.
```

For a depth `d` and residue `r mod 2^d`, write every integer in the class as

```text
n = 2^d q + r.
```

The first `d` shortcut iterates have the affine form

```text
T^d(n) = 3^o q + T^d(r),
```

where `o` is the number of odd shortcut steps taken by the low residue `r` during those `d` steps.

## Theorem 1: descent certificate criterion

If

```text
3^o < 2^d,
```

then there is an explicit finite threshold

```text
q_0 = max(0, floor((T^d(r) - r) / (2^d - 3^o)) + 1)
```

such that every positive integer `n = 2^d q + r` with `q >= q_0` satisfies

```text
T^d(n) < n.
```

### Proof

Using the affine form,

```text
T^d(n) < n
```

is equivalent to

```text
3^o q + T^d(r) < 2^d q + r,
```

or

```text
T^d(r) - r < (2^d - 3^o) q.
```

When `2^d - 3^o > 0`, the displayed threshold is exactly the least integer bound forcing this inequality.

## Theorem 2: frontier survival depends only on odd-count

At depth `d`, a residue prefix is not certified by Theorem 1 if and only if

```text
3^o >= 2^d.
```

Therefore the frontier size can be counted by a dynamic program on odd-count alone. The residue values and intercepts matter for thresholds and samples, but not for whether the multiplier test has already certified a prefix.

## Theorem 3: no finite full-`2`-adic cover by this certificate

The all-odd parity path survives the multiplier test at every finite depth, because at depth `d` it has `o = d`, hence

```text
3^d >= 2^d.
```

The corresponding residue class is

```text
n == -1 mod 2^d.
```

The nested intersection of these classes is the `2`-adic fixed point `-1`, since

```text
T(-1) = (3(-1) + 1) / 2 = -1.
```

So this descent-certificate strategy cannot produce a finite cover of the entire `2`-adic space. Any successful Collatz proof using this route must add a positive-integer exclusion principle: surviving `2`-adic boundary paths such as `-1` must be shown irrelevant to positive integer orbits, or every positive finite-bit shadow must be shown to leave the boundary and enter a certified cylinder.

## Theorem 4: convergence implies eventual usable certificate

Fix a positive integer `n > 1`. If the shortcut Collatz orbit of `n` reaches `1`, then `n` has a finite usable descent certificate in this framework: there is a depth `d` such that

```text
T^d(n) < n
```

and the residue cylinder `n mod 2^d` satisfies the multiplier condition

```text
3^o < 2^d
```

with the actual high quotient of `n` meeting the certificate threshold.

### Proof

If `n` reaches `1`, then after some time `d_0` its orbit is in the shortcut cycle

```text
1 -> 2 -> 1.
```

Each additional two shortcut steps around this cycle add one odd step and multiply the affine slope by `3`, while the modulus factor grows by `4`. Thus for sufficiently large `m`,

```text
3^(o_0 + m) < 2^(d_0 + 2m).
```

Also `T^(d_0 + 2m)(n)` is either `1` or `2`, hence below `n`. Taking `d = d_0 + 2m` also makes `d` larger than the bit length of `n`, so the high quotient of `n = 2^d q + r` is `q = 0`; because the image is below the residue, the threshold is `0`, and the certificate is usable for the start itself.

## Theorem 5: finite usable certificates are induction steps

If `n > 1` has a usable certificate, then `T^d(n) < n` for some finite `d`. Therefore, under strong induction, convergence of all smaller positive integers implies convergence of `n`.

Consequently, proving that every `n > 1` has a finite usable certificate is equivalent to the **full** conjecture, not merely its divergent-orbit half: the minimal element of a hypothetical nontrivial cycle never descends below itself, so "every `n` descends" excludes nontrivial cycles as well, and strong induction then yields convergence of every integer. (Conversely, by Theorem 4, the full conjecture implies every `n` has a usable certificate.) This equivalence is classical — "every `n > 1` eventually drops below itself" is the standard restatement of Collatz — which is why the certificate framing sharpens the target without weakening it.

## Theorem 6: Mersenne shadows leave the all-odd boundary after finite time

For every `m >= 1`, the finite positive shadow

```text
n_m = 2^m - 1
```

takes exactly `m` consecutive odd shortcut steps, and

```text
T^m(n_m) = 3^m - 1.
```

After that, the trajectory immediately takes

```text
v_2(3^m - 1)
```

even shortcut steps. By the standard lifting-the-exponent calculation,

```text
v_2(3^m - 1) = 1              if m is odd
             = 2 + v_2(m)     if m is even.
```

### Proof

The stronger induction formula is

```text
T^j(2^m - 1) = 3^j 2^(m-j) - 1
```

for `0 <= j <= m`. The right side is odd while `j < m`, so the shortcut map applies its odd branch at every one of the first `m` steps. At `j = m`, this gives `3^m - 1`, which is even. The valuation formula is the usual LTE identity for `3^m - 1`.

This proves that Mersenne starts are finite shadows of `-1`, not the boundary point itself: they follow the all-odd path for `m` steps and then must leave it.

## Consequence for the proof search

The current attack has not solved Collatz. It has reduced one route to a sharper target:

```text
Separate finite positive integer orbits from the persistent high-odd 2-adic survivor set by proving every finite binary shadow eventually exits into a usable certificate.
```

This is the exact gap Fable 5 Ultracode should attack next.

The companion script [`frontier_escape_analyzer.py`](frontier_escape_analyzer.py) tests this gap directly at finite depths: enumerate survivor prefixes, replace each by its finite positive representative, and measure the first usable descent certificate. Those computations are evidence only; the theorem still missing is a uniform reason that every positive finite shadow must escape.

The search-grade companion [`frontier_beam_search.py`](frontier_beam_search.py) probes possible hard families beyond exact enumeration. Its current signal is that mixed-bit lifts, not merely all-ones/Mersenne shadows, can delay certificate descent. A proof in this framework therefore needs an escape envelope for arbitrary survivor-prefix lifts, not just for the all-odd boundary.

The profiler [`parity_surplus_analyzer.py`](parity_surplus_analyzer.py) further splits the missing envelope into two cases. Low-excess paths stay near the exact line `3^o = 2^d`; high-excess paths accumulate image height and must later repay it. A uniform proof needs to dominate both the critical-line corridor and the high-surplus repayment regime.

## Dual-debt decomposition

For any fixed parity prefix of length `d`, the shortcut iterate has the affine form

```text
T^d(n) = (3^o n + C) / 2^d
```

for some nonnegative integer translation term `C` determined by the positions of the odd steps in that prefix. Therefore the actual height of the finite representative satisfies

```text
log2(T^d(n) / n)
  = (o log2 3 - d) + log2(1 + C / (3^o n)).
```

So actual height debt is multiplier debt plus a positive affine translation gap. The companion [`debt_phase_analyzer.py`](debt_phase_analyzer.py) measures this gap on hard examples. In the large hard examples currently tracked, the gap is below displayed double-precision scale, so the hard dynamics are almost entirely governed by the parity multiplier debt. In small starts like `27`, the gap is visible and must be covered by finite verification or a sharper translation bound.

## Repayment-window identity

Let a concrete positive start reach peak dual debt at shortcut depth `p`, and
let `c > p` be the first depth where both

```text
3^o(c) < 2^c
T^c(n) < n
```

hold. Write

```text
L = c - p
a = o(c) - o(p).
```

Then the multiplier debt repaid over the interval is exactly

```text
L - a log2(3).
```

Equivalently, repayment requires a subcritical odd density

```text
a / L < 1 / log2(3) = 0.630929753...
```

large enough to erase the peak dual debt plus any remaining affine translation
gap. This is an identity, not yet a proof of existence of such an interval.

The companion [`repayment_envelope_scan.py`](repayment_envelope_scan.py)
measures these windows. The current finite evidence suggests a concrete theorem
target: every positive finite shadow of the `2`-adic survivor frontier must
eventually contain a repayment window whose odd density is sufficiently below
`1/log2(3)` to force a usable certificate. The obstruction is now sharper: prove
that no positive integer can remain forever in the survivor frontier while
avoiding such subcritical repayment windows.

## Repayment motifs

A repayment window is not only a length and an odd count. It is a finite parity
word. The pair

```text
(L, a) = (window length, odd steps in the window)
```

is its coarse motif, and the run decomposition of the window is its fine motif.
The deficit identity depends only on `(L, a)`,

```text
deficit(L, a) = L - a log2(3),
```

while the fine motif determines which positive finite shadow actually realizes
that repayment word.

The companion [`repayment_motif_miner.py`](repayment_motif_miner.py) groups
repayment windows by these motifs. In the exact base-24 survivor frontier, the
hard slow-critical edge is carried by motifs such as

```text
210:126   odd ratio = 0.600000000
209:126   odd ratio = 0.602870813
```

with deficit per step roughly `0.049022500` and `0.044472368` bits
respectively. This does not prove a global recurrence theorem, but it suggests
the next refinement: prove that sufficiently long positive survivor shadows
must realize a member of a finite or recursively controlled family of
subcritical repayment motifs.

## Motif forcing is a finite-shadow statement

One has to be careful about the quantifier. A free infinite survivor word can
avoid every subcritical motif simply by staying all-odd forever; this is the
`2`-adic point `-1`, not a positive finite integer. Therefore motif forcing
cannot be a theorem about arbitrary survivor parity words.

The correct target is:

```text
Every positive finite shadow of the survivor frontier eventually realizes a
subcritical motif family whose accumulated deficit clears its peak debt.
```

The companion [`motif_forcing_analyzer.py`](motif_forcing_analyzer.py) tests
this finite-shadow version for selected motif families. In the exact base-24
frontier:

```text
64-step post-peak motifs:  2,532 / 286,581 representatives detected
209/210-step slow motifs:      3 / 286,581 representatives detected
```

The rare `209:126` detections are precisely the slow-critical edge examples in
that frontier. This makes the motif family useful as a classifier and proof
target, not as a universal one-size finite cover.

## Motif covers compress the finite proof obligation

The exact repayment motifs are still too granular for a theorem. The companion
[`motif_cover_analyzer.py`](motif_cover_analyzer.py) therefore groups each
peak-to-clear repayment into coarse families: exact motif, length band,
odd-ratio band, deficit-per-step band, class label, and combined
length-ratio band.

In the exact base-24 survivor frontier, this compression currently gives:

```text
representatives scanned:          286,581
distinct exact motifs:                821
distinct length-ratio families:        86
short-high-deficit class:         163,478
mixed class:                      122,876
rare outlier classes:                 227
```

The greedy coarse cover reaches `99.9207903%` of that finite frontier using
only two class families, `short-high-deficit` and `mixed`. The remaining `227`
representatives are not noise; they contain the rare low-slope, slow-long,
slow-critical-long, and high-debt-fast cases that carry the hardest behavior in
the finite frontier.

So the current proof target is no longer "find every motif." It is:

```text
Prove the common coarse repayment classes are unavoidable and harmless by a
uniform envelope, then prove a recursive forcing rule for the rare outlier
classes.
```

This remains finite evidence. It does not prove Collatz. It does sharpen the
next theorem shape: a usable proof in this lane must turn motif-cover
compression into a uniform positive-finite-shadow forcing statement, with the
nonpositive all-odd `2`-adic limit still explicitly excluded.

## Outlier transitions do not reproduce at base depth 24

The cover-compression result leaves `227` rare outliers in the exact base-24
frontier. The companion
[`outlier_transition_analyzer.py`](outlier_transition_analyzer.py) treats those
outliers recursively: after an outlier obtains its first usable descent
certificate, apply that descent and classify the smaller descendant.

With terminal classes

```text
short-high-deficit, mixed, trivial-halving
```

the exact base-24 outlier population has this finite transition matrix:

```text
low-slope            -> trivial-halving      113
low-slope            -> short-high-deficit    91
low-slope            -> mixed                  3
slow-long            -> trivial-halving        7
slow-long            -> short-high-deficit     6
slow-critical-long   -> trivial-halving        3
high-debt-fast       -> trivial-halving        2
high-debt-fast       -> short-high-deficit     1
high-debt-fast       -> mixed                  1
```

So, at base depth `24`, every one of the `227` rare outliers reaches a harmless
terminal class after one certified descent generation. This is still not a
proof: the missing theorem is the uniform version saying that rare outlier
classes cannot recursively reproduce forever for positive finite shadows at
arbitrary depth.

## Lemma 7.0: parity-word bijection (Terras)

For every depth `d >= 1`, the map sending a residue `r mod 2^d` to its parity
word

```text
w(r) = (r mod 2, T(r) mod 2, ..., T^(d-1)(r) mod 2)
```

is a bijection from `Z / 2^d` onto `{0,1}^d`.

### Proof

Injectivity: suppose `r != r' mod 2^d` share the same parity word of length
`d`, and let `2^v` exactly divide `r - r'`, so `v < d`. At every shared step
the difference transforms as

```text
delta -> 3^epsilon * delta / 2,
```

where `epsilon` is the shared parity bit, because both branches of `T` are
affine with the same slope on integers of equal parity. Since `3` is odd,
each shared step lowers the `2`-adic valuation of the difference by exactly
one. After `v` steps the difference is odd, so at step `v + 1 <= d` the two
orbits have different parities — contradicting the shared word. An injection
between finite sets of equal cardinality `2^d` is a bijection.

Consequence: counting survivor parity words is exactly counting uncertified
residue classes. This is the identity the DP instruments have been using;
it is stated here so the counting theorem below is self-contained.

## Theorem 7: frontier entropy bound

Let `o_min(d) = min { o : 3^o >= 2^d }` and let `S(d)` be the number of
depth-`d` survivor prefixes (equivalently, by Lemma 7.0, the number of
residues mod `2^d` not certified by the depth-`d` multiplier test). Let
`theta = log_3 2 = 0.6309297535714574...` and let `H` be the binary entropy
in bits. Then, unconditionally,

```text
S(d) <= sum_{k = o_min(d)}^{d} C(d, k) <= 2^(d * H(theta)),
```

and therefore the uncertified density satisfies

```text
S(d) / 2^d <= 2^(-(1 - H(theta)) * d),
1 - H(theta) = D(theta || 1/2) = 0.0500444728116693651860994...
```

### Proof

A depth-`d` survivor satisfies in particular the endpoint constraint
`o(d) >= o_min(d)` (Theorem 2), so `S(d)` is at most the number of length-`d`
binary words with at least `o_min(d)` ones — the binomial tail. For the
entropy step, put `a = o_min(d) / d`; the definition of `o_min` forces
`a >= theta > 1/2`. The standard binomial-tail bound (Chernoff tilt at
`x = a/(1-a)`, or Cover–Thomas Theorem 11.1.4 applied to the complemented
word) gives

```text
sum_{k >= a d} C(d, k) <= 2^(d * H(a)),
```

and `H` is decreasing on `[1/2, 1]`, so `H(a) <= H(theta)`.

### Numerical verification

`escape_envelope_analyzer.py` re-checks the first inequality by exact integer
comparison on a grid of 65 depths through `d = 2048` (minimum slack `0.0`
bits — equality at `d = 1`, where `S(1) = C(1,1) = 1`) and the entropy step
with slack `>= 0.9499` bits everywhere. The exact DP shows the truth is
thinner still at finite depth: the measured rate `-log2(S(d)/2^d)/d` falls
from `0.1079` at `d = 128` to `0.0564` at `d = 2048`, approaching the proved
`0.050044` from above with a correction consistent with the ballot-type
polynomial factor `d^(-3/2)`.

## Corollary 7.1: quantitative Terras-type density

For every `d`, the density of positive integers whose coefficient stopping
time (first depth at which `3^o < 2^d`) exceeds `d` is at most
`2^(-0.0500444 * d)`. The certificate frontier is exponentially thin,
unconditionally. (Not new to the literature — Terras 1976 and Everett 1977
give density zero, and Krasikov–Lagarias give stronger counting bounds — but
the repo now carries a self-contained machine-checked proof with an explicit
exponent, matched against exact counts.)

## Conjecture 7.2: first-moment escape envelope

Let `D(b)` be the maximum first usable certificate depth over the finite
representatives of the depth-`b` survivor frontier. Define the first-moment
crossing

```text
D_1(b) = max { d : b + log2(S(d)) - d >= 0 }.
```

Conjecture: `D(b) = D_1(b) + O(fluctuation)`, and asymptotically

```text
limsup D(b) / b = c* = 1 / (1 - H(theta)) = 19.9822266839190301...
```

`c*` is the first-descent analogue of the Lagarias–Weiss total-stopping-time
constant `41.677647`. Any **proved** bound `D(b) <= f(b)` for a computable
`f` would close the divergence half of Collatz (and with Theorem 5, the
whole conjecture); the random model says the sharp such bound has slope
`c*`. Exact records at base depths 14–28 (105, 135, 135, 183, 224, 287,
395) track the crossings (129, 161, 194, 229, 263, 297, 369) with deviations
between `-59` and `+26` — see [`ESCAPE-ENVELOPE.md`](ESCAPE-ENVELOPE.md) for
the full measurement.

## Lemma 8.0: distinct partial sums

For a parity word `w in {0,1}^d` define the drift path

```text
P_j = o(j) * ln 3 - j * ln 2        (j = 0, 1, ..., d),
```

where `o(j)` counts ones among the first `j` letters. Then the survivor
condition `3^(o(j)) >= 2^j` for all `j <= d` is equivalent to `P_j > 0` for
all `1 <= j <= d`, and all values `P_0, ..., P_d` are pairwise distinct.

### Proof

Equivalence: `3^(o(j)) >= 2^j` iff `P_j >= 0`, and `P_j = 0` would force
`3^(o(j)) = 2^j`, impossible for `j >= 1` (parity). Distinctness: `P_j = P_k`
with `j < k` would force `3^(o(k) - o(j)) = 2^(k - j)` with `k - j >= 1` —
again impossible. ∎

## Lemma 8.1: cycle lemma for the drift path

Let `w in {0,1}^d` have `o` ones with `3^o > 2^d` (total drift
`s = o ln 3 - d ln 2 > 0`). Then at least one of the `d` cyclic shifts of `w`
is a survivor word.

### Proof

Extend `w` periodically and let `P` be its prefix-sum path, so
`P_(j+d) = P_j + s`. By Lemma 8.0 the values `P_0, ..., P_(d-1)` are
distinct; let `m in [0, d)` be the unique index minimizing `P` over one
period. Consider the shift starting at position `m + 1`; its `k`-th partial
sum is `P_(m+k) - P_m` for `k = 1, ..., d`. If `m + k < d`, then
`P_(m+k) > P_m` by strict minimality. If `m + k >= d`, then
`P_(m+k) = P_(m+k-d) + s >= P_m + s > P_m` since `0 <= m + k - d <= m`. So
every partial sum of the shifted word is strictly positive, which by Lemma
8.0 is exactly the survivor condition. ∎

## Theorem 8: cycle-lemma lower bound (two-sided survivor mass)

For every `o` with `3^o > 2^d`,

```text
S(d) >= C(d, o) / d,
```

and in particular, taking `o = o_min(d)` and combining with Theorem 7,

```text
C(d, o_min(d)) / d  <=  S(d)  <=  2^(d * H(theta)).
```

With the standard type bound `C(d, k) >= 2^(d*H(k/d)) / (d + 1)` and
`0 <= o_min(d) - d*theta < 1`, this yields, for all `d >= 20`,

```text
2^(d * H(theta)) / (3 d^2)  <=  S(d)  <=  2^(d * H(theta)),
```

i.e. `S(d) = 2^(d*H(theta) + O(log d))` — the survivor mass is pinned to
within polynomial factors, unconditionally.

### Proof

Rotations preserve the number of ones, so the `C(d, o)` words with `o` ones
partition into cyclic classes of size at most `d`. Each class satisfies
`s > 0`, hence contains at least one survivor by Lemma 8.1. Therefore
`S(d) >= #classes >= C(d, o) / d`. For the explicit form: with
`a = o_min(d)/d in [theta, theta + 1/d)`, the mean value theorem gives
`H(a) >= H(theta) - |H'(xi)| / d` for some `xi in (theta, a)`; on
`[theta, theta + 1/20]` one has `|H'| <= 1.1` bits, so
`2^(d*H(a)) >= 2^(d*H(theta)) * 2^(-1.1)`, and
`2^(-1.1) / (d(d+1)) >= 1 / (3 d^2)` for `d >= 20`. ∎

### Numerical verification

`escape_envelope_analyzer.py` checks `C(d, o_min)/d <= S(d)` in exact integer
arithmetic on 65 grid depths through `d = 2048` (held everywhere; equality at
`d = 1` where both sides are `1`). At `d = 2048`: exact cycle floor
`log2(C(2048,1293)/2048) = 1928.07` bits, actual `log2 S = 1932.40` (slack
`4.32` bits), entropy ceiling `1945.47` (slack `13.08` bits); the weaker
closed-form floor `2^(dH)/(3d^2)` sits at `1921.92` bits.

## Corollary 8.1: what remains unproved in the envelope

Theorem 8 makes the survivor-mass side of Conjecture 7.2 unconditional:

```text
-log2( S(d) / 2^d ) = (1 - H(theta)) * d + O(log d),
```

so the first-moment crossing satisfies `D_1(b) = c* b + O(log b)` as a
**theorem**, and the box dimension `H(theta)` of the frontier follows by pure
counting. The only unproved ingredient left in the escape-envelope
conjecture is *representative equidistribution*: that the integer
representatives of survivor classes are spread in `[0, 2^d)` regularly enough
that the minimal survivor tracks `2^d / S(d)`. The measured minimal-survivor
duality products `m * S(d)/2^d` at the exhaustively-known records
(`d = 105, 135, 183, 224, 287, 395`) are `1.96, 1.74, 6.6, 1.29, 1.21, 0.30`
— order one across seventeen binary orders of magnitude of density, which is
precisely the equidistribution the conjecture needs, measured where it
matters and proved nowhere.

## Endpoint terminal mechanism

The outlier transition can be inspected one layer lower. Let

```text
x = T^d(n)
```

where `d` is the first usable certificate depth of a rare outlier `n`. The
companion [`endpoint_terminal_analyzer.py`](endpoint_terminal_analyzer.py)
records the `2`-adic valuation of `x` and the next certificate class.

For the exact base-24 rare outliers:

```text
outliers analyzed:       227
endpoint even:           125
endpoint odd:            102
next trivial-halving:    125
next short-high-deficit:  98
next mixed:                4
```

Endpoint valuations were:

```text
v2 = 0: 102
v2 = 1:  65
v2 = 2:  39
v2 = 3:  12
v2 = 4:   6
v2 = 5:   2
v2 = 7:   1
```

So the finite base-24 mechanism is: `125` outliers land immediately on an even
endpoint, and the remaining `102` odd endpoints are already in short/common
terminal classes. Three sampled base-28 slices (`sample_stride = 32`, offsets
`0`, `8`, `16`) analyzed `394` rare sampled outliers and again found all `394`
landing in `trivial-halving`, `short-high-deficit`, or `mixed` after one
certificate endpoint.

The theorem target is now even more concrete:

```text
Rare positive finite survivor shadows have certificate endpoints in terminal
residue families; rare outlier classes cannot map to rare outlier classes
indefinitely.
```

This is a proof target, not a proved global statement.

## Terminal residue cover

The endpoint result can be compressed further. The companion
[`terminal_residue_cover_analyzer.py`](terminal_residue_cover_analyzer.py)
groups rare-outlier certificate endpoints by low residue modulo `2^k` and asks
when every observed bucket has a single next terminal class.

For the exact base-24 rare outliers, the first pure low-bit endpoint cover
appears at `k = 8`:

```text
rare endpoints analyzed:       227
nonterminal next classes:        0
minimal pure cover bits:         8
pure buckets modulo 256:       118
mixed buckets at k = 8:          0
```

The cover progression is not just parity. At `k = 1`, only `125 / 227`
records lie in pure buckets; by `k = 4`, `212 / 227` do; by `k = 8`, all
`227 / 227` do. Thus the finite base-24 endpoint population has a concrete
terminal residue grammar modulo `256`.

Sampled base-28 slices with `sample_stride = 32` also produced pure endpoint
covers within small low-bit windows:

```text
offset  rare endpoints  nonterminal next  minimal pure bits  buckets at minimum
0       134             0                 1                  2
8       126             0                 8                  91
16      134             0                 10                 127
```

This is still finite evidence. The missing theorem is a uniform derivation of
these terminal endpoint buckets for every positive finite survivor shadow, not
only for the exact base-24 frontier and sampled base-28 slices.

## Terminal residue stability is a lifting problem

The next falsification test is whether the exact base-24 modulo-`256` grammar
can simply be reused as a fixed table at deeper frontier depths. The companion
[`terminal_residue_stability_analyzer.py`](terminal_residue_stability_analyzer.py)
compares a reference grammar against deeper sampled endpoints.

Using the exact base-24 rare endpoints as reference and sampled base-28 slices
with `sample_stride = 32`:

```text
offset  target rare endpoints  covered by base-24 table  contradictions  novel endpoints
0       134                    62                        0               72
8       126                    66                        1               60
16      134                    70                        3               64
```

At eight endpoint bits, the fixed base-24 table covers only about half of the
sampled base-28 rare endpoints. More importantly, it has direct class
contradictions:

```text
223 mod 256: base-24 mixed              -> base-28 short-high-deficit
 31 mod 256: base-24 short-high-deficit -> base-28 mixed
207 mod 256: base-24 mixed              -> base-28 short-high-deficit
191 mod 256: base-24 mixed              -> base-28 short-high-deficit
```

So the correct theorem cannot be "the base-24 modulo-`256` terminal table is
universal." The evidence instead points to a lifting theorem:

```text
Every deeper rare endpoint either lifts into an already terminal residue family
with compatible higher bits, or enters a new finite terminal family after
enough additional low endpoint bits are exposed.
```

This is a stronger and more honest target. It preserves the terminal endpoint
mechanism while rejecting a false fixed-table simplification.

## Mixed terminal residues resolve under finite lifting in the sampled merge

The corrected lifting target is tested by
[`terminal_residue_lift_analyzer.py`](terminal_residue_lift_analyzer.py). It
merges the exact base-24 rare endpoints with sampled base-28 rare endpoints and
asks whether mixed low-bit endpoint buckets become pure after exposing more
endpoint bits.

For the merge

```text
base24 exact rare endpoints:             227
base28 sampled offsets 0, 8, 16:         394
merged rare endpoint records:            621
```

the cover progression is:

```text
bits  buckets  mixed buckets  records in mixed buckets
8     216      6              17
9     306      6              15
10    385      2               4
11    437      2               4
12    469      1               2
13    492      0               0
```

Thus this merged finite population has a pure terminal endpoint grammar by
`13` low endpoint bits.

The six mixed modulo-`256` parents resolve as follows:

```text
parent mod 256  records  resolved bits  extra bits
31              4        10             2
207             3        10             2
191             3        10             2
159             3        10             2
223             2        12             4
127             2        13             5
```

This does not prove a global lifting theorem, but it changes the proof target
again. The observed obstruction is not persistent mixed terminal identity; it is
low-bit aliasing. A uniform theorem in this lane would show that every mixed
terminal parent bucket has a bounded or recursively controlled finite lift into
pure terminal child buckets.

## Adaptive terminal residue grammar

The fixed-width `13`-bit table is still too blunt. The companion
[`terminal_residue_tree_analyzer.py`](terminal_residue_tree_analyzer.py) builds
an adaptive low-bit decision tree: split a bucket only while it is mixed, and
stop as soon as one terminal next class remains.

On the same `621`-record merge (`base24` exact rare endpoints plus sampled
`base28` offsets `0`, `8`, and `16`), the adaptive grammar is much smaller:

```text
records classified:          621
tree nodes:                   56
internal nodes:               32
pure leaves:                  24
unresolved leaves:             0
minimum leaf depth:            1
maximum leaf depth:           13
weighted mean leaf depth:      2.185185185
weighted p50 / p90 / p95:      1 / 4 / 8
weighted p99:                 10
```

The leaf classes are:

```text
trivial-halving:      1 leaf, 315 records
short-high-deficit:  17 leaves, 298 records
mixed:                6 leaves,   8 records
```

So most terminal endpoint classification is decided by very few low bits; the
deep lift tail is tiny. The proof target sharpens again:

```text
Find a structural reason that adaptive endpoint-bit splitting terminates, and
bound the depth of the exceptional mixed-parent tail for positive finite
survivor shadows.
```

This is still finite data. It is not a proof of Collatz. It is a compact
candidate grammar for the rare-outlier endpoint step.

## Held-out adaptive grammar validation

The adaptive grammar can be treated as a classifier. The companion
[`terminal_residue_tree_cv_analyzer.py`](terminal_residue_tree_cv_analyzer.py)
trains on the existing `621`-record merge (`base24` exact plus `base28`
offsets `0`, `8`, `16`) and tests held-out `base28` offsets `4`, `12`, and
`20`.

Held-out performance:

```text
held-out rare endpoint records:       421
records reaching a known tree leaf:   418
prediction coverage:                  0.992874109
agreements:                           413
contradictions:                         5
novel branches:                         3
accuracy on predicted records:        0.988038278
unresolved train leaves:                0
```

Per held-out slice:

```text
offset  records  coverage     accuracy     contradictions  novel branches
4       138      0.992753623  0.985401460  2               1
12      150      1.000000000  0.993333333  1               0
20      133      0.984962406  0.984732824  2               2
```

The main class-flip residues are:

```text
47 mod 64:    trained short-high-deficit -> held-out mixed
255 mod 256:  trained short-high-deficit -> held-out mixed
3 mod 8:      trained short-high-deficit -> held-out mixed
```

The novel branches include `223 mod 512` and `383 mod 512`, both held-out
`short-high-deficit` endpoints in this run.

After absorbing the held-out slices, the combined adaptive tree remains pure:

```text
combined records:              1042
combined nodes:                  96
combined pure leaves:            43
unresolved leaves:                0
max leaf depth:                  15
weighted mean leaf depth:         2.433781190
weighted p50 / p90 / p95 / p99:  1 / 6 / 8 / 10
```

This is a cross-validation signal, not a proof. The theorem target now has a
data-backed refinement: the endpoint-bit grammar generalizes strongly but grows
by adding rare new leaves and splitting a few overconfident short-high-deficit
leaves. A proof must explain both phenomena.

## Full base-28 partition sweep

The held-out test used three slices. The next falsification step is to sweep the
entire base-28 frontier partition. The new
[`terminal_residue_tree_sweep_analyzer.py`](terminal_residue_tree_sweep_analyzer.py)
does this without recomputing the frontier for every offset: it enumerates the
base-28 frontier once, partitions the sorted representatives by stride offset,
then treats each offset as an active-learning batch.

Command used for the final pure run:

```powershell
python experiments/terminal_residue_tree_sweep_analyzer.py --reference-frontier-base-depth 24 --reference-max-depth 768 --target-frontier-base-depth 28 --target-max-depth 1024 --target-sample-stride 32 --seed-target-sample-offsets 0 8 16 --sweep-target-sample-offsets all --max-tree-depth 24 --top-n 8 --output experiments/results/terminal_tree_sweep_28_stride32_d24_20260702.json --quiet
```

The seed tree is the same `621`-record grammar used above: exact base-24 rare
endpoints plus base-28 offsets `0`, `8`, and `16`. Against all `29` remaining
base-28 offsets at once, that seed tree behaves as follows:

```text
sweep rare endpoint records:          3881
records reaching a seed-tree leaf:    3847
prediction coverage:                  0.991239371
agreements:                           3798
contradictions:                         49
novel branches:                         34
accuracy on predicted records:        0.987262802
```

In active-learning order, each offset is evaluated before being absorbed into
the tree. Across those pre-update evaluations the grammar sees:

```text
agreements:       3827
contradictions:     42
novel branches:     12
```

The depth cap matters. With `--max-tree-depth 18`, the final tree still had
`2` unresolved leaves over `9` records. Raising the cap to `24` resolves them
all:

```text
total rare endpoint records:       4502
tree nodes:                         294
pure leaves:                        126
unresolved leaves:                    0
max leaf depth:                      21
weighted mean leaf depth:             2.789649045
weighted p50 / p90 / p95 / p99:       2 / 7 / 10 / 13
```

Final record classes:

```text
trivial-halving:       2200 records,  1 leaf
short-high-deficit:    2239 records, 89 leaves
mixed:                   63 records, 36 leaves
```

The deepest splits are singletons or tiny buckets:

```text
depth 21: 182325295 endpoint -> mixed
depth 21:  65933359 endpoint -> short-high-deficit
depth 19: 85623035 repeated endpoints -> mixed
depth 19: 105808123 repeated endpoints -> short-high-deficit
```

This is the strongest finite endpoint-grammar result currently in the repo:
the complete sampled base-28 frontier partition is absorbed by a pure adaptive
tree, but only after allowing rare branches deeper than the earlier held-out
run exposed. The proof target is therefore not a finite table and not a fixed
depth-13 grammar. It is a controlled-growth theorem: every rare positive
endpoint branch must split into terminal children, and the branch-depth tail
must remain non-reproductive.

## Cross-depth terminal grammar transfer

The full base-28 result can still be a one-depth artifact. The next stress test
trains the terminal grammar on the complete base-28 stride partition and probes
sampled base-29 slices. The new
[`terminal_residue_depth_transfer_analyzer.py`](terminal_residue_depth_transfer_analyzer.py)
implements this transfer test.

Command:

```powershell
python experiments/terminal_residue_depth_transfer_analyzer.py --reference-frontier-base-depth 24 --reference-max-depth 768 --train-frontier-base-depth 28 --train-max-depth 1024 --train-sample-stride 32 --train-sample-offsets all --probe-frontier-base-depth 29 --probe-max-depth 1152 --probe-sample-stride 64 --probe-sample-offsets 0 16 32 48 --max-tree-depth 28 --top-n 10 --output experiments/results/terminal_depth_transfer_28_to_29_stride64_20260702.json --quiet
```

Training population:

```text
base-24 exact rare endpoints:       227
complete sampled base-28 endpoints: 4275
total train records:                4502
train tree nodes:                    294
train pure leaves:                   126
train unresolved leaves:               0
train max leaf depth:                 21
```

Base-29 probe:

```text
base-29 frontier count:             6385637
sampled probe offsets:              0, 16, 32, 48 mod 64
probe rare endpoint records:        564
records reaching train leaves:      562
prediction coverage:                0.996453901
agreements:                         554
contradictions:                       8
novel branches:                       2
accuracy on predicted records:      0.985765125
```

Per probe offset:

```text
offset  records  coverage     accuracy     contradictions  novel branches
0       137      1.000000000  0.992700730  1               0
16      121      1.000000000  0.983471074  2               0
32      154      0.993506494  0.993464052  1               1
48      152      0.993421053  0.973509934  4               1
```

After absorbing the base-29 probe slices, the combined tree is still pure:

```text
combined records:              5066
combined nodes:                 335
combined pure leaves:           143
unresolved leaves:                0
max leaf depth:                  21
weighted mean leaf depth:         2.821752862
weighted p50 / p90 / p95 / p99:  2 / 7 / 10 / 13
```

The main contradiction residues are:

```text
283/1024: short-high-deficit -> mixed
359/512:  short-high-deficit -> mixed
703/1024: short-high-deficit -> mixed
303/1024: mixed -> short-high-deficit
63/512:   short-high-deficit -> mixed
287/512:  short-high-deficit -> mixed
```

The two new branches are:

```text
1791/4096: short-high-deficit
167/2048:  short-high-deficit
```

So the endpoint grammar transfers strongly across one frontier depth, but not
as a closed finite automaton. Deeper frontiers still contribute rare new
children and occasional class flips. The emerging theorem target is now:

```text
Prove that cross-depth endpoint grammar extensions are sparse, terminal, and
non-reproductive, with a bounded or summably thin branch-depth tail.
```

## Positive-kick proof-claim audit

Several adjacent artifacts claim a full resolution via positive-kick /
affine-cocycle repulsion. The mechanism is promising, but a proof claim must be
audited against the executable definitions. The audit instrument is
[`kick_repulsion_claim_audit.py`](kick_repulsion_claim_audit.py).

Command:

```powershell
python experiments/kick_repulsion_claim_audit.py --limit-scan 1000000 --frontier-base-depth 28 --frontier-max-depth 1024 --frontier-sample-stride 1024 --frontier-sample-offsets 0 256 512 768 --top-n 12 --output experiments/results/kick_repulsion_claim_audit_20260702.json --quiet
```

Population checked:

```text
total starts checked:                 1,013,816
initial scan:                         999,999  (2..1,000,000)
hard records / hard seeds:                 34
base-29 transfer-failure starts:           15
sampled base-28 frontier shadows:      13,768
```

Finite checks that passed:

```text
uncertified starts:                       0
gamma-bound violations:                   0
better-bound violations:                  0
```

The tested gamma bound was
`escape_depth(n) <= 19.982226683919038 * bitlen(n) + 32`. The tested
stronger empirical bound was `escape_depth(n) <= 14.56 * bitlen(n) + 32`.

But the stronger mechanism subclaim fails as currently worded:

```text
repulsion-sufficiency failures:         199
```

These are not Collatz counterexamples. Every one still certifies descent.
They are counterexamples to the narrow statement that counted high-alignment
repulsion events alone always pay the excess debt. Representative failures:

```text
start       group                     max_excess  required  counted  max_align
524283      initial_scan              1.274194    1         0        2
262139      initial_scan              1.274194    1         0        2
174522363   sampled_frontier_shadow   1.226756    1         0        2
112451579   sampled_frontier_shadow   1.226756    1         0        2
```

The proof-claim status is therefore:

```text
positive-kick idea: useful candidate mechanism
linear descent bound: no finite failure found in this audit
Collatz proof claim: not proved
mechanism gap: low-alignment quick descents are not covered by counted repulsion
```

The next theorem target is a combined potential:

```text
high-alignment branch -> quantified kick/carry repulsion
low-alignment branch  -> separate quick-descent or potential-drop lemma
both branches         -> uniform certificate descent or smaller induction state
```

## Alignment dichotomy repair

The follow-up analyzer
[`alignment_dichotomy_analyzer.py`](alignment_dichotomy_analyzer.py) tests the
two-branch repair directly on the same population as the kick audit.

Command:

```powershell
python experiments/alignment_dichotomy_analyzer.py --limit-scan 1000000 --frontier-base-depth 28 --frontier-max-depth 1024 --frontier-sample-stride 1024 --frontier-sample-offsets 0 256 512 768 --top-n 12 --output experiments/results/alignment_dichotomy_20260702.json --quiet
```

Result file:

```text
experiments/results/alignment_dichotomy_20260702.json
```

The split is:

```text
total starts checked:       1,013,816
low-alignment starts:         732,062   (max_align < 3)
high-alignment starts:        281,754   (max_align >= 3)
```

Low-alignment branch:

```text
all certified:                    true
max escape depth:                 32
max steps per bit:                2.0
max excess:                       1.274194
violations of 2.0*bitlen + 16:     0
```

High-alignment branch:

```text
all certified:                    true
all repulsions sufficient:        true
max escape depth:                 738
max steps per bit:                14.4615
max excess:                       42.591095
repulsion-sufficiency failures:    0
```

Global checks:

```text
uncertified starts:                0
gamma-bound violations:            0
```

This does not close the conjecture. It repairs the previous audit gap by
splitting the proof obligation:

```text
low alignment  -> prove direct quick descent / potential drop
high alignment -> prove kick/carry repulsion pays excess debt
```

The exact next theorem target is therefore a dichotomy theorem for positive
integer shortcut orbits, followed by an induction that converts the branch
bound into uniform certificate descent.

## Low-alignment structure theorem target

The low branch of the dichotomy has a sharper local algebra now. The instrument
is [`low_alignment_structure_analyzer.py`](low_alignment_structure_analyzer.py),
with result file:

```text
experiments/results/low_alignment_structure_20260702.json
```

Exact identities:

```text
If x is odd and x == 1 or 5 mod 8, then T^2(x) = (3x + 1)/4, which is < x
for every x > 1 (at x = 1 it equals x — the trivial cycle, the unique
equality case since (3x+1)/4 < x <=> x > 1).

If x is odd and x == 3 mod 8, then T^3(x) = (9x + 5)/8.
```

Modulo `64`, the odd `3 mod 8` macro has only one repeat gate:

```text
x == 59 mod 64  <=>  x == -5 mod 64.
```

On that gate:

```text
T^3(x) + 5 = 9(x + 5)/8
v2(T^3(x) + 5) = v2(x + 5) - 3.
```

Full-population check:

```text
total starts checked:       1,013,816
low descents:                 732,062
high entered first:           281,754
uncertified:                        0
repeat-law failures:                0
max low escape depth:              32
max low repeat gates:               6
max low v2(x+5):                   19
```

This gives the low-alignment lemma a concrete rank:

```text
h(x) = v2(x + 5)
```

The proof still needs a global induction, because ordinary drop exits can later
regenerate a new `-5 mod 64` repeat gate. The local obstruction, however, is
now finite and exact: every repeat consumes three units of `h`, every nonrepeat
exit contracts, and the `h == 5` local exit transfers to the high-alignment
branch if descent has not already happened.

## High-alignment ladder theorem target

The high branch of the dichotomy also has exact local algebra. The instrument
is [`high_alignment_ladder_analyzer.py`](high_alignment_ladder_analyzer.py),
with result file:

```text
experiments/results/high_alignment_ladder_20260702.json
```

Exact identity:

```text
If x = 2^a q - 1, q odd, and a = v2(x + 1) >= 3,
then T^k(x) = 3^k 2^(a-k) q - 1 for 0 <= k <= a.
```

So the first `a - 2` odd steps in that ladder are exactly the counted
high-alignment repulsion credits:

```text
ladder credit = a - 2.
```

Full-population check:

```text
total starts checked:       1,013,816
high descents:                281,754
low descents:                 732,062
uncertified:                        0
high ladders checked:         428,318
total ladder credit:          888,579
credit failures:                    0
formula failures:                   0
alignment-burn failures:            0
max ladder alignment:              47
max forced even-chain:             17
```

This gives the high-alignment lemma a concrete credit:

```text
C_high = sum over high ladders of (v2(entry + 1) - 2).
```

The proof still needs a global potential: show that `C_high`, plus the
low-branch contraction from the previous section, dominates the positive excess
debt for every finite positive orbit segment and forces certificate descent.

## Branch-potential theorem target

The local low and high mechanisms have now been merged into one executable
credit ledger. The instrument is
[`branch_potential_analyzer.py`](branch_potential_analyzer.py), with result
file:

```text
experiments/results/branch_potential_20260702.json
```

Define:

```text
theta = log(2) / log(3)
R(n) = ceil(max(0, max_t(odd_steps_t - theta*t) - 0.999))

C_unit(n) = sum_high_ladders(v2(x+1)-2)
          + count_low_repeat_gates(x == -5 mod 64)
```

Full-population check:

```text
total starts checked:       1,013,816
uncertified:                        0
C_unit failures:                    0
C_rank failures:                    0
min C_unit surplus:                 0
max excess:                 42.591094525
high ladder credit total:      888,579
low repeat gates:              51,361
```

Class split:

```text
high-assisted descents:        281,754
low-direct descents:           703,125
low-repeat descents:            28,937
```

The exact theorem target is now:

```text
For every positive integer n > 1, C_unit(n) >= R(n) before first descent below
n, and the structural events counted by C_unit force enough actual even
insertion / height loss that this inequality yields a usable descent
certificate.
```

If proved, Theorem 5 in this file converts the descent certificate into the
full Collatz conjecture by strong induction. The current branch-potential run
is finite evidence only; it does not prove the universal inequality.

## Branch-potential stress target

The branch-potential claim was then attacked by
[`branch_potential_stress.py`](branch_potential_stress.py), result file:

```text
experiments/results/branch_potential_stress_20260702.json
```

The stress generator targets the exact obstruction shapes directly:

```text
low repeat spines:      x = 2^h q - 5, h <= 96
high ladder spines:     x = 2^a q - 1, a <= 96
near-boundary starts:   up to 160 bits
fresh frontier offsets: 128,384,640,896 mod stride 1024
random / biased high-bit starts
```

Stress result:

```text
total starts checked:       33,132
uncertified:                     0
C_unit failures:                 0
C_rank failures:                 0
max unit-credit deficit:         0
min C_unit surplus:              0
max excess:              59.051239429
```

The largest-excess stress case was a `160`-bit near-boundary start with
required credit `59` and `C_unit = 227`.

This does not change the theorem statement. It changes the falsification
status: the candidate inequality survived both inherited hard records and
adversarially generated low/high boundary families. A proof still needs to
replace the finite stress language with a universal grammar argument.

## Branch-prefix dominance target

The branch-potential claim was sharpened from terminal accounting to prefix
accounting by
[`branch_prefix_dominance_analyzer.py`](branch_prefix_dominance_analyzer.py),
result file:

```text
experiments/results/branch_prefix_dominance_20260702.json
```

At every prefix before first descent, the script checks:

```text
C_t >= R_t

R_t = ceil(max(0, max_{s<=t}(odd_steps_s - theta*s) - 0.999))

C_t = sum_{high ladder entries <= t}(v2(x+1)-2)
    + count_{low repeat entries <= t}(x == -5 mod 64)
```

Credit is assigned only when the structural event is visible at the current
state: high-ladder credit at `x = 2^a q - 1`, `a >= 3`, and low-repeat credit
at `x == -5 mod 64`.

Combined baseline plus stress result:

```text
total rows checked:          1,046,948
unique starts checked:       1,044,917
uncertified:                         0
prefix C_unit failures:              0
max prefix deficit:                  0
min prefix surplus:                  0
max prefix required credit:         59
```

The largest prefix requirement occurred on the same `160`-bit near-boundary
stress case:

```text
start:                  1461501637330902918203684832716283019655932542975
escape depth:           666
max excess:             59.051239429
max prefix required:    59
C_unit:                 227
```

This is a stronger theorem target than the terminal branch-potential
inequality: it forbids temporary debt. A proof would need to show that every
positive finite shadow receives visible structural credit before prefix excess
can exceed it, or else descends before credit is needed.

## Exact survivor-frontier prefix check

The prefix condition was then checked on the exact base-24 certificate survivor
frontier by
[`branch_prefix_frontier_exact.py`](branch_prefix_frontier_exact.py), result
file:

```text
experiments/results/branch_prefix_frontier_exact_d24_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_frontier_exact.py --base-depth 24 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_frontier_exact_d24_20260702.json --quiet
```

Result:

```text
frontier count:                 286,581
frontier fraction:              0.01708155870437622
positive residues checked:      286,581
uncertified:                          0
prefix C_unit failures:               0
max prefix deficit:                   0
min prefix surplus:                   0
max prefix required credit:          13
```

Class split:

```text
high-assisted descents:         286,575
low-repeat descents:                  6
low-direct descents:                  0
```

Every base-24 odd-count slice `16..24` had zero prefix failures. The largest
pressure case was `6,631,675`, with max excess `13.954462671`, max prefix
required credit `13`, and entry-visible `C_unit = 62`. The longest escape was
`13,421,671`, with certificate escape depth `287` and max prefix required
credit `10`.

This exact audit sharpens the missing theorem: prove a lift theorem showing
that prefix dominance on positive finite survivor shadows is preserved, or
receives new visible credit, as frontier depth increases.

## Multi-depth exact frontier lift audit

The first finite lift check is
[`branch_prefix_frontier_lift.py`](branch_prefix_frontier_lift.py), result
file:

```text
experiments/results/branch_prefix_frontier_lift_d24_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_frontier_lift.py --depths 24 25 26 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_frontier_lift_d24_d26_20260702.json --quiet
```

Aggregate result:

```text
depths checked:                 24, 25, 26
frontier rows checked:          1,897,117
uncertified:                            0
prefix C_unit failures:                 0
max prefix deficit:                     0
max prefix required credit:            14
```

Depth summaries:

```text
d=24:    286,581 live rows, max required 13, max escape 287
d=25:    573,162 live rows, max required 14, max escape 298
d=26:  1,037,374 live rows, max required 14, max escape 376
```

Lift bookkeeping:

```text
24 -> 25:
  orphan live children:             0
  live parents without children:    0
  children per parent:              2 children for 286,581 parents

25 -> 26:
  orphan live children:             0
  live parents without children:    0
  children per parent:              1 child for 108,950 parents
                                    2 children for 464,212 parents
```

This is not a proof, but it identifies the local induction lemma in exact
form: if `r` is a positive survivor residue at depth `d`, then each live child
at depth `d+1` must either preserve prefix dominance, receive visible branch
credit before fresh debt appears, or certify descent and leave the frontier.

## Parent-child lift transition split

The local lift was then opened by
[`branch_prefix_lift_transition.py`](branch_prefix_lift_transition.py), result
file:

```text
experiments/results/branch_prefix_lift_transition_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_lift_transition.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_lift_transition_d25_d26_20260702.json --quiet
```

The transition analyzer compares, for each live child,

```text
required_delta = child.max_prefix_required - parent.max_prefix_required
credit_delta   = child.C_unit - parent.C_unit
```

Exact `25 -> 26` transition result:

```text
live parents:                   573,162
live children:                1,037,374
pruned siblings:                108,950
orphan live children:                 0
live child prefix failures:           0
pruned sibling prefix failures:        0
```

Required-pressure split:

```text
nonincreasing required:         966,053
increased required:              71,321
  paid by new credit:            65,644
  partially paid by new credit:     278
  without new credit:             5,399
```

The important negative result is that a naive monotone total-credit inheritance
lemma is false as a proof strategy: some children have increased required
credit even while total child credit is lower than total parent credit. The
largest positive-pressure shortfall under this crude delta accounting is the
transition `12,132,095 -> 45,686,527`, where required credit increases by `1`
but total structural credit drops by `41`; nevertheless the child has zero
prefix deficit.

Thus the local proof target splits into:

```text
1. nonincreasing-pressure children;
2. fresh-credit children;
3. retimed-pressure children needing direct event-timing control.
```

All checked transitions satisfy prefix dominance; the remaining hard theorem is
the retimed-pressure case.

## Retimed-pressure timing audit

The retimed-pressure subcase was traced by
[`branch_prefix_retimed_pressure.py`](branch_prefix_retimed_pressure.py), result
file:

```text
experiments/results/branch_prefix_retimed_pressure_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_retimed_pressure.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_retimed_pressure_d25_d26_20260702.json --quiet
```

The script selects transitions satisfying:

```text
required_delta > 0
credit_delta < required_delta
```

and traces the child to the first prefix where `child R_t` exceeds the parent
maximum required credit.

Result:

```text
positive-pressure transitions:       71,321
retimed-pressure transitions:         5,677
retimed trace failures:                   0
max trace deficit:                       0
minimum threshold surplus:               2
maximum threshold surplus:              25
maximum threshold lag:                  19
```

Timing classes:

```text
prior high-ladder credit:            5,565
prior low-repeat credit:               112
```

Thus every retimed-pressure case in the exact `25 -> 26` lift was prepaid by
visible structural credit before above-parent pressure appeared. The next local
lemma is:

```text
Retimed-pressure lemma:
If a live child has required_delta > 0 but credit_delta < required_delta, then
before the first prefix with child R_t > parent R_max, the child has already
entered a high ladder or low-repeat gate whose accumulated credit leaves
positive surplus.
```

The finite audit gives minimum surplus `2`; the proof must derive this timing
from the lifted residue bit and the low/high alignment grammar.

## Retimed pressure-unit audit

The first retimed-pressure audit only checked the first child prefix where
required credit exceeded the parent maximum. The pressure-unit follow-up checks
every later above-parent required-credit increase in the same hard class.

Instrument:

```text
experiments/branch_prefix_pressure_units.py
```

Result:

```text
experiments/results/branch_prefix_pressure_units_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_pressure_units.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_pressure_units_d25_d26_20260702.json --quiet
```

Exact `25 -> 26` result:

```text
retimed-pressure transitions:              5,677
fully unit-certified retimed transitions:  5,677
transition failures:                           0
above-parent pressure units:               6,652
pressure-unit failures:                        0
tight pressure units:                          0
minimum pressure-unit surplus:                 2
maximum required above parent:                 5
maximum threshold lag:                        21
```

Timing classes over pressure units:

```text
prior high-ladder credit:                 6,535
prior low-repeat credit:                    117
```

Pressure-unit theorem target:

```text
For every live retimed child with required_delta > 0 and
credit_delta < required_delta, every prefix where child R_t exceeds the parent
maximum R has already received visible high-ladder or low-repeat credit, and
the accumulated credit remains strictly above the required pressure.
```

This is still finite evidence. Its value is that the local lift obligation is
now unit-local rather than stated only at the first threshold crossing.

## Retimed pressure-unit classifier

The classifier
[`branch_prefix_pressure_unit_classifier.py`](branch_prefix_pressure_unit_classifier.py)
mines symbolic structure from the same pressure units.

Result:

```text
experiments/results/branch_prefix_pressure_unit_classifier_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_pressure_unit_classifier.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_pressure_unit_classifier_d25_d26_20260702.json --quiet
```

Pure finite feature claims:

```text
all retimed transitions are upper-lift child:  true
all pressure units are upper-lift child:       true
all retimed children are high-assisted:        true
all pressure units have prior credit:          true
all pressure units have positive surplus:      true
```

Pressure-unit regimes:

```text
high_inside_active_ladder:  6,195
high_after_ladder_window:     340
low_repeat_prepaid:           117
```

For high-ladder pressure units, `lag_minus_align` ranges from `-10` to `3`.
The `340` post-ladder units are exactly the `+3` class. Thus the current local
proof target splits into active-ladder domination, low-repeat domination, and
a three-shortcut post-ladder carry bound.

## Post-ladder tail carry audit

The post-ladder tail analyzer
[`branch_prefix_post_ladder_tail.py`](branch_prefix_post_ladder_tail.py)
reconstructs the `340` post-ladder high units from the last high-ladder credit
state through the ladder terminal and the next three shortcut steps.

Result:

```text
experiments/results/branch_prefix_post_ladder_tail_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_post_ladder_tail.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_post_ladder_tail_d25_d26_20260702.json --quiet
```

Exact `25 -> 26` result:

```text
post-ladder tail units:          340
reconstruction failures:           0
terminal_v2 = 1:                 340
terminal mod 16 = 6:             340
post parity word EOO:            340
```

Elementary carry identity:

```text
y = 16r + 6
T(y)   = 8r + 3
T^2(y) = 12r + 5
T^3(y) = 18r + 8
```

So the tail pressure sublemma reduces to deriving the congruence
`3^a q - 1 == 6 mod 16` from the retimed upper-child hypotheses.

## Tail congruence audit

The congruence audit
[`branch_prefix_tail_congruence.py`](branch_prefix_tail_congruence.py) compares
the post-ladder tail congruence against every high-ladder pressure unit in the
same retimed class.

Result:

```text
experiments/results/branch_prefix_tail_congruence_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_congruence.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_tail_congruence_d25_d26_20260702.json --quiet
```

Exact findings:

```text
high-ladder pressure units:                 6,535
post-ladder tail units:                       340
tail units with terminal 6 mod 16:            340
active-ladder units with terminal 6 mod 16:   656
```

Equivalent cofactor rule:

```text
a mod 4 = 0: q mod 16 = 7    count  92
a mod 4 = 1: q mod 16 = 13   count  64
a mod 4 = 2: q mod 16 = 15   count  48
a mod 4 = 3: q mod 16 = 5    count 136
```

Thus terminal `6 mod 16` is necessary for the post-ladder tail but not
sufficient to classify it. The local proof must split active-ladder units from
post-ladder units first, then apply the congruence lemma only in the latter
case.

## Tail phase audit

The phase audit
[`branch_prefix_tail_phase.py`](branch_prefix_tail_phase.py) checks the missing
separator among terminal-`6 mod 16` high-ladder pressure units.

Result:

```text
experiments/results/branch_prefix_tail_phase_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_phase.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_tail_phase_d25_d26_20260702.json --quiet
```

The script replays the exact `25 -> 26` retimed class with 80-digit Decimal
arithmetic for

```text
odd_steps - (log 2 / log 3) * total_steps
```

and measures the terminal gap to the required-credit threshold that the pressure
event crosses.

Exact findings:

```text
terminal-6 high-ladder pressure units:       996
post-ladder tail with positive gap:          340
active ladder with nonpositive gap:          656
terminal-6 phase sign classifies tail:       true
all tail required_delta_from_terminal = 1:   true
```

Numerical separation:

```text
EOO gain:                    0.107210739285627688701419...
tail gap range:             +0.021768664287042106578247...
                             to +0.081541375001010298483449...
active terminal-6 gap range: -2.025669364284617390217970...
                             to -0.025669364284617390217970...
```

This sharpens the proof obligation.  Terminal `6 mod 16` supplies the residue
and parity-word part; positive terminal phase supplies the timing part.  The
remaining theorem target is to derive this phase sign from the lifted upper
child and frontier hypotheses, not from enumeration.

## Tail phase spectrum audit

The phase-spectrum audit
[`branch_prefix_tail_phase_spectrum.py`](branch_prefix_tail_phase_spectrum.py)
checks where the max excess used in the terminal phase gap comes from.

Result:

```text
experiments/results/branch_prefix_tail_phase_spectrum_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_phase_spectrum.py --parent-depth 25 --max-depth 1024 --top-n 12 --hist-top-n 32 --output experiments/results/branch_prefix_tail_phase_spectrum_d25_d26_20260702.json --quiet
```

Exact findings:

```text
terminal-6 high-ladder pressure units: 996
phase sign still classifies tail:      true
source misses:                         0
active max source at terminal:       656 / 656
tail max source at terminal:         334 / 340
tail max source eight steps earlier:   6 / 340
```

The tail-positive phase side collapses to four integer-linear forms in
`theta = log(2)/log(3)`:

```text
27*theta - 17.001 = 0.034103346429350801687232...  count 275
35*theta - 22.001 = 0.081541375001010298483449...  count  57
46*theta - 29.001 = 0.021768664287042106578247...  count   5
54*theta - 34.001 = 0.069206692858701603374464...  count   3
```

Thus the local phase problem is mostly terminal-local but has a six-case memory
subcase.  A proof must account for that earlier max-source rather than silently
replace `max_excess_at_terminal` with the terminal current excess in all cases.

## Tail memory-case extraction

The memory-case extractor
[`branch_prefix_tail_memory_cases.py`](branch_prefix_tail_memory_cases.py)
isolates the six non-terminal max-source cases.

Result:

```text
experiments/results/branch_prefix_tail_memory_cases_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_memory_cases.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_tail_memory_cases_d25_d26_20260702.json --quiet
```

Exact findings:

```text
terminal-6 post-ladder tail units: 340
memory-tail cases:                   6
source lag to terminal:              8 in all cases
terminal-to-event word:              EOO in all cases
source-to-terminal odd count:         5 in all cases
```

The two source-to-terminal words are:

```text
EEOOEOOO: 5
EEOEOOOO: 1
```

Both pass through the low-repeat residue `59 mod 64`.  All six share:

```text
max-source gap:       27*theta - 17.001
terminal-current gap: 35*theta - 22.001
memory drop:           8*theta - 5
```

This changes the proof target in a good way: the memory subcase is not an
unstructured exception. It is a two-word local grammar, coupled to the
low-repeat residue class, that still crosses the post-terminal `EOO` tail with
positive margin.

## Tail memory word-map lift

The word-map analyzer
[`branch_prefix_tail_memory_word_maps.py`](branch_prefix_tail_memory_word_maps.py)
turns the two memory words into exact affine cylinders and checks the lifted
residue paths of the six records.

Result:

```text
experiments/results/branch_prefix_tail_memory_word_maps_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_memory_word_maps.py --memory-result experiments/results/branch_prefix_tail_memory_cases_d25_d26_20260702.json --output experiments/results/branch_prefix_tail_memory_word_maps_d25_d26_20260702.json --quiet
```

Exact affine maps:

```text
EEOOEOOO: T^8(n) = (243*n + 1148)/256, source n == 108 mod 256
EEOEOOOO: T^8(n) = (243*n + 1364)/256, source n == 164 mod 256
```

The honest obstruction is subtler than the previous wording suggested.  The
raw modulo-`256` parity cylinders have representative paths:

```text
EEOOEOOO: 44 -> 54 -> 27 -> 41 -> 62 -> 31 -> 47 -> 7 -> 43
EEOEOOOO: 36 -> 18 -> 41 -> 62 -> 31 -> 47 -> 7 -> 43 -> 33
```

These paths do not pass through `59 mod 64`.  The `59 mod 64` bridge appears
only after lifting the source class to modulo `2^(8+6) = 16384`:

```text
EEOOEOOO, source n == 6508 mod 16384:
  44 -> 54 -> 27 -> 9 -> 14 -> 39 -> 59 -> 25 -> 38

EEOOEOOO, source n == 14700 mod 16384:
  44 -> 54 -> 27 -> 9 -> 14 -> 39 -> 59 -> 25 -> 6

EEOEOOOO, source n == 10148 mod 16384:
  36 -> 18 -> 41 -> 30 -> 47 -> 39 -> 59 -> 25 -> 38
```

Pure finite checks:

```text
all words length 8 and odd count 5:           true
raw mod-256 word paths do not force 59 mod64: true
memory lifted paths pass 59 mod64:            true
memory lifted paths have preterminal 25:      true
all memory records affine compatible:         true
all memory paths match records:               true
```

Thus the local memory lemma cannot be just "one of two parity words occurs."
It must prove the lifted source residue classes. Once those classes are known,
the exact affine maps force the recorded low-repeat bridge into the
post-ladder tail.

## Tail memory minimal-lift solver

The lift solver
[`branch_prefix_tail_memory_lift_solver.py`](branch_prefix_tail_memory_lift_solver.py)
checks which low bits are actually needed to force the memory bridge.

Result:

```text
experiments/results/branch_prefix_tail_memory_lift_solver_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_memory_lift_solver.py --memory-result experiments/results/branch_prefix_tail_memory_cases_d25_d26_20260702.json --output experiments/results/branch_prefix_tail_memory_lift_solver_d25_d26_20260702.json --quiet
```

Write a source as `n = r + 256m`, where `r` is the length-8 parity-cylinder
residue.  The bridge `59 mod 64 -> 25 mod 64` is first forced at five extra
bits beyond the word:

```text
EEOOEOOO:
  r = 108
  n == 6508 mod 8192
  m == 25 mod 32

EEOEOOOO:
  r = 164
  n == 1956 mod 8192
  m == 7 mod 32
```

Pure checks:

```text
all observed full lifts are bridge classes:         true
all observed project to forced bridge mod 8192:     true
bridge first forced at five extra bits for both:    true
there is exactly one unobserved bridge full lift:   true
```

The full modulo-`16384` lift chooses the terminal residue:

```text
EEOOEOOO:
  6508  mod 16384 -> terminal 38, observed 3 times
  14700 mod 16384 -> terminal 6,  observed 2 times

EEOEOOOO:
  1956  mod 16384 -> terminal 6,  observed 0 times
  10148 mod 16384 -> terminal 38, observed 1 time
```

Thus the memory proof target splits into a modulo-`8192` bridge lemma and a
terminal-bit refinement.  The unobserved `EEOEOOOO` class `1956 mod 16384` is
a local ghost: a proof must either rule it out from the upper-child frontier
hypotheses or show it is harmless under the same pressure accounting.

## Tail ghost-class audit

The ghost-class audit
[`branch_prefix_tail_ghost_class.py`](branch_prefix_tail_ghost_class.py)
checks the full post-ladder tail population, not just the six memory records.

Result:

```text
experiments/results/branch_prefix_tail_ghost_class_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_ghost_class.py --parent-depth 25 --max-depth 1024 --top-n 12 --hist-top-n 40 --output experiments/results/branch_prefix_tail_ghost_class_d25_d26_20260702.json --quiet
```

Exact counts:

```text
post-ladder tail units:       340
terminal ghost signature:      25
ghost memory sources:           0
source lag 0:                 334
source lag 8:                   6
```

Here the terminal ghost signature is:

```text
align a = 4
q == 23 mod 64
terminal == 6 mod 64
```

Pure checks:

```text
all sources found:                         true
terminal signature occurs:                 true
ghost memory source absent:                true
all nonterminal sources have lag 8:        true
all nonterminal sources are memory words:  true
all post-ladder tail words are EOO:        true
```

Thus the ghost terminal bit is real but terminal-local. Every one of the `25`
ghost-signature cases has the terminal itself as the max source, so it is
covered by the terminal-local phase separator. The nonterminal branch remains
exactly the six lag-8 memory cases:

```text
EEOOEOOO: 5
EEOEOOOO: 1
```

The local theorem target should therefore be a dichotomy, not a ghost
exclusion: terminal-local tails are handled by positive terminal phase; if the
tail max is nonterminal, it must be one of the two memory words and the ghost
full lift `1956 mod 16384` does not occur.

## Tail dichotomy classifier

The dichotomy classifier
[`branch_prefix_tail_dichotomy_classifier.py`](branch_prefix_tail_dichotomy_classifier.py)
mines features separating the `334` terminal-local post-ladder tails from the
six lag-8 memory tails.

Result:

```text
experiments/results/branch_prefix_tail_dichotomy_classifier_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_dichotomy_classifier.py --parent-depth 25 --max-depth 1024 --top-n 12 --max-feature-set-size 3 --output experiments/results/branch_prefix_tail_dichotomy_classifier_d25_d26_20260702.json --quiet
```

Population:

```text
terminal-local tails: 334
memory-lag-8 tails:     6
```

Pure checks:

```text
all sources found:                                      true
population is 340:                                      true
six memory records:                                     true
memory sources are two known words:                     true
has pure feature set:                                   true
has memory-pure feature set:                            true
no terminal/event feature set of searched size is pure: true
no terminal/event feature set is memory-pure:           true
```

Negative result: terminal/event-side features up to triples do not separate the
dichotomy, and even the hand-picked six-feature bucket

```text
terminal_step, event_step, align, q_mod64, terminal_mod64, terminal_current_gap
```

has three mixed memory buckets:

```text
35|38|3|37|38|0.081541375001010298483449 : memory 3, terminal-local 8
35|38|3|5 |6 |0.081541375001010298483449 : memory 2, terminal-local 3
35|38|4|55|38|0.081541375001010298483449 : memory 1, terminal-local 6
```

Positive finite separator: child low bits plus timing do separate. For example,

```text
child mod 4096, event_step
```

is pure, with memory buckets:

```text
1471|38 : memory 1
1895|38 : memory 2
2495|38 : memory 1
3791|38 : memory 1
 751|38 : memory 1
```

Equivalent pure separators use `child mod 4096` with `terminal_step`,
`terminal_current_gap`, or `terminal_current_form`.  But `child mod 4096` alone
is not enough; the same residues have terminal-local cases too. Direct checks
crossing the smaller child moduli `64, 128, 256, 512, 1024, 2048` with those
same four timing features all remain mixed; `2048` still covers only three of
the six memory records in pure buckets and leaves two mixed buckets. In this
finite search, `4096` is the first tested child modulus where timing gives a
pure separator.

Thus the lag-8 memory tail is not a terminal-phase-only phenomenon. It is a
child-residue-plus-timing phenomenon, matching the lift-lemma interpretation.

## Tail child-lift stratifier

The follow-on stratifier
`experiments/branch_prefix_tail_child_lift_stratifier.py` explains exactly why
`2048` is insufficient and why the next child bit works in the finite
`25 -> 26` lift. It recomputes the same `340` post-ladder tail cases and
compares `child mod 2048 + event_step` to `child mod 4096 + event_step`.

At `child mod 2048 + event_step`, the memory-bearing lower buckets are:

```text
1471|38 : memory 1
 447|38 : memory 1
 751|38 : memory 1
1743|38 : memory 1, terminal-local 2
1895|38 : memory 2, terminal-local 1
```

The only mixed lower buckets are therefore `1743|38` and `1895|38`. Passing to
modulo `4096` splits them purely:

```text
lower 1743|38:
  child mod 4096 = 1743, lift bit 0 : terminal-local 2
  child mod 4096 = 3791, lift bit 1 : memory 1

lower 1895|38:
  child mod 4096 = 1895, lift bit 0 : memory 2
  child mod 4096 = 3943, lift bit 1 : terminal-local 1
```

Thus the `4096` separator is not a black-box mined classifier. In this finite
lift it is equivalent to a two-bucket lift-bit rule, plus the three already-pure
lower buckets. The next proof obligation is to derive that lift-bit assignment
from the upper-child frontier hypotheses.

## Tail lift-bit witness

The witness extractor `experiments/branch_prefix_tail_lift_bit_witness.py`
distills the child-lift stratifier to a single mixed lower-phase bucket. The
following two records have identical lower residue and visible terminal phase:

```text
child mod 2048:          1743
terminal_step:             35
event_step:                38
align:                      3
q mod 64:                   5
terminal mod 64:            6
terminal_current_gap:       0.081541375001010298483449
```

but opposite labels:

```text
memory_lag_8:
  child mod 4096 = 3791, lift bit 1, source word EEOOEOOO

terminal_local:
  child mod 4096 = 1743, lift bit 0
```

So the lower residue plus terminal phase cannot prove the branch. The next
child lift bit is necessary in the finite obstruction, and any global proof
route through this local tail must account for that bit rather than hiding it in
enumeration.
