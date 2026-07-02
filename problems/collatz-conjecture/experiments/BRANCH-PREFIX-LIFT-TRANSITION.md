# Branch-Prefix Lift Transition

This note opens the local `25 -> 26` lift and classifies parent-to-child
transitions for the prefix branch-potential ledger.

The previous lift audit showed:

```text
depth 25 live parents:        573,162
depth 26 live children:     1,037,374
pruned siblings:              108,950
orphan live children:               0
prefix failures:                    0
```

This transition audit asks how the child pressure changes relative to the
parent, and whether new structural credit pays that pressure locally.

## Instrument

Script:

```text
experiments/branch_prefix_lift_transition.py
```

Result:

```text
experiments/results/branch_prefix_lift_transition_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_lift_transition.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_lift_transition_d25_d26_20260702.json --quiet
```

## Lift Summary

```text
live parents at depth 25:       573,162
live children at depth 26:    1,037,374
pruned siblings:                108,950
orphan live children:                 0
```

Parent child-count split:

```text
parents with one live child:    108,950
parents with two live children: 464,212
```

Child-bit split:

```text
live child bit 0:               518,525
live child bit 1:               518,849
pruned child bit 0:              54,637
pruned child bit 1:              54,313
```

Both live children and pruned siblings passed the prefix condition:

| Population | Count | Uncertified | Prefix Failures | Max Escape | Max Excess | Max Prefix Required |
|---|---:|---:|---:|---:|---:|---:|
| live children | `1,037,374` | `0` | `0` | `376` | `14.444979039` | `14` |
| pruned siblings | `108,950` | `0` | `0` | `26` | `5.905123943` | `5` |

## Required-Credit Delta

For each live child, compare:

```text
required_delta = child.max_prefix_required - parent.max_prefix_required
credit_delta   = child.C_unit - parent.C_unit
```

Required-delta signs:

```text
negative required delta:         67,749
zero required delta:            898,304
positive required delta:         71,321
```

Transition classification:

```text
nonincreasing required:         966,053
increased required:              71,321
  paid by new credit:            65,644
  partially paid by new credit:     278
  without new credit:             5,399
```

Thus `966,053 / 1,037,374 = 93.1249%` of live child transitions need no new
required credit at all. Of the `71,321` positive-pressure transitions,
`65,644 / 71,321 = 92.0402%` are paid directly by new total structural credit.

The remaining `5,677` positive-pressure transitions are not failures; every one
still has zero prefix deficit. They mark the proof obligation that cannot be
captured by the crude total-delta comparison alone.

## Extremal Transitions

Largest required-credit increase:

```text
parent:                 5,722,367
child:                 39,276,799
child bit:                      1
parent required:                2
child required:                13
required delta:                11
parent C_unit:                 14
child C_unit:                  73
credit delta:                  59
high-credit delta:             60
low-credit delta:              -1
child max excess:       13.814049286
child prefix deficit:           0
```

Largest positive-pressure shortfall under crude total-delta accounting:

```text
parent:                12,132,095
child:                 45,686,527
child bit:                      1
parent required:                5
child required:                 6
required delta:                 1
parent C_unit:                 58
child C_unit:                  17
credit delta:                 -41
delta shortfall:               42
child max excess:        6.393739611
child prefix deficit:           0
```

This case is important: total child credit can be much lower than total parent
credit while the child still has no prefix deficit. Therefore the proof cannot
be a naive monotone-credit inheritance theorem.

## Theorem Signal

The local lift theorem should split into at least three cases:

```text
1. Nonincreasing pressure:
   child required credit <= parent required credit.

2. Fresh-credit pressure:
   child required credit increases, and a visible high-ladder / low-repeat
   event pays the increase.

3. Retimed-pressure cases:
   child required credit increases but total child credit is not larger enough
   than total parent credit. These require a direct prefix-timing argument, not
   a parent-total-credit monotonicity argument.
```

The finite transition audit found no prefix failures in any case. Its honest
contribution is to reject an overly simple proof and isolate the smaller hard
case: `5,677` positive-pressure transitions at `25 -> 26` where local total
credit delta does not by itself explain the zero-deficit prefix ledger.

## Retimed-Pressure Follow-Up

The hard subcase is traced in
[`BRANCH-PREFIX-RETIMED-PRESSURE.md`](BRANCH-PREFIX-RETIMED-PRESSURE.md).

Result:

```text
retimed-pressure transitions:         5,677
retimed trace failures:                   0
max trace deficit:                       0
minimum threshold surplus:               2
prior high-ladder credit:            5,565
prior low-repeat credit:               112
```

So the finite hard class is not unexplained after timing is exposed: every
retimed-pressure child receives visible branch credit before above-parent
pressure appears. The proof target is now to derive that timing fact from the
lifted residue bit and the low/high alignment grammar.
