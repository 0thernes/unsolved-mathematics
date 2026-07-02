# Collatz Pursuit Current State - 2026-07-02

## Verdict

The conjecture remains open. The four shared ChatGPT threads do not contain a
proof, and their named `sandbox:/mnt/data/...` files are not publicly
recoverable from the share pages and are not present in this workspace.

What they do contain is useful: they independently point to the same current
mathematical seam in this repo. The old broad statement "spine ladders expel
positive shadows from supercritical cylinders" is now sharpened into a precise
regeneration problem:

```text
positive orbit shadows a nonpositive 2-adic spine
  -> deterministic ladder expulsion
  -> fresh alignment toward a later spine
  -> exact phase collision
  -> odd-unit congruence lock
  -> density/codimension barrier still needed
```

In parallel, the repo's branch-prefix work has sharpened the local lift
problem:

```text
exact survivor frontier lift
  -> retimed pressure child
  -> high-ladder / low-repeat structural credit
  -> tight layer-one cases
  -> pre-entry reserve >= 1
  -> equality classified by the previous reserve source
```

The pursuit now has two honest axes: a global 2-adic regeneration-lock axis and
a local frontier-lift reserve axis. The bridge between them is the live target.

## Source Intake

Four public ChatGPT share pages were decoded and summarized in
[`CHATGPT-SHARE-DEEP-ANALYSIS-2026-07-02.md`](CHATGPT-SHARE-DEEP-ANALYSIS-2026-07-02.md).

| Link | Thread content | Status in repo |
|---|---|---|
| `https://chatgpt.com/share/6a46ab12-6df8-83ec-8c83-3ad580b9daae` | Regeneration sieve | Algebraic target accepted; named files unavailable |
| `https://chatgpt.com/share/6a46ab08-8f38-83ec-9b68-f37740f93826` | Phase-collision sprint | Reproduced locally by `spine_phase_collision_lab.py` |
| `https://chatgpt.com/share/6a46aafc-df94-83ec-9e39-0a4838f4bd58` | Round 20 survival extension | Not accepted as evidence until files/logs/manifests are local |
| `https://chatgpt.com/share/6a46aae7-a2a8-83ec-836e-1db1cdfa6c3a` | Round 21 density / boundary package | Density firewall partially reproduced; boundary-ray claims remain audit targets |

The named files from the shares are listed in the deep-analysis memo. They were
not downloaded because the public share metadata exposes `file_attachments: []`
and only transcript-local sandbox paths.

## Public Literature Baseline

The external backdrop was re-checked on 2026-07-02:

- Tao's `arXiv:1909.03562` proves an almost-all result in logarithmic density,
  not convergence for every integer.
- Hercher's `arXiv:2201.00406` excludes Collatz `m`-cycles with `m <= 91` and,
  together with verification below `3*2^69`, gives the large odd-term cycle
  floor.
- Bařina's verification project page reports verification below `2^71` on
  2025-01-15.
- Angeltveit's `arXiv:2602.10466` is a verification-algorithm paper, not a
  proof.
- `arXiv:2605.13886` is withdrawn and should not be cited as support.

This keeps the repo aligned with the public mathematical state: open problem,
massive computation, strong almost-all theorem, no known counterexample.

## What Graduated Into Local Evidence

### 1. Phase-collision normal form

The exact local identity is now filed in
[`SPINE-PHASE-COLLISION.md`](SPINE-PHASE-COLLISION.md) with instrument
[`spine_phase_collision_lab.py`](spine_phase_collision_lab.py).

For a source supercritical word with spine `rho_0`, phase spine `rho_t`, and

```text
x - rho_0 = 2^m u,  u odd in Z_2,
```

we have

```text
T^t(x) - eta = 3^a(t) 2^(m-t) u + (rho_t - eta).
```

Let `e_t = v2(rho_t - eta)`. If `m - t != e_t`, then

```text
v2(T^t(x) - eta) = min(m - t, e_t).
```

Deep fresh regeneration can happen only in the matched case `m - t = e_t`,
where it becomes the odd-unit lock

```text
3^a(t) u == -2^(-e_t)(rho_t - eta) mod 2^R.
```

This is an exact theorem target. It is not a Collatz proof.

### 2. Finite phase lab

The current run:

```powershell
python experiments/spine_phase_collision_lab.py --max-depth 12 --identity-trials 5000 --output experiments/results/spine_phase_collision_lab_d12_20260702.json --quiet
```

recorded:

```text
identity checks: 5000
identity failures: 0
nonmatched valuation-rule failures: 0
supercritical necklace cycles: 181
primitive source cycles: 161
primitive source phase states: 1716
unique target spines: 161
```

The important negative result is that the phase gate alone is too permissive:

```text
allowed source-alignment fraction, unique target spines: 0.777558620542
allowed source-alignment fraction, all target cycles:    0.751980433903
```

So the proof target cannot be "phase mismatch kills regeneration." It must use
the odd unit, positivity, entropy/codimension, or a stronger invariant.

### 3. Mersenne lock anchor

The `-1` to `-5` pure Mersenne shadow would require

```text
3^k == -1 mod 2^e.
```

The lab checks `e = 3..8` and finds no residue class for `k`. This is a clean
anchor for the odd-unit-lock point of view: regeneration is a concrete
2-adic congruence problem, not a vague repulsion event.

### 4. Density firewall reproduction

The local lab reproduces the Round 21 density-firewall shape. Barrier-word
density falls rapidly:

```text
k=16:   log2 density = -4.954240338617
k=64:   log2 density = -9.387506940142
k=128:  log2 density = -13.806868252474
k=512:  log2 density = -35.849409866165
k=1024: log2 density = -62.910315553639
k=2048: log2 density = -115.604845414258
k=4096: log2 density = -219.577132699132
```

