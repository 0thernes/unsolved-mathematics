#!/usr/bin/env python3
"""Analyze finite positive representatives of certificate-frontier residues.

The residue-certificate miner shows that a full finite cover of the 2-adic
space cannot terminate: high-odd frontier prefixes persist forever, with the
all-odd path limiting to the 2-adic point -1.

This instrument asks the positive-integer version of that obstruction.  Fix a
base depth d, enumerate every residue prefix that survives the multiplier test
through d, then use the finite representative r < 2^d as a positive integer and
measure when it escapes into a usable descent certificate.

This is evidence about the boundary, not a proof of Collatz.
"""

from __future__ import annotations

import argparse
import heapq
import json
from collections import Counter
from dataclasses import dataclass
from time import perf_counter

from certificate_depth_scan import total_stopping_profile
from collatz_residue_lab import affine_for_low_bits, bits, shortcut


@dataclass(frozen=True)
class FrontierLeaf:
    depth: int
    residue: int
    odd_count: int
    image: int

    def as_dict(self) -> dict[str, int | str]:
        return {
            "depth": self.depth,
            "residue": self.residue,
            "bits": bits(self.residue, self.depth),
            "odd_count": self.odd_count,
            "image": self.image,
        }


def powers_of_three(max_depth: int) -> list[int]:
    pow3 = [1]
    for _ in range(max_depth):
        pow3.append(pow3[-1] * 3)
    return pow3


def enumerate_frontier(base_depth: int, pow3: list[int]) -> tuple[list[FrontierLeaf], dict[str, object]]:
    """Return frontier leaves at base_depth, pruning certified cylinders early."""
    started = perf_counter()
    live = [FrontierLeaf(depth=0, residue=0, odd_count=0, image=0)]
    certified_leaf_count = 0
    certified_units = 0

    for depth in range(base_depth):
        next_depth = depth + 1
        next_bit = 1 << depth
        next_live: list[FrontierLeaf] = []

        for leaf in live:
            for high_bit in (0, 1):
                residue = leaf.residue + (next_bit if high_bit else 0)
                image_before_next_step = leaf.image + (pow3[leaf.odd_count] if high_bit else 0)
                is_odd_step = image_before_next_step & 1
                odd_count = leaf.odd_count + is_odd_step
                image = shortcut(image_before_next_step)

                if pow3[odd_count] < (1 << next_depth):
                    certified_leaf_count += 1
                    certified_units += 1 << (base_depth - next_depth)
                else:
                    next_live.append(
                        FrontierLeaf(
                            depth=next_depth,
                            residue=residue,
                            odd_count=odd_count,
                            image=image,
                        )
                    )

        live = next_live

    frontier_units = len(live)
    scale = 1 << base_depth
    odd_histogram = Counter(leaf.odd_count for leaf in live)
    return live, {
        "base_depth": base_depth,
        "elapsed_seconds": round(perf_counter() - started, 6),
        "certified_leaf_count": certified_leaf_count,
        "certified_units_mod_2^base_depth": certified_units,
        "frontier_count": frontier_units,
        "frontier_fraction": frontier_units / scale,
        "certified_fraction": certified_units / scale,
        "frontier_odd_count_histogram": {str(k): odd_histogram[k] for k in sorted(odd_histogram)},
    }


def finite_escape_certificate(
    leaf: FrontierLeaf,
    max_escape_depth: int,
    pow3: list[int],
) -> dict[str, int | bool | None]:
    """Find the first usable certificate for the finite representative leaf.residue."""
    start = leaf.residue
    if start < 1:
        return {
            "certified": False,
            "start": start,
            "certificate_depth": None,
            "extra_depth_after_base": None,
            "certificate_odd_count": None,
            "certificate_image": None,
            "first_multiplier_contract_depth": None,
            "first_below_start_depth": None,
        }

    x = leaf.image
    odd_count = leaf.odd_count
    first_multiplier_contract_depth = None
    first_below_start_depth = None

    if pow3[odd_count] < (1 << leaf.depth):
        first_multiplier_contract_depth = leaf.depth
    if x < start:
        first_below_start_depth = leaf.depth

    for depth in range(leaf.depth + 1, max_escape_depth + 1):
        was_odd = x & 1
        x = shortcut(x)
        odd_count += was_odd

        if first_multiplier_contract_depth is None and pow3[odd_count] < (1 << depth):
            first_multiplier_contract_depth = depth
        if first_below_start_depth is None and x < start:
            first_below_start_depth = depth

        if pow3[odd_count] < (1 << depth) and x < start:
            return {
                "certified": True,
                "start": start,
                "certificate_depth": depth,
                "extra_depth_after_base": depth - leaf.depth,
                "certificate_odd_count": odd_count,
                "certificate_image": x,
                "first_multiplier_contract_depth": first_multiplier_contract_depth,
                "first_below_start_depth": first_below_start_depth,
            }

    return {
        "certified": False,
        "start": start,
        "certificate_depth": None,
        "extra_depth_after_base": None,
        "certificate_odd_count": None,
        "certificate_image": None,
        "first_multiplier_contract_depth": first_multiplier_contract_depth,
        "first_below_start_depth": first_below_start_depth,
    }


