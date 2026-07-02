# Cycle equation — exact form, validated on every known cycle

> The **cycle side** companion to the survivor/dimension notes. Derives the exact cycle identity for
> the shortcut map from scratch, validates it **exactly** on all known cycles of the three sibling
> maps (ground truth), re-derives the sign dichotomy quantitatively, and states the (classical,
> Eliahou/continued-fraction) exclusion mechanism — cross-referencing
> [`cycle_bound_lab.py`](cycle_bound_lab.py) and [`SIBLING-CONTROL.md`](SIBLING-CONTROL.md).
> Reproduce: `python experiments/cycle_equation.py`. Status **[PROVED]** · **[VERIFIED]**.
> **No proof of Collatz is claimed.**

Shortcut map `T_{q,ε}(x) = (q x + ε)/2` if `x` odd, `x/2` if even (`ε = ±1`).

## The cycle equation  **[PROVED]**

A cycle with odd elements `a_1,…,a_k` (`k` odd steps) and `L` total steps returns to its start, so
the net multiplier is `1`. Each odd step multiplies by `(q a_i + ε)/(2 a_i)`, each even step by `1/2`:

  `(1/2^L) · ∏_i (q + ε/a_i) = 1`  ⟺  **`∏_i (q a_i + ε) = 2^L · ∏_i a_i`**  (exact integer identity)

Taking `log₂`:  **`L = k·log₂q + Σ_i log₂(1 + ε/(q a_i))`**  (log form).

**Sign dichotomy** (the repo's, re-derived in one line): every term `log₂(1+ε/(q a_i))` has the sign
of `ε`, so `ε=+1 ⇒ L > k·log₂q ⇒ q^k < 2^L` (cycle *below* the line) and
`ε=−1 ⇒ q^k > 2^L` (cycle *above* the line).

## Exact validation on every known cycle  **[VERIFIED]**

The integer identity `∏(q a_i + ε) = 2^L·∏a_i` holds **exactly** (big-integer equality) for all six
known cycles across the three siblings, and the defect `L − k·log₂q` matches
`Σ log₂(1+ε/(q a_i))` to machine precision:

| map / cycle | k | L | odd elements `a_i` | integer identity | defect `L−k·log₂q` | side |
|---|---:|---:|---|:---:|---:|---|
| Collatz 3n+1 (trivial) | 1 | 2 | [1] | 4 = 4 | `+0.415037` | `3¹<2²` below |
| 3n−1 fixed point | 1 | 1 | [1] | 2 = 2 | `−0.584963` | `3¹>2¹` above |
| 3n−1 at 5 | 2 | 3 | [5, 7] | 280 = 280 | `−0.169925` | above |
| 3n−1 at 17 | 7 | 11 | [17,25,37,55,41,61,91] | 403123745024000 = ✓ | `−0.094738` | above |
| 5n+1 at 13 | 3 | 7 | [13, 33, 83] | 4557696 = 4557696 | `+0.034216` | below |
| 5n+1 at 17 | 3 | 7 | [17, 43, 27] | 2526336 = 2526336 | `+0.034216` | below |

Every row: identity **exact**, defect = curvature-sum **match**, sign rule **holds**. The theory
predicts every real cycle on the nose — including the razor-thin `3n−1` cycle at 17
(`3⁷ = 2187` vs `2¹¹ = 2048`, only `+0.095` bits above the line).

## What excludes Collatz cycles (honest — this is the Eliahou/CF ladder)

For a nontrivial Collatz cycle, the defect `d_k = ⌈k·log₂3⌉ − k·log₂3 = Σ log₂(1+1/(3 a_i))` is the
total "curvature budget." Since `log₂(1+t) ≤ t/ln2` and every `a_i ≥ m` (the minimum element),

  `d_k ≤ k / (3 m ln2)`,  hence  `m ≤ k / (3 ln2 · d_k)`.

All `n < 2^71` are verified, so every cycle element exceeds `2^71`; that forces
`d_k < k/(3 ln2 · 2^71)` — the defect must be astronomically small, i.e. `k` must land at a very deep
**convergent of `log₂3`** (where `k·log₂3` is nearest an integer). Sample defects at convergent
denominators (small `d_k` ⇒ large permitted `m`):

| k | `d_k` | `⇒ m ≤ k/(3 ln2 d_k)` |
|---:|---:|---:|
| 41 | `1.65×10⁻²` | `1.2×10³` |
| 306 | `1.48×10⁻³` | `1.0×10⁵` |
| 15601 | `2.63×10⁻⁵` | `2.9×10⁸` |

Pushing to convergents with `d_k ~ 2⁻⁷¹` drives `k` into the `10¹⁰–10¹¹` range — exactly the floor
`cycle_bound_lab.py` computes (`~6.5×10¹⁰` odd steps, vs Hercher's sharper `1.375×10¹¹`).

## Honesty

- **Classical.** The integer identity is the Böhm–Sontacchi parametrization; the CF exclusion is
  Eliahou (1993) / Simons–de Weger / Hercher territory. No new theorem.
- **What's done here:** a clean self-contained derivation, an **exact ground-truth validation across
  three sibling maps** (the machinery reproduces every real cycle), and the "defect = curvature
  budget" framing that makes the sign dichotomy and the CF exclusion one picture.
- **Not Collatz.** A finite verification bound can push the cycle floor arbitrarily high but never
  excludes the *infinite* family of possible `k`; and the sibling maps prove the method is honest
  (it *finds* the `3n−1` and `5n+1` cycles, and stays silent on Collatz). Cycle-freeness of Collatz
  remains open.
