#!/usr/bin/env python3
"""Analyze recursive descent transitions of rare repayment-motif outliers.

The motif-cover analyzer compresses most finite repayment motifs into two
large classes, while a small set of low-slope, slow-long, high-debt, and
slow-critical outliers carries the hard behavior.

This script asks the next structural question:

    After a rare outlier obtains its first usable descent certificate and maps
    to a smaller positive integer, what motif class does that smaller integer
    have?

The output is finite evidence only.  A proof would need to replace these
observed transitions with a uniform theorem saying that outlier classes cannot
nest forever inside positive finite shadows.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from dataclasses import dataclass
from time import perf_counter
from typing import Iterable

from collatz_residue_lab import shortcut
from motif_cover_analyzer import (
    DEFAULT_HARD_STARTS,
    RepaymentMotif,
    classify_motif,
    frontier_values,
    powers_of_three,
    repayment_motif_for_start,
    unique_preserving_order,
)
from repayment_envelope_scan import parse_ints, round_float


DEFAULT_TERMINAL_CLASSES = ("short-high-deficit", "mixed", "trivial-halving")


@dataclass(frozen=True)
class TransitionStep:
    generation: int
    start: int
    start_bit_length: int
    motif: RepaymentMotif
    motif_class: str
    next_start: int
    next_bit_length: int
    descent_bits: float

    def as_dict(self) -> dict[str, int | float | str]:
        row = self.motif.as_dict()
        row.update(
            {
                "generation": self.generation,
                "class": self.motif_class,
                "next_start": self.next_start,
                "next_bit_length": self.next_bit_length,
                "descent_bits": round_float(self.descent_bits),
            }
        )
        return row


@dataclass(frozen=True)
class TransitionChain:
    initial_start: int
    initial_class: str | None
    steps: tuple[TransitionStep, ...]
    status: str

    @property
    def terminal_generation(self) -> int | None:
        if self.status != "terminal-class-hit":
            return None
        return self.steps[-1].generation if self.steps else None

    @property
    def final_start(self) -> int:
        if not self.steps:
            return self.initial_start
        return self.steps[-1].next_start

    @property
    def max_certificate_depth(self) -> int:
        return max((step.motif.certificate_depth for step in self.steps), default=0)

    @property
    def total_descent_bits(self) -> float:
        if not self.steps:
            return 0.0
        return math.log2(self.initial_start) - math.log2(max(1, self.final_start))

    def as_dict(self) -> dict[str, object]:
        return {
            "initial_start": self.initial_start,
            "initial_class": self.initial_class,
            "status": self.status,
            "terminal_generation": self.terminal_generation,
            "final_start": self.final_start,
            "final_bit_length": self.final_start.bit_length(),
            "step_count": len(self.steps),
            "max_certificate_depth": self.max_certificate_depth,
            "total_descent_bits": round_float(self.total_descent_bits),
            "steps": [step.as_dict() for step in self.steps],
        }


def iterate_shortcut(start: int, depth: int) -> int:
    x = start
    for _ in range(depth):
        x = shortcut(x)
    return x


def parse_classes(raw: str | None) -> tuple[str, ...]:
    if not raw:
        return DEFAULT_TERMINAL_CLASSES
    classes = tuple(part.strip() for part in raw.split(",") if part.strip())
    if not classes:
        raise SystemExit("--terminal-classes must name at least one class")
    return classes


def transition_class(motif: RepaymentMotif) -> str:
    if motif.length == 0 and motif.certificate_depth == 1 and motif.certificate_odd_count == 0:
        return "trivial-halving"
    return classify_motif(motif)


def selected_starts(
    explicit_starts: Iterable[int],
    limit: int,
    frontier_base_depth: int,
    max_depth: int,
    max_frontier: int | None,
    sample_stride: int,
    sample_offset: int,
) -> tuple[list[int], dict[str, object] | None]:
    frontier_meta = None
    frontier_starts: list[int] = []
    if frontier_base_depth:
        frontier_starts, frontier_meta = frontier_values(
            base_depth=frontier_base_depth,
            max_depth=max_depth,
            max_frontier=max_frontier,
            sample_stride=sample_stride,
            sample_offset=sample_offset,
        )
    return unique_preserving_order([*explicit_starts, *range(1, limit + 1), *frontier_starts]), frontier_meta


def build_chain(
    start: int,
    max_depth: int,
    pow3: list[int],
    max_generations: int,
    terminal_classes: set[str],
) -> TransitionChain:
    current = start
    steps: list[TransitionStep] = []
    initial_class: str | None = None

    for generation in range(max_generations + 1):
        motif = repayment_motif_for_start(current, max_depth, pow3)
        if motif is None:
            return TransitionChain(start, initial_class, tuple(steps), "uncertified")
        motif_class = transition_class(motif)
        if initial_class is None:
            initial_class = motif_class
        next_start = iterate_shortcut(current, motif.certificate_depth)
        descent_bits = math.log2(current) - math.log2(max(1, next_start))
        steps.append(
            TransitionStep(
                generation=generation,
                start=current,
                start_bit_length=current.bit_length(),
                motif=motif,
                motif_class=motif_class,
                next_start=next_start,
                next_bit_length=next_start.bit_length(),
                descent_bits=descent_bits,
            )
        )
        if motif_class in terminal_classes and generation > 0:
            return TransitionChain(start, initial_class, tuple(steps), "terminal-class-hit")
        if next_start <= 1:
            return TransitionChain(start, initial_class, tuple(steps), "reached-one")
        if next_start >= current:
            return TransitionChain(start, initial_class, tuple(steps), "non-descending-certificate")
        current = next_start

    return TransitionChain(start, initial_class, tuple(steps), "max-generations")


def transition_pairs(chain: TransitionChain) -> list[str]:
    return [
        f"{chain.steps[index].motif_class}->{chain.steps[index + 1].motif_class}"
        for index in range(len(chain.steps) - 1)
    ]


def summarize(chains: list[TransitionChain], terminal_classes: tuple[str, ...], top_n: int) -> dict[str, object]:
    status_counts = Counter(chain.status for chain in chains)
    initial_classes = Counter(chain.initial_class or "uncertified" for chain in chains)
    final_step_classes = Counter(chain.steps[-1].motif_class for chain in chains if chain.steps)
    pairs = Counter(pair for chain in chains for pair in transition_pairs(chain))
    terminal_generations = Counter(
        str(chain.terminal_generation)
        for chain in chains
        if chain.terminal_generation is not None
    )
    step_class_histogram = Counter(step.motif_class for chain in chains for step in chain.steps)
    max_step_count = max((len(chain.steps) for chain in chains), default=0)
    terminal_chain_count = status_counts.get("terminal-class-hit", 0) + status_counts.get("reached-one", 0)

    hardest = sorted(
        chains,
        key=lambda chain: (
            chain.status != "terminal-class-hit",
            chain.terminal_generation if chain.terminal_generation is not None else 10**9,
            chain.max_certificate_depth,
            chain.initial_start,
        ),
        reverse=True,
    )[:top_n]
    deepest = sorted(chains, key=lambda chain: (chain.max_certificate_depth, chain.initial_start), reverse=True)[:top_n]
    least_descent = sorted(
        chains,
        key=lambda chain: (
            chain.total_descent_bits if chain.total_descent_bits > 0 else float("inf"),
            -chain.initial_start,
        ),
    )[:top_n]

    return {
        "chain_count": len(chains),
        "terminal_classes": list(terminal_classes),
        "status_counts": dict(sorted(status_counts.items())),
        "terminal_or_reached_one_count": terminal_chain_count,
        "terminal_or_reached_one_fraction": round_float(
            terminal_chain_count / len(chains) if chains else 0.0
        ),
        "max_step_count": max_step_count,
        "initial_class_histogram": dict(sorted(initial_classes.items())),
        "final_step_class_histogram": dict(sorted(final_step_classes.items())),
        "step_class_histogram": dict(sorted(step_class_histogram.items())),
        "terminal_generation_histogram": dict(sorted(terminal_generations.items())),
        "transition_pair_histogram": [
            {"transition": transition, "count": count}
            for transition, count in pairs.most_common(top_n)
        ],
        "hardest_chains": [chain.as_dict() for chain in hardest],
        "deepest_certificate_chains": [chain.as_dict() for chain in deepest],
        "least_total_descent_chains": [chain.as_dict() for chain in least_descent],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--starts", nargs="+", help="explicit starts; accepts comma-separated values")
    parser.add_argument("--limit", type=int, default=0, help="also scan starts 1..limit")
    parser.add_argument("--frontier-base-depth", type=int, default=0, help="also scan exact survivor frontier")
    parser.add_argument("--max-depth", type=int, default=1200, help="certificate/debt search depth")
    parser.add_argument("--max-generations", type=int, default=4, help="recursive descent generations")
    parser.add_argument("--terminal-classes", help="comma-separated classes that terminate a chain")
    parser.add_argument("--include-terminal-initial", action="store_true", help="keep starts already in terminal classes")
    parser.add_argument("--max-frontier", type=int, help="frontier mode: analyze at most this many leaves")
    parser.add_argument("--sample-stride", type=int, default=1, help="frontier mode: analyze every kth leaf")
    parser.add_argument("--sample-offset", type=int, default=0, help="frontier mode offset")
    parser.add_argument("--top-n", type=int, default=12, help="top rows per table")
    parser.add_argument("--summary", action="store_true", help="omit per-chain rows")
    args = parser.parse_args()

    if args.max_depth < 1:
        raise SystemExit("--max-depth must be at least 1")
    if args.max_generations < 0:
        raise SystemExit("--max-generations must be nonnegative")
    if args.limit < 0:
        raise SystemExit("--limit must be nonnegative")
    if args.sample_stride < 1:
        raise SystemExit("--sample-stride must be at least 1")
    if not 0 <= args.sample_offset < args.sample_stride:
        raise SystemExit("--sample-offset must satisfy 0 <= offset < stride")
    if args.top_n < 1:
        raise SystemExit("--top-n must be positive")

    started = perf_counter()
    explicit_starts = parse_ints(args.starts)
    if not explicit_starts and args.limit == 0 and args.frontier_base_depth == 0:
        explicit_starts = DEFAULT_HARD_STARTS
    if any(start < 1 for start in explicit_starts):
        raise SystemExit("--starts must contain positive integers")

    terminal_classes = parse_classes(args.terminal_classes)
    terminal_set = set(terminal_classes)
    starts, frontier_meta = selected_starts(
        explicit_starts=explicit_starts,
        limit=args.limit,
        frontier_base_depth=args.frontier_base_depth,
        max_depth=args.max_depth,
        max_frontier=args.max_frontier,
        sample_stride=args.sample_stride,
        sample_offset=args.sample_offset,
    )
    pow3 = powers_of_three(args.max_depth)

    chains: list[TransitionChain] = []
    skipped_terminal_initial = 0
    uncertified_initial = 0
    for start in starts:
        initial_motif = repayment_motif_for_start(start, args.max_depth, pow3)
        if initial_motif is None:
            uncertified_initial += 1
            continue
        initial_class = transition_class(initial_motif)
        if initial_class in terminal_set and not args.include_terminal_initial:
            skipped_terminal_initial += 1
            continue
        chains.append(
            build_chain(
                start=start,
                max_depth=args.max_depth,
                pow3=pow3,
                max_generations=args.max_generations,
                terminal_classes=terminal_set,
            )
        )

    payload: dict[str, object] = {
        "status": "outlier-transition-analysis",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            "starts": explicit_starts,
            "limit": args.limit,
            "frontier_base_depth": args.frontier_base_depth or None,
            "max_depth": args.max_depth,
            "max_generations": args.max_generations,
            "terminal_classes": list(terminal_classes),
            "include_terminal_initial": args.include_terminal_initial,
        },
        "frontier": frontier_meta,
        "selection": {
            "candidate_starts": len(starts),
            "chains_analyzed": len(chains),
            "skipped_terminal_initial": skipped_terminal_initial,
            "uncertified_initial": uncertified_initial,
        },
        "summary": summarize(chains, terminal_classes, args.top_n),
        "interpretation": (
            "Observed outlier transitions are finite evidence. A proof would need "
            "a uniform descent-transition theorem showing rare classes cannot "
            "reproduce indefinitely among positive finite shadows."
        ),
    }
    if not args.summary:
        payload["chains"] = [chain.as_dict() for chain in chains[: args.top_n]]

    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
