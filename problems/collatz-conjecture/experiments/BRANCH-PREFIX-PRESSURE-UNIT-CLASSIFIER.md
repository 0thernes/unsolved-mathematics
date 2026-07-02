# Branch-Prefix Pressure-Unit Classifier

This note mines theorem-facing structure from the pressure-unit audit. It does
not add a proof of Collatz. It narrows the retimed-pressure lift lemma into a
small set of symbolic subcases.

## Instrument

Script:

```text
experiments/branch_prefix_pressure_unit_classifier.py
```

Result:

```text
experiments/results/branch_prefix_pressure_unit_classifier_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_pressure_unit_classifier.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_pressure_unit_classifier_d25_d26_20260702.json --quiet
```

The classifier recomputes the exact `25 -> 26` lift, selects the same retimed
transitions,

```text
required_delta > 0
credit_delta < required_delta
```

and classifies every above-parent pressure unit by lifted child bit, pressure
event, last credit event, ladder alignment, lag, and local residues.

## Pure Feature Claims

All five finite purity claims held:

```text
all retimed transitions are upper-lift child:  true
all pressure units are upper-lift child:       true
all retimed children are high-assisted:        true
all pressure units have prior credit:          true
all pressure units have positive surplus:      true
```

Counts:

```text
retimed transitions:       5,677
pressure units:            6,652
child bit split:           bit 1 only
retimed child classes:     high-assisted-descent only
```

Thus the retimed hard class is not a two-child lift phenomenon in this exact
frontier: it is entirely carried by the upper child `child = parent + 2^25`.

## Three Pressure Regimes

Every pressure unit falls into one of three regimes:

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

The active-ladder majority is directly aligned with the exact ladder identity:
the pressure unit appears during a high ladder whose credit has already been
booked.

The low-repeat minority is directly aligned with the exact low grammar:
the last counted event is `x == -5 mod 64`.

The remaining post-ladder tail is the interesting new subcase.

## Lag Rigidity

For a high-ladder last credit event with alignment `a`, define:

```text
lag_minus_align = (pressure_step - last_credit_step) - a
```

Observed range:

```text
min lag_minus_align: -10
max lag_minus_align:   3
```

Histogram by last-credit kind:

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
low_repeat:-6        2
low_repeat:-4       21
low_repeat:-2       21
low_repeat:-1       73
```

The `340` post-ladder high cases are exactly the `high_ladder:3` bin. In this
finite lift, there is no high-ladder pressure unit with `lag_minus_align` equal
to `1`, `2`, or greater than `3`.

That turns the post-ladder tail into a concrete sublemma target:

```text
After a prepaid high ladder burns out, the only above-parent pressure units
that appear outside the active ladder occur exactly three shortcut steps after
the ladder window.
```

This is not proven yet; it is the next symbolic fact to derive from the
terminal state `3^a q - 1` and the ordinary-step carry pattern.

## Alignment Support

High-ladder last-credit alignments:

```text
a =  3: 1,543
a =  4: 1,508
a =  5: 1,195
a =  6:   713
a =  7:   531
a =  8:   383
a =  9:   240
a = 10:   160
a = 11:   109
a = 12:    65
a = 13:    26
a = 14:    23
a = 15:    12
a = 16:     7
a = 17:     6
a = 18:     7
a = 19:     5
a = 22:     2
```

Low-repeat last-credit alignments:

```text
minus5 align 6: 94
minus5 align 7: 21
minus5 align 8:  2
```

## Residue Support

The retimed upper children occupy only eight residues modulo `64`:

```text
7, 15, 27, 31, 39, 47, 59, 63
```

Counts:

```text
7:    183
15:   175
27:   851
31:   831
39:   827
47:   793
59:   194
63: 1,823
```

At modulo `256`, the retimed children occupy `19` residue classes. This is
small enough to be useful as a local grammar target, but not so small that a
fixed tiny lookup table looks like a proof.

Last-credit states occupy nine residues modulo `64`:

```text
7, 15, 23, 31, 39, 47, 55, 59, 63
```

The `59` class is the low-repeat gate. The other classes are high-ladder entry
states with varying alignment.

## Theorem Signal

The pressure-unit lift lemma can now be split into three explicit sublemmas:

```text
1. Upper-child localization:
   Retimed pressure can only occur on the upper lift child.

2. Active-ladder pressure:
   If the above-parent pressure unit occurs during a high ladder, the booked
   high-ladder credit already dominates the required credit.

3. Tail pressure:
   If the above-parent pressure unit occurs after the high ladder window, then
   it appears exactly three shortcut steps after the ladder burn and remains
   prepaid by the same ladder credit.

4. Low-repeat pressure:
   If the last credit is low-repeat, the `-5 mod 64` repeat-gate credit occurs
   before the above-parent pressure unit and leaves positive surplus.
```

The numbering deliberately separates the active-ladder and tail high-ladder
cases. The tail pressure case is now the smallest unresolved symbolic
sublemma exposed by the finite classifier.

## Post-Ladder Tail Follow-Up

The tail subcase is analyzed in
[`BRANCH-PREFIX-POST-LADDER-TAIL.md`](BRANCH-PREFIX-POST-LADDER-TAIL.md).

Result:

```text
post-ladder tail units:       340
reconstruction failures:        0
terminal_v2 = 1:              340
terminal mod 16 = 6:          340
post parity word EOO:         340
```

Thus `lag_minus_align = 3` is explained by a concrete carry pattern. If the
high-ladder terminal is `y = 3^a q - 1 = 16r + 6`, then:

```text
T(y)   = 8r + 3
T^2(y) = 12r + 5
T^3(y) = 18r + 8
```

The next proof target is no longer "explain lag 3" in general; it is to derive
`3^a q - 1 == 6 mod 16` from the retimed upper-child hypotheses.
