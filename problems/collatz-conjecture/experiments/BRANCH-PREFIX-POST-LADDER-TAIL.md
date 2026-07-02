# Branch-Prefix Post-Ladder Tail

This note analyzes the `340` pressure units that the pressure-unit classifier
placed in the post-ladder high regime:

```text
high_after_ladder_window: 340
```

These are the smallest remaining symbolic subcase in the retimed pressure-unit
lift: pressure appears after the active high ladder has already burned out, but
the last visible credit is still that high ladder.

## Instrument

Script:

```text
experiments/branch_prefix_post_ladder_tail.py
```

Result:

```text
experiments/results/branch_prefix_post_ladder_tail_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_post_ladder_tail.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_post_ladder_tail_d25_d26_20260702.json --quiet
```

The script recomputes the exact `25 -> 26` lift, selects the retimed pressure
units with regime:

```text
high_after_ladder_window
```

and reconstructs the high ladder from the last credit state
`x = 2^a q - 1` through the terminal state:

```text
3^a q - 1
```

then records the next three shortcut steps.

## Result

```text
retimed transitions:                 5,677
all above-parent pressure units:     6,652
post-ladder tail units:                340
reconstruction failures:                 0
```

Pure finite claims:

```text
all tail units satisfy terminal formula:      true
all tail units satisfy lag = align + 3:       true
all tail units reconstruct pressure state:    true
all tail units have positive surplus:         true
single terminal 2-adic valuation:             true
single post-ladder parity word:               true
```

The exact shape:

```text
terminal_v2 = 1:       340
post parity word EOO:  340
terminal mod 16 = 6:   340
```

Thus the post-ladder tail is not arbitrary. In the exact lift, every tail unit
has:

```text
3^a q - 1 == 6 mod 16
```

and therefore the next three shortcut parities are:

```text
even, odd, odd
```

## Carry Identity

Let the high-ladder terminal be:

```text
y = 3^a q - 1
```

The finite tail data says `y = 16r + 6`. Then:

```text
T(y)   = 8r + 3        odd
T^2(y) = 12r + 5       odd
T^3(y) = 18r + 8       even
```

So the three-step post-ladder parity word is forced:

```text
E O O
```

This proves the small carry fact conditional on the congruence
`3^a q - 1 == 6 mod 16`. What remains unproved is the lift-local reason that
every post-ladder pressure unit in the retimed class must satisfy this
congruence.

## Tail Distribution

High-ladder alignments in the tail:

```text
a =  3: 113
a =  4:  75
a =  5:  58
a =  6:  42
a =  7:  23
a =  8:  15
a =  9:   6
a = 10:   6
a = 12:   2
```

Above-parent pressure level:

```text
required_above_parent = 1: 320
required_above_parent = 2:  18
required_above_parent = 3:   2
```

The tightest tail unit still has surplus `2`.

## Residue Shape

Terminal residues modulo `64`:

```text
6:  115
22:  70
38: 145
54:  10
```

All four are `6 mod 16`.

Last high-ladder entry states occupy only four residues modulo `64`:

```text
31:  58
39: 113
47:  75
63:  94
```

The tail children occupy the same eight residue classes modulo `64` as the
larger retimed class, but with smaller counts:

```text
7:   12
15:  19
27:  54
31:  55
39:  52
47:  54
59:  14
63:  80
```

## Theorem Signal

The post-ladder sublemma can now be stated more sharply:

```text
Post-ladder tail lemma:
If a retimed upper child has an above-parent pressure unit after a high ladder
has burned out, then the high-ladder terminal y = 3^a q - 1 satisfies
y == 6 mod 16. Consequently the next three shortcut parities are EOO, the
pressure unit appears at lag a + 3, and the previously booked ladder credit
still leaves positive surplus.
```

The carry part `y == 6 mod 16 => EOO` is elementary. The remaining hard part is
to derive `y == 6 mod 16` from the lift-local retimed-pressure hypotheses
instead of from enumeration.

## Congruence Follow-Up

The congruence audit
[`BRANCH-PREFIX-TAIL-CONGRUENCE.md`](BRANCH-PREFIX-TAIL-CONGRUENCE.md) checks
whether terminal `6 mod 16` characterizes the tail among all high-ladder
pressure units.

Result:

```text
tail units with terminal 6 mod 16:          340
active-ladder units with terminal 6 mod 16: 656
```

So `3^a q - 1 == 6 mod 16` is necessary for the exact post-ladder tail, but not
unique to it. The equivalent cofactor rule is:

```text
q == 7 * (3^a)^(-1) mod 16
```

The next lemma must combine this congruence with the condition that pressure
appears after the high ladder has burned out.

## Phase Follow-Up

The phase audit
[`BRANCH-PREFIX-TAIL-PHASE.md`](BRANCH-PREFIX-TAIL-PHASE.md) supplies the
missing finite separator in the exact `25 -> 26` lift.  Among terminal-`6 mod
16` high-ladder pressure units, all `340` post-ladder tails have positive
terminal threshold gap, while all `656` active-ladder terminal-6 cases have
nonpositive terminal threshold gap.

Thus the carry law proven in this note is used only after two conditions are
present:

```text
1. terminal congruence: 3^a q - 1 == 6 mod 16
2. terminal phase gap: positive
```

The first condition forces `EOO`; the second explains why the `EOO` carry is
where the next required-credit threshold is crossed.
