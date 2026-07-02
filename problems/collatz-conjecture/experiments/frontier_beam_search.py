#!/usr/bin/env python3
"""Beam-search hard finite shadows inside the certificate frontier.

`frontier_escape_analyzer.py` is exact at a fixed base depth.  This script is
deliberately different: it starts from an exact seed frontier, keeps the
hardest finite representatives by certificate depth, then extends only those
frontier leaves by additional high bits.

The result is a searchlight for possible hard families.  It is not exhaustive
after the seed depth unless the frontier itself is smaller than the beam.
"""

from __future__ import annotations

import argparse
import heapq
import json
from dataclasses import dataclass
from time import perf_counter

from certificate_depth_scan import total_stopping_profile
from collatz_residue_lab import bits, shortcut
from frontier_escape_analyzer import (
    FrontierLeaf,
    enumerate_frontier,
    finite_escape_certificate,
    powers_of_three,
)


@dataclass(frozen=True)
class ScoredLeaf:
    leaf: FrontierLeaf
    certificate_depth: int
    certificate_image: int | None
    certificate_odd_count: int | None
    extra_depth_after_base: int | None
    first_below_start_depth: int | None
    first_multiplier_contract_depth: int | None
    certified: bool

    def score_key(self) -> tuple[int, int, int]:
        depth_score = self.certificate_depth if self.certified else 10**18
        return depth_score, self.leaf.residue, self.leaf.odd_count

    def as_dict(self, include_profile: bool, step_limit: int) -> dict[str, int | str | bool | None]:
        row: dict[str, int | str | bool | None] = {
            "depth": self.leaf.depth,
            "residue": self.leaf.residue,
            "bits": bits(self.leaf.residue, self.leaf.depth),
            "bit_length": self.leaf.residue.bit_length(),
            "leading_zero_padding": leading_zero_padding(self.leaf),
            "input_ones": self.leaf.residue.bit_count(),
            "trailing_ones": trailing_ones(self.leaf.residue),
            "frontier_odd_count": self.leaf.odd_count,
            "frontier_image": self.leaf.image,
            "certified": self.certified,
            "certificate_depth": self.certificate_depth if self.certified else None,
            "certificate_image": self.certificate_image,
            "certificate_odd_count": self.certificate_odd_count,
            "extra_depth_after_base": self.extra_depth_after_base,
            "first_below_start_depth": self.first_below_start_depth,
            "first_multiplier_contract_depth": self.first_multiplier_contract_depth,
        }
        if include_profile and self.leaf.residue > 0:
            row.update(total_stopping_profile(self.leaf.residue, step_limit))
        return row


def trailing_ones(n: int) -> int:
    count = 0
    while n & 1:
        count += 1
        n >>= 1
    return count


def leading_zero_padding(leaf: FrontierLeaf) -> int:
    return leaf.depth - max(leaf.residue.bit_length(), 1)


def expand_surviving_children(leaf: FrontierLeaf, pow3: list[int]) -> list[FrontierLeaf]:
    depth = leaf.depth
    next_depth = depth + 1
    next_bit = 1 << depth
    children: list[FrontierLeaf] = []

    for high_bit in (0, 1):
        residue = leaf.residue + (next_bit if high_bit else 0)
        image_before_next_step = leaf.image + (pow3[leaf.odd_count] if high_bit else 0)
        odd_count = leaf.odd_count + (image_before_next_step & 1)
        image = shortcut(image_before_next_step)
        if pow3[odd_count] >= (1 << next_depth):
            children.append(FrontierLeaf(next_depth, residue, odd_count, image))

    return children


def score_leaf(leaf: FrontierLeaf, max_escape_depth: int, pow3: list[int]) -> ScoredLeaf:
    cert = finite_escape_certificate(leaf, max_escape_depth, pow3)
    certified = bool(cert["certified"])
    certificate_depth = int(cert["certificate_depth"]) if certified else max_escape_depth + 1
    return ScoredLeaf(
        leaf=leaf,
        certificate_depth=certificate_depth,
        certificate_image=int(cert["certificate_image"]) if cert["certificate_image"] is not None else None,
        certificate_odd_count=(
            int(cert["certificate_odd_count"]) if cert["certificate_odd_count"] is not None else None
        ),
        extra_depth_after_base=(
            int(cert["extra_depth_after_base"]) if cert["extra_depth_after_base"] is not None else None
        ),
        first_below_start_depth=(
            int(cert["first_below_start_depth"]) if cert["first_below_start_depth"] is not None else None
        ),
        first_multiplier_contract_depth=(
            int(cert["first_multiplier_contract_depth"])
            if cert["first_multiplier_contract_depth"] is not None
            else None
        ),
        certified=certified,
    )


def keep_hardest(scored: list[ScoredLeaf], beam_width: int) -> list[ScoredLeaf]:
    if len(scored) <= beam_width:
        return sorted(scored, key=lambda item: item.score_key(), reverse=True)
    return heapq.nlargest(beam_width, scored, key=lambda item: item.score_key())


