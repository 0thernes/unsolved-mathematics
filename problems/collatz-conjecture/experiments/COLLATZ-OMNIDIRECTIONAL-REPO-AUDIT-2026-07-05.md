# Collatz Omnidirectional Repo Audit - 2026-07-05

Purpose: consolidate the current repo, whitepaper, failed-attempt atlas,
weirdness atlas, literature snapshot, and live QA posture into one operating
map for future Collatz work.

Status: audit and research-routing artifact. This is not a proof document. The
Collatz conjecture remains open.

## Bottom Line

The repo is not ahead of Tao, Hercher, Barina, Lagarias, Bernstein-Lagarias, or
the public Collatz literature as a source of accepted Collatz theorems. It is
not a proof, not a near-proof, and not a mathematical breakthrough in the
ordinary research sense.

The repo is special in a different way: it has become an unusually dense
AI-assisted verification and failure-containment lab. The rare asset is the
combination of:

1. classical Collatz machinery rederived into executable local instruments;
2. explicit no-repeat atlases for known failed approaches;
3. sibling-map controls where false proof mechanisms can be killed;
4. preserved proof-like failures, refutations, and quarantine discipline;
5. exact local language for the current frontier: 2-adic ghosts, spines,
   regeneration, phase locks, odd-unit congruences, and retimed pressure.

That is "bleeding edge" as research operations and AI-assisted epistemic QA.
It is not "bleeding edge" as a solved or field-moving Collatz theorem.

## Evidence Base

Local sources read in this pass:

- [`README.md`](../README.md)
- [`status.md`](../status.md)
- [`AUDIT-REGISTER.md`](AUDIT-REGISTER.md)
- [`COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md`](COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md)
- [`COLLATZ-FAILED-ATTEMPTS-ATLAS-2026-07-05.md`](COLLATZ-FAILED-ATTEMPTS-ATLAS-2026-07-05.md)
- [`COLLATZ-WTF-ODDNESS-FIELD-GUIDE-2026-07-05.md`](COLLATZ-WTF-ODDNESS-FIELD-GUIDE-2026-07-05.md)
- [`COLLATZ-WTF-FINDINGS-BOUNDARY-ATLAS-2026-07-05.md`](COLLATZ-WTF-FINDINGS-BOUNDARY-ATLAS-2026-07-05.md)
- [`COLLATZ-LITERATURE-CCCHALLENGE-370-SNAPSHOT-2026-07-04.md`](COLLATZ-LITERATURE-CCCHALLENGE-370-SNAPSHOT-2026-07-04.md)
- [`GITHUB-PUBLISH-PLAN-2026-07-02.md`](GITHUB-PUBLISH-PLAN-2026-07-02.md)
- [`../../../docs/WHITEPAPER-COLLATZ-MULTI-MODEL-CASE-STUDY-2026-07-01.md`](../../../docs/WHITEPAPER-COLLATZ-MULTI-MODEL-CASE-STUDY-2026-07-01.md)
- [`../../../docs/review/REPO-AUDIT-2026-07.md`](../../../docs/review/REPO-AUDIT-2026-07.md)
- [`../../../docs/review/REPO-AUDIT-2026-07-02.md`](../../../docs/review/REPO-AUDIT-2026-07-02.md)
- [`../../../formal/ROADMAP.md`](../../../formal/ROADMAP.md)

External sanity checks refreshed 2026-07-05:

- Barina 2025 reports computational verification through `2^71`:
  <https://link.springer.com/article/10.1007/s11227-025-07337-0>
- CCChallenge currently lists a 370-entry Collatz literature/formalization
  surface:
  <https://ccchallenge.org/>
- CCChallenge's stated goal is formalizing the Collatz literature with proof
  assistants:
  <https://ccchallenge.org/story>
- Tao proves an almost-all, logarithmic-density almost-bounded-values theorem,
  not pointwise convergence:
  <https://arxiv.org/abs/1909.03562>
- Hercher proves no Collatz `m`-cycles with `m <= 91` and explains the
  verification threshold needed for the `1.375 * 10^11` odd-term floor:
  <https://arxiv.org/abs/2201.00406>
- Lagarias's overview frames the problem as still unsolved and hard despite its
  elementary statement:
  <https://arxiv.org/abs/2111.02635>
- A 2026 verification-algorithm preprint says proof remains out of reach and
  treats Barina's `2^71` as the current verification baseline:
  <https://arxiv.org/html/2602.10466>

