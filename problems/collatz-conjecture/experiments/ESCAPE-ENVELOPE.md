# Escape Envelope — quantifying the missing uniform escape theorem

_Created: 2026-07-01. Status: proved density bound + measured envelope law, not a proof of Collatz._

The certificate-frontier program ends every prior instrument with the same
sentence: *the missing theorem is a uniform positive-integer escape principle*.
This lab makes that missing theorem quantitative. It (a) proves an
unconditional exponential-thinness bound for the frontier inside the repo,
(b) derives the conjecturally sharp envelope constant, and (c) tests the
resulting first-moment law against exact full-frontier records at seven base
depths.

## Runnable artifact

```powershell
python experiments/escape_envelope_analyzer.py --self-test --max-dp-depth 2048 --dp-report-every 64 --bound-check-every 32 --base-depths 14,16,18,20,22,24 --max-escape-depth 896 --json-out experiments/results/escape_envelope_2048.json
```

Self-test layers (all passed 2026-07-01): brute-force integer enumeration
matches the DP at depths 1–14; the Terras parity-word bijection is verified
exhaustively; the DP reproduces the anchors `S(20) = 27,328`,
`S(24) = 286,581`, `S(28) = 3,524,586` from the residue lab. Full run: 3.1 s.

## Layer 1 — proved bound (Theorem 7 in CERTIFICATE-FRONTIER-THEOREMS.md)

Let `S(d)` be the number of depth-`d` survivor prefixes and
`theta = log_3 2 = 0.6309297535714574...`. Then, unconditionally,

```text
S(d) <= sum_{k >= o_min(d)} C(d, k) <= 2^(d * H(theta)),
```

so the density of residues mod `2^d` left uncertified at depth `d` is at most

```text
2^(-(1 - H(theta)) * d),    1 - H(theta) = 0.0500444728116693651860994...
```

The first inequality was re-verified by exact integer comparison at 65 grid
depths through `d = 2048` (minimum slack `0.0` bits, equality at `d = 1`);
the entropy step held with slack `>= 0.9499` bits everywhere.

## Layer 2 — exact survivor mass through depth 2048

The exact DP extends the old depth-128 scan by a factor of 16:

| Depth `d` | `-log2(fraction)` | Effective rate (bits/step) |
|---:|---:|---:|
| 128 | 13.807 | 0.107866 |
| 256 | 21.542 | 0.084147 |
| 512 | 35.849 | 0.070018 |
| 1024 | 62.910 | 0.061436 |
| 2048 | 115.605 | 0.056448 |

The effective rate approaches the proved asymptotic rate `0.050044` from
above. The excess `rate(d) - 0.050044` fits `(a*log2(d) + c)/d` with
`a ≈ 1.44`, consistent with the classical ballot-problem polynomial factor
`d^(-3/2)` on top of the exponential — i.e. the survivor mass behaves like
`d^(-3/2) * 2^(-0.050044 d)`, exactly what a bridge-above-a-line model
predicts.

## Layer 3 — the envelope constant

The first-moment envelope for the worst certificate depth over `b`-bit starts
is the depth where the expected survivor count `2^b * S(d)/2^d` crosses 1:

```text
D_1(b) = max { d : b + log2(S(d)) - d >= 0 },
```

with asymptotic slope

```text
c* = 1 / (1 - H(theta)) = 19.9822266839190301...
```

`c*` is the first-descent analogue of the Lagarias–Weiss total-stopping-time
constant `41.677647`. It is the conjecturally sharp constant of the missing
uniform escape theorem: **any** proved bound of the form
`D(b) <= f(b)` for a computable `f` would settle the divergence half (and via
the descent equivalence, all) of Collatz; the random model says the sharp
truth is `f(b) ~ 19.98 b`.

## Layer 4 — exact records vs the first-moment law

Exact full-frontier escape records (every representative certified; base 28
from the earlier logged run):

| Base bits `b` | Frontier size | Record `D(b)` | `D(b)/b` | Crossing `D_1(b)` | `D(b) - D_1(b)` | 0.01-bracket | Worst start |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 14 | 734 | 105 | 7.50 | 129 | -24 | 239 | 10,087 |
| 16 | 2,114 | 135 | 8.44 | 161 | -26 | 275 | 35,655 |
| 18 | 7,495 | 135 | 7.50 | 194 | -59 | 310 | 35,655 |
| 20 | 27,328 | 183 | 9.15 | 229 | -46 | 345 | 1,027,431 |
| 22 | 93,222 | 224 | 10.18 | 263 | -39 | 381 | 1,126,015 |
| 24 | 286,581 | 287 | 11.96 | 297 | -10 | 416 | 13,421,671 |
| 28 | 3,524,586 | 395 | 14.11 | 369 | +26 | 491 | 217,740,015 |

Predicted crossings for reference scales: `D_1(32) = 442`, `D_1(48) = 741`,
`D_1(64) = 1,046`, `D_1(71) = 1,180`.

Observations:

1. **The alive curves match the free-coin word model to within hundredths of
   a bit through the bulk.** At base 24 the deviation
   `log2(alive) - (b + log2 fraction)` is `-0.010, -0.018, -0.041, +0.024,
   +0.011` at depths 48–144. Terras equidistribution effectively persists on
   the hard frontier far beyond the matched depth — there is no measurable
   heavy integer tail, and no measurable extra descent pressure either.
