# Branch-Prefix Retimed Low-Repeat Units

This note isolates the low-repeat subset of the retimed pressure-unit sweep.
It asks what the `low_repeat_prepaid` timing bin is arithmetically.

This is finite theorem-discovery data only. It does not prove Collatz.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_low_repeat_units.py
```

Combined result:

```text
experiments/results/branch_prefix_retimed_low_repeat_units_sweep_d18_d25_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_retimed_low_repeat_units.py --min-parent-depth 18 --max-parent-depth 25 --write-depth-cache --output experiments/results/branch_prefix_retimed_low_repeat_units_sweep_d18_d25_20260702.json
```

The script reuses the retimed-pressure condition:

```text
required_delta > 0
credit_delta < required_delta
```

Then it keeps all above-parent pressure units whose most recent structural
credit event was the low-repeat gate:

```text
low_repeat_prepaid
```

## Algebra Checked

For an odd `x == 3 mod 8`, the three-step low macro is:

```text
OOE(x) = (9x + 5) / 8.
```

The low-repeat gate is the unique residue:

```text
x == -5 mod 64.
```

Writing `h = v2(x + 5)`, the repeat law is:

```text
v2(OOE(x) + 5) = h - 3.
```

The low-repeat analyzer checked every `low_repeat_prepaid` pressure unit and
found that all `180` units across exact lifts `18 -> 19` through `25 -> 26`
come from this exact gate:

```text
all entries are -5 mod 64 repeat gates:       true
all repeat laws checked:                      true
all lag simulations match pressure state:     true
```

The pressure state is reached by only two shortcut words:

```text
lag word OO:       58
lag word OOEOO:   122
```

Equivalently, if `M(x) = OOE(x) = (9x + 5)/8`, then the pressure state is one
of:

```text
OO(x)       = (9x + 5) / 4       = 2M(x)
OOEOO(x)   = (81x + 85) / 32     = OO(M(x)).
```

So the low-repeat class is not an arbitrary delayed-credit class. It is a
pressure event inside a repeat-gate macro window, either two shortcut steps
after the gate entry or two shortcut steps after one completed `OOE` repeat
macro.

## Combined Result

Across exact lifts `18 -> 19` through `25 -> 26`:

```text
retimed-pressure transitions:          13,856
above-parent pressure units:           16,085
low-repeat pressure units:                180

pressure regimes:
  high_inside_active_ladder:            15,259
  high_after_ladder_window:                646
  low_repeat_prepaid:                      180
```

The low-repeat pressure units split by event index:

```text
event index 1:                           164
event index 2:                            15
event index 3:                             1
```

As in the post-ladder class, the event index equals the required-credit level
above the parent in every checked low-repeat unit:

```text
event_index 1 -> required_above_parent 1: 164
event_index 2 -> required_above_parent 2:  15
event_index 3 -> required_above_parent 3:   1
```

The repeat-gate alignment distribution is:

```text
h = v2(x + 5):
   6: 125
   7:  43
   8:  10
   9:   1
  16:   1
```

The post-macro alignment is exactly `h - 3`:

```text
v2(M(x) + 5):
   3: 125
   4:  43
   5:  10
   6:   1
  13:   1
```

The low `mod 256` entry split stays inside `-5 mod 64`:

```text
59:   60
123:  43
187:  65
251:  12
```

## Depth Table

| Lift | Retimed | Pressure Units | Low-Repeat Units | Event Indexes | Lags | Alignments | Offset Min | Offset Max |
|---|---:|---:|---:|---|---|---|---:|---:|
| `18 -> 19` | `166` | `178` | `2` | `1:2` | `5:2` | `6:1, 7:1` | `1` | `1` |
| `19 -> 20` | `135` | `147` | `0` | `-` | `-` | `-` | `-` | `-` |
| `20 -> 21` | `253` | `288` | `1` | `2:1` | `5:1` | `7:1` | `10` | `10` |
| `21 -> 22` | `719` | `801` | `2` | `1:2` | `5:2` | `6:1, 7:1` | `9` | `28` |
| `22 -> 23` | `869` | `1,019` | `13` | `1:12, 2:1` | `2:8, 5:5` | `6:6, 7:5, 8:2` | `8` | `27` |
| `23 -> 24` | `1,749` | `2,047` | `18` | `1:15, 2:3` | `2:6, 5:12` | `6:9, 7:7, 8:2` | `7` | `34` |
| `24 -> 25` | `4,288` | `4,953` | `27` | `1:21, 2:6` | `2:21, 5:6` | `6:14, 7:7, 8:4, 9:1, 16:1` | `6` | `52` |
| `25 -> 26` | `5,677` | `6,652` | `117` | `1:112, 2:4, 3:1` | `2:23, 5:94` | `6:94, 7:21, 8:2` | `5` | `59` |

The global offset from parent depth ranges from `1` to `59`, so this is also
not a constant-window phenomenon.

## Pressure-State Residue Classifier Test

The analyzer also asks whether the low-repeat pressure state can be isolated
by a fixed low-residue table among all pressure units. The answer is still
mostly negative:

| Modulus | Low-Repeat in Pure Buckets | Low-Repeat Total | Pure Fraction | Pure Buckets | Mixed Buckets |
|---:|---:|---:|---:|---:|---:|
| `16` | `0` | `180` | `0.0` | `0` | `8` |
| `32` | `0` | `180` | `0.0` | `0` | `16` |
| `64` | `0` | `180` | `0.0` | `0` | `31` |
| `128` | `0` | `180` | `0.0` | `0` | `54` |
| `256` | `0` | `180` | `0.0` | `0` | `79` |
| `512` | `0` | `180` | `0.0` | `0` | `107` |
| `1024` | `1` | `180` | `0.005555556` | `1` | `125` |
| `4096` | `6` | `180` | `0.033333333` | `5` | `153` |
| `65536` | `118` | `180` | `0.655555556` | `115` | `61` |

As with the post-ladder class, a high-modulus pressure-state table becomes
partially informative but does not close the class. The clean object is the
dynamic low-repeat gate plus the exact two/five-step timing.

## Lemma Target

The finite data suggests the following local sublemma for the retimed-pressure
proof target:

```text
If an above-parent pressure unit is prepaid by a low-repeat event, then its
last credit event is an odd repeat gate x == -5 mod 64. The pressure state is
either OO(x) = (9x + 5)/4 or OOEOO(x) = (81x + 85)/32, and the event index
equals the required-credit level above the parent.
```

The missing proof obligation is to derive this two/five-step window from the
live upper-lift frontier algebra and the low-repeat `-5 mod 64` macro law,
then merge it with the active-ladder and post-ladder sublemmas. The finite
sweep identifies the right algebraic object and warns against replacing it
with a fixed low-bit lookup table.
