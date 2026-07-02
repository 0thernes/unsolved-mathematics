#!/usr/bin/env python3
"""Exact affine maps for the two tail-memory shortcut words.

The memory-tail extractor found two length-8 words:

* EEOOEOOO
* EEOEOOOO

This script computes their exact shortcut cylinders, affine maps, lifted
source classes, residue paths, and the forced low-repeat bridge through
`59 mod 64`.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from time import perf_counter

from branch_potential_analyzer import round_float, shortcut_step


WORDS = ("EEOOEOOO", "EEOEOOOO")
MODULI = (16, 32, 64, 128, 256, 512, 1024, 4096, 65536)


def parity_name(parity: int) -> str:
    return "O" if parity else "E"


def word_parities(start: int, steps: int) -> str:
    current = start
    letters: list[str] = []
    for _ in range(steps):
        current, parity = shortcut_step(current)
        letters.append(parity_name(parity))
    return "".join(letters)


def cylinder_residue(word: str) -> int:
    modulus = 1 << len(word)
    matches = [residue for residue in range(modulus) if word_parities(residue, len(word)) == word]
    if len(matches) != 1:
        raise ValueError(f"expected one cylinder residue for {word}, found {matches}")
    return matches[0]


def affine_map(word: str) -> dict[str, int]:
    constant = 0
    odds = 0
    for index, letter in enumerate(word):
        if letter == "E":
            pass
        elif letter == "O":
            constant = 3 * constant + (1 << index)
            odds += 1
        else:
            raise ValueError(f"bad letter {letter!r}")
    return {
        "multiplier": 3**odds,
        "constant": constant,
        "denominator": 1 << len(word),
        "odd_count": odds,
        "length": len(word),
    }


def residue_path(start_residue: int, steps: int, modulus: int) -> list[int]:
    current = start_residue
    path = [current % modulus]
    for _ in range(steps):
        current, _ = shortcut_step(current)
        path.append(current % modulus)
    return path


def transition_table(start_residue: int, steps: int, modulus: int) -> list[dict[str, int | str]]:
    current = start_residue
    table: list[dict[str, int | str]] = []
    for index in range(1, steps + 1):
        before = current
        current, parity = shortcut_step(current)
        table.append(
            {
                "index": index,
                "parity": parity_name(parity),
                "before_mod": before % modulus,
                "after_mod": current % modulus,
            }
        )
    return table


def residue_path_from_lifted_source(start_residue: int, steps: int, modulus: int) -> list[int]:
    return residue_path(start_residue, steps, modulus)


def output_residue_classes(word: str, source_modulus: int, output_modulus: int) -> dict[str, object]:
    residue = cylinder_residue(word)
    affine = affine_map(word)
    source_classes = [value for value in range(source_modulus) if value % (1 << len(word)) == residue]
    outputs = Counter()
    examples = []
    for value in source_classes:
        out = (affine["multiplier"] * value + affine["constant"]) // affine["denominator"]
        outputs[out % output_modulus] += 1
        examples.append({"source_mod": value, "output_mod": out % output_modulus})
    return {
        "source_modulus": source_modulus,
        "output_modulus": output_modulus,
        "source_class_count": len(source_classes),
        "output_counts": dict(sorted((str(key), value) for key, value in outputs.items())),
        "examples": examples[:16],
    }


def memory_record_compatibility(word: str, records: list[dict[str, object]]) -> dict[str, object]:
    residue = cylinder_residue(word)
    lifted_modulus = 1 << (len(word) + 6)
    matched = [record for record in records if str(record["source_to_terminal_parity_word"]) == word]
    failures = []
    path_failures = []
    terminal_outputs = Counter()
    source_mods = Counter()
    lifted_source_mods = Counter()
    lifted_paths = Counter()
    lifted_terminal_outputs = Counter()
    for record in matched:
        source = int(record["source_state"])
        terminal = int(record["terminal"])
        affine = affine_map(word)
        computed = (affine["multiplier"] * source + affine["constant"]) // affine["denominator"]
        source_mods[source % 256] += 1
        lifted_source = source % lifted_modulus
        lifted_source_mods[lifted_source] += 1
        terminal_outputs[terminal % 64] += 1
        lifted_terminal_outputs[computed % 64] += 1
        path = residue_path_from_lifted_source(lifted_source, len(word), 64)
        lifted_paths[",".join(str(value) for value in path)] += 1
        if source % 256 != residue or computed != terminal:
            failures.append(
                {
                    "parent": record["parent"],
                    "child": record["child"],
                    "source_mod_256": source % 256,
                    "expected_source_mod_256": residue,
                    "computed_terminal": computed,
                    "terminal": terminal,
                }
            )
        if path != list(record["source_to_terminal_states_mod64"]):
            path_failures.append(
                {
                    "parent": record["parent"],
                    "child": record["child"],
                    "computed_path_mod64": path,
                    "record_path_mod64": record["source_to_terminal_states_mod64"],
                }
            )
    return {
        "matched_record_count": len(matched),
        "source_mod_256_counts": dict(sorted((str(key), value) for key, value in source_mods.items())),
        "lifted_source_modulus_for_mod64_path": lifted_modulus,
        "lifted_source_mod_counts": dict(sorted((str(key), value) for key, value in lifted_source_mods.items())),
        "lifted_path_mod64_counts": dict(sorted(lifted_paths.items())),
        "terminal_mod_64_counts": dict(sorted((str(key), value) for key, value in terminal_outputs.items())),
        "lifted_affine_terminal_mod_64_counts": dict(
            sorted((str(key), value) for key, value in lifted_terminal_outputs.items())
        ),
        "affine_failures": failures,
        "path_failures": path_failures,
    }


def word_report(word: str, memory_records: list[dict[str, object]]) -> dict[str, object]:
    residue = cylinder_residue(word)
    affine = affine_map(word)
    generic_path64 = residue_path(residue, len(word), 64)
    terminal_mod64 = generic_path64[-1]
    low_repeat_index = None
    for index, value in enumerate(generic_path64):
        if value == 59:
            low_repeat_index = index
            break
    compatibility = memory_record_compatibility(word, memory_records)
    memory_paths = list(compatibility["lifted_path_mod64_counts"])
    memory_paths_pass_59 = all("59" in path.split(",") for path in memory_paths)
    memory_paths_have_preterminal_25 = all(path.split(",")[-2] == "25" for path in memory_paths)
    return {
        "word": word,
        "length": len(word),
        "odd_count": affine["odd_count"],
        "cylinder_residue_mod_2^length": residue,
        "cylinder_residue_mod_64": residue % 64,
        "affine": affine,
        "affine_formula": f"T^{len(word)}(n) = ({affine['multiplier']}*n + {affine['constant']})/{affine['denominator']}",
        "generic_residue_path_mod_64_from_mod256_cylinder": generic_path64,
        "transition_table_mod_64": transition_table(residue, len(word), 64),
        "passes_low_repeat_59_mod_64": low_repeat_index is not None,
        "low_repeat_index": low_repeat_index,
        "preterminal_residue_mod_64": generic_path64[-2],
        "terminal_residue_mod_64_from_cylinder": terminal_mod64,
        "output_mod_64_by_source_mod_4096": output_residue_classes(word, 4096, 64),
        "memory_lifted_paths_pass_59_mod64": memory_paths_pass_59,
        "memory_lifted_paths_have_preterminal_25_mod64": memory_paths_have_preterminal_25,
        "memory_record_compatibility": compatibility,
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    started = perf_counter()
    memory_payload = json.loads(args.memory_result.read_text(encoding="utf-8"))
    memory_records = list(memory_payload["records"])
    reports = [word_report(word, memory_records) for word in WORDS]
    pure_claims = {
        "all_words_length_8_odd_count_5": all(report["length"] == 8 and report["odd_count"] == 5 for report in reports),
        "raw_mod256_word_paths_do_not_force_59_mod64": not any(
            bool(report["passes_low_repeat_59_mod_64"]) for report in reports
        ),
        "memory_lifted_paths_pass_59_mod64": all(
            bool(report["memory_lifted_paths_pass_59_mod64"]) for report in reports
        ),
        "memory_lifted_paths_have_preterminal_25_mod64": all(
            bool(report["memory_lifted_paths_have_preterminal_25_mod64"]) for report in reports
        ),
        "all_memory_records_affine_compatible": all(
            not report["memory_record_compatibility"]["affine_failures"] for report in reports
        ),
        "all_memory_paths_match_records": all(
            not report["memory_record_compatibility"]["path_failures"] for report in reports
        ),
    }
    return {
        "status": "branch-prefix-tail-memory-word-maps",
        "elapsed_seconds": round_float(perf_counter() - started, 6),
        "parameters": {
            key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()
        },
        "memory_record_count": len(memory_records),
        "pure_claims": pure_claims,
        "word_reports": reports,
        "interpretation": (
            "Exact affine and residue-cylinder maps for the two length-8 memory-tail words. "
            "These maps are symbolic support for replacing the six observed records with a "
            "two-word local lemma."
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
