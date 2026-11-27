# The Unsolved Mathematics Atlas — cross-platform task runner (Build Standard v1.2.0 A31, B01)
# Usage: just <recipe>

py := env_var_or_default("PY", "python")

default:
    @just --list

setup:
    {{py}} -m pip install -r requirements.txt

build:
    {{py}} scripts/generate.py

corpus:
    {{py}} rag/build_corpus.py

index:
    {{py}} scripts/build_indexes.py

register:
    {{py}} scripts/build_review_register.py

site:
    {{py}} scripts/build_site.py

check:
    {{py}} scripts/generate.py --check
    {{py}} scripts/validate.py
    {{py}} scripts/check_dossiers.py --strict
    {{py}} scripts/check_papers.py
    {{py}} scripts/proof_claim_sweep.py
    {{py}} scripts/check_retractions.py --check
    {{py}} scripts/check_readme_axioms.py
    {{py}} scripts/build_data_manifest.py --check
    {{py}} scripts/timestamp_manifest.py --check

test:
    {{py}} -m pytest -q tests/

formal:
    cd lean && lake build Challenge Solution NonVacuity Adversarial && lake env lean VerifyAxioms.lean && lake check --paranoid && lake comparator --config comparator.json --paranoid
    {{py}} scripts/test_lean_negative.py

formal-nosandbox:
    cd lean && lake build Challenge Solution NonVacuity Adversarial && lake env lean VerifyAxioms.lean && lake env leanchecker-paranoid --fresh Solution && lake env leanchecker-paranoid --fresh NonVacuity && lake env leanchecker-paranoid --fresh Adversarial
    {{py}} scripts/test_lean_negative.py

lint:
    ruff check scripts rag tests examples || true
    ruff check --select E9,F63,F7,F82,B023 problems/collatz-conjecture/experiments || true
    mypy --explicit-package-bases scripts rag examples || true

mutate:
    {{py}} tests/mutation_check.py

verify-citations:
    {{py}} scripts/verify_citations.py
    {{py}} scripts/check_retractions.py

reproduce: setup build corpus index register site check test mutate formal-nosandbox
    @echo "Reproduction complete."

audit:
    pwsh -File scripts/Audit-Repo.ps1 -Path .
