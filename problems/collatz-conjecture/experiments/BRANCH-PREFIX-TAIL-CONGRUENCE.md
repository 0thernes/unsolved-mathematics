# Branch-Prefix Tail Congruence

This note checks whether the post-ladder tail congruence

```text
3^a q - 1 == 6 mod 16
```

characterizes the tail, or only describes it.

The answer is precise: it describes every tail unit, but it is not unique to
the tail. Some active-ladder pressure units have the same terminal congruence.
So the next proof cannot use `6 mod 16` alone as a classifier.

## Instrument

Script:

```text
experiments/branch_prefix_tail_congruence.py
```

Result:

```text
experiments/results/branch_prefix_tail_congruence_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_congruence.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_tail_congruence_d25_d26_20260702.json --quiet
```

The script recomputes the exact `25 -> 26` retimed hard class, reconstructs
every high-ladder terminal attached to an above-parent pressure unit, and
checks the equivalent cofactor congruence:

```text
q == 7 * (3^a)^(-1) mod 16
```

## Result

```text
retimed transitions:              5,677
above-parent pressure units:      6,652
high-ladder pressure units:       6,535
post-ladder tail units:             340
```

Pure finite claims:

```text
all tail units have terminal mod 16 = 6:  true
all tail units match q mod 16 rule:       true
terminal mod 16 = 6 is unique to tail:    false
```

The congruence split by pressure regime:

```text
terminal 6 mod 16 in post-ladder tail:        340
terminal 6 mod 16 inside active high ladder:  656
```

So the terminal congruence is necessary for this exact post-ladder tail, but
not sufficient to identify the tail among all high-ladder pressure units.

## Equivalent Cofactor Rule

Since `3^a` is invertible modulo `16`,

```text
3^a q - 1 == 6 mod 16
```

is equivalent to:

```text
q == 7 * (3^a)^(-1) mod 16.
```

By `a mod 4`:

```text
a mod 4 = 0: q mod 16 = 7
a mod 4 = 1: q mod 16 = 13
a mod 4 = 2: q mod 16 = 15
a mod 4 = 3: q mod 16 = 5
```

Tail counts exactly match the rule:

```text
a mod 4 = 0, q mod 16 = 7:   92
a mod 4 = 1, q mod 16 = 13:  64
a mod 4 = 2, q mod 16 = 15:  48
a mod 4 = 3, q mod 16 = 5:  136
```

## Non-Uniqueness Obstruction

Terminal `6 mod 16` also appears in the active-ladder regime:

```text
high_inside_active_ladder, terminal mod 16 = 6: 656
```

Representative active examples still satisfy the same `q mod 16` rule and have
the same eventual `EOO` post-terminal parity word, but their pressure unit
occurs before the ladder has burned out. Therefore the correct proof split is:

```text
1. Active-ladder units:
   pressure occurs during the prepaid ladder, regardless of terminal mod 16.

2. Post-ladder units:
   pressure occurs after the ladder only in the congruence branch
   3^a q - 1 == 6 mod 16, forcing the EOO tail.
```

## Theorem Signal

The next symbolic target is now narrower and more honest:

```text
Tail congruence lemma:
In the retimed upper-child hard class, if an above-parent pressure unit occurs
after a high ladder has burned out, then the ladder cofactor satisfies
q == 7 * (3^a)^(-1) mod 16.
```

This lemma would imply `3^a q - 1 == 6 mod 16`, hence the three-step `EOO`
carry law from the post-ladder tail note. But terminal `6 mod 16` alone cannot
serve as a tail classifier because active-ladder pressure also occurs in that
terminal congruence branch.

## Phase Follow-Up

The phase audit
[`BRANCH-PREFIX-TAIL-PHASE.md`](BRANCH-PREFIX-TAIL-PHASE.md) checks the missing
separator among the `996` terminal-`6 mod 16` high-ladder pressure units.

Result:

```text
post-ladder terminal-6 units with positive terminal gap: 340
active terminal-6 units with nonpositive terminal gap:   656
```

So the refined finite classifier in the exact `25 -> 26` lift is:

```text
terminal 6 mod 16 + positive terminal threshold gap.
```

This does not prove the universal lift lemma, but it identifies the next exact
thing a proof has to derive from the upper-child frontier hypotheses: not just
the terminal congruence, but also the sign of the terminal phase gap.
