# Branch-Prefix Tail Lift-Bit Witness

This note extracts the smallest concrete witness from
[`BRANCH-PREFIX-TAIL-CHILD-LIFT-STRATIFIER.md`](BRANCH-PREFIX-TAIL-CHILD-LIFT-STRATIFIER.md).

It does not solve Collatz. It shows why a proof using only `child mod 2048`
and visible terminal phase cannot handle the finite `25 -> 26` tail-memory
obstruction.

## Instrument

Script:

```text
experiments/branch_prefix_tail_lift_bit_witness.py
```

Result:

```text
experiments/results/branch_prefix_tail_lift_bit_witness_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_lift_bit_witness.py --input experiments/results/branch_prefix_tail_child_lift_stratifier_d25_d26_20260702.json --output experiments/results/branch_prefix_tail_lift_bit_witness_d25_d26_20260702.json --quiet
```

## Claims Checked

```text
candidate record count is 9:                         true
phase signature has a mixed bucket:                  true
lower-phase signature has a mixed bucket:            true
lower-lift signature is pure:                        true
upper-timing signature is pure:                      true
witness has same lower phase with opposite labels:   true
witness uses both lift bits:                         true
```

## The Witness

The following two records have the same lower child residue and the same visible
terminal phase:

```text
child mod 2048:          1743
terminal_step:             35
event_step:                38
align:                      3
q mod 64:                   5
terminal mod 64:            6
terminal_current_gap:       0.081541375001010298483449
```

But they have opposite outcomes:

```text
memory_lag_8:
  child              40992463
  child mod 4096         3791
  lift bit                  1
  source word        EEOOEOOO
  source mod 16384      14700

terminal_local:
  child              53429967
  child mod 4096         1743
  lift bit                  0
```

Thus the lower residue and terminal phase are provably insufficient for this
finite lift: the next child bit is necessary for the witness pair.

## Pure Lower-Lift Rule

On the nine records consisting of the six memory tails plus the three
terminal-local collisions in their lower buckets, the pure memory lower-lift
keys are:

```text
 447|1 : memory 1
 751|0 : memory 1
1471|0 : memory 1
1743|1 : memory 1
1895|0 : memory 2
```

The terminal-local collision keys are:

```text
1743|0 : terminal-local 2
1895|1 : terminal-local 1
```

Equivalently, the finite `child mod 4096 + event_step` separator is not just a
large residue table. It is a lower-residue table plus one necessary lift bit.

## Theorem Signal

The exact local obstruction is now:

```text
lower 1743 with the visible phase (35,38,3,5,6,gap)
has both a terminal-local lift and a memory lift.
```

Any theorem that tries to close this tail branch using terminal phase, cofactor
phase, or `child mod 2048` alone is too weak. The proof must explain the lift
bit: why `1743|1` and `1895|0` are memory-bearing, while `1743|0` and
`1895|1` are terminal-local in the upper-child hard frontier.
