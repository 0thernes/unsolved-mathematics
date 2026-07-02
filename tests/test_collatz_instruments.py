#!/usr/bin/env python3
"""Smoke tests for the Collatz experiments suite (audit roadmap #4).

Runnable standalone (python tests/test_collatz_instruments.py) or via pytest.
Fast (<30 s): tiny parameters only. These test that instruments RUN and match
session-verified ground truth; they do not (and cannot) test the conjecture.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXP = ROOT / "problems" / "collatz-conjecture" / "experiments"
PY = sys.executable


def run(args, cwd=EXP, timeout=120):
    return subprocess.run([PY, *args], cwd=str(cwd), capture_output=True,
                          text=True, timeout=timeout)


def test_lib_selftest():
    r = run(["lib_collatz.py"])
    assert r.returncode == 0, r.stderr[-500:]
    assert "all checks passed" in r.stdout


def test_stochastic_model_check_small():
    r = run(["stochastic_model_check.py", "--limit", "20000", "--depth", "12"])
    assert r.returncode == 0, r.stderr[-500:]
    d = json.loads(r.stdout)
    assert "passed" in d["self_test"]
    # Terras equidistribution: empirical descent law tracks the exact model.
    assert d["descent_time_distribution"]["max_abs_deviation_from_exact_model"] < 5e-3


def test_cycle_bound_lab():
    r = run(["cycle_bound_lab.py"])
    assert r.returncode == 0, r.stderr[-500:]
    d = json.loads(r.stdout)
    # Session-verified: binding convergent q22 of log2(3) at n_min = 2^71.
    assert d["result"]["min_odd_steps_in_nontrivial_cycle"] == 65470613321


def test_survivor_count_depth16():
    # Independent inline DP (no repo imports): S(16) = 2114 exact
    # (audit-verified 2026-07-01: uncertified density 2114/65536).
    surv = {0: 1}
    for d in range(1, 17):
        nxt = {}
        for o, c in surv.items():
            for b in (0, 1):
                oo = o + b
                if 3 ** oo >= 2 ** d:
                    nxt[oo] = nxt.get(oo, 0) + c
        surv = nxt
    assert sum(surv.values()) == 2114


def test_audit_scripts_import():
    # Regression for the 2026-07-02 finding: quarantine moves broke imports.
    r = run(["-c", "import kick_repulsion_claim_audit, alignment_dichotomy_analyzer"])
    assert r.returncode == 0, r.stderr[-500:]


if __name__ == "__main__":
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"PASS {name}")
            except AssertionError as e:
                fails += 1
                print(f"FAIL {name}: {str(e)[:200]}")
    sys.exit(1 if fails else 0)
