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
python scripts/timestamp_manifest.py --check
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

## 3. Daily External Program Sync (`sync-external.yml`)

Once per day (07:37 UTC, or manually via *Run workflow*) GitHub Actions runs
`python scripts/sync_external_programs.py`, re-verifies the result offline with `--check`, and — only when the
Left to Solve data changed — commits `data/external/` + `docs/external/` straight to `main` and dispatches the Pages
workflow. Any parsing/consistency/shrink guard failure aborts without writing and turns the run red. Local equivalents:

```bash
python scripts/sync_external_programs.py           # live fetch (network)
python scripts/sync_external_programs.py --check   # offline integrity + view freshness
python scripts/sync_external_programs.py --render  # offline re-render after editing crosswalk-overrides.yaml
```

## 4. Permanent Third-Party Preservation

- **Primary remote:** `https://github.com/0thernes/unsolved-mathematics`
- **Master archive mirror (`0TH-BUILD-004`):** `https://github.com/0thernes/0thernes-research-archive`
- **Software Heritage archival (ISO/IEC 18670 SWHID):** Archived via Save Code Now — verified full snapshot `swh:1:snp:c11ec8263dd64b986c52bb400b8c3a85a3e6a254` (request `2696918`, 2026-11-26T13:32:11Z); refresh on each release via `POST https://archive.softwareheritage.org/api/1/origin/save/git/url/https://github.com/0thernes/unsolved-mathematics/`.
- **Dual cryptographic timestamps:** `data/MANIFEST.sha256.tsr` (DigiCert RFC 3161 TSA) and `data/MANIFEST.sha256.ots` (3-calendar Bitcoin OpenTimestamps), verified offline via `scripts/timestamp_manifest.py --check` and attached to every GitHub Release.
- **Zenodo DOI archival:** Prepared with valid `.zenodo.json` and `CITATION.cff` metadata; ready for owner activation under Zenodo's April 2026 depositor policy (no Zenodo DOI minted yet).
