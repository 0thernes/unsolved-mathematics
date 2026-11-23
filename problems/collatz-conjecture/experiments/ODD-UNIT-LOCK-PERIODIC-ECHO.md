# Odd-Unit Lock Periodic-Echo Classifier

**Date:** 2026-07-05
**Instrument:** [`odd_unit_lock_periodic_echo_lab.py`](odd_unit_lock_periodic_echo_lab.py)
**Related:**
[`ODD-UNIT-LOCK-TARGET-TAIL.md`](ODD-UNIT-LOCK-TARGET-TAIL.md),
[`ODD-UNIT-LOCK-HEIGHT.md`](ODD-UNIT-LOCK-HEIGHT.md),
[`ODD-UNIT-LOCK-DIAGONAL.md`](ODD-UNIT-LOCK-DIAGONAL.md)
**Results:**
[`results/odd_unit_lock_periodic_echo_s10_t22_e16_20260705.json`](results/odd_unit_lock_periodic_echo_s10_t22_e16_20260705.json),
[`results/odd_unit_lock_periodic_echo_s10_t22_e18_20260705.json`](results/odd_unit_lock_periodic_echo_s10_t22_e18_20260705.json)

Status: finite exact classification plus a parity-code lemma target. This is
not a proof of Collatz.

## Why this exists

The target-tail lab found the first high-valuation shelf:

```text
e = v2(rho_t - eta) >= 20
```

at source depth 10 and target depth 22. The top witnesses looked like long
near-repetitions of the source word. This classifier asks whether that is the
whole mechanism.

## Parity-Code Reading

For the shortcut map, a parity prefix of length `k` determines a unique residue
class modulo `2^k`. Therefore, if two 2-adic points have parity itineraries
that agree for exactly `k` steps and then differ, their difference has
`v2 = k`.

For a source phase `rho_t`, the parity itinerary is the source phase word
repeated forever. For a target spine `eta`, the itinerary is the target word
repeated forever. So a high value of

```text
v2(rho_t - eta)
```

should be read as a long common parity prefix between a repeated source phase
and a primitive target word.

That means the scary target-tail shelf is not an undifferentiated 2-adic
coincidence. It is a periodic-prefix echo.

## Source Depth 10, Target Depth 22, e >= 16

Command:

```powershell
python experiments/odd_unit_lock_periodic_echo_lab.py --source-max-depth 10 --source-min-depth 3 --target-max-depth 22 --target-cutoff 22 --threshold 16 --max-records 512 --output experiments/results/odd_unit_lock_periodic_echo_s10_t22_e16_20260705.json
```

Counts:

| Quantity | Count |
|---|---:|
| Primitive source cycles | 45 |
| Source phases | 386 |
| Target spines | 52,812 |
| Source phase / target pairs | 20,385,387 |
| Records with `e >= 16` | 378 |

Classification:

| Diagnostic | Value |
|---|---:|
| Phase `t = 0` records | 378 / 378 |
| Periodic prefix length >= `16` | 378 / 378 |
| Periodic prefix length >= valuation `e` | 378 / 378 |
| `e - periodic_prefix_len = 0` | 378 / 378 |
| Minimum periodic-prefix fraction | 0.727272727 |
| Maximum valuation `e` | 21 |

Valuation histogram:

| `e` | Count |
|---:|---:|
| 16 | 127 |
| 17 | 38 |
| 18 | 114 |
| 19 | 35 |
| 20 | 49 |
| 21 | 15 |

Echo-defect length, meaning target length minus periodic-prefix length:

| Defect length | Count |
|---:|---:|
| 1 | 82 |
| 2 | 68 |
| 3 | 65 |
| 4 | 73 |
| 5 | 45 |
| 6 | 45 |

## Source Depth 10, Target Depth 22, e >= 18

The stricter shelf has `213` records. Again:

```text
all records are phase t = 0
all records satisfy e = periodic_prefix_len
```

The defect length shrinks to `1..4`:

| Defect length | Count |
|---:|---:|
| 1 | 68 |
| 2 | 54 |
| 3 | 46 |
| 4 | 45 |

## Interpretation

This turns the target-tail question into a cleaner counting problem.

Old vague version:

```text
Do deeper target spines refill high-precision odd-unit locks?
```

Sharper version:

```text
How many primitive target words of depth L can shadow a repeated source phase
for p = L - defect bits, and do those primitive-breaking suffixes survive
odd-unit refinement or dynamic bridge persistence?
```

This is a better theorem target because the high-valuation mechanism is no
longer mysterious. In this finite window, every high-tail record is explained
by a parity-prefix echo, and the valuation is exactly the common-prefix length.

## Non-claims

- This is not a proof of Collatz.
- The parity-code observation is not new mathematics; it is the Terras
  cylinder bijection in this repo's odd-unit-lock coordinates.
- The finite classifier only checks source depth 10 and target depth 22.
- It does not prove all high-tail records at larger depth are periodic echoes.
- It does not prove the echo families are dynamically harmless.

## Reproduce

```powershell
python experiments/odd_unit_lock_periodic_echo_lab.py --source-max-depth 10 --source-min-depth 3 --target-max-depth 22 --target-cutoff 22 --threshold 16 --max-records 512 --output experiments/results/odd_unit_lock_periodic_echo_s10_t22_e16_20260705.json
python experiments/odd_unit_lock_periodic_echo_lab.py --source-max-depth 10 --source-min-depth 3 --target-max-depth 22 --target-cutoff 22 --threshold 18 --max-records 512 --output experiments/results/odd_unit_lock_periodic_echo_s10_t22_e18_20260705.json
python -m py_compile experiments/odd_unit_lock_periodic_echo_lab.py
```
