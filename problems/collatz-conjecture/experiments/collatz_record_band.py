#!/usr/bin/env python3
"""The record band: an explicit ceiling on every possible Terras violation.

THRESHOLD-ENVELOPE.md proved that any violation of Terras' coefficient
stopping time conjecture (an n >= 2 with sigma(n) > tau(n)) must satisfy
n < 2^tau(n): the violator IS the residue of its own certified class, which
is alive (supercritical) at every proper prefix.  This lab bounds how large
such an n can be, per depth, and converts the bound into a gamma floor.

Lemma (alive intercept bound - proved, verified exhaustively).  If a parity
word of length d is supercritical at every proper prefix (3^{o(j)} >= 2^j for
all j < d) with o odd steps at positions s_1 < ... < s_o (1-indexed), then
aliveness pins the odd steps early: 3^j >= 2^{s_j} gives 2^{s_j - 1} <= 3^j/2,
so

    c(w) = sum_j 3^{o-j} 2^{s_j - 1}  <=  sum_j 3^{o-j} 3^j / 2  =  o 3^o / 2.

(The generic bound is 2^{d-o}(3^o - 2^o) ~ (3/2)^o 2^d; aliveness improves it
by the exponential factor 2^d/3^o >= 1 -> the whole theorem lives here.)

Theorem (violation ceiling).  A Terras violation n with tau(n) = d and odd
count o satisfies n <= x* = c/(2^d - 3^o) <= (o/2) * 3^o/(2^d - 3^o).  With
delta = d - o log2(3) in (0, 1) (d is pinned: certificates end at the first
subcritical depth), 2^d - 3^o = 3^o(2^delta - 1) >= 3^o delta ln 2, so

    n  <=  X(o) := o / (2 ln2 * delta(o)),      delta(o) = ceil(o a) - o a,
                                                 a = log2 3.

By Lagrange's best-approximation theorem, for q_k <= o < q_{k+1} (convergent
denominators of log2 3), delta(o) >= ||o a|| >= ||q_k a||, certified exactly
by the in-repo interval continued fraction.  So X is explicitly bounded per
band, and combined with the 10^9 tau-scan (no violations below 10^9), any
surviving violation needs o and d = tau in explicit ranges with

    gamma(n) = tau(n)/log2(n) >= d(o_min) / log2(X_band)  ~  10^3,

versus the Borel-Cantelli ceiling 19.982 and the all-time measured record
14.5.  The floor grows without bound along the convergent ladder.

This does not prove Terras' conjecture (the random-model ceiling is not a
theorem); it proves that a violation must be a certificate-depth record
integer categorically beyond the extreme-value regime.

Subcommands: selftest, ceiling, theorem.
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
from collatz_frontier_geometry import KNOWN_CF_PREFIX, cf_terms_interval, ln_bounds  # noqa: E402

SCAN_FLOOR = 10**9  # tau = sigma verified for all n <= 10^9 (results/tau_scan_1e9.json)


def log2_big(x: int) -> float:
    b = x.bit_length()
    if b <= 60:
        return math.log2(x)
    return (b - 60) + math.log2(x >> (b - 60))


def alpha_interval(digits: int) -> tuple[Fraction, Fraction, Fraction]:
    scale = 10**digits
    (l2lo, l2hi), (l3lo, l3hi) = ln_bounds(scale)
    return Fraction(l3lo, l2hi), Fraction(l3hi, l2lo), Fraction(l2lo, scale)


def certified_convergents(digits: int, max_q: int) -> list[tuple[int, int]]:
    alpha_lo, alpha_hi, _ = alpha_interval(digits)
    terms = cf_terms_interval(alpha_lo, alpha_hi, 400)
    if terms[: len(KNOWN_CF_PREFIX)] != KNOWN_CF_PREFIX:
        raise AssertionError("certified CF prefix failed the literature check")
    out = []
    p_prev2, p_prev = 0, 1
    q_prev2, q_prev = 1, 0
    for a in terms:
        p = a * p_prev + p_prev2
        q = a * q_prev + q_prev2
        p_prev2, p_prev = p_prev, p
        q_prev2, q_prev = q_prev, q
        out.append((p, q))
        if q > max_q:
            break
    return out


def dist_lower(p: int, q: int, alpha_lo: Fraction, alpha_hi: Fraction) -> Fraction:
    """Certified lower bound for |q*alpha - p|."""
    conv = Fraction(p, q)
    if conv < alpha_lo:
        return q * (alpha_lo - conv)
    if conv > alpha_hi:
        return q * (conv - alpha_hi)
    raise AssertionError("convergent inside alpha interval; raise digits")


# ---------------------------------------------------------------------------
# Band ceilings
# ---------------------------------------------------------------------------


def ceil_o_alpha(o: int, alpha_lo: Fraction, alpha_hi: Fraction) -> int:
    """Certified ceil(o * log2 3) without constructing 3^o."""
    t_lo = o * alpha_lo
    t_hi = o * alpha_hi
    f_lo = t_lo.numerator // t_lo.denominator
    f_hi = t_hi.numerator // t_hi.denominator
    if f_lo != f_hi:
        raise AssertionError("alpha interval too wide to certify ceil(o*alpha); raise digits")
    return f_lo + 1


def band_table(digits: int, floors: list[int], max_bands: int) -> dict[str, object]:
    alpha_lo, alpha_hi, ln2_lo = alpha_interval(digits)
    convs = certified_convergents(digits, 10**14)
    bands = []
    summaries: dict[str, dict[str, object]] = {}
    for k in range(min(len(convs) - 1, max_bands)):
        (p, q), (p2, q2) = convs[k], convs[k + 1]
        if q2 <= q:
            continue  # degenerate band (the two q=1 convergents)
        # for q <= o < q2: delta(o) >= ||o alpha|| >= ||q alpha|| >= d_lo (Lagrange)
        d_lo = dist_lower(p, q, alpha_lo, alpha_hi)
        # X_upper(o) = o / (2 ln2 delta) is increasing in o
        x_band_hi = Fraction(q2 - 1, 2) / (ln2_lo * d_lo)
        log2_x = log2_big(x_band_hi.numerator) - log2_big(x_band_hi.denominator)
        row: dict[str, object] = {
            "band_k": k,
            "q_k": q,
            "q_k+1": q2,
            "delta_lower_bound_float": float(d_lo),
            "log2_X_ceiling_at_band_end": round(log2_x, 2),
        }
        for floor_n in floors:
            key = f"floor_{floor_n}"
            if x_band_hi <= floor_n:
                continue
            # smallest o in band with X_upper(o) > floor_n
            o_min = max(int(2 * floor_n * ln2_lo * d_lo) + 1, q)
            if o_min >= q2:
                continue
            tau_min = ceil_o_alpha(o_min, alpha_lo, alpha_hi)
            gamma_floor = tau_min / math.ceil(log2_x)
            row[f"gamma_floor_{key}"] = round(gamma_floor, 1)
            cur = summaries.get(key)
            if cur is None:
                summaries[key] = {
                    "floor_n": floor_n,
                    "first_feasible_band_q": q,
                    "o_min": o_min,
                    "tau_min": tau_min,
                    "log2_X_band_ceiling": round(log2_x, 2),
                    "gamma_floor": round(gamma_floor, 1),
                }
            elif gamma_floor < cur["gamma_floor"]:
                cur["gamma_floor"] = round(gamma_floor, 1)
                cur["note"] = f"minimum attained in later band q={q}"
        bands.append(row)
    return {
        "mode": "ceiling",
        "digits": digits,
        "floors": floors,
        "summaries": summaries,
        "bands": bands,
    }


# ---------------------------------------------------------------------------
# Theorem driver
# ---------------------------------------------------------------------------


def theorem_payload(digits: int) -> dict[str, object]:
    started = perf_counter()
    table = band_table(digits, [SCAN_FLOOR, 1 << 71], 24)
    scan_summary = table["summaries"].get(f"floor_{SCAN_FLOOR}")
    cyc_summary = table["summaries"].get(f"floor_{1 << 71}")
    gamma_floor = scan_summary["gamma_floor"] if scan_summary else None
    return {
        "mode": "theorem",
        "elapsed_seconds": round(perf_counter() - started, 3),
        "lemma": "alive words have c(w) <= o 3^o / 2 (exhaustively verified to depth 18)",
        "ceiling": "Terras violations with tau = d, odd count o satisfy n <= o/(2 ln2 delta(o))",
        "scan_input": f"tau = sigma verified for all n <= {SCAN_FLOOR} (results/tau_scan_1e9.json)",
        "terras_violation_floor": scan_summary,
        "gamma_floor": gamma_floor,
        "verdict": (
            f"Any Terras violation beyond the 10^9 scan requires a certificate-record "
            f"integer with gamma = tau/log2(n) >= {gamma_floor}, vs the Borel-Cantelli "
            f"ceiling 19.982 and the measured record 14.503; the floor grows without "
            f"bound along the convergent ladder of log2 3."
        ),
        "cycle_corollary": {
            "statement": (
                "A nontrivial cycle minimum m exceeds 2^71 (Barina) and satisfies "
                "m <= X(tau(m)); the first band whose ceiling clears 2^71 gives the "
                "minimum odd count of its certificate prefix."
            ),
            "band_summary": cyc_summary,
            "note": (
                "independent second derivation of the ~5e10-scale cycle wall: the "
                "alive-intercept route hits the same convergent ladder of log2 3 as "
                "the product-formula routes (FRONTIER-GEOMETRY.md Theorem 6, "
                "CYCLE-BOUND-LAB.md)"
            ),
        },
        "honesty": (
            "This does not prove Terras' conjecture: the 19.982 ceiling is a random-"
            "model prediction, not a theorem. What is proved is the ceiling X(o) and "
            "hence the gamma floor; a genuine violation would have to be an integer "
            "whose first tau steps are supercritical yet whose value is exponentially "
            "small relative to 2^tau - a conspiracy this bound quantifies exactly."
        ),
        "bands": table["bands"][:14],
    }


# ---------------------------------------------------------------------------
# Self tests
# ---------------------------------------------------------------------------


def alive_words_c(d: int):
    """Yield (o, c) for every parity word of length d alive at all proper prefixes."""
    stack = [(0, 0, 0, 1)]  # depth, o, c, pow3
    while stack:
        depth, o, c, p3 = stack.pop()
        if depth == d:
            yield o, c
            continue
        # next step at position depth+1 (1-indexed); prefix j = depth must be alive
        # aliveness for proper prefixes j < d checked before pushing children
        for bit in (0, 1):
            o2 = o + bit
            c2 = 3 * c + (1 << depth) if bit else c
            p32 = p3 * 3 if bit else p3
            j = depth + 1
            if j < d and p32 < (1 << j):
                continue  # died before reaching length d
            stack.append((j, o2, c2, p32))


def selftest_payload() -> dict[str, object]:
    checks = []

    # 1. alive intercept lemma, exhaustive to depth 18, with tightness ratio
    ok = True
    worst = 0.0
    for d in range(2, 19):
        for o, c in alive_words_c(d):
            if o == 0:
                continue
            bound = o * 3**o // 2
            if c > bound:
                ok = False
            r = c / (o * 3**o / 2)
            if r > worst:
                worst = r
    checks.append(
        {
            "check": "alive_intercept_bound_exhaustive_depth_le_18",
            "worst_ratio_c_over_bound": round(worst, 4),
            "pass": ok and worst <= 1.0,
        }
    )

    # 2. ceiling dominates the exact envelope: X_hi(d) >= measured max x* at
    # the spike depths 65 and 485 (exact DP from the threshold lab)
    from collatz_threshold_envelope import envelope_rows  # noqa: E402

    env = envelope_rows(500, keep_all=True)
    by = {r["depth"]: r for r in env["rows"]}
    alpha_lo, alpha_hi, ln2_lo = alpha_interval(320)
    ok2 = True
    spike_report = []
    for dd in (65, 149, 305, 485):
        r = by.get(dd)
        if r is None or r["o"] is None:
            continue
        o = r["o"]
        # exact X bound at this (d, o): (o/2) * 3^o / (2^d - 3^o), log2 form
        gap = (1 << dd) - 3**o
        x_hi_log2 = math.log2(o / 2) + o * math.log2(3) - (log2_big(gap))
        measured = dd + r["log2_max_ratio"]  # log2(x*) = log2(ratio * 2^d)
        spike_report.append({"d": dd, "o": o, "log2_X_bound": round(x_hi_log2, 2), "log2_x*_measured": round(measured, 2)})
        if x_hi_log2 < measured:
            ok2 = False
    checks.append({"check": "ceiling_dominates_exact_envelope_at_spikes", "spikes": spike_report, "pass": ok2})

    # 3. Lagrange band bound sanity: delta(o) >= ||q_k alpha|| on sampled o
    convs = certified_convergents(320, 10**7)
    ok3 = True
    for k in range(3, 10):
        p, q = convs[k]
        p2, q2 = convs[k + 1]
        d_lo = dist_lower(p, q, alpha_lo, alpha_hi)
        for o in {q, q + 1, (q + q2) // 2, q2 - 1}:
            d = pow(3, o).bit_length()
            delta = d - Fraction(o) * alpha_hi  # certified lower bound for delta(o)
            if delta < d_lo * Fraction(999, 1000):
                ok3 = False
    checks.append({"check": "band_delta_lower_bound_sampled", "pass": ok3})

    # 4. direct self-trap rescan: no n in [2, 2*10^6] has T^tau(n) >= n
    ok4 = True
    for n in range(2, 2_000_001):
        x = n
        pw = 1
        d = 0
        while True:
            if x & 1:
                pw *= 3
                x = (3 * x + 1) >> 1
            else:
                x >>= 1
            d += 1
            if pw < (1 << d):
                break
        if x >= n:
            ok4 = False
            break
    checks.append({"check": "no_self_trap_n_le_2e6", "pass": ok4})

    # 5. X(o) formula vs exact per-class maximum at moderate depth: for every
    # class of depth d <= 20, x* <= X(o) with X computed from exact delta
    ok5 = True
    for d, row in by.items():
        if d > 400 or row["o"] is None or row["log2_max_ratio"] is None:
            continue
        o = row["o"]
        gap = (1 << d) - 3**o
        lhs_log2 = d + row["log2_max_ratio"]
        rhs_log2 = math.log2(o / 2) + o * math.log2(3) - log2_big(gap)
        if lhs_log2 > rhs_log2 + 1e-6:
            ok5 = False
    checks.append({"check": "x_star_le_ceiling_every_reported_depth_le_400", "pass": ok5})

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
    p = sub.add_parser("ceiling")
    p.add_argument("--digits", type=int, default=320)
    p.add_argument("--n-floors", type=str, default=f"{SCAN_FLOOR},{1 << 71}")
    p.add_argument("--max-bands", type=int, default=24)
    p.add_argument("--out", default=None)
    p = sub.add_parser("theorem")
    p.add_argument("--digits", type=int, default=320)
    p.add_argument("--out", default=None)

    args = parser.parse_args()
    if args.cmd == "selftest":
        payload = selftest_payload()
        emit(payload, None)
        if not payload["all_pass"]:
            raise SystemExit(1)
    elif args.cmd == "ceiling":
        floors = [int(t) for t in args.n_floors.split(",") if t.strip()]
        emit(band_table(args.digits, floors, args.max_bands), args.out)
    elif args.cmd == "theorem":
        emit(theorem_payload(args.digits), args.out)


if __name__ == "__main__":
    main()
