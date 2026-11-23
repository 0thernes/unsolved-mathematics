#!/usr/bin/env python3
"""Generate or verify SHA-256 tamper-evidence manifest for canonical data & formal artifacts.

Build Standard v1.1.0 item B39.

Usage:
    python scripts/build_data_manifest.py          # regenerate data/MANIFEST.sha256
    python scripts/build_data_manifest.py --check  # exit 0 iff manifest matches disk
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "data" / "MANIFEST.sha256"

TRACKED_FILES = [
    "VERSION",
    "CITATION.cff",
    ".zenodo.json",
    "schema/problem.schema.json",
    "schema/paper.schema.json",
    "schema/review.schema.json",
    "data/problems.yaml",
    "data/problems.json",
    "data/dossier-status.json",
    "data/citation-verification-log.json",
    "rag/corpus.jsonl",
    "formal/lean-toolchain",
    "formal/lakefile.toml",
    "formal/comparator.json",
    "formal/formalization.yaml",
    "formal/Challenge.lean",
    "formal/Solution.lean",
    "formal/NonVacuity.lean",
    "formal/VerifyAxioms.lean",
    "formal/FormalAtlas.lean",
    "formal/FormalAtlas/Defs.lean",
    "formal/FormalAtlas/Collatz.lean",
    "formal/FormalAtlas/ErdosStraus.lean",
    "formal/FormalAtlas/LonelyRunner.lean",
    "formal/FormalAtlas/Brocard.lean",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def compute_manifest() -> str:
    lines: list[str] = []
    for rel in sorted(TRACKED_FILES):
        p = ROOT / rel
        if not p.exists():
            raise FileNotFoundError(f"Tracked manifest file missing: {rel}")
        lines.append(f"{sha256_file(p)}  {rel}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build or check data/MANIFEST.sha256.")
    parser.add_argument("--check", action="store_true", help="Verify manifest matches current files.")
    args = parser.parse_args()

    expected = compute_manifest()
    if args.check:
        if not MANIFEST_PATH.exists():
            print("ERROR: data/MANIFEST.sha256 does not exist. Run python scripts/build_data_manifest.py", file=sys.stderr)
            return 1
        actual = MANIFEST_PATH.read_text(encoding="utf-8").replace("\r\n", "\n")
        if actual != expected:
            print("ERROR: data/MANIFEST.sha256 is out of sync with disk files.", file=sys.stderr)
            exp_map = dict(line.split("  ", 1)[::-1] for line in expected.strip().splitlines())
            act_map = dict(line.split("  ", 1)[::-1] for line in actual.strip().splitlines() if "  " in line)
            for k in sorted(set(exp_map) | set(act_map)):
                if exp_map.get(k) != act_map.get(k):
                    print(f"  DRIFT: {k}", file=sys.stderr)
            return 1
        print(f"OK: data/MANIFEST.sha256 verified ({len(TRACKED_FILES)} tracked files).")
        return 0

    MANIFEST_PATH.write_text(expected, encoding="utf-8", newline="\n")
    print(f"Wrote data/MANIFEST.sha256 ({len(TRACKED_FILES)} tracked files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
