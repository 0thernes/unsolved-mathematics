# Gamma Upper Bound — attack map and honest wall

_Created: 2026-07-02. Status: **Open** (no global γ bound proved). Companion to `GAMMA-DUAL-ROUTE.md`, `collatz_gamma_pinch.py`, `ESCAPE-ENVELOPE.md`._

## The one theorem that closes Terras (hence cycles)

```text
∀ odd n ≥ 3 :  γ(n) = τ(n)/log₂(n) ≤ G     with G = 1/(1 − H(log₂ 3)) = 19.982…
```

**Proved conditional** (`collatz_gamma_pinch.py`): this implies every convergent band `k` with `G · log₂(ceiling_k) < τ_min(k)` is empty. At `G = 19.98`, bands 12–15 all close with pinch ratios 261×–18,000×.

**Open:** the universal quantifier.

## What is already proved (independent of γ)

| Fact | Source | Label |
|---|---|---|
| Terras violation ⇒ `n < 2^τ`, alive parity word | THRESHOLD-ENVELOPE | **Proved** |
| Violation ⇒ `γ ≥ γ_floor(k)` at band ceiling | RECORD-BAND | **Proved** |
| `γ_floor(13) = 7,366`; violation needs `τ ≥ 301,994` | reduction_squeeze | **Proved** |
| No ε-invariant statistic distinguishes Collatz from `3n−1` | EPSILON-BARRIER | **Proved** |
| Frontier density `≤ 2^{−0.05004·d}` | CERTIFICATE-FRONTIER Thm 7 | **Proved** |
| First-moment crossing slope `c* = 19.982` | ESCAPE-ENVELOPE | **Heuristic** |

## Measured through `n ≤ 9×10¹⁰` (chunk 3 complete)

| Quantity | Value | `n` |
|---:|---:|---:|
| `max τ` (global) | 547 | 14,500,812,391 |
| `max γ` (global) | **16.32** | 12,235,060,455 |
| chunk 3 local `max τ` | 535 | 83,987,887,551 |
| chunk 3 local `max γ` | **14.74** | 83,987,887,551 |
| Terras mismatches | **0** | 44.5×10⁹ odds |

Measured `γ` stays **500× below** violation floor `7,366` in band 13. Trend in chunks 2–3: local γ records **decrease** with scale (15.90 → 13.86 → 14.74). **Not a proof** — records can spike later (Lagarias–Weiss limsup ≫ finite records).

## Three attack routes (and where each stops)

### Route 1 — Parity-word / frontier statistics

**Idea:** Bound `τ(n)` via survivor-set density and free-coin entropy.

**Wall (proved):** ε-Barrier. `3n−1` has **identical** word distributions but cycles at `{5,7,10}` and `{17,…}`. Any statistic factoring through parity-word measure is ε-blind and cannot prove Collatz.

**Salvage:** Must consume intercepts `c(w) > 0` and positivity of finite binary support — not word counts alone.

### Route 2 — Escape envelope `D(b) ≤ c* · b`

**Idea:** Worst certificate depth over `b`-bit frontier reps satisfies `D(b) ≈ 19.98·b`.

**Proved:** Density bound on frontier. **Measured:** seven exact base depths, records straddle `D₁(b)` within fluctuation.

**Wall:** `D(b)` is defined on **frontier representatives**, not all integers. General `τ(n)` can be much smaller than frontier escape depth. Linking `γ(n)` for all `n` to frontier max requires a **uniform positive-integer escape theorem** — exactly the open Collatz divergence half.

### Route 3 — Branch-prefix structural credit

**Idea:** Visible high-ladder + low-repeat credit pays excess debt at every prefix.

**Measured:** 1.9M+ exact frontier rows, zero prefix failures.

**Wall:** Lift transitions show **5,677 retimed-pressure** cases where parent-to-child credit delta is insufficient; all still pass on finite evidence. Universal induction across all positive shadows — **open**.

## Why “loop until solved” hits a theorem wall

Collatz is not a computation problem at current scale:

1. **Verified to `2^71`** (Bařina) — no counterexample.
2. **Terras measured to `9×10¹⁰`** — no mismatch; band 13 still has ~`6.8×10¹¹` odds left.
3. **Infinite convergent bands** — scans cannot finish Terras globally.
4. **Proved no-go** — ε-invariant methods cannot work.
5. **Conditional closure** — `γ ≤ 19.98` would close Terras structurally; **unproved**.

A genuine solution requires a new **value-level** theorem bridging positive integers to the `2`-adic survivor boundary — not more scans alone.

## Reproduce

```powershell
python experiments/collatz_gamma_pinch.py table --out experiments/results/gamma_pinch_table.json
python experiments/collatz_gap_scanner.py ledger --out experiments/results/terras_ledger.json
python experiments/epsilon_barrier_check.py
```

## Honesty

**Collatz: OPEN.** This document maps attacks and walls; it does not claim a proof.
