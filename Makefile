# The Unsolved Mathematics Atlas — build automation
# Usage: make <target>   (POSIX). Cross-platform: see justfile or build.ps1.

PY ?= python

.DEFAULT_GOAL := help
.PHONY: help build check validate corpus index site embed query test clean all papers register dossiers sync formal lint mutate audit

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

build:  ## Regenerate folders, ranking, README table, registry JSON
	$(PY) scripts/generate.py

check:  ## Full integrity gate (registry, dossiers, papers, sweep, retractions, axioms, manifest, timestamps)
	$(PY) scripts/generate.py --check
	$(PY) scripts/validate.py
	$(PY) scripts/check_dossiers.py --strict
	$(PY) scripts/check_papers.py
	$(PY) scripts/proof_claim_sweep.py
	$(PY) scripts/check_retractions.py --check
	$(PY) scripts/check_readme_axioms.py
	$(PY) scripts/build_data_manifest.py --check
	$(PY) scripts/timestamp_manifest.py --check

validate: check  ## Alias for check

corpus:  ## Build the RAG retrieval corpus (rag/corpus.jsonl)
	$(PY) rag/build_corpus.py

index:  ## Build cross-cutting indexes under docs/indexes/
	$(PY) scripts/build_indexes.py

site:  ## Build static Atlas explorer and 8-domain Lean Proof Blueprint (_site/)
	$(PY) scripts/build_site.py

papers:  ## Integrity-gate the meta-analyses (honesty banner, no overclaims)
	$(PY) scripts/check_papers.py

register:  ## Rebuild the AI-review register (docs/review/REGISTER.md)
	$(PY) scripts/build_review_register.py

embed:  ## Build the dense vector index (needs requirements-rag.txt)
	$(PY) rag/embed_index.py

query:  ## Query the corpus: make query Q="bounded gaps between primes"
	$(PY) rag/retriever.py "$(Q)"

formal:  ## Build and multi-kernel verify the Lean 4.35.0 formal core + live negative kernel test
	cd lean && lake build Challenge Solution NonVacuity Adversarial && lake env lean VerifyAxioms.lean && lake check --paranoid && lake comparator --config comparator.json --paranoid
	$(PY) scripts/test_lean_negative.py

lint:  ## Run report-only linter and strict type check across all core Python files
	ruff check scripts rag tests examples || true
	ruff check --select E9,F63,F7,F82 problems/collatz-conjecture/experiments || true
	mypy --explicit-package-bases scripts rag examples || true

mutate:  ## Run targeted mutation test suite (100% kill required)
	$(PY) tests/mutation_check.py

audit:  ## Run Build Standard v1.2.0 repository audit
	bash scripts/audit-repo.sh . || true

test:  ## Run full test suite + targeted mutation checks
	@if $(PY) -c "import pytest" 2>/dev/null; then $(PY) -m pytest -v tests/ && $(PY) tests/mutation_check.py; else $(PY) tests/test_atlas.py && $(PY) tests/test_collatz_instruments.py; fi

all: build corpus index register site check test  ## Full local build + checks + tests

clean:  ## Remove generated, rebuildable artifacts (keeps dossiers)
	rm -f rag/index.npz
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type d -name .pytest_cache -prune -exec rm -rf {} +

dossiers:  ## Refresh dossier completeness report (data/dossier-status.json)
	$(PY) scripts/check_dossiers.py --strict

sync: dossiers corpus validate  ## Refresh dossier status + corpus, then validate (anti-staleness)
