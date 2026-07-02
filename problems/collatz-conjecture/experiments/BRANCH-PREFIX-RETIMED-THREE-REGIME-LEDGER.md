# Branch-Prefix Retimed Three-Regime Ledger

This note combines the active high-ladder, post-ladder, and low-repeat
retimed pressure-unit certificates into one coverage ledger.

This is finite theorem-discovery data only. It does not prove Collatz.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_three_regime_ledger.py
```

Combined result:

```text
experiments/results/branch_prefix_retimed_three_regime_ledger_d18_d25_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_retimed_three_regime_ledger.py --output experiments/results/branch_prefix_retimed_three_regime_ledger_d18_d25_20260702.json
```

The ledger reads the three regime certificates plus the signature sweep:

```text
experiments/results/branch_prefix_retimed_active_ladder_units_sweep_d18_d25_20260702.json
experiments/results/branch_prefix_retimed_post_ladder_all_units_sweep_d18_d25_20260702.json
experiments/results/branch_prefix_retimed_low_repeat_units_sweep_d18_d25_20260702.json
experiments/results/branch_prefix_retimed_signature_sweep_d18_d25_20260702.json
```

It does not re-enumerate the frontier. Its job is to verify that the three
separate algebraic certificates have a consistent common boundary and to
extract the shared layer law.

## Coverage

Across exact lifts `18 -> 19` through `25 -> 26`:

```text
retimed-pressure transitions:          13,856
above-parent pressure units:           16,085
```

The three dynamic regimes cover every pressure unit:

```text
active high-ladder:                    15,259
post-ladder EOO:                          646
low-repeat OO/OOEOO:                      180
regime sum:                            16,085
```

The component algebra checks are all true:

```text
active high-ladder formula checks:      true
post-ladder EOO phase checks:           true
low-repeat repeat-gate checks:          true
signature dynamic checks:               true
```

The source totals also agree:

```text
retimed transition count in all sources: 13,856
pressure unit count in all sources:      16,085
```

## Layer Law

Every above-parent pressure unit has an event index inside its retimed
transition. The combined ledger shows that this event index always equals the
required-credit level above the parent:

```text
event_index 1 -> required_above_parent 1: 13,856
event_index 2 -> required_above_parent 2:  1,913
event_index 3 -> required_above_parent 3:    263
event_index 4 -> required_above_parent 4:     46
event_index 5 -> required_above_parent 5:      7
```

There are no non-diagonal pairs:

```text
non-diagonal event_index:required_above_parent pairs: {}
```

Layer `1` is special:

```text
layer 1 count:                 13,856
retimed transition count:      13,856
```

So every checked retimed transition contributes exactly one first pressure
unit, and later layers are additional pressure increases inside the same
transition.

The layer totals are:

```text
layer 1: 13,856
layer 2:  1,913
layer 3:    263
layer 4:     46
layer 5:      7
```

The regime-by-layer matrix is:

| Regime | Layer 1 | Layer 2 | Layer 3 | Layer 4 | Layer 5 | Total |
|---|---:|---:|---:|---:|---:|---:|
| Active high-ladder | `13,120` | `1,835` | `252` | `45` | `7` | `15,259` |
| Post-ladder `EOO` | `572` | `63` | `10` | `1` | `0` | `646` |
| Low-repeat `OO`/`OOEOO` | `164` | `15` | `1` | `0` | `0` | `180` |
| **Total** | `13,856` | `1,913` | `263` | `46` | `7` | `16,085` |

## Depth Table

| Lift | Retimed | Pressure Units | Active | Post | Low | Layer Counts |
|---|---:|---:|---:|---:|---:|---|
| `18 -> 19` | `166` | `178` | `156` | `20` | `2` | `1:166, 2:10, 3:2` |
| `19 -> 20` | `135` | `147` | `143` | `4` | `0` | `1:135, 2:10, 3:2` |
| `20 -> 21` | `253` | `288` | `277` | `10` | `1` | `1:253, 2:34, 3:1` |
| `21 -> 22` | `719` | `801` | `790` | `9` | `2` | `1:719, 2:71, 3:10, 4:1` |
| `22 -> 23` | `869` | `1,019` | `967` | `39` | `13` | `1:869, 2:123, 3:23, 4:4` |
| `23 -> 24` | `1,749` | `2,047` | `1,965` | `64` | `18` | `1:1749, 2:253, 3:39, 4:6` |
| `24 -> 25` | `4,288` | `4,953` | `4,766` | `160` | `27` | `1:4288, 2:578, 3:70, 4:15, 5:2` |
| `25 -> 26` | `5,677` | `6,652` | `6,195` | `340` | `117` | `1:5677, 2:834, 3:116, 4:20, 5:5` |

At every checked depth:

```text
active + post + low = pressure units
sum(layer counts) = pressure units
layer 1 = retimed transitions
```

## Formula Map

The three regimes have these finite algebraic descriptions:

```text
active high-ladder:
  x = 2^a q - 1
  pressure state = 3^k 2^(a-k) q - 1
  word = O^k

post-ladder:
  y = 3^a q - 1
  y == 6 mod 16
  pressure state = EOO(y) = (9y + 10)/8

low-repeat:
  x == -5 mod 64
  pressure state = OO(x) or OOEOO(x)
```

## Theorem Target

The finite ledger suggests the following theorem-facing induction target:

```text
Every retimed above-parent pressure unit lies in exactly one dynamic regime.
Its event index equals its required-credit level above the parent. Layer 1
appears exactly once per retimed transition.
```

In proof terms, this would turn the retimed-pressure hard case into a layered
local induction:

```text
Layer m pressure is paid by the m-th visible dynamic event, and the event is
one of:
  active high-ladder state,
  post-ladder EOO phase,
  low-repeat OO/OOEOO repeat-gate state.
```

The missing proof obligation is not another finite table. It is to derive the
layer law and the three dynamic formulas from the live upper-lift frontier
algebra. The residue tests in the component notes warn that low-bit lookup
tables are incomplete, even when they become highly predictive at high
modulus.
