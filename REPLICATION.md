# Replication Protocol

Step-by-step instructions to reproduce every build artifact, RAG corpus,
static proof blueprint, daily external-program mirror verification, AMS-LaTeX white paper, dual cryptographic timestamps, test result, and 6-kernel
Lean 4.35.0 proof from a clean clone (`v0.8.3`).

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
python scripts/sync_external_programs.py --check
python scripts/build_data_manifest.py --check
python scripts/timestamp_manifest.py --check
python scripts/test_lean_negative.py

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

- `scripts/generate.py --check` → `OK: 120 problems validated; all generated views are current.`
- `scripts/validate.py` → `✓ Atlas validation passed.`
- `scripts/check_dossiers.py --strict` → `Complete dossiers: 120/120  ->  data/dossier-status.json` (7-col `papers.md`, 5-col `mathematicians.md`, zero duplicate/bare IDs, 1-to-1 `verified` citation-log bijection, balanced `$` math)
- `scripts/check_papers.py` → `OK: 120 meta-analyses passed the integrity gate.`
- `scripts/proof_claim_sweep.py` → `PSEUDO-PROOF SWEEP: clean — no unhedged victory-declarations found.`
- `scripts/check_retractions.py --check` → `OK: data/retraction-audit.json clean — 287 verified DOIs audited, 0 retracted, 3 with publisher update/corrigendum notices, 0 errors.`
- `scripts/check_readme_axioms.py` → `OK: 102 declarations (66 comparator theorems) verified in README.md + lean/STATEMENT_FIDELITY.md; 15 Lean files satisfy Palomar limits & zero forbidden tokens.`
- `scripts/sync_external_programs.py --check` → `OK: full external program mirror verified offline — 26 programs, 62,790 targets, 62,790 mirrored items (27 shards, all <5 MB), solved_by_kind=(open: 326, known: 1322, warmup: 161), crosswalk 114/120`
- `scripts/timestamp_manifest.py --check` → `OK: Dual cryptographic timestamps verified offline against data/MANIFEST.sha256`
- `scripts/test_lean_negative.py` → `OK: All 3 live negative Lean 4.35.0 kernel & axiom-gate rejection checks PASSED.`
- `lean/`: `autoImplicit = false`; 66/66 headline theorems across 8 domains in `Challenge.lean` matched by `Solution.lean` + 16 witnesses in `NonVacuity.lean` + 20 refutations in `Adversarial.lean`; `#print axioms` strictly within `[propext, Classical.choice, Quot.sound]` (14 use zero axioms); 0 `sorry`/`admit`/`native_decide`/custom `axiom` outside `Challenge.lean`.

## 4. Independent Replication Log

