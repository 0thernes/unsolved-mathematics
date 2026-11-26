# Replication Protocol

Step-by-step instructions to reproduce every build artifact, RAG corpus,
static proof blueprint, AMS-LaTeX white paper, test result, and 6-kernel
Lean 4.35.0 proof from a clean clone (`v0.5.0`).

## 1. Prerequisites

- **Git** 2.40+
- **Python** 3.11 or 3.12 (`pip install -r requirements-lock.txt`)
- **Lean 4.35.0** via [elan](https://github.com/leanprover/elan) (pinned in `lean/lean-toolchain`; zero Mathlib downloads needed)
- **Linux only (for sandboxed comparator):** `bubblewrap` (`sudo apt-get install -y bubblewrap`)
- **Optional (white paper PDF recompilation):** `tectonic` 0.15+ (or TeX Live `pdflatex` + `bibtex`)

## 2. Clean-Clone Reproduction Commands

```bash
git clone https://github.com/0thernes/unsolved-mathematics.git
cd unsolved-mathematics

# 1. Install pinned Python dependencies
python -m pip install -r requirements-lock.txt

# 2. Rebuild atlas views, indexes, site + blueprint and confirm zero drift
python scripts/generate.py
python rag/build_corpus.py
python scripts/build_indexes.py
python scripts/build_review_register.py
python scripts/build_site.py
python scripts/generate.py --check
python scripts/validate.py
python scripts/check_dossiers.py --strict
python scripts/check_papers.py
python scripts/proof_claim_sweep.py
python scripts/check_retractions.py --check
python scripts/check_readme_axioms.py
python scripts/build_data_manifest.py --check

# 3. Run full verification test ladder + mutation check
python -m pytest -v tests/
python tests/mutation_check.py

# 4. Build and multi-kernel verify Lean 4.35.0 formal core (zero Mathlib)
cd lean
lake build Challenge Solution NonVacuity Adversarial
lake env lean VerifyAxioms.lean
lake env leanchecker-paranoid --fresh Solution
lake env leanchecker-paranoid --fresh NonVacuity
lake env leanchecker-paranoid --fresh Adversarial

# On Linux with bubblewrap (full 6-kernel sandboxed verification + comparator):
lake check --paranoid
lake comparator --config comparator.json --paranoid

# 5. Recompile AMS-LaTeX white paper (optional, requires tectonic)
cd ../paper && tectonic -X compile Donahue_2026_unsolved_mathematics_atlas.tex
```

## 3. Expected Headline Outputs

- `scripts/generate.py --check` → `OK: 106 problems validated; all generated views are current.`
- `scripts/validate.py` → `✓ Atlas validation passed.`
- `scripts/check_papers.py` → `OK: 106 meta-analyses passed the integrity gate.`
- `scripts/proof_claim_sweep.py` → `PSEUDO-PROOF SWEEP: clean — no unhedged victory-declarations found.`
- `scripts/check_retractions.py --check` → `OK: data/retraction-audit.json clean — 220 verified DOIs audited, 0 retracted, 3 with publisher update/corrigendum notices, 0 errors.`
- `scripts/check_readme_axioms.py` → `OK: 69 declarations (45 comparator theorems) verified in README.md + lean/STATEMENT_FIDELITY.md; 15 Lean files satisfy Palomar limits & zero forbidden tokens.`
- `lean/`: 45/45 headline theorems across 8 domains in `Challenge.lean` matched by `Solution.lean` + 10 witnesses in `NonVacuity.lean` + 14 refutations in `Adversarial.lean`; `#print axioms` strictly within `[propext, Classical.choice, Quot.sound]` (12 use zero axioms); 0 `sorry`/`admit`/`native_decide`/custom `axiom` outside `Challenge.lean`.

## 4. Independent Replication Log

| Date | Replicator | Environment | Scope Verified | Outcome | Notes |
|---|---|---|---|---|---|
| 2026-11-23 | Alexander S. Donahue (operator) | Windows 11, Python 3.12.10, Lean 4.35.0 | `v0.3.0`/`v0.3.1` Python build, 45-test ladder, 6/6 mutation, 14-theorem 6-kernel Lean replay | PASS | Local non-sandboxed replay; full `bwrap` verified in Ubuntu CI |
| 2026-11-23 | GitHub Actions (`ubuntu-latest` + `windows-latest`) | Ephemeral GitHub runners, Python 3.12, Lean 4.35.0 + `bwrap` | `v0.3.1` full CI + 6-kernel `bwrap` Lean + SLSA release | PASS ([CI 45275518493](https://github.com/0thernes/unsolved-mathematics/actions/runs/45275518493), [Release 45275528462](https://github.com/0thernes/unsolved-mathematics/actions/runs/45275528462)) | All 4 CI jobs + SLSA release green |
| 2026-11-25 | GitHub Actions (`ubuntu-latest` + `windows-latest`) | Ephemeral GitHub runners, Python 3.12, Lean 4.35.0 + `bwrap` | `v0.4.0` full CI (36-decl 6-kernel `bwrap` Lean + 55 tests + 6/6 mutation + Build Standard `v1.2.0` 100%) + SLSA release | PASS ([CI 45724228403](https://github.com/0thernes/unsolved-mathematics/actions/runs/45724228403), [Release 45724232811](https://github.com/0thernes/unsolved-mathematics/actions/runs/45724232811)) | All 4 CI jobs + SLSA release green (`f811c9b`) |
| 2026-11-25 | Alexander S. Donahue (operator) | Windows 11, Python 3.12.10, Lean 4.35.0, Tectonic 0.17.0 | `v0.5.0` Cycle 4 deep refinement: 69-decl 8-domain 6-kernel Lean replay, 10-page 0-warning PDF + clean-room arXiv tarball, FAIR RO-Crate/Croissant, 65-test ladder, 6/6 mutation, `ruff`/`mypy`, Build Standard `v1.2.0` 100.0% (`68/68`) | PASS | Local 6-kernel audit recorded in `lean/six_kernel_audit.txt`; full Ubuntu `bwrap` CI + Pages deploy verified upon push to `main` |
