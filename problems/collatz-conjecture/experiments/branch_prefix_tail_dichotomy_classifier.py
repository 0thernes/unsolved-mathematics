#!/usr/bin/env python3
"""Mine classifiers for terminal-local vs memory-tail post-ladder units.

The ghost audit showed the post-ladder tail splits into 334 terminal-local
cases and 6 lag-8 memory cases.  This script recomputes the same population and
searches small terminal/event-side feature sets whose buckets are pure for that
dichotomy.

This is finite evidence only.  Its role is to suggest theorem-facing local
features, not to prove the global Collatz conjecture.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from collections import Counter, defaultdict
from decimal import Decimal, getcontext
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parent))

from branch_potential_analyzer import enumerate_frontier, powers_of_three, round_float
from branch_prefix_dominance_analyzer import analyze_prefix_start
from branch_prefix_post_ladder_tail import reconstruct_tail
from branch_prefix_pressure_unit_classifier import unit_regime
from branch_prefix_retimed_pressure import transition_row
from branch_prefix_tail_memory_cases import shortcut_segment
from branch_prefix_tail_phase import dec_string, detailed_trace, required_lower_edge
from branch_prefix_tail_phase_spectrum import max_source_before, observation_by_step_state


FEATURE_NAMES = (
    "child_mod64",
    "child_mod128",
    "child_mod256",
    "child_mod512",
    "child_mod1024",
    "child_mod2048",
    "child_mod4096",
    "child_mod8192",
    "child_mod16384",
    "child_mod65536",
    "terminal_step",
    "event_step",
    "last_credit_step",
    "align",
    "q_mod16",
    "q_mod32",
    "q_mod64",
    "terminal_mod16",
    "terminal_mod32",
    "terminal_mod64",
    "event_required",
    "terminal_required",
    "parent_required",
    "required_above_parent",
    "transition_credit_delta",
    "terminal_current_gap",
    "terminal_current_form",
    "terminal_step_mod8",
    "event_step_mod8",
)

TERMINAL_EVENT_FEATURE_NAMES = (
    "terminal_step",
    "event_step",
    "last_credit_step",
    "align",
    "q_mod16",
    "q_mod32",
    "q_mod64",
    "terminal_mod16",
    "terminal_mod32",
    "terminal_mod64",
    "event_required",
    "terminal_required",
    "parent_required",
    "required_above_parent",
    "transition_credit_delta",
    "terminal_current_gap",
    "terminal_current_form",
    "terminal_step_mod8",
    "event_step_mod8",
)


def dict_counter(counter: Counter[object]) -> dict[str, int]:
    return dict(sorted((str(key), int(value)) for key, value in counter.items()))


def label_name(source_lag: int) -> str:
    return "terminal_local" if source_lag == 0 else f"memory_lag_{source_lag}"


def source_word(source_state: int, lag: int) -> str | None:
    if lag <= 0 or lag > 16:
        return None
    return str(shortcut_segment(source_state, lag)["parity_word"])


def feature_key(record: dict[str, object], features: tuple[str, ...]) -> tuple[object, ...]:
    return tuple(record[name] for name in features)


def feature_key_text(key: tuple[object, ...]) -> str:
    return "|".join(str(part) for part in key)


def evaluate_features(records: list[dict[str, object]], features: tuple[str, ...]) -> dict[str, object]:
    buckets: dict[tuple[object, ...], Counter[str]] = defaultdict(Counter)
    for record in records:
        buckets[feature_key(record, features)][str(record["label"])] += 1

    mixed = {
        key: counts
        for key, counts in buckets.items()
        if len(counts) > 1
    }
    memory_keys = {
        key: counts
        for key, counts in buckets.items()
        if any(label.startswith("memory") for label in counts)
    }
    terminal_keys = {
        key: counts
        for key, counts in buckets.items()
        if counts.get("terminal_local", 0)
    }
    memory_record_count = sum(
        int(record["label"] != "terminal_local") for record in records
    )
    terminal_record_count = len(records) - memory_record_count
    memory_covered_by_pure_keys = sum(
        sum(count for label, count in counts.items() if label.startswith("memory"))
        for key, counts in memory_keys.items()
        if key not in mixed
    )
    terminal_covered_by_pure_keys = sum(
        int(counts["terminal_local"])
        for key, counts in terminal_keys.items()
        if key not in mixed and "terminal_local" in counts
    )
    return {
        "features": list(features),
        "bucket_count": len(buckets),
        "mixed_bucket_count": len(mixed),
        "is_pure": not mixed,
        "memory_key_count": len(memory_keys),
        "terminal_key_count": len(terminal_keys),
        "memory_covered_by_pure_keys": memory_covered_by_pure_keys,
        "terminal_covered_by_pure_keys": terminal_covered_by_pure_keys,
        "memory_record_count": memory_record_count,
        "terminal_record_count": terminal_record_count,
        "memory_keys": [
            {
                "key": feature_key_text(key),
                "counts": dict_counter(counts),
            }
            for key, counts in sorted(memory_keys.items(), key=lambda item: feature_key_text(item[0]))
        ],
        "mixed_examples": [
            {
                "key": feature_key_text(key),
                "counts": dict_counter(counts),
            }
            for key, counts in sorted(mixed.items(), key=lambda item: feature_key_text(item[0]))[:8]
        ],
    }


def mine_feature_sets(records: list[dict[str, object]], max_size: int, top_n: int) -> dict[str, object]:
    pure_sets: list[dict[str, object]] = []
    memory_pure_sets: list[dict[str, object]] = []
    for size in range(1, max_size + 1):
        for features in itertools.combinations(FEATURE_NAMES, size):
            result = evaluate_features(records, features)
            if result["is_pure"]:
                pure_sets.append(result)
            if int(result["memory_covered_by_pure_keys"]) == int(result["memory_record_count"]):
                memory_pure_sets.append(result)

    def sort_key(result: dict[str, object]) -> tuple[int, int, int, str]:
        return (
            len(result["features"]),
            int(result["bucket_count"]),
            int(result["mixed_bucket_count"]),
            ",".join(str(part) for part in result["features"]),
        )

    pure_sets.sort(key=sort_key)
    memory_pure_sets.sort(key=sort_key)
    return {
        "pure_feature_sets": pure_sets[:top_n],
        "memory_pure_feature_sets": memory_pure_sets[:top_n],
        "pure_feature_set_count": len(pure_sets),
        "memory_pure_feature_set_count": len(memory_pure_sets),
    }


def mine_from_feature_names(
    records: list[dict[str, object]],
    feature_names: tuple[str, ...],
    max_size: int,
    top_n: int,
) -> dict[str, object]:
    pure_sets: list[dict[str, object]] = []
    memory_pure_sets: list[dict[str, object]] = []
    for size in range(1, max_size + 1):
        for features in itertools.combinations(feature_names, size):
            result = evaluate_features(records, features)
            if result["is_pure"]:
                pure_sets.append(result)
            if int(result["memory_covered_by_pure_keys"]) == int(result["memory_record_count"]):
                memory_pure_sets.append(result)

    def sort_key(result: dict[str, object]) -> tuple[int, int, int, str]:
        return (
            len(result["features"]),
            int(result["bucket_count"]),
            int(result["mixed_bucket_count"]),
            ",".join(str(part) for part in result["features"]),
        )

    pure_sets.sort(key=sort_key)
    memory_pure_sets.sort(key=sort_key)
    return {
        "pure_feature_sets": pure_sets[:top_n],
        "memory_pure_feature_sets": memory_pure_sets[:top_n],
        "pure_feature_set_count": len(pure_sets),
        "memory_pure_feature_set_count": len(memory_pure_sets),
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    getcontext().prec = args.precision
    theta = Decimal(2).ln() / Decimal(3).ln()

    parent_depth = args.parent_depth
    child_depth = parent_depth + 1
    max_depth = max(args.max_depth, child_depth)

    parent_frontier, parent_stats = enumerate_frontier(parent_depth, powers_of_three(max_depth))
    child_frontier, child_stats = enumerate_frontier(child_depth, powers_of_three(max_depth))
    parent_leaves = {leaf.residue: leaf for leaf in parent_frontier if leaf.residue > 1}
    child_leaves = {leaf.residue: leaf for leaf in child_frontier if leaf.residue > 1}
    parent_rows = {residue: analyze_prefix_start(residue, args.max_steps) for residue in sorted(parent_leaves)}

    step_size = 1 << parent_depth
    records: list[dict[str, object]] = []
    source_misses: list[dict[str, object]] = []

    for parent in sorted(parent_leaves):
        parent_row = parent_rows[parent]
        parent_required = int(parent_row["max_prefix_required"])
        for child_bit in (0, 1):
            child = parent + child_bit * step_size
            child_leaf = child_leaves.get(child)
            if child_leaf is None:
                continue
            child_row = analyze_prefix_start(child, args.max_steps)
            transition = transition_row(
                parent=parent,
                child=child,
                child_bit=child_bit,
                parent_row=parent_row,
                child_row=child_row,
                child_leaf=child_leaf,
            )
            if not (
                int(transition["required_delta"]) > 0
                and int(transition["credit_delta"]) < int(transition["required_delta"])
            ):
                continue

            trace = detailed_trace(child, args.max_steps, theta)
            observations = list(trace["observations"])
            pressure_events = [
                dict(event)
                for event in trace["pressure_events"]
                if int(dict(event)["required"]) > parent_required
            ]

            for event_index, event in enumerate(pressure_events, start=1):
                if unit_regime(event) != "high_after_ladder_window":
                    continue
                last = event.get("last_credit_event")
                if last is None or str(dict(last)["kind"]) != "high_ladder":
                    continue

                last_event = dict(last)
                align = int(last_event["align"])
                last_credit_state = int(last_event["state"])
                reconstructed = reconstruct_tail(last_credit_state, align)
                terminal = int(reconstructed["ladder_terminal"])
                if terminal % 16 != 6:
                    continue

                terminal_step = int(last_event["step"]) + align
                terminal_observation = observation_by_step_state(observations, terminal_step, terminal)
                if terminal_observation is None:
                    source_misses.append({"parent": parent, "child": child, "reason": "missing terminal"})
                    continue

                terminal_max = Decimal(terminal_observation["max_excess"])
                source = max_source_before(observations, terminal_step=terminal_step, terminal_max=terminal_max)
                if source is None:
                    source_misses.append({"parent": parent, "child": child, "reason": "missing source"})
                    continue

                source_state = int(source["state"])
                source_lag = terminal_step - int(source["step"])
                threshold = required_lower_edge(int(event["required"]))
                terminal_current_gap = threshold - Decimal(terminal_observation["current_excess"])
                gap = threshold - terminal_max
                current_form_constant = threshold - Decimal(terminal_observation["odd_steps"])
                label = label_name(source_lag)

                records.append(
                    {
                        "label": label,
                        "parent": parent,
                        "child": child,
                        "child_mod64": child % 64,
                        "child_mod128": child % 128,
                        "child_mod256": child % 256,
                        "child_mod512": child % 512,
                        "child_mod1024": child % 1024,
                        "child_mod2048": child % 2048,
                        "child_mod4096": child % 4096,
                        "child_mod8192": child % 8192,
                        "child_mod16384": child % 16384,
                        "child_mod65536": child % 65536,
                        "event_index": event_index,
                        "terminal_step": terminal_step,
                        "event_step": int(event["step"]),
                        "last_credit_step": int(last_event["step"]),
                        "align": align,
                        "q_mod16": int(reconstructed["q_mod_64"]) % 16,
                        "q_mod32": int(reconstructed["q_mod_64"]) % 32,
                        "q_mod64": int(reconstructed["q_mod_64"]),
                        "terminal_mod16": terminal % 16,
                        "terminal_mod32": terminal % 32,
                        "terminal_mod64": terminal % 64,
                        "event_required": int(event["required"]),
                        "terminal_required": int(terminal_observation["required"]),
                        "parent_required": parent_required,
                        "required_above_parent": int(event["required"]) - parent_required,
                        "transition_credit_delta": int(transition["credit_delta"]),
                        "terminal_current_gap": dec_string(terminal_current_gap, 24),
                        "terminal_current_form": f"step={terminal_step};constant={dec_string(current_form_constant, 12)}",
                        "terminal_step_mod8": terminal_step % 8,
                        "event_step_mod8": int(event["step"]) % 8,
                        "gap": dec_string(gap, 24),
                        "source_lag": source_lag,
                        "source_word": source_word(source_state, source_lag),
                        "source_mod8192": source_state % 8192,
                        "source_mod16384": source_state % 16384,
                    }
                )

    label_counts = Counter(str(record["label"]) for record in records)
    word_counts = Counter(str(record["source_word"]) for record in records if record["source_word"] is not None)
    source_mod_counts = Counter(
        f"{record['source_word']}:{record['source_mod16384']}"
        for record in records
        if record["source_word"] is not None
    )
    mined = mine_feature_sets(records, args.max_feature_set_size, args.top_n)
    terminal_event_mined = mine_from_feature_names(
        records, TERMINAL_EVENT_FEATURE_NAMES, args.max_feature_set_size, args.top_n
    )
    direct_eval = {
        "terminal_step_event_step_terminal_current_gap": evaluate_features(
            records, ("terminal_step", "event_step", "terminal_current_gap")
        ),
        "terminal_step_event_step_align_q_terminal_gap": evaluate_features(
            records, ("terminal_step", "event_step", "align", "q_mod64", "terminal_mod64", "terminal_current_gap")
        ),
        "terminal_current_form_align_q_terminal": evaluate_features(
            records, ("terminal_current_form", "align", "q_mod64", "terminal_mod64")
        ),
        "child_mod1024": evaluate_features(records, ("child_mod1024",)),
        "child_mod2048": evaluate_features(records, ("child_mod2048",)),
        "child_mod4096": evaluate_features(records, ("child_mod4096",)),
        "child_mod8192": evaluate_features(records, ("child_mod8192",)),
    }
    for child_feature in (
        "child_mod64",
        "child_mod128",
        "child_mod256",
        "child_mod512",
        "child_mod1024",
        "child_mod2048",
        "child_mod4096",
    ):
        for timing_feature in ("event_step", "terminal_step", "terminal_current_gap", "terminal_current_form"):
            direct_eval[f"{child_feature}_{timing_feature}"] = evaluate_features(
                records, (child_feature, timing_feature)
            )

    pure_claims = {
        "all_sources_found": not source_misses,
        "population_is_340": len(records) == 340,
        "labels_are_terminal_local_or_memory_lag_8": set(label_counts) <= {"terminal_local", "memory_lag_8"},
        "six_memory_records": label_counts.get("memory_lag_8", 0) == 6,
        "memory_sources_are_two_known_words": set(word_counts) == {"EEOOEOOO", "EEOEOOOO"},
        "has_pure_feature_set": bool(mined["pure_feature_sets"]),
        "has_memory_pure_feature_set": bool(mined["memory_pure_feature_sets"]),
        "no_terminal_event_feature_set_of_searched_size_is_pure": not bool(terminal_event_mined["pure_feature_sets"]),
        "no_terminal_event_feature_set_of_searched_size_is_memory_pure": not bool(
            terminal_event_mined["memory_pure_feature_sets"]
        ),
    }

    result = {
        "status": "branch-prefix-tail-dichotomy-classifier",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in vars(args).items()
        },
        "frontiers": {
            "parent": {
                **parent_stats,
                "positive_live_count": len(parent_leaves),
                "depth": parent_depth,
            },
            "child": {
                **child_stats,
                "positive_live_count": len(child_leaves),
                "depth": child_depth,
            },
        },
        "record_count": len(records),
        "label_counts": dict_counter(label_counts),
        "memory_source_word_counts": dict_counter(word_counts),
        "memory_source_mod16384_counts": dict_counter(source_mod_counts),
        "pure_claims": pure_claims,
        "mined_classifiers": mined,
        "terminal_event_only_mined_classifiers": terminal_event_mined,
        "direct_feature_evaluations": direct_eval,
        "memory_examples": [record for record in records if record["label"] != "terminal_local"][: args.top_n],
        "source_misses": source_misses[: args.top_n],
        "interpretation": (
            "Finite feature mining for the terminal-local vs lag-8 memory-tail "
            "dichotomy. Pure feature sets are theorem targets, not proofs."
        ),
    }
    if getattr(args, "include_records", False):
        result["records"] = records
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parent-depth", type=int, default=25)
    parser.add_argument("--max-depth", type=int, default=1024)
    parser.add_argument("--max-steps", type=int, default=50000)
    parser.add_argument("--precision", type=int, default=80)
    parser.add_argument("--top-n", type=int, default=12)
    parser.add_argument("--max-feature-set-size", type=int, default=3)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--include-records", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if args.parent_depth < 1:
        raise SystemExit("--parent-depth must be positive")
    if args.max_depth < args.parent_depth + 1:
        raise SystemExit("--max-depth must be at least --parent-depth + 1")
    if args.max_steps < 1:
        raise SystemExit("--max-steps must be positive")
    if args.precision < 40:
        raise SystemExit("--precision must be at least 40")
    if args.top_n < 1:
        raise SystemExit("--top-n must be positive")
    if args.max_feature_set_size < 1:
        raise SystemExit("--max-feature-set-size must be positive")

    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    if not args.quiet:
        print(text)


if __name__ == "__main__":
    main()
