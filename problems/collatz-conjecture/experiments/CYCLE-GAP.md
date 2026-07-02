# Cycle-Gap arithmetic — how far elementary exclusion reaches, and where Baker takes over

**Date:** 2026-07-02
**Instrument:** [`cycle_gap_check.py`](cycle_gap_check.py) → [`results/cycle_gap.json`](results/cycle_gap.json)
**Status:** exact reproduction of the elementary core of cycle-exclusion. **Not a proof of Collatz;** it stops exactly where the literature says it must. Companion to [`EPSILON-BARRIER.md`](EPSILON-BARRIER.md): that note is the *defense* (what can't separate Collatz); this is the *attack* (what elementary arithmetic + verification actually excludes).

## The mechanism

A nontrivial cycle through `k` odd values, with `L` total halvings in the shortcut map, satisfies the cycle equation `m·(2^L − 3^k) = c(w)`, `c(w) = Σ 3^{k−i} 2^{A_i} > 0`. Because `c(w) < 2^L·3^k`, the cycle **minimum** obeys the rigorous bound

```
m  <  2^L · 3^k / (2^L − 3^k)  =:  CEIL(k, L),    maximized at the smallest gap g(k) = min_{2^L>3^k}(2^L − 3^k).
```

If `CEIL(k) < 2^71` then every `k`-cycle has minimum below the verified range, so — since all `n < 2^71` reach 1 (Bařina 2025) — **no nontrivial `k`-cycle exists**.

## What the elementary bound gives (exact, verified)

- It **excludes every odd-count `k ≤ 43`** *except* `k = 41`. That exception is the continued-fraction convergent `65/41`, whose gap `2⁶⁵ − 3⁴¹ = 420 491 770 248 316 829` is only `1.15×10⁻²` of `3⁴¹` — small enough to defeat the crude ceiling. This is the phenomenon in miniature: **CF convergents are the dangerous cycle-lengths.**
- Measured relative gaps `g(k)/3^k` at the convergents collapse geometrically: `5.35×10⁻²` (8/5), `1.15×10⁻²` (65/41), `1.02×10⁻³` (485/306), `1.82×10⁻⁵` (24727/15601) — while non-convergent neighbours sit near `1` (`0.973` at 19/12, `1.000` at 50508/31867). Any cycle must live at one of these near-integer `L/k` ratios.
- `2⁷¹ = 4·2⁶⁹ > 3·2⁶⁹` — **verified exactly**, so Hercher's threshold condition is met unconditionally.

## Where it hands off (honest boundary)

The elementary ceiling is weak — it dies past `k ≈ 43` because `3^k` alone crosses `2^71`. Turning "the gap must be tiny" into "`k` must be astronomically large" requires a **lower** bound on `|L·log2 − k·log3|`, i.e. **Baker's theory of linear forms in logarithms**. That is precisely the Steiner (1977) → Simons–de Weger → **Hercher (2023)** program, which proves: no nontrivial `m`-cycle for `m ≤ 91`, and — combined with verification below `3·2⁶⁹` — a floor of **≥ 1.375×10¹¹ odd terms** in any nontrivial cycle. That deep input is *cited, not re-derived here*; this note reproduces only the elementary scaffold and the exact gap data it rests on.

## Why this is the honest complement to the ε-barrier

The gap `2^L − 3^k` and the ratio `L/k` are **ε-blind** — identical for `3n+1` and `3n−1`. What breaks the tie is the sign of `c(w)` (the intercept), the one ε-dependent term. So the cycle side of Collatz is settled only by consuming that intercept via genuine Diophantine approximation — exactly what [`EPSILON-BARRIER.md`](EPSILON-BARRIER.md) proves no word-statistic can do. Attack and defense meet at the same object: the arithmetic of `2^L − 3^k` against a positive integer intercept.

## References

- J. L. Simons & B. M. M. de Weger, *Theoretical and computational bounds for m-cycles of the 3n+1 problem*, Acta Arith. (2005).
- T. Hercher, *There are no Collatz-m-cycles with m ≤ 91*, J. Integer Seq. 26 (2023), art. 23.3.5.
- D. Bařina, verification to `2^71` (2025). Reproduce here with `python cycle_gap_check.py`.
