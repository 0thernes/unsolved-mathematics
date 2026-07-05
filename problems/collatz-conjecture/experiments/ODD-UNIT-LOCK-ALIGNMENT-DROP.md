# Odd-Unit Lock Alignment-Drop Analyzer

**Date:** 2026-07-05
**Instrument:** [`odd_unit_lock_alignment_drop_analyzer.py`](odd_unit_lock_alignment_drop_analyzer.py)
**Result:** [`results/odd_unit_lock_alignment_drop_20260705.json`](results/odd_unit_lock_alignment_drop_20260705.json)
**Inputs:**
[`results/odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R16_N250000_20260705.json),
[`results/odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R17_N1000000_20260705.json),
[`results/odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json`](results/odd_unit_lock_bridge_classifier_d13_R18_N1000000_20260705.json)

Status: finite bridge-mechanism classification. This proves no part of the
Collatz conjecture.

## Question

The bridge classifier split repeated odd-unit locks into two broad cases:

```text
positive-fresh bridges: the next lock needs new quotient bits;
zero-fresh bridges: the previous lock already forces the next unit residue.
```

The second case is the scary one. This analyzer asks whether the measured
zero-fresh bridges are genuinely persistent for free, or whether they burn a
finite alignment reserve.

## Main Result

Across the measured `R = 16`, `R = 17`, and `R = 18` bridge classifiers:

| Quantity | Value |
|---|---:|
| Bridge families analyzed | 7 |
| Repeat transition records represented | 80 |
| Positive-fresh families | 1 |
| Positive-fresh transition records | 62 |
| Zero-fresh families | 6 |
| Zero-fresh transition records | 18 |
| Min zero-fresh alignment drop | 2 |
| Max zero-fresh alignment drop | 3 |

All checks pass:

- every fresh-bit formula matches `max(0, gap + next_m - previous_m)`;
- every measured zero-fresh bridge has `previous_m > next_m`;
- every zero-fresh bridge with an available `R = 20` / `R = 24` refinement dies
  as a repeated higher-precision lock.

## Mechanism Split

| Mechanism | Families | Repeat records | Interpretation |
|---|---:|---:|---|
| `positive-fresh-cost` | 1 | 62 | Dominant `R = 16` bridge pays `7` fresh quotient bits |
| `zero-fresh-self-spine-burn` | 2 | 8 | Same-source `011 -> 011` bridges burn alignment by `3` |
| `zero-fresh-reserve-burn` | 3 | 9 | Target/source offset has spare transport reserve; alignment drops by `2` or `3` |
| `zero-fresh-balanced-burn` | 1 | 1 | Edge-balanced alignment drop with no spare reserve |

The measured zero-fresh families are:

| R | Source pair | Count | Gap word | Previous m -> next m | Reserve | Mechanism |
|---:|---|---:|---|---|---:|---|
| 16 | `011 -> 011` | 7 | `011` | `10 -> 7` | 0 | self-spine burn |
| 16 | `0011101111 -> 011101111` | 3 | `0` | `12 -> 10` | 1 | reserve burn |
| 16 | `011 -> 011` | 1 | `011` | `7 -> 4` | 0 | self-spine burn |
| 17 | `0011111 -> 011111` | 3 | `0` | `10 -> 7` | 2 | reserve burn |
| 17 | `0110111111 -> 0111111` | 1 | `011` | `11 -> 8` | 0 | balanced burn |
| 18 | `0011111 -> 011111` | 3 | `0` | `10 -> 7` | 2 | reserve burn |

## Why This Matters

The old weak hope was:

```text
Odd-unit lock hits are sparse, so repeated hits should be rare.
```

That is false as stated: coarse positive orbits have memory.

The better theorem target is:

```text
Repeated odd-unit locks either pay fresh quotient bits, or they are zero-fresh
alignment-drop bridges that consume a finite alignment reserve and lose
refined lock depth.
```

This is still not a Collatz proof. It is a sharper obstruction ledger. It says
the measured zero-fresh loophole is not a free perpetual-motion mechanism; it is
an alignment-burning mechanism in the finite data we have.

## Non-Claims

- This is not a proof of Collatz.
- It analyzes only measured bridge families from the current finite scans.
- It does not prove that every possible zero-fresh bridge is alignment-dropping.
- It does not prove a uniform bound on alignment-reserve regeneration.
- It does not prove that larger source/target libraries introduce no new
  zero-fresh mechanism.

## Next Theorem Target

Prove a symbolic alignment-drop lemma:

```text
For any zero-fresh repeated odd-unit lock bridge along a positive orbit, either
the bridge strictly decreases alignment height m, or it belongs to a finite
exception class whose refined lock depth is uniformly bounded.
```

Then connect that lemma to the retimed reserve-source stack: alignment can rise
again only by paying structural reserve, so free repeated locks cannot persist
without a separate replenishment budget.

## Reproduce

```powershell
python -m py_compile experiments\odd_unit_lock_alignment_drop_analyzer.py
python experiments\odd_unit_lock_alignment_drop_analyzer.py --output experiments\results\odd_unit_lock_alignment_drop_20260705.json
python -m json.tool experiments\results\odd_unit_lock_alignment_drop_20260705.json > $null
```
