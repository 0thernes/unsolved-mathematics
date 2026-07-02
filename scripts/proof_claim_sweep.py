#!/usr/bin/env python3
"""
proof_claim_sweep.py — automate the pseudo-proof discriminator.

A recurring failure mode in this repo: AI sessions deposit files that DECLARE an
open conjecture solved ("QED", "the prompt is the proof", "S ∩ ℤ>0 = ∅ therefore
Collatz", "beyond the simulation"). ~22% of authored Collatz artifacts were this
genre; all were caught and quarantined by hand. This script makes the check
mechanical so it can gate commits / CI.

Discriminator (low false-positive by design): a file is flagged only when it
BOTH looks like a victory-declaration (attractor filename OR >=2 strong claim
phrases) AND lacks the honest-hedging vocabulary that every legitimate analysis
or audit in this repo uses ("does not prove", "remains open", "[VERIFIED]",
"candidate", "obstruction", "no proof claim", ...). Honest files quote the same
phrases while hedging, so they pass; victory-declarations do not hedge, so they
are flagged.

Exit 0 = clean. Exit 1 = suspected pseudo-proof(s) found (prints them).

Usage:
  python scripts/proof_claim_sweep.py                 # scan all problems/
  python scripts/proof_claim_sweep.py <path> [...]    # scan specific files
"""
from __future__ import annotations
import os, re, sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

STRONG = [
    r"the prompt is the proof", r"\bP ?⊢ ?C\b", r"QED under (this )?P\b",
    r"the rocket has", r"\bAI did it\b", r"RESOLVED OUTSIDE", r"beyond the simulation",
    r"Achieved\.?\s*QED", r"the conjecture is resolved", r"Collatz (is|conjecture[:]?) .{0,20}resolved",
    r"Shipped under YOLO", r"\bLFG\b", r"the repetition is the proof",
    r"colimit is C\b", r"fixedpoint is visible", r"S ∩ (ℤ|Z)\s*>?\s*0\s*=\s*∅.{0,40}(therefore|hence|so|⇒|resolved|Collatz)",
    r"P-repetition.{0,30}(proof|resolv|colimit|fixedpoint)",
]
HEDGE = [
    r"does not prove", r"do not prove", r"not a proof", r"no proof claim", r"proves no part",
    r"remains open", r"\bis OPEN\b", r"\bStatus:\s*\*{0,2}Open", r"\[VERIFIED\]", r"\[PROVED\]",
    r"CLAIM-AUDIT", r"\bcandidate\b", r"\bobstruction\b", r"Non-claims", r"heuristic",
    r"not (a )?proof of Collatz", r"evidence only", r"finite (evidence|measurement)",
]
FNAME_ATTRACTOR = re.compile(
    r"(-RESOLUTION|-CLOSURE|-COLIMIT|-FIXEDPOINT|THE-PROMPT-IS|THIS-P-|THIS-REPETITION|"
    r"PROMPT-ATTRACTOR|WORLD-OPERATOR|STRANGE-LOOP|BECOMING|EIGHTH|ONTOLOGICAL|"
    r"PROOF-CLAIM-OUTSIDE|OUTSIDE-RESOLUTION|MASTER_THEOREM|_formal_proof|_matrix_proof|"
    r"ASSAULT-DYNAMICS|EIGEN-SHEAF|KOLMOGOROV-ECHO)", re.I)

EXCLUDE_DIRS = {"_quarantine", "unverified-claims", "node_modules", ".git"}

def scan_text(name: str, text: str) -> tuple[bool, list[str]]:
    # Attractor filenames flag unconditionally: no honest analysis is named
    # THE-PROMPT-IS-THE-PROOF or P-*-RESOLUTION, and such files often fake-hedge
    # ("not a traditional proof") while still declaring victory.
    if FNAME_ATTRACTOR.search(name):
        return True, ["attractor filename"]
    # Content path: >=2 strong victory phrases AND no honest hedging.
    strong_hits = [p for p in STRONG if re.search(p, text, re.I)]
    if len(strong_hits) < 2:
        return False, []
    hedges = sum(1 for p in HEDGE if re.search(p, text, re.I))
    if hedges >= 1:
        return False, []  # honest discussion/audit that quotes the phrases — passes
    return True, [f"{len(strong_hits)} strong claim phrases, no hedging"]

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
            text = open(path, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        hit, reasons = scan_text(os.path.basename(path), text)
        if hit:
            flagged.append((path, reasons))
    if flagged:
        print(f"PSEUDO-PROOF SWEEP: {len(flagged)} suspected victory-declaration file(s):")
        for p, r in flagged:
            print(f"  ✗ {os.path.relpath(p)}  ({'; '.join(r)})")
        print("\nIf this is real math, add honest framing ('remains open', 'not a proof',")
        print("'[VERIFIED]', 'candidate', ...) or move it to _quarantine/. See REPO-HEALTH-AUDIT.md.")
        return 1
    print("PSEUDO-PROOF SWEEP: clean — no unhedged victory-declarations found.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
