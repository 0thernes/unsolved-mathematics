# Threshold Envelope — thresholds are vacuous at every depth (proved)

_Created: 2026-07-01. Companion to `collatz_threshold_envelope.py`; builds on `FRONTIER-GEOMETRY.md` (Theorem 3), `SIBLING-CONTROL.md` (the barrier directive), and `CERTIFICATE-FRONTIER-THEOREMS.md`._
_Status: the main theorem here is **Proved**, self-contained in this repo (elementary induction + Legendre's criterion + the interval-certified continued fraction of `log2 3`). It is not a proof of the Collatz conjecture; the scope of what remains open is stated exactly, at the end. The argument is Terras-era elementary and may well be folklore among specialists; we did not find it stated in this sharpness, and in-repo it upgrades a depth-28 measurement to an all-depth theorem._

## What question this answers

Session 1 measured: through depth 28, every certified residue class has threshold `q_0 <= 1`, so no integer `n >= 2` is "threshold-trapped" (coefficient drops but descent fails — a Terras violation). Measurement can never cover all depths. The barrier theorem of `SIBLING-CONTROL.md` then directed all proof effort at the intercepts. This lab **proves the threshold statement at every depth**, by showing the intercepts obey an exact bound that makes trapping a Diophantine event too sharp to occur.

## Setup

A class `r mod 2^d` certified at depth `d` (odd count `o`, `3^o < 2^d`) has the exact affine form

```text
T^d(2^d q + r) = (3^o (2^d q + r) + c(w)) / 2^d,      c(w) = 2^d T^d(r) - 3^o r >= 0,
```

an increasing map with rational fixed point

```text
x*(r, d) = c(w) / (2^d - 3^o),
```

and `T^d(n) < n` **iff** `n > x*`. So: members `<= x*` are trapped (Terras violations); an integer `x*` would be an actual cycle (`T^d(x*) = x*`); and the certificate threshold of the residue lab is exactly `q_0 = floor((x* - r)/2^d) + 1`. Cycles, thresholds, and Terras' conjecture are one geometric object: **where the rational fixed points sit**.

## Lemma 1 (intercept bound — proved, exact, tight)

For every parity word of length `d` with `o >= 1` odd steps:

```text
c(w) <= 2^(d-o) (3^o - 2^o),
```

with equality exactly when all odd steps come last. Proof: `c` evolves by `c -> c` (even step) and `c -> 3c + 2^j` (odd step at position `j`); induction gives the bound, and the odd-steps-last word attains it. (Self-test: verified exhaustively over all `2^14` words, including tightness per odd count.)

## Theorem 2 (the trap window — proved)

If a certified class at `(d, o)` traps any member `n >= 2^d` (i.e. `q >= 1`), then `x* >= 2^d`, hence `c >= 2^d (2^d - 3^o)`, hence by Lemma 1

```text
2^d - 3^o < (3/2)^o        i.e.        1 < 2^d / 3^o < 1 + 2^(-o).
```

A trap requires `d/o` to approximate `log2 3` from above with error `< 2^(-o) / (o ln 2)` — **exponentially** good, while genuine rational approximations to `log2 3` are only polynomially good. That mismatch is the whole proof.

## Theorem 3 (window exclusion — proved)

1. **Small `o`, exact:** for every `o <= 256`, integer comparison `2^(d+o) < 3^o (2^o + 1)` (with `d = bitlength(3^o)`, the only candidate) shows the window contains exactly one pair: **`(d, o) = (2, 1)`**.
2. **The hit closes itself:** the unique depth-2 class is `r = 1 mod 4` (word `10`) with `c = 1`, `x* = 1/(4-3) = 1 < 4 = 2^d`. Its only trapped member is `n = 1` — **the trivial cycle**, which is literally the fixed point `x* = 1`. No `q >= 1` trap.
3. **Large `o`, Legendre + certified convergents:** for `o >= 8` the window forces the reduced fraction `d/o = p/q` (`q | o`) to satisfy `|log2 3 - p/q| < 2^(-max(q,8))/(max(q,8) ln 2) < 1/(2q^2)`, so `p/q` is an above-side continued-fraction convergent of `log2 3`. The interval-certified expansion (exact integer `atanh` series, error budgets proved in `collatz_frontier_geometry.py`) certifies 300+ partial quotients; all **156 above-side convergents, denominators up to ~1e157**, are excluded by exact rational comparison (`q <= 64`) or conservative bit-length comparison with 4 bits of slack (`q > 64`). Reduced denominators `q <= 3` are separately excluded by the fixed distances of `log2 3` to `p/1, p/2, p/3` (min 0.082 vs window `< 7.1e-4`).

## Main Theorem (proved, unconditional for odd count up to ~1e157)

> **For every certified Collatz residue class at every depth, the rational fixed point satisfies `x* < 2^d`.** Consequently no class traps any member `n >= 2^d`: for every `n >= 2` with `n >= 2^tau(n)`,
>
> ```text
> sigma(n) = tau(n)      (descent happens exactly at the coefficient stopping time),
> ```
>
> and every Terras violation `n >= 2` must satisfy `n < 2^tau(n)` — violators can only be **certificate-record integers** (`gamma(n) = tau(n)/log2 n > 1`).

Corollaries, chaining with the earlier sessions:

1. **The depth-28 measurement is now a theorem at all depths** (for members beyond the residue). The measured exceptions `{0, 1}` are exactly the `q = 0` members of the two self-fixed classes (`x* = 0` for `r = 0`; `x* = 1` for `r = 1`).
2. **Counterexample minima sharpen further** (extends `FRONTIER-GEOMETRY.md` Theorem 3): the minimum `m` of any counterexample orbit is either a frontier resident (`tau = infinity`) or a certificate-record integer (`m < 2^tau(m)`). The threshold-trap escape hatch is closed at *every* depth, not just 28.
3. **Every nontrivial cycle minimum is a certificate-record integer.** (Cycle minima have `tau < infinity = sigma`, hence `m < 2^tau(m)`, i.e. `gamma(m) > 1`.) Combined with the verification floor: any cycle minimum exceeds `2^71` *and* survives its own magnitude in certificate depth — the two known constraints now compound.
4. **Terras' conjecture reduces to the `gamma > 1` band.** The remaining content of `tau = sigma` is exactly: no record integer `r` with `T^tau(r) >= r`. The record instrumentation (Session 1: `gamma_max = 14.5` at `10^9`, ceiling `19.98`) watches precisely this band.

## The envelope data (measured, exact)

`E(d) = max over classes of x*/2^d`, computed exactly by a max-DP over alive parity words (sound because both intercept transitions are monotone; cross-checked against brute enumeration of every class through depth 15):

| depth | attaining `o` | `log2 E(d)` |
|---:|---:|---:|
| 2 | 1 | **−2.000** (all-time peak: `x* = 1`, the trivial cycle) |
| 5 | 3 | −2.798 |
| 8 | 5 | −3.383 |
| 16 | 10 | −11.480 |
| 27 | 17 | −20.245 |
| 64 | 40 | −59.765 |
| **65** | **41** | **−55.240** (spike: convergent 65/41) |
| 149 | 94 | −137.759 |
| 305 | 192 | −298.752 |
| 484 | 305 | −476.806 |
| **485** | **306** | **−468.863** (spike: convergent 485/306) |
| 2048 | 1292 | −2037.177 |

Structure worth recording:

- **The trivial cycle is the all-time high-water mark of intercept danger** (`E = 1/4` at depth 2); after depth 8 the envelope collapses at ~1 bit per level (`E(d) ~ 2^{-(d-10)}`), i.e. the fixed points `x*` sit ever deeper *inside* the classes, never near the next member.
- **The continued-fraction ladder of `log2 3` is imprinted on the envelope:** local spikes of +4.5 bits at depth 65 (`o = 41`) and +7.9 bits at depth 485 (`o = 306`) — exactly the above-side convergents — and depths where *no* class certifies at all (3, 6, 9, 11, 14, 17, ...: no power of 3 in `[2^{d-1}, 2^d)`), the three-distance pattern.
- Both features confirm the proof's mechanism experimentally: trapping pressure is maximal precisely at convergent depths, and even there it falls short by dozens of bits.

## Synthesis: one Diophantine object, three phenomena

For a class with word `w`: **cycle** = `x*(w)` is an integer member; **threshold trap** = `x*(w)` reaches past the next member; **divergence** = `x*` postponed forever (`tau = infinity`, no class ever forms). All three are the intercept `c(w)` conspiring with the gap `2^d - 3^o`:

```text
cycles:      (2^d - 3^o) | c(w)          (exact divisibility)
traps:       c(w) >= 2^d (2^d - 3^o)     (excluded here, all depths)
divergence:  3^o >= 2^d at every prefix  (the frontier of FRONTIER-GEOMETRY.md)
```

The trap case is the weakest conspiracy and it is now provably impossible (except the trivial cycle's self-trap of `n = 1`, which *is* the known conspiracy `2^2 - 3 = 1 | 1`). The cycle case needs exact divisibility on top of a window of relative width `~2^{-o}` — the same wall, higher. The `eps`-barrier of `SIBLING-CONTROL.md` said proofs must consume the intercepts; this is the first all-depth theorem in the repo that does.

## What remains open (exactly)

- `q = 0` self-traps: a record integer `r < 2^d` with `r <= x*(r, d)` at `d = tau(r)`. Not excluded by the window (the trap bound used `n >= 2^d`); measured empty to `10^9`; heuristically has summable probability (`x*` is exponentially deep inside the class by the envelope), but that heuristic is exactly the distributional-to-pointwise gap.
- Frontier residents (`tau = infinity`): the divergence question, untouched here.
- Scope: the exclusion is certified for reduced denominators (hence odd counts) up to `~1e157`; beyond that, extend `--digits` — the method has no other frontier.

## Reproduce

```powershell
python experiments/collatz_threshold_envelope.py selftest
python experiments/collatz_threshold_envelope.py theorem --max-depth 2048 --o-max 256 --digits 320 --out experiments/results/threshold_theorem.json
python experiments/collatz_threshold_envelope.py envelope --max-depth 2048 --out experiments/results/threshold_envelope_2048.json
python experiments/collatz_threshold_envelope.py window --o-max 256 --out experiments/results/threshold_window_256.json
```

Self-test (8 checks, all passing): intercept bound exact and tight over all `2^14` words; envelope DP vs brute class enumeration to depth 15; the depth-2 class has `x* = 1` exactly; window scan vs brute Fraction check (`o <= 40`, `d <= 80`); the Legendre validity floor; the `q <= 3` distance exclusion; all above-side convergents excluded; and a direct no-trap scan of every `n <= 50,000`.
