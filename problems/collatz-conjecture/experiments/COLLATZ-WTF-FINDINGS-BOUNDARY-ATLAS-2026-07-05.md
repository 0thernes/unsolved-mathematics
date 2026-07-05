# Collatz WTF Findings Boundary Atlas - 2026-07-05

Purpose: collect the strangest, most useful oddities from the public Collatz
literature and this repo's experiments. These are the boundary phenomena worth
pushing on because they expose where ordinary proof strategies fail.

Status: research-routing artifact. It does not prove Collatz. It separates:

- **External theorem/result**: accepted or source-backed literature.
- **Repo proved identity**: exact local algebra checked/proved in repo docs.
- **Repo measured**: finite computation with scripts/results.
- **Hypothesis/target**: promising theorem target, not yet proved.
- **Quarantine**: useful failure pattern, not support.

## One-Screen Verdict

The weirdest thing is not that Collatz looks random. The weirdest thing is that
several exact mathematical views make the bad set look simultaneously:

```text
measure-zero
statistically invisible
locally unrestricted
2-adically natural
computationally absent through enormous ranges
still not logically empty
```

That contradiction-feeling is the frontier. Future novelty should attack that
gap directly, not rediscover average drift, finite verification, or prettier
inverse trees.

## Top WTF Leaderboard

| Rank | Finding | Status | WTF score | Why it matters | Boundary rule |
|---:|---|---|---:|---|---|
| 1 | The `3n+1` and `3n-1` word systems have identical parity-word statistics, but `3n-1` has positive frontier cycles. | Repo proved + measured | 10 | Kills every proof route based only on parity-word counts, density, entropy, dimension, or typicality. | Any future proof must consume the affine intercept/sign, not only the word. |
| 2 | The 2-adic survivor frontier has exact dimension `H(log_3 2) = 0.9499555...`, measure zero, and still never empties. | Repo proved + classical context | 10 | "Small" is not "empty"; density-zero arguments can miss every counterexample. | Never claim dimension/density decay proves convergence. |
| 3 | Tao's theorem gets almost all orbits almost bounded, yet the remaining exceptional set can still host all counterexamples. | External theorem | 10 | This is the modern professional version of the distributional-to-pointwise wall. | New work must beat the exceptional-set barrier, not restate it. |
| 4 | Every finite parity word occurs as a residue class modulo `2^d`. | Classical / repo used | 9 | No finite local parity pattern is forbidden, including very scary high-odd patterns. | Finite word exclusion needs a lift theorem or it is not global. |
| 5 | Generalized Collatz maps can be computationally universal / undecidable. | External theorem family | 9 | A method that proves too broad a class is suspect by design. | The proof must be special to `3`, `2`, `+1`, positivity, or intercepts. |
| 6 | Nontrivial cycles, if they exist, are forced past absurd floors, but finite cycle floors still do not rule out cycles. | External + repo rederived | 9 | The cycle half feels almost physically impossible while remaining logically open. | Keep cycle work separate from divergence work. |
| 7 | The Mersenne shadows `2^j-1` track the 2-adic `-1` boundary for `j` forced odd steps, then detach at model rate. | Repo proved + measured | 8 | The most obvious positive shadow of the ghost does not stick anomalously. | Use as a calibration stress test, not as proof. |
| 8 | Phase collision is exact, but the phase gate alone is too permissive: ~75% of finite source alignments pass. | Repo proved + measured | 8 | "Phase mismatch kills regeneration" is false. The real object is the odd-unit lock. | Push odd-unit/codimension, not phase-only arguments. |
| 9 | Retimed pressure units split into three local regimes with exact finite coverage in checked lifts. | Repo measured | 8 | This is the best local theorem-mining seam in the repo. | Needs induction/lift proof before it is mathematics beyond finite evidence. |
| 10 | `5n+1` and `3n-1` sibling runs make the same instruments visibly detect failure modes. | Repo measured | 8 | Turns silent Collatz scans into calibrated negative readings. | Every proposed invariant should be tested on siblings. |
| 11 | Paradoxical sequences exceed what odd/even ratio intuition predicts after stopping time. | External recent work | 8 | Shows average-ratio heuristics can fail in finite structured ways. | Treat as stress cases for drift/potential claims. |
| 12 | Human-LLM collaboration is now producing plausible Collatz frameworks, but the key hypotheses remain open. | External + repo process | 7 | Workflow novelty is real; theorem novelty is not automatic. | Extract obligations, scripts, and falsifiers from model output. |
| 13 | The repo preserved false proof attempts and built instruments that refuted them. | Repo process | 7 | Rare artifact: a live failure-containment lab on an open problem. | This is methodological novelty, not a Collatz breakthrough. |
| 14 | Claimed proofs repeatedly smuggle "almost all -> all", inverse-tree coverage, or finite-to-infinite jumps. | Literature/process | 7 | The same cognitive trap keeps reappearing under new notation. | Quarantine proof claims until obligations are explicit. |
| 15 | Exact affine/cocycle identities can be true while their sufficiency claims fail. | Repo audits | 7 | Correct algebra can still be proof-shaped noise if it lacks a global invariant. | Separate identity, mechanism, and sufficiency. |

