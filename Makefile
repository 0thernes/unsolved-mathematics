# The Unsolved Mathematics Atlas — build automation
# Usage: make <target>   (POSIX). Cross-platform: see justfile or build.ps1.

PY ?= python

.DEFAULT_GOAL := help
.PHONY: help build check validate corpus index embed query test clean all papers register dossiers sync formal lint

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

build:  ## Regenerate folders, ranking, README table, registry JSON
	$(PY) scripts/generate.py

check:  ## Validate registry + ranking freshness + links + corpus IDs
	$(PY) scripts/generate.py --check
	$(PY) scripts/validate.py

validate: check  ## Alias for check

corpus:  ## Build the RAG retrieval corpus (rag/corpus.jsonl)
	$(PY) rag/build_corpus.py

index:  ## Build cross-cutting indexes under docs/indexes/
	$(PY) scripts/build_indexes.py

papers:  ## Integrity-gate the meta-analyses (honesty banner, no overclaims)
	$(PY) scripts/check_papers.py

register:  ## Rebuild the AI-review register (docs/review/REGISTER.md)
	$(PY) scripts/build_review_register.py

embed:  ## Build the dense vector index (needs requirements-rag.txt)
	$(PY) rag/embed_index.py

query:  ## Query the corpus: make query Q="bounded gaps between primes"
	$(PY) rag/retriever.py "$(Q)"

formal:  ## Build and multi-kernel verify the Lean 4 formal core
	cd formal && lake build && lake env leanchecker --fresh FormalAtlas && lake check --paranoid

lint:  ## Run report-only linter and strict type check
	ruff check scripts rag tests || true
	mypy scripts rag || true

test:  ## Run full test suite (pytest if available, else standalone runners)
	@if $(PY) -c "import pytest" 2>/dev/null; then $(PY) -m pytest -q tests/; else $(PY) tests/test_atlas.py && $(PY) tests/test_collatz_instruments.py; fi

all: build corpus index register check papers test  ## Full local build + checks

clean:  ## Remove generated, rebuildable artifacts (keeps dossiers)
	rm -f rag/index.npz
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type d -name .pytest_cache -prune -exec rm -rf {} +

dossiers:  ## Refresh dossier completeness report (data/dossier-status.json)
	$(PY) scripts/check_dossiers.py

sync: dossiers corpus validate  ## Refresh kanban + corpus, then validate (anti-staleness)
