#!/usr/bin/env python3
"""Solve the lifted residue classes behind the tail-memory words.

The word-map analyzer showed that the raw modulo-256 parity cylinder does not
force the memory paths through `59 mod 64`.  This script separates two facts:

* the bridge `59 mod 64 -> 25 mod 64` is already forced by a modulo-8192 lift;
* the final terminal residue modulo 64 needs one more source bit, i.e. a
  modulo-16384 lift.

It also identifies the local ghost class left by the bridge condition.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from time import perf_counter

from branch_potential_analyzer import round_float
from branch_prefix_tail_memory_word_maps import WORDS, affine_map, cylinder_residue, residue_path


FULL_EXTRA_BITS = 6
BRIDGE_EXTRA_BITS = 5


def dict_counter(counter: Counter[object]) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.items()))


def parity_cylinder_lifts(word: str, extra_bits: int = FULL_EXTRA_BITS) -> list[int]:
    residue = cylinder_residue(word)
    step = 1 << len(word)
    modulus = 1 << (len(word) + extra_bits)
    return list(range(residue, modulus, step))


def lift_parameter(source_residue: int, word: str) -> int:
    residue = cylinder_residue(word)
    return ((source_residue - residue) // (1 << len(word))) % (1 << FULL_EXTRA_BITS)


def path_record(source_residue: int, word: str, observed_count: int) -> dict[str, object]:
    path = residue_path(source_residue, len(word), 64)
    return {
        "source_mod_16384": source_residue,
        "m_mod_64": lift_parameter(source_residue, word),
        "path_mod_64": path,
        "passes_59_mod64": 59 in path,
        "has_bridge_59_to_25_preterminal": path[-3] == 59 and path[-2] == 25,
        "terminal_mod_64": path[-1],
        "observed_count": observed_count,
    }


def forced_classes_by_extra_bits(word: str, full_records: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for extra_bits in range(FULL_EXTRA_BITS + 1):
        modulus = 1 << (len(word) + extra_bits)
        groups: dict[int, list[dict[str, object]]] = defaultdict(list)
        for record in full_records:
            groups[int(record["source_mod_16384"]) % modulus].append(record)

        forced_bridge = []
        possible_bridge = []
        forced_pass59 = []
        possible_pass59 = []
        for projected, records in sorted(groups.items()):
            bridge_flags = [bool(record["has_bridge_59_to_25_preterminal"]) for record in records]
            pass_flags = [bool(record["passes_59_mod64"]) for record in records]
            if any(bridge_flags):
                possible_bridge.append(projected)
            if all(bridge_flags):
                forced_bridge.append(projected)
            if any(pass_flags):
                possible_pass59.append(projected)
            if all(pass_flags):
                forced_pass59.append(projected)

        rows.append(
            {
                "extra_bits_above_word": extra_bits,
                "modulus": modulus,
                "group_count": len(groups),
                "forced_bridge_class_count": len(forced_bridge),
                "forced_bridge_classes": forced_bridge,
                "possible_bridge_class_count": len(possible_bridge),
                "possible_bridge_classes": possible_bridge,
                "forced_pass59_class_count": len(forced_pass59),
                "forced_pass59_classes": forced_pass59,
                "possible_pass59_class_count": len(possible_pass59),
                "possible_pass59_classes": possible_pass59,
            }
        )
    return rows


def q_mod64_for_alignment(terminal_mod64: int, align: int) -> int:
    return ((terminal_mod64 + 1) * pow(pow(3, align, 64), -1, 64)) % 64


def word_report(word: str, memory_records: list[dict[str, object]]) -> dict[str, object]:
    residue = cylinder_residue(word)
    affine = affine_map(word)
    matched = [record for record in memory_records if str(record["source_to_terminal_parity_word"]) == word]
    observed_sources = Counter(int(record["source_state"]) % (1 << (len(word) + FULL_EXTRA_BITS)) for record in matched)
    observed_aligns = sorted({int(record["align"]) for record in matched})

    full_records = [
        path_record(source_residue, word, int(observed_sources[source_residue]))
        for source_residue in parity_cylinder_lifts(word)
    ]
    bridge_records = [record for record in full_records if bool(record["has_bridge_59_to_25_preterminal"])]
    pass59_records = [record for record in full_records if bool(record["passes_59_mod64"])]
    ghost_records = [record for record in bridge_records if int(record["observed_count"]) == 0]
    forced_rows = forced_classes_by_extra_bits(word, full_records)
    bridge_row = forced_rows[BRIDGE_EXTRA_BITS]

    for record in bridge_records:
        record["q_mod64_by_observed_align"] = {
            str(align): q_mod64_for_alignment(int(record["terminal_mod_64"]), align) for align in observed_aligns
        }

    observed_projection_counts_mod8192 = Counter(
        int(source) % (1 << (len(word) + BRIDGE_EXTRA_BITS)) for source, count in observed_sources.items() for _ in range(count)
    )
    observed_terminal_counts = Counter(
        int(record["terminal_mod_64"])
        for record in bridge_records
        for _ in range(int(record["observed_count"]))
    )
    observed_q_mod64_by_align = Counter()
    for record in bridge_records:
        count = int(record["observed_count"])
        if count == 0:
            continue
        for align, q_mod64 in dict(record["q_mod64_by_observed_align"]).items():
            observed_q_mod64_by_align[f"align={align};q_mod64={q_mod64}"] += count

    return {
        "word": word,
        "length": len(word),
        "cylinder_residue_mod_256": residue,
        "affine": affine,
        "affine_formula": f"T^{len(word)}(n) = ({affine['multiplier']}*n + {affine['constant']})/{affine['denominator']}",
        "observed_record_count": len(matched),
        "observed_aligns": observed_aligns,
        "observed_source_mod_16384_counts": dict_counter(observed_sources),
        "observed_projection_mod_8192_counts": dict_counter(observed_projection_counts_mod8192),
        "observed_terminal_mod64_counts": dict_counter(observed_terminal_counts),
        "observed_q_mod64_by_align": dict_counter(observed_q_mod64_by_align),
        "pass59_full_lifts": pass59_records,
        "bridge_full_lifts": bridge_records,
        "ghost_bridge_full_lifts": ghost_records,
        "forced_classes_by_extra_bits": forced_rows,
        "minimal_extra_bits_with_forced_bridge_classes": next(
            row["extra_bits_above_word"] for row in forced_rows if int(row["forced_bridge_class_count"]) > 0
        ),
        "bridge_projection_mod_8192": bridge_row["forced_bridge_classes"],
        "pure_claims": {
            "all_observed_full_lifts_are_bridge": all(
                bool(record["has_bridge_59_to_25_preterminal"])
                for record in full_records
                if int(record["observed_count"]) > 0
            ),
            "observed_project_to_forced_bridge_mod8192": all(
                source % (1 << (len(word) + BRIDGE_EXTRA_BITS)) in bridge_row["forced_bridge_classes"]
                for source in observed_sources
            ),
            "bridge_forced_first_at_extra_bits_5": not any(
                int(row["forced_bridge_class_count"]) > 0 for row in forced_rows[:BRIDGE_EXTRA_BITS]
            )
            and int(bridge_row["forced_bridge_class_count"]) > 0,
            "has_ghost_bridge_full_lift": bool(ghost_records),
        },
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    memory_payload = json.loads(args.memory_result.read_text(encoding="utf-8"))
    memory_records = list(memory_payload["records"])
    reports = [word_report(word, memory_records) for word in WORDS]
    ghost_count = sum(len(report["ghost_bridge_full_lifts"]) for report in reports)
    pure_claims = {
        "all_observed_full_lifts_are_bridge": all(
            report["pure_claims"]["all_observed_full_lifts_are_bridge"] for report in reports
        ),
        "all_observed_project_to_forced_bridge_mod8192": all(
            report["pure_claims"]["observed_project_to_forced_bridge_mod8192"] for report in reports
        ),
        "bridge_is_first_forced_at_extra_bits_5_for_all_words": all(
            report["pure_claims"]["bridge_forced_first_at_extra_bits_5"] for report in reports
        ),
        "there_is_exactly_one_unobserved_bridge_full_lift": ghost_count == 1,
    }
    return {
        "status": "branch-prefix-tail-memory-lift-solver",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()
        },
        "memory_record_count": len(memory_records),
        "full_lift_modulus": 1 << (8 + FULL_EXTRA_BITS),
        "bridge_lift_modulus": 1 << (8 + BRIDGE_EXTRA_BITS),
        "pure_claims": pure_claims,
        "word_reports": reports,
        "interpretation": (
            "Local lifted-residue solver for the two memory-tail words. The "
            "low-repeat bridge is forced at modulus 8192; the terminal residue "
            "needs modulus 16384. The remaining ghost full lift is a local "
            "candidate class, not an observed memory record."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--memory-result",
        type=Path,
        default=Path("experiments/results/branch_prefix_tail_memory_cases_d25_d26_20260702.json"),
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if not args.memory_result.exists():
        raise SystemExit(f"memory result not found: {args.memory_result}")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)


if __name__ == "__main__":
    main()
