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
[`results/odd_unit_lock_target_tail_s10_t22_20260705.json`](results/odd_unit_lock_target_tail_s10_t22_20260705.json),
[`results/odd_unit_lock_target_tail_s10_t24_t26_catalytic_20261127.json`](results/odd_unit_lock_target_tail_s10_t24_t26_catalytic_20261127.json),
[`results/odd_unit_lock_target_tail_s12_t24_t26_catalytic_20261127.json`](results/odd_unit_lock_target_tail_s12_t24_t26_catalytic_20261127.json)

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

## Catalytic Native Frontier Extension: Target Depth 26 (`884,406,475` Exact Pairs, `2026-11-27`)

Using the zero-workspace catalytic native C17/BMI2 accelerator ([`../native/collatz_catalytic.c`](../native/collatz_catalytic.c), cross-verified 100% bit-for-bit against the independent safe Rust oracle [`../native/collatz_catalytic_oracle.rs`](../native/collatz_catalytic_oracle.rs) and the exact Python `Fraction` oracle; see [`../../../docs/benchmarks.md`](../../../docs/benchmarks.md)), we extended exact target-tail measurement through **target depth 26** (`515,689` unique supercritical target spines):

| Window | Exact Pairs | `max_e` | `e >= 16` | `e >= 18` | `e >= 20` | `e >= 22` | `e >= 24` | `e >= 26` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `s<=10, t<=24` | `55,609,045` | `23` | `1,010` (`1.19x`) | `609` (`2.87x`) | `214` (`4.04x`) | `26` (`1.96x`) | `0` | `0` |
| `s<=10, t<=26` | `199,055,909` | `25` | `2,670` (`0.88x`) | `1,684` (`2.22x`) | `614` (`3.23x`) | `111` (`2.34x`) | `36` (`3.03x`) | `0` |
| `s<=12, t<=24` | `247,071,315` | `23` | `3,417` (`0.91x`) | `1,424` (`1.51x`) | `498` (`2.11x`) | `153` (`2.60x`) | `0` | `0` |
| `s<=12, t<=26` | `884,406,475` | `25` | `10,002` (`0.74x`) | `4,321` (`1.28x`) | `1,737` (`2.06x`) | `770` (`3.65x`) | `234` (`4.44x`) | `0` |

### Key Structural Finding at `t <= 26`

1. **Exact echo rigidity at high valuations:** For `s <= 10, t <= 26`, **100%** of hits at `e >= 16` (`2,670/2,670`) are `phase_t = 0` exact echoes (`e == periodic_prefix_len`), peaking at `e = 25` (`36/36` hits at `e >= 24` have `pfx >= 90%`, top witness `source=01111`, `target=01111011110111101111011111`, `e=25`). For `s <= 12, t <= 26`, **100%** of hits at `e >= 18` (`4,321/4,321`), `e >= 20` (`1,737/1,737`), `e >= 22` (`770/770`), and `e >= 24` (`234/234`) are `phase_t = 0` exact echoes, with **`0` hits at `e >= 26`**.
2. **Isolated Lyndon Periodic Wrap-Around Witness (`e > target_depth`):** Across all `884,406,475` exact pairs in `s <= 12, t <= 26`, at `e >= 16` (`10,002` hits), `21` hits occur at non-zero phase rotations (`phase_t != 0`) and **exactly `1` Lyndon target word** exhibits a periodic wrap-around echo where `e > target_depth`:
   - `source = 010101011111` (`|w| = 12`), `phase_t = 2` (`phase_word = 010101111101`), `target = 0101011111` (`|v| = 10`), achieving `e = v2(rho_t - eta) = 16 > 10`, strictly bounded by our Lean 4.35.0 Fine–Wilf ceiling (`thm_collatz_fine_wilf_spine_ceiling`): $|w| + |v| - \gcd(|w|, |v|) = 12 + 10 - 2 = 20$.
3. **Python RAM Bug Fixed (`V90-BUG-01`):** `odd_unit_lock_target_tail_lab.py` previously appended every pair's valuation into `e_values: list[int]` ($O(\text{pairs})$ heap explosion); `v0.9.0` computes `max_valuation_e` and `avg_valuation_e` in $O(1)$ space from `e_sum`/`max_e` while preserving bit-for-bit identical output.

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
