# Branch-Prefix Retimed Tight Reserve Source

Date: 2026-07-02

This note follows the inherited reserve identified in
`BRANCH-PREFIX-RETIMED-TIGHT-CREDIT-FLOOR.md` one step farther back.  The
credit-floor identity showed that, for the align-3 `OOO` / `OOOEOO` local
grammar, the final high-ladder credit cancels the new one-unit demand.  The
remaining question is where the pre-entry reserve came from.

This is finite theorem-discovery evidence plus bookkeeping identities.  It is
not a proof of the Collatz conjecture.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_tight_reserve_source.py
```

Command:

```powershell
python experiments/branch_prefix_retimed_tight_reserve_source.py --min-parent-depth 18 --max-parent-depth 25 --top-n 20 --quiet --output experiments/results/branch_prefix_retimed_tight_reserve_source_d18_d25_20260702.json
```

Output:

```text
experiments/results/branch_prefix_retimed_tight_reserve_source_d18_d25_20260702.json
```

## Global result

Across exact lifts `18 -> 19` through `25 -> 26`:

```text
retimed transitions:      13,856
first thresholds present: 13,856
local grammar records:       511
```

All direct trace checks passed:

```text
all first thresholds present:                 true
all trace first events match records:          true
all inherited-reserve identities hold:         true
all local records have prior credit:           true
all reserve-vs-current-required nonnegative:   true
```

The inherited reserve histogram is unchanged from the credit-floor note:

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

The new fact is that the final align-3 entry occurs before any additional
required layer appears:

```text
parent_required - entry_required_before_final_credit = 0
for all 511 checked local-grammar records.
```

Therefore:

```text
inherited_reserve_before_entry
  = credit_before_last - parent_required
  = credit_before_last - entry_required_before_final_credit.
```

So the inherited reserve is not a hidden artifact of comparing against an old
parent level.  In the checked window it is the actual reserve against the
current required layer immediately before the final align-3 credit event.

## Reserve source

Every checked local-grammar record has at least one prior credit event before
the final align-3 entry.  The immediately previous credit event already leaves
exactly the reserve later seen at entry:

```text
previous_reserve_vs_parent_after histogram
  = inherited_reserve histogram.
```

The source split for the immediately previous credit event is:

```text
previous high-ladder credit: 461
previous low-repeat credit:   50
```

Prior credit-event counts:

```text
1 prior event:   5
2 prior events: 129
3 prior events: 287
4 prior events:  85
5 prior events:   5
```

The final pre-entry reserve is therefore carried into the align-3 local
grammar by already-visible structural credit, not created by the last local
word.

## Tight equality cases

The five reserve-`1` cases are exactly the five surplus-`1` first thresholds.
All five have:

```text
prior credit events before final align-3 entry: 2
entry required layer:                           1
parent-required minus entry-required:           0
previous reserve after prior credit:            1
previous credit amount:                         1
```

Their previous credit sources split as:

```text
previous high-ladder align-3 credit: 4
previous low-repeat align-8 credit:  1
```

The final local words remain:

```text
OOO:    3
OOOEOO: 2
```

Thus the equality case has moved one step back:

```text
reserve 1
  <=> the immediately previous structural-credit event leaves reserve 1
      before the final align-3 entry.
```

This equivalence is finite evidence in the checked window, not a theorem.

## Depth split

Local grammar appears only at parent depths `18`, `21`, and `24` in this
window:

```text
d = 18: local  30, reserve-1 3, reserve range 1..8
d = 21: local 108, reserve-1 2, reserve range 1..8
d = 24: local 373, reserve-1 0, reserve range 2..10
```

Depth `24` is informative: the same local align-3 grammar appears many times,
but none are tight because all arrive with reserve at least `2`.

## Refined theorem target

The base-case target is now pre-local and credit-historical:

```text
For every live upper-lift retimed first threshold satisfying the align-3
OOO/OOOEOO local grammar:

1. Prove the final align-3 entry occurs while entry_required = parent_required.
2. Prove a prior structural-credit event leaves reserve at least 1 before
   that entry.
3. Classify equality reserve = 1 by the immediately previous reserve source.
```

This is sharper than the prior local-word target.  The local word explains the
final one-unit pressure step, while the equality/tightness question is carried
by the earlier reserve source.
