# Odd-Unit Lock Bridge Refinement

**Date:** 2026-07-05
**Instrument:** [`odd_unit_lock_bridge_refinement.py`](odd_unit_lock_bridge_refinement.py)
**Input:** [`results/odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json)
**Result:** [`results/odd_unit_lock_bridge_refinement_d13_R16_to_R20_R24_N250000_20260705.json`](results/odd_unit_lock_bridge_refinement_d13_R16_to_R20_R24_N250000_20260705.json)
**Related:**
[`ODD-UNIT-LOCK-BRIDGE-CLASSIFIER.md`](ODD-UNIT-LOCK-BRIDGE-CLASSIFIER.md),
[`ODD-UNIT-LOCK-TRANSITION-WITNESS-MICROSCOPE.md`](ODD-UNIT-LOCK-TRANSITION-WITNESS-MICROSCOPE.md),
[`ODD-UNIT-LOCK-REFINEMENT.md`](ODD-UNIT-LOCK-REFINEMENT.md)

Status: finite bridge-refinement measurement. This proves no part of the
Collatz conjecture.

## Question

The bridge classifier reduced the `73` repeated `R = 16` lock-hit transitions
from the `250,000` odd-start scan to `4` exact affine bridge geometries.

This follow-up asks the dangerous question directly:

```text
If the previous R=16 odd-unit lock is lifted to R=20 or R=24,
does the same shortcut bridge still land in a next odd-unit lock?
```

If yes, then repeated locks may have a persistent high-precision transition
mechanism. If no, then the observed `R = 16` clustering is compatible with the
codimension/refinement story.

## Main Result

All measured base bridges die as repeated locks after refinement.

| Quantity | Value |
|---|---:|
| Base precision | `R = 16` |
| Higher precisions tested | `R = 20, 24` |
| Bridge geometries checked | `4` |
| Total higher-precision refinement checks | `8` |
| Higher-precision previous-lock lifts found | `8` |
| Higher-precision repeated next-lock hits | `0` |
| Low-projection mismatches | `2` |

By family:

| Source pair | Base repeat count | Fresh quotient bits at R=16 bridge | R=20 previous lifts | R=20 repeats | R=24 previous lifts | R=24 repeats |
|---|---:|---:|---:|---:|---:|---:|
| `0111 -> 001111` | 62 | 7 | 1 | 0 | 1 | 0 |
| `011 -> 011` | 7 | 0 | 1 | 0 | 1 | 0 |
| `0011101111 -> 011101111` | 3 | 0 | 1 | 0 | 1 | 0 |
| `011 -> 011` | 1 | 0 | 1 | 0 | 1 | 0 |

The dominant `0111 -> 001111` bridge is even less stable than the low-precision
picture suggests: both higher-precision lifts project to a different current
`R = 16` unit residue than the original measured bridge. The other
alignment-drop bridges preserve the low current projection, but still fail to
be higher-precision next-lock hits.

## Interpretation

This is the strongest local evidence so far against a persistent repeated-lock
mechanism in the measured window.

The static coverage and refinement labs showed that high-precision odd-unit
lock sets are thin. The transition microscope showed that coarse lock hits are
not independent and can cluster at `R = 16`. The bridge classifier showed that
the clustering collapses into a small number of exact affine bridges. This
refinement pass adds:

```text
Those measured bridges do not survive as repeated locks at R=20 or R=24.
```

That does not prove Collatz. It does, however, improve the theorem target:
instead of trying to assume independent sparse events, prove that repeated
bridge families either acquire fresh quotient-bit cost or lose refined lock
depth.

## Theorem Target

A useful next lemma would look like:

```text
For any repeated odd-unit lock bridge at precision R, either

1. the bridge imposes positive fresh quotient-bit cost under the affine
   state-coordinate map, or
2. it is an alignment-drop bridge whose repeated-lock depth is uniformly
   bounded under refinement.
```

This would still need a separate entropy comparison for the number of
dynamically relevant target locks, plus a way to cover new bridge geometries at
larger depth. But it would remove the biggest local loophole exposed by the
transition-memory lab.

## Non-Claims

- This is not a proof of Collatz.
- It refines only the four measured `R = 16` bridge geometries from the
  depth-13, odd-start scan through `250,000`.
- It does not classify bridge geometries that appear at larger depth, larger
  start bounds, or different source/target libraries.
- It does not prove that every alignment-drop bridge is harmless.
- It does not prove the global entropy-vs-precision comparison.

## Reproduce

```powershell
python -m py_compile experiments\odd_unit_lock_bridge_refinement.py
python experiments\odd_unit_lock_bridge_refinement.py --classifier experiments\results\odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json --output experiments\results\odd_unit_lock_bridge_refinement_d13_R16_to_R20_R24_N250000_20260705.json
```
