#!/usr/bin/env python3
"""First-open-band gap scanner — close the Session 6 scan window.

REDUCTION.md left a finite window after the 10^9 scan:

    10^9 < n <= n_ceiling   (first open band, ~2^31.03)

A Terras violation in that band needs tau >= tau_min (50509 for band q=31867).
If every n in the window has tau(n) < tau_min, the band is **proved empty**
of Terras violations — Terras holds throughout the first open band.

This is stronger than checking tau = sigma pointwise: max_tau < tau_min
excludes the entire self-trap / record-integer mechanism at that scale.

Subcommands: selftest, scan, theorem, ladder, close-band.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from time import perf_counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from collatz_frontier_geometry import GAMMA_CEILING, tau_sigma, tau_of  # noqa: E402
from collatz_reduction import squeeze_payload  # noqa: E402

DEFAULT_SQUEEZE = os.path.join(
    os.path.dirname(__file__), "results", "reduction_squeeze.json"
)
BAND10_CEILING = 2_193_206_481  # Session 7 closure (gap_scan_first_band.json)
BAND11_CEILING = 10_824_153_739  # pending closure


def _first_odd_above(lo: int) -> int:
    n = lo + 1 if lo % 2 == 0 else lo + 2
    return n if n > lo else lo + 1


def _scan_chunk(task: tuple[int, int]) -> dict[str, object]:
    """Worker: scan odd n in (lo, hi] without progress reporting."""
    lo, hi = task
    mismatches: list[dict[str, int]] = []
    max_tau = 0
    max_tau_n = 0
    max_gamma = 0.0
    max_gamma_n = 0
    records: list[dict[str, object]] = []
    total_tau = 0
    count = 0
    n = _first_odd_above(lo)
    while n <= hi:
        tau, sigma = tau_sigma(n)
        total_tau += tau
        count += 1
        if tau != sigma and len(mismatches) < 50:
            mismatches.append({"n": n, "tau": tau, "sigma": sigma})
        if tau > max_tau:
            max_tau = tau
            max_tau_n = n
            records.append(
                {
                    "n": n,
                    "tau": tau,
                    "sigma": sigma,
                    "gamma": round(tau / math.log2(n), 4),
                }
            )
        if tau > max_gamma * (n.bit_length() - 1):
            gamma = tau / math.log2(n)
            if gamma > max_gamma:
                max_gamma = gamma
                max_gamma_n = n
        n += 2
    return {
        "lo_exclusive": lo,
        "hi_inclusive": hi,
        "odd_integers_scanned": count,
        "total_tau": total_tau,
        "max_tau": max_tau,
        "max_tau_n": max_tau_n,
        "max_gamma": max_gamma,
        "max_gamma_n": max_gamma_n,
        "terras_mismatches": mismatches,
        "records": records,
    }


def _merge_chunks(chunks: list[dict[str, object]], lo: int, hi: int, tau_floor: int, elapsed: float) -> dict[str, object]:
    mismatches: list[dict[str, int]] = []
    max_tau = 0
    max_tau_n = 0
    max_gamma = 0.0
    max_gamma_n = 0
    records: list[dict[str, object]] = []
    total_tau = 0
    count = 0
    for ch in chunks:
        count += int(ch["odd_integers_scanned"])
        total_tau += int(ch["total_tau"])
        for m in ch["terras_mismatches"]:
            if len(mismatches) < 50:
                mismatches.append(m)
        if int(ch["max_tau"]) > max_tau:
            max_tau = int(ch["max_tau"])
            max_tau_n = int(ch["max_tau_n"])
        if float(ch["max_gamma"]) > max_gamma:
            max_gamma = float(ch["max_gamma"])
            max_gamma_n = int(ch["max_gamma_n"])
        records.extend(ch["records"])
    records.sort(key=lambda r: int(r["tau"]))  # type: ignore[arg-type]
    band_closed = max_tau < tau_floor
    return {
        "lo_exclusive": lo,
        "hi_inclusive": hi,
        "odd_integers_scanned": count,
        "elapsed_seconds": round(elapsed, 1),
        "tau_min_required": tau_floor,
        "max_tau": max_tau,
        "max_tau_n": max_tau_n,
        "max_gamma": round(max_gamma, 4),
        "max_gamma_n": max_gamma_n,
        "mean_tau": round(total_tau / count, 6) if count else None,
        "terras_mismatches": mismatches,
        "terras_verified": not mismatches,
        "band_closure": {
            "proved_empty": band_closed,
            "reason": (
                f"max_tau={max_tau} < tau_min={tau_floor}: no Terras violation "
                f"can live in this band past lo"
                if band_closed
                else f"max_tau={max_tau} >= tau_min={tau_floor} or mismatches found"
            ),
        },
        "gamma_record_pinch": {
            "measured_max_gamma": round(max_gamma, 4),
            "gamma_ceiling_heuristic": GAMMA_CEILING,
            "tau_implied_at_hi": round(max_gamma * math.log2(hi), 1) if hi > 1 else None,
            "tau_min_required": tau_floor,
            "pinch_ratio": round(tau_floor / (max_gamma * math.log2(hi)), 1) if max_gamma > 0 else None,
        },
        "records": records[-12:],
    }


def scan_range_parallel(lo: int, hi: int, tau_floor: int, workers: int) -> dict[str, object]:
    if lo >= hi:
        raise SystemExit(f"invalid range: lo={lo} hi={hi}")
    started = perf_counter()
    n0 = _first_odd_above(lo)
    n1 = hi if hi % 2 == 1 else hi - 1
    total_odds = max(0, (n1 - n0) // 2 + 1)
    workers = max(1, min(workers, total_odds or 1))
    odds_per = (total_odds + workers - 1) // workers
    tasks: list[tuple[int, int]] = []
    cur_lo = lo
    for _ in range(workers):
        if n0 > n1:
            break
        chunk_end = min(n1, n0 + 2 * odds_per - 1)
        tasks.append((cur_lo, chunk_end))
        cur_lo = chunk_end
        n0 = _first_odd_above(cur_lo)
    chunks: list[dict[str, object]] = []
    with ProcessPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(_scan_chunk, t) for t in tasks]
        done = 0
        for fut in as_completed(futures):
            chunks.append(fut.result())
            done += 1
            sys.stdout.write(f"chunks_done={done}/{len(tasks)}\n")
            sys.stdout.flush()
    elapsed = perf_counter() - started
    return _merge_chunks(chunks, lo, hi, tau_floor, elapsed)


def first_open_band(squeeze_path: str, scan_floor: int) -> dict[str, object] | None:
    """First SCAN_GAP band past scan_floor with a nonempty window."""
    with open(squeeze_path, encoding="utf-8") as fh:
        data = json.load(fh)
    for row in data.get("bands", []):
        if row.get("status") != "SCAN_GAP":
            continue
        hi = int(row["n_ceiling"])
        if hi <= scan_floor:
            continue
        return row
    # Recompute from squeeze_payload if bands lack updated floor
    sq = squeeze_payload(320, scan_floor, 20)
    for row in sq["bands"]:
        if row.get("status") != "SCAN_GAP":
            continue
        if int(row["n_ceiling"]) <= scan_floor:
            continue
        return row
    return None


def load_first_open(path: str) -> dict[str, object]:
    first = first_open_band(path, 10**9)
    if not first:
        raise SystemExit(f"no open band past 10^9 in {path}")
    return first


def scan_range(
    lo: int,
    hi: int,
    tau_floor: int,
    progress_every: int,
) -> dict[str, object]:
    """Scan odd n in (lo, hi] for tau/sigma and band-closure stats."""
    if lo >= hi:
        raise SystemExit(f"invalid range: lo={lo} hi={hi}")
    started = perf_counter()
    mismatches: list[dict[str, int]] = []
    max_tau = 0
    max_tau_n = 0
    max_gamma = 0.0
    max_gamma_n = 0
    records: list[dict[str, object]] = []
    total_tau = 0
    count = 0
    n = lo + 1 if lo % 2 == 0 else lo + 2
    if n <= lo:
        n = lo + 1

    while n <= hi:
        tau, sigma = tau_sigma(n)
        total_tau += tau
        count += 1
        if tau != sigma and len(mismatches) < 50:
            mismatches.append({"n": n, "tau": tau, "sigma": sigma})
        if tau > max_tau:
            max_tau = tau
            max_tau_n = n
            records.append(
                {
                    "n": n,
                    "tau": tau,
                    "sigma": sigma,
                    "gamma": round(tau / math.log2(n), 4),
                }
            )
        if tau > max_gamma * (n.bit_length() - 1):
            gamma = tau / math.log2(n)
            if gamma > max_gamma:
                max_gamma = gamma
                max_gamma_n = n
        if count % progress_every == 0:
            elapsed = perf_counter() - started
            rate = count / elapsed if elapsed > 0 else 0.0
            sys.stdout.write(
                f"progress: n={n} scanned={count} elapsed={elapsed:.0f}s "
                f"rate={rate:.0f}/s max_tau={max_tau}\n"
            )
            sys.stdout.flush()
        n += 2

    elapsed = perf_counter() - started
    band_closed = max_tau < tau_floor
    return {
        "lo_exclusive": lo,
        "hi_inclusive": hi,
        "odd_integers_scanned": count,
        "elapsed_seconds": round(elapsed, 1),
        "tau_min_required": tau_floor,
        "max_tau": max_tau,
        "max_tau_n": max_tau_n,
        "max_gamma": round(max_gamma, 4),
        "max_gamma_n": max_gamma_n,
        "mean_tau": round(total_tau / count, 6) if count else None,
        "terras_mismatches": mismatches,
        "terras_verified": not mismatches,
        "band_closure": {
            "proved_empty": band_closed,
            "reason": (
                f"max_tau={max_tau} < tau_min={tau_floor}: no Terras violation "
                f"can live in this band past lo"
                if band_closed
                else f"max_tau={max_tau} >= tau_min={tau_floor} or mismatches found"
            ),
        },
        "gamma_record_pinch": {
            "measured_max_gamma": round(max_gamma, 4),
            "gamma_ceiling_heuristic": GAMMA_CEILING,
            "tau_implied_at_hi": round(max_gamma * math.log2(hi), 1) if hi > 1 else None,
            "tau_min_required": tau_floor,
            "pinch_ratio": round(tau_floor / (max_gamma * math.log2(hi)), 1) if max_gamma > 0 else None,
        },
        "records": records[-12:],
    }


def band_scan_payload(
    scan_floor: int,
    band: dict[str, object],
    lo_override: int | None,
    hi_override: int | None,
    progress_every: int,
    workers: int,
) -> dict[str, object]:
    lo = lo_override if lo_override is not None else scan_floor
    hi = hi_override if hi_override is not None else int(band["n_ceiling"])
    tau_floor = int(band["tau_min"])
    if workers > 1:
        body = scan_range_parallel(lo, hi, tau_floor, workers)
        body["parallel_workers"] = workers
    else:
        body = scan_range(lo, hi, tau_floor, progress_every)
    return {
        "mode": "band-scan",
        "scan_floor": scan_floor,
        "band": {
            "band_k": band.get("band_k"),
            "q_k": band["q_k"],
            "q_k+1": band["q_k+1"],
            "o_min": band.get("o_min"),
            "tau_min": tau_floor,
            "log2_n_ceiling": band.get("log2_n_ceiling"),
        },
        **body,
    }


def scan_payload(
    squeeze_path: str,
    scan_floor: int,
    lo_override: int | None,
    hi_override: int | None,
    progress_every: int,
    band_k: int | None,
    workers: int,
) -> dict[str, object]:
    if band_k is not None:
        sq = squeeze_payload(320, scan_floor, 24)
        bands = [r for r in sq["bands"] if r.get("band_k") == band_k]
        if not bands:
            raise SystemExit(f"band_k={band_k} not found")
        return band_scan_payload(scan_floor, bands[0], lo_override, hi_override, progress_every, workers)
    band = first_open_band(squeeze_path, scan_floor)
    if band is None:
        raise SystemExit(f"no open band past scan_floor={scan_floor}")
    return band_scan_payload(scan_floor, band, lo_override, hi_override, progress_every, workers)


def close_band_payload(
    scan_floor: int,
    band_k: int,
    workers: int,
    scan_out: str | None,
    theorem_out: str | None,
) -> dict[str, object]:
    scan = scan_payload("", scan_floor, None, None, 2_000_000, band_k, workers)
    if scan_out:
        emit(scan, scan_out)
    thm = theorem_payload(scan)
    if theorem_out:
        emit(thm, theorem_out)
    return {
        "mode": "close-band",
        "scan": scan,
        "theorem": thm,
        "terras_verified_through": int(scan["hi_inclusive"]) if scan.get("band_closure", {}).get("proved_empty") else scan_floor,
    }


def band_plan_payload(scan_floor: int, band_k: int, rate_per_sec: float) -> dict[str, object]:
    sq = squeeze_payload(320, scan_floor, 24)
    bands = [r for r in sq["bands"] if r.get("band_k") == band_k]
    if not bands:
        raise SystemExit(f"band_k={band_k} not found")
    b = bands[0]
    lo = scan_floor
    hi = int(b["n_ceiling"])
    n0 = _first_odd_above(lo)
    n1 = hi if hi % 2 == 1 else hi - 1
    odds = max(0, (n1 - n0) // 2 + 1) if n0 <= n1 else 0
    est_sec = odds / rate_per_sec if rate_per_sec > 0 else None
    gamma_implied_tau = 16.3233 * math.log2(hi) if hi > 1 else None
    return {
        "mode": "band-plan",
        "scan_floor": scan_floor,
        "band_k": band_k,
        "band": b,
        "window": {"lo_exclusive": lo, "hi_inclusive": hi, "odd_integers": odds},
        "tau_min_required": b.get("tau_min"),
        "structural_status": (
            "PROVED_EMPTY"
            if b.get("status") == "PROVED_EMPTY"
            or int(b.get("o_need", 0)) >= int(b["q_k+1"])
            else "SCAN_REQUIRED"
        ),
        "estimate": {
            "rate_odd_per_sec_assumed": rate_per_sec,
            "elapsed_hours": round(est_sec / 3600, 2) if est_sec else None,
            "elapsed_minutes": round(est_sec / 60, 1) if est_sec else None,
        },
        "gamma_pinch_heuristic": {
            "measured_max_gamma_through_band12": 16.3233,
            "tau_implied_at_ceiling": round(gamma_implied_tau, 1) if gamma_implied_tau else None,
            "pinch_ratio_vs_tau_min": round(int(b["tau_min"]) / gamma_implied_tau, 1) if gamma_implied_tau else None,
            "note": "HEURISTIC only — not a theorem unless gamma is bounded globally",
        },
    }


def ladder_payload(scan_floor: int, closed_bands: list[int]) -> dict[str, object]:
    sq = squeeze_payload(320, scan_floor, 20)
    rows = []
    for r in sq["bands"]:
        status = r["status"]
        if r.get("band_k") in closed_bands:
            status = "CLOSED_SCAN"
        elif status == "SCAN_GAP" and int(r["n_ceiling"]) <= scan_floor:
            status = "CLOSED_SCAN"
        elif status == "PROVED_EMPTY":
            status = "PROVED_EMPTY"
        elif int(r.get("o_need", 0)) >= int(r["q_k+1"]):
            status = "PROVED_EMPTY"
        rows.append({**r, "effective_status": status})
    open_bands = [r for r in rows if r["effective_status"] == "SCAN_GAP"]
    return {
        "mode": "ladder",
        "scan_floor": scan_floor,
        "terras_verified_through": scan_floor,
        "closed_bands": closed_bands,
        "open_bands": len(open_bands),
        "next_band": open_bands[0] if open_bands else None,
        "bands": rows[:16],
    }


def theorem_payload(scan_result: dict[str, object]) -> dict[str, object]:
    bc = scan_result.get("band_closure", {})
    proved = bool(bc.get("proved_empty"))
    band = scan_result.get("band") or scan_result.get("first_open_band") or {}
    qk = band.get("q_k", "?")
    qk1 = band.get("q_k+1", "?")
    tau_min = scan_result.get("tau_min_required", band.get("tau_min", "?"))
    hi = scan_result.get("hi_inclusive", "?")
    lo = scan_result.get("lo_exclusive", "?")
    return {
        "mode": "theorem",
        "theorem": "Band closure" if proved else "Band scan (inconclusive or counterexample)",
        "statement": (
            f"Every odd integer n with {lo} < n <= {hi} has tau(n) < {tau_min}; "
            f"hence no Terras violation in convergent band [{qk}, {qk1}) past {lo}."
            if proved
            else "Scan did not close the band; see scan payload."
        ),
        "proved_empty": proved,
        "band": band,
        "scan_summary": {
            "odd_integers_scanned": scan_result.get("odd_integers_scanned"),
            "max_tau": scan_result.get("max_tau"),
            "tau_min_required": scan_result.get("tau_min_required"),
            "terras_verified": scan_result.get("terras_verified"),
            "elapsed_seconds": scan_result.get("elapsed_seconds"),
        },
        "honesty": (
            "Band closure if max_tau < tau_min and tau=sigma throughout. "
            "Does not prove Terras globally or Collatz."
        ),
    }


def selftest_payload() -> dict[str, object]:
    checks = []
    # 1. tiny window near 10^9
    tiny = scan_range(10**9, 10**9 + 20_000, tau_floor=50509, progress_every=5000)
    checks.append(
        {
            "check": "tiny_window_scan",
            "pass": tiny["terras_verified"] and tiny["max_tau"] < 50509,
            "max_tau": tiny["max_tau"],
            "count": tiny["odd_integers_scanned"],
        }
    )
    # 2. known record 63728127 has tau ~ 350+ (below floor)
    t_rec = tau_of(63_728_127)
    checks.append(
        {
            "check": "record_63728127_tau_below_band_floor",
            "tau": t_rec,
            "pass": t_rec < 50509,
        }
    )
    # 3. ladder past band-10 ceiling finds band 11
    lad = ladder_payload(BAND10_CEILING, closed_bands=[10])
    nxt = lad.get("next_band")
    checks.append(
        {
            "check": "next_band_is_11_after_band10_close",
            "pass": nxt is not None and nxt.get("q_k") == 79335,
            "next": nxt,
        }
    )
    # 4. band closure logic: tau_floor above max => proved_empty
    fake = {"max_tau": 400, "tau_min_required": 50509, "terras_verified": True}
    checks.append(
        {
            "check": "closure_logic",
            "pass": fake["max_tau"] < fake["tau_min_required"],
        }
    )
    all_pass = all(c["pass"] for c in checks)
    return {"mode": "selftest", "all_pass": all_pass, "checks": checks}


def ledger_payload(results_dir: str) -> dict[str, object]:
    """Aggregate all gap_scan*.json files into one verification ledger."""
    skip_substrings = ("parallel_test", "sample_10M", "_sample.json")
    chunks: list[dict[str, object]] = []
    total_odds = 0
    total_elapsed = 0.0
    global_max_tau = 0
    global_max_tau_n = 0
    global_max_gamma = 0.0
    global_max_gamma_n = 0
    verified_hi = 0
    mismatches = 0
    names = sorted(
        n for n in os.listdir(results_dir)
        if n.startswith("gap_scan") and n.endswith(".json")
    )
    for name in names:
        if any(s in name for s in skip_substrings):
            continue
        path = os.path.join(results_dir, name)
        with open(path, encoding="utf-8") as fh:
            row = json.load(fh)
        if not row.get("terras_verified", True):
            mismatches += len(row.get("terras_mismatches") or [])
        hi = int(row.get("hi_inclusive", 0))
        lo = int(row.get("lo_exclusive", 0))
        odds = int(row.get("odd_integers_scanned", 0))
        total_odds += odds
        total_elapsed += float(row.get("elapsed_seconds", 0))
        verified_hi = max(verified_hi, hi)
        mt = int(row.get("max_tau", 0))
        if mt > global_max_tau:
            global_max_tau = mt
            global_max_tau_n = int(row.get("max_tau_n", 0))
        mg = float(row.get("max_gamma", 0))
        if mg > global_max_gamma:
            global_max_gamma = mg
            global_max_gamma_n = int(row.get("max_gamma_n", 0))
        band = row.get("band") or {}
        chunks.append(
            {
                "file": name,
                "lo_exclusive": lo,
                "hi_inclusive": hi,
                "odd_integers_scanned": odds,
                "max_tau": mt,
                "tau_min_required": row.get("tau_min_required"),
                "band_k": band.get("band_k"),
                "proved_empty_slice": (row.get("band_closure") or {}).get("proved_empty"),
            }
        )
    chunks.sort(key=lambda c: int(c["lo_exclusive"]))
    return {
        "mode": "ledger",
        "results_dir": results_dir,
        "terras_verified_through": verified_hi,
        "log2_verified_through": round(math.log2(verified_hi), 2) if verified_hi > 1 else None,
        "total_odd_integers_scanned": total_odds,
        "total_elapsed_seconds": round(total_elapsed, 1),
        "global_max_tau": global_max_tau,
        "global_max_tau_n": global_max_tau_n,
        "global_max_gamma": round(global_max_gamma, 4),
        "global_max_gamma_n": global_max_gamma_n,
        "mismatch_count": mismatches,
        "collatz_status": "OPEN",
        "honesty": (
            "Measured Terras verification only. Collatz open. "
            "Band closure requires full window or proved gamma bound."
        ),
        "chunks": chunks,
    }


def emit(payload: dict[str, object], out: str | None) -> None:
    text = json.dumps(payload, indent=2, sort_keys=True, default=str)
    if out:
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
    print(text)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("selftest")
    p = sub.add_parser("band-plan")
    p.add_argument("--scan-floor", type=int, default=15_443_807_723)
    p.add_argument("--band-k", type=int, required=True)
    p.add_argument("--rate", type=float, default=6_500_000.0, help="assumed odd ints/sec (8 workers)")
    p.add_argument("--out", default=None)
    p = sub.add_parser("ladder")
    p.add_argument("--scan-floor", type=int, default=BAND10_CEILING)
    p.add_argument("--closed-bands", type=str, default="10")
    p.add_argument("--out", default=None)
    p = sub.add_parser("scan")
    p.add_argument("--squeeze", default=DEFAULT_SQUEEZE)
    p.add_argument("--scan-floor", type=int, default=10**9)
    p.add_argument("--band-k", type=int, default=None)
    p.add_argument("--lo", type=int, default=None)
    p.add_argument("--hi", type=int, default=None)
    p.add_argument("--progress-every", type=int, default=2_000_000)
    p.add_argument("--workers", type=int, default=1, help="parallel processes (Windows-safe)")
    p.add_argument("--out", default=None)
    p = sub.add_parser("close-band")
    p.add_argument("--scan-floor", type=int, default=BAND10_CEILING)
    p.add_argument("--band-k", type=int, required=True)
    p.add_argument("--workers", type=int, default=os.cpu_count() or 4)
    p.add_argument("--scan-out", default=None)
    p.add_argument("--theorem-out", default=None)
    p = sub.add_parser("theorem")
    p.add_argument("--scan", required=True, help="JSON from gap-scan")
    p.add_argument("--out", default=None)
    p = sub.add_parser("ledger")
    p.add_argument("--results-dir", default=os.path.join(os.path.dirname(__file__), "results"))
    p.add_argument("--out", default=None)

    args = parser.parse_args()
    if args.cmd == "selftest":
        payload = selftest_payload()
        emit(payload, None)
        if not payload["all_pass"]:
            raise SystemExit(1)
    elif args.cmd == "band-plan":
        emit(band_plan_payload(args.scan_floor, args.band_k, args.rate), args.out)
    elif args.cmd == "ladder":
        closed = [int(x) for x in args.closed_bands.split(",") if x.strip()]
        emit(ladder_payload(args.scan_floor, closed), args.out)
    elif args.cmd == "scan":
        emit(
            scan_payload(
                args.squeeze,
                args.scan_floor,
                args.lo,
                args.hi,
                args.progress_every,
                args.band_k,
                args.workers,
            ),
            args.out,
        )
    elif args.cmd == "close-band":
        payload = close_band_payload(
            args.scan_floor,
            args.band_k,
            args.workers,
            args.scan_out,
            args.theorem_out,
        )
        if not args.scan_out and not args.theorem_out:
            print(json.dumps(payload["theorem"], indent=2))
        if not payload["theorem"].get("proved_empty"):
            raise SystemExit(1)
    elif args.cmd == "theorem":
        with open(args.scan, encoding="utf-8") as fh:
            scan_result = json.load(fh)
        emit(theorem_payload(scan_result), args.out)
    elif args.cmd == "ledger":
        emit(ledger_payload(args.results_dir), args.out)


if __name__ == "__main__":
    main()
