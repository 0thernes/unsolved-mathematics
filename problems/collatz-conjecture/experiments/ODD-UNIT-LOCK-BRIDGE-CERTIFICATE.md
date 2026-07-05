# Odd-Unit Lock Bridge Collapse Certificate

**Date:** 2026-07-05
**Instrument:** [`odd_unit_lock_bridge_certificate.py`](odd_unit_lock_bridge_certificate.py)
**Result:** [`results/odd_unit_lock_bridge_collapse_certificate_20260705.json`](results/odd_unit_lock_bridge_collapse_certificate_20260705.json)
**Related:**
[`ODD-UNIT-LOCK-PERSISTENCE-LADDER.md`](ODD-UNIT-LOCK-PERSISTENCE-LADDER.md),
[`ODD-UNIT-LOCK-BRIDGE-CLASSIFIER.md`](ODD-UNIT-LOCK-BRIDGE-CLASSIFIER.md),
[`ODD-UNIT-LOCK-BRIDGE-REFINEMENT.md`](ODD-UNIT-LOCK-BRIDGE-REFINEMENT.md)

Status: finite machine-checkable certificate. This proves no part of the
Collatz conjecture.

## Purpose

The transition and bridge labs now have enough moving pieces that a prose-only
summary is too fragile. This certificate ties together the transition
microscope, bridge classifier, and bridge refinement receipts, then fails if
the current collapse story stops being true.

The exact finite story being checked is:

```text
coarse repeated locks exist at R=16;
the 250k scan has no repeats at R=17,18,19,20,24;
the million-start stress scan has tiny R=17/R=18 repeats;
those stress repeats disappear at R=19;
all measured R=16/R=17/R=18 bridge families die under R=20/R=24 refinement.
```

## Certificate Summary

All checks passed.

| Check | Result |
|---|---:|
| `250k` window R16 repeat transitions | `73` |
| `250k` window R17 repeat transitions | `0` |
| `250k` window R18 repeat transitions | `0` |
| `250k` window R19 repeat transitions | `0` |
| `250k` window R20 repeat transitions | `0` |
| `250k` window R24 repeat transitions | `0` |
| `1,000,000` stress R17 repeat transitions | `4` |
| `1,000,000` stress R18 repeat transitions | `3` |
| `1,000,000` stress R19 repeat transitions | `0` |
| R18 stress state bridge | `400252 -> 200126` |
| Refinement base precisions checked | `16, 17, 18` |
| Total refined repeat lifts at R20/R24 | `0` |

## Passing Gates

The certificate currently checks:

| Gate | Meaning |
|---|---|
| `fixed_250k_window_has_only_R16_repeat_bridges` | The fixed depth-13, 250k odd-start window has repeated locks only at R16. |
| `million_stress_repeats_die_by_R19` | The million-start R17/R18 stress repeats disappear at R19. |
| `million_stress_R18_state_bridges_are_subset_of_R17` | The R18 stress bridge is not a new expanding family; it is contained in the R17 state bridges. |
| `all_bridge_classifier_checks_pass` | Every measured classifier family satisfies its exact affine/residue checks. |
| `all_refined_bridge_families_die` | Every measured bridge family fails to remain a repeated next-lock hit at R20/R24. |
| `repeat_counts_stay_below_local_coverage_expectation` | Observed repeat counts stay at or below the local sparse-coverage baseline in every checked transition artifact. |

## Interpretation

This is a useful hardening step for the current proof search. It turns the
strongest finite signal into a regression gate:

```text
repeated odd-unit locks look like a coarse-precision bridge phenomenon,
not a persistent high-precision chaining mechanism, in the checked windows.
```

That does not close the Collatz problem. It does sharpen the next theorem
target. A proof path would need to replace the finite certificate with a
symbolic bridge theorem:

```text
Every dynamically possible repeated odd-unit lock bridge either pays fresh
quotient-bit cost, or belongs to an alignment-drop family whose refined
repeat-lock depth is uniformly bounded.
```

The certificate is valuable because it names exactly what would falsify this
path: a bridge family that passes classifier checks and survives refinement as
a repeated next-lock hit.

## Non-Claims

- This is not a proof of Collatz.
- It only checks the finite receipt set named by the script.
- It does not rule out new bridge geometries at larger depth or larger start
  windows.
- It does not prove that every alignment-drop bridge is harmless.
- It does not prove a global entropy comparison.
- It does not prove that the depth-13 source/target library is complete.

## Reproduce

```powershell
python -m py_compile experiments\odd_unit_lock_bridge_certificate.py
python experiments\odd_unit_lock_bridge_certificate.py --output experiments\results\odd_unit_lock_bridge_collapse_certificate_20260705.json
```
