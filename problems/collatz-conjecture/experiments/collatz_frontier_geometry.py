#!/usr/bin/env python3
"""Frontier geometry of the Collatz certificate program.

This module quantifies the geometry of the uncertified frontier left by
finite-residue descent certificates (see collatz_residue_lab.py and
CERTIFICATE-FRONTIER-THEOREMS.md).  Everything it reports is either

  * proved (elementary and self-contained; see FRONTIER-GEOMETRY.md),
  * measured exactly (integer dynamic programs, exhaustive scans), or
  * conditional on the published verification floor (Barina 2025, n < 2^71),

and the output labels which is which.  Nothing in this file claims a proof
of the Collatz conjecture.

Notation (shortcut map):

    T(n) = n / 2          if n is even
         = (3n + 1) / 2   if n is odd

    o(d)   = number of odd steps among the first d shortcut steps
    tau(n) = least d with 3^o(d) < 2^d      (Terras' coefficient stopping time;
                                             identical to the certificate depth
                                             of n's residue class)
    sigma(n) = least d with T^d(n) < n      (stopping time)
    theta  = log_3 2 = 0.63092975...        (critical odd-step density)

Subcommands:

    constants     closed-form frontier constants (dimension, decay, ceilings)
    rates         exact survivor counts and decay-rate convergence (bigint DP)
    tau-scan      tau(n) vs sigma(n) for all n <= limit: Terras-conjecture
                  check, record table, frontier-tail vs exact-density ratios
    mersenne      tau(2^j - 1) along the Mersenne spine vs predicted slope
    cycle-floor   rigorous cycle-length floor from the verified range via an
                  interval continued fraction of log2(3) (exact integers only)
    selftest      independent consistency checks of all of the above
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from fractions import Fraction
from math import comb, isqrt
from time import perf_counter

# ---------------------------------------------------------------------------
# Closed-form constants
# ---------------------------------------------------------------------------

THETA = math.log(2) / math.log(3)          # log_3 2 = 0.63092975...
ALPHA = math.log(3) / math.log(2)          # log_2 3 = 1.58496250...
H_THETA = -(THETA * math.log2(THETA) + (1.0 - THETA) * math.log2(1.0 - THETA))
DECAY_RATE = 1.0 - H_THETA                 # 0.05004447...
GAMMA_CEILING = 1.0 / DECAY_RATE           # 19.98222...
MERSENNE_SLOPE = 1.0 / (2.0 * THETA - 1.0)  # 3.81884...

# Continued fraction prefix of log_2 3, independently certified by its
# convergent-denominator chain 1, 2, 5, 12, 41, 53, 306, 665, 15601, 31867,
# 79335, 111202, 190537, 10590737, ... (the classical cycle-paper values).
KNOWN_CF_PREFIX = [1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 3]

# Frontier sizes measured independently by experiments/collatz_residue_lab.py
# (frontier_units at max depth, logged in FABLE5-ULTRACODE-COLLATZ-LOG.md).
RESIDUE_LAB_ANCHORS = {20: 27328, 24: 286581, 28: 3524586}


def log2_int(x: int) -> float:
    """log2 of a positive big integer, accurate to ~1e-15 relative."""
    b = x.bit_length()
    if b <= 60:
        return math.log2(x)
    return float(b - 60) + math.log2(x >> (b - 60))


def constants_payload() -> dict[str, object]:
    return {
        "mode": "constants",
        "theta_log3_2": THETA,
        "alpha_log2_3": ALPHA,
        "entropy_H_theta_bits": H_THETA,
        "frontier_dimension": H_THETA,
        "frontier_decay_rate_bits_per_level": DECAY_RATE,
        "record_gamma_ceiling": GAMMA_CEILING,
        "mersenne_tau_slope": MERSENNE_SLOPE,
        "meaning": {
            "frontier_dimension": (
                "Box-counting dimension of the 2-adic survivor set of the "
                "descent-certificate test (proved in FRONTIER-GEOMETRY.md; "
                "Hausdorff <= box always, equality not claimed)."
            ),
            "frontier_decay_rate_bits_per_level": (
                "F(d) = density of n with tau(n) > d equals "
                "2^(-(1-H(theta)) d + O(log d)); this is the exact uncertified "
                "fraction at depth d."
            ),
            "record_gamma_ceiling": (
                "Heuristic ceiling for tau(n)/log2(n): records should approach "
                "1/(1-H(theta)) = 19.9822... from below if positive integers "
                "carry no extra frontier structure."
            ),
            "mersenne_tau_slope": (
                "Predicted tau(2^j - 1)/j -> 1/(2 theta - 1) = 3.81884... "
                "(deficit-repayment heuristic for the Mersenne spine)."
            ),
        },
    }


# ---------------------------------------------------------------------------
# Survivor dynamic program (exact)
# ---------------------------------------------------------------------------


def dp_rows(report_depths: set[int]) -> list[tuple[int, int, int, int]]:
    """Exact survivor DP.

    Returns rows (depth, min_odd_count, survivors, boundary_count) for each
    requested depth, where survivors is the exact number of parity prefixes
    of that length with 3^o(j) >= 2^j for every prefix j <= depth, and
    boundary_count is the number of those sitting at the minimal odd count.
    """
    max_depth = max(report_depths)
    rows: list[tuple[int, int, int, int]] = []
    counts: list[int] = [1]      # counts[i] = prefixes with odd count o_min + i
    o_min = 0
    threshold = 0                # smallest o with 3^o >= 2^depth
    pow3_threshold = 1
    for depth in range(1, max_depth + 1):
        boundary = 1 << depth
        while pow3_threshold < boundary:
            pow3_threshold *= 3
            threshold += 1
        new = [0] * (len(counts) + 1)
        for i, c in enumerate(counts):
            if c:
                new[i] += c       # next step even: odd count unchanged
                new[i + 1] += c   # next step odd: odd count + 1
        drop = threshold - o_min
        if drop > 0:
            new = new[drop:]
            o_min = threshold
        counts = new
        if depth in report_depths:
            survivors = sum(counts)
            rows.append((depth, o_min, survivors, counts[0] if counts else 0))
    return rows


def survivor_counts(depths: set[int]) -> dict[int, int]:
    return {depth: survivors for depth, _, survivors, _ in dp_rows(depths)}


def rates_payload(max_depth: int) -> dict[str, object]:
    base = [1, 16, 20, 24, 28, 32, 48, 64, 96, 128, 192]
    base += list(range(256, max_depth + 1, 256))
    base.append(max_depth)
    report = {d for d in base if 1 <= d <= max_depth}
    started = perf_counter()
    raw = dp_rows(report)
    elapsed = perf_counter() - started

    rows = []
    anchor_checks = []
    for depth, o_min, survivors, boundary in raw:
        log2_s = log2_int(survivors)
        log2_fraction = log2_s - depth
        rate = -log2_fraction / depth
        rows.append(
            {
                "depth": depth,
                "min_odd_count": o_min,
                "survivors": str(survivors),
                "survivors_log2": round(log2_s, 6),
                "fraction_log2": round(log2_fraction, 6),
                "decay_rate_bits_per_level": round(rate, 6),
                "rate_minus_asymptotic": round(rate - DECAY_RATE, 6),
                "boundary_mass_fraction": round(float(Fraction(boundary, survivors)), 6),
            }
        )
        if depth in RESIDUE_LAB_ANCHORS:
            anchor_checks.append(
                {
                    "depth": depth,
                    "expected_frontier_leaves": RESIDUE_LAB_ANCHORS[depth],
                    "dp_survivors": survivors,
                    "match": survivors == RESIDUE_LAB_ANCHORS[depth],
                }
            )

    return {
        "mode": "rates",
        "max_depth": max_depth,
        "elapsed_seconds": round(elapsed, 3),
        "asymptotic_rate_1_minus_H": DECAY_RATE,
        "cross_check_vs_collatz_residue_lab": anchor_checks,
        "interpretation": (
            "F(depth) = 2^fraction_log2 is the exact fraction of every block of "
            "2^depth consecutive integers still uncertified at that depth "
            "(equivalently: with tau > depth).  The decay rate converges slowly "
            "to 1 - H(theta) = 0.0500444...; the O(log d)/d finite-size term is "
            "visible in rate_minus_asymptotic."
        ),
        "rows": rows,
    }


# ---------------------------------------------------------------------------
# tau / sigma scan
# ---------------------------------------------------------------------------


def tau_sigma(n: int) -> tuple[int, int]:
    """(tau, sigma) for n >= 2 under the shortcut map."""
    x = n
    d = 0
    pw3 = 1
    pw2 = 1
    tau = 0
    while True:
        if x & 1:
            x = (3 * x + 1) >> 1
            pw3 *= 3
        else:
            x >>= 1
        d += 1
        pw2 <<= 1
        if tau == 0 and pw3 < pw2:
            tau = d
        if x < n:
            if tau == 0:
                raise AssertionError(f"descent before coefficient drop at n={n}")
            return tau, d


def tau_of(n: int) -> int:
    """Coefficient stopping time only (works for huge n)."""
    x = n
    d = 0
    pw3 = 1
    pw2 = 1
    while True:
        if x & 1:
            x = (3 * x + 1) >> 1
            pw3 *= 3
        else:
            x >>= 1
        d += 1
        pw2 <<= 1
        if pw3 < pw2:
            return d


def tau_scan_payload(limit: int, tail_depths: list[int]) -> dict[str, object]:
    if limit < 3:
        raise SystemExit("--limit must be at least 3")
    tails_sorted = sorted(tail_depths)
    guard = tails_sorted[0]
    tail_counts = {t: 0 for t in tails_sorted}

    started = perf_counter()
    records = [{"n": 2, "tau": 1, "sigma": 1, "gamma": 1.0}]
    best_tau = 1
    max_gamma = 1.0
    max_gamma_n = 2
    mismatches: list[dict[str, int]] = []
    total_tau = 1                     # n = 2
    evens = limit // 2 - 1            # n = 4, 6, ..., each tau = sigma = 1
    total_tau += evens
    progress_every = 5_000_000

    n = 3
    while n <= limit:
        tau, sigma = tau_sigma(n)
        total_tau += tau
        if tau != sigma and len(mismatches) < 20:
            mismatches.append({"n": n, "tau": tau, "sigma": sigma})
        if tau > best_tau:
            best_tau = tau
            records.append({"n": n, "tau": tau, "sigma": sigma, "gamma": round(tau / math.log2(n), 4)})
        # gamma can only beat the running max if tau > max_gamma*(bit_length-1),
        # because log2(n) > bit_length - 1; this keeps the hot loop cheap.
        if tau > max_gamma * (n.bit_length() - 1):
            gamma = tau / math.log2(n)
            if gamma > max_gamma:
                max_gamma = gamma
                max_gamma_n = n
        if tau > guard:
            for t in tails_sorted:
                if tau > t:
                    tail_counts[t] += 1
                else:
                    break
        if (n - 1) % progress_every < 2 and n > progress_every:
            print(
                f"progress: n={n} elapsed={perf_counter() - started:.0f}s "
                f"records={len(records)} best_tau={best_tau}",
                file=sys.stderr,
                flush=True,
            )
        n += 2

    exact = survivor_counts(set(tails_sorted))
    total_n = limit - 1
    tails = []
    for t in tails_sorted:
        f_exact = Fraction(exact[t], 1 << t)
        expected = float(f_exact) * total_n
        count = tail_counts[t]
        if (1 << t) <= total_n:
            regime = "exact (2^d <= N: ratio forced to 1 up to O(2^d/N))"
        elif expected >= 25.0:
            regime = "equidistribution (2^d > N, expected count large: measures integer-vs-shadow structure)"
        else:
            regime = "record-tail (expected count small: fluctuation dominated)"
        tails.append(
            {
                "depth": t,
                "count_tau_gt_depth": count,
                "exact_density_F": float(f_exact),
                "expected_count_N_times_F": round(expected, 3),
                "ratio_observed_over_expected": round(count / expected, 6) if expected else None,
                "regime": regime,
            }
        )

    elapsed = perf_counter() - started
    return {
        "mode": "tau-scan",
        "limit": limit,
        "elapsed_seconds": round(elapsed, 1),
        "sigma_ge_tau_theorem": "held for every scanned n (descent implies coefficient drop)",
        "terras_coefficient_conjecture": {
            "statement": "tau(n) == sigma(n) for all 1 < n <= limit",
            "counterexamples": mismatches,
            "verified": not mismatches,
        },
        "mean_tau": round(total_tau / total_n, 6),
        "max_tau": best_tau,
        "max_gamma_tau_over_log2n": {"n": max_gamma_n, "gamma": round(max_gamma, 4)},
        "gamma_ceiling_heuristic": GAMMA_CEILING,
        "records": records,
        "frontier_tails": tails,
        "interpretation": (
            "records approaching gamma = 19.982 from below, and record-regime "
            "tail ratios near 1, are the random-model behavior; any systematic "
            "departure would be the first quantitative sign of positive-integer "
            "structure against the 2-adic frontier."
        ),
    }


# ---------------------------------------------------------------------------
# Mersenne spine
# ---------------------------------------------------------------------------


def mersenne_payload(max_j: int) -> dict[str, object]:
    sample = sorted(set(list(range(1, min(64, max_j) + 1)) + list(range(64, max_j + 1, 8))))
    started = perf_counter()
    rows = []
    for j in sample:
        tau = tau_of((1 << j) - 1)
        rows.append({"j": j, "tau": tau, "tau_over_j": round(tau / j, 4)})
    elapsed = perf_counter() - started
    upper_half = [r for r in rows if r["j"] >= max_j // 2]
    ratios = [r["tau_over_j"] for r in upper_half]
    return {
        "mode": "mersenne",
        "max_j": max_j,
        "elapsed_seconds": round(elapsed, 3),
        "predicted_slope_1_over_2theta_minus_1": MERSENNE_SLOPE,
        "observed_upper_half_mean": round(sum(ratios) / len(ratios), 4),
        "observed_upper_half_min": min(ratios),
        "observed_upper_half_max": max(ratios),
        "interpretation": (
            "n = 2^j - 1 opens with j forced odd steps (surplus j(1-theta)); the "
            "certificate can only close once the continuation repays the deficit, "
            "predicting tau ~ j/(2 theta - 1) = 3.8188 j if the continuation is "
            "measure-typical.  Persistent excess above the slope would flag "
            "structure in the deepest positive-integer corridor of the frontier."
        ),
        "rows": rows,
    }


# ---------------------------------------------------------------------------
# Rigorous cycle floor from the verified range
# ---------------------------------------------------------------------------


def atanh_recip_scaled(inv: int, scale: int) -> tuple[int, int]:
    """Integer bounds (lo, hi) with lo <= scale*atanh(1/inv) <= hi."""
    total = 0
    k = 0
    power = inv
    inv2 = inv * inv
    while True:
        term = scale // ((2 * k + 1) * power)
        if term == 0:
            break
        total += term
        power *= inv2
        k += 1
    # Each floored term lost < 1; the untruncated tail is < 2 (geometric,
    # ratio <= 1/9, first uncomputed true term < 1).
    return total, total + k + 2


def ln_bounds(scale: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Integer interval bounds for scale*ln2 and scale*ln3."""
    a3lo, a3hi = atanh_recip_scaled(3, scale)   # atanh(1/3) = ln(2)/2
    a5lo, a5hi = atanh_recip_scaled(5, scale)   # atanh(1/5) = ln(3/2)/2
    ln2 = (2 * a3lo, 2 * a3hi)
    ln3 = (2 * (a3lo + a5lo), 2 * (a3hi + a5hi))
    return ln2, ln3


