# Threat Model

Evaluates adversarial, epistemic, and supply-chain failure modes relevant to an
independent AI-assisted mathematical research repository.

## Assets to Protect

1. **Epistemic integrity of mathematical claims** (preventing false "solved" claims, unverified citations presented as fact, or representational mismatch in Lean definitions).
2. **Logical soundness of `formal/`** (preventing hidden axioms, `sorry`, `native_decide`, kernel bugs, or signature drift between `Challenge.lean` and `Solution.lean`).
3. **Reproducibility & supply-chain integrity** (preventing tampered artifacts, unpinned dependencies, or silent data drift).

## Threats & Mechanical Mitigations

| # | Threat | Vector | Mechanical Mitigation |
|---|---|---|---|
| T1 | **AI pseudo-proof / overclaim injection** | Unhedged victory-declarations deposited in `problems/` or `meta-analyses/` | `scripts/proof_claim_sweep.py` (requires explicit non-proof disclaimers; bans attractor filenames) + `scripts/check_papers.py` (enforces AI banner & bans overclaims) |
| T2 | **Hallucinated DOIs / arXiv IDs** | LLM-generated plausible identifiers pointing to unrelated or nonexistent papers | `scripts/verify_citations.py` queries live arXiv & Crossref APIs, checks title/author overlap, logs and purges mismatches |
| T3 | **Lean kernel soundness bug or axiom smuggling** | Single-kernel bug (e.g. Lean #14576), `native_decide`, custom `axiom`, or macro injection | `formal/VerifyAxioms.lean` + forbidden-token grep + 6-kernel `lake check --paranoid` (`lean`, `leanchecker-paranoid`, `lean4lean`, `nanoda`, `con-leche`, `con-ron`) |
| T4 | **Silent statement weakening / vacuity** | Formalizing a weaker or vacuously true definition that compiles in Lean | Isolated `formal/Challenge.lean` judged by `lake comparator --paranoid`, concrete witnesses in `formal/NonVacuity.lean`, line-by-line `formal/STATEMENT_FIDELITY.md` |
| T5 | **Silent corpus/ranking corruption** | Duplicate RAG chunk IDs clobbering dense search; stale dossier ranks after registry edits | `scripts/validate.py` checks global chunk-ID uniqueness, view freshness across all 106 dossiers, `VERSION` parity, and link integrity |
| T6 | **Supply-chain / secret leakage** | Vulnerable Python deps or accidental credential commits | Report-only `pip-audit` + secret-pattern scan in CI; zero credentials required; `yaml.safe_load` only |
| T7 | **Post-hoc repository tampering** | Silent retroactive edits after claiming results | GitHub Actions SLSA build provenance (`actions/attest-build-provenance@v2`), `SHA256SUMS`, `data/MANIFEST.sha256`, Software Heritage SWHID |
