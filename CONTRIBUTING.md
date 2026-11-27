# 🤝 Contributing to the Unsolved Mathematics Atlas

Thank you for helping build a rigorous, honest, and machine-verified map of mathematics' open frontier.

## High-Impact Contributions

1. **Verify primary-source citations (highest impact):**
   Promote remaining `needs-verification`, `high-confidence`, or `ai-suggested` entries in `problems/*/papers.md` by confirming live DOI/arXiv resolution and matching author/title/year (`python scripts/verify_citations.py --slug <slug> --apply`). See [`docs/methodology/SOURCING.md`](docs/methodology/SOURCING.md).
2. **Academic mathematician review:**
   Audit any problem dossier or meta-analysis and open an **Academic Review Request** issue via `.github/ISSUE_TEMPLATE/academic-review-request.yml`. See [`docs/review/ACADEMIC-REVIEW.md`](docs/review/ACADEMIC-REVIEW.md).
3. **Extend the Lean 4.35.0 formal core (`lean/`):**
   Formalize additional structural lemmas, classical foundations, finite cases, or barrier meta-theorems in pure Lean 4.35.0 Core (`autoImplicit = false`) with zero `sorry`/`admit`/`native_decide`/custom `axiom`, standard axioms only (`VerifyAxioms.lean`), concrete witnesses (`NonVacuity.lean`), adversarial refutations (`Adversarial.lean`), and `STATEMENT_FIDELITY.md` correspondence.
4. **Update live mathematical frontiers or refine rankings:**
   Update `data/problems.yaml` (must satisfy `schema/problem.schema.json`) and regenerate all views cleanly.

## Ground Rules

- **Honesty is non-negotiable.** Never fabricate an identifier or overclaim an open problem as solved. Every finding is strictly classified under the ten Build Standard `v1.2.0` classes (`bug`, `error`, `issue`, `problem`, `concern`, `dilemma`, `conflict`, `gap`, `hole`, `blindspot`).
- **Never hand-edit generated files:** `data/problems.json`, `RANKING.md`, `docs/indexes/*.md`, the `README.md` ranking table, `rag/corpus.jsonl`, and `data/MANIFEST.sha256` are produced deterministically by the build scripts.
- **No unhedged proof claims:** `scripts/proof_claim_sweep.py` flags unhedged victory declarations across all active prose in CI.

## Local Workflow (Straight-to-`main` per Build Standard R2)

```bash
python -m pip install -r requirements-lock.txt

# Rebuild all derived views and tamper-evidence manifest
python scripts/generate.py
python scripts/build_indexes.py
python rag/build_corpus.py
python scripts/build_site.py
python scripts/build_data_manifest.py

# Run full verification gate before pushing to main
python scripts/generate.py --check
python scripts/validate.py
python scripts/check_dossiers.py --strict
python scripts/check_papers.py
python scripts/proof_claim_sweep.py
python scripts/check_retractions.py --check
python scripts/check_readme_axioms.py
python scripts/build_data_manifest.py --check
python scripts/timestamp_manifest.py --check
python -m pytest -v tests/
python tests/mutation_check.py
```

For Lean 4 changes in `lean/`:
```bash
cd lean
lake build Challenge Solution NonVacuity Adversarial
lake env lean VerifyAxioms.lean
python ../scripts/test_lean_negative.py
# On Linux with bubblewrap:
lake check --paranoid
lake comparator --config comparator.json --paranoid
```

## Commit & Issue Conventions

- **Direct commits to `main`:** Small, scoped commits directly on `main` (no pull-request templates, no long-lived unmerged feature branches). External contributors should file issues using `.github/ISSUE_TEMPLATE/` forms (`finding.yml`, `verification.yml`, `new-problem.yml`, `academic-review-request.yml`).
- **Conventional prefixes:** `feat:`, `fix:`, `verify:`, `formal:`, `dossier:`, `docs:`, `ci:`, `chore:`.
- **Code of Conduct:** Be rigorous and be kind. See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
