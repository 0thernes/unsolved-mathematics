# Odd-Unit Lock Diagonal Target-Growth Lab

**Date:** 2026-07-05
**Instrument:** [`odd_unit_lock_diagonal_lab.py`](odd_unit_lock_diagonal_lab.py)
**Related:**
[`ODD-UNIT-LOCK-COVERAGE.md`](ODD-UNIT-LOCK-COVERAGE.md),
[`ODD-UNIT-LOCK-REFINEMENT.md`](ODD-UNIT-LOCK-REFINEMENT.md),
[`ODD-UNIT-LOCK-HEIGHT.md`](ODD-UNIT-LOCK-HEIGHT.md),
[`ODD-UNIT-LOCK-TARGET-TAIL.md`](ODD-UNIT-LOCK-TARGET-TAIL.md)
**Results:**
[`results/odd_unit_lock_diagonal_s10_t15_20260705.json`](results/odd_unit_lock_diagonal_s10_t15_20260705.json),
[`results/odd_unit_lock_diagonal_s10_t16_r24_20260705.json`](results/odd_unit_lock_diagonal_s10_t16_r24_20260705.json),
[`results/odd_unit_lock_diagonal_s12_t15_20260705.json`](results/odd_unit_lock_diagonal_s12_t15_20260705.json)

Status: finite exact measurement. This is not a proof of Collatz.

## Why this exists

Fixed target-spine libraries thin out at high 2-adic precision for a simple
reason: each target lock contributes one residue class modulo `2^R`.

So the real diagonal question is:

```text
As target spines get deeper, do newly added target locks refill odd-unit space
faster than precision removes it?
```

This lab fixes a source-spine library, grows the target-spine library by depth,
and measures coverage at several precisions.

## Source Depth 10, Target Depth 10..15

Command:

```powershell
python experiments/odd_unit_lock_diagonal_lab.py --source-max-depth 10 --source-min-depth 3 --target-depths 10,12,14,15 --bits '12,16,20' --output experiments/results/odd_unit_lock_diagonal_s10_t15_20260705.json
```

Counts:

| Quantity | Count |
|---|---:|
| Primitive source cycles | 45 |
| Source alignment bins | 386 |

Average coverage:

| Target depth | Target spines | R=12 | R=16 | R=20 |
|---:|---:|---:|---:|---:|
| 10 | 46 | 0.021674121600 | 0.001363803686 | 0.000085237730 |
| 12 | 161 | 0.072586929242 | 0.004868186200 | 0.000304582823 |
| 14 | 491 | 0.112953620871 | 0.014750979725 | 0.000933439620 |
| 15 | 820 | 0.117227979275 | 0.024221706885 | 0.001560389069 |

Max-bin coverage:

| Target depth | R=12 | R=16 | R=20 |
|---:|---:|---:|---:|
| 10 | 0.031738281250 | 0.001983642578 | 0.000123977661 |
| 12 | 0.113769531250 | 0.008392333984 | 0.000524520874 |
| 14 | 0.176757812500 | 0.027893066406 | 0.001764297485 |
| 15 | 0.177734375000 | 0.045623779297 | 0.003015518188 |

Target growth matters, but precision still dominates in this window. At target
depth 15, increasing R from 16 to 20 drops average coverage from about `2.42%`
to about `0.156%`.

## Source Depth 10, Target Depth 16, R up to 24

Command:

```powershell
python experiments/odd_unit_lock_diagonal_lab.py --source-max-depth 10 --source-min-depth 3 --target-depths 12,14,15,16 --bits '16,20,24' --output experiments/results/odd_unit_lock_diagonal_s10_t16_r24_20260705.json
```

Average coverage:

| Target depth | Target spines | R=16 | R=20 | R=24 |
|---:|---:|---:|---:|---:|
| 12 | 161 | 0.004868186200 | 0.000304582823 | 0.000019036426 |
| 14 | 491 | 0.014750979725 | 0.000933439620 | 0.000058375492 |
| 15 | 820 | 0.024221706885 | 0.001560389069 | 0.000097595348 |
| 16 | 1248 | 0.035848825089 | 0.002373576782 | 0.000148601483 |

