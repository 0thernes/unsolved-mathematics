#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
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


def test_catalytic_native_parity_and_budget(tmp_path):
    """Build C17/BMI2 + safe Rust oracle when compilers exist and verify bit-exact parity + <2s budget (B11/B12/B27)."""
    import shutil
    import time

    gcc = shutil.which("gcc")
    rustc = shutil.which("rustc")
    native_dir = ROOT / "problems" / "collatz-conjecture" / "native"
    c_src = native_dir / "collatz_catalytic.c"
    rs_src = native_dir / "collatz_catalytic_oracle.rs"
    assert c_src.exists() and rs_src.exists()

    if not gcc:
        return  # C compiler optional on bare Python environments; CI runs dedicated native-catalytic-audit job.

    c_exe = tmp_path / "collatz_catalytic"
    subprocess.run(
        [gcc, "-O3", "-std=c17", "-Wall", "-Wextra", "-Werror", str(c_src), "-o", str(c_exe)],
        check=True,
        capture_output=True,
        text=True,
    )
    st = subprocess.run([str(c_exe), "self-test"], check=True, capture_output=True, text=True)
    assert "PASS" in st.stdout

    c_json = tmp_path / "c_s10_t20.json"
    t0 = time.perf_counter()
    subprocess.run(
        [
            str(c_exe),
            "target-tail",
            "--source-max-depth", "10",
            "--target-max-depth", "20",
            "--target-cutoffs", "12,14,16,18,20",
            "--thresholds", "8,10,12,14,16,18,20,22,24",
            "--output", str(c_json),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    elapsed = time.perf_counter() - t0
    assert elapsed < 2.0, f"C17 s10_t20 exceeded 2.0s performance budget: {elapsed:.3f}s"

    py_ref = json.loads((EXP / "results" / "odd_unit_lock_target_tail_s10_t20_20260705.json").read_text(encoding="utf-8"))
    c_res = json.loads(c_json.read_text(encoding="utf-8"))
    assert c_res["by_target_cutoff"]["20"]["valuation_histogram"] == py_ref["by_target_cutoff"]["20"]["valuation_histogram"]
    assert c_res["by_target_cutoff"]["20"]["max_valuation_e"] == py_ref["by_target_cutoff"]["20"]["max_valuation_e"]

    if rustc:
        rs_exe = tmp_path / "collatz_oracle"
        subprocess.run([rustc, "-O", str(rs_src), "-o", str(rs_exe)], check=True, capture_output=True, text=True)
        rs_out = json.loads(
            subprocess.run([str(rs_exe), "target-tail", "3", "10", "1", "20"], check=True, capture_output=True, text=True).stdout
        )
        assert rs_out["valuation_histogram"] == py_ref["by_target_cutoff"]["20"]["valuation_histogram"]
        assert rs_out["max_valuation_e"] == py_ref["by_target_cutoff"]["20"]["max_valuation_e"]


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