def analyze(
    seed_depth: int,
    target_depth: int,
    max_escape_depth: int,
    beam_width: int,
    top_n: int,
    step_limit: int,
    max_leading_zero_padding: int | None,
) -> dict[str, object]:
    started = perf_counter()
    pow3 = powers_of_three(max_escape_depth)
    frontier, frontier_stats = enumerate_frontier(seed_depth, pow3)

    frontier_for_seed = filter_by_padding(frontier, max_leading_zero_padding)
    seed_scored = [score_leaf(leaf, max_escape_depth, pow3) for leaf in frontier_for_seed]
    beam = keep_hardest(seed_scored, beam_width)
    generations: list[dict[str, int | float | str | bool | None]] = []

    generations.append(generation_summary(seed_depth, len(frontier), beam, 0.0, exact=len(frontier) <= beam_width))

    for depth in range(seed_depth + 1, target_depth + 1):
        generation_started = perf_counter()
        children: list[FrontierLeaf] = []
        for scored_leaf in beam:
            children.extend(expand_surviving_children(scored_leaf.leaf, pow3))
        children = filter_by_padding(children, max_leading_zero_padding)

        scored_children = [score_leaf(child, max_escape_depth, pow3) for child in children]
        beam = keep_hardest(scored_children, beam_width)
        generations.append(
            generation_summary(
                depth=depth,
                candidate_count=len(children),
                beam=beam,
                elapsed_seconds=perf_counter() - generation_started,
                exact=False,
            )
        )

    top_records = sorted(beam, key=lambda item: item.score_key(), reverse=True)[:top_n]
    elapsed = perf_counter() - started

    return {
        "status": "beam-search",
        "elapsed_seconds": round(elapsed, 6),
        "seed": {
            **frontier_stats,
            "seed_depth": seed_depth,
            "seed_frontier_count": len(frontier),
            "seed_exact_until_frontier_count_le_beam": len(frontier) <= beam_width,
        },
        "search": {
            "target_depth": target_depth,
            "max_escape_depth": max_escape_depth,
            "beam_width": beam_width,
            "top_n": top_n,
            "max_leading_zero_padding": max_leading_zero_padding,
            "exhaustive_after_seed": len(frontier) <= beam_width,
        },
        "generations": generations,
        "top_records": [record.as_dict(include_profile=True, step_limit=step_limit) for record in top_records],
        "interpretation": (
            "This is a heuristic hard-family search after the exact seed frontier. "
            "It follows leaves with largest current finite-representative certificate depth; "
            "a missed branch can later become hard, so these records are candidates, not bounds."
        ),
    }


def filter_by_padding(frontier: list[FrontierLeaf], max_leading_zero_padding: int | None) -> list[FrontierLeaf]:
    if max_leading_zero_padding is None:
        return frontier
    return [leaf for leaf in frontier if leading_zero_padding(leaf) <= max_leading_zero_padding]


def generation_summary(
    depth: int,
    candidate_count: int,
    beam: list[ScoredLeaf],
    elapsed_seconds: float,
    exact: bool,
) -> dict[str, int | float | str | bool | None]:
    if not beam:
        return {
            "depth": depth,
            "candidate_count": candidate_count,
            "kept_count": 0,
            "exact": exact,
            "elapsed_seconds": round(elapsed_seconds, 6),
            "max_certificate_depth": None,
            "max_residue": None,
            "max_bits": None,
        }

    hardest = max(beam, key=lambda item: item.score_key())
    return {
        "depth": depth,
        "candidate_count": candidate_count,
        "kept_count": len(beam),
        "exact": exact,
        "elapsed_seconds": round(elapsed_seconds, 6),
        "max_certificate_depth": hardest.certificate_depth if hardest.certified else None,
        "max_residue": hardest.leaf.residue,
        "max_bits": bits(hardest.leaf.residue, hardest.leaf.depth),
        "max_bit_length": hardest.leaf.residue.bit_length(),
        "max_leading_zero_padding": leading_zero_padding(hardest.leaf),
        "max_frontier_odd_count": hardest.leaf.odd_count,
        "max_extra_depth_after_base": hardest.extra_depth_after_base,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed-depth", type=int, default=20, help="exact frontier depth used to seed the beam")
    parser.add_argument("--target-depth", type=int, default=40, help="last frontier depth to beam-search")
    parser.add_argument("--max-escape-depth", type=int, default=1536, help="maximum certificate depth to search")
    parser.add_argument("--beam-width", type=int, default=512, help="number of hard leaves kept per generation")
    parser.add_argument("--top-n", type=int, default=12, help="number of final beam records to report")
    parser.add_argument("--step-limit", type=int, default=100000, help="step cap for profile metadata on top records")
    parser.add_argument(
        "--max-leading-zero-padding",
        type=int,
        help="discard frontier states with more than this many leading zero bits above the finite representative",
    )
    args = parser.parse_args()

    if args.seed_depth < 1:
        raise SystemExit("--seed-depth must be at least 1")
    if args.target_depth < args.seed_depth:
        raise SystemExit("--target-depth must be at least --seed-depth")
    if args.max_escape_depth <= args.target_depth:
        raise SystemExit("--max-escape-depth must be greater than --target-depth")
    if args.beam_width < 1:
        raise SystemExit("--beam-width must be at least 1")
    if args.top_n < 1:
        raise SystemExit("--top-n must be at least 1")
    if args.max_leading_zero_padding is not None and args.max_leading_zero_padding < 0:
        raise SystemExit("--max-leading-zero-padding must be nonnegative when provided")

    payload = analyze(
        seed_depth=args.seed_depth,
        target_depth=args.target_depth,
        max_escape_depth=args.max_escape_depth,
        beam_width=args.beam_width,
        top_n=args.top_n,
        step_limit=args.step_limit,
        max_leading_zero_padding=args.max_leading_zero_padding,
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
