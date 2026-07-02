#!/usr/bin/env python3
"""Gamma-pinch band closure — proved lemmas + closure table.

Two independent Terras exclusion routes (see GAMMA-DUAL-ROUTE.md):

  Route A: max tau < tau_min(k) in a window  =>  band slice empty.
  Route B: gamma(n) <= G for all n  =>  tau(n) <= G log2(n);
           if G log2(hi) < tau_min(k), band k empty past hi's scale.

Route B lower bound (proved, RECORD-BAND): any Terras violation in band k
needs gamma >= gamma_floor(k).  Measured max gamma << gamma_floor in scanned range.

This script does NOT prove a global gamma upper bound.  It computes which
bands would close under a hypothetical G and compares to the Terras ledger.

Subcommands: selftest, table, close-if.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from time import perf_counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from collatz_frontier_geometry import GAMMA_CEILING  # noqa: E402
from collatz_reduction import squeeze_payload  # noqa: E402

DEFAULT_SQUEEZE = os.path.join(
    os.path.dirname(__file__), "results", "reduction_squeeze.json"
)
DEFAULT_LEDGER = os.path.join(os.path.dirname(__file__), "results", "terras_ledger.json")
SCAN_FLOOR = 15_443_807_723


def pinch_row(band: dict[str, object], g_upper: float) -> dict[str, object]:
    log2_hi = float(band["log2_n_ceiling"])
    tau_min = int(band["tau_min"])
    gamma_floor = float(band.get("gamma_floor_at_ceiling", float("inf")))
    tau_implied = g_upper * log2_hi
    return {
        "band_k": band["band_k"],
        "q_k": band["q_k"],
        "status_structural": band["status"],
        "log2_n_ceiling": log2_hi,
        "tau_min": tau_min,
        "gamma_floor": gamma_floor,
        "g_upper_assumed": g_upper,
        "tau_implied_at_ceiling": round(tau_implied, 1),
        "pinch_ratio_tau": round(tau_min / tau_implied, 1) if tau_implied > 0 else None,
        "pinch_ratio_gamma_floor": round(gamma_floor / g_upper, 1),
        "closes_via_gamma_lemma": tau_implied < tau_min and g_upper < gamma_floor,
        "closes_via_gamma_floor_only": g_upper < gamma_floor,
    }


def table_payload(
    scan_floor: int,
    g_upper: float,
    max_bands: int,
    ledger_path: str | None,
) -> dict[str, object]:
    sq = squeeze_payload(320, scan_floor, max_bands)
    bands = [
        b
        for b in sq["bands"]
        if b["status"] == "SCAN_GAP" and "log2_n_ceiling" in b and "tau_min" in b
    ]
    rows = [pinch_row(b, g_upper) for b in bands]
    measured_max_gamma: float | None = None
    terras_through: int | None = None
    if ledger_path and os.path.isfile(ledger_path):
        with open(ledger_path, encoding="utf-8") as f:
            led = json.load(f)
        measured_max_gamma = float(led.get("global_max_gamma", 0))
        terras_through = int(led.get("terras_verified_through", 0))
    closes = [r for r in rows if r["closes_via_gamma_lemma"]]
    return {
        "mode": "table",
        "scan_floor": scan_floor,
        "g_upper_hypothesis": g_upper,
        "borel_cantelli_ceiling": GAMMA_CEILING,
        "lemma_gamma_tau": (
            "If gamma(n) <= G for all n, then tau(n) <= G log2(n); "
            "band k empty at ceiling hi if G log2(hi) < tau_min(k)."
        ),
        "lemma_gamma_floor": (
            "Terras violation in band k implies gamma >= gamma_floor(k) "
            "(RECORD-BAND, proved)."
        ),
        "measured_max_gamma": measured_max_gamma,
        "terras_verified_through": terras_through,
        "bands_would_close_under_G": len(closes),
        "first_open_under_G": next((r for r in rows if not r["closes_via_gamma_lemma"]), None),
        "rows": rows,
        "honesty": (
            "Hypothetical G only. Collatz OPEN. Proving G globally would close "
            "Terras structurally; measured max gamma does not."
        ),
    }


def close_if_payload(g_upper: float, band_k: int, scan_floor: int) -> dict[str, object]:
    sq = squeeze_payload(320, scan_floor, 24)
    bands = [b for b in sq["bands"] if b.get("band_k") == band_k]
    if not bands:
        raise SystemExit(f"band_k={band_k} not found")
    row = pinch_row(bands[0], g_upper)
    return {
        "mode": "close-if",
        "band_k": band_k,
        "verdict": (
            f"Band {band_k} would be PROVED EMPTY under gamma <= {g_upper}"
            if row["closes_via_gamma_lemma"]
            else f"Band {band_k} NOT closed by gamma <= {g_upper} alone at ceiling"
        ),
        "row": row,
    }


def selftest_payload() -> dict[str, object]:
    checks: list[dict[str, object]] = []
    # Lemma: G=20, band 13 ceiling log2~40.4 => tau_implied~808 < 301994
    row = pinch_row(
        {
            "band_k": 13,
            "q_k": 190537,
            "status": "SCAN_GAP",
            "log2_n_ceiling": 40.426,
            "tau_min": 301994,
            "gamma_floor_at_ceiling": 7365.7,
        },
        20.0,
    )
    checks.append({"name": "band13_closes_at_G20", "pass": row["closes_via_gamma_lemma"]})
    # G=19.98 should still close band 13
    row2 = pinch_row(
        {
            "band_k": 13,
            "q_k": 190537,
            "status": "SCAN_GAP",
            "log2_n_ceiling": 40.426,
            "tau_min": 301994,
            "gamma_floor_at_ceiling": 7365.7,
        },
        GAMMA_CEILING,
    )
    checks.append({"name": "band13_closes_at_BC_ceiling", "pass": row2["closes_via_gamma_lemma"]})
    # Violation floor >> measured: 16.32 < 1578
    checks.append(
        {
            "name": "measured_gamma_below_violation_floor_band10",
            "pass": 16.32 < 1578.4,
        }
    )
    # G too large: G=10000 cannot close band 13 via tau pinch (tau_implied huge)
    row3 = pinch_row(
        {
            "band_k": 13,
            "q_k": 190537,
            "status": "SCAN_GAP",
            "log2_n_ceiling": 40.426,
            "tau_min": 301994,
            "gamma_floor_at_ceiling": 7365.7,
        },
        10000.0,
    )
    checks.append({"name": "G10000_does_not_close_band13", "pass": not row3["closes_via_gamma_lemma"]})
    return {
        "mode": "selftest",
        "all_pass": all(c["pass"] for c in checks),
        "checks": checks,
    }


def ledger_gap_payload(ledger_path: str, scan_floor: int) -> dict[str, object]:
    with open(ledger_path, encoding="utf-8") as f:
        led = json.load(f)
    max_gamma = float(led.get("global_max_gamma", 0))
    max_gamma_n = int(led.get("global_max_gamma_n", 0))
    sq = squeeze_payload(320, scan_floor, 16)
    bands = [b for b in sq["bands"] if b["status"] == "SCAN_GAP" and "gamma_floor_at_ceiling" in b]
    gaps = []
    for b in bands:
        gf = float(b["gamma_floor_at_ceiling"])
        gaps.append(
            {
                "band_k": b["band_k"],
                "gamma_floor": gf,
                "measured_max_gamma": max_gamma,
                "margin_ratio": round(gf / max_gamma, 1) if max_gamma > 0 else None,
                "violation_possible_at_measured_gamma": max_gamma >= gf,
            }
        )
    return {
        "mode": "ledger-gap",
        "terras_verified_through": led.get("terras_verified_through"),
        "global_max_gamma": max_gamma,
        "global_max_gamma_n": max_gamma_n,
        "borel_cantelli_ceiling": GAMMA_CEILING,
        "below_BC_ceiling": max_gamma < GAMMA_CEILING,
        "bands": gaps,
        "verdict": (
            f"Measured max gamma {max_gamma} is below every violation floor "
            f"(min floor {min(g['gamma_floor'] for g in gaps):.1f} in scan-gap bands)."
            if gaps and all(not g["violation_possible_at_measured_gamma"] for g in gaps)
            else "Check bands table"
        ),
        "honesty": "Measured only. Does not prove global gamma bound.",
    }


def emit(payload: dict[str, object], out: str | None) -> None:
    text = json.dumps(payload, indent=2)
    if out:
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    print(text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Gamma-pinch band closure table")
    sub = parser.add_subparsers(dest="cmd", required=True)
    st = sub.add_parser("selftest")
    st.add_argument("--out", default="")
    tb = sub.add_parser("table")
    tb.add_argument("--scan-floor", type=int, default=SCAN_FLOOR)
    tb.add_argument("--g-upper", type=float, default=GAMMA_CEILING)
    tb.add_argument("--max-bands", type=int, default=16)
    tb.add_argument("--ledger", default=DEFAULT_LEDGER)
    tb.add_argument("--out", default="")
    ci = sub.add_parser("close-if")
    ci.add_argument("--g-upper", type=float, required=True)
    ci.add_argument("--band-k", type=int, required=True)
    ci.add_argument("--scan-floor", type=int, default=SCAN_FLOOR)
    ci.add_argument("--out", default="")
    lg = sub.add_parser("ledger-gap")
    lg.add_argument("--ledger", default=DEFAULT_LEDGER)
    lg.add_argument("--scan-floor", type=int, default=SCAN_FLOOR)
    lg.add_argument("--out", default="")
    args = parser.parse_args()
    started = perf_counter()
    if args.cmd == "selftest":
        payload = selftest_payload()
    elif args.cmd == "table":
        payload = table_payload(
            args.scan_floor,
            args.g_upper,
            args.max_bands,
            args.ledger if args.ledger else None,
        )
    elif args.cmd == "ledger-gap":
        payload = ledger_gap_payload(args.ledger, args.scan_floor)
    else:
        payload = close_if_payload(args.g_upper, args.band_k, args.scan_floor)
    payload["elapsed_seconds"] = round(perf_counter() - started, 3)
    emit(payload, args.out or None)
    if args.cmd == "selftest" and not payload["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
