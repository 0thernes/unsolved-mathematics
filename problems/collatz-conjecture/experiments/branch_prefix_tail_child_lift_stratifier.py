#!/usr/bin/env python3
"""Stratify the child-residue lift behind the tail-memory separator.

The dichotomy classifier found that terminal/event features do not separate the
six lag-8 memory tails, while child residue modulo 4096 plus timing does.  This
script explains the precise failure at modulo 2048 and the extra bit that fixes
it.

This is finite evidence only.  It produces theorem targets for the exact
25 -> 26 retimed hard lift; it is not a proof of the Collatz conjecture.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from time import perf_counter
from types import SimpleNamespace

from branch_prefix_tail_dichotomy_classifier import run as run_dichotomy


def dict_counter(counter: Counter[object]) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.items()))


def key_text(parts: tuple[object, ...]) -> str:
    return "|".join(str(part) for part in parts)


def compact_record(record: dict[str, object], lower_modulus: int, upper_modulus: int) -> dict[str, object]:
    upper = int(record["child"]) % upper_modulus
    lower = int(record["child"]) % lower_modulus
    return {
        "label": record["label"],
        "parent": record["parent"],
        "child": record["child"],
        f"child_mod{lower_modulus}": lower,
        f"child_mod{upper_modulus}": upper,
        "lift_bit": upper // lower_modulus if upper_modulus == 2 * lower_modulus else None,
        "event_step": record["event_step"],
        "terminal_step": record["terminal_step"],
        "align": record["align"],
        "q_mod64": record["q_mod64"],
        "terminal_mod64": record["terminal_mod64"],
        "terminal_current_gap": record["terminal_current_gap"],
        "source_lag": record["source_lag"],
        "source_word": record["source_word"],
        "source_mod8192": record["source_mod8192"],
        "source_mod16384": record["source_mod16384"],
    }


def bucket_records(
    records: list[dict[str, object]],
    modulus: int,
    timing_feature: str,
) -> dict[tuple[int, object], list[dict[str, object]]]:
    buckets: dict[tuple[int, object], list[dict[str, object]]] = defaultdict(list)
    for record in records:
        buckets[(int(record["child"]) % modulus, record[timing_feature])].append(record)
    return buckets


def summarize_bucket(
    key: tuple[int, object],
    records: list[dict[str, object]],
    lower_modulus: int,
    upper_modulus: int,
) -> dict[str, object]:
    label_counts = Counter(str(record["label"]) for record in records)
    upper_counts: dict[int, Counter[str]] = defaultdict(Counter)
    for record in records:
        upper_counts[int(record["child"]) % upper_modulus][str(record["label"])] += 1

    return {
        "key": key_text(key),
        "counts": dict_counter(label_counts),
        "record_count": len(records),
        "is_pure": len(label_counts) == 1,
        "upper_split": [
            {
                f"child_mod{upper_modulus}": residue,
                "lift_bit": residue // lower_modulus if upper_modulus == 2 * lower_modulus else None,
                "counts": dict_counter(counts),
                "is_pure": len(counts) == 1,
            }
            for residue, counts in sorted(upper_counts.items())
        ],
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    if args.upper_modulus % args.lower_modulus != 0:
        raise SystemExit("--upper-modulus must be a multiple of --lower-modulus")

    classifier_args = SimpleNamespace(
        parent_depth=args.parent_depth,
        max_depth=args.max_depth,
        max_steps=args.max_steps,
        precision=args.precision,
        top_n=args.top_n,
        max_feature_set_size=args.max_feature_set_size,
        output=None,
        include_records=True,
        quiet=True,
    )
    base = run_dichotomy(classifier_args)
    records = list(base["records"])
    memory_records = [record for record in records if str(record["label"]) != "terminal_local"]

    lower_buckets = bucket_records(records, args.lower_modulus, args.timing_feature)
    upper_buckets = bucket_records(records, args.upper_modulus, args.timing_feature)

    memory_lower_keys = sorted(
        {
            (int(record["child"]) % args.lower_modulus, record[args.timing_feature])
            for record in memory_records
        }
    )
    memory_upper_keys = sorted(
        {
            (int(record["child"]) % args.upper_modulus, record[args.timing_feature])
            for record in memory_records
        }
    )

    memory_lower_bucket_summaries = [
        summarize_bucket(key, lower_buckets[key], args.lower_modulus, args.upper_modulus)
        for key in memory_lower_keys
    ]
    mixed_memory_lower_buckets = [
        summary for summary in memory_lower_bucket_summaries if not bool(summary["is_pure"])
    ]
    pure_memory_lower_buckets = [
        summary for summary in memory_lower_bucket_summaries if bool(summary["is_pure"])
    ]

    memory_upper_bucket_summaries = [
        summarize_bucket(key, upper_buckets[key], args.lower_modulus, args.upper_modulus)
        for key in memory_upper_keys
    ]
    mixed_memory_upper_buckets = [
        summary for summary in memory_upper_bucket_summaries if not bool(summary["is_pure"])
    ]

    terminal_collision_records = [
        compact_record(record, args.lower_modulus, args.upper_modulus)
        for key in memory_lower_keys
        for record in lower_buckets[key]
        if str(record["label"]) == "terminal_local"
    ]
    memory_details = [
        compact_record(record, args.lower_modulus, args.upper_modulus)
        for record in memory_records
    ]

    timing_values = Counter(str(record[args.timing_feature]) for record in memory_records)
    memory_upper_residues = sorted({int(record["child"]) % args.upper_modulus for record in memory_records})
    memory_lower_residues = sorted({int(record["child"]) % args.lower_modulus for record in memory_records})
    collision_lower_residues = sorted(
        int(str(summary["key"]).split("|", maxsplit=1)[0])
        for summary in mixed_memory_lower_buckets
    )

    high_bit_explanations = []
    for summary in mixed_memory_lower_buckets:
        lower_key = str(summary["key"])
        split = list(summary["upper_split"])
        high_bit_explanations.append(
            {
                "lower_bucket": lower_key,
                "upper_split": split,
                "all_upper_subbuckets_pure": all(bool(part["is_pure"]) for part in split),
            }
        )

    pure_claims = {
        "population_is_340": len(records) == 340,
        "memory_record_count_is_6": len(memory_records) == 6,
        "lower_modulus_timing_not_pure": bool(mixed_memory_lower_buckets),
        "lower_mixed_memory_bucket_count_is_2": len(mixed_memory_lower_buckets) == 2,
        "lower_terminal_collision_count_is_3": len(terminal_collision_records) == 3,
        "upper_modulus_timing_pure_on_memory_buckets": not mixed_memory_upper_buckets,
        "upper_memory_residues_are_expected_five": memory_upper_residues == [751, 1471, 1895, 2495, 3791],
        "timing_value_is_38_for_all_memory_records": dict(timing_values) == {"38": 6},
        "mixed_lower_buckets_split_purely_by_lift_bit": all(
            item["all_upper_subbuckets_pure"] for item in high_bit_explanations
        ),
    }

    return {
        "status": "branch-prefix-tail-child-lift-stratifier",
        "elapsed_seconds": round(perf_counter() - started, 6),
        "parameters": {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in vars(args).items()
        },
        "base_status": base["status"],
        "record_count": len(records),
        "label_counts": base["label_counts"],
        "timing_values_on_memory_records": dict_counter(timing_values),
        "memory_lower_residues": memory_lower_residues,
        "memory_upper_residues": memory_upper_residues,
        "collision_lower_residues": collision_lower_residues,
        "memory_lower_bucket_summaries": memory_lower_bucket_summaries,
        "pure_memory_lower_buckets": pure_memory_lower_buckets,
        "mixed_memory_lower_buckets": mixed_memory_lower_buckets,
        "memory_upper_bucket_summaries": memory_upper_bucket_summaries,
        "mixed_memory_upper_buckets": mixed_memory_upper_buckets,
        "high_bit_explanations": high_bit_explanations,
        "terminal_collision_records": terminal_collision_records,
        "memory_records": memory_details,
        "pure_claims": pure_claims,
        "theorem_target": (
            "Modulo 2048 plus timing leaves exactly two memory-bearing mixed "
            "buckets. Passing to modulo 4096 splits both by the next child bit, "
            "and the memory-bearing modulo-4096 timing buckets are pure."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--precision", type=int, default=80)
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--max-feature-set-size", type=int, default=3)
    parser.add_argument("--lower-modulus", type=int, default=2048)
    parser.add_argument("--upper-modulus", type=int, default=4096)
    parser.add_argument("--timing-feature", default="event_step")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    result = run(args)
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)


if __name__ == "__main__":
    main()
