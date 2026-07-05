# Odd-Unit Lock Persistence Ladder

**Date:** 2026-07-05
**Inputs:**
[`results/odd_unit_lock_transition_microscope_d13_R16_N250000_20260705.json`](results/odd_unit_lock_transition_microscope_d13_R16_N250000_20260705.json),
[`results/odd_unit_lock_transition_microscope_d13_R17_N250000_20260705.json`](results/odd_unit_lock_transition_microscope_d13_R17_N250000_20260705.json),
[`results/odd_unit_lock_transition_microscope_d13_R18_N250000_20260705.json`](results/odd_unit_lock_transition_microscope_d13_R18_N250000_20260705.json),
[`results/odd_unit_lock_transition_microscope_d13_R19_N250000_20260705.json`](results/odd_unit_lock_transition_microscope_d13_R19_N250000_20260705.json),
[`results/odd_unit_lock_transition_microscope_d13_R20_N250000_20260705.json`](results/odd_unit_lock_transition_microscope_d13_R20_N250000_20260705.json),
[`results/odd_unit_lock_transition_microscope_d13_R24_N250000_20260705.json`](results/odd_unit_lock_transition_microscope_d13_R24_N250000_20260705.json),
[`results/odd_unit_lock_transition_microscope_d13_R17_N1000000_20260705.json`](results/odd_unit_lock_transition_microscope_d13_R17_N1000000_20260705.json),
[`results/odd_unit_lock_transition_microscope_d13_R18_N1000000_20260705.json`](results/odd_unit_lock_transition_microscope_d13_R18_N1000000_20260705.json),
[`results/odd_unit_lock_transition_microscope_d13_R19_N1000000_20260705.json`](results/odd_unit_lock_transition_microscope_d13_R19_N1000000_20260705.json)

