# Gamma Bound Attempt — honest failure map and minimal open lemma

_Created: 2026-07-02. Status: **Open**. Does not prove Collatz or Terras._

## What “solve Collatz via γ” would mean

From `collatz_gamma_pinch.py` (proved conditional):

```text
(∀n: γ(n) ≤ G)  ∧  (G · log₂(ceiling_k) < τ_min(k) for all bands k)  ⟹  Terras globally
```

At `G = 19.982…` (Borel–Cantelli / escape-envelope constant `c*`), **every** convergent band 12+ pinches with ratio ≥ 261×. Terras globally would follow; cycles die via `RECORD-BAND` trapping.

**Collatz** still needs frontier separation `S ∩ ℤ_{>0} = ∅` (divergence half). The γ route attacks Terras only.

## Reduction: global γ bound = record-integer envelope

**Proved** (`THRESHOLD-ENVELOPE.md`): Terras violation `σ(n) > τ(n)` forces `n < 2^τ(n)` — the violator is a **certificate-record integer** (`γ > 1`).

So:

```text
sup_{n≥2} γ(n)  =  sup { τ(n)/log₂(n) : n < 2^τ(n) }  =  sup over record integers
```

A global upper bound on γ is **exactly** a uniform ceiling on how deep certificate-record integers can be relative to their bit length. This is the first-moment escape envelope `D(b) ≤ f(b)` in disguise:

```text
γ(n) ≤ f(bitlen(n)) / bitlen(n)   ⟺   τ(n) ≤ f(bitlen(n))   for record n
```

## What is already proved (does not close γ)

| Result | Source | Why insufficient |
|---|---|---|
| Frontier density `≤ 2^{-0.05004 d}` | Theorem 7 | Counting, not pointwise |
| `D₁(b) = c* b + O(log b)` for first-moment crossing | Corollary 8.1 | Crosses **expected** count, not max |
| Violation needs `γ ≥ γ_floor(k) → ∞` | RECORD-BAND | Lower bound only |
| `τ = σ` through `6×10¹⁰` | gap scans | Finite measurement |
| ε-invariance barrier | SIBLING-CONTROL | Blocks word-only upper bounds |

## The exact open wall (named)

**Conjecture 7.2 / representative equidistribution** (`CERTIFICATE-FRONTIER-THEOREMS.md`, Corollary 8.1):

> Integer representatives of depth-`d` survivor classes are spread in `[0, 2^d)` regularly enough that the **minimal** positive survivor tracks `2^d / S(d)`.

Equivalently for γ: **no** positive integer in the record class at depth `d` has `τ` exceeding `D₁(bitlen) + fluctuation` where `D₁(b) ≈ 19.98 b`.

Measured: record integers at depths 105–395 have `D/b` from 7.5 to 14.1 — all below `c* = 19.98`. The 62-bit beam champion certifies at 509 vs `D₁(62) ≈ 1,010`. **No counterexample found**; **no proof**.

## Why three naive “proof” routes fail

### 1. Random-model / typical-orbit drift

The `3/4` heuristic gives **almost-all** descent, not **every** integer. Tao (2019) is logarithmic-density almost-bounded — the exceptional set where γ could blow up is exactly the divergence hiding set. **Fails:** confuses measure with integers.

### 2. Parity-word / ε-invariant statistics

`3n−1` has **identical** word distribution to Collatz but cycles at `{5, 17}`. Any bound derived only from word frequencies cannot distinguish Collatz from a cycling map. **Fails:** ε-barrier (`EPSILON-BARRIER.md`).

### 3. Finite frontier exhaustion

Exact survivor frontier at depth 28 has 3,524,586 residues; all finite representatives escape by depth 395. But the all-odd `2`-adic point `-1` survives every depth — a **non-integer** boundary. Proving escape for **all** positive finite shadows requires a uniform lift theorem, not finite DP. **Fails:** `-1` is the structural obstruction (`Theorem 3`).

## Minimal theorem target (single sentence)

**Open Lemma (γ):** For every positive integer `n` with certificate depth `τ(n) = d`,

```text
d ≤ c* · bitlen(n) + O(√bitlen(n))     where c* = 1/(1 - H(log₂ 3)) = 19.982…
```

This is strictly weaker than Collatz but implies Terras globally via `collatz_gamma_pinch.py`.

## Falsification criteria (honest)

Any of these would break the envelope law:

- `n` with `γ(n) > 20` (e.g. `τ > 20 · log₂ n`)
- 32-bit start with certificate depth `> 700`
- Systematic positive drift in alive-curve deviation vs free-coin model at large depth

None observed through `9×10¹⁰` scan; band 13 chunks show chunk max `γ` **14.74** (chunk 3), not climbing toward violation floor `7,366`.

## Reproduce

```powershell
python experiments/collatz_gamma_pinch.py table --out experiments/results/gamma_pinch_table.json
python experiments/collatz_gamma_pinch.py close-if --g-upper 19.982 --band-k 13
python experiments/escape_envelope_analyzer.py --self-test --max-dp-depth 2048
```

## Verdict

**Cannot solve Collatz this session.** The γ-bound route reduces to the same open equidistribution lemma as the escape envelope — proved on the **mass** side, open on the **representative** side. Computation extends Terras incrementally; structure needs the named lemma above or a genuinely new positivity-consuming input (not ε-blind).
