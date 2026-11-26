# Operations, Backup & Offsite Mirror Protocol

This repository is a static mathematical corpus and formal proof library (no
live database or runtime server). Operational durability relies on deterministic
checksums, git bundle backups, and third-party archival mirrors.

## 1. Data Checksums (`data/MANIFEST.sha256`)

Every authoritative data file (`data/problems.yaml`, `data/problems.json`,
`data/dossier-status.json`, `data/citation-verification-log.json`,
`data/retraction-audit.json`, `rag/corpus.jsonl`, `lean/comparator.json`,
`lean/formalization.yaml`, `paper/*`, `ro-crate-metadata.json`, `croissant.json`) is
hashed in `data/MANIFEST.sha256`. Regenerate and verify after any data update:

```bash
python scripts/build_data_manifest.py
python scripts/build_data_manifest.py --check
```

## 2. Offsite Repository Mirror & Git Bundle Backup

Create a self-contained offline mirror bundle (full history + all refs):

```bash
git bundle create unsolved-mathematics-backup.bundle --all
git bundle verify unsolved-mathematics-backup.bundle
```

Restore test into a fresh directory:

```bash
git clone unsolved-mathematics-backup.bundle restored-atlas
cd restored-atlas && python scripts/validate.py
```

## 3. Permanent Third-Party Preservation

- **Primary remote:** `https://github.com/0thernes/unsolved-mathematics`
- **Master archive mirror (pinned submodule):** `https://github.com/0thernes/0thernes-research-archive`
- **Software Heritage archival (ISO/IEC 18670 SWHID):** Submit via Save Code Now (`POST https://archive.softwareheritage.org/api/1/origin/save/git/url/https://github.com/0thernes/unsolved-mathematics/`).
- **Zenodo DOI archival:** Enabled via GitHub release tags with `.zenodo.json` and `CITATION.cff` metadata.
