# Branch-Prefix Retimed Pressure Sweep

This note checks whether the retimed-pressure timing pattern observed in the
exact `25 -> 26` lift is stable across smaller exact frontier lifts.

It is finite evidence only. It does not prove Collatz.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_pressure_sweep.py
```

Combined result:

```text
experiments/results/branch_prefix_retimed_pressure_sweep_d18_d25_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_retimed_pressure_sweep.py --min-parent-depth 18 --max-parent-depth 25 --use-cache --write-depth-cache --output experiments/results/branch_prefix_retimed_pressure_sweep_d18_d25_20260702.json
```

The sweep wraps
[`branch_prefix_retimed_pressure.py`](branch_prefix_retimed_pressure.py).
For each lift `d -> d+1`, it selects live child transitions with

```text
required_delta > 0
credit_delta < required_delta
```

and checks whether the first prefix where the child required credit exceeds
the parent required credit is one unit above parent and already prepaid by a
visible high-ladder or low-repeat credit event.

## Sweep Result

Global checks over `18 -> 19` through `25 -> 26`:

```text
all depths trace safe:           true
all thresholds one-unit:         true
all thresholds prepaid:          true
minimum positive threshold margin: 1
```

Depth table:

| Lift | Live Parents | Live Children | Positive Pressure | Retimed | Min Threshold Surplus | Max Lag | Prior High | Prior Low | Threshold High Step | Threshold Ordinary |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `18 -> 19` | `7,495` | `14,990` | `1,398` | `166` | `1` | `11` | `164` | `2` | `144` | `22` |
| `19 -> 20` | `14,990` | `27,328` | `1,950` | `135` | `3` | `15` | `135` | `0` | `131` | `4` |
| `20 -> 21` | `27,328` | `46,611` | `3,705` | `253` | `2` | `19` | `253` | `0` | `247` | `6` |
| `21 -> 22` | `46,611` | `93,222` | `7,217` | `719` | `1` | `22` | `717` | `2` | `710` | `9` |
| `22 -> 23` | `93,222` | `168,807` | `11,438` | `869` | `3` | `17` | `857` | `12` | `824` | `45` |
| `23 -> 24` | `168,807` | `286,581` | `22,122` | `1,749` | `2` | `16` | `1,734` | `15` | `1,684` | `65` |
| `24 -> 25` | `286,581` | `573,162` | `41,509` | `4,288` | `2` | `21` | `4,267` | `21` | `4,135` | `153` |
| `25 -> 26` | `573,162` | `1,037,374` | `71,321` | `5,677` | `2` | `19` | `5,565` | `112` | `5,245` | `432` |

Every row has:

```text
retimed trace failures:                  0
max trace deficit:                       0
threshold required above parent:         exactly 1
```

## Corrected Theorem Signal

The `25 -> 26` audit had minimum threshold surplus `2`, but the depth sweep
shows that `2` is not the right universal finite pattern: depths `18` and `21`
have threshold surplus `1`.

The more stable local lemma suggested by the sweep is therefore:

```text
For a live retimed-pressure child, the first above-parent pressure threshold
is a one-unit required-credit increase, and some visible high-ladder or
low-repeat credit event occurs before that threshold with enough accumulated
credit to keep the prefix ledger nonnegative.
```

The finite sweep supports this lemma on `13,856` retimed-pressure transitions
across eight exact frontier lifts, but the proof obligation remains open:
derive the timing fact from the child lift bit plus the low/high alignment
grammar, without enumerating depths.

The exact `25 -> 26` hard class is further split into dynamic regimes in
[`BRANCH-PREFIX-RETIMED-SIGNATURE.md`](BRANCH-PREFIX-RETIMED-SIGNATURE.md).
That follow-up also shows that low child residues alone do not recognize the
hard class through modulus `65536`.

The regime split itself was then swept across the same depth range in
[`BRANCH-PREFIX-RETIMED-SIGNATURE-SWEEP.md`](BRANCH-PREFIX-RETIMED-SIGNATURE-SWEEP.md):
all `13,856` retimed transitions remained upper-lift, high-assisted children,
and all `16,085` pressure units remained inside the three dynamic regimes.

The first threshold in each retimed transition is isolated in
[`BRANCH-PREFIX-RETIMED-FIRST-THRESHOLD.md`](BRANCH-PREFIX-RETIMED-FIRST-THRESHOLD.md).
It preserves the one-unit/prepaid result and shows the first threshold offset
from parent depth ranges from `1` to `99`.
