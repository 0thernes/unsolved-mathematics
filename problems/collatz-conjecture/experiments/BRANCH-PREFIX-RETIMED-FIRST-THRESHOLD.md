# Branch-Prefix Retimed First Threshold

This note focuses only on the first above-parent pressure threshold inside
retimed-pressure transitions.

Previous notes showed that the retimed class is prepaid and split into three
dynamic regimes. This instrument asks a sharper timing question:

```text
When does the first one-unit above-parent threshold occur relative to the
parent frontier depth and the last visible credit event?
```

This is finite evidence only. It does not prove Collatz.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_first_threshold.py
```

Combined result:

```text
experiments/results/branch_prefix_retimed_first_threshold_sweep_d18_d25_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_retimed_first_threshold.py --min-parent-depth 18 --max-parent-depth 25 --use-cache --write-depth-cache --output experiments/results/branch_prefix_retimed_first_threshold_sweep_d18_d25_20260702.json
```

The sweep recomputes exact lifts `18 -> 19` through `25 -> 26`, selects
retimed transitions:

```text
required_delta > 0
credit_delta < required_delta
```

and records only the first pressure event with:

```text
child required credit > parent max required credit.
```

## Stable First-Threshold Checks

Across the checked exact lifts:

```text
retimed-pressure transitions:     13,856
first thresholds found:           13,856
```

All first-threshold checks held:

```text
all first thresholds present:          true
all first thresholds upper child:      true
all first thresholds one-unit:         true
all first thresholds have prior credit:true
all first thresholds positive surplus: true
```

Aggregate first-threshold regimes:

```text
high_inside_active_ladder: 13,120
high_after_ladder_window:     572
low_repeat_prepaid:           164
```

The `572` post-ladder first thresholds were isolated in
[`BRANCH-PREFIX-RETIMED-POST-LADDER.md`](BRANCH-PREFIX-RETIMED-POST-LADDER.md).
In every checked post-ladder case, the preceding high ladder terminates at
`y == 6 mod 16`, the next shortcut word is `EOO`, and the threshold state is:

```text
EOO(y) = (9y + 10) / 8.
```

In phase form, with `y = 3^a q - 1`, the same result is:

```text
3^a q == 7 mod 16.
```

Aggregate first-threshold events:

```text
high_ladder_step:          13,120
ordinary_step:                736
```

Aggregate last-credit kinds:

```text
high_ladder:               13,692
low_repeat:                   164
```

## Depth Table

| Lift | Retimed | Active Ladder | Post-Ladder `+3` | Low Repeat | Offset Min | Offset Max | Surplus Min | Lag-Align Min | Lag-Align Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `18 -> 19` | `166` | `144` | `20` | `2` | `1` | `37` | `1` | `-5` | `3` |
| `19 -> 20` | `135` | `131` | `4` | `0` | `3` | `22` | `3` | `-4` | `3` |
| `20 -> 21` | `253` | `247` | `6` | `0` | `2` | `32` | `2` | `-5` | `3` |
| `21 -> 22` | `719` | `710` | `7` | `2` | `1` | `45` | `1` | `-7` | `3` |
| `22 -> 23` | `869` | `824` | `33` | `12` | `3` | `57` | `3` | `-9` | `3` |
| `23 -> 24` | `1,749` | `1,684` | `50` | `15` | `2` | `99` | `2` | `-8` | `3` |
| `24 -> 25` | `4,288` | `4,135` | `132` | `21` | `1` | `63` | `2` | `-14` | `3` |
| `25 -> 26` | `5,677` | `5,245` | `320` | `112` | `3` | `62` | `2` | `-10` | `3` |

Here:

```text
offset = first_threshold_step - parent_depth
lag_minus_align = (first_threshold_step - last_credit_step) - last_credit_alignment
```

## Corrected Timing Signal

The first threshold is not confined to a tiny constant post-depth window. The
checked offsets range from:

```text
global offset min:  1
global offset max: 99
```

So the next proof should not try to prove:

```text
first threshold appears within O(1) shortcut steps of the frontier depth.
```

The stable finite fact is different:

```text
The first above-parent threshold may occur much later, but when it appears it
is still one-unit, upper-child, positive-surplus, and already prepaid by a
visible high-ladder or low-repeat event.
```

The high-ladder relative timing is still rigid at the top end:

```text
global lag_minus_align min: -14
global lag_minus_align max:   3
```

Every post-ladder first threshold sits in the `lag_minus_align = 3` class.

## Refined Lemma Target

The first-threshold lemma suggested by the data is:

```text
For every live retimed-pressure upper child, the first prefix whose required
credit exceeds the parent maximum is exactly one required-credit unit above
parent. It has positive surplus because the child has already entered one of:

1. an active high ladder;
2. the three-step `EOO` post-ladder tail after a high ladder terminal
   `y == 6 mod 16`; or
3. a low-repeat gate.
```

The proof obligation is to derive this from the one-bit lift algebra plus the
exact high-ladder and low-repeat identities. The observed timing offset is
not itself the invariant; visible prepayment is.
