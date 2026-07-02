# Gamma Attack — honest obstruction map for closing Terras structurally

_Created: 2026-07-02. Companion to `GAMMA-DUAL-ROUTE.md`, `collatz_gamma_pinch.py`, `ESCAPE-ENVELOPE.md`, `CERTIFICATE-FRONTIER-THEOREMS.md` Corollary 8.1._
_Status: **Open**. This documents what is proved, what would suffice, and exactly where a global `γ` proof stalls._

## Target theorem (would close Terras globally)

```text
γ(n) = τ(n) / log₂(n)  ≤  G   for all odd n ≥ 3,   with G ≤ 19.982…
```

**Proved conditional** (`collatz_gamma_pinch.py`): at `G = 19.982`, bands 12–15 all satisfy `G · log₂(ceiling) < τ_min(k)` with pinch ratios 261×–18,056×. So:

> **Lemma (γ-pinch closure — proved).** If `γ(n) ≤ G` for all `n`, and `G · log₂(hi_k) < τ_min(k)` for convergent band `k`, then band `k` contains no Terras violation. At `G = 19.982`, bands 12+ close without scanning.

Terras globally ⇒ no nontrivial cycles (threshold envelope). Terras + frontier separation ⇒ Collatz. **This note attacks Terras only.**

## What is already proved (independent of γ)

| Fact | Source | Status |
|---|---|---|
| Terras violation ⇒ `n < 2^τ`, alive word, record integer | `THRESHOLD-ENVELOPE.md` | **Proved** |
| Violation ⇒ `γ ≥ γ_floor(k)` rising along CF ladder; band 13 floor `7,366` | `RECORD-BAND.md` | **Proved** |
| `S(d) = 2^(d·H(θ) + O(log d))`; frontier density `2^(-0.05004·d)` | Theorem 7–8 | **Proved** |
| `D₁(b) = c*·b + O(log b)` for first-moment crossing | Corollary 8.1 | **Proved** |
| ε-invariant arguments cannot prove Collatz | `EPSILON-BARRIER.md` | **Proved** |
| Measured `max γ = 16.32` through `n ≤ 9×10¹⁰` | gap scans | **Measured** |

## The reduction chain (what a γ proof must bridge)

```text
γ(n) ≤ G
    ⇐  τ(n) ≤ G · log₂(n)                    [definition]
    ⇐  τ(n) ≤ D(n) + O(1)                    [? OPEN for all integers]
    ⇐  D(n) ≤ D₁(bitlen(n)) + fluctuation    [? OPEN — equidistribution]
    ⇐  D₁(b) = c*·b + O(log b)               [PROVED — survivor mass only]
```

**Proved bottom rung:** survivor mass pins `D₁(b)` to slope `c* = 19.982`.

**Open top rung:** for an arbitrary positive integer `n`, certificate depth `D(n)` is not the same object as `τ(n)` in general — but **τ-records** (integers maximizing `τ` at their scale) are exactly the certificate-depth records the escape envelope tracks. The conjecture is that no integer beats `D₁(b)` by more than a fluctuation term.

## Precise obstruction (Corollary 8.1 — proved statement of the wall)

From `CERTIFICATE-FRONTIER-THEOREMS.md`:

> The only unproved ingredient in the escape-envelope conjecture is **representative equidistribution**: integer representatives of survivor classes are spread in `[0, 2^d)` regularly enough that the minimal survivor tracks `2^d / S(d)`.

Measured duality products `m · S(d)/2^d` at exact records (`d = 105, 135, …, 395`) stay order-one (`0.30`–`6.6`) across seventeen binary orders of magnitude — **consistent** with equidistribution, **not proved**.

A global `γ ≤ 19.98` theorem is therefore **equivalent in difficulty** to:

> **Uniform escape:** every positive `b`-bit integer certifies by depth `≤ 19.98·b + O(log b)`.

This is strictly stronger than Tao (log-density almost-bounded) and strictly weaker than full Collatz (which also needs cycle exclusion and frontier separation).

## Why naive attacks fail (proved no-go's)

1. **Pure parity-word statistics** — ε-blind; `3n−1` has identical word distribution and cycles at `{5, 17}`. Any γ bound derived only from word frequencies cannot be Collatz-specific.

2. **Density / almost-all** — Terras violations live on a `2^(-0.05τ)`-sparse Cantor set. Density-1 descent (Terras 1976, Tao 2019) does not exclude a single integer threading the frontier.

3. **Scan induction** — infinitely many convergent bands; scans verify slices only. Band 13 alone has `7.3×10¹¹` odds in its window.

4. **Heuristic random model** — predicts `γ ≤ 19.98` but is not a proof; record slope `D(b)/b` climbs slowly toward `c*` (same phenomenon as Lagarias–Weiss `24.7` vs `41.68` limsup).

5. **Bitlen slack** — if one only proves `τ(n) ≤ c · bitlen(n)`, then `γ(n) ≤ c · (1 + 1/log₂ n) < 1.5c` for `n ≥ 4`. An escape envelope `D(b) ≤ c* · b` does **not** immediately yield `γ ≤ c*`; one needs `τ(n) ≤ c* · log₂ n` exactly.

## Measured evidence (not proof)

| Quantity | Value | Implication |
|---|---:|---|
| `max γ` through `9×10¹⁰` | 16.32 (global); chunk 3 max 14.74 | 22% below `c*` |
| `max τ` through `9×10¹⁰` | 547 | vs violation need `301,994` |
| Violation `γ_floor` band 13 | 7,366 | measured max is **450× below** |
| Record slope `D(b)/b` at `b=28` | 14.11 | vs `c*=19.98` |

No positive-integer anomaly visible at any probe. That is **calibrated silence**, not a theorem.

## Honest verdict

**Collatz: OPEN.** A global `γ ≤ 19.98` proof has not been found and cannot be obtained from current in-repo proved tools without solving **representative equidistribution** (or an equivalent uniform escape principle). The attack is correctly aimed: prove the envelope for all integers, not just frontier shadows.

## Reproduce

```powershell
python experiments/collatz_gamma_pinch.py selftest
python experiments/collatz_gamma_pinch.py table --out experiments/results/gamma_pinch_table.json
python experiments/collatz_gamma_pinch.py ledger-gap --out experiments/results/gamma_ledger_gap.json
```

## Next honest moves

1. **Scan** — band 13 chunk 4 (`9×10¹⁰`–`1.2×10¹¹`) in flight; chunk 5 queued after.
2. **Lemma E** — prove `m(d) ≥ 2^d/(C·S(d))` for positive integers; implies global `γ ≤ c*` and Terras.
3. **Branch-prefix lift** — finite evidence on pressure-unit prepaid surplus; target lift theorem consuming positivity.