## The Weirdest External Discoveries

### 1. Undecidable Generalizations

Conway/Kurtz-Simon style generalized Collatz systems show that innocent-looking
arithmetic iteration can simulate computation. This is beyond-the-beyond weird:
the family surrounding Collatz contains program halting shadows.

Use: falsify overgeneral proof strategies.

Do not use: as evidence that original `3n+1` is undecidable or impossible.

### 2. The 2-Adic Ghost World

In `Z_2`, parity sequences become natural symbolic dynamics. The catch is that
positive integers are a very special subset. Typical 2-adic behavior can be
mathematically clean and still miss the actual problem.

Use: exact language for parity cylinders, spines, and survivor sets.

Do not use: "almost every 2-adic point behaves" as a positive-integer theorem.

### 3. Tao's Almost-All Breakthrough

Tao's result is the strongest public theorem on the divergence side: almost all
orbits, in logarithmic density, attain almost bounded values. Its weirdness is
that it proves an enormous amount while also spotlighting the unclosed hole:
the exceptional set may still be the whole counterexample set.

Use: benchmark. If a new density theorem is weaker than Tao, it is probably not
frontier-moving.

### 4. Paradoxical Sequences

Rozier/Terracol-style paradoxical behavior says that after a stopping time,
some finite sequences can exceed the first term despite odd/even ratio
intuition. This is a finite "don't trust the average" warning.

Use: hard finite tests for drift, potential, and repayment claims.

### 5. Verification Is Astronomical And Still Finite

Barina's `2^71` verification and Angeltveit-style verification algorithms
create enormous empirical floors. The WTF is the mismatch between practical
certainty and logical nonclosure.

Use: support cycle floors, calibrate code, reject small counterexamples.

Do not use: as proof beyond the floor.

## The Weirdest Repo Findings

### A. The Epsilon-Invariance Barrier

`SIBLING-CONTROL.md` is the repo's sharpest mathematical/process contribution.
The parity-word universe cannot distinguish `(3,+1)` from `(3,-1)`, but the
positive frontier truth changes. The sign of the intercept is not decoration;
it is the battlefield.

Novelty posture: known-in-spirit from sibling folklore, sharpened here into a
machine-checked certificate-frontier control system.

### B. Frontier Geometry Is Almost Empty And Still Alive

`FRONTIER-GEOMETRY.md` makes the bad set exact: a Cantor-like 2-adic survivor
frontier, density `F(d)`, dimension `H(theta)`, exact `E[tau]`, and localization
of any counterexample minimum to frontier residues.

WTF: at depth 8192, the uncertified fraction is around `2^-426`, but the proof
program still cannot replace "tiny" with "none."

### C. The Mersenne Boundary Does Not Cheat

The natural positive truncations of the all-odd `-1` ghost,
`2^j - 1`, ride the boundary exactly for `j` odd shortcut steps. Measurements
then show detachment close to the model rate.

