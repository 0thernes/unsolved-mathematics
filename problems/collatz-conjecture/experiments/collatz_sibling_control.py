#!/usr/bin/env python3
"""Sibling-control experiments: run the certificate machinery on maps where
the analogous conjecture is FALSE, and measure what changes.

The family under study is

    T_{q,eps}(n) = n / 2                if n is even
                 = (q n + eps) / 2      if n is odd,

with (q, eps) in {(3,+1) Collatz, (3,-1) sibling with known nontrivial
cycles (minima 5 and 17), (5,+1) sibling with conjectured divergent orbits}.

Everything certificate-theoretic generalizes verbatim:

    T^d(n) = (q^{o(d)} n + c_d) / 2^d,   sign(c_d) = eps  (c_d = 0 iff o = 0)

    tau(n)   = least d with q^{o(d)} < 2^d      (coefficient stopping time)
    sigma(n) = least d with T^d(n) < n          (stopping time)
    S_{q,eps} = 2-adic integers with q^{o(d)} >= 2^d for all d  (survivor set)

Two elementary sign theorems split the family (proofs in SIBLING-CONTROL.md):

    eps = +1  =>  tau <= sigma   and every cycle satisfies q^o < 2^d
                  (cycles live BELOW the critical line, in certified land;
                   counterexamples can hide under certificate thresholds)
    eps = -1  =>  sigma <= tau   and every cycle satisfies q^o > 2^d
                  (cycles live ABOVE the line, inside the survivor set;
                   certificates have NO thresholds - descent is unconditional)

The word system (residue <-> parity-word bijection, survivor counts, densities,
dimension) depends only on q, NOT on eps.  So (3,+1) and (3,-1) have
IDENTICAL frontier statistics while having different truth values for
"S contains a positive integer" - the no-go observation this control run
makes quantitative.  Nothing here proves the Collatz conjecture.

Subcommands: selftest, dichotomy, membership, rates, scan.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from time import perf_counter

KNOWN_CYCLE_MINIMA = {
    (3, 1): [1],
    (3, -1): [1, 5, 17],
    (5, 1): [1, 13, 17],
}


def step(q: int, eps: int, x: int) -> int:
    return (q * x + eps) >> 1 if x & 1 else x >> 1


# ---------------------------------------------------------------------------
# Cycle discovery and the sign dichotomy
# ---------------------------------------------------------------------------


def find_cycle(q: int, eps: int, start: int, max_steps: int = 10000) -> dict[str, object]:
    """Iterate from start until the value returns to start; assert it is the
    cycle minimum; return exact cycle data."""
    x = start
    word = []
    values = [start]
    for _ in range(max_steps):
        word.append(x & 1)
        x = step(q, eps, x)
        if x == start:
            break
        values.append(x)
        if x < start:
            raise AssertionError(f"start {start} is not the minimum of its cycle under ({q},{eps})")
    else:
        raise AssertionError(f"no cycle within {max_steps} steps from {start} under ({q},{eps})")

    d = len(word)
    o = sum(word)
    side = "below" if (q**o) < (1 << d) else "above"
    margin_bits = o * math.log2(q) - d
    return {
        "q": q,
        "eps": eps,
        "min_element": start,
        "length_shortcut": d,
        "odd_steps": o,
        "elements": values,
        "word": "".join(str(b) for b in word),
        "q^o_vs_2^d": side,
        "per_period_margin_bits": round(margin_bits, 6),
        "sign_rule_expected_side": "below" if eps > 0 else "above",
        "sign_rule_holds": side == ("below" if eps > 0 else "above"),
    }


def dichotomy_payload() -> dict[str, object]:
    cycles = []
    for (q, eps), minima in KNOWN_CYCLE_MINIMA.items():
        for m in minima:
            cycles.append(find_cycle(q, eps, m))
    return {
        "mode": "dichotomy",
        "theorem": (
            "For a positive-integer cycle of T_{q,eps} with o odd steps in d total "
            "steps: x (2^d - q^o) = c_d and sign(c_d) = eps, hence eps=+1 forces "
            "q^o < 2^d (cycle below the critical line) and eps=-1 forces q^o > 2^d "
            "(cycle above the line, inside the survivor set)."
        ),
        "all_sign_rules_hold": all(c["sign_rule_holds"] for c in cycles),
        "cycles": cycles,
        "notable_margins": {
            "collatz_trivial_1": "d=2,o=1: 4 vs 3, +0.415 bits below the line",
            "3n-1_cycle_17": "d=11,o=7: 2187 vs 2048, +0.094 bits ABOVE the line (razor thin)",
            "5n+1_cycle_13": "d=7,o=3: 125 vs 128, -0.035 bits below the line (razor thin)",
        },
    }


# ---------------------------------------------------------------------------
# Frontier membership certificates (eps = -1 integers inside S)
# ---------------------------------------------------------------------------


def membership_certificate(q: int, eps: int, m: int) -> dict[str, object]:
    """Prove m is in S_{q,eps} when m is a cycle minimum whose cycle sits above
    the line: check q^{o(j)} >= 2^j exactly for one period, plus positive
    per-period surplus; periodicity then gives every deeper prefix."""
    cyc = find_cycle(q, eps, m)
    d, o = cyc["length_shortcut"], cyc["odd_steps"]
    if q**o <= (1 << d):
        return {"q": q, "eps": eps, "n": m, "member": False, "reason": "cycle not above the line"}
    word = [int(ch) for ch in cyc["word"]]
    prefix_ok = True
    min_margin = None
    oj = 0
    for j, bit in enumerate(word, start=1):
        oj += bit
        margin = oj * math.log2(q) - j
        if min_margin is None or margin < min_margin:
            min_margin = margin
        if q**oj < (1 << j):
            prefix_ok = False
            break
    return {
        "q": q,
        "eps": eps,
        "n": m,
        "member": prefix_ok,
        "proof": (
            "exact prefix check q^o(j) >= 2^j for j = 1..d, plus per-period surplus "
            "q^o > 2^d; every prefix of the periodic word is a prefix-of-period plus "
            "whole periods, and both factors are >= 1"
        ) if prefix_ok else "prefix check failed",
        "period": {"d": d, "o": o},
        "per_period_surplus_bits": cyc["per_period_margin_bits"],
        "min_prefix_margin_bits": round(min_margin, 6) if min_margin is not None else None,
    }


def membership_payload() -> dict[str, object]:
    certs = [membership_certificate(3, -1, m) for m in (1, 5, 17)]
    return {
        "mode": "membership",
        "statement": (
            "S_{3,-1} (the 3n-1 survivor set, whose word system and all statistics "
            "are IDENTICAL to Collatz's S_{3,+1}) provably contains the positive "
            "integers 1, 5, 17 - the cycle minima. The all-odd universal survivor "
            "is x = -eps: for 3n+1 it is -1 (not positive), for 3n-1 it is +1."
        ),
        "certificates": certs,
        "all_proved": all(c["member"] for c in certs),
    }


# ---------------------------------------------------------------------------
# Word-system DP: survivor counts for multiplier q (eps-independent)
# ---------------------------------------------------------------------------


def dp_rows(q: int, report_depths: set[int]) -> list[tuple[int, int]]:
    """Exact survivor counts: parity prefixes with q^{o(j)} >= 2^j for all j <= d."""
    max_depth = max(report_depths)
    rows: list[tuple[int, int]] = []
    counts: list[int] = [1]
    o_min = 0
    threshold = 0
    powq_threshold = 1
    for depth in range(1, max_depth + 1):
        boundary = 1 << depth
        while powq_threshold < boundary:
            powq_threshold *= q
            threshold += 1
        new = [0] * (len(counts) + 1)
        for i, c in enumerate(counts):
            if c:
                new[i] += c
                new[i + 1] += c
        drop = threshold - o_min
        if drop > 0:
            new = new[drop:]
            o_min = threshold
        counts = new
        if depth in report_depths:
            rows.append((depth, sum(counts)))
    return rows


def brute_survivors(q: int, depth: int) -> int:
    total = 0
    for r in range(1 << depth):
        x = r
        pw = 1
        ok = True
        for j in range(1, depth + 1):
            if x & 1:
                pw *= q
            x = step(q, 1, x)  # parity path of the residue; eps only shifts values, not the count law
            if pw < (1 << j):
                ok = False
                break
        if ok:
            total += 1
    return total


def rates_payload(q: int, max_depth: int) -> dict[str, object]:
    theta = math.log(2) / math.log(q)
    report = sorted({1, 8, 16, 24, 32, 48, 64, 96, 128, 256, 512, 1024, 2048, max_depth} | set(range(256, max_depth + 1, 512)))
    report = {d for d in report if 1 <= d <= max_depth}
    started = perf_counter()
    rows_raw = dp_rows(q, report)
    elapsed = perf_counter() - started
    rows = []
    partial_mean = None
    if q == 5:
        # E[tau] = sum F(d); for q = 5 the terms tend to a positive constant.
        small = dp_rows(5, set(range(1, 257)))
        partial_mean = float(sum(Fraction(s, 1 << d) for d, s in small))
    for depth, survivors in rows_raw:
        log2s = math.log2(survivors) if survivors.bit_length() <= 60 else (survivors.bit_length() - 60) + math.log2(survivors >> (survivors.bit_length() - 60))
        rows.append(
            {
                "depth": depth,
                "fraction_log2": round(log2s - depth, 6),
                "fraction": float(Fraction(survivors, 1 << depth)) if depth <= 1024 else None,
            }
        )
    return {
        "mode": "rates",
        "q": q,
        "critical_density_log_q_2": theta,
        "random_walk_density": 0.5,
        "regime": "drift BELOW critical line: survivor fraction -> 0" if 0.5 < theta
        else "drift ABOVE critical line: survivor fraction -> positive constant (divergence-typical)",
        "elapsed_seconds": round(elapsed, 3),
        "partial_E_tau_first_256_terms": partial_mean,
        "rows": rows,
    }


# ---------------------------------------------------------------------------
# Integer scans with frontier-residency detection
# ---------------------------------------------------------------------------


def scan_one_exact(q: int, eps: int, n: int, cap: int) -> tuple[int | None, int | None, bool]:
    """Return (tau, sigma, flagged). Exact values; stops when tau fires (for
    eps=-1 sigma<=tau has then already been observed) or when both fired
    (eps=+1), or flags at cap. Cycles are detected to prove tau = infinity."""
    x = n
    pw = 1
    d = 0
    tau = None
    sigma = None
    seen_at = {}
    while d < cap:
        if x & 1:
            pw *= q
            x = (q * x + eps) >> 1
        else:
            x >>= 1
        d += 1
        if sigma is None and x < n:
            sigma = d
        if tau is None and pw < (1 << d):
            tau = d
        if tau is not None and (sigma is not None or eps > 0):
            # for eps=+1 sigma may exceed tau (threshold trap); we only need tau
            # here, sigma is tracked to measure Terras mismatches when it fired.
            return tau, sigma, False
        if tau is None and eps < 0:
            # cycle detection: values in a 3n-1 orbit are bounded once periodic
            k = seen_at.get(x)
            if k is not None:
                # entered a cycle at step k with coefficient still supercritical;
                # verify surplus over the cycle => tau = infinity, proven.
                cyc_len = d - k
                # count odd steps around the cycle once more, exactly
                oc = 0
                y = x
                for _ in range(cyc_len):
                    if y & 1:
                        oc += 1
                    y = step(q, eps, y)
                if q**oc > (1 << cyc_len):
                    return None, sigma, True
                seen_at.clear()
            seen_at[x] = d
    return tau, sigma, True


def scan_one_masked(q: int, n: int, cap: int, mask_bits: int) -> tuple[int | None, bool]:
    """tau only, values tracked mod 2^mask_bits (valid parities for cap steps).
    For q=5 eps=+1 divergent candidates never fire; flag at cap."""
    mask = (1 << mask_bits) - 1
    x = n & mask
    pw = 1
    for d in range(1, cap + 1):
        if x & 1:
            pw *= q
            x = ((q * x + 1) >> 1) & mask
        else:
            x >>= 1
        if pw.bit_length() <= d:  # q^o < 2^d  <=>  bit_length(q^o) <= d
            return d, False
    return None, True


def scan_payload(q: int, eps: int, limit: int, cap: int, tails: list[int]) -> dict[str, object]:
    started = perf_counter()
    tails_sorted = sorted(t for t in tails if t <= cap)
    tail_counts = {t: 0 for t in tails_sorted}
    flagged: list[int] = []
    mismatch_count = 0
    mismatch_samples: list[dict[str, int]] = []
    tau_sum = 0
    tau_finite = 0
    max_tau = 0
    max_tau_n = 0

    evens = limit // 2  # every even n has tau = sigma = 1
    tau_sum += evens
    tau_finite += evens

    masked_mode = q == 5 and eps == 1
    n = 1
    while n <= limit:
        if masked_mode:
            tau, is_flagged = scan_one_masked(q, n, cap, cap + 16)
            sigma = None
        else:
            tau, sigma, is_flagged = scan_one_exact(q, eps, n, cap)
        if is_flagged:
            flagged.append(n)
        else:
            tau_sum += tau
            tau_finite += 1
            if tau > max_tau:
                max_tau, max_tau_n = tau, n
            # For the exact eps=+1 scanner, returning at tau-fire with sigma=None
            # means sigma > tau strictly (a Terras violation). For eps=-1 sigma
            # is always observed by tau-fire (theorem sigma <= tau). The masked
            # q=5 scanner never tracks sigma, so it is excluded.
            if (not masked_mode and eps > 0 and sigma is None) or (sigma is not None and sigma != tau):
                mismatch_count += 1
                if len(mismatch_samples) < 12:
                    mismatch_samples.append({"n": n, "tau": tau, "sigma": sigma if sigma is not None else -1})
        upper = tau if tau is not None else cap + 1
        for t in tails_sorted:
            if upper > t:
                tail_counts[t] += 1
            else:
                break
        n += 2

    exact = {d: s for d, s in dp_rows(q, set(tails_sorted))}
    total_n = limit
    tails_out = []
    for t in tails_sorted:
        f = Fraction(exact[t], 1 << t)
        expected = float(f) * total_n
        tails_out.append(
            {
                "depth": t,
                "count_tau_gt_depth": tail_counts[t],
                "word_model_expected": round(expected, 3),
                "ratio": round(tail_counts[t] / expected, 6) if expected > 0 else None,
            }
        )

    elapsed = perf_counter() - started
    return {
        "mode": "scan",
        "q": q,
        "eps": eps,
        "limit": limit,
        "cap": cap,
        "elapsed_seconds": round(elapsed, 1),
        "flagged_frontier_residents": {
            "count": len(flagged),
            "density": len(flagged) / total_n,
            "samples": flagged[:40],
            "meaning": (
                "integers whose coefficient never dropped (tau = infinity proven via "
                "supercritical terminal cycle for eps=-1; tau > cap for q=5)"
            ),
        },
        "terras_mismatches_sigma_ne_tau": {
            "count": None if masked_mode else mismatch_count,
            "samples": mismatch_samples,
            "note": "sigma not tracked by the masked q=5 scanner" if masked_mode
            else "sigma < tau allowed for eps=-1 (theorem sigma<=tau); tau < sigma would be a threshold trap for eps=+1",
        },
        "mean_tau_over_finite": round(tau_sum / tau_finite, 6) if tau_finite else None,
        "max_finite_tau": {"n": max_tau_n, "tau": max_tau},
        "frontier_tails_vs_word_model": tails_out,
    }


# ---------------------------------------------------------------------------
# Self tests
# ---------------------------------------------------------------------------


def word_of(q: int, eps: int, r: int, depth: int) -> tuple[int, ...]:
    x = r
    w = []
    for _ in range(depth):
        w.append(x & 1)
        x = step(q, eps, x)
    return tuple(w)


def selftest_payload() -> dict[str, object]:
    checks = []

    # 1. residue <-> word bijection for all three maps, depths 1..10
    bij_ok = True
    for (q, eps) in [(3, 1), (3, -1), (5, 1)]:
        for depth in range(1, 11):
            words = {word_of(q, eps, r, depth) for r in range(1 << depth)}
            if len(words) != (1 << depth):
                bij_ok = False
    checks.append({"check": "terras_bijection_all_maps_depth_le_10", "pass": bij_ok})

    # 2. affine law with eps: T^d(2^d k + r) = q^o k + T^d(r)
    aff_ok = True
    for (q, eps) in [(3, -1), (5, 1)]:
        for depth in range(1, 9):
            for r in range(1 << depth):
                o = sum(word_of(q, eps, r, depth))
                img = r
                for _ in range(depth):
                    img = step(q, eps, img)
                for k in (1, 2, 5):
                    x = (1 << depth) * k + r
                    for _ in range(depth):
                        x = step(q, eps, x)
                    if x != q**o * k + img:
                        aff_ok = False
    checks.append({"check": "affine_law_with_eps", "pass": aff_ok})

    # 3. known cycles exist, are minimal, and obey the sign dichotomy
    dich = dichotomy_payload()
    checks.append({"check": "cycles_and_sign_dichotomy", "pass": dich["all_sign_rules_hold"]})

    # 4. sign theorems on scans: eps=-1 => sigma <= tau observed; eps=+1 => tau <= sigma
    st_ok = True
    for n in range(2, 2001):
        tau, sigma, fl = scan_one_exact(3, -1, n, 3000)
        if not fl and sigma is not None and tau is not None and sigma > tau:
            st_ok = False
    for n in range(2, 2001):
        tau, sigma, fl = scan_one_exact(3, 1, n, 3000)
        if not fl and tau is not None and sigma is not None and tau > sigma:
            st_ok = False
    checks.append({"check": "sign_theorems_sigma_vs_tau_n_le_2000", "pass": st_ok})

    # 5. frontier residents of 3n-1 up to 1000 are exactly the cycle minima
    flagged_small = [n for n in range(1, 1001, 2) if scan_one_exact(3, -1, n, 4096)[2]]
    checks.append(
        {
            "check": "3n-1_frontier_residents_le_1000_are_exactly_1_5_17",
            "value": flagged_small,
            "pass": flagged_small == [1, 5, 17],
        }
    )

    # 6. membership certificates for 1, 5, 17 under 3n-1
    mem = membership_payload()
    checks.append({"check": "membership_1_5_17_in_S_3minus", "pass": mem["all_proved"]})

    # 7. DP vs brute enumeration for q=5 at depth 12 and q=3 at depth 12
    dp5 = dict(dp_rows(5, {12}))[12]
    br5 = brute_survivors(5, 12)
    dp3 = dict(dp_rows(3, {12}))[12]
    br3 = brute_survivors(3, 12)
    checks.append({"check": "dp_vs_brute_depth_12", "values": {"q5": [dp5, br5], "q3": [dp3, br3]}, "pass": dp5 == br5 and dp3 == br3})

    # 8. q=3 word system matches the main instrument's anchors (eps-independence)
    anchors = dict(dp_rows(3, {20, 24, 28}))
    ok = anchors == {20: 27328, 24: 286581, 28: 3524586}
    checks.append({"check": "q3_word_system_matches_collatz_anchors", "pass": ok})

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
    p = sub.add_parser("dichotomy")
    p.add_argument("--out", default=None)
    p = sub.add_parser("membership")
    p.add_argument("--out", default=None)
    p = sub.add_parser("rates")
    p.add_argument("--q", type=int, default=5)
    p.add_argument("--max-depth", type=int, default=4096)
    p.add_argument("--out", default=None)
    p = sub.add_parser("scan")
    p.add_argument("--q", type=int, default=3)
    p.add_argument("--eps", type=int, default=-1)
    p.add_argument("--limit", type=int, default=1000000)
    p.add_argument("--cap", type=int, default=4096)
    p.add_argument("--tails", type=str, default="10,20,24,30,40,60,80,100")
    p.add_argument("--out", default=None)

    args = parser.parse_args()
    if args.cmd == "selftest":
        payload = selftest_payload()
        emit(payload, None)
        if not payload["all_pass"]:
            raise SystemExit(1)
    elif args.cmd == "dichotomy":
        emit(dichotomy_payload(), args.out)
    elif args.cmd == "membership":
        emit(membership_payload(), args.out)
    elif args.cmd == "rates":
        emit(rates_payload(args.q, args.max_depth), args.out)
    elif args.cmd == "scan":
        tails = [int(t) for t in args.tails.split(",") if t.strip()]
        emit(scan_payload(args.q, args.eps, args.limit, args.cap, tails), args.out)


if __name__ == "__main__":
    main()
