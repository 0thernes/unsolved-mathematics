# Master Reduction — where Collatz actually lives after Sessions 1–6

_Created: 2026-07-01. Companion to `collatz_reduction.py`; synthesizes `FRONTIER-GEOMETRY.md`, `SIBLING-CONTROL.md`, `THRESHOLD-ENVELOPE.md`, `RECORD-BAND.md`._
_Status: every link in the chain below is labeled **Proved**, **Measured**, or **Conditional**. This document does not prove the Collatz conjecture; it states the exact residue._

## The one-line map

```text
Collatz
  |-- (conditional on Terras) -->  S ∩ Z_{>0} = ∅     [divergence]
  |-- Terras (tau = sigma)      -->  no self-trap record integers  [gamma > 1 band]
  |-- cycles (unconditional)    -->  same self-trap band + 2^71 floor
```

Under Terras' coefficient stopping time conjecture, **the entire conjecture is the frontier-separation statement** `S ∩ Z_{>0} = ∅`. Terras alone already kills nontrivial cycles (`sigma = ∞` on a cycle minimum contradicts `tau = sigma`). Everything else in this repo sharpens *where* a Terras violation or a frontier resident could hide.

## Proof chain (executable: `collatz_reduction.py reduction`)

| Step | Source | Status | Content |
|---|---|---|---|
| A | FRONTIER-GEOMETRY Thm 3 | **Proved** | Counterexample minima localize to the frontier or sit below a certificate threshold |
| B | THRESHOLD-ENVELOPE | **Proved** | Threshold traps are vacuous at every depth; Terras violations need `n < 2^tau(n)` |
| C | RECORD-BAND | **Proved** | Alive violations obey `n <= o/(2 ln2 δ(o))` with explicit per-band gamma floors |
| D | REDUCTION (delta-squeeze) | **Proved** | Nine convergent bands below `q = 31,867` are **empty** of violations past `10^9` |
| E | tau scan | **Measured** | `tau(n) = sigma(n)` for all `1 < n <= 10^9` |
| F | SIBLING-CONTROL | **Proved** | Word statistics cannot finish the job; intercept sign `ε = +1` is essential |

## Theorem (delta-squeeze band exclusion — proved)

Let `N = 10^9` (scan floor). A Terras violation with odd count `o` in convergent band `[q_k, q_{k+1})` satisfies

```text
n  <=  o / (2 ln2 δ(o)),          δ(o) >= ||q_k log2 3||     (Lagrange),
```

hence `n <= o / (2 ln2 ||q_k log2 3||)`. Past `N`, need `o >= o_need(N) := floor(2 N ln2 ||q_k log2 3||) + 1`. If `o_need(N) >= q_{k+1}`, **no** odd count in the band yields `X(o) > N`, so the band cannot host a violation beyond the scan.

**Result:** bands with `q_{k+1} <= 665` through `q_k = 15,601` (nine bands, all denominators below `31,867`) are **proved empty** of Terras violations past `10^9`. The first band that is not structurally excluded is:

```text
31,867  <=  o  <  79,335
tau  >=  50,509
10^9  <  n  <=  2,147,483,648   (log2 ceiling 31.03, tight at o = o_min)
gamma  >=  1,561   (at the ceiling)
```

This tightens RECORD-BAND's `log2 X = 32.35` (band-end ceiling at `o = 79,334`) to `log2 X = 31.03` at the **minimum** feasible odd count `o = 31,867`. The scan gap is a finite window of width `~2.15×` above `10^9`, not `~5.4×`.

## What each phenomenon is now

```text
cycles:       (2^d - 3^o) | c(w)           exact divisibility on alive words
self-traps:   n <= x*(n, tau(n))            record integers, gamma > 1
              threshold traps: EXCLUDED       THRESHOLD-ENVELOPE, all depths
divergence:   tau = infinity                  frontier residents in S
```

The trap-with-threshold case is dead. The self-trap case is confined to record integers with quantified ceilings. Divergence is exactly positive integers in `S`.

## Conditional vs unconditional reductions

**Under Terras (`tau = sigma` for all `n >= 2`):**

```text
Collatz  <=>  S ∩ Z_{>0} = ∅.
```

**Unconditional (what is actually proved without Terras):**

1. No threshold-trapped Terras violation at any depth.
2. **Terras verified for all `n <= 2,193,206,481`** (`10^9` scan + Session 7 gap closure; `max_tau = 433` in gap vs `tau_min = 50,509` required).
3. Any Terras violation past `2^31` needs band 11+ (`tau >= 125,743`, `n <= 2^33.33`).
4. Any nontrivial cycle minimum (if one exists) is a record integer with `gamma >= 10^9` (conditional on `m > 2^71`).
5. Ten convergent bands below band 11 are empty past the scans (nine delta-squeeze + one gap closure).
6. `ε`-invariant arguments cannot prove frontier separation.

## What remains open (exactly)

| Gap | Type | Statement |
|---|---|---|
| Scan window (band 10) | **Closed** | `596,603,241` odds scanned; `max_tau = 433`; band proved empty (`BIT-BUDGET.md`) |
| Terras globally | **Open** | Bands 11+; next needs `tau >= 125,743`, `n <= 2^33.33` |
| Frontier | **Open** | `S ∩ Z_{>0} = ∅` |
| Extreme-value law | **Heuristic** | `gamma(n) <= 19.982` for all `n`; gap max `gamma = 14.07` |
| Cycles | **Computational + proved floor** | Excluded below `2^71`; structural wall at `~5×10^10` odd steps |

The first-open-band conspiracy is **eliminated**. The next venue is band 11: a wider `n`-window (`~2^33`) but requiring `tau >= 125,743` — still `~290×` beyond the gap's measured `max_tau = 433`.

## Reproduce

```powershell
python experiments/collatz_reduction.py selftest
python experiments/collatz_reduction.py squeeze --out experiments/results/reduction_squeeze.json
python experiments/collatz_reduction.py reduction --out experiments/results/reduction_master.json
```

## Honest verdict

Human methods stalled on the distributional-to-pointwise gap. This repo does not close that gap with a proof. It **does** reduce Collatz to Terras record integers (now verified through `2^31`), frontier residents, and the convergent-band ladder — with ten bands eliminated and the first scan gap closed by exhaustive measurement.
