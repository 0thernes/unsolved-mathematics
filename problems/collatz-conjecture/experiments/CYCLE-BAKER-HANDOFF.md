# Cycle exclusion: the linear-form records and the exact Baker handoff

**Date:** 2026-07-02
**Instrument:** [`cycle_baker_check.py`](cycle_baker_check.py) → [`results/cycle_baker.json`](results/cycle_baker.json)
**Status:** exact measured data + honest citation boundary. Deepens [`CYCLE-GAP.md`](CYCLE-GAP.md). **Not a proof.**

## The controlling quantity

A nontrivial cycle with `k` odd steps needs the linear form in logarithms
`λ(k) = L·ln2 − k·ln3 = ln(2^L/3^k) > 0` (with `L = bitlen(3^k)`) to be small, and the
cycle minimum obeys `m < 3^k/(2^λ − 1) ≈ 3^k/λ`. So a cycle with minimum above the
verified `2^71` can only live where `λ(k)` is tiny.

## Measured record-small λ(k) (the dangerous lengths)

| k | L | λ(k) | cycle-min ceiling can exceed 2⁷¹? |
|---|---|------|---|
| 1 | 2 | 2.88e−1 | no |
| 3 | 5 | 1.70e−1 | no |
| 5 | 8 | 5.21e−2 | no |
| 17 | 27 | 3.86e−2 | no |
| 29 | 46 | 2.50e−2 | no |
| **41** | **65** | **1.15e−2** | **yes ← first** |
| 94 | 149 | 9.38e−3 | yes |
| 147 | 233 | 7.29e−3 | yes |
| 200 | 317 | 5.20e−3 | yes |
| 253 | 401 | 3.11e−3 | yes |

Record-small `λ` lands on the one-sided best approximants of `log₂3`. The **first `k` the elementary ceiling cannot exclude is `k = 41`** — the continued-fraction convergent `65/41` — in exact agreement with [`CYCLE-GAP.md`](CYCLE-GAP.md). Below that, every cycle length is excluded outright by `m < 2^71` + verification.

## The exact handoff (honest boundary)

Elementary arithmetic pins `λ(k)` only at the convergents it can enumerate; it gives **no uniform lower bound** valid for all `k`. Such a bound would require `log₂3` to have bounded partial quotients — **unproven** (the CF already shows a partial quotient `23`). The uniform bound

```
λ(k) = |L·ln2 − k·ln3|  >  c · k^(−κ)      (effective c, κ)
```

is **Baker's theory of effective linear forms in logarithms** (with the sharp effective irrationality measure of `log₂3` due to Rhin and successors, and Nesterenko-type estimates). That is precisely the input the Steiner (1977) → Simons–de Weger (2005) → **Hercher (2023)** program uses to convert "λ small only at convergents" into "any nontrivial cycle has `≥ 1.375×10¹¹` odd terms" (unconditional once verification passes `3·2⁶⁹`, which `2⁷¹` does).

**So the elementary/transcendence boundary is exactly here:** everything up to enumerating the gaps at convergents is elementary and reproduced in this repo; the *uniform* control of `λ(k)` — hence the real cycle-length floor — is effective transcendence, cited not re-derived.

## References
- C. J. Everett–style + R. P. Steiner, *A theorem on the Syracuse problem* (1977).
- J. L. Simons & B. M. M. de Weger, Acta Arith. (2005). — T. Hercher, J. Integer Seq. 26 (2023), art. 23.3.5.
- G. Rhin, effective irrationality measures for logarithms of rationals; Yu. Nesterenko, linear forms in logarithms. Reproduce here: `python cycle_baker_check.py`.
