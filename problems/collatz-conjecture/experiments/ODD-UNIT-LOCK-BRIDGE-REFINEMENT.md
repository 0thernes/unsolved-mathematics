# Odd-Unit Lock Bridge Refinement

**Date:** 2026-07-05
**Instrument:** [`odd_unit_lock_bridge_refinement.py`](odd_unit_lock_bridge_refinement.py)
**Input:** [`results/odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json)
**Result:** [`results/odd_unit_lock_bridge_refinement_d13_R16_to_R20_R24_N250000_20260705.json`](results/odd_unit_lock_bridge_refinement_d13_R16_to_R20_R24_N250000_20260705.json)
**Related:**
[`ODD-UNIT-LOCK-BRIDGE-CLASSIFIER.md`](ODD-UNIT-LOCK-BRIDGE-CLASSIFIER.md),
[`ODD-UNIT-LOCK-TRANSITION-WITNESS-MICROSCOPE.md`](ODD-UNIT-LOCK-TRANSITION-WITNESS-MICROSCOPE.md),
[`ODD-UNIT-LOCK-REFINEMENT.md`](ODD-UNIT-LOCK-REFINEMENT.md),
[`ODD-UNIT-LOCK-PERSISTENCE-LADDER.md`](ODD-UNIT-LOCK-PERSISTENCE-LADDER.md),
[`ODD-UNIT-LOCK-ALIGNMENT-DROP.md`](ODD-UNIT-LOCK-ALIGNMENT-DROP.md),
[`ODD-UNIT-LOCK-BRIDGE-STATE-LIFT.md`](ODD-UNIT-LOCK-BRIDGE-STATE-LIFT.md)

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

## R = 17 Stress Follow-Up

The `R = 17`, odd-start scan through `1,000,000` finds only `4`
hit-after-hit transitions against local-coverage expectation
`136.842514038086`. Those four repeats collapse to two exact zero-fresh bridge
geometries:

| Source pair | Base repeat count | Fresh quotient bits at R=17 bridge | R=20 previous lifts | R=20 repeats | R=24 previous lifts | R=24 repeats |
|---|---:|---:|---:|---:|---:|---:|
| `0011111 -> 011111` | 3 | 0 | 1 | 0 | 1 | 0 |
| `0110111111 -> 0111111` | 1 | 0 | 1 | 0 | 1 | 0 |

Result files:
[`results/odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json)
and
[`results/odd_unit_lock_bridge_refinement_d13_R17_to_R20_R24_N1000000_20260705.json`](results/odd_unit_lock_bridge_refinement_d13_R17_to_R20_R24_N1000000_20260705.json).

Interpretation: the alignment-drop loophole is not gone, but the measured
larger-window instances still lose refined lock depth at `R = 20` and `R = 24`.

## R = 18 Stress Follow-Up

The `R = 18`, odd-start scan through `1,000,000` finds only `3`
hit-after-hit transitions against local-coverage expectation
`47.528289794922`, keeping only the dominant `R = 17` stress bridge alive:

| Source pair | Base repeat count | Fresh quotient bits at R=18 bridge | R=20 previous lifts | R=20 repeats | R=24 previous lifts | R=24 repeats |
|---|---:|---:|---:|---:|---:|---:|
| `0011111 -> 011111` | 3 | 0 | 1 | 0 | 1 | 0 |

