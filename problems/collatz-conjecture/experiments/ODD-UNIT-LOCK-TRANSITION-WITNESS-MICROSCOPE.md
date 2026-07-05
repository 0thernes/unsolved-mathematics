# Odd-Unit Lock Transition Witness Microscope

**Date:** 2026-07-05
**Instrument:** [`odd_unit_lock_transition_witness_microscope.py`](odd_unit_lock_transition_witness_microscope.py)
and stress helper [`odd_unit_lock_transition_microscope.py`](odd_unit_lock_transition_microscope.py)
**Primary results:**
[`results/odd_unit_lock_transition_witness_microscope_R16_N50000_20260705.json`](results/odd_unit_lock_transition_witness_microscope_R16_N50000_20260705.json),
[`results/odd_unit_lock_transition_witness_microscope_R20_N50000_20260705.json`](results/odd_unit_lock_transition_witness_microscope_R20_N50000_20260705.json),
[`results/odd_unit_lock_transition_witness_microscope_R24_N50000_20260705.json`](results/odd_unit_lock_transition_witness_microscope_R24_N50000_20260705.json),
[`results/odd_unit_lock_transition_microscope_d13_R16_N250000_20260705.json`](results/odd_unit_lock_transition_microscope_d13_R16_N250000_20260705.json),
[`results/odd_unit_lock_transition_microscope_d13_R20_N250000_20260705.json`](results/odd_unit_lock_transition_microscope_d13_R20_N250000_20260705.json)

Follow-up classifier:
[`ODD-UNIT-LOCK-BRIDGE-CLASSIFIER.md`](ODD-UNIT-LOCK-BRIDGE-CLASSIFIER.md)

Status: finite theorem-discovery data. This proves no part of the Collatz
conjecture.

## Purpose

The transition lab found `12` raw `R = 16` hit-after-hit events among positive
orbits up to `50,000`. This microscope asks whether those are genuinely twelve
mechanisms or just merged starts passing through one shared state-level bridge.

For every chained lock hit it records:

- the previous and next source cylinders;
- alignment class and odd-unit residue at each visit;
- exact target-lock witnesses for each residue;
- the shortcut bridge between visits;
- raw starts versus unique transition edges.

## Main Result

| R | Lock-hit visits | Previous-hit transitions | Raw hit-after-hit transitions | Unique state-level edges |
|---:|---:|---:|---:|---:|
| 16 | 1,258 | 1,258 | 12 | 1 |
| 20 | 568 | 568 | 0 | 0 |
| 24 | 430 | 430 | 0 | 0 |

Interpretation: the finite `R = 16` chained-hit anomaly collapses to one shared
orbit bridge and does not survive at `R = 20` or `R = 24` in the same scan.

## The Unique `R = 16` Bridge

All twelve raw starts pass through the same transition:

```text
18542 -> 9271 -> 13907 -> 20861 -> 31292
shortcut parity word: EOOO
source pair: 0111 -> 001111
```

Starts:

```text
10987, 12361, 14649, 16481, 21975, 26043,
29299, 32963, 39065, 43949, 46299, 49445
```

Previous visit:

| Field | Value |
|---|---:|
| `n` | 18,542 |
| Source | `0111` |
| Source depth | 4 |
| Alignment `m` | 5 |
| Alignment class | 1 |
| Unit residue mod `2^16` | 18,453 |
| Local union size | 390 |
| Local coverage | 0.011901855469 |
| Witness count for this residue | 1 |
| Witness target | `0011111101011` |
| Witness source phase `t` | 1 |
| Witness valuation `e` | 0 |

Next visit:

| Field | Value |
|---|---:|
| `n` | 31,292 |
| Source | `001111` |
| Source depth | 6 |
| Alignment `m` | 8 |
| Alignment class | 2 |
| Unit residue mod `2^16` | 46,383 |
| Local union size | 419 |
| Local coverage | 0.012786865234 |
| Witness count for this residue | 1 |
| Witness target | `0001111111111` |
| Witness source phase `t` | 0 |
| Witness valuation `e` | 2 |