2. **The record deficit `D(b) - D_1(b)` climbs from -24 to +26 across
   `b = 14..28`,** i.e. records fluctuate around the first-moment crossing
   exactly as a max-of-thin-tail statistic should (the `+26` at `b = 28` is
   far inside the 0.01-expected bracket 491). The envelope law survives its
   first seven exact tests.
3. **The record slope `D(b)/b` (7.5 → 14.1) is still far below `c* = 19.98`,**
   and the crossing slope `D_1(b)/b` (9.2 → 13.2, then 16.3 at `b = 64`)
   approaches `c*` only logarithmically — the same slow-climb phenomenon as
   the Lagarias–Weiss gamma records (measured 24.7 vs limsup 41.68). Finite
   verification can never watch the envelope saturate.
4. **Known extremal integers sit at roughly half the predicted envelope.**
   The 62-bit beam-search champion certifies at 509 vs `D_1(62) ≈ 1,010`;
   the 71-bit Bařina path-record start certifies at 738 vs `D_1(71) = 1,180`.
   If the envelope law is right, the hardest 64-bit starts are roughly twice
   as certificate-deep as anything currently known — a concrete gap for
   `frontier_beam_search.py` to attack.

## Layer 5 — two-sided mass theorem (proved)

The upper bound of Layer 1 now has a matching elementary lower bound
(Theorem 8 in CERTIFICATE-FRONTIER-THEOREMS.md), via a cycle-lemma argument:
the drift path `P_j = o(j) ln 3 - j ln 2` has pairwise-distinct partial sums
(no relation `3^a = 2^b`), so every cyclic class of words with total drift
`3^o > 2^d` contains at least one rotation that stays strictly positive —
a survivor. Hence

```text
C(d, o_min(d)) / d  <=  S(d)  <=  2^(d * H(theta)),
```

and for `d >= 20` the closed form `2^(d*H(theta)) / (3 d^2) <= S(d)`. The
survivor mass is `2^(d*H(theta) + O(log d))` **unconditionally**, so the
first-moment crossing obeys `D_1(b) = c* b + O(log b)` as a theorem, not a
heuristic. Verified in exact integers at 65 grid depths through 2048; at
`d = 2048` the exact floor–actual–ceiling stack reads
`1928.07 <= 1932.40 <= 1945.47` bits.

## Layer 6 — minimal-survivor duality (measured)

Inverting the record function: let `m` be the smallest integer whose
certificate depth reaches `D`. Equidistribution of survivor representatives
predicts `m ~ 2^D / S(D)`, i.e. the duality product `m * S(D)/2^D` should be
order one. At the six exhaustively-known record pairs:

| Record depth `D` | Record integer `m` | `log2 m` | `-log2 frac(D)` | Duality product |
|---:|---:|---:|---:|---:|
| 105 | 10,087 | 13.30 | 12.33 | 1.97 |
| 135 | 35,655 | 15.12 | 14.32 | 1.74 |
| 183 | 1,027,431 | 19.97 | 17.25 | 6.61 |
| 224 | 1,126,015 | 20.10 | 19.73 | 1.29 |
| 287 | 13,421,671 | 23.68 | 23.41 | 1.21 |
| 395 | 217,740,015 | 27.70 | 29.43 | 0.30 |

The product stays within `[0.30, 6.61]` while the density itself falls
through seventeen binary orders of magnitude. This is the equidistribution
statement the envelope conjecture needs, measured exactly where it matters.
(The 62-bit beam candidate and 71-bit Bařina start are excluded: those
searches are not exhaustive below, so they bound `m` only from above.)

## What would falsify the envelope

A single positive integer with certificate depth `> 20.0 * bit_length + O(log)`
— e.g. a 32-bit start surviving past depth ~700, or any start with
`D/b > 20` at large `b` — would break the first-moment law, contradict the
random model in its extreme tail, and mark the exact place where integers
refuse measure-typical behavior. The analyzer's deviation samples are the
early-warning instrument: a systematic positive drift of the alive-curve
deviation with depth would be visible long before any record breaks the
envelope.

## Honest interpretation

- The **proved** content is Layers 1 and 5: the uncertified density is
  `2^(-(1-H(theta))d + O(log d))` — upper bound by entropy (Theorem 7), lower
  bound by the cycle lemma (Theorem 8) — unconditional, self-contained in the
  theorems file, verified against exact counts. The Terras-class upper bound
  is not new to the literature; the point is the two-sided pin with explicit
  constants, machine-checked inside the repo, which promotes the crossing law
  `D_1(b) = c* b + O(log b)` from heuristic to theorem.
- The **measured** content (Layers 2–4, 6) says the missing uniform escape
  theorem has a precise conjectural form: `D(b) = D_1(b) + fluctuations`,
  slope `c* = 19.982`. After Theorem 8, exactly one ingredient of that
  sentence remains unproved: *representative equidistribution* — that the
  integer representatives of survivor classes spread regularly enough for
  the minimal survivor to track `2^d / S(d)`. Layer 6 measures that very
  quantity and finds it order-one across the entire exhaustively-known
  range. Everything computable agrees with it; nothing computable can prove
  it.
- The all-odd 2-adic boundary point `-1` still survives every depth. The
  envelope conjecture is exactly the statement that positive integers cannot
  imitate it for more than `~20` steps per bit — positivity and finiteness
  as a quantitative repulsion law, which is what every instrument in this
  directory has been circling.
