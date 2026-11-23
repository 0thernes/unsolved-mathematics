# Security Policy

## Scope

The Unsolved Mathematics Atlas is a static mathematical reference corpus,
Python validation/RAG toolchain, and standalone Lean 4.35.0 formal verification
suite. It does not run a network service, store credentials, or process user
personal data.

## Threat Surface

- Supply-chain integrity of Python dependencies (`requirements.txt`, `pyproject.toml`, `requirements-lock.txt`) and Lean 4 toolchain pins (`formal/lean-toolchain`, `formal/lake-manifest.json`).
- Untrusted input parsing in `rag/retriever.py`, `scripts/generate.py`, and experiment analyzers (no `eval`, `exec`, `pickle`, or `yaml.load` — only `yaml.safe_load` and `json.loads`).
- Proof-assistant soundness and adversarial definition drift (mitigated via `lake check --paranoid` across six independent kernels and `lake comparator --paranoid`).

See [`docs/threat-model.md`](docs/threat-model.md) for the full threat model.

## Reporting a Vulnerability

Please report security issues or suspected integrity/soundness defects by email
to `0_0@0thernes.art` or by opening a GitHub issue with the `bug` label (for
non-sensitive issues). Acknowledgment target: within 7 days.