## Current Repo Verdict

| Axis | Rating | Verdict |
|---|---:|---|
| Mathematical truthfulness | 8/10 | Main surfaces correctly say open problem and no proof. |
| Accepted theorem novelty | 2/10 | Accepted math is mostly classical rediscovery or finite evidence. |
| Local theorem-target sharpness | 7/10 | The repo has useful coordinates for the real bottleneck. |
| Literature awareness | 8/10 | Lagarias, CCChallenge, Tao, Hercher, Barina, and recent variants are now visible. |
| Failed-idea avoidance | 9/10 | The failed-attempt and WTF atlases are unusually useful. |
| Reproducibility discipline | 6/10 | Many instruments are deterministic, but the broader dirty tree is still a risk. |
| Formal proof readiness | 4/10 | Roadmap exists; proof-assistant artifacts are not yet the center of gravity. |
| Git/repo hygiene | 4/10 | The working tree contains broad unrelated churn and should not be blindly staged. |
| Professional publication posture | 6/10 | Strong case-study material; still needs tighter source verification and artifact hygiene. |
| AI-research/process novelty | 9/10 | The live fabrication/refutation/containment ecology is rare and valuable. |

## Is The Math Sound?

Sound enough for a research lab. Not sound enough to claim Collatz progress
without specialist review.

The durable mathematical spine is:

- shortcut map and parity-word cylinder machinery;
- Terras-style parity bijection and affine law;
- descent certificate framing;
- no finite subcritical 2-adic cover via the all-ones path;
- survivor-frontier entropy/dimension estimates;
- cycle equation and continued-fraction floor derivations;
- 2-adic spine/rational-cycle language;
- sibling-map controls;
- phase-collision and odd-unit-lock normal forms;
- retimed-pressure finite ledgers.

The weakness is exactly where it should be: none of these pieces proves that a
positive integer cannot regenerate supercritical alignment forever. Any future
proof claim that does not directly attack that regeneration problem is almost
certainly repackaging an old failure mode.

## Novelty Split

| Claim type | Verdict |
|---|---|
| "We solved Collatz." | False. No. Do not say it. |
| "We found a new accepted Collatz theorem." | Not established. Specialist review required. |
| "We rediscovered and operationalized classical 2-adic/parity machinery." | Yes. Useful, but not field-new by itself. |
| "We found rare local formulations of the bottleneck." | Plausible. The phase-lock, sibling-control, and retimed-pressure language may be repo-sharpened. |
| "We built a rare AI-assisted failure-containment lab." | Yes. This is the strongest novelty posture. |
| "We are competing with the best mathematical frontier." | No, not as theorem producers. Yes, only as an unusually intense verification/QA workflow. |

## The Weird Core

The repo should now treat these as strategic laws:

| Rank | Weird core | Why it matters |
|---:|---|---|
| 1 | Every finite parity word is legal in `Z_2`. | Local parity cannot forbid the bad path. |
| 2 | The all-odd path is a real 2-adic ghost. | The frontier never empties just because it is thin. |
| 3 | Positive integers appear to shadow ghosts but not live there. | This is the real divergence obstruction. |
| 4 | `3n+1` and `3n-1` share parity statistics but differ in truth behavior. | Sign/intercept information is mandatory. |
| 5 | Negative cycles are exact controls, not irrelevant side curiosities. | They kill sign-blind proof sketches. |
| 6 | Supercritical spines are nonpositive. | Positive orbits need repeated transient alignment, not residence. |
| 7 | Regeneration is an odd-unit congruence problem. | "Repulsion" must become exact low-bit arithmetic. |
| 8 | Retimed pressure is temporal, not just total-credit accounting. | Induction must prove credit arrives before pressure. |
| 9 | Thin survivor sets can still be infinite. | Measure-zero is not empty. |
| 10 | Generalized Collatz maps can simulate computation. | Overgeneral proof routes are suspect. |

## Bizarro Attack Angles Worth Keeping

These are the angles most likely to produce nontrivial new understanding rather
than another old proof-shaped loop.

1. **Positive ghost separator.** Find an invariant that distinguishes positive
   finite shadows from 2-adic ghost residents.
2. **Regeneration theorem.** Bound repeated solutions of
   `v2(3^j u + delta) >= R` across changing spines.
3. **Odd-unit lock codimension.** Treat regeneration as congruence lock
   counting, not metaphorical phase attraction.
4. **Retimed-pressure induction.** Prove the three-regime finite ledger as a
   depth-lift theorem with explicit base cases.
