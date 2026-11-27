# Threat Model

Evaluates adversarial, epistemic, and supply-chain failure modes relevant to an
independent AI-assisted mathematical research repository.

## Assets to Protect

1. **Epistemic integrity of mathematical claims** (preventing false "solved" claims, unverified citations presented as fact, or representational mismatch in Lean definitions).
2. **Logical soundness of `lean/`** (preventing hidden axioms, `sorry`, `native_decide`, kernel bugs, or signature drift between `Challenge.lean` and `Solution.lean`).
3. **Reproducibility & supply-chain integrity** (preventing tampered artifacts, unpinned dependencies, or silent data drift).

## Threats & Mechanical Mitigations

| # | Threat | Vector | Mechanical Mitigation |
|---|---|---|---|
| T1 | **AI pseudo-proof / overclaim injection** | Unhedged victory-declarations deposited in `problems/` or `meta-analyses/` | `scripts/proof_claim_sweep.py` (requires explicit non-proof disclaimers; bans attractor filenames) + `scripts/check_papers.py` (enforces AI banner & bans overclaims) |
| T2 | **Hallucinated or retracted DOIs / arXiv IDs** | LLM-generated plausible identifiers pointing to unrelated, nonexistent, or retracted papers | `scripts/verify_citations.py` queries live arXiv & Crossref APIs, checks title/author overlap, logs and purges mismatches; `scripts/check_retractions.py` audits all verified DOIs against Crossref & DataCite retraction metadata |
| T3 | **Lean kernel soundness bug or axiom smuggling** | Single-kernel bug (e.g. Lean #14576), `native_decide`, custom/private `axiom`, `implemented_by`, `@[extern]`, implicit variable capture | `autoImplicit = false` in `lean/lakefile.toml`, `lean/VerifyAxioms.lean`, `scripts/check_readme_axioms.py` (comment-stripped forbidden-token & Palomar gate), live 3-case negative rejection (`scripts/test_lean_negative.py`), and 6-kernel `lake check --paranoid` (`lean`, `leanchecker-paranoid`, `lean4lean`, `nanoda_bin`, `con-leche`, `con-ron`) |
| T4 | **Silent statement weakening / vacuity** | Formalizing a weaker or vacuously true definition that compiles in Lean | Isolated `lean/Challenge.lean` judged by `lake comparator --paranoid`, concrete witnesses in `lean/NonVacuity.lean`, explicit false-variant refutations in `lean/Adversarial.lean`, line-by-line `lean/STATEMENT_FIDELITY.md` |
| T5 | **Silent corpus/ranking corruption** | Duplicate RAG chunk IDs clobbering dense search; stale dossier ranks after registry edits; broken Markdown table columns or unlogged `verified` rows | `scripts/validate.py` checks global chunk-ID uniqueness, view freshness across all 120 dossiers, `VERSION` parity across 7 manifests (incl. RO-Crate & Croissant), and link integrity; `scripts/check_dossiers.py --strict` enforces 7-col `papers.md`, 5-col `mathematicians.md`, zero duplicate/bare IDs, 1-to-1 citation-log parity, and balanced `$` math delimiters |
| T6 | **Supply-chain / secret leakage** | Vulnerable Python deps or accidental credential commits | Report-only `pip-audit`, SHA-256-verified `gitleaks 8.30.1` + `osv-scanner 2.7.1` in CI; zero credentials required; `yaml.safe_load` only |
| T7 | **Post-hoc repository tampering** | Silent retroactive edits after claiming results | GitHub Actions SLSA build provenance (`actions/attest-build-provenance@v4`), `SHA256SUMS`, `data/MANIFEST.sha256`, dual DigiCert RFC 3161 (`.tsr`) + Bitcoin OpenTimestamps (`.ots`) proofs, and Software Heritage SWHID |
