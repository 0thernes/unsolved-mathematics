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

## Threshold Fingerprint

The regenerated JSON now records aggregate timing fingerprints for the hard
class. The first above-parent threshold is always a one-unit pressure increase:

```text
required - parent_required:
1: 5,677
```

The threshold event itself is usually still inside the high ladder, with a
smaller ordinary-step tail:

```text
high_ladder_step: 5,245
ordinary_step:      432
```

The last counted credit before threshold was:

```text
prior high ladder: 5,565
prior low repeat:    112
```

For prior high-ladder cases, the last credit alignment ranged from `3` to `22`
and the last credit amount ranged from `1` to `20`. The threshold lag ranged
from `2` to `19`, with `lag - credit_amount` between `-8` and `5`. For prior
low-repeat cases, the repeat gate had `v2(x+5)` in `{6, 7, 8}`, threshold lag
was `2..5`, and `lag - credit_amount` was `1..4`.

Grouped threshold stats:

```text
prior_high_ladder:
  count:                    5,565
  threshold lag:            2..19, avg 4.732075472
  required above parent:    exactly 1
  threshold surplus:        2..25, avg 8.386163522

prior_low_repeat:
  count:                      112
  threshold lag:            2..5, avg 4.4375
  required above parent:    exactly 1
  threshold surplus:        4..22, avg 7.142857143
```

So the retimed-pressure obstruction is now smaller than "credit delta is
insufficient." It is a one-unit above-parent pressure event that always appears
after a visible local-grammar credit with at least two units of surplus.

## Depth-Sweep Check

The `25 -> 26` threshold surplus buffer of `2` is not universal. The companion
sweep [`BRANCH-PREFIX-RETIMED-SWEEP.md`](BRANCH-PREFIX-RETIMED-SWEEP.md)
checks exact lifts `18 -> 19` through `25 -> 26` and finds:

```text
retimed-pressure transitions checked: 13,856
retimed trace failures:                   0
all thresholds one-unit:               true
all thresholds prepaid:                true
minimum positive threshold margin:        1
```

Thus the stable finite pattern is not "surplus at least two"; it is
"one-unit above-parent pressure, prepaid before threshold, with nonnegative
prefix surplus." The proof target should use the depth-independent one-unit
and prepayment facts, not the accidental `25 -> 26` surplus margin.

## Signature Follow-Up

The companion classifier
[`BRANCH-PREFIX-RETIMED-SIGNATURE.md`](BRANCH-PREFIX-RETIMED-SIGNATURE.md)
mines the exact `25 -> 26` hard class for theorem-facing subcases. It finds
that all `5,677` retimed transitions are the upper lift child and
high-assisted descents. The `6,652` above-parent pressure units split into:

```text
inside active high ladder:       6,195
post-ladder tail:                  340
low-repeat prepaid:                117
```

The post-ladder tail is rigid in this finite lift: for a high-ladder credit
event of alignment `a`, every post-ladder pressure unit has
`(pressure_step - credit_step) - a = 3`.

The same classifier also rejects a tempting shortcut: no child-residue bucket
through modulus `65536` is pure retimed. The hard class is dynamic, not a fixed
low-bit residue table.

The signature claims were then swept across exact lifts `18 -> 19` through
`25 -> 26` in
[`BRANCH-PREFIX-RETIMED-SIGNATURE-SWEEP.md`](BRANCH-PREFIX-RETIMED-SIGNATURE-SWEEP.md).
The same three dynamic regimes and the same negative residue result persisted
over `13,856` retimed transitions and `16,085` pressure units.

The first threshold itself is isolated in
[`BRANCH-PREFIX-RETIMED-FIRST-THRESHOLD.md`](BRANCH-PREFIX-RETIMED-FIRST-THRESHOLD.md).
Across the same `13,856` retimed transitions, every first threshold is
one-unit and prepaid, but its offset from parent frontier depth ranges from
`1` to `99`. The proof invariant is therefore prepayment before threshold, not
a fixed small timing window after depth.

The post-ladder first-threshold subset is then reconstructed in
[`BRANCH-PREFIX-RETIMED-POST-LADDER.md`](BRANCH-PREFIX-RETIMED-POST-LADDER.md):
the `572` checked cases all have high-ladder terminal `y == 6 mod 16`,
shortcut tail `EOO`, and threshold state `(9y + 10)/8`.

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
the child's first above-parent pressure event is a one-unit required-credit
increase preceded by a visible high ladder or low-repeat gate whose accumulated
credit leaves positive surplus.
```

The exact checked transition has minimum threshold surplus `2`, so the finite
evidence even leaves a small buffer. The proof obligation is to derive this
from the affine lift bit and the low/high alignment grammar, not from
enumeration.
