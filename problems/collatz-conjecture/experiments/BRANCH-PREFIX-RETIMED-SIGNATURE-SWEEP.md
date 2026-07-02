# Branch-Prefix Retimed Signature Sweep

This note checks whether the symbolic features found in the exact `25 -> 26`
retimed-pressure signature persist across smaller exact frontier lifts.

It is finite evidence only. It does not prove Collatz.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_signature_sweep.py
```

Combined result:

```text
experiments/results/branch_prefix_retimed_signature_sweep_d18_d25_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_retimed_signature_sweep.py --min-parent-depth 18 --max-parent-depth 25 --use-cache --write-depth-cache --output experiments/results/branch_prefix_retimed_signature_sweep_d18_d25_20260702.json
```

The sweep wraps
[`branch_prefix_retimed_signature.py`](branch_prefix_retimed_signature.py)
and caches per-depth signature outputs.

## Stable Checks

Across exact lifts `18 -> 19` through `25 -> 26`:

```text
retimed-pressure transitions:     13,856
above-parent pressure units:      16,085
```

All depth-level dynamic checks held:

```text
all retimed transitions are upper-lift child:      true
all pressure units are upper-lift child:           true
all retimed children are high-assisted descents:   true
all retimed transitions have a first pressure unit:true
all first pressure units are one-unit:             true
all pressure units have prior credit:              true
all pressure units have positive surplus:          true
post-ladder tail equals lag-minus-align 3:         true
no pure retimed low-residue buckets:               true
```

Aggregate pressure-unit regimes:

```text
high_inside_active_ladder: 15,259
high_after_ladder_window:     646
low_repeat_prepaid:           180
```

Thus the three-regime split is not just a `25 -> 26` artifact in the checked
range.

## Depth Table

| Lift | Retimed | Pressure Units | Active Ladder | Post-Ladder `+3` | Low Repeat | High Lag-Min | High Lag-Max | Pure Retimed Buckets mod `65536` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `18 -> 19` | `166` | `178` | `156` | `20` | `2` | `-5` | `3` | `0` |
| `19 -> 20` | `135` | `147` | `143` | `4` | `0` | `-4` | `3` | `0` |
| `20 -> 21` | `253` | `288` | `277` | `10` | `1` | `-5` | `3` | `0` |
| `21 -> 22` | `719` | `801` | `790` | `9` | `2` | `-7` | `3` | `0` |
| `22 -> 23` | `869` | `1,019` | `967` | `39` | `13` | `-9` | `3` | `0` |
| `23 -> 24` | `1,749` | `2,047` | `1,965` | `64` | `18` | `-8` | `3` | `0` |
| `24 -> 25` | `4,288` | `4,953` | `4,766` | `160` | `27` | `-8` | `3` | `0` |
| `25 -> 26` | `5,677` | `6,652` | `6,195` | `340` | `117` | `-10` | `3` | `0` |

The high-ladder maximum `lag_minus_align` is `3` at every checked depth. Every
post-ladder pressure unit is exactly in that `+3` class.

## Theorem Signal

The stable finite statement is:

```text
Every checked retimed-pressure transition is an upper-lift, high-assisted
child. Its first above-parent pressure unit is one unit above the parent level
and is preceded by visible credit. All later above-parent pressure units remain
in one of three regimes: active high ladder, three-step post-ladder tail, or
low-repeat prepaid.
```

The negative residue statement is also stable:

```text
No tested low child-residue table through modulus 65536 isolates the retimed
class. Every retimed bucket is mixed with non-retimed live children.
```

So the next proof target is dynamic, not tabular: derive the three regimes from
the upper-lift bit, the exact high-ladder identity, and the exact low-repeat
`-5 mod 64` gate.

The active high-ladder subset is reconstructed in
[`BRANCH-PREFIX-RETIMED-ACTIVE-LADDER.md`](BRANCH-PREFIX-RETIMED-ACTIVE-LADDER.md).
All `15,259` checked active pressure units are exact ladder states
`3^k 2^(a-k)q - 1` reached by shortcut word `O^k`, with
`v2(state+1)=a-k` and event index equal to required level above parent.

The first above-parent threshold in each retimed transition is isolated in
[`BRANCH-PREFIX-RETIMED-FIRST-THRESHOLD.md`](BRANCH-PREFIX-RETIMED-FIRST-THRESHOLD.md).
That follow-up shows the threshold offset from parent depth ranges from `1` to
`99`, so a constant post-depth window is not the invariant; visible prepayment
is.

The first-threshold post-ladder subset is then reconstructed in
[`BRANCH-PREFIX-RETIMED-POST-LADDER.md`](BRANCH-PREFIX-RETIMED-POST-LADDER.md).
Among the `572` first thresholds in the post-ladder `+3` class, every checked
ladder terminal has residue `6 mod 16` and the exact three-step shortcut word
`EOO`, giving threshold state `(9y + 10)/8`.

The low-repeat subset is reconstructed in
[`BRANCH-PREFIX-RETIMED-LOW-REPEAT.md`](BRANCH-PREFIX-RETIMED-LOW-REPEAT.md).
All `180` checked low-repeat pressure units come from the exact
`x == -5 mod 64` repeat gate, obey `v2(OOE(x)+5)=v2(x+5)-3`, and reach the
pressure state by shortcut word `OO` or `OOEOO`.

The three component certificates are combined in
[`BRANCH-PREFIX-RETIMED-THREE-REGIME-LEDGER.md`](BRANCH-PREFIX-RETIMED-THREE-REGIME-LEDGER.md).
It verifies that active + post + low covers all `16,085` pressure units and
extracts the shared layer law: event index equals required-credit level above
the parent, with layer `1` occurring exactly once per retimed transition.