**Bridge classifiers:**
[`results/odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json),
[`results/odd_unit_lock_bridge_classifier_d13_R20_N250000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R20_N250000_20260705.json),
[`results/odd_unit_lock_bridge_classifier_d13_R24_N250000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R24_N250000_20260705.json),
[`results/odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json),
[`results/odd_unit_lock_bridge_refinement_d13_R17_to_R20_R24_N1000000_20260705.json`](results/odd_unit_lock_bridge_refinement_d13_R17_to_R20_R24_N1000000_20260705.json),
[`results/odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json),
[`results/odd_unit_lock_bridge_refinement_d13_R18_to_R20_R24_N1000000_20260705.json`](results/odd_unit_lock_bridge_refinement_d13_R18_to_R20_R24_N1000000_20260705.json),
[`results/odd_unit_lock_bridge_state_lift_d13_R17_to_R18_R19_R20_R24_N1000000_20260705.json`](results/odd_unit_lock_bridge_state_lift_d13_R17_to_R18_R19_R20_R24_N1000000_20260705.json),
[`results/odd_unit_lock_bridge_state_lift_d13_R18_to_R19_R20_R24_N1000000_20260705.json`](results/odd_unit_lock_bridge_state_lift_d13_R18_to_R19_R20_R24_N1000000_20260705.json)

**Depth-14 stress:**
[`results/odd_unit_lock_transition_microscope_d14_R16_N250000_20260705.json`](results/odd_unit_lock_transition_microscope_d14_R16_N250000_20260705.json),
[`results/odd_unit_lock_transition_microscope_d14_R17_N250000_20260705.json`](results/odd_unit_lock_transition_microscope_d14_R17_N250000_20260705.json),
[`results/odd_unit_lock_transition_microscope_d14_R18_N250000_20260705.json`](results/odd_unit_lock_transition_microscope_d14_R18_N250000_20260705.json),
[`results/odd_unit_lock_transition_microscope_d14_R19_N250000_20260705.json`](results/odd_unit_lock_transition_microscope_d14_R19_N250000_20260705.json),
[`results/odd_unit_lock_bridge_classifier_d14_R17_N250000_20260705.json`](results/odd_unit_lock_bridge_classifier_d14_R17_N250000_20260705.json),
[`results/odd_unit_lock_bridge_refinement_d14_R17_to_R20_R24_N250000_20260705.json`](results/odd_unit_lock_bridge_refinement_d14_R17_to_R20_R24_N250000_20260705.json)

Status: finite theorem-discovery data. This proves no part of the Collatz
conjecture.

## Question

The static refinement lab showed that high-precision odd-unit locks do not
refill: once target-lock collisions separate, additional precision keeps adding
fresh codimension.

The transition labs ask the dynamic version:

```text
Along actual positive orbits, do lock hits keep chaining as R grows?
```

This note records the current largest same-configuration scan:

```text
source/target depth <= 13
source depth >= 3
odd starts <= 250000
max shortcut steps = 512
```

It also records targeted `R = 17`, `R = 18`, and `R = 19` stress extensions
through odd starts `<= 1,000,000`.

## Persistence Ladder

| Extra bits R | Odd starts | Source visits | Lock hits | Previous-hit transitions | Hit-after-hit transitions | Local expectation | Observed / expected |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 16 | 124,999 | 1,629,627 | 8,554 | 8,549 | 73 | 88.125518798828 | 0.828363917682 |
| 17 | 124,999 | 1,629,627 | 5,545 | 5,540 | 0 | 28.565139770508 | 0.000000000000 |
| 18 | 124,999 | 1,629,627 | 4,096 | 4,096 | 0 | 10.353897094727 | 0.000000000000 |
| 19 | 124,999 | 1,629,627 | 3,083 | 3,083 | 0 | 3.892978668213 | 0.000000000000 |
| 20 | 124,999 | 1,629,627 | 2,889 | 2,889 | 0 | 1.829259872437 | 0.000000000000 |
| 24 | 124,999 | 1,629,627 | 2,094 | 2,094 | 0 | 0.097301363945 | 0.000000000000 |

At `R = 16`, repeated lock hits exist. At `R = 17` through `R = 24`, the same
`250,000` scan still has thousands of lock hits, but none chain to another
lock hit at the next canonical source-cylinder visit.

The `1,000,000` stress extension finds repeats again at `R = 17` and `R = 18`,
but only as rare compressed bridges; by `R = 19`, repeats disappear again:

| Extra bits R | Odd starts | Source visits | Lock hits | Previous-hit transitions | Hit-after-hit transitions | Local expectation | Observed / expected |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 499,999 | 7,374,595 | 26,664 | 26,641 | 4 | 136.842514038086 | 0.029230681913 |
| 18 | 499,999 | 7,374,595 | 18,816 | 18,811 | 3 | 47.528289794922 | 0.063120301886 |
| 19 | 499,999 | 7,374,595 | 13,586 | 13,581 | 0 | 17.202903747559 | 0.000000000000 |

Three of the four `R = 17` repeat starts pass through the identical state bridge
`400252 -> 200126`. The `R = 18` repeats are exactly those same three starts
and the same state bridge, with the previous unit refined from `65357 mod
2^17` to `196429 mod 2^18`. No `R = 19` repeated lock appears in this
one-million window.

## R = 16 Bridge Families

The `R = 16` repeated hits are not all the same phenomenon. The bridge
classifier finds four bridge geometries:

| Source pair | Count | Gap word | Fresh quotient bits |
|---|---:|---|---:|
| `0111 -> 001111` | 62 | `0111` | 7 |
| `011 -> 011` | 7 | `011` | 0 |
| `0011101111 -> 011101111` | 3 | `0` | 0 |
| `011 -> 011` | 1 | `011` | 0 |

The dominant bridge is not free: once the previous `R = 16` lock is fixed, the
next lock still imposes `7` fresh quotient bits. The remaining three geometries
are free at `R = 16`, but they disappear from the repeated-hit scan at `R = 20`.

## R = 17 Stress Bridge Families

At `R = 17` and odd starts through `1,000,000`, the four repeat hits collapse to
two zero-fresh bridge geometries:

| Source pair | Count | Gap word | Fresh quotient bits | State bridge |
|---|---:|---|---:|---|
| `0011111 -> 011111` | 3 | `0` | 0 | `400252 -> 200126` |
| `0110111111 -> 0111111` | 1 | `011` | 0 | `733750 -> 825470` |

Both measured `R = 17` bridge geometries have one previous-lock lift at
`R = 20` and at `R = 24`; all four higher-precision lift checks fail to be
repeated next-lock hits.

At `R = 18`, the only measured bridge geometry is the surviving
`0011111 -> 011111` state bridge:

| Source pair | Count | Gap word | Fresh quotient bits | State bridge |
|---|---:|---|---:|---|
| `0011111 -> 011111` | 3 | `0` | 0 | `400252 -> 200126` |

Its `R = 20` and `R = 24` previous-lock lifts also fail to be repeated next-lock
hits. Thus the current one-million stress picture is bounded refinement death:
`R = 17` has two tiny bridge families, `R = 18` has one, and `R = 19` has none.

The state-lift microscope corrects the `R = 19` interpretation. The surviving
`400252 -> 200126` bridge still exists algebraically at `R = 19`, but the
required previous state class lifts from `400252` to:

```text
400252 + 2^28 = 268835708  (mod 2^29)
```

So the one-million scan sees no observed `R = 19` repeated lock because the
positive orbits merge into the low representative `400252`, not the lifted
residue class. In this tested target library, the bridge then stops being a
next-lock hit by `R = 20`.

## Depth-14 Stress

Increasing the source/target library from depth `13` to depth `14` is the first
real robustness test. It nearly doubles the primitive source count (`244` to
`490`) and does create new repeated-lock bridge families, but the same
precision-death pattern remains in the `250,000` odd-start window.

| Max depth | Extra bits R | Odd starts | Source visits | Lock hits | Previous-hit transitions | Hit-after-hit transitions | Local expectation | Observed / expected |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 14 | 16 | 124,999 | 1,660,608 | 14,384 | 14,379 | 255 | 287.260803222656 | 0.887695074090 |
| 14 | 17 | 124,999 | 1,660,608 | 8,006 | 8,001 | 15 | 78.147247314453 | 0.191945340565 |
| 14 | 18 | 124,999 | 1,660,608 | 4,207 | 4,207 | 0 | 20.665351867676 | 0.000000000000 |
| 14 | 19 | 124,999 | 1,660,608 | 2,286 | 2,286 | 0 | 5.125400543213 | 0.000000000000 |

The depth-14 `R = 17` survivors classify into three bridge geometries:

| Source pair | Count | Fresh quotient bits | Refinement result |
|---|---:|---:|---|
| `00110111011101 -> 01101110111` | 12 | 0 | dies at `R = 20` and `R = 24` |
| `001111101 -> 011111` | 2 | 0 | dies at `R = 20` and `R = 24` |
| `011 -> 0111` | 1 | 6 | dies at `R = 20` and `R = 24` |

Interpretation: depth growth does create new coarse bridge families, including
zero-fresh alignment-drop bridges. The current finite evidence says those
families still lose repeated-lock status under refinement. A proof attempt now
has to control a moving bridge catalogue, not just one fixed list.

## Current Theorem Target

The refined proof target is no longer "lock hits are independent." They are not
at coarse precision. The target is sharper:

```text
For positive orbits, repeated odd-unit locks form finitely many bridge
geometries at coarse precision. Under precision refinement, every bridge either
requires fresh quotient bits or vanishes from the repeated-hit set.
```

This is the codimension route in a theorem-shaped form. A proof would need to
replace the finite `depth <= 13`, `starts <= 250000` scan with a symbolic bridge
classification and a uniform refinement bound. The `R = 17` million-start
stress results sharpen the scary subcase: alignment-drop bridges can reappear
at larger start windows and larger source libraries, can persist algebraically
for one more precision while escaping the observed low state, and then lose
refined next-lock status quickly in these configurations.

The companion [`ODD-UNIT-LOCK-ALIGNMENT-DROP.md`](ODD-UNIT-LOCK-ALIGNMENT-DROP.md)
turns that scary subcase into a finite ledger: every measured zero-fresh bridge
is alignment-descending, with drop `2` or `3`, and every checked zero-fresh
family dies under the available `R = 20` / `R = 24` refinements.

## Non-Claims

- This is not a proof of Collatz.
- This does not rule out repeated locks beyond the finite scan.
- This does not prove that depth-13 target spines capture all future
  regeneration events.
- This does not prove a uniform bridge classification.
- It does identify the exact finite mechanism that a uniform theorem would
  have to generalize.

## Reproduce

```powershell
python experiments\odd_unit_lock_transition_microscope.py --excess-bits 16 --start-limit 250000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d13_R16_N250000_20260705.json
python experiments\odd_unit_lock_transition_microscope.py --excess-bits 17 --start-limit 250000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d13_R17_N250000_20260705.json
python experiments\odd_unit_lock_transition_microscope.py --excess-bits 18 --start-limit 250000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d13_R18_N250000_20260705.json
python experiments\odd_unit_lock_transition_microscope.py --excess-bits 19 --start-limit 250000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d13_R19_N250000_20260705.json
python experiments\odd_unit_lock_transition_microscope.py --excess-bits 20 --start-limit 250000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d13_R20_N250000_20260705.json
python experiments\odd_unit_lock_transition_microscope.py --excess-bits 24 --start-limit 250000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d13_R24_N250000_20260705.json
python experiments\odd_unit_lock_transition_microscope.py --excess-bits 17 --start-limit 1000000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d13_R17_N1000000_20260705.json
python experiments\odd_unit_lock_transition_microscope.py --excess-bits 18 --start-limit 1000000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d13_R18_N1000000_20260705.json
python experiments\odd_unit_lock_transition_microscope.py --excess-bits 19 --start-limit 1000000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d13_R19_N1000000_20260705.json
python experiments\odd_unit_lock_bridge_classifier.py --input experiments\results\odd_unit_lock_transition_microscope_d13_R16_N250000_20260705.json --output experiments\results\odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json --quiet
python experiments\odd_unit_lock_bridge_classifier.py --input experiments\results\odd_unit_lock_transition_microscope_d13_R20_N250000_20260705.json --output experiments\results\odd_unit_lock_bridge_classifier_d13_R20_N250000_20260705.json --quiet
python experiments\odd_unit_lock_bridge_classifier.py --input experiments\results\odd_unit_lock_transition_microscope_d13_R24_N250000_20260705.json --output experiments\results\odd_unit_lock_bridge_classifier_d13_R24_N250000_20260705.json --quiet
python experiments\odd_unit_lock_bridge_classifier.py --input experiments\results\odd_unit_lock_transition_microscope_d13_R17_N1000000_20260705.json --output experiments\results\odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json --quiet
python experiments\odd_unit_lock_bridge_refinement.py --classifier experiments\results\odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json --output experiments\results\odd_unit_lock_bridge_refinement_d13_R17_to_R20_R24_N1000000_20260705.json --quiet
python experiments\odd_unit_lock_bridge_classifier.py --input experiments\results\odd_unit_lock_transition_microscope_d13_R18_N1000000_20260705.json --output experiments\results\odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json --quiet
python experiments\odd_unit_lock_bridge_refinement.py --classifier experiments\results\odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json --output experiments\results\odd_unit_lock_bridge_refinement_d13_R18_to_R20_R24_N1000000_20260705.json --quiet
python experiments\odd_unit_lock_bridge_state_lift.py --classifier experiments\results\odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json --high-bits 18,19,20,24 --output experiments\results\odd_unit_lock_bridge_state_lift_d13_R17_to_R18_R19_R20_R24_N1000000_20260705.json
python experiments\odd_unit_lock_bridge_state_lift.py --classifier experiments\results\odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json --high-bits 19,20,24 --output experiments\results\odd_unit_lock_bridge_state_lift_d13_R18_to_R19_R20_R24_N1000000_20260705.json
python experiments\odd_unit_lock_transition_microscope.py --max-depth 14 --min-source-depth 3 --excess-bits 16 --start-limit 250000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d14_R16_N250000_20260705.json
python experiments\odd_unit_lock_transition_microscope.py --max-depth 14 --min-source-depth 3 --excess-bits 17 --start-limit 250000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d14_R17_N250000_20260705.json
python experiments\odd_unit_lock_transition_microscope.py --max-depth 14 --min-source-depth 3 --excess-bits 18 --start-limit 250000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d14_R18_N250000_20260705.json
python experiments\odd_unit_lock_transition_microscope.py --max-depth 14 --min-source-depth 3 --excess-bits 19 --start-limit 250000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d14_R19_N250000_20260705.json
python experiments\odd_unit_lock_bridge_classifier.py --input experiments\results\odd_unit_lock_transition_microscope_d14_R17_N250000_20260705.json --output experiments\results\odd_unit_lock_bridge_classifier_d14_R17_N250000_20260705.json --quiet
python experiments\odd_unit_lock_bridge_refinement.py --max-depth 14 --classifier experiments\results\odd_unit_lock_bridge_classifier_d14_R17_N250000_20260705.json --output experiments\results\odd_unit_lock_bridge_refinement_d14_R17_to_R20_R24_N250000_20260705.json --quiet
```
