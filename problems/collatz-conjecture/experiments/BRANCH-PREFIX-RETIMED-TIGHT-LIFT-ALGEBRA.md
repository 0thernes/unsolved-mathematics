# Branch-Prefix Retimed Tight Lift Algebra

Date: 2026-07-02

This note checks the parent/upper-child lift algebra behind the five tight
surplus-`1` layer-one pressure units. It is finite theorem-discovery evidence,
not a proof of the Collatz conjecture.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_tight_lift_algebra.py
```

Command:

```powershell
python experiments/branch_prefix_retimed_tight_lift_algebra.py --output experiments/results/branch_prefix_retimed_tight_lift_algebra_d18_d25_20260702.json
```

Input:

```text
experiments/results/branch_prefix_retimed_tight_layer_one_d18_d25_20260702.json
```

Output:

```text
experiments/results/branch_prefix_retimed_tight_lift_algebra_d18_d25_20260702.json
```

## Affine lift law

For an upper lift `child = parent + 2^d`, the parent and child share the first
`d` shortcut parities by the proved
[`BRANCH-PREFIX-AFFINE-LIFT-LEMMA.md`](BRANCH-PREFIX-AFFINE-LIFT-LEMMA.md).
Their iterates obey

```text
T^j(child) - T^j(parent) = 3^o_j 2^(d-j),     0 <= j <= d,
```

where `o_j` is the number of odd shortcut steps in the shared prefix of length
`j`. The checker verifies this identity directly for all five tight records,
but the identity itself is a local theorem of the shortcut map.

Direct checks:

```text
record_count:                               5
all affine lift laws hold to depth:         true
all parities are shared before depth d:     true
all boundary pairs are parent even -> child odd: true
all pressure events occur at step d + 1:    true
all pressure last steps are the depth step: true
all pressure last steps are odd:            true
all child excess gaps at pressure are 1:    true
```

The depth-boundary deltas are:

```text
d = 18: T^18(child) - T^18(parent) = 3^13 = 1,594,323
d = 21: T^21(child) - T^21(parent) = 3^15 = 14,348,907
```

Thus the tight pressure is exactly a boundary phenomenon: before depth `d`,
parent and child have the same odd count; at depth `d`, the parent takes an
even step and the upper child takes an odd step. One step later, the child's
excess is exactly one unit above the parent's excess.

```text
d = 18: parent excess at d+1 = 1.012334682, child excess = 2.012334682
d = 21: parent excess at d+1 = 1.119545421, child excess = 2.119545421
```

This explains why the required credit jumps from parent requirement `1` to
child requirement `2` at the tight pressure event.

## Local words

The five local words from high-ladder entry to pressure are:

```text
OOO:    3
OOOEOO: 2
```

The split is exact:

```text
active terminal align-3 ladder:
  entry offset from depth:    -2
  terminal offset from depth: +1
  word:                       OOO

post-terminal EOO:
  entry offset from depth:    -5
  terminal offset from depth: -2
  word:                       OOOEOO
```

In both cases the high-ladder entry has alignment exactly `3`:

```text
child entry mod 16: 7 in all five cases
child entry = 8q - 1
terminal y = 27q - 1
```

The active cases take the pressure at the terminal state `y`. The post cases
take pressure after the `EOO` tail:

```text
EOO(y) = (9y + 10) / 8.
```

All terminal and pressure formulas match the recorded states.

## Congruence trace at entry

The entry congruence is also forced by where the high ladder sits relative to
the lift boundary:

```text
active OOO:
  entry step = d - 2
  lift delta at entry = 3^o * 2^2
  child entry == 7 mod 16
  parent entry == 11 mod 16

post OOOEOO:
  entry step = d - 5
  lift delta at entry = 3^o * 2^5
  child entry == 7 mod 16
  parent entry == 7 mod 16
```

Observed counts:

```text
entry offset -2: 3
entry offset -5: 2
entry delta power 2: 3
entry delta power 5: 2
parent entry mod 16 = 11: 3
parent entry mod 16 = 7:  2
child entry mod 16 = 7:   5
```

## Theorem target

The earlier tight-layer note reduced the base case to align-3 high-ladder
states. This lift-algebra note sharpens the target:

```text
Tight lift-boundary target:
For a live upper-lift retimed transition with surplus 1 at its first
above-parent pressure event, prove that the parent and child share the first
d shortcut parities, that the depth-d parity pair is E->O, and that the odd
boundary step sits inside either an OOO align-3 terminal ladder or an OOOEOO
align-3 post-terminal tail.
```

Equivalently, prove the five finite observations from the live upper-lift
algebra rather than by enumeration:

```text
affine prefix law + E->O boundary + align-3 entry + local word in {OOO, OOOEOO}
```

This remains a local finite certificate, but the proof object is now smaller:
one affine lift identity, one boundary parity flip, and one align-3 local word
classification.

The affine lift identity is now discharged by
[`BRANCH-PREFIX-AFFINE-LIFT-LEMMA.md`](BRANCH-PREFIX-AFFINE-LIFT-LEMMA.md).
What remains open is the retimed-specific implication from live upper-lift
surplus-`1` pressure to `E->O` boundary type and align-3 local word
classification.
