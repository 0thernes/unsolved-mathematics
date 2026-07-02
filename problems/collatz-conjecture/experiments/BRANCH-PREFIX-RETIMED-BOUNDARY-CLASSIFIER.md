# Branch-Prefix Retimed Boundary Classifier

Date: 2026-07-02

This note classifies the depth-`d` boundary parity type for every first
above-parent threshold in the exact retimed hard class, across frontier lifts
`18 -> 19` through `25 -> 26`. It is finite theorem-discovery evidence, not a
proof of the Collatz conjecture.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_boundary_classifier.py
```

Command:

```powershell
python experiments/branch_prefix_retimed_boundary_classifier.py --min-parent-depth 18 --max-parent-depth 25 --top-n 16 --output experiments/results/branch_prefix_retimed_boundary_classifier_d18_d25_20260702.json
```

Output:

```text
experiments/results/branch_prefix_retimed_boundary_classifier_d18_d25_20260702.json
```

The script re-enumerates exact retimed transitions, extracts the first
above-parent pressure threshold, and records:

```text
boundary type at depth d: E->O or O->E
threshold offset from depth d
threshold surplus
last visible credit event
local word from last credit to pressure
```

## Global checks

Across the checked exact window:

```text
retimed transitions:       13,856
first thresholds present:  13,856
```

All direct checks passed:

```text
all affine lift laws hold to depth:        true
all parities are shared before depth d:    true
all boundary pairs are opposite:           true
all surplus-1 cases are E->O:              true
all surplus-1 cases have offset 1:         true
all surplus-1 cases have align 3:          true
all surplus-1 cases have known local word: true
```

The affine-law checks are expected from
[`BRANCH-PREFIX-AFFINE-LIFT-LEMMA.md`](BRANCH-PREFIX-AFFINE-LIFT-LEMMA.md);
they are kept here as runtime guardrails against implementation mistakes.

## Boundary counts

Both boundary types occur:

```text
E->O: 11,447
O->E:  2,409
```

So the retimed class is not globally `E->O`. The sharper observation is about
the tight lower edge:

```text
E->O min offset:  1
E->O min surplus: 1

O->E min offset:  5
O->E min surplus: 2
```

In the checked window, `O->E` is delayed and never reaches the surplus-`1`
base case.

By regime:

```text
high_inside_active_ladder, E->O: 10,793
high_inside_active_ladder, O->E:  2,327
high_after_ladder_window,  E->O:    507
high_after_ladder_window,  O->E:     65
low_repeat_prepaid,        E->O:    147
low_repeat_prepaid,        O->E:     17
```

## Tight surplus-one slice

The only surplus-`1` first thresholds are the same five tight cases found by
the layer-margin and tight-layer extractors:

```text
surplus 1, E->O: 5
surplus 1, O->E: 0
```

All five have:

```text
offset from depth d: 1
last credit kind:    high_ladder
last credit align:   3
local word:          OOO or OOOEOO
```

The local word split is:

```text
OOO:    3
OOOEOO: 2
```

Thus the current finite implication is:

```text
surplus 1 first threshold
  => E->O boundary
  => pressure at d+1
  => align-3 high-ladder credit
  => local word in {OOO, OOOEOO}.
```

This is still an observed implication over `18..25`, not a theorem.

## What this rules out

The classifier rules out two tempting but false simplifications:

```text
False target 1: every retimed transition has E->O boundary.
False target 2: every E->O boundary is tight.
```

`O->E` appears in `2,409` checked retimed transitions, and offset-`1` `E->O`
thresholds occur with many surplus values:

```text
offset 1 surplus 1:   5
offset 1 surplus 2:  30
offset 1 surplus 3: 128
offset 1 surplus 4: 260
offset 1 surplus 5: 387
offset 1 surplus 6: 575
offset 1 surplus 7: 413
offset 1 surplus 8: 345
```

So the proof target cannot be just "boundary is `E->O`" or just "offset is
`1`." The tight base case is the intersection of low surplus, depth-boundary
pressure, and align-3 local credit.

## Refined theorem target

The affine lift lemma already proves the shared-prefix law and the boundary
parity flip. The remaining retimed-specific statement has now sharpened to:

```text
For a live upper-lift retimed transition, if the first above-parent pressure
threshold has surplus 1, then the depth-d boundary type is E->O, the pressure
occurs at d+1, and the last credit event is an align-3 high ladder whose local
word to pressure is OOO or OOOEOO.
```

The next proof work should explain why `O->E` boundaries have observed reserve
and delay, and why surplus `1` forces exactly the align-3 local grammar.
