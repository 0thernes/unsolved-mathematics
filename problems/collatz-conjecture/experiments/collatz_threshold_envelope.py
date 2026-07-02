#!/usr/bin/env python3
"""The threshold envelope: proving certificate thresholds vacuous at ALL depths.

Setting (shortcut Collatz map, notation as in FRONTIER-GEOMETRY.md): a residue
class r mod 2^d certified at depth d (o odd steps, 3^o < 2^d) has

    T^d(2^d q + r) = 3^o (2^d q + r)/2^d + c(w)/2^d,   c(w) = 2^d T^d(r) - 3^o r,

an increasing affine map with rational fixed point

    x*(r, d) = c(w) / (2^d - 3^o),

and T^d(n) < n exactly when n > x*.  Members n <= x* are "threshold-trapped":
tau fired but descent did not (a Terras violation); an INTEGER x* would be a
genuine cycle.  Session-1 measured max thresholds <= 1 through depth 28.  This
instrument PROVES the q >= 1 part at every depth:

  Lemma (intercept bound).  c(w) <= 2^(d-o) (3^o - 2^o), with equality iff all
  odd steps come last.  (Exact induction; verified here.)

  Window theorem.  A trapped member n >= 2^d (i.e. q >= 1) requires
  x* >= 2^d, hence 2^d - 3^o < (3/2)^o, hence

      1 < 2^d / 3^o < 1 + 2^(-o).

  So a trap needs an EXPONENTIALLY good rational approximation d/o to
  log2(3) from above.  Legendre's criterion turns each candidate into a
  continued-fraction convergent, and the interval-certified convergents of
  log2(3) (already in-repo) exclude them all; tiny o is checked exactly;
  the single window hit (d, o) = (2, 1) is closed by the exact envelope DP.

  Conclusion (unconditional within the certified CF table, which reaches
  denominators ~1e150):  NO certified class at ANY depth traps any member
  n >= 2^d.  Every Terras violation n >= 2 satisfies n < 2^tau(n), i.e.
  violators are certificate-record integers (gamma = tau/log2 n > 1).

The envelope DP also computes the exact maximum of x*/2^d over all classes of
every depth ("how close the intercepts ever get to trapping"), which shows the
all-time maximum is the trivial-cycle class at depth 2 (x* = 1) and exhibits
the Diophantine ladder of log2(3) as visible spikes at convergent depths.

Nothing here proves the Collatz conjecture; the q = 0 self-trap case (n = r
with T^d(r) >= r, the "record integers") remains open and is measured by the
companion scans.

Subcommands: selftest, envelope, window, cf-exclusion, theorem.
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

LN2_OVER = math.log(2)


def log2_big(x: int) -> float:
    b = x.bit_length()
    if b <= 60:
        return math.log2(x)
    return (b - 60) + math.log2(x >> (b - 60))


# ---------------------------------------------------------------------------
# Envelope DP: exact max intercept c over alive words, per (depth, odd count)
# ---------------------------------------------------------------------------


def envelope_rows(max_depth: int, keep_all: bool = False) -> dict[str, object]:
    """For each depth d, the exact maximum of x*/2^d over every residue class
    whose certificate depth is exactly d.  Sound because c evolves by the
    monotone maps c -> c (even) and c -> 3c + 2^(depth-1) (odd), so per-(o)
    maxima propagate exactly; a class leaves (is certified) at the first even
    step that makes 3^o < 2^d."""
    states: dict[int, int] = {0: 0}
    pow3 = [1]
    rows = []
    best_overall = (Fraction(-1), 0, 0)  # (ratio, depth, o)
    for depth in range(1, max_depth + 1):
        while len(pow3) <= depth + 1:
            pow3.append(pow3[-1] * 3)
        boundary = 1 << depth
        new: dict[int, int] = {}
        leaving: dict[int, int] = {}
        for o, c in states.items():
            c_odd = 3 * c + (1 << (depth - 1))
            if c_odd > new.get(o + 1, -1):
                new[o + 1] = c_odd
            if pow3[o] >= boundary:
                if c > new.get(o, -1):
                    new[o] = c
            else:
                if c > leaving.get(o, -1):
                    leaving[o] = c
        states = new
        if leaving:
            best_ratio = Fraction(-1)
            best_o = None
            for o, c in leaving.items():
                ratio = Fraction(c, (boundary - pow3[o]) * boundary)  # x*/2^d
                if ratio > best_ratio:
                    best_ratio, best_o = ratio, o
            if best_ratio > best_overall[0]:
                best_overall = (best_ratio, depth, best_o)
            rows.append(
                {
                    "depth": depth,
                    "o": best_o,
                    "max_xstar_over_2^d": float(best_ratio) if best_ratio.denominator.bit_length() < 900 else None,
                    "log2_max_ratio": round(log2_big(best_ratio.numerator) - log2_big(best_ratio.denominator), 3)
                    if best_ratio > 0 else None,
                    "max_xstar_exact": str(Fraction(leaving[best_o], boundary - pow3[best_o])) if depth <= 20 else None,
                    "trap_possible_q_ge_1": best_ratio >= 1,
                }
            )
    peak = best_overall
    return {
        "rows": rows if keep_all else [r for r in rows if r["depth"] <= 16 or r["depth"] % (max_depth // 64 or 1) == 0 or r["depth"] == max_depth or (r["o"] is not None and r["log2_max_ratio"] is not None and r["log2_max_ratio"] > -40)],
        "all_time_peak": {
            "ratio": float(peak[0]),
            "depth": peak[1],
            "o": peak[2],
        },
        "any_trap_possible": any(r["trap_possible_q_ge_1"] for r in rows),
    }


def brute_envelope(max_depth: int) -> dict[int, Fraction]:
    """Exact max x*/2^d per depth by enumerating every residue class."""
    out: dict[int, tuple[Fraction, int]] = {}
    limit = 1 << max_depth
    for r in range(limit):
        x = r
        pw = 1
        o = 0
        for d in range(1, max_depth + 1):
            if x & 1:
                o += 1
                pw *= 3
                x = (3 * x + 1) >> 1
            else:
                x >>= 1
            if pw < (1 << d):
                break
        else:
            continue
        # r's class mod 2^d is certified at depth d; but each class is counted
        # once via its smallest representative r < 2^d
        if r < (1 << d):
            c = (1 << d) * x - pw * r
            ratio = Fraction(c, ((1 << d) - pw) * (1 << d))
            cur = out.get(d)
            if cur is None or ratio > cur[0]:
                out[d] = (ratio, r)
    return {d: v[0] for d, v in out.items()}


# ---------------------------------------------------------------------------
# Window scan: exact small-o check of 2^d < 3^o + (3/2)^o
# ---------------------------------------------------------------------------


def window_payload(o_max: int) -> dict[str, object]:
    hits = []
    margins = []
    for o in range(1, o_max + 1):
        p3 = 3**o
        d = p3.bit_length()  # minimal d with 2^d > 3^o
        # window: 2^(d+o) < 3^o (2^o + 1); larger d fails since 2^(d+1)/3^o >= 2
        in_window = (1 << (d + o)) < p3 * ((1 << o) + 1)
        if in_window:
            hits.append({"o": o, "d": d})
        if o <= 64:
            margins.append(
                {
                    "o": o,
                    "d": d,
                    "log2_gap": round(log2_big((1 << d) - p3), 3),
                    "log2_intercept_cap_(3/2)^o": round(o * (math.log2(3) - 1), 3),
                    "in_window": in_window,
                }
            )
    return {
        "mode": "window",
        "o_max": o_max,
        "statement": "a q>=1 threshold trap at (d, o) requires 2^d - 3^o < (3/2)^o with 3^o < 2^d",
        "hits": hits,
        "sample_margins": margins[:24],
    }


# ---------------------------------------------------------------------------
# CF exclusion for all large o
# ---------------------------------------------------------------------------


def cf_exclusion_payload(digits: int) -> dict[str, object]:
    scale = 10**digits
    (l2lo, l2hi), (l3lo, l3hi) = ln_bounds(scale)
    alpha_lo = Fraction(l3lo, l2hi)
    alpha_hi = Fraction(l3hi, l2lo)
    terms = cf_terms_interval(alpha_lo, alpha_hi, 400)
    if terms[: len(KNOWN_CF_PREFIX)] != KNOWN_CF_PREFIX:
        raise AssertionError("certified CF prefix failed the literature check")

    convergents = []
    p_prev2, p_prev = 0, 1
    q_prev2, q_prev = 1, 0
    max_q = 0
    all_excluded = True
    for k, a in enumerate(terms):
        p = a * p_prev + p_prev2
        q = a * q_prev + q_prev2
        p_prev2, p_prev = p_prev, p
        q_prev2, q_prev = q_prev, q
        max_q = q
        conv = Fraction(p, q)
        if alpha_lo <= conv <= alpha_hi:
            raise AssertionError("convergent inside alpha interval; raise --digits")
        if conv < alpha_lo:
            continue  # traps need d/o > alpha: only above-side convergents matter
        gap_lo = conv - alpha_hi
        # A trap in the Legendre branch has odd count o >= 8 and o >= q (q | o),
        # and its window is w(o) = 2^-o/(o ln2), decreasing in o.  So the
        # sufficient exclusion test is gap_lo >= W_hi(max(q, 8)).
        o_eff = max(q, 8) if q <= 64 else q
        if q <= 64:
            w_hi = Fraction(scale, o_eff * l2lo) / (1 << o_eff)
            excluded = gap_lo >= w_hi
            method = "exact"
        else:
            # bit-length comparison with 4 bits of slack:
            # gap_lo * q * l2lo * 2^q >= scale  is implied by
            # log2(gap_lo) + log2(q) + log2(l2lo) + q >= log2(scale) + 4
            lhs = (
                (gap_lo.numerator.bit_length() - 1 - gap_lo.denominator.bit_length())
                + (q.bit_length() - 1)
                + (l2lo.bit_length() - 1)
                + q
            )
            excluded = lhs >= scale.bit_length() + 4
            method = "bit-length"
        all_excluded = all_excluded and excluded
        convergents.append(
            {
                "k": k,
                "q": str(q),
                "p": str(p),
                "log2_gap_lower": round(log2_big(gap_lo.numerator) - log2_big(gap_lo.denominator), 2),
                "log2_window_upper": -q + round(math.log2(1.0 / (min(q, 10**6) * 0.69)), 2) if q <= 10**6 else -q,
                "excluded": excluded,
                "method": method,
            }
        )

    return {
        "mode": "cf-exclusion",
        "digits": digits,
        "certified_terms": len(terms),
        "max_certified_denominator_log10": round(log2_big(max_q) * math.log10(2), 1),
        "legendre_note": (
            "for o >= 8 a trap forces d/o (reduced p/q, q | o) to be an above-side "
            "convergent of log2 3 with p/q - alpha < 2^-q/(q ln 2); q in {1,2,3} is "
            "excluded by the fixed distances 0.415/0.085/0.082 for o >= 8; o <= 256 "
            "is checked exactly by the window scan"
        ),
        "above_side_convergents_checked": len(convergents),
        "all_excluded": all_excluded,
        "convergents": convergents,
    }


# ---------------------------------------------------------------------------
# Theorem driver
# ---------------------------------------------------------------------------


def theorem_payload(max_depth: int, o_max: int, digits: int) -> dict[str, object]:
    started = perf_counter()
    win = window_payload(o_max)
    cf = cf_exclusion_payload(digits)
    env = envelope_rows(max_depth)

    # close each window hit with the exact envelope DP value at that (d, o)
    closures = []
    hits_closed = True
    for hit in win["hits"]:
        d, o = hit["d"], hit["o"]
        states: dict[int, int] = {0: 0}
        target_c = None
        for depth in range(1, d + 1):
            new: dict[int, int] = {}
            for oo, c in states.items():
                c_odd = 3 * c + (1 << (depth - 1))
                if c_odd > new.get(oo + 1, -1):
                    new[oo + 1] = c_odd
                if 3**oo >= (1 << depth):
                    if c > new.get(oo, -1):
                        new[oo] = c
                elif depth == d and oo == o:
                    if target_c is None or c > target_c:
                        target_c = c
            states = new
        gap = (1 << d) - 3**o
        closed = target_c is not None and target_c < (1 << d) * gap
        hits_closed = hits_closed and closed
        closures.append(
            {
                "d": d,
                "o": o,
                "max_intercept_c": target_c,
                "required_for_trap": (1 << d) * gap,
                "max_xstar": str(Fraction(target_c, gap)) if target_c is not None else None,
                "closed": closed,
            }
        )

    verdict = win["o_max"] >= 256 and cf["all_excluded"] and hits_closed and not env["any_trap_possible"]
    return {
        "mode": "theorem",
        "elapsed_seconds": round(perf_counter() - started, 3),
        "theorem": (
            "No certified Collatz residue class at any depth traps a member "
            "n >= 2^d: for every n >= 2 with n >= 2^tau(n), sigma(n) = tau(n). "
            "Every Terras violation is a certificate-record integer (n < 2^tau(n))."
        ),
        "proof_chain": {
            "intercept_bound_lemma": "c(w) <= 2^(d-o)(3^o - 2^o), exact induction (selftest-verified)",
            "window_reduction": "trap with q>=1 => 1 < 2^d/3^o < 1 + 2^-o",
            "small_o_exact": {"o_max": win["o_max"], "hits": win["hits"]},
            "hit_closures_by_exact_DP": closures,
            "large_o_CF_exclusion": {
                "all_excluded": cf["all_excluded"],
                "convergents_checked": cf["above_side_convergents_checked"],
                "coverage_log10_denominator": cf["max_certified_denominator_log10"],
            },
            "envelope_confirmation": {
                "max_depth_computed": max_depth,
                "any_trap_possible": env["any_trap_possible"],
                "all_time_peak_xstar_over_2^d": env["all_time_peak"],
            },
        },
        "verdict": "PROVED (within certified CF coverage, denominators to ~1e"
        + str(int(cf["max_certified_denominator_log10"])) + ")" if verdict else "NOT ESTABLISHED",
        "honesty": (
            "The q = 0 case (n = r with T^d(r) >= r, i.e. certificate-record "
            "integers with gamma > 1) is NOT excluded by this theorem; it is "
            "measured empty to 10^9 by the tau-scan and remains the entire "
            "content of Terras' conjecture."
        ),
    }


# ---------------------------------------------------------------------------
# Self tests
# ---------------------------------------------------------------------------


def selftest_payload() -> dict[str, object]:
    checks = []

    # 1. intercept recursion and exact bound at depth <= 14 (all words)
    ok_bound = True
    ok_tight = True
    for d in range(1, 15):
        best = {}
        for word in range(1 << d):
            c = 0
            o = 0
            for j in range(d):
                if (word >> j) & 1:
                    c = 3 * c + (1 << j)
                    o += 1
            bound = (1 << (d - o)) * (3**o - (1 << o)) if o else 0
            if c > bound:
                ok_bound = False
            best[o] = max(best.get(o, -1), c)
        for o, c in best.items():
            bound = (1 << (d - o)) * (3**o - (1 << o)) if o else 0
            if c != bound:
                ok_tight = False
    checks.append({"check": "intercept_bound_exact_and_tight_depth_le_14", "pass": ok_bound and ok_tight})

    # 2. DP envelope vs brute-force class enumeration through depth 15
    dp = envelope_rows(15, keep_all=True)
    dp_map = {r["depth"]: r for r in dp["rows"]}
    brute = brute_envelope(15)
    ok_env = True
    for d, ratio in brute.items():
        row = dp_map.get(d)
        got = None if row is None else row["max_xstar_over_2^d"]
        if got is None or abs(got - float(ratio)) > 1e-12:
            ok_env = False
    checks.append({"check": "envelope_dp_vs_brute_depth_le_15", "pass": ok_env})

    # 3. depth-2 class: x* = 1 (the trivial cycle), ratio 1/4
    row2 = dp_map.get(2)
    checks.append(
        {
            "check": "depth_2_trivial_cycle_class_xstar_1",
            "value": row2["max_xstar_exact"] if row2 else None,
            "pass": row2 is not None and row2["max_xstar_exact"] == "1" and abs(row2["max_xstar_over_2^d"] - 0.25) < 1e-15,
        }
    )

    # 4. window scan brute cross-check for o <= 40 over all d <= 80
    ok_win = True
    hits_brute = []
    for o in range(1, 41):
        for d in range(1, 81):
            if 3**o < (1 << d) and (1 << d) - 3**o < Fraction(3, 2) ** o:
                hits_brute.append((d, o))
    win = window_payload(40)
    if [(h["d"], h["o"]) for h in win["hits"]] != hits_brute:
        ok_win = False
    checks.append({"check": "window_scan_vs_brute_o_le_40", "hits": hits_brute, "pass": ok_win})

    # 5. legendre validity floor: 2^-o/(o ln2) < 1/(2 o^2) for o >= 4
    ok_leg = all(2.0**-o / (o * LN2_OVER) < 1.0 / (2 * o * o) for o in range(4, 200))
    checks.append({"check": "legendre_floor_o_ge_4", "pass": ok_leg})

    # 5b. small-denominator branch: every above-side p/q with q <= 3 sits at
    # distance > w(8) = 2^-8/(8 ln2) from alpha, so o >= 8 traps with reduced
    # denominator q <= 3 are impossible (exact rational comparison).
    scale = 10**80
    (l2lo, l2hi), (l3lo, l3hi) = ln_bounds(scale)
    alpha_lo80 = Fraction(l3lo, l2hi)
    alpha_hi80 = Fraction(l3hi, l2lo)
    w8_hi = Fraction(scale, 8 * l2lo) / (1 << 8)
    ok_smallq = True
    for q in (1, 2, 3):
        # smallest p with p/q > alpha
        p = (alpha_hi80.numerator * q) // alpha_hi80.denominator + 1
        gap = Fraction(p, q) - alpha_hi80
        if gap < w8_hi:
            ok_smallq = False
    checks.append({"check": "q_le_3_above_fractions_outside_window_o_ge_8", "pass": ok_smallq})

    # 6. CF machinery: prefix check + all above-side convergents excluded
    cf = cf_exclusion_payload(320)
    checks.append({"check": "cf_exclusion_all_above_convergents", "pass": cf["all_excluded"]})

    # 7. sigma=tau consistency spot check: for n in [2, 50000] with n >= 2^tau
    ok_st = True
    for n in range(2, 50001):
        x = n
        pw = 1
        d = 0
        tau = None
        while tau is None:
            if x & 1:
                pw *= 3
                x = (3 * x + 1) >> 1
            else:
                x >>= 1
            d += 1
            if pw < (1 << d):
                tau = d
        if n >= (1 << tau) and x >= n:
            ok_st = False  # would be a q>=1 trap: theorem says impossible
    checks.append({"check": "no_q_ge_1_trap_among_n_le_50000", "pass": ok_st})

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
    p = sub.add_parser("envelope")
    p.add_argument("--max-depth", type=int, default=2048)
    p.add_argument("--out", default=None)
    p = sub.add_parser("window")
    p.add_argument("--o-max", type=int, default=256)
    p.add_argument("--out", default=None)
    p = sub.add_parser("cf-exclusion")
    p.add_argument("--digits", type=int, default=320)
    p.add_argument("--out", default=None)
    p = sub.add_parser("theorem")
    p.add_argument("--max-depth", type=int, default=2048)
    p.add_argument("--o-max", type=int, default=256)
    p.add_argument("--digits", type=int, default=320)
    p.add_argument("--out", default=None)

    args = parser.parse_args()
    if args.cmd == "selftest":
        payload = selftest_payload()
        emit(payload, None)
        if not payload["all_pass"]:
            raise SystemExit(1)
    elif args.cmd == "envelope":
        payload = envelope_rows(args.max_depth)
        payload["mode"] = "envelope"
        emit(payload, args.out)
    elif args.cmd == "window":
        emit(window_payload(args.o_max), args.out)
    elif args.cmd == "cf-exclusion":
        emit(cf_exclusion_payload(args.digits), args.out)
    elif args.cmd == "theorem":
        emit(theorem_payload(args.max_depth, args.o_max, args.digits), args.out)


if __name__ == "__main__":
    main()
