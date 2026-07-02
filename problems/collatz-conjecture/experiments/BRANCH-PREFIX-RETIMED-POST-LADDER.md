# Branch-Prefix Retimed Post-Ladder Tail

This note isolates the post-ladder subset of the first-threshold timing sweep.
It asks what the `lag_minus_align = 3` tail actually is arithmetically.

This is finite theorem-discovery data only. It does not prove Collatz.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_post_ladder_tail.py
```

Combined result:

```text
experiments/results/branch_prefix_retimed_post_ladder_tail_sweep_d18_d25_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_retimed_post_ladder_tail.py --min-parent-depth 18 --max-parent-depth 25 --use-cache --write-depth-cache --output experiments/results/branch_prefix_retimed_post_ladder_tail_sweep_d18_d25_20260702.json
```

The script reuses the retimed-pressure condition:

```text
required_delta > 0
credit_delta < required_delta
```

Then it keeps only first above-parent thresholds whose signature classifier
places them in the high-ladder post-window class:

```text
high_after_ladder_window
```

## Algebra Checked

For the last high-ladder credit event, write the ladder entry as:

```text
x = 2^a q - 1,  a >= 3.
```

The high-ladder identity gives the terminal after `a` odd shortcut steps:

```text
y = 3^a q - 1.
```

The post-ladder analyzer then checks the next three shortcut steps. Across the
checked first-threshold post-ladder class, every terminal satisfies:

```text
y == 6 mod 16
v2(y) = 1
post-ladder shortcut word = EOO
```

With the shortcut convention:

```text
E(n) = n/2
O(n) = (3n + 1)/2
```

the three-step tail is therefore the exact map:

```text
EOO(y) = (9y + 10) / 8.
```

Thus the observed `+3` timing bin is not an arbitrary tail in this window. It
is the specific residue and parity event:

```text
y == 6 mod 16  ->  EOO  ->  (9y + 10)/8.
```

Equivalently, since `y + 1 = 3^a q`, the checked terminal residue is the phase
law:

```text
3^a q == 7 mod 16.
```

The exact phase table is:

| `a mod 4` | Required `q mod 16` | Count |
|---:|---:|---:|
| `0` | `7` | `168` |
| `1` | `13` | `96` |
| `2` | `15` | `73` |
| `3` | `5` | `235` |

The residue does not sharpen to a single terminal class modulo `64` in this
window:

```text
y mod 64:
  6:  205
  22: 147
  38: 195
  54: 25
```

## Low-Residue Classifier Test

The refreshed analyzer also tests a tempting shortcut:

```text
Can the post-ladder first-threshold class be recognized by a fixed low
parent/child residue table among all retimed first-threshold transitions?
```

For the checked lifts, parent depths are at least `18`, so parent and upper
child have the same residue modulo every tested modulus through `65536`.
Consequently the parent and child low-residue purity tables are identical.

Result across all `13,856` retimed first-threshold transitions:

| Modulus | Post-Ladder in Pure Buckets | Post-Ladder Total | Pure Fraction | Pure Buckets | Mixed Buckets |
|---:|---:|---:|---:|---:|---:|
| `16` | `0` | `572` | `0.0` | `0` | `3` |
| `32` | `0` | `572` | `0.0` | `0` | `4` |
| `64` | `0` | `572` | `0.0` | `0` | `8` |
| `128` | `0` | `572` | `0.0` | `0` | `13` |
| `256` | `0` | `572` | `0.0` | `0` | `19` |
| `512` | `0` | `572` | `0.0` | `0` | `38` |
| `1024` | `0` | `572` | `0.0` | `0` | `63` |
| `4096` | `0` | `572` | `0.0` | `0` | `180` |
| `65536` | `7` | `572` | `0.012237762` | `7` | `478` |

At modulus `65536`, the only pure buckets are seven singleton buckets:

```text
8859, 11455, 11983, 30055, 30567, 47515, 64763.
```

So the post-ladder class is not explained by a fixed low-residue table through
sixteen bits. The `3^a q == 7 mod 16` law is a dynamic phase condition after
the high-ladder event has been exposed, not a standalone child-residue
classifier.

## Combined Result

Across exact lifts `18 -> 19` through `25 -> 26`:

```text
retimed-pressure transitions:          13,856
first thresholds found:                13,856
post-ladder first thresholds:             572

post-ladder word counts:
  EOO:                                    572

terminal v2 counts:
  1:                                      572

terminal mod 16 counts:
  6:                                      572

q mod 8 counts:
  5:                                      331
  7:                                      241

q-align phase counts:
  a0:q7                                   168
  a1:q13                                   96
  a2:q15                                   73
  a3:q5                                   235
