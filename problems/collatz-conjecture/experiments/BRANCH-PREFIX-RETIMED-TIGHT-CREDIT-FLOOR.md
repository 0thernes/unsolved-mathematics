# Branch-Prefix Retimed Tight Credit Floor

Date: 2026-07-02

This note analyzes why the align-3 `OOO` / `OOOEOO` local grammar is necessary
but not sufficient for surplus-`1` first thresholds. It separates the final
local credit from the credit already inherited before the align-3 entry.

This is finite theorem-discovery evidence plus one accounting identity. It is
not a proof of the Collatz conjecture.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_tight_credit_floor.py
```

Command:

```powershell
python experiments/branch_prefix_retimed_tight_credit_floor.py --min-parent-depth 18 --max-parent-depth 25 --top-n 20 --output experiments/results/branch_prefix_retimed_tight_credit_floor_d18_d25_20260702.json
```

Output:

```text
experiments/results/branch_prefix_retimed_tight_credit_floor_d18_d25_20260702.json
```

## Accounting identity

For a first above-parent threshold, write:

```text
required_above_parent = required_at_pressure - parent_required
credit_before_last    = credit immediately before the last credit event
last_credit_amount    = amount contributed by the last credit event
```

Then:

```text
pressure_surplus
  = credit_at_pressure - required_at_pressure
  = (credit_before_last - parent_required)
    + (last_credit_amount - required_above_parent).
```

For every checked align-3 local-grammar record:

```text
last_credit_amount = 1
required_above_parent = 1
```

Therefore the local term cancels:

```text
pressure_surplus = credit_before_last - parent_required.
```

Call the right-hand side the inherited reserve before the final align-3 entry.

## Global result

Across exact lifts `18 -> 19` through `25 -> 26`:

```text
retimed transitions:          13,856
first thresholds present:     13,856
local grammar records:           511
minimal inherited reserve:         5
credit-3 records:                  5
```

All direct checks passed:

```text
all local surplus identities hold:              true
all local credit amounts match new layer:        true
minimal inherited reserve is surplus one:        true
credit three implies minimal inherited reserve:  true
minimal reserve count equals credit-three count: true
```

The inherited reserve histogram is exactly the same as the local-grammar
surplus histogram:

```text
1:   5
2:  25
3:  89
4: 119
5:  98
6: 112
7:  32
8:  27
9:   3
10:  1
```

This explains the previous selector result: the final align-3 step does not
create the tightness gap. It cancels one unit of new demand with one unit of
new credit. Tightness is inherited from the reserve already present before the
entry.

## Depth split

Local grammar appears only at checked parent depths `18`, `21`, and `24`:

```text
d = 18: local  30, minimal reserve 3
d = 21: local 108, minimal reserve 2
d = 24: local 373, minimal reserve 0
```

The other checked depths have no local-grammar records in this window.

## What changed

The previous target was:

```text
Prove surplus-1 forces align-3 OOO/OOOEOO local grammar.
```

That is still true in the checked window, but it is not sharp enough. The
local grammar has `506` near-misses. This note shows why:

```text
near-miss = same local grammar + inherited reserve >= 2.
```

The five tight records are exactly:

```text
same local grammar + inherited reserve = 1.
```

Equivalently, in this checked window:

```text
surplus 1
  <=> inherited reserve before align-3 entry is 1
  <=> credit-3 local grammar.
```

The equivalence is finite evidence, while the surplus decomposition is an
accounting identity from the definitions.

## Refined theorem target

The proof target is now pre-entry rather than post-entry:

```text
For every live upper-lift retimed first threshold in the align-3 local
grammar, prove that inherited reserve before the align-3 entry is at least 1.
Then classify the equality case inherited reserve = 1.
```

This is narrower than the previous local-word target and explains why the
near-misses are harmless: they already carry surplus reserve before the final
align-3 credit event.
