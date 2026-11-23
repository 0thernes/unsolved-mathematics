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
| [Lean 4 (v4.35.0)](https://github.com/leanprover/lean4) | Apache-2.0 | Proof assistant & official C++ kernel (`formal/`) |
| [lean4lean](https://github.com/digama0/lean4lean), [nanoda](https://github.com/ammkrn/nanoda_lib), `con-leche`, `con-ron` | Apache-2.0 / MIT | Independent external Lean kernels bundled with Lean 4.35.0 |
| [pytest](https://github.com/pytest-dev/pytest) | MIT | Test runner (dev dependency) |
| [Hypothesis](https://github.com/HypothesisWorks/hypothesis) | MPL-2.0 | Property-based testing (dev dependency) |
| [Ruff](https://github.com/astral-sh/ruff) | MIT | Static analysis & linting (dev dependency) |
| [mypy](https://github.com/python/mypy) | MIT | Static type checking (dev dependency) |

## External Primary Registries Queried (Read-Only)

- **arXiv API** (`export.arxiv.org`) — metadata verification of arXiv preprint identifiers.
- **Crossref REST API** (`api.crossref.org`) — metadata verification of publisher DOIs.

No third-party copyrighted manuscripts or arXiv source tarballs are redistributed in this repository.