Max-bin coverage:

| Target depth | R=16 | R=20 | R=24 |
|---:|---:|---:|---:|
| 12 | 0.008392333984 | 0.000524520874 | 0.000032782555 |
| 14 | 0.027893066406 | 0.001764297485 | 0.000110268593 |
| 15 | 0.045623779297 | 0.003015518188 | 0.000188469887 |
| 16 | 0.064147949219 | 0.004610061646 | 0.000288128853 |

This is the clean diagonal signal. From R=16 to R=20 to R=24, the drop is still
close to the expected `16x` per four added precision bits, even while the target
library grows to 1248 spines.

## Source Depth 12 Control

Command:

```powershell
python experiments/odd_unit_lock_diagonal_lab.py --source-max-depth 12 --source-min-depth 3 --target-depths 12,14,15 --bits '16,20' --output experiments/results/odd_unit_lock_diagonal_s12_t15_20260705.json
```

Counts:

| Quantity | Count |
|---|---:|
| Primitive source cycles | 160 |
| Source alignment bins | 1715 |

Average coverage:

| Target depth | Target spines | R=16 | R=20 |
|---:|---:|---:|---:|
| 12 | 161 | 0.004866512732 | 0.000304475123 |
| 14 | 491 | 0.014749634857 | 0.000933359663 |
| 15 | 820 | 0.024202325671 | 0.001560331295 |

Max-bin coverage:

| Target depth | R=16 | R=20 |
|---:|---:|---:|
| 12 | 0.008392333984 | 0.000524520874 |
| 14 | 0.027923583984 | 0.001766204834 |
| 15 | 0.045684814453 | 0.003019332886 |

The depth-12 source control nearly matches the depth-10 source run. In this
finite window, target-library growth is the main coverage driver; source-library
growth does not erase the precision loss.

## What This Adds

The diagonal data separates the real obstruction from a finite-library artifact:

```text
fixed targets thin out: expected
targets grow with depth: dangerous
targets grow through depth 16: still far slower than R=24 precision loss
```

The next theorem target is now cleaner:

```text
Bound the number of relevant target-spine locks available to a positive orbit
as a function of the required odd-unit precision R.  If relevant target growth
is o(2^R), or more sharply if it grows with entropy below the precision loss,
then repeated regeneration becomes a vanishing channel.
```

This does not prove Collatz, but it turns the odd-unit route into a precise
entropy-vs-precision problem.

The exact-height companion checks the orbit-aligned version of this envelope:
actual alignment height `m`, period burn `q`, and the resulting `3^(q o)`
factor in the odd-unit residue. In the tested window, the exact-height slices
reach the same diagonal envelope quickly because observed target valuations are
small.

The target-tail companion isolates where the first high-valuation refill comes
from: finite depth-22 periodic echoes near source phase `t = 0`, not a diffuse
target-library entropy flood.

## Non-claims

- This is not a proof of Collatz.
- This does not show the infinite target library is harmless.
- This does not prove which target spines are dynamically relevant to a
  positive orbit.
- This does not prove independence between repeated regeneration events.

## Reproduce

```powershell
python experiments/odd_unit_lock_diagonal_lab.py --source-max-depth 10 --source-min-depth 3 --target-depths 10,12,14,15 --bits '12,16,20' --output experiments/results/odd_unit_lock_diagonal_s10_t15_20260705.json
python experiments/odd_unit_lock_diagonal_lab.py --source-max-depth 10 --source-min-depth 3 --target-depths 12,14,15,16 --bits '16,20,24' --output experiments/results/odd_unit_lock_diagonal_s10_t16_r24_20260705.json
python experiments/odd_unit_lock_diagonal_lab.py --source-max-depth 12 --source-min-depth 3 --target-depths 12,14,15 --bits '16,20' --output experiments/results/odd_unit_lock_diagonal_s12_t15_20260705.json
python -m py_compile experiments/odd_unit_lock_diagonal_lab.py
```
