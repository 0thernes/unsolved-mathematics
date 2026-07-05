# Odd-Unit Lock Bridge State-Lift Microscope

**Date:** 2026-07-05
**Instrument:** [`odd_unit_lock_bridge_state_lift.py`](odd_unit_lock_bridge_state_lift.py)
**Inputs:**
[`results/odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json),
[`results/odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json)
**Results:**
[`results/odd_unit_lock_bridge_state_lift_d13_R17_to_R18_R19_R20_R24_N1000000_20260705.json`](results/odd_unit_lock_bridge_state_lift_d13_R17_to_R18_R19_R20_R24_N1000000_20260705.json),
[`results/odd_unit_lock_bridge_state_lift_d13_R18_to_R19_R20_R24_N1000000_20260705.json`](results/odd_unit_lock_bridge_state_lift_d13_R18_to_R19_R20_R24_N1000000_20260705.json)

Status: finite bridge state-lift measurement. This proves no part of the
Collatz conjecture.

## Question

The persistence ladder found a tension:

```text
R = 18: the bridge 400252 -> 200126 appears as a repeated lock.
R = 19: the one-million positive-orbit scan reports no repeated locks.
```

The bridge-refinement algebra says the same bridge still has a repeated-lock
lift at `R = 19`. This microscope separates two questions:

1. Does a higher-precision repeated-lock bridge exist as a residue class?
2. Does the observed merged orbit state lie in that higher-precision class?

## Main Result

For the `R = 17` stress bridges:

| Precision | Algebraic refined repeat lifts | Observed-state repeat lifts | State-escape lifts |
|---:|---:|---:|---:|
| 18 | 2 | 1 | 1 |
| 19 | 2 | 0 | 2 |
| 20 | 0 | 0 | 0 |
| 24 | 0 | 0 | 0 |

For the `R = 18` surviving bridge:

| Precision | Algebraic refined repeat lifts | Observed-state repeat lifts | State-escape lifts |
|---:|---:|---:|---:|
| 19 | 1 | 0 | 1 |
| 20 | 0 | 0 | 0 |
| 24 | 0 | 0 | 0 |

So `R = 19` is not pure lock death. It is state-class escape.

## The `400252 -> 200126` Lift

The surviving stress bridge is:

```text
0011111 | m=10 -> 011111 | m=7
gap word: 0
state bridge: 400252 -> 200126
```

At `R = 18`, the observed state is exactly the required lifted residue class:

| Side | Observed state | Required state residue | Modulus |
|---|---:|---:|---:|
| previous | 400252 | 400252 | `2^28` |
| current | 200126 | 200126 | `2^25` |

At `R = 19`, the current state still matches, but the previous state does not:

| Side | Observed state | Required state residue | Lift delta | Modulus |
|---|---:|---:|---:|---:|
| previous | 400252 | 268835708 | `2^28` | `2^29` |
| current | 200126 | 200126 | 0 | `2^26` |

This explains the apparent contradiction. The repeated-lock bridge survives
algebraically at `R = 19`, but the required previous state class is:

```text
400252 + 2^28  (mod 2^29)
```

The one-million positive-start scan reaches the merged low representative
`400252`, not that lifted residue class.

## Interpretation

The local picture is now more precise:

```text
R17/R18 repeat locks are not random.
They are exact alignment-drop bridges.
At R19, the bridge can persist algebraically while escaping the observed state.
At R20 and R24, the tested bridge no longer survives as a next-lock hit.
```

This is not yet a proof route by itself. It suggests the next theorem target
must track both lock residues and positive-orbit access to lifted state classes.

## Non-Claims

- This is not a proof of Collatz.
- It only analyzes the measured `R = 17` and `R = 18` bridge families from the
  depth-13, one-million odd-start scan.
- It does not prove that the lifted `R = 19` state class is unreachable by all
  positive starts.
- It does not classify all possible future alignment-drop bridges.

## Reproduce

```powershell
python -m py_compile experiments\odd_unit_lock_bridge_state_lift.py
python experiments\odd_unit_lock_bridge_state_lift.py --classifier experiments\results\odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json --high-bits 18,19,20,24 --output experiments\results\odd_unit_lock_bridge_state_lift_d13_R17_to_R18_R19_R20_R24_N1000000_20260705.json
python experiments\odd_unit_lock_bridge_state_lift.py --classifier experiments\results\odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json --high-bits 19,20,24 --output experiments\results\odd_unit_lock_bridge_state_lift_d13_R18_to_R19_R20_R24_N1000000_20260705.json
```
