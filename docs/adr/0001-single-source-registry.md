# ADR 0001: Single-Source YAML Registry & Deterministic View Generation

- **Status:** Accepted
- **Date:** 2026-07-01 (amended 2026-11-23 for `v0.3.0`)
- **Deciders:** Alexander S. Donahue

## Context

An atlas covering 106 unsolved mathematical problems with 9+ files per problem (`~950` dossier files plus 8 summary indexes, JSON exports, and a RAG corpus) rapidly suffers silent metadata drift if ranks, statuses, tags, or severity scores are hand-edited across files. During the 2026-11-23 forensic audit, we discovered that 81 of 106 `problems/<slug>/README.md` headers held stale Composite Severity Score (CSS) ranks because `scripts/generate.py` updated `docs/indexes/*` but never refreshed per-dossier READMEs, and `generate.py` broke ties non-deterministically.

## Decision

1. `data/problems.yaml` is the **sole source of truth** for problem metadata (validated strictly against `schema/problem.schema.json` using mandatory `jsonschema`, never silently skipped).
2. `scripts/generate.py` deterministically derives `data/problems.json`, all generated `docs/indexes/*.md` tables, and the metadata/rank header block of all 106 `problems/<slug>/README.md` dossiers using a total tie-break key `(-composite_severity(p), p["slug"])` and an explicit pinned `CURRENT_YEAR = 2026`.
3. `rag/build_corpus.py` deterministically compiles `rag/corpus.jsonl` with globally unique `(slug, section, chunk_idx)` IDs and zero optional environment-dependent tokenizers (`tiktoken` branch removed).
4. CI executes `scripts/generate.py --check`, `scripts/validate.py`, `scripts/check_dossiers.py`, `scripts/check_papers.py`, and `scripts/build_data_manifest.py --check` so any drift fails the build immediately.

## Consequences

- **Positive:** Eliminates silent rank/status drift across 106 dossiers; guarantees byte-reproducible JSON/Markdown/JSONL outputs across Ubuntu and Windows.
- **Negative / Trade-off:** `CURRENT_YEAR` must be explicitly bumped (and views regenerated) each calendar year instead of silently reading wall-clock `date.today().year` (see Dilemma D4 in `docs/reviews/2026-11-23-forensic-philosophical-audit.md`).