Interpretation: the obvious positive ghost-shadow does not show anomalous
adhesion. That is evidence against the simplest counterexample shape, not proof.

### D. Phase Collision Is Real, But Not Enough

The exact phase-collision normal form turns regeneration into a congruence:

```text
3^a(t) u == -2^(-e_t)(rho_t - eta) mod 2^R
```

The finite lab found zero identity failures, but also found that phase matching
alone is far too permissive. The odd unit is the lock.

### E. Retimed Pressure Has A Three-Regime Local Grammar

The branch-prefix retimed work splits checked above-parent pressure units into:

```text
active high-ladder
post-ladder EOO
low-repeat OO / OOEOO
```

with exact finite coverage across checked lifts. This is where new theorem
mining should happen, because it is specific, falsifiable, and not just a
restatement of known density.

### F. Failed Proofs Became Instruments

The repo's most unusual contribution is not a theorem. It is that false proof
routes were not erased; they were audited into:

- pseudo-proof sweeps;
- claim manifests;
- sibling controls;
- finite certificate ledgers;
- source-check matrices;
- quarantine directories.

That is rare and potentially publishable as methodology.

## Boundary Between "Special" And "Breakthrough"

| Claim | Honest status |
|---|---|
| "We found a Collatz proof." | False / unsupported. |
| "We found new theorem targets." | Yes. |
| "We built a rare AI-assisted failure-containment lab." | Yes, likely special. |
| "The repo has finite discoveries that may be novel in presentation." | Yes, possible. |
| "The accepted math moves beyond Tao/Hercher/Barina." | No. |
| "The weirdest local insight is the sibling/intercept barrier." | Yes. |
| "The most promising next theorem target is regeneration/odd-unit locks plus retimed reserve induction." | Yes, as a target. |

## Push-Boundary Program

Future work should prioritize these exact attacks:

1. **Odd-unit lock theorem.**
   Prove repeated regeneration requires accumulating congruence codimension that
   positive integer shadows cannot keep paying.

2. **Retimed reserve induction.**
   Lift the finite three-regime pressure ledger into an induction over frontier
   depth.

3. **Sibling-falsification harness.**
   Every new invariant must be run on `(3,-1)` and `5n+1`; if it cannot tell
   them apart, it cannot close Collatz.

4. **Paradoxical-sequence stress suite.**
   Import paradoxical finite sequences as adversarial tests for any drift or
   potential claim.

5. **Proof-assistant candidates.**
   Formalize only the exact local identities first: affine law, high ladder,
   phase collision, sign/intercept theorem. Do not formalize speculative closure
   claims until the missing induction is explicit.

6. **Prior-art collision gate.**
   Every new idea must name the old row it is colliding with in the failed-ideas
   atlas and state the new ingredient in one sentence.

## Source Backbone

- Lagarias annotated bibliography I: <https://arxiv.org/abs/math/0309224>
- Lagarias annotated bibliography II: <https://arxiv.org/abs/math/0608208>
- Lagarias overview: <https://arxiv.org/abs/2111.02635>
- Tao almost-all theorem: <https://arxiv.org/abs/1909.03562>
- Hercher cycle result: <https://arxiv.org/abs/2201.00406>
- Rozier/Terracol paradoxical sequences: <https://arxiv.org/abs/2502.00948>
- Angeltveit verification algorithm: <https://arxiv.org/abs/2602.10466>
- Chang human-LLM Collatz exploration: <https://arxiv.org/abs/2603.11066>
- Barina verification project: <https://pcbarina.fit.vutbr.cz/>
- Local prior-art snapshot:
  `COLLATZ-LITERATURE-CCCHALLENGE-370-SNAPSHOT-2026-07-04.md`

## Final Operating Rule

The next genuinely special thing will not be "another reason Collatz should be
true." We already have hundreds. It will be a theorem or certificate that turns
one of these WTF residues into a separator:

```text
positive integers cannot remain in the 2-adic survivor frontier
```

Everything else is scaffolding.
