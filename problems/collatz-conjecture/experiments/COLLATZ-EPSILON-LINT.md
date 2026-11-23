# Collatz Epsilon/Sibling Lint Harness - 2026-07-05

**Instrument:** [`collatz_epsilon_lint.py`](collatz_epsilon_lint.py)  
**Result:** [`results/collatz_epsilon_lint_20260705.json`](results/collatz_epsilon_lint_20260705.json)  
**Status:** executable proof-sketch guardrail. This is not a proof of Collatz.

## Purpose

The repo already has the epsilon barrier: parity-word statistics cannot separate
`3n+1` from the false sibling world `3n-1`. This harness turns that doctrine
into a reusable lint gate for future work.

A candidate invariant should not be promoted unless it can answer:

1. Where does the `+1` intercept enter?
2. Why does the same argument fail on positive `3n-1` cycles?
3. Why does it fail on known nontrivial `5n+1` cycles, or why is that sibling
   outside the claim's domain?
4. How does it separate positive integers from negative cycles and 2-adic
   ghost residents?
5. What exact command and result path can falsify it?

## What The Run Checks

The generated JSON records:

- the depth-12 parity-word barrier for `(3,+1)` versus `(3,-1)`;
- exact affine traces showing that the coefficient is epsilon-blind while the
  intercept sign flips with epsilon;
- known positive cycle controls for `(3,+1)`, `(3,-1)`, and `(5,+1)`;
- negative Collatz cycle controls, via the `3n-1` conjugacy;
- stress families: hard Collatz starts, Mersenne shadows, high ladders,
  low-repeat gates, and false-world cycle minima;
- lint verdicts for common proof ingredients.

The depth-12 run reproduced:

```text
word distribution identical: true
odd-count distribution identical: true
pointwise same-integer word differs: 4094 / 4096
survivor frontier word count: 226 / 4096
all positive cycle sign rules hold: true
```

## Lint Verdicts

| Probe | Status | Reason |
|---|---|---|
| parity-word distribution | reject as standalone | identical for `3n+1` and `3n-1` |
| odd density / multiplier excess | reject as standalone | word-only and epsilon-blind |
| survivor frontier count | reject as standalone | word-only and epsilon-blind |
| affine intercept sign | allowed input | this is where `+1` versus `-1` enters |
| positive cycle side of critical line | allowed input | sign-sensitive cycle obstruction |
| low-repeat / high-ladder value gates | stress required | useful only with positivity, intercept, and infinite-lift control |

## Commands

```powershell
python experiments\collatz_epsilon_lint.py selftest --json
python experiments\collatz_epsilon_lint.py run --depth 12 --trace-depth 40 --out experiments\results\collatz_epsilon_lint_20260705.json
python experiments\build_results_manifest.py
```

## How To Use It

Before a future proof sketch gets theorem language, add or name a probe here.
If the probe is word-only, it starts dead. If it is value-level, it must still
explain the false sibling worlds and the positive-integer boundary.

The target is not confidence theater. The target is a cheap, replayable way to
make bad ideas fail before they become polished prose.
