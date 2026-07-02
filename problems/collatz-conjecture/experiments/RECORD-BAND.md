# Record Band — an explicit ceiling on every possible Terras violation

_Created: 2026-07-01. Companion to `collatz_record_band.py`; direct sequel to `THRESHOLD-ENVELOPE.md`._
_Status: the lemma and ceiling are **Proved** (self-contained; exhaustively machine-verified where finite); the numerical floors are exact computations from the certified continued fraction plus the `10^9` scan. Nothing here proves Terras' conjecture or the Collatz conjecture; the exact open residue is stated at the end._

## Where this picks up

`THRESHOLD-ENVELOPE.md` proved that any violation of Terras' coefficient stopping time conjecture (`sigma(n) > tau(n)`, `n >= 2`) must satisfy `n < 2^tau(n)`: the violator is the residue of its own certified class, whose parity word is **alive** (supercritical, `3^{o(j)} >= 2^j`) at every proper prefix. This lab answers: *how large can such an `n` be?* The answer is an explicit, provable, surprisingly small ceiling — because aliveness crushes the intercept.

## Lemma (alive intercept bound — proved, exhaustively verified)

If a length-`d` word is alive at all proper prefixes, with odd steps at positions `s_1 < ... < s_o`, then aliveness pins each odd step early — `3^j >= 2^{s_j}` gives `2^{s_j - 1} <= 3^j / 2` — so

```text
c(w) = sum_{j=1}^{o} 3^{o-j} 2^{s_j - 1}  <=  sum_{j=1}^{o} 3^{o-j} 3^j / 2  =  o 3^o / 2.
```

Compare the generic (odd-steps-last) maximum `2^{d-o}(3^o - 2^o) ~ (3/2)^o 2^d`: aliveness improves the intercept bound by the exponential factor `~2^d/3^o`. Exhaustive check over every alive word to depth 18: bound holds, worst ratio `c / (o 3^o / 2) = 0.667`, so it is tight within a factor 1.5.

## Theorem (violation ceiling — proved)

A Terras violation `n` with `tau(n) = d` and odd count `o` is trapped in its own alive class: `n <= x* = c/(2^d - 3^o)`. Certificates end at the first subcritical depth, so `d = ceil(o log2 3)` and `delta := d - o log2 3` lies in `(0, 1)`. Then `2^d - 3^o = 3^o(2^delta - 1) >= 3^o delta ln 2`, and the Lemma gives

```text
n  <=  X(o) := o / (2 ln2 * delta(o)).
```

`delta(o) >= ||o log2 3||`, and by Lagrange's best-approximation theorem, `||o log2 3|| >= ||q_k log2 3||` for `q_k <= o < q_{k+1}` (convergent denominators). Every `||q_k log2 3||` is bounded below exactly by the in-repo interval-certified continued fraction. The ceiling is validated against the exact envelope DP: at the spike depths 65/149/305/485 the bound `X` sits 1.0–1.1 bits above the exact maximum `x*` — it is essentially sharp.

## The numbers (exact, `results/record_band_theorem.json`)

Per convergent band, the maximum possible size of a Terras violation:

| band `q_k <= o < q_{k+1}` | ceiling `log2 X` | gamma floor (beyond the `10^9` scan) |
|---|---:|---:|
| 665 – 15,601 | 27.41 | (below scan floor — excluded) |
| 15,601 – 31,867 | 29.71 | (below scan floor — excluded) |
| **31,867 – 79,335** | **32.35** | **1,530.6** |
| 79,335 – 111,202 | 33.82 | 3,698.3 |
| 111,202 – 190,537 | 34.62 | 5,035.8 |
| 190,537 – 10,590,737 | 46.22 | 6,425.4 |
| 10,590,737 – 10,781,274 | 46.55 | 357,147.3 |

Combined with the `10^9` scan (`tau = sigma` for all `n <= 10^9`, zero exceptions):

> **Theorem (record-band floor).** Any violation of Terras' coefficient stopping time conjecture satisfies ALL of:
>
> - `o >= 31,867` odd steps and `tau >= 50,509` total steps in its certificate;
> - `n <= X(o)` — e.g. `n <= 2^{32.4}` in the first admissible band;
> - `gamma(n) = tau(n)/log2(n) >= 1,530.6`, with the floor rising along the convergent ladder (`3,698` in the next band, `357,147` past `q = 10^7`, unboundedly thereafter).
>
> For calibration: the Borel–Cantelli ceiling for `gamma` under the random model is `1/(1 - H(theta)) = 19.982...`; the all-time measured record is `14.503` (`n = 63,728,127`). A Terras violation must therefore be a certificate-depth record integer **at least 76x beyond the extreme-value ceiling** — and the requirement grows without bound.

