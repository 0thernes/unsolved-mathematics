# Bit Budget — closing the first open band

_Created: 2026-07-01. Companion to `collatz_gap_scanner.py`; sequel to `REDUCTION.md`._
_Status: the band-closure criterion is **Proved** (logic); scan completion is **Measured** when `max_tau < tau_min` throughout the window._

## The closure criterion (proved, one line)

A Terras violation in the first open convergent band `[31,867, 79,335)` past the `10^9` scan requires **simultaneously**:

```text
tau(n) >= 50,509
10^9 < n <= 2,193,206,481
```

If **every** odd integer in `(10^9, 2,193,206,481]` satisfies `tau(n) < 50,509`, the band is **proved empty** — no Terras violation can occur there. No intercept conspiracy, no frontier statistics, no random model: pure certificate-depth arithmetic.

This is strictly stronger than pointwise `tau = sigma` checking for the band-closure purpose: a violator must be a record integer with `gamma > 1`, which forces enormous `tau` relative to `n`.

## Gamma-record pinch (structural, measured)

Along the classical stopping-time record ladder through `10^9`:

| `n` | `tau` | `gamma = tau/log2(n)` |
|---:|---:|---:|
| 27 | 59 | 12.41 |
| 63,728,127 | 376 | 14.50 |
| 217,740,015 | 395 | 14.26 |

The all-time record `gamma` is **14.503**. The Borel–Cantelli / escape-envelope ceiling is **19.982**.

A Terras violation at the first-band ceiling needs:

```text
gamma >= 1,578   (proved from RECORD-BAND + delta-squeeze)
tau  >= 50,509
log2(n) <= 31.03
```

So `gamma` must exceed the measured record by a factor of **~108×** and the heuristic ceiling by **~79×**. Under the measured record law, `tau(n) <= 14.5 * log2(n) <= 450` for all `n <= 2^31` — three orders of magnitude below `50,509`.

This is not yet a theorem (the `gamma <= 19.982` law is heuristic), but it explains why the gap scan is expected to close the band in minutes, not millennia.

## Executable closure

```powershell
python experiments/collatz_gap_scanner.py selftest
python experiments/collatz_gap_scanner.py scan --out experiments/results/gap_scan_first_band.json
python experiments/collatz_gap_scanner.py theorem --scan experiments/results/gap_scan_first_band.json --out experiments/results/gap_band_closure.json
```

**Band closed** when the scan JSON reports `"proved_empty": true` under `band_closure`.

## Result (Session 7 — measured, 2026-07-01)

Full scan of **596,603,241** odd integers in `(10^9, 2,193,206,481]`:

| Quantity | Value |
|---|---:|
| `max_tau` | **433** (`n = 1,827,397,567`) |
| `tau_min` required | 50,509 |
| `max_gamma` | **14.074** |
| `tau = sigma` | **verified** (zero mismatches) |
| Band status | **PROVED EMPTY** |

**Terras' conjecture now holds for all `n <= 2,193,206,481` (~2^31.03)** — combining the `10^9` scan and this gap closure. The next Terras-violation venue is convergent band 11 (`q = 79,335`), needing `tau >= 125,743` and `n <= 2^33.33`.

Results: `results/gap_scan_first_band.json`, `results/gap_band_closure.json`.

## Band ladder (Session 8+)

After each band closes, advance `scan_floor` to that band's `n_ceiling` and scan the next `SCAN_GAP` band:

```powershell
python experiments/collatz_gap_scanner.py ladder --scan-floor 2193206481 --closed-bands 10
python experiments/collatz_gap_scanner.py scan --scan-floor 2193206481 --band-k 11 --out experiments/results/gap_scan_band11.json
```

| Band | `q` range | `tau_min` | `n` ceiling | Status |
|---:|---|---:|---:|---|
| 10 | 31,867 – 79,335 | 50,509 | 2^31.03 | **CLOSED** (Session 7) |
| 11 | 79,335 – 111,202 | 125,743 | 2^33.33 | **CLOSED** (4,315,473,629 odds, `max_τ=447`) |
| 12 | 111,202 – 190,537 | 176,252 | 2^33.85 | **CLOSED** (2,309,826,992 odds, `max_τ=547`) |

**Terras verified (measured) through `n ≤ 15,443,807,723` (~2^33.85).** Collatz remains open.

## Band 13 scale wall (honest)

```powershell
python experiments/collatz_gap_scanner.py band-plan --scan-floor 15443807723 --band-k 13
```

| Quantity | Value |
|---|---:|
| Window | `(1.54×10^10, 1.48×10^12]` |
| Odd integers | **~7.31×10^11** |
| `τ_min` required | 301,994 |
| Est. scan time (8 workers) | **~31 hours** |
| Heuristic `τ` at ceiling (`γ≤16.32`) | **~659** |
| Pinch ratio (heuristic) | **~458×** |

Full band-13 closure requires chunked scanning or a **proved** bound on `γ(n)` — not yet available. Chunk scans extend Terras verification incrementally; they do not close the band unless the full window is covered.

## After closure

If the first band closes, the next Terras-violation venue moves to band 11 (`q = 79,335`), with `tau_min = 125,743` and ceiling `log2 n = 33.33` — another finite scan gap, but wider (~8× in `n`). The delta-squeeze + scan pattern repeats band by band up the convergent ladder.

## What remains (exactly)

- Global Terras: infinitely many bands, scan cannot finish all
- Frontier residents: untouched
- `gamma` ceiling as a theorem: still open
- Collatz: still open even if all scan gaps through some scale close
