# 🏗️ Architecture

> How the Unsolved Mathematics Atlas is engineered as a reproducible, machine-
> readable knowledge system rather than a static document.

## 1. Design goals

| Goal | Mechanism |
|------|-----------|
| **Single source of truth** | All problem metadata lives in `data/problems.yaml`. Nothing authoritative is duplicated by hand. |
| **Reproducible ranking** | `scripts/generate.py` computes the Composite Severity Score; ordering is a pure function of the registry. |
| **Idempotent scaffolding** | Re-running the generator never clobbers human-written prose — it only fills gaps and refreshes generated artifacts. |
| **Machine-ingestible** | Every dossier is chunked into `rag/corpus.jsonl`; retrieval works out of the box. |
| **Provenance everywhere** | Papers/people carry verification flags; chunks link back to source files. |
| **CI-enforced integrity** | Schema validation, ranking freshness, and corpus build run on every push. |

## 2. Data-flow

```
            ┌────────────────────────┐
            │   data/problems.yaml   │   (human-edited source of truth)
            └───────────┬────────────┘
                        │  scripts/generate.py
        ┌───────────────┼─────────────────────────────┐
        ▼               ▼                               ▼
 data/problems.json   RANKING.md / README table   problems/<slug>/*.md
 (computed registry)  (generated views)           (scaffolded dossiers)
        │                                               │
        │                                  rag/build_corpus.py
        │                                               ▼
        │                                       rag/corpus.jsonl
        │                                               │
        │                                   rag/embed_index.py (optional)
        │                                               ▼
        └───────────────────────────────────────▶ rag/index.npz
                                                        │
                                                rag/retriever.py
                                                  (BM25 / dense)
```

## 3. Components

### 3.1 Registry (`data/problems.yaml`)
The canonical list. Each entry is validated against
[`schema/problem.schema.json`](schema/problem.schema.json). Scores are 0–100
editorial estimates; `year_posed` may be negative (BCE).

### 3.2 Build engine (`scripts/generate.py`)
- validates the registry,
- computes CSS and the canonical rank,
- writes `data/problems.json`, `RANKING.md`, and patches the README ranking block,
- scaffolds each `problems/<slug>/` folder with eight dossier files + `metadata.json` + `rag/`.

Idempotency rule: prose files are written **only if absent**; `metadata.json` is
always regenerated (it is fully derived).

### 3.3 Dossier (`problems/<slug>/`)
The unit of knowledge. Eight markdown files (see README) plus a machine record.
Folders are keyed by the **stable slug**, never by rank — ranks shift as scores
are refined, so the rank lives in `metadata.json` and `RANKING.md` instead. The
generator reconciles the tree on every run: orphaned, unauthored folders (whose
slug left the registry) are removed; authored orphans are flagged, never deleted.

### 3.4 RAG layer (`rag/`)
Heading-aware, token-aware chunker → JSONL corpus → BM25 (zero-dep) or dense
(sentence-transformers) retrieval. See [rag/README.md](rag/README.md).

### 3.5 Documentation (`docs/`)
- `architecture/` — the ER model and data model (below).
- `methodology/` — ranking formula and sourcing standards.
- `kanban/` — the live research board.

### 3.6 External program mirror (`data/external/`, `docs/external/`)

`scripts/sync_external_programs.py` mirrors the public [Left to Solve](https://lefttosolve.com/programs) program catalogue once per day (`.github/workflows/sync-external.yml`): program-level counts and provenance in `data/external/lefttosolve/snapshot.json`, a formal-statement item index per program in `items/*.jsonl`, an append-only `history.jsonl`, and a deterministic Atlas crosswalk (`crosswalk.json`, curated via `data/external/crosswalk-overrides.yaml`). This layer is deliberately **outside** `data/problems.yaml`, `data/MANIFEST.sha256` and the RAG corpus: it changes daily, carries its own content SHA-256, is verified offline by `--check` in CI, and can only raise human-review signals — it never edits an Atlas status.

## 4. Entity model (summary)

The atlas is, conceptually, a small graph database flattened into files. The
core entities and relationships:

```mermaid
erDiagram
    PROBLEM ||--o{ PAPER          : "is studied by"
    PROBLEM ||--o{ MATHEMATICIAN  : "is worked on by"
    PROBLEM ||--o{ APPROACH       : "is attacked via"
    PROBLEM ||--o{ ATTEMPT        : "has"
    MATHEMATICIAN ||--o{ PAPER    : "authors"
    MATHEMATICIAN ||--o{ PROBLEM  : "originates"
    APPROACH ||--o{ PAPER         : "is developed in"
    PROBLEM }o--|| FIELD          : "belongs to"
    PROBLEM }o--o{ PROBLEM        : "relates to"

    PROBLEM {
        string slug PK
        string title
        int    year_posed
        int    difficulty
        int    centrality
        int    tractability
        float  css
        int    rank
        enum   status
    }
    PAPER {
        string title
        int    year
        enum   kind
        enum   verification
    }
    MATHEMATICIAN {
        string name
        string era
        string affiliation
    }
```

The full ER specification, including cardinalities and the "ERP" (Entity-
Relationship-Process) operational layer, is in
[docs/architecture/ERD.md](docs/architecture/ERD.md).

## 5. Build, Formal Core & CI

| Workflow | Trigger | Does |
|----------|---------|------|
| `ci.yml` | push to `main` / manual | Windows + Ubuntu verification ladder (pytest, Hypothesis, mutation, manifest, `.tsr`/`.ots` timestamps), Linux `bwrap` 6-kernel Lean 4.35.0 replay + live negative kernel test, report-only `ruff`/`mypy`/`gitleaks`/`osv-scanner`/Build Standard audit |
| `validate-registry.yml` | push to `data/**`, `schema/**`, `scripts/**`, `lean/**` | Schema, view freshness, proof-claim sweep, retraction, axiom-parity, manifest & timestamp checks |
| `pages.yml` | push to `main` | Build and deploy live Atlas Explorer (`_site/index.html`) + 8-domain Lean Proof Blueprint (`_site/blueprint.html`) |
| `release.yml` | push `v*` tag | Package reproducible tarball, white paper PDF & arXiv bundle, `.tsr`/`.ots` timestamps, `SHA256SUMS`, SLSA provenance (`attest-build-provenance@v4`), and GitHub Release |

CI reports immediately if the committed `RANKING.md`, README table, `data/MANIFEST.sha256`, or verbatim `#print axioms` block drifts from canonical sources.

## 6. Extending

Adding a problem is a one-file change plus one command:

```bash
# 1. append an entry to data/problems.yaml (must satisfy the schema)
# 2. rebuild
python scripts/generate.py
python rag/build_corpus.py
# 3. flesh out the new problems/<slug>/*.md dossier
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the authoring and sourcing standards.
