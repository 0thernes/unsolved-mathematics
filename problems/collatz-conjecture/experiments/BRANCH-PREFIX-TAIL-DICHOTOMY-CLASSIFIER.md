# Branch-Prefix Tail Dichotomy Classifier

This note mines finite classifiers for the split exposed by
[`BRANCH-PREFIX-TAIL-GHOST-CLASS.md`](BRANCH-PREFIX-TAIL-GHOST-CLASS.md):

```text
334 terminal-local post-ladder tail cases
  6 lag-8 memory-tail cases
```

It does not solve Collatz. It asks what local features separate those two
classes in the exact `25 -> 26` retimed hard lift.

## Instrument

Script:

```text
experiments/branch_prefix_tail_dichotomy_classifier.py
```

Result:

```text
experiments/results/branch_prefix_tail_dichotomy_classifier_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_dichotomy_classifier.py --parent-depth 25 --max-depth 1024 --top-n 12 --max-feature-set-size 3 --output experiments/results/branch_prefix_tail_dichotomy_classifier_d25_d26_20260702.json --quiet
```

The script recomputes all `340` post-ladder tail units and labels each one:

```text
terminal_local   if the terminal observation itself is the max source
memory_lag_8     if the max source is eight shortcut steps before terminal
```

It then searches feature sets up to size `3`.

## Population Check

```text
record count:       340
terminal_local:     334
memory_lag_8:         6
```

The six memory sources are still exactly:

```text
EEOOEOOO: 5
EEOEOOOO: 1
```

with full source classes:

```text
EEOOEOOO:  6508 mod 16384  count 3
EEOOEOOO: 14700 mod 16384  count 2
EEOEOOOO: 10148 mod 16384  count 1
```

Pure finite claims:

```text
all sources found:                                      true
population is 340:                                      true
labels are terminal_local or memory_lag_8:              true
six memory records:                                     true
memory sources are two known words:                     true
has pure feature set:                                   true
has memory-pure feature set:                            true
no terminal/event feature set of searched size is pure: true
no terminal/event feature set is memory-pure:           true
```

## Negative Result: Terminal/Event Features Do Not Separate

Searching terminal/event-side features up to triples found:

```text
pure feature sets:        0
memory-pure feature sets: 0
```

Even a hand-picked six-feature terminal/event bucket remains mixed:

```text
terminal_step, event_step, align, q_mod64, terminal_mod64, terminal_current_gap
```

The three mixed memory buckets are:

```text
35|38|3|37|38|0.081541375001010298483449 : memory 3, terminal-local 8
35|38|3|5 |6 |0.081541375001010298483449 : memory 2, terminal-local 3
35|38|4|55|38|0.081541375001010298483449 : memory 1, terminal-local 6
```

So the memory branch is not determined by the visible terminal phase, terminal
residue, alignment, and cofactor residue alone.  This is an important no-go for
an over-simple terminal-local proof.

## Positive Result: Child Residue Plus Timing Separates

Allowing child low bits changes the picture.  Among the tested power-of-two
child moduli, the first modulus that becomes pure when paired with the timing
features below is `4096`.  The smallest pure feature sets found have size `2`,
and all involve `child mod 4096` plus a terminal/event timing or phase feature.

One pure classifier is:

```text
child mod 4096, event_step
```

Memory buckets:

```text
1471|38 : memory 1
1895|38 : memory 2
2495|38 : memory 1
3791|38 : memory 1
 751|38 : memory 1
```

No terminal-local record occupies any of those same buckets.

Equivalent pure classifiers include:

```text
child mod 4096, terminal_step
child mod 4096, terminal_current_gap
child mod 4096, terminal_current_form
```

By contrast, `child mod 4096` alone is not enough:

```text
1471 : memory 1, terminal-local 1
1895 : memory 2, terminal-local 2
2495 : memory 1, terminal-local 3
3791 : memory 1, terminal-local 2
 751 : memory 1, terminal-local 5
```

So the finite separator is not just a residue table; it is a residue-plus-timing
statement.

The JSON includes direct checks for the smaller child moduli crossed with each
of `event_step`, `terminal_step`, `terminal_current_gap`, and
`terminal_current_form`.  All four timing features give the same purity
profile:

```text
child modulus   memory records in pure buckets   mixed buckets   pure?
64                                      0               4        no
128                                     0               4        no
256                                     2               3        no
512                                     2               3        no
1024                                    3               2        no
2048                                    3               2        no
4096                                    6               0        yes
```

## Theorem Signal

The refined local proof target is now:

```text
Terminal/event phase alone cannot classify the memory branch.

The memory branch is controlled by child low bits plus timing:
  child mod 4096 in {751, 1471, 1895, 2495, 3791}
  and terminal/event timing at step 35/38.
```

This points back to the lift lemma: the lag-8 memory tail is a child-residue
phenomenon, not merely a terminal cofactor/phase phenomenon.

This remains finite evidence. The next proof obligation is to derive the five
`child mod 4096` timing buckets from the upper-child frontier hypotheses and
show that all other post-ladder terminal-`6 mod 16` tail cases stay
terminal-local.  The first refinement of that obligation is isolated in
[`BRANCH-PREFIX-TAIL-CHILD-LIFT-STRATIFIER.md`](BRANCH-PREFIX-TAIL-CHILD-LIFT-STRATIFIER.md):
the `2048` failure is exactly two mixed lower buckets, both split purely by the
next child bit at modulus `4096`.
