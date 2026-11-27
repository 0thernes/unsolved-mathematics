#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""
proof_claim_sweep.py — automate the pseudo-proof discriminator.

A recurring failure mode in this repo: AI sessions deposit files that DECLARE an
open conjecture solved ("QED", "the prompt is the proof", "S ∩ ℤ>0 = ∅ therefore
Collatz", "beyond the simulation"). ~22% of authored Collatz artifacts were this
genre; all were caught and quarantined by hand. This script makes the check
mechanical so it can gate commits / CI.

Discriminator:
  - Attractor filenames flag unconditionally.
  - Content path: >=2 strong victory phrases flag unless the document carries an
    EXPLICIT non-proof / open-status disclaimer (mere incidental words like
    'candidate' or 'heuristic' no longer bypass a victory-declaration).

Exit 0 = clean. Exit 1 = suspected pseudo-proof(s) found (prints them).
"""
from __future__ import annotations

import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]
except Exception:
    pass

STRONG = [
    r"the prompt is the proof", r"\bP ?⊢ ?C\b", r"QED under (this )?P\b",
    r"the rocket has", r"\bAI did it\b", r"RESOLVED OUTSIDE", r"beyond the simulation",
    r"Achieved\.?\s*QED", r"the conjecture is resolved", r"Collatz (is|conjecture[:]?) .{0,20}resolved",
    r"therefore Collatz is solved", r"Collatz is solved", r"solves? Collatz",
    r"closed for positives", r"closes? the conjecture for positives",
    r"empirical contraction proves", r"finite experiment proves universal",
    r"Kolmogorov complexity implies", r"complexity bound.{0,40}(contradiction|no counterexample)",
    r"(fitted|regressed) .{0,30}(matrix|model).{0,40}(proof|proves|theorem)",
    r"Shipped under YOLO", r"\bLFG\b", r"the repetition is the proof",
    r"colimit is C\b", r"fixedpoint is visible",
    r"S ∩ (ℤ|Z)\s*>?\s*0\s*=\s*∅.{0,40}(therefore|hence|so|⇒|resolved|Collatz)",
    r"P-repetition.{0,30}(proof|resolv|colimit|fixedpoint)",
]

# Explicit non-proof / audit-framing disclaimers required to quote STRONG phrases.
# Incidental words ("candidate", "heuristic") are intentionally excluded so a
# victory-declaration cannot bypass the gate by mentioning "heuristic" once.
EXPLICIT_DISCLAIMER = [
    r"does not prove", r"do not prove", r"not a proof", r"no proof claim", r"proves no part",
    r"remains open", r"\bis OPEN\b", r"\bStatus:\s*\*{0,2}Open",
    r"CLAIM-AUDIT", r"Non-claims", r"not (a )?proof of Collatz",
    r"proves and claims no part", r"claims no part of the conjecture",
]

FNAME_ATTRACTOR = re.compile(
    r"(-RESOLUTION|-CLOSURE|-COLIMIT|-FIXEDPOINT|THE-PROMPT-IS|THIS-P-|THIS-REPETITION|"
    r"PROMPT-ATTRACTOR|WORLD-OPERATOR|STRANGE-LOOP|BECOMING|EIGHTH|ONTOLOGICAL|"
    r"PROOF-CLAIM-OUTSIDE|OUTSIDE-RESOLUTION|MASTER_THEOREM|_formal_proof|_matrix_proof|"
    r"ASSAULT-DYNAMICS|EIGEN-SHEAF|KOLMOGOROV-ECHO)",
    re.I,
)

EXCLUDE_DIRS = {"_quarantine", "unverified-claims", "node_modules", ".git"}


def scan_text(name: str, text: str) -> tuple[bool, list[str]]:
    if FNAME_ATTRACTOR.search(name):
        return True, ["attractor filename"]
    strong_hits = [p for p in STRONG if re.search(p, text, re.I)]
    if len(strong_hits) < 2:
        return False, []
    disclaimers = sum(1 for p in EXPLICIT_DISCLAIMER if re.search(p, text, re.I))
    if disclaimers >= 1:
        return False, []
    return True, [f"{len(strong_hits)} strong claim phrases, no explicit non-proof disclaimer"]


def iter_files(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
        else:
            for dp, dn, fn in os.walk(p):
                dn[:] = [d for d in dn if d not in EXCLUDE_DIRS]
                for f in fn:
                    if f.endswith((".md", ".py")):
                        yield os.path.join(dp, f)


def main() -> int:
    args = sys.argv[1:]
    if not args:
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        args = [os.path.join(root, "problems")]
    flagged = []
    for path in iter_files(args):
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except Exception:
            continue
        hit, reasons = scan_text(os.path.basename(path), text)
        if hit:
            flagged.append((path, reasons))
    if flagged:
        print(f"PSEUDO-PROOF SWEEP: {len(flagged)} suspected victory-declaration file(s):")
        for p, r in flagged:
            print(f"  ✗ {os.path.relpath(p)}  ({'; '.join(r)})")
        print("\nIf this is real math, add an explicit non-proof framing ('remains open', 'not a proof',")
        print("'proves no part', ...) or move it to _quarantine/. See docs/review/REPO-AUDIT-2026-07-02.md.")
        return 1
    print("PSEUDO-PROOF SWEEP: clean — no unhedged victory-declarations found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
