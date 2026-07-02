#!/usr/bin/env python3
"""Escape-envelope analyzer: quantifies the uniform positive-integer escape gap.

The certificate-frontier program (see CERTIFICATE-FRONTIER-THEOREMS.md) names
one missing theorem: a uniform escape principle sending every positive finite
shadow of the 2-adic survivor frontier into a usable descent certificate.

This instrument makes that gap quantitative in four exact layers:

1.  Exact survivor mass.  A per-depth dynamic program computes the exact
    number S(d) of parity prefixes that survive the multiplier test
    3^o >= 2^j at every prefix depth j <= d.  By the Terras parity-word
    bijection, S(d)/2^d is exactly the density of residues mod 2^d left
    uncertified by the depth-d certificate pass.

2.  Proved-bound check.  Theorem 7 in CERTIFICATE-FRONTIER-THEOREMS.md proves

        S(d) <= sum_{k >= o_min(d)} C(d, k) <= 2^(d * H(theta)),

    where theta = log_3 2 and o_min(d) = min{o : 3^o >= 2^d}.  Hence the
    uncertified density is at most 2^(-(1 - H(theta)) * d).  Both
    inequalities are re-verified here at every computed depth, the first in
    exact integer arithmetic.

3.  Envelope constants.  1 - H(theta) = D(theta || 1/2) is the asymptotic
    decay rate in bits per step, so the first-moment escape envelope for the
    worst certificate depth over b-bit survivors is

        D_1(b) = max { d : b + log2(S(d)) - d >= 0 },

    with asymptotic slope c* = 1 / (1 - H(theta)) = 19.98...  This is the
    stopping-time analogue of the Lagarias-Weiss total-stopping-time
    constant 41.677647.

4.  Free-coin test.  For selected base depths b, the exact frontier is
    enumerated and every representative's first usable certificate depth is
    measured (reusing frontier_escape_analyzer).  The measured alive curve
    alive_b(d) is compared to the word-model prediction 2^b * S(d) / 2^d.
    The deviation measures how determined integer continuations differ from
    fresh parity coins - the exact content of the missing escape theorem.

Research instrument, not a proof.
"""

from __future__ import annotations

import argparse
import json
import math
from decimal import Decimal, getcontext
from time import perf_counter

from frontier_escape_analyzer import analyze as frontier_analyze

KNOWN_SURVIVOR_COUNTS = {20: 27_328, 24: 286_581, 28: 3_524_586}
LOGGED_ESCAPE_RECORDS = {20: 183, 24: 287, 28: 395}


def exact_log2(n: int) -> float:
    """log2 of an arbitrarily large positive integer, safe beyond float range."""
    if n <= 0:
        raise ValueError("exact_log2 requires a positive integer")
    bl = n.bit_length()
    if bl <= 900:
        return math.log2(n)
    shift = bl - 60
    return shift + math.log2(n >> shift)


def envelope_constants(digits: int) -> dict[str, object]:
    getcontext().prec = digits + 15
    ln2 = Decimal(2).ln()
    ln3 = Decimal(3).ln()
    theta = ln2 / ln3
    log2_theta = theta.ln() / ln2
    log2_comp = (1 - theta).ln() / ln2
    entropy = -(theta * log2_theta + (1 - theta) * log2_comp)
    rate = 1 - entropy
    c_star = 1 / rate

    def fmt(x: Decimal) -> str:
        return str(+x)[: digits + 2]

    return {
        "theta_log3_2": fmt(theta),
        "binary_entropy_H_theta": fmt(entropy),
        "decay_rate_1_minus_H": fmt(rate),
        "envelope_slope_c_star": fmt(c_star),
        "decay_rate_float": float(rate),
        "envelope_slope_float": float(c_star),
        "lagarias_weiss_total_stopping_analogue": 41.677647,
    }


def survivor_dp(max_depth: int) -> tuple[list[int], list[int]]:
    """Exact survivor counts S(d) and minimal live odd count, d = 1..max_depth."""
    states: dict[int, int] = {0: 1}
    pow3 = [1]
    counts: list[int] = []
    min_odds: list[int] = []

    for depth in range(1, max_depth + 1):
        pow3.append(pow3[-1] * 3)
        boundary = 1 << depth
        nxt: dict[int, int] = {}
        for odd_count, count in states.items():
            for child in (odd_count, odd_count + 1):
                if pow3[child] >= boundary:
                    nxt[child] = nxt.get(child, 0) + count
        states = nxt
        counts.append(sum(states.values()))
        min_odds.append(min(states) if states else 0)

    return counts, min_odds