def select_frontier(
    frontier: list[FrontierLeaf],
    max_frontier: int | None,
    sample_stride: int,
    sample_offset: int,
) -> list[FrontierLeaf]:
    if max_frontier is None and sample_stride == 1 and sample_offset == 0:
        return frontier

    selected = sorted(frontier, key=lambda leaf: leaf.residue)
    if sample_stride > 1:
        selected = [leaf for index, leaf in enumerate(selected) if index % sample_stride == sample_offset]
    if max_frontier is not None:
        selected = selected[:max_frontier]
    return selected


def analyze(
    base_depth: int,
    max_escape_depth: int,
    top_n: int,
    max_frontier: int | None,
    sample_stride: int,
    sample_offset: int,
    step_limit: int,
    sample_limit: int,
) -> dict[str, object]:
    if max_escape_depth <= base_depth:
        raise ValueError("--max-escape-depth must be greater than --base-depth")

    pow3 = powers_of_three(max_escape_depth)
    started = perf_counter()
    frontier, frontier_stats = enumerate_frontier(base_depth, pow3)
    selected = select_frontier(frontier, max_frontier, sample_stride, sample_offset)

    depth_histogram: Counter[int] = Counter()
    extra_depth_histogram: Counter[int] = Counter()
    uncertified: list[dict[str, int | str]] = []
    top_records: list[dict[str, int | str | bool | None]] = []
    record_setters: list[dict[str, int | str | bool | None]] = []
    max_certificate_depth = -1
    max_extra_depth = -1

    for leaf in selected:
        cert = finite_escape_certificate(leaf, max_escape_depth, pow3)
        if not cert["certified"]:
            uncertified.append(leaf.as_dict())
            continue

        certificate_depth = int(cert["certificate_depth"])
        extra_depth = int(cert["extra_depth_after_base"])
        depth_histogram[certificate_depth] += 1
        extra_depth_histogram[extra_depth] += 1
        row: dict[str, int | str | bool | None] = {
            **leaf.as_dict(),
            **cert,
        }

        top_records.append(row)
        top_records = sorted(
            top_records,
            key=lambda item: (int(item["certificate_depth"]), int(item["start"])),
            reverse=True,
        )[:top_n]

        if certificate_depth > max_certificate_depth:
            max_certificate_depth = certificate_depth
            max_extra_depth = extra_depth
            record_setters.append(row)

    for row in top_records:
        profile = total_stopping_profile(int(row["start"]), step_limit)
        row.update(profile)

    exact_full_frontier = (
        max_frontier is None
        and sample_stride == 1
        and sample_offset == 0
        and len(selected) == len(frontier)
    )
    if uncertified:
        status = "uncertified-within-search-depth"
    elif exact_full_frontier:
        status = "full-frontier-certified-within-search-depth"
    else:
        status = "sample-certified-within-search-depth"

    return {
        "status": status,
        "base_depth": base_depth,
        "max_escape_depth": max_escape_depth,
        "elapsed_seconds": round(perf_counter() - started, 6),
        "frontier": {
            **frontier_stats,
            "sample_frontier_leaves": [
                leaf.as_dict() for leaf in heapq.nsmallest(sample_limit, frontier, key=lambda item: item.residue)
            ],
        },
        "selection": {
            "exact_full_frontier": exact_full_frontier,
            "sample_stride": sample_stride,
            "sample_offset": sample_offset,
            "max_frontier": max_frontier,
            "analyzed_count": len(selected),
            "frontier_count": len(frontier),
        },
        "analysis": {
            "certified_count": len(selected) - len(uncertified),
            "uncertified_count": len(uncertified),
            "uncertified_samples": uncertified[:sample_limit],
            "max_certificate_depth": max_certificate_depth,
            "max_extra_depth_after_base": max_extra_depth,
            "certificate_depth_histogram": {str(k): depth_histogram[k] for k in sorted(depth_histogram)},
            "extra_depth_after_base_histogram": {str(k): extra_depth_histogram[k] for k in sorted(extra_depth_histogram)},
            "top_escape_records": sorted(
                top_records,
                key=lambda row: (int(row["certificate_depth"]), int(row["start"])),
            ),
            "record_setters_by_certificate_depth": record_setters,
        },
        "interpretation": (
            "A full-frontier-certified status means every positive integer represented by the "
            "base-depth survivor residues escaped into a usable descent certificate within the "
            "search depth. This is a finite boundary experiment, not a global proof."
        ),
    }