The two lock witnesses have no shared target in the sampled witness lists.

## Wider Stress Result

The `50,000`-start bridge collapse is real but too small to support a
same-source impossibility claim. A wider odd-start scan through `250,000`
finds three `R = 16` transition signatures, including one same-source family.

| Start limit | R | Canonical source visits | Lock-hit visits | Previous-hit transitions | Raw hit-after-hit transitions | Transition signatures | Hit-after-hit / local expectation |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 50,000 | 16 | 274,989 | 1,258 | 1,258 | 12 | 1 | 0.923779542358 |
| 250,000 | 16 | 1,629,627 | 8,554 | 8,549 | 73 | 3 | 0.828363917682 |
| 250,000 | 20 | 1,629,627 | 2,889 | 2,889 | 0 | 0 | 0.000000000000 |

The `R = 16`, `N = 250,000` transition split is:

| Source pair | Count | Gap | Shortcut parity word | Representative state bridge |
|---|---:|---:|---|---|
| `0111 -> 001111` | 62 | 4 | `0111` | `18542 -> 31292` |
| `011 -> 011` | 8 | 3 | `011` | `4893686 -> 5505398` |
| `0011101111 -> 011101111` | 3 | 1 | `0` | `2181532 -> 1090766` |

All `73` widened-window `R = 16` repeat-hit records have `0` shared witness
targets between the previous and next hit. At `R = 20`, the same window still
has `2,889` individual lock-hit visits but `0` hit-after-hit transitions.

## Why This Matters

The useful crack in the wall is not "there are no repeated locks." That is
false at `R = 16`. The sharper finite statement is:

```text
In the depth-13 source/target library and odd-start scan up to 50,000,
the entire R=16 repeated-lock anomaly is one merged EOOO bridge, and
that bridge does not persist as an R=20 or R=24 repeated lock.
```

The wider statement is better and more honest:

```text
In the depth-13 source/target library and odd-start scan up to 250,000,
R=16 repeat locks split into three small transition families, but all vanish
as repeated locks at R=20 while individual R=20 lock hits still occur.
```

That is not a proof, but it is much better than a random-model guess. It gives
a concrete theorem target: prove that finite-depth repeated odd-unit locks
either collapse under refinement or enter a classified bridge family whose
refined lock depth is bounded.

The bridge classifier sharpens this target: the dominant `0111 -> 001111`
repeat family costs `7` fresh quotient bits after the first lock, while the
remaining measured repeats are alignment-drop bridges that collapse to merged
state edges in this finite window.

## Non-Claims

- This is not a proof of Collatz.
- It uses the finite depth-13 supercritical source/target library.
- It scans odd positive starts up to `50,000`.
- The extended stress scan reaches odd positive starts up to `250,000`, still
  finite.
- It uses canonical source-cylinder visits, not every rotated phase cylinder.
- Absence at `R = 20` and `R = 24` is finite evidence, not an infinite theorem.

## Reproduce

```powershell
python -m py_compile experiments\odd_unit_lock_transition_witness_microscope.py
python experiments\odd_unit_lock_transition_witness_microscope.py --bits 16 --quiet --output experiments\results\odd_unit_lock_transition_witness_microscope_R16_N50000_20260705.json
python experiments\odd_unit_lock_transition_witness_microscope.py --bits 20 --quiet --output experiments\results\odd_unit_lock_transition_witness_microscope_R20_N50000_20260705.json
python experiments\odd_unit_lock_transition_witness_microscope.py --bits 24 --quiet --output experiments\results\odd_unit_lock_transition_witness_microscope_R24_N50000_20260705.json
python -m py_compile experiments\odd_unit_lock_transition_microscope.py
python experiments\odd_unit_lock_transition_microscope.py --start-limit 250000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d13_R16_N250000_20260705.json
python experiments\odd_unit_lock_transition_microscope.py --excess-bits 20 --start-limit 250000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d13_R20_N250000_20260705.json
```
