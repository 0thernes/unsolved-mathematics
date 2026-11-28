#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Generate or verify SHA-256 tamper-evidence manifest for canonical data, formal & paper artifacts.

Build Standard v1.2.0 item B39.

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
    "ERRATA.md",
    "HARDENING_INDEX.md",
    "ro-crate-metadata.json",
    "croissant.json",
    "schema/problem.schema.json",
    "schema/paper.schema.json",
    "schema/review.schema.json",
    "data/problems.yaml",
    "data/problems.json",
    "data/dossier-status.json",
    "data/citation-verification-log.json",
    "data/retraction-audit.json",
    "rag/corpus.jsonl",
    "lean/lean-toolchain",
    "lean/lakefile.toml",
    "lean/lake-manifest.json",
    "lean/comparator.json",
    "lean/formalization.yaml",
    "lean/Challenge.lean",
    "lean/Solution.lean",
    "lean/NonVacuity.lean",
    "lean/Adversarial.lean",
    "lean/VerifyAxioms.lean",
    "lean/FormalAtlas.lean",
    "lean/FormalAtlas/Defs.lean",
    "lean/FormalAtlas/Collatz.lean",
    "lean/FormalAtlas/ErdosStraus.lean",
    "lean/FormalAtlas/LonelyRunner.lean",
    "lean/FormalAtlas/Brocard.lean",
    "lean/FormalAtlas/Primes.lean",
    "lean/FormalAtlas/Goldbach.lean",
    "lean/FormalAtlas/PerfectNumbers.lean",
    "lean/FormalAtlas/Ramsey.lean",
    "lean/STATEMENT_FIDELITY.md",
    "lean/six_kernel_audit.txt",
    "paper/Donahue_2026_unsolved_mathematics_atlas.tex",
    "paper/references.bib",
    "paper/Donahue_2026_unsolved_mathematics_atlas.pdf",
    "paper/arxiv_submission.tar.gz",
    "docs/benchmarks.md",
    "docs/COLLATZ-TOOLSTACK-AND-CATALYTIC-AUDIT.md",
    "problems/collatz-conjecture/native/collatz_catalytic.c",
    "problems/collatz-conjecture/native/collatz_catalytic_oracle.rs",
    "problems/collatz-conjecture/native/fuzz_collatz_catalytic.c",
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