| Date | Replicator | Environment | Scope Verified | Outcome | Notes |
|---|---|---|---|---|---|
| 2026-11-23 | Alexander S. Donahue (operator) | Windows 11, Python 3.12.10, Lean 4.35.0 | `v0.3.0`/`v0.3.1` Python build, 45-test ladder, 6/6 mutation, 14-theorem 6-kernel Lean replay | PASS | Local non-sandboxed replay; full `bwrap` verified in Ubuntu CI |
| 2026-11-23 | GitHub Actions (`ubuntu-latest` + `windows-latest`) | Ephemeral GitHub runners, Python 3.12, Lean 4.35.0 + `bwrap` | `v0.3.1` full CI + 6-kernel `bwrap` Lean + SLSA release | PASS ([CI 45275518493](https://github.com/0thernes/unsolved-mathematics/actions/runs/45275518493), [Release 45275528462](https://github.com/0thernes/unsolved-mathematics/actions/runs/45275528462)) | All 4 CI jobs + SLSA release green |
| 2026-11-25 | GitHub Actions (`ubuntu-latest` + `windows-latest`) | Ephemeral GitHub runners, Python 3.12, Lean 4.35.0 + `bwrap` | `v0.4.0` full CI (36-decl 6-kernel `bwrap` Lean + 55 tests + 6/6 mutation + Build Standard `v1.2.0` 100%) + SLSA release | PASS ([CI 45724228403](https://github.com/0thernes/unsolved-mathematics/actions/runs/45724228403), [Release 45724232811](https://github.com/0thernes/unsolved-mathematics/actions/runs/45724232811)) | All 4 CI jobs + SLSA release green (`f811c9b`) |
| 2026-11-25 | GitHub Actions (`ubuntu-latest` + `windows-latest`) | Ephemeral GitHub runners, Python 3.12, Lean 4.35.0 + `bwrap` | `v0.5.0` full CI (69-decl 8-domain 6-kernel `bwrap` Lean + 65 tests + 6/6 mutation + Build Standard `v1.2.0` 100%) + SLSA release + Pages | PASS ([CI 45742865067](https://github.com/0thernes/unsolved-mathematics/actions/runs/45742865067), [Release 45742871338](https://github.com/0thernes/unsolved-mathematics/actions/runs/45742871338), [Pages 45742865456](https://github.com/0thernes/unsolved-mathematics/actions/runs/45742865456)) | All 4 CI/Release/Pages workflows green (`0604df5`) |
| 2026-11-26 | GitHub Actions (`ubuntu-latest` + `windows-latest`) | Ephemeral GitHub runners, Python 3.12, Lean 4.35.0 + `bwrap` | `v0.6.0` full CI (81-decl 6-kernel `bwrap` Lean + 3/3 live neg rejection + dual `.tsr`/`.ots` + 70 tests + 6/6 mutation + Build Standard `v1.2.0` 100%) + SLSA release + Pages + SWH full snapshot | PASS ([CI 45829951418](https://github.com/0thernes/unsolved-mathematics/actions/runs/45829951418), [Release 45829958516](https://github.com/0thernes/unsolved-mathematics/actions/runs/45829958516), [Pages 45829951468](https://github.com/0thernes/unsolved-mathematics/actions/runs/45829951468)) | All 4 workflows green (`4ce816d`); Software Heritage `swh:1:snp:c11ec8263dd64b986c52bb400b8c3a85a3e6a254` |
| 2026-11-26 | Alexander S. Donahue (operator) | Windows 11, Python 3.12.10, Lean 4.35.0 (`eb6cafb7`), Tectonic 0.17.0 | `v0.7.0` 3-cycle `/goal` hardening: 102-decl 8-domain 6-kernel Lean replay, 3/3 live neg rejection, 0-warning visually inspected PDF + clean-room arXiv tarball, dual `.tsr` + `.ots`, 84 tests, 6/6 mutation, 19/19 `mypy`, `ruff` + `B023`, Build Standard `v1.2.0` 100.0% (`68/68`) | PASS ([CI 45940334677](https://github.com/0thernes/unsolved-mathematics/actions/runs/45940334677), [Release 45940340185](https://github.com/0thernes/unsolved-mathematics/actions/runs/45940340185)) | Local 6-kernel audit recorded in `lean/six_kernel_audit.txt`; Node 24 Ubuntu `bwrap` CI, `gitleaks`/`osv-scanner`, SLSA release & Pages deploy verified green |
| 2026-11-27 | GitHub Actions (`ubuntu-latest` + `windows-latest`) | Ephemeral GitHub runners, Python 3.12, Lean 4.35.0 + `bwrap` | `v0.8.1` full CI (120 curated problems, 59,396 daily-mirrored Left to Solve items across 26 `<4 MiB` shards, 102-decl 6-kernel `bwrap` Lean + 3/3 live neg rejection, zero-drift `rag/corpus.jsonl`, 87 tests, 6/6 mutation, 20/20 `mypy`) + Validate + Pages + SLSA release | PASS ([CI 45949011546](https://github.com/0thernes/unsolved-mathematics/actions/runs/45949011546), [Release 45949011416](https://github.com/0thernes/unsolved-mathematics/actions/runs/45949011416), [Pages 45949011485](https://github.com/0thernes/unsolved-mathematics/actions/runs/45949011485)) | All 4 workflows green (`8aeba1a`); immutable snapshot registered in `0thernes-research-archive` (`42a6081`) |
| 2026-11-27 | Alexander S. Donahue (operator) & GitHub Actions | Windows 11 & Ephemeral Linux runners, Python 3.12, Lean 4.35.0 (`eb6cafb7`), Tectonic 0.17.0 | `v0.8.2`–`v0.8.3` 3-cycle 10-subsystem hardening + live 26-program (`62,790` targets, `27` shards, `114/120` crosswalk, 4 unverified third-party agent-claim review signals) sync: 537/537 citation bijection, 287/287 DOIs 0 retracted, 95 tests, 10/10 mutants, `mypy --check-untyped-defs` 20/20, 0-warning PDF + clean-room arXiv tarball, 42-file SHA-256 + `.tsr`/`.ots` | PASS ([Release v0.8.2 46048510181](https://github.com/0thernes/unsolved-mathematics/actions/runs/46048510181), [Daily Sync 46043383151](https://github.com/0thernes/unsolved-mathematics/actions/runs/46043383151)) | `v0.8.2` (`15530ff`) merged cleanly with daily sync `510dc64` into `v0.8.3` on `main` |
