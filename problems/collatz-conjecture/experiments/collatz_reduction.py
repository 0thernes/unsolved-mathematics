#!/usr/bin/env python3
"""Master reduction: Collatz <=> Terras + frontier separation (+ cycle bounds).

Chains the proved lemmas from Sessions 1-5 into one executable certificate and
adds the delta-squeeze band classification: which convergent bands can still
host a Terras violation beyond the 10^9 scan.

Delta-squeeze (proved).  A Terras violation with odd count o in convergent band
[q_k, q_{k+1}) satisfies

    n <= o / (2 ln2 * delta(o)),     delta(o) >= ||q_k log2 3||  (Lagrange),

so n <= o / (2 ln2 * d_lo) with d_lo = ||q_k log2 3||.  Past scan floor N,
need o >= o_need(N) := floor(2 N ln2 d_lo) + 1.  If o_need >= q_{k+1}, the
entire band is excluded: no odd count in [q_k, q_{k+1}) can yield X(o) > N.

Combined with tau = sigma for all n <= N (measured), bands with o_need >= q_{k+1}
are **proved empty** of Terras violations beyond N without any further scan.

Subcommands: selftest, squeeze, reduction.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from fractions import Fraction
from time import perf_counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from collatz_record_band import (  # noqa: E402
    SCAN_FLOOR,
    alpha_interval,
    band_table,
    ceil_o_alpha,
    certified_convergents,
    dist_lower,
    log2_big,
    theorem_payload,
)

# ---------------------------------------------------------------------------
# Delta-squeeze band classification
# ---------------------------------------------------------------------------


def band_squeeze_row(
    k: int,
    p: int,
    q: int,
    p2: int,
    q2: int,
    scan_floor: int,
    alpha_lo: Fraction,
    alpha_hi: Fraction,
    ln2_lo: Fraction,
) -> dict[str, object]:
    d_lo = dist_lower(p, q, alpha_lo, alpha_hi)
    o_need = int(2 * scan_floor * ln2_lo * d_lo) + 1
    o_min = max(o_need, q)
    if o_min >= q2:
        return {
            "band_k": k,
            "q_k": q,
            "q_k+1": q2,
            "delta_lower": float(d_lo),
            "o_need": o_need,
            "o_min": o_min,
            "status": "PROVED_EMPTY",
            "reason": "o_need >= q_{k+1}: no odd count in band yields X(o) > scan_floor",
        }
    x_tight = Fraction(o_min, 2) / (ln2_lo * d_lo)
    log2_x = log2_big(x_tight.numerator) - log2_big(x_tight.denominator)
    tau_min = ceil_o_alpha(o_min, alpha_lo, alpha_hi)
    gamma_at_ceiling = tau_min / math.ceil(log2_x)
    if x_tight <= scan_floor:
        return {
            "band_k": k,
            "q_k": q,
            "q_k+1": q2,
            "delta_lower": float(d_lo),
            "o_need": o_need,
            "o_min": o_min,
            "tau_min": tau_min,
            "n_ceiling": int(x_tight),
            "log2_n_ceiling": round(log2_x, 3),
            "status": "PROVED_EMPTY",
            "reason": "tight ceiling <= scan_floor",
        }
    return {
        "band_k": k,
        "q_k": q,
        "q_k+1": q2,
        "delta_lower": float(d_lo),
        "o_need": o_need,
        "o_min": o_min,
        "tau_min": tau_min,
        "n_ceiling": int(x_tight),
        "log2_n_ceiling": round(log2_x, 3),
        "gamma_floor_at_ceiling": round(gamma_at_ceiling, 1),
        "status": "SCAN_GAP",
        "reason": (
            f"violations past {scan_floor} need n in ({scan_floor}, {int(x_tight)}] "
            f"with tau >= {tau_min}; not covered by scan"
        ),
    }


def squeeze_payload(digits: int, scan_floor: int, max_bands: int) -> dict[str, object]:
    started = perf_counter()
    alpha_lo, alpha_hi, ln2_lo = alpha_interval(digits)
    convs = certified_convergents(digits, 10**14)
    rows = []
    for k in range(min(len(convs) - 1, max_bands)):
        (p, q), (p2, q2) = convs[k], convs[k + 1]
        if q2 <= q:
            continue
        rows.append(
            band_squeeze_row(k, p, q, p2, q2, scan_floor, alpha_lo, alpha_hi, ln2_lo)
        )
    proved_empty = [r for r in rows if r["status"] == "PROVED_EMPTY"]
    scan_gaps = [r for r in rows if r["status"] == "SCAN_GAP"]
    first_open = scan_gaps[0] if scan_gaps else None
    return {
        "mode": "squeeze",
        "elapsed_seconds": round(perf_counter() - started, 3),
        "scan_floor": scan_floor,
        "scan_input": f"tau = sigma verified for all n <= {scan_floor}",
        "proved_empty_bands": len(proved_empty),
        "scan_gap_bands": len(scan_gaps),
        "first_open_band": first_open,
        "theorem": (
            "Past scan_floor N, a Terras violation needs odd count o with X(o) > N. "
            "In band [q_k, q_{k+1}), Lagrange gives X(o) <= o/(2 ln2 ||q_k log2 3||); "
            "if floor(2 N ln2 ||q_k log2 3||)+1 >= q_{k+1}, the band is proved empty."
        ),
        "bands": rows,
    }


# ---------------------------------------------------------------------------
# Master reduction
# ---------------------------------------------------------------------------


def reduction_payload(digits: int) -> dict[str, object]:
    started = perf_counter()
    squeeze = squeeze_payload(digits, SCAN_FLOOR, 20)
    record = theorem_payload(digits)
    first_open = squeeze["first_open_band"]
    terras = record.get("terras_violation_floor") or {}

    chain = [
        {
            "id": "A",
            "label": "Localization (FRONTIER-GEOMETRY Thm 3)",
            "status": "PROVED",
            "statement": (
                "Any counterexample orbit minimum m has sigma(m)=infinity; "
                "either tau(m)=infinity (frontier resident) or m is below its "
                "class certificate threshold at depth tau(m)."
            ),
        },
        {
            "id": "B",
            "label": "Threshold vacuity (THRESHOLD-ENVELOPE)",
            "status": "PROVED",
            "statement": (
                "No certified class traps n >= 2^d at any depth; Terras violations "
                "must satisfy n < 2^tau(n) (certificate-record integers, gamma > 1)."
            ),
        },
        {
            "id": "C",
            "label": "Record ceiling (RECORD-BAND)",
            "status": "PROVED",
            "statement": (
                "Alive Terras violations obey n <= o/(2 ln2 delta(o)); per convergent "
                "band this gives explicit gamma floors (first open: "
                f"gamma >= {terras.get('gamma_floor', '?')})."
            ),
        },
        {
            "id": "D",
            "label": "Delta-squeeze band exclusion (this lab)",
            "status": "PROVED",
            "statement": (
                f"{squeeze['proved_empty_bands']} convergent bands below the first "
                f"open band are proved empty of Terras violations past {SCAN_FLOOR}."
            ),
        },
        {
            "id": "E",
            "label": "Terras scan",
            "status": "MEASURED",
            "statement": f"tau(n) = sigma(n) for all 1 < n <= {SCAN_FLOOR} (zero exceptions).",
        },
        {
            "id": "F",
            "label": "eps-invariance barrier (SIBLING-CONTROL)",
            "status": "PROVED",
            "statement": (
                "Parity-word statistics cannot separate Collatz from 3n-1; proofs must "
                "consume intercept sign (eps=+1)."
            ),
        },
    ]

    reductions = {
        "collatz_full": (
            "Every positive integer reaches 1 (no divergent orbit, no nontrivial cycle)."
        ),
        "under_terras": (
            "Collatz <=> S intersect Z_{>0} = empty (frontier has no positive integers). "
            "Terras (tau=sigma) already implies no nontrivial cycle."
        ),
        "unconditional_terras_half": (
            "Terras conjecture <=> no certificate-record integer r with T^tau(r) >= r "
            "(self-trap / gamma > 1 band)."
        ),
        "first_open_band": (
            None
            if first_open is None
            else (
                f"First band not proved empty: o in [{first_open['q_k']}, "
                f"{first_open['q_k+1']}), tau >= {first_open['tau_min']}, "
                f"n <= {first_open['n_ceiling']} (2^{first_open['log2_n_ceiling']}), "
                f"gamma >= {first_open.get('gamma_floor_at_ceiling', '?')}."
            )
        ),
        "cycle_conditional": record.get("cycle_corollary", {}).get("statement"),
    }

    open_exactly = [
        "SCAN_GAP: Terras violations in the first open band need n in a finite window "
        f"above {SCAN_FLOOR} not yet scanned (width ~2^{float(first_open['log2_n_ceiling']) - 30:.1f} "
        "bits if first_open else 'n/a').",
        "Frontier residents (tau=infinity): positive integers in survivor set S — divergence.",
        "Pointwise extreme-value gap: no theorem yet that gamma(n) <= 19.982 for all n.",
        "Cycles beyond 2^71: excluded computationally; structural gamma >= 10^9 floor proved.",
    ]

    return {
        "mode": "reduction",
        "elapsed_seconds": round(perf_counter() - started, 3),
        "honesty": (
            "This instrument chains proved and measured lemmas. It does NOT prove Collatz. "
            "The reduction identifies the exact residue: Terras record-band integers, "
            "frontier residents, and the finite scan gaps between proved band ceilings."
        ),
        "proof_chain": chain,
        "reductions": reductions,
        "squeeze_summary": {
            "proved_empty_bands": squeeze["proved_empty_bands"],
            "first_open_band": first_open,
        },
        "record_band_summary": terras,
        "open_exactly": open_exactly,
    }


# ---------------------------------------------------------------------------
# Self tests
# ---------------------------------------------------------------------------


def selftest_payload() -> dict[str, object]:
    checks = []
    sq = squeeze_payload(320, SCAN_FLOOR, 16)
    rows = sq["bands"]

    # 1. Bands 8 and 9 (665..31867) proved empty past 10^9
    by_q = {r["q_k"]: r for r in rows}
    for q in (665, 15601):
        r = by_q.get(q)
        ok = r is not None and r["status"] == "PROVED_EMPTY"
        checks.append({"check": f"band_q_{q}_proved_empty", "pass": ok, "row": r})

    # 2. First open band is q=31867
    first = sq["first_open_band"]
    ok2 = first is not None and first["q_k"] == 31867 and first["status"] == "SCAN_GAP"
    checks.append({"check": "first_open_band_is_31867", "pass": ok2, "first": first})

    # 3. Tight ceiling at first open: log2 n ~ 31.03
    if first:
        log2x = first["log2_n_ceiling"]
        ok3 = 30.5 <= log2x <= 31.5
        checks.append(
            {
                "check": "first_open_log2_ceiling_near_31",
                "log2_n_ceiling": log2x,
                "pass": ok3,
            }
        )

    # 4. Reduction payload loads and has six chain steps
    red = reduction_payload(320)
    ok4 = len(red["proof_chain"]) == 6 and red["squeeze_summary"]["proved_empty_bands"] >= 9
    checks.append(
        {
            "check": "reduction_chain_complete",
            "proved_empty_bands": red["squeeze_summary"]["proved_empty_bands"],
            "pass": ok4,
        }
    )

    # 5. Monotone: o_need decreases as delta decreases along ladder
    o_needs = [r["o_need"] for r in rows if "o_need" in r]
    ok5 = all(o_needs[i] >= o_needs[i + 1] for i in range(len(o_needs) - 1))
    checks.append({"check": "o_need_monotone_decreasing", "pass": ok5})

    all_pass = all(c["pass"] for c in checks)
    return {"mode": "selftest", "all_pass": all_pass, "checks": checks}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


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
    p = sub.add_parser("squeeze")
    p.add_argument("--digits", type=int, default=320)
    p.add_argument("--scan-floor", type=int, default=SCAN_FLOOR)
    p.add_argument("--max-bands", type=int, default=20)
    p.add_argument("--out", default=None)
    p = sub.add_parser("reduction")
    p.add_argument("--digits", type=int, default=320)
    p.add_argument("--out", default=None)

    args = parser.parse_args()
    if args.cmd == "selftest":
        payload = selftest_payload()
        emit(payload, None)
        if not payload["all_pass"]:
            raise SystemExit(1)
    elif args.cmd == "squeeze":
        emit(
            squeeze_payload(args.digits, args.scan_floor, args.max_bands),
            args.out,
        )
    elif args.cmd == "reduction":
        emit(reduction_payload(args.digits), args.out)


if __name__ == "__main__":
    main()