def verify_proved_bounds(
    counts: list[int], min_odds: list[int], entropy_bits: float, check_every: int
) -> dict[str, object]:
    """Check C(d,o_min)/d <= S(d) <= binomial tail <= 2^(d*H(theta)) on a grid.

    Upper chain: Theorem 7 (endpoint tail + entropy).  Lower: Theorem 8
    (cycle-lemma bound; every cyclic class of words with 3^o > 2^d contains a
    survivor, so S(d) >= C(d,o)/d for each admissible o).  Both checked in
    exact integer arithmetic.
    """
    worst_exact_slack_bits = None
    worst_entropy_slack_bits = None
    worst_lower_slack_bits = None
    checked = 0
    for index, survivors in enumerate(counts):
        depth = index + 1
        if depth != 1 and depth != len(counts) and depth % check_every != 0:
            continue
        checked += 1
        k_min = min_odds[index]
        tail = sum(math.comb(depth, k) for k in range(k_min, depth + 1))
        if survivors > tail:
            raise AssertionError(
                f"exact endpoint-tail bound violated at depth {depth}: "
                f"S={survivors} > tail={tail}"
            )
        log2_tail = exact_log2(tail)
        if log2_tail > depth * entropy_bits + 1e-6:
            raise AssertionError(
                f"entropy bound violated at depth {depth}: "
                f"log2(tail)={log2_tail} > d*H={depth * entropy_bits}"
            )
        lower = math.comb(depth, k_min) // depth
        if lower > survivors:
            raise AssertionError(
                f"cycle-lemma lower bound violated at depth {depth}: "
                f"C(d,o_min)/d={lower} > S={survivors}"
            )
        exact_slack = exact_log2(tail) - exact_log2(survivors)
        entropy_slack = depth * entropy_bits - exact_log2(survivors)
        lower_slack = exact_log2(survivors) - (exact_log2(lower) if lower else 0.0)
        if worst_exact_slack_bits is None or exact_slack < worst_exact_slack_bits:
            worst_exact_slack_bits = exact_slack
        if worst_entropy_slack_bits is None or entropy_slack < worst_entropy_slack_bits:
            worst_entropy_slack_bits = entropy_slack
        if worst_lower_slack_bits is None or lower_slack < worst_lower_slack_bits:
            worst_lower_slack_bits = lower_slack
    return {
        "checked_depths": checked,
        "exact_endpoint_tail_bound_held": True,
        "entropy_bound_held": True,
        "cycle_lemma_lower_bound_held": True,
        "min_slack_vs_endpoint_tail_bits": round(worst_exact_slack_bits, 6),
        "min_slack_vs_entropy_bound_bits": round(worst_entropy_slack_bits, 6),
        "min_slack_vs_cycle_lower_bits": round(worst_lower_slack_bits, 6),
    }


