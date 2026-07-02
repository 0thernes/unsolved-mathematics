# Branch-Prefix Retimed Tight Layer-One Base Cases

Date: 2026-07-02

This note isolates the only observed surplus-`1` pressure units in the exact
retimed hard case. It is finite theorem-discovery evidence, not a proof of the
Collatz conjecture.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_tight_layer_one.py
```

Command:

```powershell
python experiments/branch_prefix_retimed_tight_layer_one.py --min-parent-depth 18 --max-parent-depth 25 --output experiments/results/branch_prefix_retimed_tight_layer_one_d18_d25_20260702.json
```

Result:

```text
experiments/results/branch_prefix_retimed_tight_layer_one_d18_d25_20260702.json
```

The script re-enumerates the exact survivor-frontier lifts `18 -> 19` through
`25 -> 26`, filters above-parent pressure units by `surplus = credit -
required`, and records the dynamic formula around each tight unit.

## Result

The layer-margin ledger found exactly `5` surplus-`1` units. The direct
extractor confirms all five have the same coarse fingerprint:

```text
selected_count:                                      5
all selected are layer one:                          true
all selected are upper child:                        true
all selected have parent_required = 1:               true
all selected have required_delta = 1:                true
all selected have credit_delta = 0:                  true
all selected have required = 2:                      true
all selected have credit = 3:                        true
all selected have credit_above_parent = 2:           true
all selected have last high-ladder credit:           true
all selected have last_credit_align = 3:             true
all selected have step offset from parent depth = 1: true
```

Depth and regime counts:

```text
parent depth 18: 3
parent depth 21: 2

high_inside_active_ladder: 3
high_after_ladder_window:  2

high_ladder_step: 3
ordinary_step:    2
```

## The five cases

Let the last high-ladder credit entry be `x = 2^3 q - 1`. Let
`y = 3^3 q - 1 = 27q - 1` be the terminal align-3 ladder state.

| d | parent | child | regime | event | q | y | pressure state | post word |
|---|--------|-------|--------|-------|---|---|----------------|-----------|
| 18 | 1115 | 263259 | active ladder | high_ladder_step | 88951 | 2401676 | 2401676 | active |
| 18 | 65607 | 327751 | post ladder | ordinary_step | 98437 | 2657798 | 2990024 | EOO |
| 18 | 246363 | 508507 | post ladder | ordinary_step | 152725 | 4123574 | 4639022 | EOO |
| 21 | 1427291 | 3524443 | active ladder | high_ladder_step | 1339699 | 36171872 | 36171872 | active |
| 21 | 1637543 | 3734695 | active ladder | high_ladder_step | 1419619 | 38329712 | 38329712 | active |

The three active cases are terminal align-3 ladder states:

```text
pressure state = y = 27q - 1
lag_from_credit = 3
lag_minus_align = 0
```

The two post-ladder cases have the exact `EOO` tail:

```text
q == 5 mod 16
y = 27q - 1 == 6 mod 16
EOO(y) = (9y + 10) / 8
lag_from_credit = 6
lag_minus_align = 3
```

The extractor verified both formulas exactly:

```text
all active selected match terminal ladder formula: true
all post selected match EOO terminal 6 mod 16:      true
```

## Interpretation

The tight surplus-`1` cases are not distributed across all regimes. In the
checked window, low-repeat never reaches surplus `1`; its observed minimum is
`3`. The tight cases are entirely an align-3 high-ladder phenomenon, with two
forms:

```text
active terminal:
  x = 8q - 1
  pressure state = 27q - 1

post-terminal EOO:
  x = 8q - 1
  y = 27q - 1 == 6 mod 16
  pressure state = (9y + 10) / 8
```

This refines the local induction target. It is no longer enough to say
"pressure units are prepaid." The base case where the surplus buffer is only
one unit appears to require an align-3 high-ladder lemma:

```text
Tight layer-one target:
For a live upper-lift retimed transition whose first above-parent pressure
unit has only surplus 1, derive the align-3 high-ladder entry x = 8q - 1
from the lift algebra. Then show the pressure state is either the terminal
ladder state 27q - 1 or the EOO post-terminal state (9(27q - 1) + 10) / 8.
```

The result is useful because it names a small proof object instead of asking
for another broad finite table. It remains finite evidence over depths
`18..25`.

Follow-up:
[`BRANCH-PREFIX-RETIMED-TIGHT-LIFT-ALGEBRA.md`](BRANCH-PREFIX-RETIMED-TIGHT-LIFT-ALGEBRA.md)
checks that these five cases obey the parent/upper-child affine lift law up to
depth `d`, then isolates the common boundary mechanism: parent even, child odd
at depth `d`, with pressure at `d+1`.
