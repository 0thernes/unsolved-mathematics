# Branch-Prefix Retimed Pressure

This note traces the hard subcase isolated by the parent-child transition
audit: live children whose required prefix credit increases, but whose total
structural credit does not increase enough relative to the parent.

These are the retimed-pressure cases. They are not failures; every checked child
still has zero prefix deficit. The question is what visible event timing keeps
them solvent.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_pressure.py
```

Result:

```text
experiments/results/branch_prefix_retimed_pressure_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_retimed_pressure.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_retimed_pressure_d25_d26_20260702.json --quiet
```

The script recomputes the exact `25 -> 26` lift, selects transitions with:

```text
required_delta > 0
credit_delta < required_delta
```

and traces the child prefix ledger to the first moment its required credit
exceeds the parent required credit.

## Result

```text
positive-pressure transitions:       71,321
retimed-pressure transitions:         5,677
retimed prefix failures:                  0
max trace deficit:                       0
minimum threshold surplus:               2
maximum threshold surplus:              25
maximum threshold lag:                  19
```

Timing classes:

```text
prior high-ladder credit:            5,565  (98.0271%)
prior low-repeat credit:               112  (1.9729%)
```

So every retimed-pressure child was already prepaid by a visible structural
credit event before the first prefix where it exceeded the parent pressure.

## Threshold Timing

The threshold is:

```text
first t where child R_t > parent max_prefix_required
```

Lag is:

```text
threshold_lag = threshold_step - last_credit_event_step
```

Observed lags:

```text
2:    264
3:  1,674
4:  1,409
5:    815
6:    558
7:    337
8:    237
9:    169
10:    88
11:    52
12:    30
13:    18
14:    11
15:     5
16:     4
17:     2
18:     3
19:     1
```

Every threshold had positive surplus. The minimum observed threshold surplus
was `2`.

## Extremal Cases

Largest crude total-delta shortfall:

```text
parent:                  12,132,095
child:                   45,686,527
parent required:                  5
child required:                   6
required delta:                   1
parent C_unit:                   58
child C_unit:                    17
credit delta:                   -41
crude shortfall:                 42
timing class:          prior_high_ladder
threshold lag:                   4
threshold surplus:              10
child prefix deficit:            0
```

Largest required-delta case among retimed-pressure transitions:

```text
parent:                  26,979,431
child:                   60,533,863
parent required:                  6
child required:                  11
required delta:                   5
parent C_unit:                   35
child C_unit:                    32
credit delta:                    -3
crude shortfall:                  8
timing class:          prior_high_ladder
threshold lag:                   3
threshold surplus:              11
child prefix deficit:            0
```

Largest lag:

```text
parent:                  15,419,387
child:                   48,973,819
parent required:                  6
child required:                   7
required delta:                   1
threshold lag:                  19
timing class:          prior_high_ladder
threshold surplus:              12
child prefix deficit:            0
```

## Theorem Signal

The hard subcase is not mysterious after timing is exposed:

```text
Every retimed-pressure child in the exact 25 -> 26 lift receives visible
high-ladder or low-repeat credit before its required prefix credit first
exceeds the parent's required prefix credit.
```

This suggests the next local lemma:

```text
Retimed-pressure lemma:
If a live child has required_delta > 0 but credit_delta < required_delta, then
the child's first above-parent pressure event is preceded by a visible high
ladder or low-repeat gate whose accumulated credit leaves positive surplus.
```

The exact checked transition has minimum threshold surplus `2`, so the finite
evidence even leaves a small buffer. The proof obligation is to derive this
from the affine lift bit and the low/high alignment grammar, not from
enumeration.
