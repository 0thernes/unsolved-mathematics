# Collatz 104-Builder QA Rubric - 2026-07-04

## Source and Status

Input: user-supplied AGENTS-style framework, "The 104 Greatest: Developers,
Programmers, Engineers & Architects (1950s-2020s)."

Status: internal QA rubric only. This document does not validate the historical
ranking, does not cite the framework as academic evidence, and proves no part
of the Collatz conjecture. It converts the framework into repo rules for
research discipline, publication quality, and anti-overclaim review.

## Executive Verdict

The 104-builder framework helps if it is used as an operating discipline:

1. formalists demand exact theorem obligations;
2. systems builders demand boundaries, manifests, and reproducibility;
3. performance engineers demand measurements and independent reruns;
4. security and ethics thinkers demand threat models for false claims;
5. pragmatists demand small working tools before grand language;
6. educators demand clear explanations only after the math is honest.

It does not help if used as inspiration theater. No person, quote, paradigm, or
historical lineage is evidence for Collatz.

## Non-Negotiable Research Gates

Every new Collatz route must answer these before it is allowed into public
claim language:

| Gate | Required answer | Reject if |
|---|---|---|
| Claim class | `proved`, `checked-finite`, `computed`, `sampled`, `conjectural`, or `refuted` | The document uses theorem language without status. |
| Exact object | Map, residue class, parity word, affine block, cycle equation, or artifact | The method is named but no Collatz object is encoded. |
| Falsifier | Concrete counterexample shape or failing sibling/control system | No stated way to be wrong. |
| Checker | Script, proof certificate, proof assistant target, or manual derivation | Only narrative confidence is supplied. |
| Scope bound | Depth, modulus, start range, theorem hypotheses, or literature source | Finite evidence is presented as universal. |
| Repro artifact | Command, result path, hash/manifest entry, and expected summary | Output cannot be replayed. |
| Prior-art note | Literature anchor or explicit "not checked" status | Rediscovery is marketed as novelty. |

## Builder Lens Applied to This Repo

| Builder family | Collatz translation | Practical rule |
|---|---|---|
| Turing / Dijkstra / Knuth / Liskov / SPJ | Proof obligations, invariants, exact semantics | Write the theorem target before celebrating an experiment. |
| Hamilton / Schneier / Russell / Gebru-Buolamwini | Failure modes, safety, accountability | Treat every proof-looking AI artifact as hostile until checked. |
| Ritchie / Pike / Bellard | Minimal trusted kernels | Prefer a tiny verifier over a giant clever script. |
| Patterson-Hennessy / Gregg / McConnell | Measure, rerun, compare | Every table needs a command and an independent sanity check. |
| Torvalds / Hashimoto / Eghbal | Versioned public infrastructure | Keep manifests, hashes, CI gates, and maintainer-readable docs current. |
| Kay / Victor / Papert / Appleton | Human understanding | Visuals and metaphors are allowed only after claim status is explicit. |
| Conway / Vogels / Newman | Architecture mirrors process | Separate theorem docs, labs, results, unverified claims, and audits. |
| Beck / Fowler / Feathers | Refactor through tests | Improve experiments by adding characterization checks first. |
| Hoare / Stroustrup / Alexandrescu | Safety plus performance | Do not trade exact integer semantics for faster approximate models. |
| Ng / Karpathy / Howard | Data-centric iteration | Use models to propose hypotheses, never to certify the conjecture. |

## Method Selection Rule

The algorithm catalog and the 104-builder framework should be joined by this
one rule:

```text
method name -> Collatz object -> finite or formal obligation -> checker -> artifact
```

Examples:

| Method | Acceptable route | Unacceptable route |
|---|---|---|
| SAT/SMT | Encode a bounded retimed-pressure lemma and emit model/UNSAT certificate. | "SAT is powerful, so the proof is close." |
| BDD/ZDD | Compress survivor-frontier sets and match exact DP counts. | Visualize a large tree and call it structure. |
| E-graphs | Normalize affine block identities and expose missing hypotheses. | Rewrite until a desired formula appears. |
| CEGAR | Refine an abstract bad trace against exact Collatz replay. | Treat an abstraction as the true orbit space. |
| MCTS/search | Find hard residues or counterexamples to local claims. | Infer universal truth from no found counterexample. |
| ML/statistics | Prioritize experiments and detect anomalies. | Relabel fitted contraction as theorem. |

## Current Quality Benchmark

For the present Collatz repo, "cutting edge" should be claimed only in this
narrow sense:

| Axis | Current honest rating | Meaning |
|---|---:|---|
| Collatz proof value | 2/10 | Useful structure and falsification, no proof of the conjecture. |
| Finite verification discipline | 7/10 | Strong scripts/results exist, but coverage and certificates need hardening. |
| AI-research workflow novelty | 8/10 | The adversarial audit, quarantine, and multi-model failure ledger are rare and valuable. |
| Public reproducibility | 6/10 | Manifests and CI exist, but the dirty research front still needs scoped publication. |
| Academic readiness | 5/10 | Promising as a case study, not ready as a math breakthrough paper. |
| Overclaim control | 7/10 | The repo has explicit open-status language and pseudo-proof gates; keep strengthening them. |

## Immediate QA Requirements for New Work

1. Any "solved", "closed", "complete", or "proved" wording must cite a
   machine-checkable theorem artifact or be rejected by proof-claim sweep.
2. Any bounded computation must print its bound in the result and in the doc.
3. Any heuristic search result must include a counterexample/falsification
   role, not proof language.
4. Any new mechanism claim must be run on at least one sibling/control map.
5. Any algebraic identity used in a proof sketch should be routed through an
   affine normal form or explicit derivation.
6. Any public-facing novelty claim must separate:
   - new to this repo;
   - new as workflow;
   - new as Collatz mathematics;
   - not new / rediscovered.

## Publication Standard

A future paper or repo release may cite this rubric only as internal method
governance. It should not cite the 104-builder framework as a source of
mathematical authority.

The publishable standard is:

```text
open problem status first
claim class attached
artifact path attached
checker attached
prior art checked
overclaim language removed
```

Anything weaker can still be useful research work, but it should stay in
experiments or unverified-claims until it earns a stronger status.
