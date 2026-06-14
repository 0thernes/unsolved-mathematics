# The Unsolved Mathematics Atlas — build automation
# Usage: make <target>   (POSIX). Windows users: see build.ps1.

PY ?= python

.DEFAULT_GOAL := help
.PHONY: help build check validate corpus index embed query test clean all

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

build:  ## Regenerate folders, ranking, README table, registry JSON
	$(PY) scripts/generate.py

check:  ## Validate registry + ranking freshness (what CI runs)
	$(PY) scripts/generate.py --check
	$(PY) scripts/validate.py

validate: check  ## Alias for check

corpus:  ## Build the RAG retrieval corpus (rag/corpus.jsonl)
	$(PY) rag/build_corpus.py

index:  ## Build cross-cutting indexes under docs/indexes/
	$(PY) scripts/build_indexes.py

embed:  ## Build the dense vector index (needs requirements-rag.txt)
	$(PY) rag/embed_index.py

query:  ## Query the corpus: make query Q="bounded gaps between primes"
	$(PY) rag/retriever.py "$(Q)"

test:  ## Run the test suite
	$(PY) -m pytest -q || $(PY) tests/test_atlas.py

all: build corpus index check test  ## Full local build + checks

clean:  ## Remove generated, rebuildable artifacts (keeps dossiers)
	rm -f rag/index.npz
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type d -name .pytest_cache -prune -exec rm -rf {} +
