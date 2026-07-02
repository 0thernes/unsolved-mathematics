# Gamma Dual-Route Exclusion — two independent ways Terras fails in a band

_Created: 2026-07-02. Companion to `RECORD-BAND.md`, `TERRAS-LEDGER.md`, `collatz_gap_scanner.py`._
_Status labels: **Proved**, **Measured**, **Heuristic**, **Open**._

## The honest headline

**Collatz: OPEN.** Terras globally: **OPEN.** This note does not close either.

What it adds is a **second, independent exclusion criterion** for convergent bands. Bands 10–12 were closed by exhaustive τ-scan. The same bands — and every partial band-13 chunk scanned so far — are also incompatible with Terras violations by a **proved γ lower bound** vs a **measured γ upper bound**. The two routes agree; either alone would suffice in the measured range.

## Route A — τ floor (proved criterion + measurement)

From `THRESHOLD-ENVELOPE.md` + `RECORD-BAND.md`: a Terras violation in convergent band `k` (odd-step count `o ∈ [q_k, q_{k+1})`) needs

```text
τ(n) ≥ τ_min(k)
```

where `τ_min` is the certificate length at the band’s Diophantine ceiling (exact from the continued fraction of log₂ 3).

**Band-closure theorem (proved):** If every odd `n` in a window `(lo, hi]` satisfies `τ(n) < τ_min(k)`, then **no** Terras violation can occur in that band past `lo`.

**Measured (bands 10–12 + band 13 chunk 1):**

| Band | `τ_min` | `max τ` measured | Margin |
|---:|---:|---:|---:|
| 10 | 50,509 | 433 | 116× |
| 11 | 125,743 | 447 | 281× |
| 12 | 176,252 | 547 | 322× |
| 13 (to 3×10¹⁰) | 301,994 | 546 | 553× |

Zero `τ ≠ σ` mismatches in **14.5×10⁹** odd integers scanned.

## Route B — γ floor (proved lower bound vs measured upper bound)

Define `γ(n) = τ(n) / log₂ n`.

### Lower bound (proved — `RECORD-BAND.md`)

Any Terras violation beyond the `10⁹` scan with odd count in band `k` must be a certificate-record integer trapped below the band ceiling `X(o)`. At the band ceiling,

```text
γ(n) ≥ γ_floor(k) := τ_min(k) / ⌈log₂ X_band⌉
```

Exact values from `record_band_theorem.json` / `reduction_squeeze.json`:

| Band | `γ_floor` at ceiling | Borel–Cantelli heuristic max | Measured max γ (verified range) |
|---:|---:|---:|---:|
| 10 | 1,578 | 19.98 | ≤ 14.07 (band 10 scan) |
| 11 | 3,698 | 19.98 | ≤ 14.07 |
| 12 | 5,184 | 19.98 | **16.32** |
| 13 | 7,366 | 19.98 | **15.90** (chunk 1) |

**Proved inequality chain:** violation ⇒ `γ ≥ γ_floor` with `γ_floor ≥ 1,531` already in the first post-scan band; `γ_floor` rises without bound along the convergent ladder.

### Upper bound (measured only — not proved globally)

Through `n ≤ 1.45×10¹⁰` (band 12 ceiling) and `n ≤ 3×10¹⁰` (band 13 chunk 1):

```text
max γ = 16.32   at n = 12,235,060,455   (band 12 closure)
max γ = 15.90   at n = 21,751,218,587   (band 13 chunk 1)
```

Both sit **below** the random-model ceiling `1/(1−H(log₂ 3)) = 19.982…` and **far below** any admissible violation floor (`≥ 1,578` in band 10 alone).

### Dual-route corollary (measured range)

For every `n` in the scanned windows, **both**:

1. `τ(n) < τ_min(k)` — direct scan, and  
2. `γ(n) < γ_floor(k)` — because `16.32 ≪ 1,578`.

So Terras holds in those windows by **two independent mechanisms**. A conspiracy would need to beat the τ scan **and** thread a γ gap of order `10²–10³` simultaneously.

## Heuristic pinch (not a theorem)

If one could **prove** `γ(n) ≤ G` for all `n` with `G = 16.32` (or even `G = 19.98`), then at band 13’s ceiling (`log₂ n ≈ 40.4`):

```text
τ(n) ≤ G · log₂ n ≈ 660   ≪   τ_min = 301,994
```

Pinch ratio ≈ **458×** (`band13_plan.json`). This would close band 13 without scanning — but **no global γ upper bound is proved**. The escape-envelope conjecture (`D(b) ≈ 19.98·b`) is the sharpest candidate; it is **conjectural**, verified only on frontier representatives and finite samples.

## What would actually close Terras (and what each route buys)

| Target | Route A (τ scan) | Route B (γ bound) |
|---|---|---|
| One band slice | Exhaust odd window; check `max τ < τ_min` | **Open:** prove `γ ≤ G` globally |
| All bands | Infinite scan wall | **Open:** prove `G · log₂ X_k < τ_min(k)` for all `k` |
| Collatz | Terras + `S ∩ ℤ_{>0} = ∅` | Same — γ does not touch divergence |

## Reproduce

```powershell
python experiments/collatz_record_band.py theorem --digits 320 --out experiments/results/record_band_theorem.json
python experiments/collatz_gap_scanner.py ladder --scan-floor 15443807723 --closed-bands 10,11,12
python experiments/collatz_gap_scanner.py band-plan --scan-floor 15443807723 --band-k 13
python experiments/collatz_gap_scanner.py ledger --out experiments/results/terras_ledger.json
```

## Open (exactly)

1. **Prove** `γ(n) ≤ f(bitlen)` for a computable `f` small enough to close bands 13+ without scanning.  
2. **Or** finish band 13 window scan (~31 h at 6.5M odds/sec for the remainder).  
3. **Collatz divergence half** — frontier residents, untouched by Terras/γ.  
4. **Do not** claim proof without global Terras or empty frontier.
