# Odd-Unit Lock Target-Tail Lab

**Date:** 2026-07-05
**Instrument:** [`odd_unit_lock_target_tail_lab.py`](odd_unit_lock_target_tail_lab.py)
**Related:**
[`ODD-UNIT-LOCK-COVERAGE.md`](ODD-UNIT-LOCK-COVERAGE.md),
[`ODD-UNIT-LOCK-DIAGONAL.md`](ODD-UNIT-LOCK-DIAGONAL.md),
[`ODD-UNIT-LOCK-HEIGHT.md`](ODD-UNIT-LOCK-HEIGHT.md),
[`ODD-UNIT-LOCK-PERIODIC-ECHO.md`](ODD-UNIT-LOCK-PERIODIC-ECHO.md)
**Results:**
[`results/odd_unit_lock_target_tail_s10_t20_20260705.json`](results/odd_unit_lock_target_tail_s10_t20_20260705.json),
[`results/odd_unit_lock_target_tail_s12_t20_20260705.json`](results/odd_unit_lock_target_tail_s12_t20_20260705.json),
[`results/odd_unit_lock_target_tail_s10_t22_20260705.json`](results/odd_unit_lock_target_tail_s10_t22_20260705.json)

Status: finite exact measurement. This is not a proof of Collatz.

## Why this exists

The exact-height lab reduced the next odd-unit-lock proof obligation to target
spines with unusually high

```text
e = v2(rho_t - eta),
```

where `rho_t` is a source phase and `eta` is a target spine. If the count of
large-`e` target spines grows too quickly, deeper target libraries can refill
the lock space. If that tail is sparse or structurally classifiable, the
codimension route still has a real obstruction to exploit.

This lab measures the finite tail

```text
#{(source phase, target spine): v2(rho_t - eta) >= r}
```

and compares it to the naive geometric baseline `2^-r`.

## Source Depth 10, Target Depth 22

Command:

```powershell
python experiments/odd_unit_lock_target_tail_lab.py --source-max-depth 10 --source-min-depth 3 --target-max-depth 22 --target-cutoffs 18,20,22 --thresholds '8,10,12,14,16,18,20,22,24,26' --output experiments/results/odd_unit_lock_target_tail_s10_t22_20260705.json
```

Counts:

| Quantity | Count |
|---|---:|
| Primitive source cycles | 45 |
| Source phases | 386 |
| Unique target spines through depth 22 | 52,812 |

Tail summary at target cutoff 22:

| Threshold | Observed count | Geometric expected | Observed / geometric |
|---:|---:|---:|---:|
| `e >= 12` | 2,313 | 4,976.901123 | 0.464747 |
| `e >= 14` | 865 | 1,244.225281 | 0.695212 |
| `e >= 16` | 378 | 311.056320 | 1.215214 |
| `e >= 18` | 213 | 77.764080 | 2.739054 |
| `e >= 20` | 64 | 19.441020 | 3.292008 |
| `e >= 22` | 0 | 4.860255 | 0.000000 |

The first high-tail shelf appears at `e >= 20`, but it does not continue to
`e >= 22` in this finite window.

## Periodic-Echo Shelf

The `e >= 20` hits are not diffuse random-looking hits. At target cutoff 22:

| Diagnostic | Value |
|---|---:|
| `e >= 20` hits | 64 |
| Phase `t = 0` hits | 64 |
| Target depths 21 / 22 | 24 / 40 |
| Periodic-prefix >= 75% of target | 64 |
| Periodic-prefix >= 90% of target | 64 |

The top witnesses are long near-repetitions of the source word with a small
primitive-breaking deformation near the end:

| Source | Target | `e` | Periodic prefix |
|---|---|---:|---:|
| `011` | `0110110110110110110111` | 21 | 21 / 22 |
| `0011111` | `0011111001111100111111` | 21 | 21 / 22 |
| `0101111` | `0101111010111101011111` | 21 | 21 / 22 |
| `0110111` | `0110111011011101101111` | 21 | 21 / 22 |
| `0111111` | `0111111011111101111111` | 21 | 21 / 22 |

This is the useful weird thing: the first target-depth-22 high-valuation refill
is a periodic echo shelf, not an undifferentiated entropy flood.

The periodic-echo classifier sharpens this further: in the finite
source-depth-10 / target-depth-22 window, all `e >= 16` target-tail records are
phase-0 echoes and satisfy `e = periodic_prefix_len`. That is the Terras
parity-code cylinder metric showing up inside the odd-unit-lock coordinates.

## Source Depth 12 Control

Command:

```powershell
python experiments/odd_unit_lock_target_tail_lab.py --source-max-depth 12 --source-min-depth 3 --target-max-depth 20 --target-cutoffs 16,18,20 --thresholds '8,10,12,14,16,18,20,22,24' --output experiments/results/odd_unit_lock_target_tail_s12_t20_20260705.json
```

Counts:

| Quantity | Count |
|---|---:|
| Primitive source cycles | 160 |
| Source phases | 1,715 |
| Unique target spines through depth 20 | 16,100 |

Tail summary at target cutoff 20:

| Threshold | Observed count | Geometric expected | Observed / geometric |
|---:|---:|---:|---:|
| `e >= 12` | 10,028 | 6,741.049805 | 1.487602 |
| `e >= 14` | 1,249 | 1,685.262451 | 0.741131 |
| `e >= 16` | 395 | 421.315613 | 0.937539 |
| `e >= 18` | 113 | 105.328903 | 1.072830 |
| `e >= 20` | 0 | 26.332226 | 0.000000 |

Adding many more source phases does not create an `e >= 20` tail through target
depth 20.

## Interpretation

This does not prove the odd-unit route. It does sharpen it.

The apparent next theorem target is no longer just "target growth is sparse."
It is more specific:

```text
Classify and bound primitive-breaking periodic echoes near source phases.
```

If those echoes can be shown to consume fresh quotient bits or fail persistence
under precision lift, they become a finite-geometry nuisance rather than a
proof-killing entropy source. If they proliferate indefinitely at the necessary
precision, this route may fail.

## Non-claims

- This is not a proof of Collatz.
- This does not control all target depths.
- This does not prove the periodic-echo shelf is the only high-valuation
  mechanism.
- This does not prove dynamic relevance along positive integer orbits.
- This does not prove independence or non-persistence of repeated locks.

## Reproduce

```powershell
python experiments/odd_unit_lock_target_tail_lab.py --source-max-depth 10 --source-min-depth 3 --target-max-depth 20 --target-cutoffs '12,14,16,18,20' --thresholds '8,10,12,14,16,18,20,22,24' --output experiments/results/odd_unit_lock_target_tail_s10_t20_20260705.json
python experiments/odd_unit_lock_target_tail_lab.py --source-max-depth 12 --source-min-depth 3 --target-max-depth 20 --target-cutoffs '16,18,20' --thresholds '8,10,12,14,16,18,20,22,24' --output experiments/results/odd_unit_lock_target_tail_s12_t20_20260705.json
python experiments/odd_unit_lock_target_tail_lab.py --source-max-depth 10 --source-min-depth 3 --target-max-depth 22 --target-cutoffs '18,20,22' --thresholds '8,10,12,14,16,18,20,22,24,26' --output experiments/results/odd_unit_lock_target_tail_s10_t22_20260705.json
python -m py_compile experiments/odd_unit_lock_target_tail_lab.py
```
