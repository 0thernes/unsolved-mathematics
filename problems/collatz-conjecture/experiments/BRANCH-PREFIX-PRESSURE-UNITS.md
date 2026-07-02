# Branch-Prefix Pressure Units

This note strengthens the retimed-pressure audit. The previous timing audit
checked the first prefix where a retimed child needs more credit than its
parent ever needed. This audit checks every later above-parent required-credit
increase inside the same retimed hard class.

The point is narrow and falsifiable: a local lift proof cannot merely show that
the first above-parent pressure event is prepaid. It must show that every unit
of above-parent pressure remains prepaid until descent.

## Instrument

Script:

```text
experiments/branch_prefix_pressure_units.py
```

Result:

```text
experiments/results/branch_prefix_pressure_units_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_pressure_units.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_pressure_units_d25_d26_20260702.json --quiet
```

The script recomputes the exact `25 -> 26` lift, selects the same retimed
transitions:

```text
required_delta > 0
credit_delta < required_delta
```

and then inspects every pressure event satisfying:

```text
child required credit > parent max required credit
```

## Result

```text
positive-pressure transitions:            71,321
retimed-pressure transitions:              5,677
fully unit-certified retimed transitions:  5,677
transition failures:                           0

above-parent pressure units:               6,652
pressure-unit failures:                        0
tight pressure units:                          0
minimum pressure-unit surplus:                 2
maximum pressure-unit surplus:                30
maximum required above parent:                 5
maximum threshold lag:                        21
```

Timing classes over pressure units:

```text
prior high-ladder credit:                 6,535
prior low-repeat credit:                    117
```

Every retimed child in the exact `25 -> 26` lift is therefore certified at the
level of each above-parent pressure unit, not only at the first threshold
crossing.

## Pressure-Unit Shape

How many above-parent pressure units each retimed transition had:

```text
1 unit:   4,843 transitions
2 units:    718 transitions
3 units:     96 transitions
4 units:     15 transitions
5 units:      5 transitions
```

Pressure levels above the parent:

```text
required_above_parent = 1:  5,677 events
required_above_parent = 2:    834 events
required_above_parent = 3:    116 events
required_above_parent = 4:     20 events
required_above_parent = 5:      5 events
```

The tightest pressure units still had surplus `2`. The two tightest examples
were:

```text
parent -> child:       8,250,439 -> 41,804,871
parent required:       1
child required:        2
event:                 high_ladder_step
last credit:           high_ladder, align 3, amount 1
threshold lag:         3
surplus at pressure:   2

parent -> child:       27,101,095 -> 60,655,527
parent required:       1
child required:        2
event:                 high_ladder_step
last credit:           high_ladder, align 3, amount 1
threshold lag:         3
surplus at pressure:   2
```

Largest above-parent pressure level observed:

```text
parent -> child:       24,264,191 -> 57,818,623
parent required:       5
child required:        10
required above parent: 5
event index:           5
event:                 high_ladder_step
last credit:           high_ladder, align 6, amount 4
threshold lag:         6
surplus at pressure:   19
```

## Theorem Signal

The finite hard class now suggests a sharper lemma than the first retimed
audit:

```text
Pressure-unit lift lemma:
For every live retimed child with required_delta > 0 and
credit_delta < required_delta, each prefix at which the child required credit
exceeds the parent maximum required credit has already received visible
high-ladder or low-repeat credit, and the accumulated credit remains strictly
above the required pressure.
```

The exact checked lift leaves a minimum surplus of `2` at every above-parent
pressure unit. That is still finite evidence, not a proof of Collatz. The proof
obligation is to derive this unit-pressure timing from the affine lift bit and
the low/high alignment grammar without enumerating the depth-26 frontier.

## Classifier Follow-Up

The symbolic classifier
[`BRANCH-PREFIX-PRESSURE-UNIT-CLASSIFIER.md`](BRANCH-PREFIX-PRESSURE-UNIT-CLASSIFIER.md)
splits the `6,652` units into three regimes:

```text
high_inside_active_ladder:  6,195
high_after_ladder_window:     340
low_repeat_prepaid:           117
```

It also finds five pure finite features in the exact `25 -> 26` lift:

```text
all retimed transitions are upper-lift child:  true
all pressure units are upper-lift child:       true
all retimed children are high-assisted:        true
all pressure units have prior credit:          true
all pressure units have positive surplus:      true
```

The remaining post-ladder tail is especially rigid: all `340` high-after-ladder
pressure units have `lag_minus_align = 3`.
