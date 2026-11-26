#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Live Negative Lean 4.35.0 Kernel & Axiom-Gate Rejection Test (Playbook v1.3 Item #12).

Proves empirically that our active Lean 4.35.0 kernel and axiom filter are NON-VACUOUS:
  1. Rejects a deliberately false Brocard claim (`IsBrocardSol 6 27`, 721 != 729) with exit != 0.
  2. Rejects a deliberately false Lonely Runner claim (`FarEnough 3 1 9 1`) with exit != 0.
  3. Detects `sorryAx` if a proof uses `sorry`, proving the CI axiom allowlist actively fails closed.

Usage:
    python scripts/test_lean_negative.py
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEAN_DIR = ROOT / "lean"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def find_lake() -> str:
    found = shutil.which("lake")
    if found:
        return found
    home = Path.home()
    for cand in (home / ".elan" / "bin" / "lake.exe", home / ".elan" / "bin" / "lake"):
        if cand.exists():
            return str(cand)
    raise FileNotFoundError("Could not locate `lake` binary on PATH or under ~/.elan/bin")


def run_lean_snippet(lake: str, code: str) -> subprocess.CompletedProcess[str]:
    fd, tmp_name = tempfile.mkstemp(prefix="neg_kernel_", suffix=".lean")
    os.close(fd)
    tmp_path = Path(tmp_name)
    try:
        tmp_path.write_text(code, encoding="utf-8", newline="\n")
        return subprocess.run(
            [lake, "env", "lean", str(tmp_path)],
            cwd=str(LEAN_DIR),
            capture_output=True,
            text=True,
        )
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def main() -> int:
    lake = find_lake()

    # Negative Case 1: deliberately false Brocard solution (6! + 1 = 721 != 27^2 = 729)
    neg1 = (
        "import FormalAtlas.Defs\n"
        "theorem neg_false_brocard : FormalAtlas.IsBrocardSol 6 27 := by\n"
        "  unfold FormalAtlas.IsBrocardSol\n"
        "  decide\n"
    )
    r1 = run_lean_snippet(lake, neg1)
    if r1.returncode == 0:
        print("FAIL: Lean kernel accepted deliberately FALSE Brocard theorem!", file=sys.stderr)
        return 1
    print("PASS [1/3]: Lean 4.35.0 kernel actively REJECTED false Brocard claim (6!+1 = 27^2).")

    # Negative Case 2: deliberately false Lonely Runner claim (t=1/9, v=1 -> 1/9 < 1/3)
    neg2 = (
        "import FormalAtlas.Defs\n"
        "theorem neg_false_lonely_runner : FormalAtlas.FarEnough 3 1 9 1 := by\n"
        "  unfold FormalAtlas.FarEnough\n"
        "  decide\n"
    )
    r2 = run_lean_snippet(lake, neg2)
    if r2.returncode == 0:
        print("FAIL: Lean kernel accepted deliberately FALSE Lonely Runner theorem!", file=sys.stderr)
        return 1
    print("PASS [2/3]: Lean 4.35.0 kernel actively REJECTED false Lonely Runner claim (1/9 >= 1/3).")

    # Negative Case 3: sorry-tampered theorem triggers sorryAx in #print axioms allowlist gate
    neg3 = (
        "import FormalAtlas.Defs\n"
        "theorem neg_sorry_tamper : FormalAtlas.IsBrocardSol 6 27 := sorry\n"
        "#print axioms neg_sorry_tamper\n"
    )
    r3 = run_lean_snippet(lake, neg3)
    m = re.search(r"'neg_sorry_tamper'\s+depends on axioms:\s*\[([^\]]*)\]", r3.stdout, re.S)
    if not m:
        print(f"FAIL: Could not observe #print axioms on sorry-tamper probe:\n{r3.stdout}\n{r3.stderr}", file=sys.stderr)
        return 1
    used = {a.strip() for a in m.group(1).split(",") if a.strip()}
    bad = used - ALLOWED_AXIOMS
    if "sorryAx" not in bad:
        print(f"FAIL: Axiom gate failed to catch sorryAx (observed: {used})", file=sys.stderr)
        return 1
    print(f"PASS [3/3]: Axiom allowlist gate actively CAUGHT forbidden axiom {sorted(bad)} on sorry-tamper probe.")

    print("OK: All 3 live negative Lean 4.35.0 kernel & axiom-gate rejection checks PASSED.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
