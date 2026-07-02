# Branch-Prefix Retimed Layer Margin

This note measures the credit surplus at each pressure layer in the retimed
hard case.

This is finite theorem-discovery data only. It does not prove Collatz.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_layer_margin.py
```

Combined result:

```text
experiments/results/branch_prefix_retimed_layer_margin_sweep_d18_d25_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_retimed_layer_margin.py --min-parent-depth 18 --max-parent-depth 25 --write-depth-cache --output experiments/results/branch_prefix_retimed_layer_margin_sweep_d18_d25_20260702.json
```

Unlike the three-regime ledger, this script re-enumerates the exact frontier
lifts and records every above-parent pressure unit directly. For each unit it
stores:

```text
event index
required level above parent
dynamic regime
credit
required credit
surplus = credit - required
last visible credit event
```

## Combined Result

Across exact lifts `18 -> 19` through `25 -> 26`:

```text
retimed-pressure transitions:          13,856
above-parent pressure units:           16,085
first-layer units:                     13,856
```

The same coverage and layer laws are rechecked:

```text
regime counts:
  high_inside_active_ladder:            15,259
  high_after_ladder_window:                646
  low_repeat_prepaid:                      180

layer counts:
  1:                                    13,856
  2:                                     1,913
  3:                                       263
  4:                                        46
  5:                                         7

event_index -> required_above_parent:
  1 -> 1:                               13,856
  2 -> 2:                                1,913
  3 -> 3:                                  263
  4 -> 4:                                   46
  5 -> 5:                                    7
```

All margin checks pass:

```text
all pressure units have positive surplus:       true
all pressure units have prior credit:           true
all event indexes equal required level:         true
all retimed transitions have layer one:         true
```

## Minimum Surplus

The global minimum surplus is `1`, but it occurs only in the first layer:

```text
minimum surplus by layer:
  layer 1:  1
  layer 2:  4
  layer 3:  6
  layer 4:  7
  layer 5: 11
```

By regime:

```text
minimum surplus by regime:
  active high-ladder: 1
  post-ladder EOO:   1
  low-repeat:        3
```

By regime and layer:

```text
active high-ladder:
  layer 1:  1
  layer 2:  4
  layer 3:  6
  layer 4:  7
  layer 5: 11

post-ladder EOO:
  layer 1:  1
  layer 2:  5
  layer 3:  7
  layer 4: 13

low-repeat:
  layer 1:  3
  layer 2:  6
  layer 3: 10
```

The first layer is therefore the tight layer. Higher layers carry a visible
positive buffer in the checked window.

## Surplus Histogram

The low end of the combined surplus histogram:

```text
surplus 1:     5
surplus 2:    38
surplus 3:   209
surplus 4:   647
surplus 5: 1,313
surplus 6: 2,272
surplus 7: 2,537
surplus 8: 2,586
surplus 9: 2,125
surplus 10: 1,550
surplus 11: 1,015
surplus 12:   638
```

Distribution of pressure units per retimed transition:

```text
1 unit:  11,943 transitions
2 units:  1,650 transitions
3 units:    217 transitions
4 units:     39 transitions
5 units:      7 transitions
```

## Depth Table

| Lift | Retimed | Pressure Units | Min Layer 1 | Min Layer 2 | Min Layer 3 | Min Layer 4 | Min Layer 5 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `18 -> 19` | `166` | `178` | `1` | `5` | `13` | `-` | `-` |
| `19 -> 20` | `135` | `147` | `3` | `8` | `12` | `-` | `-` |
| `20 -> 21` | `253` | `288` | `2` | `5` | `14` | `-` | `-` |
| `21 -> 22` | `719` | `801` | `1` | `5` | `7` | `13` | `-` |
| `22 -> 23` | `869` | `1,019` | `3` | `5` | `8` | `12` | `-` |
| `23 -> 24` | `1,749` | `2,047` | `2` | `4` | `6` | `10` | `-` |
| `24 -> 25` | `4,288` | `4,953` | `2` | `4` | `7` | `7` | `19` |
| `25 -> 26` | `5,677` | `6,652` | `2` | `4` | `8` | `11` | `11` |

## Theorem Target

The three-regime ledger gave the layer law:

```text
event_index = required_above_parent.
```

This margin sweep adds the proof-facing inequality:

```text
credit - required >= 1
```

at every checked pressure unit, with higher layers having observed minimum
buffer:

```text
layer 2: >= 4
layer 3: >= 6
layer 4: >= 7
layer 5: >= 11
```

The resulting induction target is:

```text
For every live upper-lift retimed transition, the m-th above-parent pressure
unit is preceded by a visible dynamic event in one of the three regimes, and
the credit surplus after that event remains positive.
```

The tight part is layer `1`: the checked data has only five surplus-`1`
events, all in layer `1`. A proof should therefore first explain the first
layer, then use the larger observed higher-layer buffer as the induction
reserve.
