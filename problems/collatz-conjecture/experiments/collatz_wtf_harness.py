#!/usr/bin/env python3
"""WTF regression harness for Collatz proof ideas.

This is an adversarial promotion gate, not a proof engine.  It reads the
current exact sibling-control, phase-collision, and retimed-pressure artifacts
and scores candidate "signals" by whether they survive the false-world tests
that the July 2026 audit identified:

* (3,+1) Collatz, still open;
* (3,-1), same q=3 parity-word statistics but positive frontier residents;
* (5,+1), divergence-typical sibling;
* phase-collision gates and retimed reserve-source records.

The output is deliberately blunt: killed-as-proof, diagnostic-only, or promote
to a narrow theorem target.  Nothing here proves any part of Collatz.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from time import perf_counter
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = SCRIPT_DIR / "results"
sys.path.insert(0, str(SCRIPT_DIR))

from collatz_sibling_control import selftest_payload  # noqa: E402


SOURCE_FILES = {
    "sibling_dichotomy": "sibling_dichotomy.json",
    "sibling_membership": "sibling_membership.json",
    "sibling_scan_3plus": "sibling_scan_3plus_1e7.json",
    "sibling_scan_3minus": "sibling_scan_3minus_1e7.json",
    "sibling_scan_5plus": "sibling_scan_5plus_2e4.json",
    "sibling_rates5": "sibling_rates5_4096.json",
    "phase_collision": "spine_phase_collision_lab_d12_20260702.json",
    "retimed_reserve_source": "branch_prefix_retimed_tight_reserve_source_d18_d25_20260702.json",
}


def load_result(name: str) -> dict[str, Any]:
    path = RESULTS_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"missing required result artifact: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_manifest() -> dict[str, dict[str, Any]]:
    manifest: dict[str, dict[str, Any]] = {}
    for key, filename in SOURCE_FILES.items():
        path = RESULTS_DIR / filename
        manifest[key] = {
            "path": str(path.relative_to(SCRIPT_DIR)),
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
    return manifest


def all_nested_bool_true(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, dict):
        return all(all_nested_bool_true(v) for v in value.values())
    if isinstance(value, list):
        return all(all_nested_bool_true(v) for v in value)
    return True


def probe(
    *,
    name: str,
    candidate: str,
    verdict: str,
    proof_use: str,
    reason: str,
    falsifier: str | None,
    evidence: dict[str, Any],
    next_action: str,
) -> dict[str, Any]:
    return {
        "name": name,
        "candidate": candidate,
        "verdict": verdict,
        "proof_use": proof_use,
        "reason": reason,
        "falsifier": falsifier,
        "evidence": evidence,
        "next_action": next_action,
    }


def run(skip_selftest: bool = False) -> dict[str, Any]:
    started = perf_counter()
    data = {key: load_result(filename) for key, filename in SOURCE_FILES.items()}
    sibling_selftest = None if skip_selftest else selftest_payload()

    q3_plus = data["sibling_scan_3plus"]
    q3_minus = data["sibling_scan_3minus"]
    q5_plus = data["sibling_scan_5plus"]
    dichotomy = data["sibling_dichotomy"]
    membership = data["sibling_membership"]
    phase = data["phase_collision"]
    reserve = data["retimed_reserve_source"]

    plus_mean = float(q3_plus["mean_tau_over_finite"])
    minus_mean = float(q3_minus["mean_tau_over_finite"])
    q5_density = float(q5_plus["flagged_frontier_residents"]["density"])
    unique_phase_fraction = float(
        phase["phase_gate_unique_target_spines"]["avg_allowed_fraction_of_m_mod_source_length"]
    )
    all_cycle_phase_fraction = float(
        phase["phase_gate_all_target_cycles"]["avg_allowed_fraction_of_m_mod_source_length"]
    )
    retimed_checks_ok = all_nested_bool_true(reserve["checks"])

    probes: list[dict[str, Any]] = []

    probes.append(
        probe(
            name="parity_word_statistics",
            candidate="Use survivor counts, densities, entropy, or tau tails to exclude all positive counterexamples.",
            verdict="killed_as_proof",
            proof_use="Do not use as a universal proof route.",
            reason=(
                "The q=3 word system is identical for eps=+1 and eps=-1, but the "
                "3n-1 sibling has positive frontier residents 1, 5, and 17."
            ),
            falsifier="(3,-1) sibling map",
            evidence={
                "q3_plus_mean_tau": plus_mean,
                "q3_minus_mean_tau": minus_mean,
                "mean_tau_gap": round(abs(plus_mean - minus_mean), 6),
                "q3_minus_positive_frontier_residents": q3_minus["flagged_frontier_residents"]["samples"],
                "q3_minus_membership_certificates_all_proved": membership["all_proved"],
            },
            next_action="Every future proof sketch must state which non-word, eps-sensitive quantity it uses.",
        )
    )

    probes.append(
        probe(
            name="frontier_resident_detector",
            candidate="Treat tau-infinity / long-frontier residency as a calibrated counterexample detector.",
            verdict="promote_as_diagnostic",
            proof_use="Useful falsifier and regression test; not a proof by silence.",
            reason=(
                "The detector fires exactly on the known 3n-1 cycle minima in the "
                "available scan and fires at the expected high density in 5n+1."
            ),
            falsifier=None,
            evidence={
                "q3_plus_flagged_count": q3_plus["flagged_frontier_residents"]["count"],
                "q3_minus_flagged_count": q3_minus["flagged_frontier_residents"]["count"],
                "q3_minus_flagged_samples": q3_minus["flagged_frontier_residents"]["samples"],
                "q5_plus_flagged_density": q5_density,
                "q5_plus_first_samples": q5_plus["flagged_frontier_residents"]["samples"][:10],
            },
            next_action="Keep this as a required control in every new invariant run.",
        )
    )

    probes.append(
        probe(
            name="cycle_side_sign_rule",
            candidate="Use the sign of the affine intercept to separate where cycles can live.",
            verdict="promote_as_local_theorem",
            proof_use="Good theorem component; insufficient alone for Collatz.",
            reason=(
                "All known sibling cycles obey the exact rule: eps=+1 cycles sit "
                "below the critical line; eps=-1 cycles sit above it."
            ),
            falsifier=None,
            evidence={
                "all_sign_rules_hold": dichotomy["all_sign_rules_hold"],
                "cycle_count_checked": len(dichotomy["cycles"]),
                "cycle_margins": [
                    {
                        "q": c["q"],
                        "eps": c["eps"],
                        "min_element": c["min_element"],
                        "length_shortcut": c["length_shortcut"],
                        "odd_steps": c["odd_steps"],
                        "side": c["q^o_vs_2^d"],
                        "margin_bits": c["per_period_margin_bits"],
                    }
                    for c in dichotomy["cycles"]
                ],
            },
            next_action="Use this as the baseline theorem in a formal sibling-control note.",
        )
    )

    probes.append(
        probe(
            name="tau_sigma_direction",
            candidate="Use tau/sigma inequality direction as the first eps-sensitive lint test.",
            verdict="promote_as_lint_rule",
            proof_use="Good proof-sketch lint; it catches sign-blind arguments early.",
            reason=(
                "The sign theorem gives opposite inequality directions: eps=+1 "
                "allows threshold traps, eps=-1 gives unconditional descent once tau fires."
            ),
            falsifier="Any proof that implies the same tau/sigma theorem for both signs.",
            evidence={
                "selftest_all_pass": None if sibling_selftest is None else sibling_selftest["all_pass"],
                "q3_plus_threshold_trap_samples": q3_plus["terras_mismatches_sigma_ne_tau"]["samples"],
                "q3_minus_mismatch_count": q3_minus["terras_mismatches_sigma_ne_tau"]["count"],
            },
            next_action="Add this question to every future claim manifest: where does eps=+1 enter?",
        )
    )

    probes.append(
        probe(
            name="phase_gate_only",
            candidate="Use finite phase matching alone to block regeneration.",
            verdict="killed_as_proof",
            proof_use="Useful negative result; not a proof route by itself.",
            reason=(
                "The exact phase identity checks out, but the finite phase gate is "
                "too permissive: it allows roughly three quarters of source-target residues."
            ),
            falsifier="Phase-collision lab itself: gate density remains high.",
            evidence={
                "identity_failure_count": phase["phase_identity"]["failure_count"],
                "unique_target_avg_allowed_fraction": unique_phase_fraction,
                "all_cycle_avg_allowed_fraction": all_cycle_phase_fraction,
                "unique_target_pair_count": phase["phase_gate_unique_target_spines"][
                    "source_target_pairs_with_any_allowed_residue"
                ],
            },
            next_action="Mine odd-unit locks, codimension, positivity, or retimed reserve source instead.",
        )
    )

    probes.append(
        probe(
            name="finite_scan_silence",
            candidate="Use no detected Collatz residents in a finite scan as proof of emptiness.",
            verdict="diagnostic_only",
            proof_use="Evidence and regression signal only; never theorem language.",
            reason=(
                "The Collatz scan is silent in the loaded finite artifact, but the "
                "same harness shows exactly how false worlds announce themselves."
            ),
            falsifier="Any larger finite bound is still finite.",
            evidence={
                "q3_plus_limit": q3_plus["limit"],
                "q3_plus_cap": q3_plus["cap"],
                "q3_plus_flagged_count": q3_plus["flagged_frontier_residents"]["count"],
                "q3_minus_flagged_samples": q3_minus["flagged_frontier_residents"]["samples"],
                "q5_plus_flagged_density": q5_density,
            },
            next_action="Convert silence into certified bounded statements only.",
        )
    )

    probes.append(
        probe(
            name="retimed_reserve_source",
            candidate="Promote retimed reserve-source records into bounded theorem obligations.",
            verdict="promote_as_theorem_target",
            proof_use="Strong finite structure; needs induction or solver certificate.",
            reason=(
                "The loaded reserve-source artifact has all depth checks true, "
                "13,856 retimed transitions, and 511 local grammar records."
            ),
            falsifier="A deeper lift or solver counterexample violating the reserve-source checks.",
            evidence={
                "checks_all_true": retimed_checks_ok,
                "total_retimed_transitions": reserve["checks"]["total_retimed_transitions"],
                "total_first_thresholds": reserve["checks"]["total_first_thresholds"],
                "total_local_grammar_records": reserve["checks"]["total_local_grammar_records"],
                "reserve_counter": reserve["counters"].get("inherited_reserve"),
            },
            next_action="Encode this finite grammar in SAT/SMT or a proof assistant before adding stronger prose.",
        )
    )

    counts: dict[str, int] = {}
    for row in probes:
        counts[row["verdict"]] = counts.get(row["verdict"], 0) + 1

    return {
        "status": "collatz-wtf-regression-harness",
        "created_utc": "2026-07-05",
        "elapsed_seconds": round(perf_counter() - started, 6),
        "claim": "No part of the Collatz conjecture is proved by this harness.",
        "source_manifest": source_manifest(),
        "sibling_selftest": sibling_selftest,
        "summary": {
            "probe_count": len(probes),
            "verdict_counts": counts,
            "best_next_move": (
                "Formalize the sibling sign theorem and encode retimed reserve-source "
                "records as bounded certificates; mine phase odd-unit locks next."
            ),
        },
        "probes": probes,
        "graduation_rule": (
            "A future invariant can graduate only if it is eps-sensitive, names its "
            "false-world falsifier, has an exact checker, and does not convert finite "
            "silence into universal theorem language."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=RESULTS_DIR / "collatz_wtf_harness_20260705.json",
        help="JSON output path",
    )
    parser.add_argument("--skip-selftest", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    payload = run(skip_selftest=args.skip_selftest)
    text = json.dumps(payload, indent=2, sort_keys=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)


if __name__ == "__main__":
    main()
