#!/usr/bin/env python3
"""Targeted Mutation Testing Suite (Build Standard B13).

Injects 6 concrete logic mutants in-memory (never modifying tracked files on disk),
recreating real bug classes caught during the v0.3.0 forensic audit, and asserts
that our test suite kills 100% of mutants.

Exit 0 iff all mutants are killed; exit 1 if any mutant survives.
"""

from __future__ import annotations

import sys
import tempfile
from collections.abc import Callable
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
for _p in (ROOT, ROOT / "scripts", ROOT / "rag", ROOT / "tests"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import build_corpus  # noqa: E402
import check_dossiers  # noqa: E402
import generate  # noqa: E402
import proof_claim_sweep  # noqa: E402
import test_atlas  # noqa: E402
import test_verification_ladder as tvl  # noqa: E402


def run_mutant(name: str, apply_mutation: Callable[[], Callable[[], None]], check: Callable[[], None]) -> bool:
    """Apply a mutant, run check(); return True if mutant is KILLED (check raises)."""
    restore = apply_mutation()
    try:
        try:
            check()
        except AssertionError:
            print(f"  KILLED    {name}")
            return True
        except Exception as exc:
            print(f"  KILLED    {name} ({type(exc).__name__})")
            return True
        else:
            print(f"  SURVIVED  {name}")
            return False
    finally:
        restore()


def main() -> int:
    print("Running targeted mutation suite (6 mutants covering core invariants & historical bugs):")
    results: list[bool] = []

    # Mutant 1: Drop centrality weight from composite_severity
    def mut_drop_centrality():
        orig = generate.composite_severity

        def broken(p: dict) -> float:
            return round(
                0.40 * p["difficulty"]
                + 0.00 * p["centrality"]
                + 0.20 * generate.age_score(p["year_posed"])
                + 0.10 * (100 - p["tractability"]),
                3,
            )

        generate.composite_severity = broken
        return lambda: setattr(generate, "composite_severity", orig)

    results.append(run_mutant("M1: drop centrality weight in generate.composite_severity", mut_drop_centrality, tvl.test_metamorphic_css_monotonicity))

    # Mutant 2: Constant age_score (breaks age sensitivity)
    def mut_const_age():
        orig = generate.age_score
        generate.age_score = lambda _y: 50.0
        return lambda: setattr(generate, "age_score", orig)

    results.append(run_mutant("M2: constant age_score in generate.age_score", mut_const_age, test_atlas.test_age_score_bounds))

    # Mutant 3: Non-deterministic/reversed slug tie-break in generate.rank_problems (recreates BUG-03)
    def mut_bad_tiebreak():
        orig = generate.rank_problems

        def broken(problems: list[dict]):
            ordered = sorted(problems, key=lambda p: -generate.composite_severity(p))
            return [(i + 1, generate.composite_severity(p), p) for i, p in enumerate(ordered)]

        generate.rank_problems = broken
        return lambda: setattr(generate, "rank_problems", orig)

    results.append(run_mutant("M3: remove slug tie-break in generate.rank_problems (BUG-03)", mut_bad_tiebreak, tvl.test_regression_bug03_deterministic_css_tie_breaking))

    # Mutant 4: Reset chunk_idx per heading in build_corpus (recreates BUG-01 duplicate chunk IDs)
    def mut_dup_chunk_ids():
        orig = build_corpus.build_records

        def broken(problems_dir: Path = build_corpus.PROBLEMS_DIR, root: Path = build_corpus.ROOT):
            recs = orig(problems_dir, root)
            for r in recs:
                r["id"] = f"{r['slug']}::{r['section']}::0"
            return recs

        build_corpus.build_records = broken
        return lambda: setattr(build_corpus, "build_records", orig)

    def check_m4():
        with tempfile.TemporaryDirectory() as td:
            tvl.test_regression_bug01_rag_chunk_ids_globally_unique(Path(td))

    results.append(run_mutant("M4: reset chunk_idx=0 per heading in build_corpus (BUG-01)", mut_dup_chunk_ids, check_m4))

    # Mutant 5: Re-introduce single-word 'heuristic' bypass in proof_claim_sweep (recreates BUG-07)
    def mut_hedge_bypass():
        orig = list(proof_claim_sweep.EXPLICIT_DISCLAIMER)
        proof_claim_sweep.EXPLICIT_DISCLAIMER.append(r"\bheuristic\b")
        return lambda: proof_claim_sweep.EXPLICIT_DISCLAIMER.__setitem__(slice(None), orig)

    results.append(run_mutant("M5: re-add single-word 'heuristic' disclaimer in proof_claim_sweep (BUG-07)", mut_hedge_bypass, tvl.test_negative_single_word_hedge_cannot_bypass_sweep))

    # Mutant 6: Miscount multi-table headers in check_dossiers.count_table_rows (recreates BUG-04)
    def mut_table_count():
        orig = check_dossiers.count_table_rows

        def broken(text: str) -> int:
            pipe_lines = [ln for ln in text.splitlines() if ln.strip().startswith("|")]
            return max(0, len(pipe_lines) - 2)

        check_dossiers.count_table_rows = broken
        return lambda: setattr(check_dossiers, "count_table_rows", orig)

    results.append(run_mutant("M6: naive pipe-line - 2 count in check_dossiers.count_table_rows (BUG-04)", mut_table_count, tvl.test_regression_bug04_count_table_rows_excludes_all_headers))

    killed = sum(results)
    total = len(results)
    print(f"\nMutation score: {killed}/{total} ({100.0 * killed / total:.1f}%)")
    return 0 if killed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
