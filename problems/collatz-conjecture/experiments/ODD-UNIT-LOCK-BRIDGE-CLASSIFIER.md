# Odd-Unit Lock Bridge Classifier

**Date:** 2026-07-05
**Instrument:** [`odd_unit_lock_bridge_classifier.py`](odd_unit_lock_bridge_classifier.py)
**Input:** [`results/odd_unit_lock_transition_microscope_d13_R16_N250000_20260705.json`](results/odd_unit_lock_transition_microscope_d13_R16_N250000_20260705.json)
**Result:** [`results/odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json)

Status: finite symbolic classification of measured bridges. This proves no
part of the Collatz conjecture.

## Purpose

The transition witness microscope found `73` repeated `R = 16` odd-unit lock
hits in the odd-start scan through `250,000`. Those repeats split into three
coarse source-pair families. This classifier asks a sharper symbolic question:

```text
Once the previous R-bit unit lock is known, does the next R-bit lock come for
free, or does it impose fresh quotient bits?
```

For a bridge gap of length `g`, previous alignment `m0`, and next alignment
`m1`, the state-coordinate lift cost observed by the classifier is:

```text
fresh bits = max(0, g + m1 - m0)
```

The script does not assume the formula blindly. It solves the exact linear
congruence modulo `2^R` and checks every observed previous and current state
against the derived residue class.

## Main Result

The `73` repeat records become `4` absolute bridge geometries:

| Source pair | Count | Gap word | Previous `m` | Next `m` | Fresh quotient bits | Previous state class |
|---|---:|---|---:|---:|---:|---|
| `0111 -> 001111` | 62 | `0111` | 5 | 8 | 7 | `18542 mod 2^28` |
| `011 -> 011` | 7 | `011` | 10 | 7 | 0 | `4893686 mod 2^26` |
| `0011101111 -> 011101111` | 3 | `0` | 12 | 10 | 0 | `2181532 mod 2^28` |
| `011 -> 011` | 1 | `011` | 7 | 4 | 0 | `611702 mod 2^23` |

All classifier checks pass:

- the formula matches the solved congruence for every geometry;
- observed previous states match the derived base or lifted residue class;
- observed current states match the derived current lock residue class;
- the bridge affine map reaches the claimed next alignment.

## Interpretation

The repeat-lock phenomenon is not one thing.

The dominant bridge,

```text
0111|m5|u18453 -> 001111|m8|u46383 through gap 0111
```

is fragile: after the previous `R = 16` lock, the next lock still costs `7`
fresh quotient bits. That makes it compatible with the codimension story.

The other measured bridges are different. Their next alignment drops far enough
that the previous lock already determines the next unit residue modulo `2^16`.
Those are the dangerous-looking cases for a proof strategy, but in this finite
window they collapse to one or two merged state edges rather than an expanding
repeat-lock mechanism.

## Theorem Target

A plausible next lemma is:

```text
For a measured repeated-lock bridge with gap g and alignments m0 -> m1,
the second lock imposes max(0, g + m1 - m0) fresh quotient bits unless the
bridge is in the alignment-drop class. Alignment-drop bridges must be classified
as finite merged-state families or shown to lose refined lock depth.
```

That would not prove Collatz by itself. It would, however, replace a vague
"independence" hope with an exact bridge-accounting rule.

## Non-Claims

- This is not a proof of Collatz.
- It classifies only the repeated `R = 16` bridges found by the finite
  depth-13, odd-start scan through `250,000`.
- It does not rule out new bridge geometries at larger depth, larger starts, or
  higher precision.
- It does not prove that all alignment-drop bridges are harmless.

## Reproduce

```powershell
python -m py_compile experiments\odd_unit_lock_bridge_classifier.py
python experiments\odd_unit_lock_bridge_classifier.py --input experiments\results\odd_unit_lock_transition_microscope_d13_R16_N250000_20260705.json --output experiments\results\odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json
```
