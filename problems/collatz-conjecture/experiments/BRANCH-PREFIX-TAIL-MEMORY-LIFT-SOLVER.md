# Branch-Prefix Tail Memory Lift Solver

This note refines
[`BRANCH-PREFIX-TAIL-MEMORY-WORD-MAPS.md`](BRANCH-PREFIX-TAIL-MEMORY-WORD-MAPS.md).
It does not solve Collatz. It separates the local memory bridge into two
different low-bit facts:

```text
mod 8192   forces the bridge 59 mod 64 -> 25 mod 64
mod 16384  decides the final terminal residue mod 64
```

The distinction matters because the earlier word-map note correctly identified
the full observed source classes modulo `16384`, but the actual low-repeat
bridge needs only one fewer lifted bit.

## Instrument

Script:

```text
experiments/branch_prefix_tail_memory_lift_solver.py
```

Result:

```text
experiments/results/branch_prefix_tail_memory_lift_solver_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_memory_lift_solver.py --memory-result experiments/results/branch_prefix_tail_memory_cases_d25_d26_20260702.json --output experiments/results/branch_prefix_tail_memory_lift_solver_d25_d26_20260702.json --quiet
```

The script writes a source in the form

```text
n = r + 256m
```

where `r` is the length-8 parity-cylinder residue, then enumerates
`m mod 64`.  It groups the full modulo-`16384` lifts by smaller projections to
find the first modulus at which the bridge is forced for all refinements.

## Pure Claims

```text
all observed full lifts are bridge classes:          true
all observed classes project to forced mod-8192:     true
bridge is first forced at five extra bits for both:  true
there is exactly one unobserved bridge full lift:    true
```

Here "five extra bits" means `2^(8+5) = 8192`, since the words have length `8`.

## Word EEOOEOOO

Exact word map:

```text
r = 108
T^8(n) = (243*n + 1148)/256
```

Bridge class:

```text
n == 6508 mod 8192
equivalently m == 25 mod 32
```

Full terminal lifts modulo `16384`:

```text
n == 6508 mod 16384:
  m == 25 mod 64
  path: 44 -> 54 -> 27 -> 9 -> 14 -> 39 -> 59 -> 25 -> 38
  observed count: 3
  if align a = 3, q == 37 mod 64

n == 14700 mod 16384:
  m == 57 mod 64
  path: 44 -> 54 -> 27 -> 9 -> 14 -> 39 -> 59 -> 25 -> 6
  observed count: 2
  if align a = 3, q == 5 mod 64
```

For this word, both terminal-bit refinements of the forced modulo-`8192`
bridge class occur in the six memory records.

## Word EEOEOOOO

Exact word map:

```text
r = 164
T^8(n) = (243*n + 1364)/256
```

Bridge class:

```text
n == 1956 mod 8192
equivalently m == 7 mod 32
```

Full terminal lifts modulo `16384`:

```text
n == 1956 mod 16384:
  m == 7 mod 64
  path: 36 -> 18 -> 41 -> 30 -> 47 -> 39 -> 59 -> 25 -> 6
  observed count: 0
  if align a = 4, q == 23 mod 64

n == 10148 mod 16384:
  m == 39 mod 64
  path: 36 -> 18 -> 41 -> 30 -> 47 -> 39 -> 59 -> 25 -> 38
  observed count: 1
  if align a = 4, q == 55 mod 64
```

The unobserved class `n == 1956 mod 16384` is a local ghost candidate. It
satisfies the same source-to-terminal bridge but does not occur among the six
memory-tail records in the exact `25 -> 26` retimed hard class.

## Theorem Signal

The memory lemma should now be stated in two layers:

```text
Layer 1: bridge lift
  EEOOEOOO  -> source n == 6508 mod 8192
  EEOEOOOO  -> source n == 1956 mod 8192

Layer 2: terminal-bit refinement
  EEOOEOOO  -> both terminal refinements occur
  EEOEOOOO  -> only the terminal-38 refinement is observed;
               terminal-6 is a ghost local class
```

This is an honest tightening of the proof target. A local proof does not need
to force the full modulo-`16384` class just to obtain the low-repeat bridge.
But if it wants to match the exact observed memory records, it must also either
exclude the `EEOEOOOO` ghost class or prove that the ghost is harmless under the
same post-ladder pressure accounting.

## Follow-Up: Ghost-Class Audit

[`branch_prefix_tail_ghost_class.py`](branch_prefix_tail_ghost_class.py) checks
the full `340` post-ladder tail population. The terminal ghost signature

```text
a = 4, q == 23 mod 64, terminal == 6 mod 64
```

does occur, with count `25`. But all `25` occurrences are terminal-local:

```text
source_lag_to_terminal = 0
ghost memory-source count = 0
```

So the ghost does not need to be excluded merely as a terminal class in the
exact `25 -> 26` lift. It is absorbed by the terminal-local phase branch; the
nonterminal memory branch still has only the six known lag-8 records.
