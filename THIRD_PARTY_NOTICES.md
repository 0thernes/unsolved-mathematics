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

- **Left to Solve** (`lefttosolve.com`, public `/api/problems` endpoint and `/programs` page; robots.txt allows both; site source <https://github.com/GuillaumeBAUD-coder/open-math-agents>, no license declared). Mirrored once per day: aggregate program counts, item identifiers, titles, kinds, field tags, prize labels and "solved here" flags only. Excerpts, difficulty scores and live-agent counters are **not** stored. Not affiliated with or endorsed by Left to Solve.
- **google-deepmind/formal-conjectures** (Apache-2.0) — origin of the formal Lean statements whose identifiers and titles appear in `data/external/lefttosolve/items/`; the pinned upstream commit is recorded in `snapshot.json`.
- **teorth/erdosproblems** (Apache-2.0), **Wikipedia** (CC BY-SA 4.0) and the **Open Problem Garden** are upstream sources of Left to Solve; only short problem names/identifiers derived from them are mirrored. Programs whose titles are CC BY-SA user content (MathOverflow, Mathematics Stack Exchange, OEIS-not-formalized) are mirrored as **counts only**.

No third-party copyrighted manuscripts or arXiv source tarballs are redistributed in this repository.