```

All derived checks are true in the combined file:

```text
all ladder formulas checked:             true
all post3 states match threshold state:  true
all post-ladder tails have lag-align 3:  true
all post-ladder words are EOO:           true
all ladder terminals are 6 mod 16:       true
all ladder terminals have v2 1:          true
all q are 5 or 7 mod 8:                  true
all q-align phases force terminal 6:     true
```

## Depth Table

| Lift | Retimed | First Thresholds | Post-Ladder First Thresholds | Word | Terminal `mod 16` | Terminal `v2` | Offset Min | Offset Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `18 -> 19` | `166` | `166` | `20` | `EOO` | `6` | `1` | `1` | `1` |
| `19 -> 20` | `135` | `135` | `4` | `EOO` | `6` | `1` | `11` | `11` |
| `20 -> 21` | `253` | `253` | `6` | `EOO` | `6` | `1` | `10` | `18` |
| `21 -> 22` | `719` | `719` | `7` | `EOO` | `6` | `1` | `9` | `17` |
| `22 -> 23` | `869` | `869` | `33` | `EOO` | `6` | `1` | `8` | `46` |
| `23 -> 24` | `1,749` | `1,749` | `50` | `EOO` | `6` | `1` | `7` | `26` |
| `24 -> 25` | `4,288` | `4,288` | `132` | `EOO` | `6` | `1` | `6` | `33` |
| `25 -> 26` | `5,677` | `5,677` | `320` | `EOO` | `6` | `1` | `5` | `32` |

## Lemma Target

The finite data suggests the following sublemma for the retimed-pressure proof
target:

```text
If the first above-parent threshold is in the high-ladder post-window class,
then the preceding high ladder terminates at y = 3^a q - 1 with y == 6 mod 16.
The threshold state is exactly EOO(y) = (9y + 10)/8, three shortcut steps after
the ladder terminal.
```

The missing proof obligation is to derive `y == 6 mod 16` from the live
upper-lift condition, the parent-child frontier algebra, and the exact
high-ladder identity. In phase form, this means proving:

```text
q == 7 * (3^a)^(-1) mod 16.
```

The finite sweep identifies that algebraic target and also warns against
over-sharpening it to a fixed `mod 64` terminal residue.

## All Pressure Units Extension

The first-threshold result is not the full post-ladder population. The
signature sweep counts all above-parent pressure units, including later units
inside the same retimed transition. The companion analyzer:

```text
experiments/branch_prefix_retimed_post_ladder_all_units.py
```

with result:

```text
experiments/results/branch_prefix_retimed_post_ladder_all_units_sweep_d18_d25_20260702.json
```

was run with:

```powershell
python experiments/branch_prefix_retimed_post_ladder_all_units.py --min-parent-depth 18 --max-parent-depth 25 --refresh --write-depth-cache --output experiments/results/branch_prefix_retimed_post_ladder_all_units_sweep_d18_d25_20260702.json
```

Across the same exact lifts:

```text
retimed-pressure transitions:          13,856
above-parent pressure units:           16,085
post-ladder pressure units:               646

pressure regimes:
  high_inside_active_ladder:            15,259
  high_after_ladder_window:                646
  low_repeat_prepaid:                      180
```

All `646` post-ladder pressure units satisfy the same algebraic law:

```text
post-ladder word counts:
  EOO:                                    646

terminal mod 16 counts:
  6:                                      646

q-align phase counts:
  a0:q7                                   189
  a1:q13                                  115
  a2:q15                                   86
  a3:q5                                   256
```

The event-index split explains the difference from the `572` first thresholds:

```text
post-ladder pressure unit index within its retimed transition:
  1:                                      572
  2:                                       63
  3:                                       10
  4:                                        1
```

The index is not just an ordering label. In every checked post-ladder pressure
unit, it equals the required-credit level above the parent:

```text
event_index 1 -> required_above_parent 1: 572
event_index 2 -> required_above_parent 2:  63
event_index 3 -> required_above_parent 3:  10
event_index 4 -> required_above_parent 4:   1
```

Most later-index units are not repeated post-ladder cascades in the same
transition. Counting post-ladder units per retimed transition gives:

```text
transitions with one post-ladder pressure unit: 644
transitions with two post-ladder pressure units: 1
```

So an event-index `2`, `3`, or `4` post-ladder unit usually means earlier
above-parent pressure units occurred in another regime before the first
post-ladder appearance. The post-ladder state itself still obeys the same
`EOO` phase law.

So the `EOO` / `3^a q == 7 mod 16` law is not merely a first-threshold
artifact; it persists for every checked post-ladder pressure unit.

The pressure-state residue purity test is more mixed than the parent/child
residue test:

| Modulus | Post-Ladder in Pure Buckets | Post-Ladder Total | Pure Fraction | Pure Buckets | Mixed Buckets |
|---:|---:|---:|---:|---:|---:|
| `16` | `0` | `646` | `0.0` | `0` | `7` |
| `32` | `0` | `646` | `0.0` | `0` | `14` |
| `64` | `0` | `646` | `0.0` | `0` | `28` |
| `128` | `0` | `646` | `0.0` | `0` | `55` |
| `256` | `0` | `646` | `0.0` | `0` | `105` |
| `512` | `0` | `646` | `0.0` | `0` | `183` |
| `1024` | `0` | `646` | `0.0` | `0` | `290` |
| `4096` | `15` | `646` | `0.023219814` | `15` | `486` |
| `65536` | `442` | `646` | `0.684210526` | `432` | `190` |

This gives a nuanced target. The all-unit post-ladder law is stable, but a
low pressure-state residue table only becomes partially informative at high
modulus and still misses `204/646` cases at sixteen bits. The clean theorem
object remains the dynamic high-ladder phase law, not a finite residue lookup.
