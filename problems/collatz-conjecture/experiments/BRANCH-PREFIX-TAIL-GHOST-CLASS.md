# Branch-Prefix Tail Ghost Class

This note audits the single ghost full-lift class exposed by
[`BRANCH-PREFIX-TAIL-MEMORY-LIFT-SOLVER.md`](BRANCH-PREFIX-TAIL-MEMORY-LIFT-SOLVER.md).
It does not solve Collatz. It answers a local question:

```text
Does the unobserved EEOEOOOO terminal-6 lift become a real memory-tail source,
or is it absorbed by terminal-local phase accounting?
```

## Instrument

Script:

```text
experiments/branch_prefix_tail_ghost_class.py
```

Result:

```text
experiments/results/branch_prefix_tail_ghost_class_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_ghost_class.py --parent-depth 25 --max-depth 1024 --top-n 12 --hist-top-n 40 --output experiments/results/branch_prefix_tail_ghost_class_d25_d26_20260702.json --quiet
```

The script recomputes the exact `25 -> 26` retimed hard class, filters to the
`340` post-ladder terminal-`6 mod 16` tail units, and records where the phase
maximum at the ladder terminal is sourced.

## Ghost Definitions

The lift solver found this local ghost full-lift:

```text
word:          EEOEOOOO
source:        n == 1956 mod 16384
bridge:        36 -> 18 -> 41 -> 30 -> 47 -> 39 -> 59 -> 25 -> 6
terminal:      6 mod 64
observed as memory record: 0
```

At the ladder terminal, this corresponds to the terminal signature:

```text
align a = 4
q == 23 mod 64
terminal == 6 mod 64
```

The audit distinguishes this terminal signature from the stronger memory-source
signature:

```text
source_lag_to_terminal = 8
source_to_terminal_word = EEOEOOOO
source == 1956 mod 16384
```

## Result

Exact counts:

```text
post-ladder tail units:       340
terminal ghost signature:      25
ghost memory sources:           0
```

Pure finite claims:

```text
all sources found:                         true
terminal signature occurs:                 true
ghost memory source absent:                true
all nonterminal sources have lag 8:        true
all nonterminal sources are memory words:  true
all post-ladder tail words are EOO:        true
```

The source-lag split is:

```text
source lag 0: 334
source lag 8:   6
```

The six nonterminal sources are exactly the already-known memory words:

```text
EEOOEOOO: 5
EEOEOOOO: 1
```

Their lifted classes are:

```text
EEOOEOOO  mod 8192:  6508  count 5
EEOEOOOO  mod 8192:  1956  count 1

EEOOEOOO  mod 16384:  6508   count 3
EEOOEOOO  mod 16384:  14700  count 2
EEOEOOOO  mod 16384:  10148  count 1
```

The ghost source class:

```text
EEOEOOOO mod 16384 = 1956
```

has count `0` as a nonterminal memory source.

## What Happens To The Ghost Signature?

The terminal signature itself is real:

```text
a = 4, q == 23 mod 64, terminal == 6 mod 64: 25 cases
```

But every one of those `25` cases has:

```text
source_lag_to_terminal = 0
source_word = none
terminal_current_gap = terminal max gap
```

So in this exact lift the ghost terminal bit is not an extra memory exception.
It is handled by the terminal-local side of the phase separator.

The terminal-local gaps across all `334` terminal-local post-ladder tail units
are:

```text
0.021768664287042106578247   count   5
0.034103346429350801687232   count 269
0.069206692858701603374464   count   3
0.081541375001010298483449   count  57
```

The `25` ghost-signature terminal-local cases are contained in these positive
terminal-local gaps.

## Theorem Signal

The memory-tail proof target can now avoid a false fork:

```text
1. Nonterminal memory branch:
   source lag = 8, exactly the two memory words, with observed full lifts
   6508, 14700, and 10148 modulo 16384.

2. Terminal-local branch:
   includes the unobserved EEOEOOOO terminal-6 lift signature
   (a = 4, q = 23 mod 64), but with source lag = 0.
```

Thus the ghost does not need to be excluded merely because it is terminal-`6`.
The real local lemma should prove a dichotomy:

```text
Either the tail max is terminal-local, in which case the positive terminal
gap handles the event directly, or the tail max is eight steps earlier, in
which case the source word is one of the two memory words and the ghost
full-lift 1956 mod 16384 does not occur.
```

This remains finite evidence from the exact `25 -> 26` lift. The useful gain
is that the ghost class has been downgraded from a possible extra memory case
to a terminal-local phase case in the observed hard lift.
