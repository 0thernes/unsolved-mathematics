# Branch-Prefix Frontier Lift

This note checks the proposed lift theorem behind branch-prefix dominance.

The base-24 exact frontier pass showed zero prefix failures on every live
residue modulo `2^24`. The next question is whether the property survives as
the survivor frontier is refined to deeper residues.

This is still finite evidence. It is not a proof of Collatz.

## Instrument

Script:

```text
experiments/branch_prefix_frontier_lift.py
```

Result:

```text
experiments/results/branch_prefix_frontier_lift_d24_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_frontier_lift.py --depths 24 25 26 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_frontier_lift_d24_d26_20260702.json --quiet
```

The script enumerates the exact certificate survivor frontier at each requested
depth, runs the entry-credit prefix-dominance check on every positive live
residue, and records how live residues lift from one checked depth to the next.

## Aggregate Result

```text
depths checked:                 24, 25, 26
total frontier rows checked:    1,897,117
uncertified:                            0
prefix C_unit failures:                 0
max prefix deficit:                     0
min prefix surplus:                     0
max prefix required credit:            14
```

Depth summaries:

| Depth | Live Residues | Frontier Fraction | Max Escape | Max Excess | Max Prefix Required | Prefix Failures |
|---:|---:|---:|---:|---:|---:|---:|
| `24` | `286,581` | `0.01708155870437622` | `287` | `13.954462671` | `13` | `0` |
| `25` | `573,162` | `0.01708155870437622` | `298` | `14.444979039` | `14` | `0` |
| `26` | `1,037,374` | `0.015458077192306519` | `376` | `14.444979039` | `14` | `0` |

Class split:

| Depth | High-Assisted | Low-Repeat | Low-Direct |
|---:|---:|---:|---:|
| `24` | `286,575` | `6` | `0` |
| `25` | `573,147` | `15` | `0` |
| `26` | `1,037,363` | `11` | `0` |

## Lift Histograms

Every checked live child had a live parent at the previous checked depth.

Depth `24 -> 25`:

```text
previous live parents:          286,581
current live children:          573,162
children with live parent:      573,162
orphan children:                      0
parents without children:             0
children per parent:
  2 children:                  286,581
```

Depth `25 -> 26`:

```text
previous live parents:          573,162
current live children:        1,037,374
children with live parent:    1,037,374
orphan children:                      0
parents without children:             0
children per parent:
  1 child:                     108,950
  2 children:                  464,212
```

So the checked lift has no extinction of live parents and no spontaneous
frontier children outside the previous frontier. At `25 -> 26`, pruning appears
as one child being certified while the sibling remains live.

## Largest Pressure Cases

Largest excess across all three depths:

```text
start:                  19,638,399
frontier depth:         25
frontier odd count:     19
escape depth:           264
max excess:             14.444979039
max prefix required:    14
high ladder credit:     72
low repeat credit:      0
C_unit:                 72
max prefix deficit:     0
```

Longest escape across all three depths:

```text
start:                  63,728,127
frontier depth:         26
frontier odd count:     24
escape depth:           376
max excess:             8.131880104
max prefix required:    8
high ladder credit:     85
low repeat credit:      3
C_unit:                 88
max prefix deficit:     0
```

## Theorem Target

The finite result points to a concrete lift theorem:

```text
If r is a positive live survivor residue at depth d and prefix dominance holds
for r, then every live child of r at depth d+1 either:

  1. inherits prefix dominance from r,
  2. receives visible high-ladder or low-repeat credit before new prefix debt,
     or
  3. certifies descent and leaves the frontier.
```

The exact checked depths support the shape:

* no current live child had a non-live parent;
* no live parent had zero live children across `24 -> 25 -> 26`;
* all live children still had zero prefix deficit.

The universal proof obligation is to derive this from the affine residue
transition, not from enumeration.

## Transition Follow-Up

The `25 -> 26` lift is opened in
[`BRANCH-PREFIX-LIFT-TRANSITION.md`](BRANCH-PREFIX-LIFT-TRANSITION.md).

It compares child required-credit deltas against child structural-credit deltas:

```text
live child transitions:       1,037,374
nonincreasing required:         966,053
increased required:              71,321
  paid by new credit:            65,644
  partially paid by new credit:     278
  without new credit:             5,399
live child prefix failures:           0
pruned sibling prefix failures:        0
```

This rejects a too-simple monotone total-credit proof. The hard subcase is the
retimed-pressure class where the child has increased required credit but the
parent-to-child total-credit delta is insufficient. Those cases still have zero
prefix deficit in the exact audit, so they are the next local theorem target.
