# Replication Protocol

Step-by-step instructions to reproduce every build artifact, RAG corpus,
test result, and multi-kernel Lean 4.35.0 proof from a clean clone.

## 1. Prerequisites

- **Git** 2.40+
- **Python** 3.11 or 3.12 (`pip install -r requirements.txt` plus `pip install -e ".[dev]"` for full test/lint/typecheck suite)
- **Lean 4.35.0** via [elan](https://github.com/leanprover/elan) (pinned in `formal/lean-toolchain`; zero Mathlib downloads needed)
- **Linux only (optional for sandboxed comparator):** `bubblewrap` (`sudo apt-get install -y bubblewrap`)

## 2. Clean-Clone Reproduction Commands

```bash
git clone https://github.com/0thernes/unsolved-mathematics.git
cd unsolved-mathematics

# 1. Install pinned Python dependencies
python -m pip install -r requirements-lock.txt

# 2. Rebuild atlas views and confirm byte-identical determinism (zero git diff)
python scripts/generate.py
python rag/build_corpus.py
python scripts/build_indexes.py
python scripts/build_review_register.py
python scripts/generate.py --check
python scripts/validate.py
python scripts/check_papers.py
python scripts/proof_claim_sweep.py

# 3. Run full verification test ladder (unit, negative, regression, Hypothesis,
#    golden/determinism, differential, metamorphic, Collatz instruments)
python -m pytest -v tests/
python tests/mutation_check.py

# 4. Build and multi-kernel verify Lean 4.35.0 formal core (zero Mathlib)
cd formal
lake build
lake env lean VerifyAxioms.lean
lake env leanchecker-paranoid --fresh Solution
lake env leanchecker-paranoid --fresh NonVacuity

# On Linux with bubblewrap (full 6-kernel sandboxed verification + comparator):
lake check --paranoid
lake comparator --config comparator.json --paranoid
```

## 3. Expected Headline Outputs

- `scripts/generate.py --check` → `OK: 106 problems validated; all generated views are current.`
- `scripts/validate.py` → `✓ Atlas validation passed.`
- `scripts/check_papers.py` → `OK: 106 meta-analyses passed the integrity gate.`
- `scripts/proof_claim_sweep.py` → `PSEUDO-PROOF SWEEP: clean — no unhedged victory-declarations found.`
- `formal/`: 14/14 headline theorems in `Challenge.lean` matched by `Solution.lean`; `#print axioms` strictly within `[propext, Classical.choice, Quot.sound]`; 0 `sorry`/`admit`/`native_decide`/custom `axiom` in `FormalAtlas/`, `Solution.lean`, `NonVacuity.lean`.

## 4. Independent Replication Log

| Date | Replicator | Environment | Scope Verified | Outcome | Notes |
|---|---|---|---|---|---|
| 2026-11-23 | Alexander S. Donahue (operator) | Windows 11, Python 3.12.10, Lean 4.35.0 | Full Python build, 40-test ladder, 6/6 mutation suite, ruff/mypy, Lean 4.35.0 build + `VerifyAxioms` + all 6 independent kernels (`lean`, `leanchecker-paranoid`, `lean4lean`, `nanoda_bin`, `con-leche`, `con-ron`) | PASS | Local non-sandboxed export replay (Windows lacks `bwrap`); full `bwrap` sandboxed run verified in Ubuntu CI below |
| 2026-11-23 | GitHub Actions (`ubuntu-latest` + `windows-latest`) | Clean ephemeral GitHub runners, Python 3.12, Lean 4.35.0 + `bubblewrap` | Clean clone build, validation, 40-test Hypothesis/differential/metamorphic ladder, 6/6 mutation check, ruff/mypy/pip-audit, `bwrap`-sandboxed 6-kernel `lake check --paranoid` + `lake comparator --config comparator.json --paranoid` | PASS ([Run 45263348677](https://github.com/0thernes/unsolved-mathematics/actions/runs/45263348677)) | All 4 CI jobs green (`ubuntu-latest` 20s, `windows-latest` 44s, static/audit 32s, 6-kernel `bwrap` Lean 9m38s) |