This supports "density zero," not "empty." A divergent orbit could still hide
in a null exceptional set unless the odd-unit/positivity structure kills it.

### 5. Boundary-ray positivity sensor

The same run computes inverse residues along the coefficient-boundary word.
Nearest-distance bit lengths are large:

```text
L=64:  63
L=128: 123
L=256: 255
L=512: 509
```

Ordinary fixed positive integers have eventually bounded distance to either
`0` or `2^L` modulo `2^L`. The critical boundary residue does not show that
behavior in the sampled prefixes. This is a positivity sensor, not a theorem.

## What Did Not Graduate

### Round 20 survival extension

The third share names a Round 20 extension with manifests and C++ audit tools,
but those files are absent locally and unavailable from the share. Therefore:

- no claimed Round 20 survivor count is accepted;
- no manifest verification is accepted;
- no `M_+(606)` or related boundary claim is accepted from that thread alone;
- the thread is a replication target, not repo evidence.

To graduate, the actual manifest files and source must be placed in the repo,
compiled, run, and cross-checked against independent counters.

### Round 21 boundary-ray package

The fourth share's density-firewall idea was partially reproduced in the local
phase lab. Its boundary-ray script and sample output were not recoverable.
Therefore the boundary-ray package remains only partially accepted: the
general positivity-sensor direction is useful, but file-specific claims are
unverified.

### Full proof language

Any statement implying that the conjecture is solved, closed, finished, or
proved is rejected. The repo status remains `open`.

## Integration With Existing Repo State

### Spine ladder axis

[`SPINE-LADDER.md`](SPINE-LADDER.md) already gave the key localization:
supercritical spines are nonpositive, positive integers cannot be periodic
points on them, and positive shadows are expelled after a deterministic number
of blocks. That note also identified the missing regeneration problem.

The share-thread material advances the missing part by identifying the exact
regeneration equation and congruence lock. It does not close it.

### Branch-prefix / retimed-reserve axis

The retimed pressure series now reaches
[`BRANCH-PREFIX-RETIMED-TIGHT-RESERVE-SOURCE.md`](BRANCH-PREFIX-RETIMED-TIGHT-RESERVE-SOURCE.md).
The current finite state is:

- exact lifts `18 -> 19` through `25 -> 26`;
- `13,856` retimed transitions checked;
- `16,085` above-parent pressure units checked;
- all pressure units have prior credit and positive surplus;
- all `511` align-3 local-grammar records enter the final align-3 credit with
  `entry_required = parent_required`;
- the five tight cases are exactly prior reserve-`1` cases;
- equality is sourced by four previous align-3 high-ladder credits and one
  previous low-repeat align-8 credit.

The open local theorem is now clean:

```text
prove pre-entry reserve >= 1 for every live retimed frontier lift,
and classify equality from the previous reserve source.
```

### Bridge target

The promising bridge is to show that the retimed-reserve sources are local
finite-shadow manifestations of the global phase-collision odd-unit locks.
The same two structural objects keep recurring:

- high ladder: `x = 2^a q - 1`;
- low repeat: `x == -5 mod 64`.

The repo should now test whether every local reserve-source equality case can
be expressed as a phase-collision lock with a measurable odd-unit codimension.
If yes, the local lift induction and the global density firewall may become
one theorem instead of two disconnected empirical ledgers.

## Current Proof-Shaped Target

The strongest honest target, after integrating the four shares, is:

```text
Every positive orbit that repeatedly shadows supercritical 2-adic spines
must repeatedly satisfy explicit phase-collision odd-unit locks. The cumulative
codimension of those locks, together with positivity of finite integer shadows,
dominates the entropy of admissible survivor branches. Locally, every exact
frontier lift either inherits branch-prefix credit, receives structural credit
before a new pressure unit, or exits by certificate descent.
```

This would attack both halves:

- divergent orbit: no infinite positive finite shadow can stay inside the
  null frontier while paying the locks forever;
- nontrivial cycle: a positive cycle would have to be a periodic positive
  shadow of a supercritical spine, but supercritical spines are nonpositive and
  regeneration would have to close an impossible odd-unit loop.

That paragraph is a theorem program, not a theorem.

## Immediate Next Work

1. **Odd-unit lock census.** Extend `spine_phase_collision_lab.py` from phase
   gates to actual unit-residue locks modulo `2^R`, and measure codimension
   across source/target spine transitions.
2. **Retimed bridge extraction.** For the `511` align-3 grammar records, compute
   the corresponding source spine, target spine, phase `t`, unit `u`, and lock
   residue. Compare the five reserve-`1` cases against the `506` near-misses.
3. **Round 20 replication gate.** Do not cite Round 20 counts until the missing
   files are recovered or recreated and independently verified.
4. **Boundary-ray reproduction.** Rebuild the Round 21 boundary-ray script from
   first principles in the repo, not from unavailable sandbox output.
5. **Status discipline.** Keep `status.md`, `metadata.json`, and the audit
   register aligned: open problem, verified finite evidence, theorem targets
   only.

## Bottom Line

The four shares did not solve Collatz. They did something still valuable: they
forced the current repo into a sharper shape. The live wall is no longer a
generic "exceptional set" wall. It is the exact collision between:

- deterministic expulsion from nonpositive supercritical spines;
- fresh positive regeneration through odd-unit congruence locks;
- density-zero-but-not-empty survivor frontiers;
- local retimed lift pressure paid by high-ladder and low-repeat reserve.

That is where the pursuit stands now.