## Corollary (cycle minima — conditional on the `2^71` verification)

A nontrivial cycle minimum `m` has `sigma(m) = infinity`, `tau(m) < infinity`, hence is trapped (`m <= x*`), hence obeys the same ceiling. Since `m > 2^71` (Bařina), the first band whose ceiling clears `2^71` gives, exactly:

```text
o(certificate of m) >= 47,805,107,717        tau(m) >= 75,769,303,075
gamma(m) = tau(m)/log2(m) >= 1.05 x 10^9.
```

Two remarks. (1) This is an *independent second derivation* of the `~5 x 10^10` cycle wall: the alive-intercept route lands in the same convergent band (`q = 6.5 x 10^10 / 1.375 x 10^11`) as the product-formula routes (`FRONTIER-GEOMETRY.md` Theorem 6: `4.95 x 10^10`; `CYCLE-BOUND-LAB.md`: `6.55 x 10^10`) — three distinct arguments, one Diophantine wall. (2) The `gamma >= 10^9` form is new phrasing with content: a cycle minimum would have to violate the extreme-value law of certificate depths by a factor of fifty million.

## Why this matters for the program

1. **Terras' conjecture now has a quantified impossibility margin.** After Sessions 1–3 the only possible violations were `q = 0` self-traps; now they must simultaneously be (a) larger than `10^9`, (b) smaller than `~2^{32}` — a window of width `~4.3x` in log scale for the first band — and (c) certificate-record integers with `gamma > 1,500`, two orders of magnitude beyond the ceiling that governs every measured record. The candidate set per band is finite and *conceptually* enumerable: integers in `(10^9, 2^{32.4}]` whose first `~50,000` steps are supercritical. Under the exact frontier density `F(50,509) ~ 2^{-2,510}`, the expected number of candidates in the first band is `~2^{32} x 2^{-2,510} ~ 10^{-746}`.
2. **The gap between "measured" and "proved" is now purely the distributional-to-pointwise gap.** Everything short of "no integer beats the extreme-value law by 76x" is proved. The remaining conspiracy is a single integer threading a `2^{-2,510}`-density Cantor set while staying below `2^{32.4}` — exactly the kind of statement the invariance barrier (`SIBLING-CONTROL.md`) says cannot be finished with word statistics alone.
3. **The sibling cross-check.** For `3n-1` the intercept is *negative* (`sign(c) = eps`), so subcritical classes have `x* < 0` and trapping below `x*` is impossible — consistent with the `sigma <= tau` theorem there. The conspiracies `3n-1` actually realizes live on the other side: its cycle minima `1, 5, 17` are supercritical fixed points (`x = c/(2^d - 3^o)` with both factors negative), i.e. frontier residents. The trap mechanism bounded by this lab is genuinely `+1`-specific — once more, the mathematics lives on the `eps`-sensitive side of the barrier.

## What remains open (exactly)

- A Terras violation inside the proved window (`n > 10^9`, `n <= X(o)`, `gamma > 1,530`): not excluded, only measured absent and heuristically `10^{-746}`-improbable per band. Proving emptiness needs pointwise control this method cannot give.
- Divergence (frontier residents) and cycles beyond the floors: untouched here beyond the corollary.
- Scope: floors certified for `o` up to the CF table range (`~10^{157}`); `--digits` extends it.

## Reproduce

```powershell
python experiments/collatz_record_band.py selftest
python experiments/collatz_record_band.py theorem --digits 320 --out experiments/results/record_band_theorem.json
python experiments/collatz_record_band.py ceiling --digits 320 --n-floors 1000000000,2361183241434822606848 --max-bands 24
```

Self-test (5 checks, all passing): the alive-intercept lemma exhaustively over every alive word to depth 18 (with tightness ratio); ceiling-dominates-envelope at the four spike depths against the exact DP; Lagrange band bounds on sampled `o`; a direct self-trap rescan of all `n <= 2x10^6`; and `x* <= X` at every reported depth `<= 400`.
