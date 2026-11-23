# Odd-Unit Lock R12 Coarse Memory

**Date:** 2026-07-05
**Microscope:** [`odd_unit_lock_transition_microscope.py`](odd_unit_lock_transition_microscope.py)
**Classifier:** [`odd_unit_lock_bridge_classifier.py`](odd_unit_lock_bridge_classifier.py)
**Inputs:**
[`results/odd_unit_lock_transition_microscope_d13_R12_N50000_20260705.json.gz`](results/odd_unit_lock_transition_microscope_d13_R12_N50000_20260705.json.gz) (losslessly gzip-compressed from 38.6 MB to 0.64 MB),
[`results/odd_unit_lock_bridge_classifier_d13_R12_N50000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R12_N50000_20260705.json)

Status: finite theorem-discovery data. This proves no part of the Collatz
conjecture.

## Purpose

The persistence ladder showed that repeated odd-unit locks almost disappear as
precision rises:

| R | Odd starts | Lock hits | Hit-after-hit repeats |
|---:|---:|---:|---:|
| 16 | 124,999 | 8,554 | 73 |
| 17 | 124,999 | 5,545 | 0 |
| 18 | 124,999 | 4,096 | 0 |
| 19 | 124,999 | 3,083 | 0 |
| 20 | 124,999 | 2,889 | 0 |
| 24 | 124,999 | 2,094 | 0 |

This note probes the opposite edge: a coarse `R = 12` scan where repeated lock
memory is deliberately loud. The question is whether the loud behavior is
unstructured, or whether it still compresses into exact bridge geometries.

## R12 Scan

Configuration:

```text
source/target depth <= 13
source depth >= 3
odd starts <= 50000
max shortcut steps = 512
extra unit bits R = 12
```

Measured scan:

| Quantity | Value |
|---|---:|
| Odd starts scanned | 24,999 |
| Canonical source visits | 274,989 |
| Lock hits | 46,294 |
| Previous-hit transitions | 39,866 |
| Hit-after-hit transitions | 15,629 |
| Starts with at least one repeat | 13,505 |
| Same-source repeats | 4,548 |
| Different-source repeats | 11,081 |
| Expected repeats from local coverage | 4,235.00 |
| Observed / expected repeats | 3.690432580947 |

The microscope intentionally fails its harmless-randomness check here:
hit-after-hit repeats are far above twice the local coverage baseline. That is
the point of this run. `R = 12` is the coarse sticky regime.

## Classifier Extension

The original bridge classifier was built around `R = 16`, where the previous
lock supplied enough state bits for the next current-unit equation. At `R = 12`
that assumption fails for some bridges. Instead of rejecting those cases, the
classifier now normalizes the exact quotient equation.

Let

```text
E = previous_m + R - gap_steps - current_m
base = (F_gap(previous_residue) - rho_1) / 2^current_m
s = max(0, -E, -v2(base))
```

Then it solves the integer congruence

```text
2^s * (current_unit - base) =
    3^odd_gap * 2^(E+s) * k          (mod 2^(R+s)).
```

This keeps the state-coordinate bridge exact even when the previous lock
undersupplies the next alignment. The solved fresh quotient cost still matches

```text
fresh bits = max(0, gap_steps + current_m - previous_m).
```

## R12 Bridge Compression

The `15,629` repeat records compress to `130` exact bridge geometries. All
classifier checks pass.

| Quantity | Value |
|---|---:|
| Transition records | 15,629 |
| Bridge geometries | 130 |
| Coarse lock signatures | 130 |
| Zero-fresh geometries | 49 |
| Positive-fresh geometries | 81 |
| Geometries needing normalization | 26 |
| Zero-fresh transitions | 9,906 |
| Positive-fresh transitions | 5,723 |
| Normalized transitions | 332 |
| Maximum fresh quotient bits | 24 |

Fresh-bit distribution by bridge geometry and transition mass:

| Fresh bits | Geometries | Transitions |
|---:|---:|---:|
| 0 | 49 | 9,906 |
| 1 | 3 | 74 |
| 2 | 5 | 57 |
| 4 | 11 | 39 |
| 5 | 7 | 4,458 |
| 6 | 1 | 1 |
| 7 | 7 | 22 |
| 8 | 4 | 27 |
| 9 | 3 | 4 |
| 10 | 1 | 12 |
| 11 | 7 | 193 |
| 12 | 6 | 504 |
| 13 | 2 | 126 |
| 14 | 3 | 11 |
| 15 | 3 | 5 |
| 16 | 4 | 90 |
| 17 | 4 | 28 |
| 18 | 4 | 31 |
| 19 | 1 | 1 |
| 21 | 2 | 25 |
| 23 | 1 | 9 |
| 24 | 2 | 6 |

Normalization-shift distribution:

| Normalization shift | Geometries | Transitions |
|---:|---:|---:|
| 0 | 104 | 15,297 |
| 1 | 2 | 126 |
| 2 | 3 | 11 |
| 3 | 3 | 5 |
| 4 | 4 | 90 |
| 5 | 4 | 28 |
| 6 | 4 | 31 |
| 7 | 1 | 1 |
| 9 | 2 | 25 |
| 11 | 1 | 9 |
| 12 | 2 | 6 |

## Largest R12 Families

| Source pair | Count | Gap word | Fresh bits | Normalization shift |
|---|---:|---|---:|---:|
| `0110111111 -> 0111111` | 8,416 | `011` | 0 | 0 |
| `011 -> 011` | 4,430 | `0110` | 5 | 0 |
| `010111 -> 0111` | 1,109 | `01` | 0 | 0 |
| `0111 -> 010111` | 382 | `0111000001` | 12 | 0 |
| `011 -> 010111` | 147 | `01100100` | 11 | 0 |
| `0111 -> 011` | 117 | `0111000100000` | 13 | 1 |
| `010110101111 -> 011` | 100 | `01` | 0 | 0 |
| `0111 -> 0010111111` | 90 | `0111` | 12 | 0 |
| `01111 -> 011` | 69 | `01111` | 1 | 0 |
| `010111 -> 0111` | 56 | `01` | 0 | 0 |
| `011111 -> 011` | 42 | `0111110100010010010` | 16 | 4 |
| `011 -> 001111111111` | 35 | `011` | 16 | 4 |

The dominant family is a single finite state bridge:

```text
0110111111 -> 0111111 through gap 011
```

It accounts for `8,416` repeats by itself and costs zero fresh quotient bits at
`R = 12`. This is the coarse dangerous-looking case. In the higher-precision
ladder, the corresponding phenomenon does not persist as an expanding repeat
mechanism; repeated hits collapse sharply by `R = 16` and vanish in the
`250,000`-start scan by `R = 17`.

## Interpretation

This is stronger than "coarse locks cluster." The R12 cluster is algebraically
structured:

1. Most repeat mass is finite bridge recycling, not free-form regeneration.
2. A large minority of bridge geometries already require fresh quotient bits.
3. The weirdest coarse failures become exact normalization debts instead of
   undefined exceptions.
4. The same proof route remains plausible but sharper: classify finite bridge
   families, then prove refinement death or fresh-bit accumulation uniformly.

The next theorem-shaped target is:

```text
For fixed bounded source depth, repeated odd-unit locks at coarse precision
compress into finitely many affine bridge geometries. Under precision
refinement, every such bridge either accumulates fresh quotient codimension or
collapses into a finite merged-state family that cannot regenerate indefinitely.
```

The finite data does not prove the uniform statement. It gives a concrete list
of algebraic enemies the uniform proof must defeat.

## Reproduce

```powershell
python -m py_compile experiments\odd_unit_lock_bridge_classifier.py
python experiments\odd_unit_lock_transition_microscope.py --excess-bits 12 --start-limit 50000 --quiet --output experiments\results\odd_unit_lock_transition_microscope_d13_R12_N50000_20260705.json
python experiments\odd_unit_lock_bridge_classifier.py --input experiments\results\odd_unit_lock_transition_microscope_d13_R12_N50000_20260705.json --output experiments\results\odd_unit_lock_bridge_classifier_d13_R12_N50000_20260705.json --quiet
```

The microscope exits nonzero for this run because its coarse-clustering check
is intentionally violated at `R = 12`. The classifier exits zero and records
the exact bridge algebra.