def dp_rows(
    counts: list[int], min_odds: list[int], report_every: int, decay_rate: float
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    max_depth = len(counts)
    for depth in range(1, max_depth + 1):
        if depth != 1 and depth != max_depth and depth % report_every != 0:
            continue
        survivors = counts[depth - 1]
        log2_frac = exact_log2(survivors) - depth
        rows.append(
            {
                "depth": depth,
                "survivors": survivors if survivors.bit_length() <= 128 else None,
                "log2_survivors": round(exact_log2(survivors), 6),
                "log2_fraction": round(log2_frac, 6),
                "effective_rate_bits_per_step": round(-log2_frac / depth, 9),
                "proved_rate_bits_per_step": round(decay_rate, 9),
                "min_live_odd_count": min_odds[depth - 1],
            }
        )
    return rows


def log2_fraction_table(counts: list[int]) -> list[float]:
    return [exact_log2(s) - (i + 1) for i, s in enumerate(counts)]


def first_moment_envelope(log2_frac: list[float], bits: int) -> dict[str, object]:
    """Depths where the expected survivor count 2^b * frac(d) crosses 1 and 0.01."""
    crossing_one = None
    crossing_low = None
    for index, value in enumerate(log2_frac):
        depth = index + 1
        expected_bits = bits + value
        if expected_bits >= 0:
            crossing_one = depth
        if expected_bits >= math.log2(0.01):
            crossing_low = depth
    return {
        "bits": bits,
        "first_moment_crossing_depth": crossing_one,
        "expected_0.01_bracket_depth": crossing_low,
    }


def alive_curve_from_histogram(
    histogram: dict[str, int], analyzed: int
) -> list[tuple[int, int]]:
    """(depth, count of representatives still uncertified strictly beyond depth)."""
    pairs = sorted((int(k), v) for k, v in histogram.items())
    alive = analyzed
    curve: list[tuple[int, int]] = []
    for depth, certified_here in pairs:
        curve.append((depth - 1, alive))
        alive -= certified_here
        curve.append((depth, alive))
    return curve


def deviation_samples(
    curve: list[tuple[int, int]],
    log2_frac: list[float],
    bits: int,
    sample_every: int,
) -> list[dict[str, object]]:
    samples: list[dict[str, object]] = []
    seen: set[int] = set()
    last_positive = max((d for d, a in curve if a > 0), default=None)
    wanted: set[int] = set()
    for depth, _alive in curve:
        if depth % sample_every == 0:
            wanted.add(depth)
    if last_positive is not None:
        wanted.add(last_positive)
    for depth, alive in curve:
        if depth not in wanted or depth in seen or alive <= 0:
            continue
        if depth < 1 or depth > len(log2_frac):
            continue
        seen.add(depth)
        predicted = bits + log2_frac[depth - 1]
        samples.append(
            {
                "depth": depth,
                "alive": alive,
                "log2_alive": round(math.log2(alive), 6),
                "word_model_log2_expected": round(predicted, 6),
                "deviation_bits": round(math.log2(alive) - predicted, 6),
            }
        )
    return samples


def escape_layer(
    base_depth: int,
    max_escape_depth: int,
    log2_frac: list[float],
    top_n: int,
    step_limit: int,
    sample_every: int,
) -> dict[str, object]:
    payload = frontier_analyze(
        base_depth=base_depth,
        max_escape_depth=max_escape_depth,
        top_n=top_n,
        max_frontier=None,
        sample_stride=1,
        sample_offset=0,
        step_limit=step_limit,
        sample_limit=2,
    )
    analysis = payload["analysis"]
    frontier = payload["frontier"]
    assert isinstance(analysis, dict)
    assert isinstance(frontier, dict)

    histogram = analysis["certificate_depth_histogram"]
    assert isinstance(histogram, dict)
    analyzed = int(analysis["certified_count"]) + int(analysis["uncertified_count"])
    curve = alive_curve_from_histogram(histogram, analyzed)
    envelope = first_moment_envelope(log2_frac, base_depth)
    observed_max = int(analysis["max_certificate_depth"])
    record_rows = analysis["record_setters_by_certificate_depth"]
    assert isinstance(record_rows, list)
    final_record = record_rows[-1] if record_rows else None

    crossing = envelope["first_moment_crossing_depth"]
    return {
        "base_depth": base_depth,
        "frontier_count": frontier["frontier_count"],
        "certified_count": analysis["certified_count"],
        "uncertified_count": analysis["uncertified_count"],
        "observed_max_certificate_depth": observed_max,
        "observed_ratio_depth_per_bit": round(observed_max / base_depth, 6),
        "first_moment_crossing_depth": crossing,
        "expected_0.01_bracket_depth": envelope["expected_0.01_bracket_depth"],
        "observed_minus_crossing": (observed_max - crossing) if crossing else None,
        "worst_start": int(final_record["start"]) if final_record else None,
        "deviation_samples": deviation_samples(
            curve, log2_frac, base_depth, sample_every
        ),
        "elapsed_seconds": payload["elapsed_seconds"],
    }


def self_test(max_brute_depth: int) -> dict[str, object]:
    """Brute-force validation of the DP against integer trajectories and words."""

    def shortcut(x: int) -> int:
        return x // 2 if x % 2 == 0 else (3 * x + 1) // 2

    counts, min_odds = survivor_dp(max(max_brute_depth, 28))

    for depth in range(1, max_brute_depth + 1):
        pow3 = [3**i for i in range(depth + 1)]
        brute = 0
        words: set[tuple[int, ...]] = set()
        for r in range(1 << depth):
            x = r
            odd = 0
            word: list[int] = []
            alive = True
            for j in range(1, depth + 1):
                parity = x & 1
                word.append(parity)
                odd += parity
                x = shortcut(x)
                if alive and pow3[odd] < (1 << j):
                    alive = False
            words.add(tuple(word))
            if alive:
                brute += 1
        if len(words) != (1 << depth):
            raise AssertionError(
                f"parity-word bijection failed at depth {depth}: "
                f"{len(words)} distinct words for {1 << depth} residues"
            )
        if brute != counts[depth - 1]:
            raise AssertionError(
                f"DP mismatch at depth {depth}: brute={brute}, dp={counts[depth - 1]}"
            )

    for depth, expected in KNOWN_SURVIVOR_COUNTS.items():
        if counts[depth - 1] != expected:
            raise AssertionError(
                f"anchor mismatch at depth {depth}: "
                f"dp={counts[depth - 1]}, expected={expected}"
            )

    return {
        "brute_force_depths_checked": max_brute_depth,
        "parity_word_bijection_verified": True,
        "dp_matches_integer_enumeration": True,
        "anchors_verified": {str(k): v for k, v in KNOWN_SURVIVOR_COUNTS.items()},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-dp-depth", type=int, default=640)
    parser.add_argument("--dp-report-every", type=int, default=32)
    parser.add_argument("--base-depths", type=str, default="14,16,18,20,22,24")
    parser.add_argument("--max-escape-depth", type=int, default=896)
    parser.add_argument("--skip-escape", action="store_true")
    parser.add_argument("--top-n", type=int, default=3)
    parser.add_argument("--step-limit", type=int, default=100000)
    parser.add_argument("--deviation-sample-every", type=int, default=24)
    parser.add_argument("--bound-check-every", type=int, default=16)
    parser.add_argument("--probe-depths", type=str, default="")
    parser.add_argument("--constants-digits", type=int, default=40)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--self-test-depth", type=int, default=14)
    parser.add_argument("--json-out", type=str, default=None)
    args = parser.parse_args()

    if args.max_dp_depth < 32:
        raise SystemExit("--max-dp-depth must be at least 32")

    started = perf_counter()
    constants = envelope_constants(args.constants_digits)
    payload: dict[str, object] = {"constants": constants}

    if args.self_test:
        payload["self_test"] = self_test(args.self_test_depth)

    counts, min_odds = survivor_dp(args.max_dp_depth)
    decay_rate = float(constants["decay_rate_float"])
    payload["proved_bound_check"] = verify_proved_bounds(
        counts, min_odds, 1 - decay_rate, args.bound_check_every
    )
    payload["survivor_dp_rows"] = dp_rows(
        counts, min_odds, args.dp_report_every, decay_rate
    )

    log2_frac = log2_fraction_table(counts)
    if args.probe_depths:
        payload["probes"] = [
            {
                "depth": depth,
                "log2_fraction": round(log2_frac[depth - 1], 6),
                "minus_log2_fraction": round(-log2_frac[depth - 1], 6),
            }
            for depth in (
                int(x) for x in args.probe_depths.split(",") if x.strip()
            )
            if 1 <= depth <= len(log2_frac)
        ]
    payload["first_moment_envelope"] = [
        first_moment_envelope(log2_frac, bits)
        for bits in (14, 16, 18, 20, 22, 24, 28, 32, 48, 64, 71, 128)
    ]

    if not args.skip_escape:
        base_depths = [int(x) for x in args.base_depths.split(",") if x.strip()]
        escapes: list[dict[str, object]] = []
        for base_depth in base_depths:
            escapes.append(
                escape_layer(
                    base_depth=base_depth,
                    max_escape_depth=args.max_escape_depth,
                    log2_frac=log2_frac,
                    top_n=args.top_n,
                    step_limit=args.step_limit,
                    sample_every=args.deviation_sample_every,
                )
            )
        payload["escape_layers"] = escapes
        payload["logged_records_for_context"] = {
            str(k): v for k, v in LOGGED_ESCAPE_RECORDS.items()
        }

    payload["elapsed_seconds"] = round(perf_counter() - started, 3)
    payload["interpretation"] = (
        "The proved bound caps the uncertified density at 2^(-(1-H(theta))d) "
        "unconditionally. The first-moment crossings and deviation samples "
        "quantify the conjectural pointwise escape envelope; deviations of the "
        "alive curves from the word model are the measurable content of the "
        "missing uniform escape theorem. No proof of Collatz is claimed."
    )

    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
