# Third-Party Notices & Attribution

This repository contains original curation, build scripts, and Lean 4 formal
proofs by Alexander S. Donahue (MIT license for code in `LICENSE-CODE`, CC BY 4.0
for prose/data in `LICENSE`). Mathematical theorems, conjectures, and historical
facts are not subject to copyright.

## Runtime & Build Dependencies

| Component | License | Role |
|---|---|---|
| [Python Standard Library](https://docs.python.org/3/license.html) | PSF-2.0 | Core scripts, RAG BM25 retriever, citation verifier |
| [PyYAML](https://github.com/yaml/pyyaml) | MIT | Registry YAML parsing (`data/problems.yaml`) |
| [jsonschema](https://github.com/python-jsonschema/jsonschema) | MIT | Draft 2020-12 JSON Schema validation |
| [Lean 4 (v4.35.0)](https://github.com/leanprover/lean4) | Apache-2.0 | Proof assistant & official C++ kernel (`lean/`) |
| [lean4lean](https://github.com/digama0/lean4lean), [nanoda](https://github.com/ammkrn/nanoda_lib), `con-leche`, `con-ron` | Apache-2.0 / MIT | Independent external Lean kernels bundled with Lean 4.35.0 |
| [Tectonic](https://tectonic-typesetting.github.io/) | MIT | Reproducible AMS-LaTeX typesetting engine (`paper/`) |
| [pytest](https://github.com/pytest-dev/pytest) | MIT | Test runner (dev dependency) |
| [Hypothesis](https://github.com/HypothesisWorks/hypothesis) | MPL-2.0 | Property-based testing (dev dependency) |
| [Ruff](https://github.com/astral-sh/ruff) | MIT | Static analysis & linting (dev dependency) |
| [mypy](https://github.com/python/mypy) | MIT | Static type checking (dev dependency) |
| [gitleaks](https://github.com/gitleaks/gitleaks) & [osv-scanner](https://github.com/google/osv-scanner) | MIT / Apache-2.0 | SHA-256-verified report-only secret and vulnerability scanners in CI |

## External Primary Registries & Timestamp Services Queried (Read-Only / Public)

- **arXiv API** (`export.arxiv.org`) — metadata verification of arXiv preprint identifiers.
- **Crossref REST API** (`api.crossref.org`) — metadata verification and retraction auditing of publisher DOIs.
- **DataCite REST API** (`api.datacite.org`) — retraction/metadata auditing of DataCite / arXiv DOIs (`10.48550/*`).
- **DigiCert RFC 3161 TSA** (`timestamp.digicert.com`) — trusted timestamp reply (`data/MANIFEST.sha256.tsr`).
- **OpenTimestamps Calendar Pool** (`opentimestamps.org`, `eternitywall.com`) — Bitcoin-anchored timestamp proof (`data/MANIFEST.sha256.ots`).
- **Software Heritage** (`archive.softwareheritage.org`) — permanent ISO/IEC 18670 SWHID archival snapshots.

## Mirrored Third-Party Open-Problem Data (`data/external/`, `docs/external/`)

These external metadata files are refreshed daily by `.github/workflows/sync-external.yml` as a clearly separated sidecar layer and are **explicitly carved out of this repository's CC BY 4.0 data license** (see `LICENSE`). Only factual metadata and back-links are stored (`id`, `title`, `kind`, `fields`, `prize`, `solved`); **zero statement excerpts** and zero volatile counters (`liveAgents`, `claimed`, `difficulty`) are copied. Entries are removed on request. Not affiliated with or endorsed by Left to Solve or any upstream source.

- **Left to Solve** (`lefttosolve.com`, public `/api/problems`, `/api/stats`, and `/programs` endpoints; `robots.txt` allows all three, while disallowed `/api/desk/` and `/api/verdict` are never requested; site source <https://github.com/GuillaumeBAUD-coder/open-math-agents>, no aggregate license declared). Mirrored once per day across **all 25 programs** (sharded at $\le 4\text{ MiB}$ per JSONL file to stay strictly under Build Standard A24's 5 MB cap).
- **google-deepmind/formal-conjectures** (Apache-2.0) — origin of the formal Lean statements whose identifiers and titles appear in `data/external/lefttosolve/items/`; the pinned upstream commit is recorded in `snapshot.json`.
- **teorth/erdosproblems** (Apache-2.0) and the **Open Problem Garden** — upstream sources of Erdős and OPG metadata/identifiers mirrored via Left to Solve.
- **Wikipedia, MathOverflow, Mathematics Stack Exchange, and OEIS** (CC BY-SA 4.0) — upstream sources of problem/question titles in the corresponding programs (`wikipedia-list-not-formalized`, `mathoverflow-not-formalized`, `mathematics-stack-exchange-not-formalized`, `oeis-conjectures-not-formalized`, etc.). Third-party titles retain their upstream CC BY-SA 4.0 licenses, link directly back to their source pages, and are excluded from automatic Atlas crosswalk matching where raw Q&A streams would introduce noise.

No third-party copyrighted manuscripts or arXiv source tarballs are redistributed in this repository.
