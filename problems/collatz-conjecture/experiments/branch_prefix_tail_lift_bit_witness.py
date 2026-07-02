#!/usr/bin/env python3
"""Extract the lift-bit witness inside the tail child-lift stratifier.

The child-lift stratifier shows that child mod 2048 plus event timing has two
mixed memory-bearing buckets, and child mod 4096 fixes them.  This script
extracts the sharper witness: a terminal-local record and a memory record with
the same lower bucket and the same visible terminal phase, differing only by
the next child lift bit among the local separator fields.

This is finite evidence only; it names a local theorem target, not a proof of
the Collatz conjecture.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


PHASE_FIELDS = (
    "terminal_step",
    "event_step",
    "align",
    "q_mod64",
    "terminal_mod64",
    "terminal_current_gap",
)
LOWER_PHASE_FIELDS = ("child_mod2048",) + PHASE_FIELDS
LOWER_LIFT_FIELDS = ("child_mod2048", "lift_bit")
UPPER_TIMING_FIELDS = ("child_mod4096", "event_step")


def dict_counter(counter: Counter[object]) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.items()))


def key(record: dict[str, object], fields: tuple[str, ...]) -> tuple[object, ...]:
    return tuple(record[field] for field in fields)


def key_text(parts: tuple[object, ...]) -> str:
    return "|".join(str(part) for part in parts)


def compact(record: dict[str, object]) -> dict[str, object]:
    return {
        "label": record["label"],
        "parent": record["parent"],
        "child": record["child"],
        "child_mod2048": record["child_mod2048"],
        "child_mod4096": record["child_mod4096"],
        "lift_bit": record["lift_bit"],
        "terminal_step": record["terminal_step"],
        "event_step": record["event_step"],
        "align": record["align"],
        "q_mod64": record["q_mod64"],
        "terminal_mod64": record["terminal_mod64"],
        "terminal_current_gap": record["terminal_current_gap"],
        "source_lag": record["source_lag"],
        "source_word": record["source_word"],
        "source_mod8192": record["source_mod8192"],
        "source_mod16384": record["source_mod16384"],
    }


def bucket(records: list[dict[str, object]], fields: tuple[str, ...]) -> dict[tuple[object, ...], list[dict[str, object]]]:
    buckets: dict[tuple[object, ...], list[dict[str, object]]] = defaultdict(list)
    for record in records:
        buckets[key(record, fields)].append(record)
    return buckets


def summarize_buckets(
    records: list[dict[str, object]],
    fields: tuple[str, ...],
) -> list[dict[str, object]]:
    summaries = []
    for bucket_key, bucket_records in sorted(bucket(records, fields).items(), key=lambda item: key_text(item[0])):
        labels = Counter(str(record["label"]) for record in bucket_records)
        summaries.append(
            {
                "key": key_text(bucket_key),
                "counts": dict_counter(labels),
                "is_pure": len(labels) == 1,
                "records": [compact(record) for record in bucket_records],
            }
        )
    return summaries


def mixed_summaries(summaries: list[dict[str, object]]) -> list[dict[str, object]]:
    return [summary for summary in summaries if not bool(summary["is_pure"])]


def run(args: argparse.Namespace) -> dict[str, object]:
    source = json.loads(args.input.read_text(encoding="utf-8"))
    records = list(source["memory_records"]) + list(source["terminal_collision_records"])

    phase_summaries = summarize_buckets(records, PHASE_FIELDS)
    lower_phase_summaries = summarize_buckets(records, LOWER_PHASE_FIELDS)
    lower_lift_summaries = summarize_buckets(records, LOWER_LIFT_FIELDS)
    upper_timing_summaries = summarize_buckets(records, UPPER_TIMING_FIELDS)

    mixed_lower_phase = mixed_summaries(lower_phase_summaries)
    witness = mixed_lower_phase[0] if mixed_lower_phase else None
    witness_records = list(witness["records"]) if witness else []

    same_lower_phase_opposite_labels = False
    witness_lift_values = []
    if witness_records:
        labels = {str(record["label"]) for record in witness_records}
        witness_lift_values = sorted({int(record["lift_bit"]) for record in witness_records})
        same_lower_phase_opposite_labels = len(labels) > 1

    memory_rule = [
        {
            "key": summary["key"],
            "counts": summary["counts"],
        }
        for summary in lower_lift_summaries
        if any(str(label).startswith("memory") for label in summary["counts"])
    ]
    terminal_collision_rule = [
        {
            "key": summary["key"],
            "counts": summary["counts"],
        }
        for summary in lower_lift_summaries
        if summary["counts"].get("terminal_local")
    ]

    pure_claims = {
        "candidate_record_count_is_9": len(records) == 9,
        "phase_signature_has_mixed_bucket": bool(mixed_summaries(phase_summaries)),
        "lower_phase_signature_has_mixed_bucket": bool(mixed_lower_phase),
        "lower_lift_signature_is_pure": not mixed_summaries(lower_lift_summaries),
        "upper_timing_signature_is_pure": not mixed_summaries(upper_timing_summaries),
        "witness_has_same_lower_phase_opposite_labels": same_lower_phase_opposite_labels,
        "witness_uses_both_lift_bits": witness_lift_values == [0, 1],
    }

    return {
        "status": "branch-prefix-tail-lift-bit-witness",
        "parameters": {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in vars(args).items()
        },
        "candidate_record_count": len(records),
        "phase_fields": list(PHASE_FIELDS),
        "lower_phase_fields": list(LOWER_PHASE_FIELDS),
        "lower_lift_fields": list(LOWER_LIFT_FIELDS),
        "upper_timing_fields": list(UPPER_TIMING_FIELDS),
        "pure_claims": pure_claims,
        "mixed_phase_signatures": mixed_summaries(phase_summaries),
        "mixed_lower_phase_signatures": mixed_lower_phase,
        "lower_lift_rule": lower_lift_summaries,
        "memory_lower_lift_rule": memory_rule,
        "terminal_collision_lower_lift_rule": terminal_collision_rule,
        "upper_timing_rule": upper_timing_summaries,
        "witness": witness,
        "theorem_target": (
            "A memory and terminal-local record share child mod 2048, event timing, "
            "alignment, q mod 64, terminal residue, and terminal-current gap. The "
            "next child lift bit separates them. Any proof using only the lower "
            "bucket and visible terminal phase is therefore insufficient for this "
            "finite lift."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("experiments/results/branch_prefix_tail_child_lift_stratifier_d25_d26_20260702.json"),
    )
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
