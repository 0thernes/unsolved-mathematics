# Branch-Prefix Retimed Signature

This note mines symbolic structure inside the exact `25 -> 26` retimed-pressure
class. It follows the depth sweep, but asks a different question:

```text
What local features distinguish the hard class, and can low residues alone
recognize it?
```

This is finite theorem-discovery data only. It does not prove Collatz.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_signature.py
```

Result:

```text
experiments/results/branch_prefix_retimed_signature_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_retimed_signature.py --parent-depth 25 --max-depth 1024 --top-n 12 --residue-top-n 12 --output experiments/results/branch_prefix_retimed_signature_d25_d26_20260702.json --quiet
```

The classifier recomputes the exact `25 -> 26` lift, selects transitions with:

```text
required_delta > 0
credit_delta < required_delta
```

and classifies every above-parent pressure unit by child bit, child descent
class, pressure event, last credit event, ladder alignment, lag, and low
residue buckets.

## Pure Dynamic Features

Counts:

```text
positive-pressure transitions:       71,321
retimed-pressure transitions:         5,677
first pressure units:                 5,677
all above-parent pressure units:      6,652
```

All checked pure-feature claims held:

```text
all retimed transitions are upper-lift child:      true
all pressure units are upper-lift child:           true
all retimed children are high-assisted descents:   true
all retimed transitions have a first pressure unit:true
all first pressure units are one-unit:             true
all pressure units have prior credit:              true
all pressure units have positive surplus:          true
```

Thus the `25 -> 26` retimed hard class is entirely carried by:

```text
child = parent + 2^25
```

and the child orbit always enters the high-alignment branch before descent.

## Pressure-Unit Regimes

Every above-parent pressure unit falls into one of three regimes:

```text
high_inside_active_ladder:  6,195
high_after_ladder_window:     340
low_repeat_prepaid:           117
```

Pressure event types:

```text
high_ladder_step:          6,195
ordinary_step:               457
```

Last credit kinds:

```text
high_ladder:               6,535
low_repeat:                  117
```

The first above-parent pressure unit is always one unit above parent:

```text
first required above parent:
1: 5,677
```

Later above-parent pressure units can continue the climb:

```text
required above parent, all pressure units:
1: 5,677
2:   834
3:   116
4:    20
5:     5
```

So the one-unit theorem target applies to the first above-parent threshold,
not to every later pressure observation.

## Lag Rigidity

For a high-ladder last credit with alignment `a`, define:

```text
lag_minus_align = (pressure_step - last_credit_step) - a
```

Observed high-ladder range:

```text
min lag_minus_align: -10
max lag_minus_align:   3
```

Histogram:

```text
high_ladder:-10      1
high_ladder:-9       1
high_ladder:-8       1
high_ladder:-7       7
high_ladder:-6      11
high_ladder:-5      19
high_ladder:-4      96
high_ladder:-3     215
high_ladder:-2     541
high_ladder:-1   1,358
high_ladder:0    3,945
high_ladder:3      340
```

The `340` post-ladder high cases are exactly the `high_ladder:3` bin. No
high-ladder pressure unit appeared with `lag_minus_align` equal to `1`, `2`,
or greater than `3`.

This isolates a concrete sublemma:

```text
If above-parent pressure is not inside the active high ladder, then in this
finite lift it appears exactly three shortcut steps after the prepaid ladder
window.
```

The low-repeat minority is also rigid in this finite lift:

```text
low_repeat:-6   2
low_repeat:-4  21
low_repeat:-2  21
low_repeat:-1  73
```

## Low-Residue Negative Result

The signature miner also checked whether low child residues alone identify the
retimed hard class. They do not.

For every tested modulus through `65536`, every retimed bucket was mixed with
non-retimed live child transitions:

| Modulus | Occupied Buckets | Retimed Buckets | Pure Retimed Buckets | Mixed Buckets | Retimed Covered by Pure Buckets |
|---:|---:|---:|---:|---:|---:|
| `16` | `3` | `3` | `0` | `3` | `0.0` |
| `64` | `8` | `8` | `0` | `8` | `0.0` |
| `256` | `19` | `19` | `0` | `19` | `0.0` |
| `1024` | `64` | `64` | `0` | `64` | `0.0` |
| `4096` | `226` | `226` | `0` | `226` | `0.0` |
| `65536` | `2,114` | `1,740` | `0` | `1,740` | `0.0` |

This is a useful negative theorem signal: the retimed-pressure class is not a
fixed low-residue table, at least through sixteen child bits. A proof should
not try to recognize the hard class from low child residues alone. It must use
the lifted child bit plus dynamic prefix timing: high-ladder entry, low-repeat
entry, and the first above-parent excess crossing.

## Corrected Lemma Target

The finite `25 -> 26` signature suggests this sharper local target:

```text
Retimed signature lemma:
For a live retimed-pressure child in the upper lift, the first above-parent
pressure event is one required-credit unit above the parent level. Before that
event, the child has entered either:

1. an active high ladder whose booked alignment credit covers the crossing;
2. the three-step post-ladder tail after a booked high ladder; or
3. a low-repeat gate whose booked repeat credit covers the crossing.
```

The open proof task is to derive these three regimes from the exact high ladder
law, the low `-5 mod 64` repeat law, and the one-bit frontier lift algebra.

## Multi-Depth Follow-Up

The companion sweep
[`BRANCH-PREFIX-RETIMED-SIGNATURE-SWEEP.md`](BRANCH-PREFIX-RETIMED-SIGNATURE-SWEEP.md)
checks the same signature claims on exact lifts `18 -> 19` through `25 -> 26`.
Across `13,856` retimed transitions and `16,085` above-parent pressure units,
all pure dynamic features above remain true, and the post-ladder tail remains
exactly the `lag_minus_align = 3` class at every checked depth. The low-residue
negative result also persists through modulus `65536`.

The first-threshold subset of that post-ladder class is analyzed in
[`BRANCH-PREFIX-RETIMED-POST-LADDER.md`](BRANCH-PREFIX-RETIMED-POST-LADDER.md):
all `572` checked first-threshold tails have terminal `6 mod 16`, shortcut word
`EOO`, and exact map `(9y + 10)/8`.
