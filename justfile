# The Unsolved Mathematics Atlas — cross-platform task runner (Build Standard A31, B01)
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

check:
    {{py}} scripts/generate.py --check
    {{py}} scripts/validate.py
    {{py}} scripts/check_papers.py
    {{py}} scripts/proof_claim_sweep.py

test:
    {{py}} -m pytest -q tests/

formal:
    cd formal && lake build && lake env lean VerifyAxioms.lean && lake check --paranoid && lake comparator --config comparator.json --paranoid

formal-nosandbox:
    cd formal && lake build Challenge Solution NonVacuity && lake env lean VerifyAxioms.lean && lake env leanchecker-paranoid --fresh Solution && lake env leanchecker-paranoid --fresh NonVacuity

lint:
    ruff check scripts rag tests || true
    mypy || true

mutate:
    {{py}} tests/mutation_check.py

verify-citations:
    {{py}} scripts/verify_citations.py

reproduce: setup build corpus index register check test formal-nosandbox
    @echo "Reproduction complete."

audit:
    pwsh -File scripts/Audit-Repo.ps1 -Path .
