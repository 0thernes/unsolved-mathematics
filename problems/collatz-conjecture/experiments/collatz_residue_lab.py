#!/usr/bin/env python3
"""Finite residue descent certificates for the shortcut Collatz map.

The shortcut map is

    T(n) = n / 2          if n is even
         = (3n + 1) / 2  if n is odd.

For a fixed bit depth k and residue r, every n = 2^k q + r has

    T^k(n) = 3^o q + T^k(r),

where o is the number of odd shortcut steps taken by r during the first k
iterations.  If 3^o < 2^k, then all sufficiently large members of that
residue class strictly descend below their start.  A finite cover of all
residue classes by such certificates, plus a finite direct verification
below the largest threshold, would prove the divergent-orbit half of Collatz.

This script mines that cover frontier.  It is a research instrument, not a
proof of the conjecture.
"""

from __future__ import annotations

import argparse
import json
from collections import deque
from dataclasses import dataclass
from time import perf_counter


def shortcut(n: int) -> int:
    return (3 * n + 1) // 2 if n & 1 else n // 2


def affine_for_low_bits(depth: int, residue: int) -> tuple[int, int]:
    """Return (odd_count, T^depth(residue)) for the shortcut map."""
    x = residue
    odd_count = 0
    for _ in range(depth):
        if x & 1:
            odd_count += 1
            x = (3 * x + 1) // 2
        else:
            x //= 2
    return odd_count, x


