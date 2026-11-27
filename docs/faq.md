# Frequently Asked Questions (`docs/faq.md`)

## 1. Does this repository claim to solve any open mathematical conjecture?

**No.** Every open problem in the 106-problem catalog remains open unless the external mathematical community has produced a verifiable resolution (such as `unit-distance-problem`, updated to `recently-resolved` with explicit peer-review caveats following the May 2026 disproof `arXiv:2605.20695`). The Lean 4.35.0 formal core in `lean/` proves **structural lemmas, classical foundations, and finite cases** — never full solutions of open conjectures. Its Collatz "$\varepsilon$-invariance" theorem (`thm_collatz_epsilon_invariance_barrier`) records facts about the $3n-1$ map; the methodological reading drawn from it is a heuristic, not a formalized meta-theorem. See [`CLAIMS.md`](../CLAIMS.md) and [`LIMITATIONS.md`](../LIMITATIONS.md).

## 2. Why is `problems/collatz-conjecture/` so much larger than the other 105 dossiers?

In July 2026, `unsolved-mathematics` served as the live workspace for a multi-model research & QA case study on Collatz (`docs/WHITEPAPER-COLLATZ-MULTI-MODEL-CASE-STUDY-2026-07-01.md`), generating ~58.5 MB of experimental scripts, certificates, and quarantined refuted sketches. This asymmetry is intentionally documented as **Dilemma D1** in [`docs/reviews/2026-11-23-forensic-philosophical-audit.md`](reviews/2026-11-23-forensic-philosophical-audit.md) and tracked for clean modular separation in `ROADMAP.md`.

## 3. What do the citation verification flags in `problems/*/papers.md` mean?

- `verified`: Identifier (arXiv ID or DOI) was queried live against `export.arxiv.org` or `api.crossref.org` and matched author/title/year (`data/citation-verification-log.json`).
- `high-confidence`: Foundational or classic reference without an audited identifier in our automated pass yet (e.g., pre-DOI 18th–20th century papers or books).
- `needs-verification`: Either no identifier has been verified yet, or an automated audit detected and stripped an invalid/mismatched identifier rather than leaving a poisoned link.
- `ai-suggested`: Suggested during LLM literature drafting; treat as a lead to verify before citing.

## 4. How many AI models and human mathematicians have reviewed the 106 dossiers?

As of `v0.7.0` (`2026-11-26`): **1 AI model pass** (Claude's in-house self-review on `2026-06-14`, recorded under the historical non-canonical session label `claude-opus-4-8` in `meta-analyses/*.md`) across the 106 meta-analyses and **0 independent human mathematician peer reviews**. Earlier README text mentioning a "four-model review panel" described a planned architecture, not completed reviews; `v0.3.0`+ corrects this disclosure explicitly across `README.md`, `CLAIMS.md`, and `LIMITATIONS.md`.

## 5. How is the Composite Severity Score (CSS) computed? Is it objective?

No — CSS is a transparent, deterministic **editorial heuristic** defined in [`docs/methodology/RANKING.md`](methodology/RANKING.md) combining difficulty, inverse tractability, centrality, age (`CURRENT_YEAR = 2026`), and status. Ties break deterministically by alphabetical `slug`. It exists to organize study, never to pronounce objective mathematical value.

## 6. How do I run the Lean 4.35.0 formal proofs and all 6 independent kernels?

See [`REPLICATION.md`](../REPLICATION.md) and [`lean/STATEMENT_FIDELITY.md`](../lean/STATEMENT_FIDELITY.md). In short:
```bash
cd lean
lake build Challenge Solution NonVacuity Adversarial
lake env lean VerifyAxioms.lean
# On Linux (with bubblewrap / bwrap installed):
lake check --paranoid
lake comparator --config comparator.json --paranoid
```
On Windows, Lean 4.35.0's `lake check` currently hits an upstream `git` PATH check and lacks `bwrap`; run the bundled kernel binaries (`leanchecker-paranoid`, `lean4lean --import`, `con-leche --verified`, `con-ron --verified`, `nanoda_bin`) directly on exported artifacts, or inspect the live Ubuntu CI run where all 6 kernels run inside `bwrap`.

## 7. Why does `CITATION.cff` list Alexander S. Donahue as an independent researcher rather than an LLC?

No legal LLC entity has been formed as of November 2026. In keeping with our strict factual-accuracy standard, `CITATION.cff`, `.zenodo.json`, and all companion papers list the author accurately as `Alexander S. Donahue` (independent researcher, ORCID `0009-0006-8168-9648`).
