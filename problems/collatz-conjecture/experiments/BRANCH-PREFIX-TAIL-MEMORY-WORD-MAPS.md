# Branch-Prefix Tail Memory Word Maps

This note is a follow-up to
[`BRANCH-PREFIX-TAIL-MEMORY-CASES.md`](BRANCH-PREFIX-TAIL-MEMORY-CASES.md).
It does not solve Collatz. It turns the six memory-tail records into exact
affine word maps and identifies the low-bit lift required to recover their
residue paths.

The important correction is that the length-8 parity word cylinder modulo
`2^8` does not by itself force the observed `59 mod 64` low-repeat gate. To
know the whole path modulo `64` through eight shortcut steps, the source must
be lifted to modulo `2^(8+6) = 16384`.

## Instrument

Script:

```text
experiments/branch_prefix_tail_memory_word_maps.py
```

Result:

```text
experiments/results/branch_prefix_tail_memory_word_maps_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_memory_word_maps.py --memory-result experiments/results/branch_prefix_tail_memory_cases_d25_d26_20260702.json --output experiments/results/branch_prefix_tail_memory_word_maps_d25_d26_20260702.json --quiet
```

The script reads the six memory records and computes, for each source-to-terminal
word `w`, its shortcut cylinder, exact affine map, raw representative path
modulo `64`, and lifted source classes modulo `16384`.

## Exact Word Maps

For a length-8 word with five odd shortcut steps, the map has multiplier
`3^5 = 243` and denominator `2^8 = 256`.

```text
EEOOEOOO:
  source cylinder: n == 108 mod 256
  affine map:      T^8(n) = (243*n + 1148)/256
  memory records:  5

EEOEOOOO:
  source cylinder: n == 164 mod 256
  affine map:      T^8(n) = (243*n + 1364)/256
  memory records:  1
```

The affine compatibility check is exact:

```text
all memory records affine compatible: true
all memory paths match records:       true
all words length 8 and odd count 5:   true
```

## Raw Cylinder Is Not Enough

If one uses only the least representative of each modulo-`256` cylinder, the
residue paths modulo `64` are:

```text
EEOOEOOO:
  44 -> 54 -> 27 -> 41 -> 62 -> 31 -> 47 -> 7 -> 43

EEOEOOOO:
  36 -> 18 -> 41 -> 62 -> 31 -> 47 -> 7 -> 43 -> 33
```

Neither raw path passes through `59 mod 64`.

This is not a contradiction with the memory-case extractor. Division by `2`
inside the shortcut map means that, after even steps, the next residue modulo
`64` depends on source bits above the first `8` parity-cylinder bits. The
length-8 word fixes the parity itinerary, but it does not fix the full modulo
`64` state itinerary.

## Lifted Memory Paths

Lifting the source to modulo `16384` recovers the exact recorded paths.

```text
EEOOEOOO, source n == 6508 mod 16384, count 3:
  44 -> 54 -> 27 -> 9 -> 14 -> 39 -> 59 -> 25 -> 38

EEOOEOOO, source n == 14700 mod 16384, count 2:
  44 -> 54 -> 27 -> 9 -> 14 -> 39 -> 59 -> 25 -> 6

EEOEOOOO, source n == 10148 mod 16384, count 1:
  36 -> 18 -> 41 -> 30 -> 47 -> 39 -> 59 -> 25 -> 38
```

Thus every actual memory-tail record passes through the low-repeat gate
`59 mod 64`, then through `25 mod 64`, immediately before the terminal state.

Pure lifted claims:

```text
raw mod-256 word paths do not force 59 mod 64: true
memory lifted paths pass 59 mod 64:            true
memory lifted paths have preterminal 25 mod64: true
all memory records affine compatible:          true
all memory paths match records:                true
```

## Theorem Signal

The memory-tail subcase is now smaller but more honest:

```text
1. Prove that the upper-child frontier hypotheses force one of two length-8
   source-to-terminal words:
      EEOOEOOO or EEOEOOOO.

2. Prove the additional lifted source class:
      EEOOEOOO -> n == 6508 or 14700 mod 16384
      EEOEOOOO -> n == 10148 mod 16384

3. Then the exact affine maps and lifted residue paths force the bridge
      59 mod 64 -> 25 mod 64 -> terminal,
   connecting the low-repeat grammar to the post-ladder high-tail carry.
```

This is finite evidence from the exact `25 -> 26` lift, not a proof of the
conjecture. The useful gain is that the old phrase "both words pass through
`59 mod 64`" has been sharpened into an exact lifted-residue statement, which
is the form a local proof would actually have to establish.

## Follow-Up: Minimal Lift Solver

The companion
[`branch_prefix_tail_memory_lift_solver.py`](branch_prefix_tail_memory_lift_solver.py)
shows that the low-repeat bridge is forced one bit earlier than the full
terminal path:

```text
EEOOEOOO: n == 6508 mod 8192
EEOEOOOO: n == 1956 mod 8192
```

Modulo `16384` then selects the terminal residue:

```text
EEOOEOOO:
  6508  -> terminal 38, observed
  14700 -> terminal 6,  observed

EEOEOOOO:
  1956  -> terminal 6,  unobserved ghost class
  10148 -> terminal 38, observed
```

So the sharper theorem target is layered: prove the modulo-`8192` bridge
classes first, then either exclude or absorb the one `EEOEOOOO` ghost
terminal-bit lift.