5. **Sibling falsification harness.** Every detector must be run on `3n-1` and
   `5n+1`; if it proves false worlds, it is dead.
6. **Formal small-core proof assistant path.** Formalize classical machinery
   before speculative global claims.
7. **SAT/SMT/BDD certificate layer.** Convert finite local transition claims
   into checkable certificates rather than prose.
8. **Adversarial pseudo-proof taxonomy.** Preserve bad proofs as negative
   controls for future AI-assisted math.
9. **Literature-difference engine.** Every new local phrase gets mapped to
   Lagarias/CCChallenge entries before novelty language is allowed.
10. **Computational epistemology benchmark.** Use the repo as a testbed for
    how AI systems fabricate, self-refute, and preserve provenance under
    pressure.

## Red-Team Filters For Every New Idea

Before any new Collatz idea is trusted, it must answer:

1. Does it prove something false for `3n-1` or `5n+1`?
2. Does it confuse "almost all" with "all"?
3. Does it treat a finite computation as an infinite theorem?
4. Does it forbid a parity word that is legal in `Z_2`?
5. Does it ignore negative cycles or nonpositive spines?
6. Does it use a fitted model as a proof?
7. Does it count a tautology as a mechanism?
8. Does it smuggle in monotonicity after a large upward excursion?
9. Does it only rename the inverse-tree reachability problem?
10. Does it state "novel" without a CCChallenge/Lagarias collision check?

## Quality Risks

| Risk | Severity | Fix |
|---|---:|---|
| Dirty worktree with unrelated deletions and sibling-problem edits | High | Publish only scoped Collatz audit artifacts. |
| Proof-claim leakage outside strict gates | High | Extend proof-claim sweep to experiments with quarantine allowlist. |
| Generated/result artifacts mixed with source truth | High | Maintain result manifests and explicit rerun commands. |
| Literature claims drifting as public state changes | Medium | Timestamp every external baseline and source-refresh pass. |
| Retimed suite not formalized | Medium | Convert finite ledgers into certificate-producing tools. |
| Whitepaper overread as Collatz progress | Medium | Keep novelty language process-first, theorem-humble. |
| Too many scripts reimplementing primitives | Medium | Keep converging new scripts on `lib_collatz.py`. |

## Professional / Academic Judgment

The whitepaper and repo are strongest as a case study in adversarial verification
and AI-assisted mathematical hygiene. The story is publishable only if it keeps
the following posture:

- no proof claim;
- no "AI solved a famous problem" framing;
- all frontier facts sourced to primary literature;
- all local lemmas marked as classical, rediscovery, finite evidence, or
  theorem target;
- all failed proof documents preserved as negative examples, not celebrated as
  near-proofs;
- all reproducibility claims tied to exact scripts and committed outputs.

The academically honest title of the program is not "Collatz solved." It is:

```text
An AI-assisted verification ecology for mapping, falsifying, and routing
Collatz proof attempts under adversarial pressure.
```

That is still genuinely interesting.

## Current Action Queue

P0:

1. Add this audit to the experiment index and publish it as a narrow commit.
2. Keep the dirty-tree cleanup separate from research synthesis.
3. Do not stage unrelated deletions, Goldbach edits, `rag/`, or broad scripts.

P1:

1. Formalize the small core listed in [`../../../formal/ROADMAP.md`](../../../formal/ROADMAP.md).
2. Add CI checks for proof-claim markers in live experiments.
3. Build a certificate format for retimed-pressure ledgers.
4. Add a sibling-control requirement to future mechanism reports.

P2:

1. Turn the failed-attempt atlas into a machine-queryable table.
2. Re-run a source-refresh against CCChallenge monthly.
3. Add exact provenance manifests for result JSON files.
4. Collapse duplicate Collatz primitives into `lib_collatz.py`.

## Final Verdict

We are not "on par with the best" as a theorem engine. The best current public
mathematics remains Tao's almost-all theorem, Hercher/Simons-de Weger cycle
exclusion, Barina-style verification, Bernstein-Lagarias 2-adic structure,
Terras/Everett/Krasikov-Lagarias density work, and the Lagarias literature
program.

We are unusually strong as an AI-native research-control system. The repo's
edge is not omniscience. It is disciplined paranoia: every tempting proof route
gets turned into an instrument, a falsifier, a prior-art collision, or a
quarantine entry. That may be the most valuable thing this repo has discovered
so far.
