# Terras Verification Ledger

_Created: 2026-07-02. Honest accounting of what is **Proved**, **Measured**, and **Open** for Terras' coefficient stopping time conjecture (`τ = σ`). This does not prove Collatz._

## Current verification ceiling (measured)

```text
Terras (τ = σ) verified for all odd n  ≤  90,000,000,000   (log₂ n ≤ 36.39)
```

Zero mismatches across **44.5×10⁹** odd integers scanned (bands 10–12 full + band 13 chunks 1–3).

Band 13 remains **open** above `9×10¹⁰`: window `(9×10¹⁰, 1.48×10¹²]`, ~`6.85×10¹¹` odds (~25 h remaining). Chunk 4 (`9×10¹⁰`–`1.2×10¹¹`) in progress.

## Dual-route exclusion (see `GAMMA-DUAL-ROUTE.md`)

Every scanned window is closed by **two independent routes**:

| Route | Mechanism | Status in verified range |
|---|---|---|
| **A** | `max τ < τ_min(k)` | **Measured** — bands 10–12 + band 13 chunks 1–3 |
| **B** | `max γ < γ_floor(k)` | **Proved** lower bound vs **measured** upper (`16.32 ≪ 1,578`) |

A Terras violation in band 10+ would need `γ ≥ 1,578`; measured max is `16.32` — a gap of **~97×** even before the τ scan.

## Ladder status

| Band | `q` range | Status | Method |
|---:|---|---|---|
| 1–9 | below 31,867 | **PROVED empty** | delta-squeeze past `10^9` |
| 10 | 31,867 – 79,335 | **CLOSED** | scan: `max_τ=433` `<` `50,509` |
| 11 | 79,335 – 111,202 | **CLOSED** | scan: `max_τ=447` `<` `125,743` |
| 12 | 111,202 – 190,537 | **CLOSED** | scan: `max_τ=547` `<` `176,252` |
| 13 | 190,537 – 10,590,737 | **PARTIAL** | chunks 1–3 to `9×10¹⁰`: `max_τ=535` (chunk 3) `<` `301,994`; chunk 4 in flight |

At scan floor `1.54×10¹⁰`, bands 1–11 are also **structurally proved empty** by delta-squeeze (no scan needed for violations past that floor in those bands).

## Record statistics (measured, in verified range)

| Quantity | Value | `n` |
|---:|---:|---:|
| max `τ` | 547 | 14,500,812,391 (band 12); chunk 3 max `535` at `8.40×10¹⁰` |
| max `γ = τ/log₂ n` | 16.32 | 12,235,060,455 (band 12); chunk 3 max `14.74` at `8.40×10¹⁰` |
| mean `τ` | ~5.985 | — |

Borel–Cantelli heuristic ceiling: `γ ≤ 19.982`. Measured records stay well below.

## Band 13 (next target)

| Quantity | Value |
|---|---:|
| Window | `(1.54×10¹⁰, 1.48×10¹²]` |
| `τ_min` for violation | 301,994 |
| Heuristic `τ` at ceiling (`γ≤16.32`) | ~660 |
| Pinch ratio | ~458× (heuristic, **not proved**) |

Chunk scans extend verification incrementally; only a full-window scan or a **proved** `γ` bound closes the band.

## What Terras would imply for Collatz

```text
Terras globally  +  frontier separation (S ∩ ℤ_{>0} = ∅)  ⟹  Collatz
```

Terras alone already kills nontrivial cycles. Scans attack Terras; frontier residents are the divergence half — untouched here.

## Reproduce

```powershell
python experiments/collatz_gap_scanner.py ladder --scan-floor 15443807723 --closed-bands 10,11,12
python experiments/collatz_gap_scanner.py band-plan --scan-floor 15443807723 --band-k 13
python experiments/collatz_gap_scanner.py close-band --scan-floor 15443807723 --band-k 12 --workers 8
```

## Honesty

- **Collatz: OPEN**
- **Terras through `9×10¹⁰`: measured** (band 13 chunks 1–3 complete; chunk 4 in flight)
- **Bands 10–12 closure: proved empty per band-closure criterion + measurement**
- **Band 13+: scan wall or needs new theorem**
