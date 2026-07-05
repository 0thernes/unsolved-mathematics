# Odd-Unit Lock Exact-Height Lab

**Date:** 2026-07-05
**Instrument:** [`odd_unit_lock_height_lab.py`](odd_unit_lock_height_lab.py)
**Related:**
[`ODD-UNIT-LOCK-COVERAGE.md`](ODD-UNIT-LOCK-COVERAGE.md),
[`ODD-UNIT-LOCK-REFINEMENT.md`](ODD-UNIT-LOCK-REFINEMENT.md),
[`ODD-UNIT-LOCK-DIAGONAL.md`](ODD-UNIT-LOCK-DIAGONAL.md),
[`ODD-UNIT-LOCK-TARGET-TAIL.md`](ODD-UNIT-LOCK-TARGET-TAIL.md)
**Results:**
[`results/odd_unit_lock_height_s10_t16_h48_20260705.json`](results/odd_unit_lock_height_s10_t16_h48_20260705.json),
[`results/odd_unit_lock_height_s12_t16_h48_20260705.json`](results/odd_unit_lock_height_s12_t16_h48_20260705.json)

Status: finite exact measurement. This is not a proof of Collatz.

## Why this exists

The coverage and diagonal labs group source alignment by `m mod d`. A real
orbit has an actual alignment height `m`. If it burns `q` full periods of a
source word before colliding with target phase `t`, then

```text
m = t + e + q d,
e = v2(rho_t - eta).
```

The odd-unit lock must use the total odd prefix

```text
a(t) + q * o(source),
```

not just `a(t)`. This lab measures the exact-height union with that
`q`-dependent power of `3` included.

## Source Depth 10, Target Depth 16, Heights 0..48

Command:

```powershell
python experiments/odd_unit_lock_height_lab.py --source-max-depth 10 --source-min-depth 3 --target-max-depth 16 --min-height 0 --max-height 48 --bits '16,20,24' --output experiments/results/odd_unit_lock_height_s10_t16_h48_20260705.json
```

Counts:

| Quantity | Count |
|---|---:|
| Primitive source cycles | 45 |
| Source alignment bins | 386 |
| Unique target spines | 1248 |
| Max observed valuation `e` | 15 |

Coverage over exact source/height bins:

| Extra lock bits `R` | Max coverage | Avg coverage |
|---:|---:|---:|
| 16 | 0.064147949219 | 0.035454851700 |
| 20 | 0.004610061646 | 0.002351636303 |
| 24 | 0.000288128853 | 0.000147234934 |

The densest exact-height bins at `R = 16` cover `2102 / 32768` odd residues,
the same max coverage seen in the diagonal depth-16 target run. This means the
height-aware model reaches the diagonal envelope quickly in the checked finite
library.

## Source Depth 12 Control

Command:

```powershell
python experiments/odd_unit_lock_height_lab.py --source-max-depth 12 --source-min-depth 3 --target-max-depth 16 --min-height 0 --max-height 48 --bits '20,24' --output experiments/results/odd_unit_lock_height_s12_t16_h48_20260705.json
```

Counts:

| Quantity | Count |
|---|---:|
| Primitive source cycles | 160 |
| Source alignment bins | 1715 |
| Unique target spines | 1248 |
| Max observed valuation `e` | 16 |

Coverage:

| Extra lock bits `R` | Max coverage | Avg coverage |
|---:|---:|---:|
| 20 | 0.004615783691 | 0.002337592962 |
| 24 | 0.000288486481 | 0.000146346098 |

The source-depth-12 control matches the source-depth-10 run closely. In this
finite window, source-library growth is not the main danger; target growth and
high-valuation availability are.

## What This Adds

This corrects a possible overcount concern:

```text
mod-class lock union: upper envelope
exact-height lock union: orbit-aligned slice with q-dependent powers of 3
finite result: exact-height slices reach the same envelope quickly because
               target valuations are small in the tested library
```

That is a useful negative result. Exact height alone does not crack the problem.
It sharpens the real proof obligation:

```text
Control high-valuation target availability and target-spine growth as a
function of required precision R along positive orbits.
```

If deep target spines with large `e` remain too sparse, the codimension route
has teeth. If they proliferate at entropy near `2^R`, this route may fail.

## Non-claims

- This is not a proof of Collatz.
- This does not control the infinite target-spine library.
- This does not prove which target spines are dynamically relevant.
- This does not prove independence between repeated exact-height locks.

## Reproduce

```powershell
python experiments/odd_unit_lock_height_lab.py --source-max-depth 10 --source-min-depth 3 --target-max-depth 16 --min-height 0 --max-height 48 --bits '16,20,24' --output experiments/results/odd_unit_lock_height_s10_t16_h48_20260705.json
python experiments/odd_unit_lock_height_lab.py --source-max-depth 12 --source-min-depth 3 --target-max-depth 16 --min-height 0 --max-height 48 --bits '20,24' --output experiments/results/odd_unit_lock_height_s12_t16_h48_20260705.json
python -m py_compile experiments/odd_unit_lock_height_lab.py
```