def cf_terms_interval(lo: Fraction, hi: Fraction, max_terms: int) -> list[int]:
    """Common continued fraction prefix of every x in [lo, hi], minus one
    safety term.  Provably correct terms of the true irrational inside."""
    terms: list[int] = []
    a, b = lo, hi
    for _ in range(max_terms):
        fa = a.numerator // a.denominator
        fb = b.numerator // b.denominator
        if fa != fb:
            break
        terms.append(fa)
        fra = a - fa
        frb = b - fb
        if fra == 0 or frb == 0:
            break
        a, b = 1 / frb, 1 / fra
    return terms[:-1]


def cycle_floor_payload(verified_bits: int, digits: int) -> dict[str, object]:
    scale = 10**digits
    (l2lo, l2hi), (l3lo, l3hi) = ln_bounds(scale)
    alpha_lo = Fraction(l3lo, l2hi)
    alpha_hi = Fraction(l3hi, l2lo)
    terms = cf_terms_interval(alpha_lo, alpha_hi, 400)
    prefix_ok = terms[: len(KNOWN_CF_PREFIX)] == KNOWN_CF_PREFIX
    if not prefix_ok:
        raise AssertionError("continued fraction of log2(3) failed the literature check")

    B = 1 << verified_bits
    # Case split: for o <= o_star, the approximation is finer than 1/(2 o^2),
    # so Legendre's criterion forces d/o (reduced) to be a convergent.
    o_star = isqrt((3 * B * l2lo) // (2 * scale))
    eps_hi = Fraction(scale, 3 * B * l2lo)   # rigorous upper bound for 1/(3B ln2)

    convergents = []
    qualifying: list[int] = []
    p_prev2, p_prev = 0, 1
    q_prev2, q_prev = 1, 0
    for k, a in enumerate(terms):
        p = a * p_prev + p_prev2
        q = a * q_prev + q_prev2
        p_prev2, p_prev = p_prev, p
        q_prev2, q_prev = q_prev, q
        conv = Fraction(p, q)
        if alpha_lo <= conv <= alpha_hi:
            raise AssertionError("convergent inside alpha interval; raise --digits")
        side = "above" if conv > alpha_hi else "below"
        row: dict[str, object] = {
            "k": k,
            "a_k": a,
            "p": str(p),
            "q": str(q),
            "side": side,
        }
        if side == "above" and q <= o_star:
            gap_lo = conv - alpha_hi
            excluded = gap_lo >= eps_hi
            row["gap_lower_bound"] = float(gap_lo)
            row["excluded"] = excluded
            if not excluded:
                qualifying.append(q)
        row["within_o_star"] = q <= o_star
        convergents.append(row)
        if q > 10 * o_star:
            break

    floor_odd = min(qualifying) if qualifying else o_star + 1
    d_floor = (alpha_lo * floor_odd).numerator // (alpha_lo * floor_odd).denominator + 1
    standard_floor = floor_odd + d_floor

    return {
        "mode": "cycle-floor",
        "verified_bits": verified_bits,
        "B": str(B),
        "precision_digits": digits,
        "alpha_interval_width_log10": round(
            (
                (alpha_hi - alpha_lo).numerator.bit_length()
                - (alpha_hi - alpha_lo).denominator.bit_length()
            )
            * math.log10(2),
            1,
        ),
        "cf_terms_certified": terms,
        "cf_known_prefix_check": prefix_ok,
        "epsilon_upper_bound_1_over_3Bln2": float(eps_hi),
        "o_star_legendre_cap": o_star,
        "qualifying_convergents_below_cap": qualifying,
        "floor_odd_steps": floor_odd,
        "floor_shortcut_steps": d_floor,
        "floor_standard_steps": standard_floor,
        "assumptions": [
            f"Every n < 2^{verified_bits} converges to 1 "
            "(Barina 2025, Journal of Supercomputing: verified through 2^71).",
            "Legendre's continued fraction criterion "
            "(|alpha - p/q| < 1/(2q^2) forces p/q to be a convergent).",
            "Interval-certified continued fraction of log2(3), computed above "
            "with exact integer arithmetic (atanh series with bounded tails).",
        ],
        "statement": (
            f"Conditional on the 2^{verified_bits} verification: every nontrivial "
            f"cycle of the shortcut Collatz map has at least {floor_odd} odd steps "
            f"and at least {d_floor} total shortcut steps; equivalently at least "
            f"{standard_floor} steps of the standard Collatz map."
        ),
        "comparison": (
            "Hercher (2023) proves >= 1.375e11 odd terms by excluding all m-cycles "
            "with m <= 91 on top of the verification floor; the floor computed here "
            "is weaker but fully reproducible in-repo from first principles."
        ),
        "convergents": convergents,
    }


# ---------------------------------------------------------------------------
# Self tests
# ---------------------------------------------------------------------------


def brute_survivors(depth: int) -> int:
    total = 0
    for r in range(1 << depth):
        x = r
        pw3 = 1
        pw2 = 1
        ok = True
        for _ in range(depth):
            if x & 1:
                x = (3 * x + 1) >> 1
                pw3 *= 3
            else:
                x >>= 1
            pw2 <<= 1
            if pw3 < pw2:
                ok = False
                break
        if ok:
            total += 1
    return total


def brute_tau_sigma(n: int) -> tuple[int, int]:
    parities = []
    x = n
    sigma = None
    for d in range(1, 100000):
        parities.append(x & 1)
        x = (3 * x + 1) >> 1 if x & 1 else x >> 1
        if x < n:
            sigma = d
            break
    assert sigma is not None
    o = 0
    for d, p in enumerate(parities, start=1):
        o += p
        if 3**o < 2**d:
            return d, sigma
    raise AssertionError(f"coefficient never dropped before sigma at n={n}")


def selftest_payload() -> dict[str, object]:
    checks = []

    dp14 = survivor_counts({14})[14]
    brute14 = brute_survivors(14)
    checks.append({"check": "dp_vs_enumeration_depth_14", "dp": dp14, "brute": brute14, "pass": dp14 == brute14})

    anchors = survivor_counts(set(RESIDUE_LAB_ANCHORS))
    ok = all(anchors[d] == v for d, v in RESIDUE_LAB_ANCHORS.items())
    checks.append({"check": "dp_vs_residue_lab_anchors", "values": {str(k): anchors[k] for k in anchors}, "pass": ok})

    mism = []
    for n in range(2, 3001):
        got = tau_sigma(n)
        want = brute_tau_sigma(n)
        if got != want:
            mism.append({"n": n, "got": got, "want": want})
    checks.append({"check": "tau_sigma_vs_bruteforce_n_le_3000", "mismatches": mism, "pass": not mism})

    t27 = tau_sigma(27)
    checks.append({"check": "tau_sigma_27_equals_59_59", "value": t27, "pass": t27 == (59, 59)})

    mers_ok = True
    for j in (3, 8, 15, 24):
        x = (1 << j) - 1
        for k in range(1, j + 1):
            if not x & 1:
                mers_ok = False
            x = (3 * x + 1) >> 1
            if x != (3**k) * (1 << (j - k)) - 1:
                mers_ok = False
    checks.append({"check": "mersenne_forced_odd_identity", "pass": mers_ok})

    scale = 10**80
    (l2lo, l2hi), (l3lo, l3hi) = ln_bounds(scale)
    width_ok = (l2hi - l2lo) < 1000 and (l3hi - l3lo) < 1000
    float_ok = abs(l2lo / scale - math.log(2)) < 1e-14 and abs(l3lo / scale - math.log(3)) < 1e-14
    terms = cf_terms_interval(Fraction(l3lo, l2hi), Fraction(l3hi, l2lo), 400)
    cf_ok = terms[: len(KNOWN_CF_PREFIX)] == KNOWN_CF_PREFIX
    checks.append({"check": "interval_ln_bounds_and_cf_prefix", "pass": width_ok and float_ok and cf_ok})

    bounds_ok = True
    counts = survivor_counts(set(range(6, 21)))
    for d in range(6, 21):
        m = math.ceil(THETA * d) + 1
        lower = comb(d, m) // d
        upper = (d + 1) * comb(d, math.ceil(THETA * d))
        if not lower <= counts[d] <= upper:
            bounds_ok = False
    checks.append({"check": "rotation_lemma_and_union_bounds_6_to_20", "pass": bounds_ok})

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

    sub.add_parser("constants")

    p_rates = sub.add_parser("rates")
    p_rates.add_argument("--max-depth", type=int, default=512)
    p_rates.add_argument("--out", type=str, default=None)

    p_tau = sub.add_parser("tau-scan")
    p_tau.add_argument("--limit", type=int, default=10_000_000)
    p_tau.add_argument("--tails", type=str, default="10,20,30,40,60,80,100,120,140")
    p_tau.add_argument("--out", type=str, default=None)

    p_mers = sub.add_parser("mersenne")
    p_mers.add_argument("--max-j", type=int, default=600)
    p_mers.add_argument("--out", type=str, default=None)

    p_cyc = sub.add_parser("cycle-floor")
    p_cyc.add_argument("--verified-bits", type=int, default=71)
    p_cyc.add_argument("--digits", type=int, default=320)
    p_cyc.add_argument("--out", type=str, default=None)

    p_self = sub.add_parser("selftest")
    p_self.add_argument("--out", type=str, default=None)

    args = parser.parse_args()

    if args.cmd == "constants":
        emit(constants_payload(), None)
    elif args.cmd == "rates":
        emit(rates_payload(args.max_depth), args.out)
    elif args.cmd == "tau-scan":
        tails = [int(t) for t in args.tails.split(",") if t.strip()]
        emit(tau_scan_payload(args.limit, tails), args.out)
    elif args.cmd == "mersenne":
        emit(mersenne_payload(args.max_j), args.out)
    elif args.cmd == "cycle-floor":
        emit(cycle_floor_payload(args.verified_bits, args.digits), args.out)
    elif args.cmd == "selftest":
        payload = selftest_payload()
        emit(payload, args.out)
        if not payload["all_pass"]:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