def descent_threshold(depth: int, residue: int, pow3: list[int]) -> tuple[int, int, int] | None:
    """Return (odd_count, image_of_residue, q_threshold) when descent is certified."""
    odd_count, image = affine_for_low_bits(depth, residue)
    denominator = (1 << depth) - pow3[odd_count]
    if denominator <= 0:
        return None

    numerator = image - residue
    q_threshold = 0 if numerator < 0 else (numerator // denominator) + 1
    return odd_count, image, q_threshold


def bits(residue: int, depth: int) -> str:
    return format(residue, f"0{depth}b")


@dataclass
class Sample:
    depth: int
    residue: int
    odd_count: int
    image: int
    q_threshold: int | None = None

    def as_dict(self) -> dict[str, int | str | None]:
        return {
            "depth": self.depth,
            "residue": self.residue,
            "bits": bits(self.residue, self.depth),
            "odd_count": self.odd_count,
            "image": self.image,
            "q_threshold": self.q_threshold,
        }


def mine(max_depth: int, sample_limit: int) -> dict[str, object]:
    pow3 = [1]
    for _ in range(max_depth):
        pow3.append(pow3[-1] * 3)

    started = perf_counter()
    scale = 1 << max_depth
    queue: deque[tuple[int, int]] = deque([(1, 0), (1, 1)])

    certified_count = 0
    frontier_count = 0
    certified_units = 0
    frontier_units = 0
    finite_q_exceptions = 0
    max_direct_check_n = -1
    max_threshold = 0
    deepest_certificate = 0
    certified_samples: list[Sample] = []
    frontier_samples: list[Sample] = []
    odd_histogram: dict[str, int] = {}

    while queue:
        depth, residue = queue.popleft()
        cert = descent_threshold(depth, residue, pow3)
        if cert is not None:
            odd_count, image, q_threshold = cert
            certified_count += 1
            certified_units += scale >> depth
            deepest_certificate = max(deepest_certificate, depth)
            finite_q_exceptions += q_threshold
            max_threshold = max(max_threshold, q_threshold)
            if q_threshold > 0:
                max_direct_check_n = max(max_direct_check_n, (q_threshold - 1) * (1 << depth) + residue)
            if len(certified_samples) < sample_limit:
                certified_samples.append(Sample(depth, residue, odd_count, image, q_threshold))
            continue

        if depth >= max_depth:
            odd_count, image = affine_for_low_bits(depth, residue)
            frontier_count += 1
            frontier_units += 1
            odd_histogram[str(odd_count)] = odd_histogram.get(str(odd_count), 0) + 1
            if len(frontier_samples) < sample_limit:
                frontier_samples.append(Sample(depth, residue, odd_count, image))
            continue

        next_bit = 1 << depth
        queue.append((depth + 1, residue))
        queue.append((depth + 1, residue + next_bit))

    elapsed = perf_counter() - started
    certified_fraction = certified_units / scale
    frontier_fraction = frontier_units / scale
    status = "finite-cover" if frontier_count == 0 else "open-frontier"

    return {
        "status": status,
        "max_depth": max_depth,
        "elapsed_seconds": round(elapsed, 6),
        "certified_leaves": certified_count,
        "frontier_leaves": frontier_count,
        "certified_fraction": certified_fraction,
        "frontier_fraction": frontier_fraction,
        "certified_units_mod_2^max_depth": certified_units,
        "frontier_units_mod_2^max_depth": frontier_units,
        "deepest_certificate": deepest_certificate,
        "finite_q_exceptions_upper_bound": finite_q_exceptions,
        "max_q_threshold": max_threshold,
        "max_direct_check_n": max_direct_check_n,
        "frontier_odd_count_histogram": odd_histogram,
        "certified_samples": [sample.as_dict() for sample in certified_samples],
        "frontier_samples": [sample.as_dict() for sample in frontier_samples],
        "interpretation": (
            "A finite-cover status would reduce divergent-orbit exclusion to a finite direct check. "
            "An open-frontier status identifies the residue classes where this finite-depth method "
            "has not yet forced descent."
        ),
    }


def trace_start(start: int, max_depth: int) -> dict[str, object]:
    """Follow one positive integer's actual low-bit prefixes until the start is certified."""
    if start < 1:
        raise ValueError("trace_start requires a positive integer")

    pow3 = [1]
    for _ in range(max_depth):
        pow3.append(pow3[-1] * 3)

    samples: list[dict[str, int | str | None]] = []
    for depth in range(1, max_depth + 1):
        residue = start & ((1 << depth) - 1)
        quotient = start >> depth
        cert = descent_threshold(depth, residue, pow3)
        odd_count, image = affine_for_low_bits(depth, residue)
        threshold = cert[2] if cert is not None else None
        start_in_certified_tail = threshold is not None and quotient >= threshold
        if depth <= 16 or depth == max_depth or cert is not None:
            samples.append(
                {
                    **Sample(
                        depth=depth,
                        residue=residue,
                        odd_count=odd_count,
                        image=image,
                        q_threshold=threshold,
                    ).as_dict(),
                    "quotient_for_start": quotient,
                    "start_in_certified_tail": start_in_certified_tail,
                }
            )
        if start_in_certified_tail:
            return {
                "status": "certified",
                "start": start,
                "certificate_depth": depth,
                "residue": residue,
                "bits": bits(residue, depth),
                "quotient_for_start": quotient,
                "odd_count": odd_count,
                "image": image,
                "q_threshold": threshold,
                "interpretation": (
                    f"The start has q={quotient}, and every n = 2^{depth} q + {residue} "
                    f"with q >= {threshold} descends after {depth} shortcut steps."
                ),
                "prefix_samples": samples,
            }

    return {
        "status": "not-certified-within-depth",
        "start": start,
        "max_depth": max_depth,
        "prefix_samples": samples,
    }


def self_test(max_depth: int) -> None:
    for depth in range(1, max_depth + 1):
        modulus = 1 << depth
        for residue in range(modulus):
            odd_count, image = affine_for_low_bits(depth, residue)
            multiplier = 3**odd_count
            for q in range(8):
                n = modulus * q + residue
                x = n
                for _ in range(depth):
                    x = shortcut(x)
                expected = multiplier * q + image
                if x != expected:
                    raise AssertionError(
                        f"affine law failed at depth={depth}, residue={residue}, q={q}: {x} != {expected}"
                    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-depth", type=int, default=20, help="maximum 2-adic bit depth to mine")
    parser.add_argument("--sample-limit", type=int, default=12, help="number of sample leaves to report")
    parser.add_argument("--self-test", action="store_true", help="verify the affine law before mining")
    parser.add_argument("--trace-start", type=int, help="trace certificate depth for one positive starting value")
    args = parser.parse_args()

    if args.max_depth < 1:
        raise SystemExit("--max-depth must be at least 1")

    if args.self_test:
        self_test(min(args.max_depth, 12))

    if args.trace_start is not None:
        payload = trace_start(args.trace_start, args.max_depth)
    else:
        payload = mine(args.max_depth, args.sample_limit)

    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