Result files:
[`results/odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json)
and
[`results/odd_unit_lock_bridge_refinement_d13_R18_to_R20_R24_N1000000_20260705.json`](results/odd_unit_lock_bridge_refinement_d13_R18_to_R20_R24_N1000000_20260705.json).

Interpretation: in this finite depth-13 configuration, the one-million stress
ladder has two `R = 17` bridge families, one `R = 18` bridge family, and no
`R = 19` repeated locks despite local-coverage expectation `17.202903747559`.
The surviving `R = 18` measured bridge still loses refined lock depth at
`R = 20` and `R = 24`.

The state-lift follow-up adds the missing intermediate precision. The
`400252 -> 200126` bridge survives algebraically at `R = 19`, but the required
previous state class lifts to `400252 + 2^28 (mod 2^29)`, so the observed low
representative state is no longer a repeated-lock state at that precision.

## Depth-14 Stress Follow-Up

The depth-14 scan through odd starts `<= 250,000` creates more coarse bridge
families, but the measured `R = 17` survivors still fail as repeated locks when
lifted to `R = 20` and `R = 24`.

| Source pair | Base repeat count | Fresh quotient bits at R=17 bridge | R=20 previous lifts | R=20 repeats | R=24 previous lifts | R=24 repeats |
|---|---:|---:|---:|---:|---:|---:|
| `00110111011101 -> 01101110111` | 12 | 0 | 1 | 0 | 1 | 0 |
| `001111101 -> 011111` | 2 | 0 | 1 | 0 | 1 | 0 |
| `011 -> 0111` | 1 | 6 | 1 | 0 | 1 | 0 |

Result files:
[`results/odd_unit_lock_bridge_classifier_d14_R17_N250000_20260705.json`](results/odd_unit_lock_bridge_classifier_d14_R17_N250000_20260705.json)
and
[`results/odd_unit_lock_bridge_refinement_d14_R17_to_R20_R24_N250000_20260705.json`](results/odd_unit_lock_bridge_refinement_d14_R17_to_R20_R24_N250000_20260705.json).

Interpretation: raising the finite source/target library to depth `14` exposes
new bridge families, including two zero-fresh alignment-drop bridges. The
current finite evidence still supports bounded refinement death, but the proof
target must classify bridge families uniformly as the library grows.

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
- The R17/R18 stress follow-up refines only the measured bridge geometries from
  the depth-13, odd-start scan through `1,000,000`.
- The depth-14 stress follow-up refines only the measured `R = 17` bridge
  geometries from the depth-14, odd-start scan through `250,000`.
- It does not classify bridge geometries that appear at larger depth, larger
  start bounds, or different source/target libraries.
- It does not prove that every alignment-drop bridge is harmless.
- It does not prove the global entropy-vs-precision comparison.

## Reproduce

```powershell
python -m py_compile experiments\odd_unit_lock_bridge_refinement.py
python experiments\odd_unit_lock_bridge_refinement.py --classifier experiments\results\odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json --output experiments\results\odd_unit_lock_bridge_refinement_d13_R16_to_R20_R24_N250000_20260705.json
python experiments\odd_unit_lock_bridge_classifier.py --input experiments\results\odd_unit_lock_transition_microscope_d13_R17_N1000000_20260705.json --output experiments\results\odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json --quiet
python experiments\odd_unit_lock_bridge_refinement.py --classifier experiments\results\odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json --output experiments\results\odd_unit_lock_bridge_refinement_d13_R17_to_R20_R24_N1000000_20260705.json --quiet
python experiments\odd_unit_lock_bridge_classifier.py --input experiments\results\odd_unit_lock_transition_microscope_d13_R18_N1000000_20260705.json --output experiments\results\odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json --quiet
python experiments\odd_unit_lock_bridge_refinement.py --classifier experiments\results\odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json --output experiments\results\odd_unit_lock_bridge_refinement_d13_R18_to_R20_R24_N1000000_20260705.json --quiet
python experiments\odd_unit_lock_bridge_state_lift.py --classifier experiments\results\odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json --high-bits 18,19,20,24 --output experiments\results\odd_unit_lock_bridge_state_lift_d13_R17_to_R18_R19_R20_R24_N1000000_20260705.json
python experiments\odd_unit_lock_bridge_state_lift.py --classifier experiments\results\odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json --high-bits 19,20,24 --output experiments\results\odd_unit_lock_bridge_state_lift_d13_R18_to_R19_R20_R24_N1000000_20260705.json
python experiments\odd_unit_lock_bridge_classifier.py --input experiments\results\odd_unit_lock_transition_microscope_d14_R17_N250000_20260705.json --output experiments\results\odd_unit_lock_bridge_classifier_d14_R17_N250000_20260705.json --quiet
python experiments\odd_unit_lock_bridge_refinement.py --max-depth 14 --classifier experiments\results\odd_unit_lock_bridge_classifier_d14_R17_N250000_20260705.json --output experiments\results\odd_unit_lock_bridge_refinement_d14_R17_to_R20_R24_N250000_20260705.json --quiet
```
