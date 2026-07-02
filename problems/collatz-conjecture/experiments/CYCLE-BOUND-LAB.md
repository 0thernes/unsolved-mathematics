# Cycle Bound Lab — the cycle half, derived in-repo

_Created: 2026-07-01. Status: verification/derivation instrument, not proof._

The divergence half of the conjecture has three instruments in this
directory; this adds the missing **cycle half**. It derives, from first
principles with auditable arithmetic, an unconditional lower bound on the
length of any nontrivial Collatz cycle, using only (a) the verified
convergence bound (all n < 2⁷¹ converge — Bařina 2025), and (b) the
continued fraction of log₂3. The argument is the classical Eliahou-style
one; the repo previously *cited* the modern cycle floor, now it can
*re-derive its magnitude*.

## The argument (complete)

Around a nontrivial shortcut-map cycle with k odd steps, ℓ total steps, and
minimum element n_min:

```text
1 = (3^k / 2^ℓ) · ∏_odd (1 + 1/(3nᵢ))     (exact product identity)
⟹ 0 < ℓ − k·log₂3 ≤ k·log₂(1 + 1/(3·n_min)) =: k·δ
```

(Self-test: the trivial cycle 1→2→1 satisfies 2²/3¹ = 4/3 = 1 + 1/(3·1)
exactly.) So ℓ/k approximates log₂3 from above to within δ ≈ 2.04×10⁻²²
per odd step — and best-approximation theory for continued fractions says
approximations that good require enormous k: for k below the next
convergent denominator q_{j+1}, ‖k·log₂3‖ > 1/(q_j + q_{j+1}), forcing
k > 1/(δ·(q_j+q_{j+1})). Laddering over convergents until this threshold
drops below q_{j+1} yields the bound.

## Results (2026-07-01)

```powershell
python experiments/cycle_bound_lab.py                 # n_min = 2^71
python experiments/cycle_bound_lab.py --log2-nmin 68  # older bound, for comparison
```

| Verified bound | Min odd steps k | Min shortcut steps | Min classic steps |
|---|---:|---:|---:|
| 2⁷¹ (current) | **65,470,613,321** | 103,768,467,014 | 169,239,080,335 |
| 2⁶⁸ (2020-era) | 8,517,411,710 | 13,499,778,164 | 22,017,189,874 |

The binding object at 2⁷¹ is the convergent denominator
q₂₂ = 65,470,613,321 of log₂3.

**A pleasing structural observation.** The *next* convergent denominator is
q₂₃ = 137,528,045,312 ≈ 1.37528×10¹¹. Hercher's published floor is stated
as "K ≥ 1.375×10¹¹ odd terms" (given verification to 3·2⁶⁹ < 2⁷¹) — i.e.
exactly q₂₃ rounded down to four significant figures (ratio 1.0002). This
is numerically consistent with his exact bound being this convergent,
which the theory predicts: sharper m-cycle machinery pushes k past our
binding convergent toward the next rung. (Confirming exact equality would
require the constant in his paper's final inequality; not asserted here.)
Either way, the famous number in the literature sits on the
continued-fraction ladder of log₂3. This is
exactly how bounds along this route behave: they climb the convergent
ladder, one rung per improvement, against an infinite ladder.

## Precision honesty

- CF terms of log₂3 are computed at two precisions (150 and 300 digits) and
  only the agreeing prefix (minus a 2-term safety margin) is used; the
  computed prefix [1; 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, …]
  matches the classical expansion, and the convergent self-test pins the
  music-theory denominators 12, 41, 53, 306, 665, 15601.
- Every convergent used by the ladder is numerically re-verified against
  |q·θ − p| < 1/q_next at double precision.
- The bound is **unconditional** (given Bařina's verification) but **not
  new**, and the structural limitation is the whole point: a finite
  computation plus a finite Diophantine bound climbs the convergent ladder
  forever without ever excluding the infinite family. Closing the cycle
  half needs uniform control of 2^ℓ − 3^k — the transcendence-theory gap
  named in [status.md](../status.md).
