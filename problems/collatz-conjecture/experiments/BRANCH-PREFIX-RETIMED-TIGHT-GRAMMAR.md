# Branch-Prefix Retimed Tight Grammar

Date: 2026-07-02

This note tests whether the five surplus-`1` first-threshold records can be
recognized by local grammar features rather than by looking at the surplus
value directly. It is finite theorem-discovery evidence, not a proof of the
Collatz conjecture.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_tight_grammar.py
```

Command:

```powershell
python experiments/branch_prefix_retimed_tight_grammar.py --min-parent-depth 18 --max-parent-depth 25 --top-n 20 --output experiments/results/branch_prefix_retimed_tight_grammar_d18_d25_20260702.json
```

Output:

```text
experiments/results/branch_prefix_retimed_tight_grammar_d18_d25_20260702.json
```

The script re-enumerates the exact retimed first thresholds across lifts
`18 -> 19` through `25 -> 26`, enriches each first threshold with its local
word from last credit to pressure, entry offset, terminal formula, and
mod-`16` entry data, then tests selectors.

## Global result

Across the checked exact window:

```text
retimed transitions:      13,856
first thresholds present: 13,856
surplus-1 thresholds:          5
```

All surplus-`1` thresholds satisfy the surplus-free local grammar:

```text
upper child
boundary E->O
pressure at d+1
last credit is a high ladder
last credit align = 3
local word is OOO or OOOEOO
entry offset is -2 or -5
child entry is 7 mod 16
terminal formula from the entry matches
```

But this local grammar is not sufficient. It selects `511` records:

```text
local grammar selected: 511
surplus histogram:
  1:   5
  2:  25
  3:  89
  4: 119
  5:  98
  6: 112
  7:  32
  8:  27
  9:   3
 10:   1
```

So the pure local word target is too weak. The same `OOO` / `OOOEOO` shell has
many near-misses with additional credit reserve.

## Exact selector in the checked window

Adding the minimal observed credit condition `credit = 3` selects exactly the
five surplus-`1` cases:

```text
credit-3 local grammar selected: 5
surplus histogram:
  1: 5
```

The global checks say:

```text
tight local grammar selects all surplus-1:        true
tight local grammar has no non-surplus-1:         false
credit-3 local grammar selects all surplus-1:     true
credit-3 local grammar has no non-surplus-1:      true
base-required local grammar has no non-surplus-1: false
```

This matters because even adding `parent_required = 1` is still insufficient:

```text
base-required local grammar selected: 126
surplus histogram:
  1:  5
  2: 21
  3: 58
  4: 34
  5:  7
  6:  1
```

Thus the tight base case is not just "parent requirement one plus align-3
local grammar." It is the minimal-credit edge of that grammar.

## Filter chain

The full filter chain shows where the finite population collapses:

```text
upper_child:                    13,856
boundary_E_to_O:                11,447
pressure_at_d_plus_1:            2,504
last_credit_high_ladder:         2,502
align_3:                           513
known_tight_word:                  511
entry_offset_minus_2_or_minus_5:   511
child_entry_7_mod_16:              511
terminal_formula_matches:          511
credit_3:                            5
```

The local grammar only appears at checked parent depths:

```text
d = 18:  30 local-grammar records, 3 credit-3 records
d = 21: 108 local-grammar records, 2 credit-3 records
d = 24: 373 local-grammar records, 0 credit-3 records
```

No local-grammar records appeared at depths `19`, `20`, `22`, `23`, or `25` in
this window. This depth pattern is evidence, not a theorem.

## The five credit-3 local grammar records

The exact five selected records are the previously isolated surplus-`1` cases:

```text
word counts:
  OOO:    3
  OOOEOO: 2

tail after ladder:
  active terminal: 3
  EOO tail:        2

entry offset:
  -2: 3
  -5: 2

q mod 16:
  3: 2
  5: 2
  7: 1
```

The `OOO` cases are active terminal align-3 ladder states. The `OOOEOO` cases
are post-terminal `EOO` tails.

## What this rules out

The test rules out another tempting but false theorem target:

```text
False target: surplus-1 is characterized by the align-3 local word grammar
alone.
```

That grammar admits `506` non-tight near-misses. The near-misses are not
structural failures; they carry extra credit. The missing theorem is therefore
about minimal credit, not just local word shape.

## Refined theorem target

The current finite implication is:

```text
surplus 1
  => local align-3 grammar
  => credit = 3
```

The checked finite equivalence is:

```text
surplus 1  <=>  credit-3 local grammar
```

inside the exact window `18 -> 19` through `25 -> 26`.

The next proof target is to explain why all local-grammar near-misses have
credit at least `4`, and why credit `3` can occur only in the five observed
upper-lift boundary configurations. That is a narrower, more honest base-case
lemma than the previous "local word" formulation.