def summarize_payload(payload: dict[str, object]) -> dict[str, object]:
    frontier = payload["frontier"]
    selection = payload["selection"]
    analysis_payload = payload["analysis"]
    assert isinstance(frontier, dict)
    assert isinstance(selection, dict)
    assert isinstance(analysis_payload, dict)

    record_setters = analysis_payload["record_setters_by_certificate_depth"]
    assert isinstance(record_setters, list)
    final_record = record_setters[-1] if record_setters else None

    return {
        "status": payload["status"],
        "base_depth": payload["base_depth"],
        "max_escape_depth": payload["max_escape_depth"],
        "elapsed_seconds": payload["elapsed_seconds"],
        "frontier_count": frontier["frontier_count"],
        "frontier_fraction": frontier["frontier_fraction"],
        "certified_fraction": frontier["certified_fraction"],
        "frontier_odd_count_histogram": frontier["frontier_odd_count_histogram"],
        "analyzed_count": selection["analyzed_count"],
        "exact_full_frontier": selection["exact_full_frontier"],
        "certified_count": analysis_payload["certified_count"],
        "uncertified_count": analysis_payload["uncertified_count"],
        "max_certificate_depth": analysis_payload["max_certificate_depth"],
        "max_extra_depth_after_base": analysis_payload["max_extra_depth_after_base"],
        "final_record_setter": final_record,
        "top_escape_records": analysis_payload["top_escape_records"],
    }


def self_test(max_depth: int) -> None:
    pow3 = powers_of_three(max_depth)
    live = [FrontierLeaf(depth=0, residue=0, odd_count=0, image=0)]
    for depth in range(max_depth):
        next_depth = depth + 1
        next_bit = 1 << depth
        next_live: list[FrontierLeaf] = []
        for leaf in live:
            for high_bit in (0, 1):
                residue = leaf.residue + (next_bit if high_bit else 0)
                image_before_next_step = leaf.image + (pow3[leaf.odd_count] if high_bit else 0)
                odd_count = leaf.odd_count + (image_before_next_step & 1)
                image = shortcut(image_before_next_step)
                expected_odd_count, expected_image = affine_for_low_bits(next_depth, residue)
                if odd_count != expected_odd_count or image != expected_image:
                    raise AssertionError(
                        "incremental frontier state mismatch: "
                        f"depth={next_depth}, residue={residue}, "
                        f"got=({odd_count}, {image}), expected=({expected_odd_count}, {expected_image})"
                    )
                if pow3[odd_count] >= (1 << next_depth):
                    next_live.append(FrontierLeaf(next_depth, residue, odd_count, image))
        live = next_live


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-depth", type=int, default=20, help="frontier depth to analyze")
    parser.add_argument("--max-escape-depth", type=int, default=512, help="maximum certificate depth to search")
    parser.add_argument("--top-n", type=int, default=12, help="number of worst escape records to keep")
    parser.add_argument("--max-frontier", type=int, help="analyze at most this many selected frontier leaves")
    parser.add_argument("--sample-stride", type=int, default=1, help="analyze every kth frontier leaf after sorting")
    parser.add_argument("--sample-offset", type=int, default=0, help="offset used with --sample-stride")
    parser.add_argument("--sample-limit", type=int, default=12, help="number of sample frontier/uncertified rows")
    parser.add_argument("--step-limit", type=int, default=50000, help="step cap for profile metadata on top records")
    parser.add_argument("--self-test", action="store_true", help="verify incremental affine updates before analysis")
    parser.add_argument("--summary", action="store_true", help="print a compact summary JSON payload")
    args = parser.parse_args()

    if args.base_depth < 1:
        raise SystemExit("--base-depth must be at least 1")
    if args.max_escape_depth <= args.base_depth:
        raise SystemExit("--max-escape-depth must be greater than --base-depth")
    if args.top_n < 1:
        raise SystemExit("--top-n must be at least 1")
    if args.sample_stride < 1:
        raise SystemExit("--sample-stride must be at least 1")
    if not 0 <= args.sample_offset < args.sample_stride:
        raise SystemExit("--sample-offset must satisfy 0 <= offset < stride")
    if args.max_frontier is not None and args.max_frontier < 1:
        raise SystemExit("--max-frontier must be at least 1 when provided")

    if args.self_test:
        self_test(min(args.base_depth, 12))

    payload = analyze(
        base_depth=args.base_depth,
        max_escape_depth=args.max_escape_depth,
        top_n=args.top_n,
        max_frontier=args.max_frontier,
        sample_stride=args.sample_stride,
        sample_offset=args.sample_offset,
        step_limit=args.step_limit,
        sample_limit=args.sample_limit,
    )
    if args.summary:
        payload = summarize_payload(payload)
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
