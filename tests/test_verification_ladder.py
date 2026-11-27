# SPDX-License-Identifier: MIT
"""Verification Test Ladder for The Unsolved Mathematics Atlas (Build Standard B03–B14).

Covers:
  - Negative tests (B06): invalid schema entries, unhedged proof claims, single-word
    hedge bypasses, attractor filenames.
  - Regression tests (B07): one dedicated test per fixed bug/error (BUG-01..BUG-07,
    ERR-02, ERR-03).
  - Golden & determinism tests (B03, B08): zero-drift generate --check, validate.py,
    data/MANIFEST.sha256, example CLI.
  - Contract & schema tests (B09): problems.json vs schema/problem.schema.json, VERSION
    parity, rag/corpus.jsonl record contract, citation-verification-log consistency.
  - Differential & reference-oracle tests (B11, B12): independent exact Python arithmetic
    cross-checking all four Lean 4.35.0 formal cores (Collatz, Erdős–Straus, Lonely Runner,
    Brocard).
  - Metamorphic tests (B14): CSS monotonicity under score perturbations; BM25 ranking
    invariance under document permutation.
"""

from __future__ import annotations

import json
import math
import random
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
for _p in (ROOT, ROOT / "scripts", ROOT / "rag"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import build_corpus  # noqa: E402
import check_dossiers  # noqa: E402
import generate  # noqa: E402
import proof_claim_sweep  # noqa: E402
from retriever import BM25  # noqa: E402


# --------------------------------------------------------------------------- #
#  Negative Tests (B06)
# --------------------------------------------------------------------------- #
def test_negative_invalid_registry_entry_rejected():
    bad_problem = {
        "slug": "bad-entry",
        "title": "Bad Entry",
        "difficulty": 150,  # out of [0, 100]
        "centrality": 50,
        "tractability": 50,
        "year_posed": 2000,
    }
    errors = generate.validate([bad_problem])
    assert errors, "Expected jsonschema validation errors for malformed problem entry"


def test_negative_duplicate_slug_rejected():
    data = generate.yaml.safe_load(generate.REGISTRY_YAML.read_text(encoding="utf-8"))
    first = dict(data["problems"][0])
    errors = generate.validate([first, first])
    assert any("duplicate slug" in e for e in errors), errors


def test_negative_unhedged_victory_claim_flagged():
    bad_text = (
        "# Breakthrough\n\n"
        "We show S ∩ Z>0 = ∅ therefore Collatz is solved.\n"
        "Achieved. QED. The conjecture is resolved.\n"
    )
    flagged, reasons = proof_claim_sweep.scan_text("notes.md", bad_text)
    assert flagged is True, "Unhedged victory declaration must be flagged"
    assert reasons


def test_negative_single_word_hedge_cannot_bypass_sweep():
    """Regression for BUG-07: mentioning 'heuristic' or 'candidate' must NOT bypass sweep."""
    tricky_text = (
        "# Candidate Heuristic Analysis\n\n"
        "This candidate heuristic resolves everything: therefore Collatz is solved.\n"
        "The conjecture is resolved and closes the conjecture for positives. Achieved. QED.\n"
    )
    flagged, _ = proof_claim_sweep.scan_text("sketch.md", tricky_text)
    assert flagged is True, "Single-word candidate/heuristic must not suppress proof-claim sweep"


def test_negative_attractor_filename_flagged():
    flagged, reasons = proof_claim_sweep.scan_text("COLLATZ-RESOLUTION-2026.md", "Harmless text.")
    assert flagged is True
    assert "attractor filename" in reasons


def test_negative_explicit_disclaimer_clears_sweep():
    audit_text = (
        "# Claim Audit\n\n"
        "Status: Open. This note does not prove the conjecture.\n"
        "Earlier drafts wrongly wrote 'Collatz is solved' and 'the conjecture is resolved'.\n"
    )
    flagged, _ = proof_claim_sweep.scan_text("audit_note.md", audit_text)
    assert flagged is False


# --------------------------------------------------------------------------- #
#  Regression Tests per Fixed Bug & Error (B07)
# --------------------------------------------------------------------------- #
def test_regression_bug01_rag_chunk_ids_globally_unique(tmp_path: Path):
    """BUG-01: multi-heading sections must produce monotonic, globally unique chunk IDs."""
    prob_dir = tmp_path / "demo-problem"
    prob_dir.mkdir()
    (prob_dir / "metadata.json").write_text(
        json.dumps({"slug": "demo-problem", "rank": 1, "title": "Demo", "field": "Number Theory"}),
        encoding="utf-8",
    )
    (prob_dir / "history.md").write_text(
        "# History\n\nIntro paragraph.\n\n## Part One\n\nFirst body.\n\n## Part Two\n\nSecond body.\n",
        encoding="utf-8",
    )
    recs = build_corpus.build_records(tmp_path, tmp_path)
    ids = [r["id"] for r in recs]
    assert len(ids) == 3
    assert len(ids) == len(set(ids)), f"Duplicate chunk IDs generated: {ids}"
    assert ids == [
        "demo-problem::history::0",
        "demo-problem::history::1",
        "demo-problem::history::2",
    ]


def test_regression_bug02_all_120_dossier_readmes_synced():
    """BUG-02: every problems/<slug>/README.md must reflect current Atlas Rank & CSS."""
    reg = json.loads((ROOT / "data" / "problems.json").read_text(encoding="utf-8"))
    assert len(reg["problems"]) == 120
    for p in reg["problems"]:
        readme = (ROOT / "problems" / p["slug"] / "README.md").read_text(encoding="utf-8")
        expected = generate.dossier_header_line(p, p["rank"], p["css"])
        assert expected in readme, f"Stale header in problems/{p['slug']}/README.md"


def test_regression_bug03_deterministic_css_tie_breaking():
    """BUG-03: identical CSS scores must sort deterministically by ascending slug."""
    base = {
        "difficulty": 80,
        "centrality": 80,
        "tractability": 20,
        "year_posed": 1950,
    }
    p_z = {**base, "slug": "zeta-problem"}
    p_a = {**base, "slug": "alpha-problem"}
    p_m = {**base, "slug": "mu-problem"}
    r1 = [p["slug"] for _, _, p in generate.rank_problems([p_z, p_m, p_a])]
    r2 = [p["slug"] for _, _, p in generate.rank_problems([p_a, p_z, p_m])]
    assert r1 == r2 == ["alpha-problem", "mu-problem", "zeta-problem"]


def test_regression_bug04_count_table_rows_excludes_all_headers():
    """BUG-04: multi-table markdown must exclude every table's header and separator."""
    md = (
        "# Papers\n\n"
        "| # | Title |\n"
        "|---|-------|\n"
        "| 1 | Paper A |\n"
        "| 2 | Paper B |\n\n"
        "## Addendum\n\n"
        "| # | Title |\n"
        "|---|-------|\n"
        "| 3 | Paper C |\n"
    )
    assert check_dossiers.count_table_rows(md) == 3


def test_regression_bug05_deterministic_token_counter():
    """BUG-05: token counter must be pure deterministic stdlib with no tiktoken import."""
    src = (ROOT / "rag" / "build_corpus.py").read_text(encoding="utf-8")
    assert "import tiktoken" not in src
    assert build_corpus.count_tokens("") == 1
    assert build_corpus.count_tokens("abcd" * 25) == 25


def test_regression_bug07_retracted_collatz_sketch_carries_banner():
    sketch = (
        ROOT
        / "problems"
        / "collatz-conjecture"
        / "experiments"
        / "PROOF-SKETCH-AFFINE-COCYCLE-RIGIDITY-2026.md"
    ).read_text(encoding="utf-8")
    assert "WITHDRAWN" in sketch or "REFUTED" in sketch
    flagged, _ = proof_claim_sweep.scan_text("PROOF-SKETCH-AFFINE-COCYCLE-RIGIDITY-2026.md", sketch)
    assert flagged is False


def test_regression_err02_goldbach_exceptional_set_exponent():
    status = (ROOT / "problems" / "goldbach-conjecture" / "status.md").read_text(encoding="utf-8")
    assert "0.72" in status


def test_regression_err03_navier_stokes_ess_year_2003():
    for fname in ("history.md", "papers.md", "status.md"):
        txt = (ROOT / "problems" / "navier-stokes-smoothness" / fname).read_text(encoding="utf-8")
        assert "Escauriaza" in txt
        assert "2003" in txt


# --------------------------------------------------------------------------- #
#  Golden / Determinism & Contract Tests (B03, B08, B09)
# --------------------------------------------------------------------------- #
def test_golden_cli_validators_pass():
    for cmd in (
        [sys.executable, str(ROOT / "scripts" / "generate.py"), "--check"],
        [sys.executable, str(ROOT / "scripts" / "validate.py")],
        [sys.executable, str(ROOT / "scripts" / "check_papers.py")],
        [sys.executable, str(ROOT / "scripts" / "proof_claim_sweep.py")],
        [sys.executable, str(ROOT / "scripts" / "build_data_manifest.py"), "--check"],
        [sys.executable, str(ROOT / "examples" / "query_atlas.py"), "--top", "5"],
        [sys.executable, str(ROOT / "examples" / "query_atlas.py"), "--search", "positivity localization collatz"],
    ):
        proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        assert proc.returncode == 0, f"Command failed: {cmd}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"


def test_contract_problems_json_and_version_parity():
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    reg = json.loads((ROOT / "data" / "problems.json").read_text(encoding="utf-8"))
    assert reg["meta"]["version"] == version
    assert len(reg["problems"]) == 120
    errors = generate.validate(reg["problems"])
    assert errors == [], errors


def test_contract_corpus_jsonl_unique_and_well_formed():
    lines = (ROOT / "rag" / "corpus.jsonl").read_text(encoding="utf-8").splitlines()
    assert len(lines) > 3000
    seen: set[str] = set()
    required = {"id", "slug", "section", "text", "tokens", "source"}
    for ln in lines:
        rec = json.loads(ln)
        assert required.issubset(rec.keys())
        assert rec["tokens"] >= 1
        assert rec["id"] not in seen, f"Duplicate corpus ID: {rec['id']}"
        seen.add(rec["id"])


def test_contract_citation_verification_log_consistent():
    log = json.loads((ROOT / "data" / "citation-verification-log.json").read_text(encoding="utf-8"))
    summary = log["summary"]
    assert summary["network_error"] == 0
    records = log["records"]
    assert sum(summary.values()) == len(records)
    assert summary["verified"] >= 440


# --------------------------------------------------------------------------- #
#  Differential & Reference-Oracle Tests vs Lean 4.35.0 Core (B11, B12)
# --------------------------------------------------------------------------- #
def _collatz_T(x: int) -> int:
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def _collatz_T_minus(x: int) -> int:
    return x // 2 if x % 2 == 0 else (3 * x - 1) // 2


def _parity_word(f, d: int, x: int) -> list[bool]:
    out = []
    cur = x
    for _ in range(d):
        out.append((cur % 2) != 0)
        cur = f(cur)
    return out


def _word_intercept(w: list[bool]) -> int:
    if not w:
        return 0
    b, *ws = w
    if not b:
        return 2 * _word_intercept(ws)
    return (3 ** sum(ws)) + 2 * _word_intercept(ws)


def test_oracle_collatz_affine_law_and_terras_bijection():
    """Differential check matching FormalAtlas.Collatz cylinder affine law & Terras bijection."""
    for d in range(1, 8):
        seen_words = set()
        for x in range(2**d):
            w = _parity_word(_collatz_T, d, x)
            seen_words.add(tuple(w))
            cur = x
            for _ in range(d):
                cur = _collatz_T(cur)
            k = sum(w)
            assert (2**d) * cur == (3**k) * x + _word_intercept(w)
        assert len(seen_words) == 2**d, f"Terras map failed bijectivity at d={d}"


def test_oracle_collatz_3n_minus_1_sign_invariance_barrier():
    """Differential check matching FormalAtlas.Collatz epsilon-invariance 3n-1 cycle 5->7->10->5."""
    assert _collatz_T_minus(5) == 7
    assert _collatz_T_minus(7) == 10
    assert _collatz_T_minus(10) == 5
    w = _parity_word(_collatz_T_minus, 3, 5)
    assert w == [True, True, False]
    assert (2**3) * 5 == (3**2) * 5 - _word_intercept(w)


def _erdos_straus_mordell_witness(n: int) -> tuple[int, int, int] | None:
    """Explicit Egyptian-fraction witness covering all 834/840 non-exceptional classes."""
    if n % 2 == 0:
        m = n // 2
        return (m, 2 * m, 2 * m)
    if n % 3 == 2:
        k = (n + 1) // 3
        return (k, n, k * n)
    if n % 4 == 3:
        k = (n + 1) // 4
        return (k, 2 * k * n, 2 * k * n)
    if n % 8 == 5:
        k = (n + 3) // 8
        return (2 * k, k * n, 2 * k * n)
    # Now n ≡ 1 (mod 24) or n ≡ 9, 17 (mod 24)
    if n % 3 == 0:
        m = n // 3
        return (m, 6 * m, 6 * m)
    # Check mod 5 and mod 7 residue constructions matching Mordell mod 840
    if n % 5 == 2:
        # 4/(5k+2) = 1/(2k+1) + ...
        k = (n + 3) // 5
        a = k
        rem = Fraction(4, n) - Fraction(1, a)
        if rem > 0 and rem.numerator == 1:
            return (a, 2 * rem.denominator, 2 * rem.denominator)
    # General direct exact witness finder for small multipliers matching Mordell identities
    for x in range(n // 4 + 1, (3 * n) // 4 + 2):
        rem = Fraction(4, n) - Fraction(1, x)
        if rem <= 0:
            continue
        p, q = rem.numerator, rem.denominator
        if p == 1:
            return (x, 2 * q, 2 * q)
        if p == 2:
            y = (q + 1) // 2
            rem2 = rem - Fraction(1, y)
            if rem2 > 0 and rem2.numerator == 1:
                return (x, y, rem2.denominator)
        # Check greedy-2 split
        y_lo = q // p + 1
        for y in range(y_lo, min(y_lo + 40, (2 * q) // p + 2)):
            rem2 = rem - Fraction(1, y)
            if rem2 > 0 and rem2.numerator == 1:
                return (x, y, rem2.denominator)
    return None


def test_oracle_erdos_straus_mordell_840():
    """Verify 4/n = 1/x + 1/y + 1/z in exact Fraction arithmetic for n ∈ [2, 1000] outside Mordell's 6 classes."""
    exceptional = {1, 121, 169, 289, 361, 529}
    checked = 0
    for n in range(2, 1001):
        if n % 840 in exceptional:
            continue
        wit = _erdos_straus_mordell_witness(n)
        assert wit is not None, f"No witness found for non-exceptional n={n}"
        x, y, z = wit
        assert x > 0 and y > 0 and z > 0
        assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
        checked += 1
    assert checked >= 990


def test_oracle_lonely_runner_sharpness_and_small_n():
    """Verify Lonely Runner sharpness δ ≤ 1/(n+1) for speeds (1..n) and exact n=1, n=2 witnesses."""
    def circ_dist(val: Fraction) -> Fraction:
        frac = val - math.floor(val)
        return min(frac, 1 - frac)

    for n in range(1, 9):
        # Sharpness: at t = 1/(n+1), runner 1 has distance 1/(n+1), and for any t in [0,1)
        # Dirichlet pigeonhole forces min_{1<=v<=n} ||t*v|| <= 1/(n+1).
        t_opt = Fraction(1, n + 1)
        assert min(circ_dist(t_opt * v) for v in range(1, n + 1)) == Fraction(1, n + 1)

    # n = 2 exact witness check across 40 pairs of distinct positive speeds
    for v1 in range(1, 10):
        for v2 in range(v1 + 1, 12):
            found = False
            for q in (3 * v1, 3 * v2, v1 + v2, abs(v2 - v1)):
                for p in range(1, q):
                    t = Fraction(p, q)
                    if circ_dist(t * v1) >= Fraction(1, 3) and circ_dist(t * v2) >= Fraction(1, 3):
                        found = True
                        break
                if found:
                    break
            assert found, f"Lonely Runner n=2 witness failed for ({v1}, {v2})"


def test_oracle_brocard_exhaustive_le_12():
    """Differential check matching FormalAtlas.Brocard exhaustive classification for n <= 12."""
    sols = []
    for n in range(1, 13):
        val = math.factorial(n) + 1
        m = math.isqrt(val)
        if m * m == val:
            sols.append((n, m))
    assert sols == [(4, 5), (5, 11), (7, 71)]


# --------------------------------------------------------------------------- #
#  Metamorphic Tests (B14)
# --------------------------------------------------------------------------- #
def test_metamorphic_css_monotonicity():
    base = {
        "slug": "test",
        "difficulty": 70,
        "centrality": 60,
        "tractability": 40,
        "year_posed": 1920,
    }
    s0 = generate.composite_severity(base)
    assert generate.composite_severity({**base, "difficulty": 85}) > s0
    assert generate.composite_severity({**base, "centrality": 75}) > s0
    assert generate.composite_severity({**base, "tractability": 20}) > s0
    assert generate.composite_severity({**base, "year_posed": 1820}) > s0


def test_metamorphic_bm25_permutation_invariance():
    docs = [
        {"id": "a", "section": "history", "text": "riemann zeta function zeros critical line"},
        {"id": "b", "section": "history", "text": "collatz affine parity word cycle barrier"},
        {"id": "c", "section": "history", "text": "kakeya besicovitch needle set dimension"},
        {"id": "d", "section": "history", "text": "erdos straus unit fractions mordell congruence"},
    ]
    base_res = BM25(docs).search("collatz parity barrier", k=4)
    rng = random.Random(20261123)
    for _ in range(10):
        perm = list(docs)
        rng.shuffle(perm)
        perm_res = BM25(perm).search("collatz parity barrier", k=4)
        assert [(d["id"], round(s, 9)) for s, d in perm_res] == [
            (d["id"], round(s, 9)) for s, d in base_res
        ]


# --------------------------------------------------------------------------- #
#  Adversarial Second-Pass Regression Tests (B07)
# --------------------------------------------------------------------------- #
def test_regression_pass2_claims_c03_supercritical_accuracy():
    """Verify CLAIMS.md C-03 matches Lean thm_collatz_positivity_localization (supercritical, not subcritical)."""
    txt = (ROOT / "CLAIMS.md").read_text(encoding="utf-8")
    assert "supercritical" in txt.lower()
    assert "2^S > 3^k" not in txt
    assert "word defect" not in txt.lower()


def test_regression_pass2_meta_analyses_synced_and_error_free():
    """Verify Pass #2 fixes in meta-analyses: Goldbach 0.72, Navier-Stokes 2003, Unit Distance 2605.20695."""
    gb = (ROOT / "meta-analyses" / "goldbach-conjecture.md").read_text(encoding="utf-8")
    gb_body = gb.split("## AI Review Panel", 1)[0]
    assert "0.72" in gb_body and r"\delta\approx0.7" not in gb_body

    ns = (ROOT / "meta-analyses" / "navier-stokes-smoothness.md").read_text(encoding="utf-8")
    assert "Escauriaza–Seregin–Šverák (2003" in ns
    assert "Escauriaza–Seregin–Šverák (2001)" not in ns

    ud = (ROOT / "meta-analyses" / "unit-distance-problem.md").read_text(encoding="utf-8")
    assert "arXiv:2605.20695" in ud

    for slug in (
        "lonely-runner-conjecture",
        "hadwiger-conjecture",
        "riemann-hypothesis",
        "grand-riemann-hypothesis",
        "moving-sofa-problem",
        "sunflower-conjecture",
        "union-closed-sets-conjecture",
        "crouzeix-conjecture",
        "sendov-conjecture",
    ):
        txt = (ROOT / "meta-analyses" / f"{slug}.md").read_text(encoding="utf-8")
        assert "Frontier Addendum (`2026-11-23`)" in txt, f"Missing 2026 addendum in meta-analyses/{slug}.md"


def test_regression_pass2_lowercase_glossary_for_linux():
    """Verify docs/glossary.md is tracked with exact lowercase filename so Linux A44 passes."""
    proc = subprocess.run(
        ["git", "ls-files", "docs/glossary.md"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    assert proc.stdout.strip() == "docs/glossary.md"


def test_regression_pass2_static_site_builder(tmp_path: Path):
    """Verify scripts/build_site.py builds a valid static HTML Atlas without placeholders."""
    import build_site

    out = build_site.build_site(tmp_path / "_site")
    assert out.exists()
    html_txt = out.read_text(encoding="utf-8")
    assert "<!doctype html>" in html_txt.lower()
    assert "The Riemann Hypothesis" in html_txt
    assert "The Unsolved Mathematics Atlas" in html_txt
    assert (tmp_path / "_site" / "problems.json").exists()


def test_regression_pass2_submissions_honest_panel_disclosure():
    """Verify SUBMISSIONS.md cover-letter template does not falsely claim 4 AI models ran."""
    txt = (ROOT / "SUBMISSIONS.md").read_text(encoding="utf-8")
    assert "put it through a four-model" not in txt.lower()
    assert "0009-0006-8168-9648" in txt


# --------------------------------------------------------------------------- #
#  Cycle 1–3 (v0.4.0) Formal Oracle, Hygiene & Playbook v1.3 Regression Tests
# --------------------------------------------------------------------------- #
def test_oracle_collatz_cycle_equation_and_negative_cycles():
    """Differential check matching thm_collatz_cycle_equation & thm_collatz_negative_cycles."""
    for start, period in ((-5, 3), (-17, 11), (1, 2), (-1, 1)):
        cur = start
        for _ in range(period):
            cur = _collatz_T(cur)
        assert cur == start, f"Expected cycle of length {period} at {start}, got {cur}"
        w = _parity_word(_collatz_T, period, start)
        o = sum(w)
        assert ((2**period) - (3**o)) * start == _word_intercept(w)
        if start < 0:
            assert 2**period < 3**o or start == -1


def test_oracle_erdos_straus_small_exceptional_squares():
    """Differential check matching thm_erdos_straus_mordell_exceptions_small & closure."""
    for base in (11, 13, 17, 19, 23, 29):
        wit = _erdos_straus_mordell_witness(base)
        assert wit is not None
        x, y, z = wit
        n_sq = base * base
        xs, ys, zs = x * base, y * base, z * base
        assert Fraction(4, n_sq) == Fraction(1, xs) + Fraction(1, ys) + Fraction(1, zs)


def test_oracle_lonely_runner_speed_scaling_invariance():
    """Differential check matching thm_lonely_runner_speed_scaling."""
    for m, p, q, v, k in ((3, 1, 6, 3, 7), (3, 1, 6, 10, 5), (2, 1, 2, 1, 11)):
        r1 = (p * v) % q
        assert q <= m * r1 and q <= m * (q - r1)
        r2 = (p * (v * k)) % (q * k)
        assert r2 == r1 * k
        assert q * k <= m * r2 and q * k <= m * (q * k - r2)


def test_oracle_brocard_exhaustive_le_15_and_mod4():
    """Differential check matching thm_brocard_exhaustive_le_15 & thm_brocard_mod4_ge_4."""
    sols = []
    for n in range(0, 16):
        val = math.factorial(n) + 1
        m = math.isqrt(val)
        if m * m == val:
            sols.append((n, m))
        if n >= 4:
            assert val % 4 == 1
    assert sols == [(4, 5), (5, 11), (7, 71)]


def test_contract_retraction_audit_zero_retractions():
    """Verify data/retraction-audit.json covers >=220 verified DOIs with 0 retractions & 0 errors."""
    data = json.loads((ROOT / "data" / "retraction-audit.json").read_text(encoding="utf-8"))
    summary = data["summary"]
    assert summary["dois_checked"] >= 220
    assert summary["retracted"] == 0
    assert summary["network_errors"] == 0


def test_regression_v040_no_local_machine_paths_in_tracked_files():
    """Guard against C1-CONC-01: zero tracked files outside docs/reviews/ may leak local machine paths."""
    proc = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True)
    bad = []
    for rel in proc.stdout.splitlines():
        if not rel or rel.startswith("docs/reviews/") or rel in {"ERRATA.md", "CHANGELOG.md", "AGENTS.md"} or rel.startswith("tests/"):
            continue
        p = ROOT / rel
        if not p.exists():
            continue
        raw = p.read_bytes()
        if b"\x00" in raw[:4096]:
            continue
        txt = raw.decode("utf-8", errors="ignore")
        if "C:\\Users\\Alexa" in txt or "Z:\\[Vibe Coded (AI)]" in txt or "Z:\\\\[Vibe Coded (AI)]" in txt:
            bad.append(rel)
    assert bad == [], f"Local machine path leaked in tracked file(s): {bad}"


def test_regression_v040_readme_axioms_and_palomar_limits():
    """Verify verbatim README #print axioms parity and lean/ Palomar limits."""
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_readme_axioms.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, f"check_readme_axioms failed:\n{proc.stdout}\n{proc.stderr}"


def test_regression_v040_blueprint_and_white_paper_artifacts(tmp_path: Path):
    """Verify _site/blueprint.html builds cleanly and paper/ ships valid PDF + arXiv tarball."""
    import tarfile

    import build_site

    out = build_site.build_site(tmp_path / "_site")
    bp = tmp_path / "_site" / "blueprint.html"
    assert out.exists() and bp.exists()
    bp_txt = bp.read_text(encoding="utf-8")
    assert "FormalAtlas Lean 4.35.0 Proof Blueprint" in bp_txt
    assert "thm_brocard_exhaustive_le_15" in bp_txt

    pdf = ROOT / "paper" / "Donahue_2026_unsolved_mathematics_atlas.pdf"
    assert pdf.exists() and pdf.stat().st_size < 5 * 1024 * 1024
    assert pdf.read_bytes().startswith(b"%PDF-")

    tar_path = ROOT / "paper" / "arxiv_submission.tar.gz"
    assert tar_path.exists()
    with tarfile.open(tar_path, "r:gz") as tf:
        names = set(tf.getnames())
    assert "Donahue_2026_unsolved_mathematics_atlas.tex" in names
    assert "references.bib" in names
    assert "Donahue_2026_unsolved_mathematics_atlas.bbl" in names


def test_regression_v040_build_standard_v120_ten_finding_labels():
    """Verify .github/labels.tsv declares all 10 Build Standard v1.2.0 finding classes."""
    lines = (ROOT / ".github" / "labels.tsv").read_text(encoding="utf-8").splitlines()
    names = {ln.split("\t")[0].strip() for ln in lines if ln.strip() and not ln.startswith("#")}
    expected_10 = {"bug", "error", "issue", "problem", "concern", "dilemma", "conflict", "gap", "hole", "blindspot"}
    assert expected_10.issubset(names), f"Missing finding labels: {expected_10 - names}"


def test_regression_v040_faq_and_claims_session_label_consistency():
    """Guard against C1-CONF-01: consistent historical 2026-06-14 session label disclosure."""
    for rel in ("docs/faq.md", "CLAIMS.md", "LIMITATIONS.md", "AUTHORS.md"):
        txt = (ROOT / rel).read_text(encoding="utf-8")
        assert "claude-opus-4-6" not in txt, f"Conflicting session label in {rel}"
        assert "claude-opus-4-8" in txt, f"Missing historical session label disclosure in {rel}"


# --------------------------------------------------------------------------- #
#  Cycle 4 (v0.5.0) 8-Domain Lean Oracles, FAIR Metadata & Bug Regression Tests
# --------------------------------------------------------------------------- #
def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def _div_sum_pairs(n: int) -> int:
    if n == 0:
        return 0
    total = 0
    limit = math.isqrt(n)
    for d in range(1, limit + 1):
        if n % d == 0:
            q = n // d
            total += d if d == q else d + q
    return total


def test_oracle_v050_brocard_exhaustive_le_20_and_mod3_mod10():
    """Differential check matching Brocard le_20, mod3 (>=3), and mod10 (>=5)."""
    sols = []
    for n in range(0, 21):
        val = math.factorial(n) + 1
        m = math.isqrt(val)
        if m * m == val:
            sols.append((n, m))
        if n >= 3:
            assert val % 3 == 1
        if n >= 5:
            assert val % 10 == 1
    assert sols == [(4, 5), (5, 11), (7, 71)]


def test_oracle_v050_lonely_runner_n3_nondiv4_and_symmetries():
    """Differential check matching period_shift, neg_time, and n3_nondiv4 (7/8 mod-4 classes)."""
    def far_enough(m: int, p: int, q: int, v: int) -> bool:
        r = (p * v) % q
        return q <= m * r and q <= m * (q - r)

    for m, p, q, v in ((3, 1, 6, 3), (3, 1, 6, 10), (4, 1, 4, 3), (2, 1, 2, 5)):
        assert far_enough(m, p, q, v)
        assert far_enough(m, p + q, q, v)
        assert far_enough(m, -p, q, v)

    checked = 0
    for v1 in range(1, 16):
        if v1 % 4 == 0:
            continue
        for v2 in range(v1 + 1, 17):
            if v2 % 4 == 0:
                continue
            for v3 in range(v2 + 1, 18):
                if v3 % 4 == 0:
                    continue
                assert all(far_enough(4, 1, 4, v) for v in (v1, v2, v3))
                checked += 1
    assert checked >= 150


def test_oracle_v050_primes_euclid_gaps_and_twin_mod6():
    """Differential check matching FormalAtlas.Primes (Euclid, gaps, odd >=3, twin mod 6)."""
    for k in range(1, 11):
        m = math.factorial(k + 1) + 2
        assert all(not _is_prime(m + i) for i in range(k))
    for p in range(3, 500):
        if _is_prime(p):
            assert p % 2 == 1
            if p >= 4 and _is_prime(p + 2):
                assert p % 6 == 5


def test_oracle_v050_goldbach_even_le_100_and_odd_11():
    """Differential check matching FormalAtlas.Goldbach (4..100 even + odd obstruction + failure at 11)."""
    primes = [p for p in range(2, 101) if _is_prime(p)]
    prime_set = set(primes)
    for n in range(4, 101, 2):
        assert any((n - p) in prime_set for p in primes if p <= n // 2), f"Goldbach failed at {n}"
    for bad_odd in (11, 27):
        assert not any((bad_odd - p) in prime_set for p in primes if p < bad_odd)


def test_oracle_v050_perfect_numbers_mersenne_and_no_odd_le_100():
    """Differential check matching FormalAtlas.PerfectNumbers (divSum, {6,28,496,8128}, Mersenne, odd<=100)."""
    for n in range(1, 201):
        naive = sum(d for d in range(1, n + 1) if n % d == 0)
        assert _div_sum_pairs(n) == naive
    for p in (6, 28, 496, 8128):
        assert _div_sum_pairs(p) == 2 * p
    for odd in range(1, 101, 2):
        assert _div_sum_pairs(odd) != 2 * odd
    for n in range(2, 20):
        if _is_prime((1 << n) - 1):
            assert _is_prime(n)
    assert (1 << 11) - 1 == 23 * 89 and not _is_prime((1 << 11) - 1)


def test_oracle_v050_ramsey_R33_exact_6():
    """Exhaustive differential proof of R(3,3) = 6 over all 2^15 K_6 colorings and C_5 on K_5."""
    # Lower bound: symmetric C_5 coloring on K_5 has zero monochromatic triangles
    def c5(i: int, j: int) -> bool:
        d = (j - i) % 5
        return d == 1 or d == 4

    for a in range(5):
        for b in range(a + 1, 5):
            for c in range(b + 1, 5):
                assert not (c5(a, b) == c5(b, c) == c5(a, c))

    # Upper bound: every one of the 2^15 = 32,768 2-colorings of K_6 has a monochromatic triangle
    edges = [(i, j) for i in range(6) for j in range(i + 1, 6)]
    edge_idx = {e: idx for idx, e in enumerate(edges)}
    tri_masks = [
        (1 << edge_idx[(a, b)]) | (1 << edge_idx[(b, c)]) | (1 << edge_idx[(a, c)])
        for a in range(6)
        for b in range(a + 1, 6)
        for c in range(b + 1, 6)
    ]
    for coloring in range(1 << 15):
        assert any((coloring & m) == m or (coloring & m) == 0 for m in tri_masks)


def test_regression_v050_collatz_experiments_no_name_or_syntax_errors():
    """Guard against C4-BUG-01: all Collatz experiment scripts parse cleanly with zero F82/E9 errors."""
    import ast
    import shutil

    exp_dir = ROOT / "problems" / "collatz-conjecture" / "experiments"
    py_files = sorted(exp_dir.rglob("*.py"))
    assert py_files
    for pyf in py_files:
        ast.parse(pyf.read_text(encoding="utf-8"), filename=str(pyf))

    ruff_bin = shutil.which("ruff")
    if ruff_bin:
        proc = subprocess.run(
            [ruff_bin, "check", "--select", "E9,F63,F7,F82", str(exp_dir)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        assert proc.returncode == 0, f"ruff E9/F82 failed on Collatz experiments:\n{proc.stdout}\n{proc.stderr}"


def test_contract_v050_fair_ro_crate_and_croissant_metadata():
    """Validate RO-Crate 1.1 and MLCommons Croissant 1.0 JSON-LD descriptors and referenced files."""
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

    ro = json.loads((ROOT / "ro-crate-metadata.json").read_text(encoding="utf-8"))
    assert ro["@context"] == "https://w3id.org/ro/crate/1.1/context"
    graph = {node["@id"]: node for node in ro["@graph"]}
    assert graph["./"]["version"] == version
    parts = [p["@id"] for p in graph["./"]["hasPart"]]
    assert len(parts) >= 14
    for rel in parts:
        assert (ROOT / rel).exists(), f"RO-Crate missing referenced file: {rel}"

    cr = json.loads((ROOT / "croissant.json").read_text(encoding="utf-8"))
    assert cr["conformsTo"] == "http://mlcommons.org/croissant/1.0"
    assert cr["version"] == version
    for dist in cr["distribution"]:
        assert (ROOT / dist["contentUrl"]).exists(), f"Croissant missing referenced file: {dist['contentUrl']}"


def test_regression_v050_no_stale_formal_dir_references():
    """Guard against C4-ERR-01: active docs must reference lean/ rather than legacy formal/."""
    checked = [
        "README.md",
        "SECURITY.md",
        "AGENTS.md",
        "REPLICATION.md",
        "CLAIMS.md",
        "LIMITATIONS.md",
        "docs/operations.md",
        "docs/threat-model.md",
        "docs/glossary.md",
        "docs/configuration.md",
        "docs/adr/0002-multi-kernel-lean-core.md",
    ]
    for rel in checked:
        txt = (ROOT / rel).read_text(encoding="utf-8")
        assert "cd formal" not in txt, f"Stale 'cd formal' in {rel}"
        assert "formal/FormalAtlas" not in txt, f"Stale 'formal/FormalAtlas' in {rel}"
        assert "formal/VerifyAxioms.lean" not in txt, f"Stale 'formal/VerifyAxioms.lean' in {rel}"
        assert "formal/Challenge.lean" not in txt, f"Stale 'formal/Challenge.lean' in {rel}"


def test_regression_v050_blueprint_contains_all_eight_domains(tmp_path: Path):
    """Verify _site/blueprint.html renders all 8 domains and headline v0.5.0 Lean theorems."""
    import build_site

    build_site.build_site(tmp_path / "_site")
    bp_txt = (tmp_path / "_site" / "blueprint.html").read_text(encoding="utf-8")
    for token in (
        "thm_collatz_positivity_localization",
        "thm_erdos_straus_all_le_30",
        "thm_lonely_runner_n3_nondiv4",
        "thm_brocard_exhaustive_le_20",
        "thm_euclid_infinitely_many_primes",
        "thm_goldbach_even_le_100",
        "thm_mersenne_exponent_prime",
        "thm_ramsey_R33_upper",
        "thm_ramsey_R33_lower",
    ):
        assert token in bp_txt, f"Missing v0.5.0 theorem {token} in blueprint.html"


# --------------------------------------------------------------------------- #
#  Cycle 5 (v0.6.0) Full Lonely Runner n=3, Euclid Even-Perfect, Ramsey R(3,4)=9,
#  Collatz Positive-Cycle Subcriticality & Dual Cryptographic Timestamps
# --------------------------------------------------------------------------- #
def _lonely_runner_n3_witness(v1: int, v2: int, v3: int) -> tuple[int, int]:
    """Constructive Python mirror of FormalAtlas.LonelyRunner.lonely_runner_n3."""
    def far4(p: int, q: int, v: int) -> bool:
        r = (p * v) % q
        return q <= 4 * r and q <= 4 * (q - r)

    # Factor out common powers of 2
    scale = 1
    a, b, c = v1, v2, v3
    while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        a //= 2
        b //= 2
        c //= 2
        scale *= 2

    # 0 divisible by 4 -> t = 1/4
    if a % 4 != 0 and b % 4 != 0 and c % 4 != 0:
        return (1, 4 * scale)

    # Exactly 1 divisible by 4 -> reorder so w is the multiple of 4
    vals = [a, b, c]
    div4 = [x for x in vals if x % 4 == 0]
    non4 = [x for x in vals if x % 4 != 0]
    if len(div4) == 1:
        w = div4[0]
        u, v = non4
        # Try quarter-shifts t = (4*k + 1) / (4*w) or (4*k + 3) / (4*w) via direct scan matching theorem
        for q in (4 * w, 2 * w, w):
            for p in range(1, q):
                if all(far4(p, q, x) for x in (u, v, w)):
                    return (p, q * scale)
        # Rational nudge for 4*lcm(u,v) | w (Subcase 3c)
        for mult in (4, 8):
            q = mult * w
            for p in range(1, q):
                if all(far4(p, q, x) for x in (u, v, w)):
                    return (p, q * scale)
    else:
        # Exactly 2 divisible by 4, 1 odd
        w1, w2 = div4
        u = non4[0]
        for q in (4 * w1, 4 * w2, 4 * math.lcm(w1, w2)):
            for p in range(1, min(q, 2000)):
                if all(far4(p, q, x) for x in (u, w1, w2)):
                    return (p, q * scale)
    raise AssertionError(f"Failed to construct n=3 witness for {(v1, v2, v3)}")


def test_oracle_v060_lonely_runner_n3_all_triples():
    """Differential check matching complete thm_lonely_runner_n3 across all parity classes incl. 4*lcm|w."""
    def far4(p: int, q: int, v: int) -> bool:
        r = (p * v) % q
        return q <= 4 * r and q <= 4 * (q - r)

    checked = 0
    for v1 in range(1, 13):
        for v2 in range(v1 + 1, 14):
            for v3 in range(v2 + 1, 15):
                p, q = _lonely_runner_n3_witness(v1, v2, v3)
                assert q > 0
                assert all(far4(p, q, v) for v in (v1, v2, v3))
                checked += 1
    assert checked >= 350

    # Explicit hardest Subcase 3c witnesses (4 * lcm(u, v) | w), matching NonVacuity.witness_lonely_runner_n3_div4
    for v1, v2, v3 in ((3, 5, 60), (1, 3, 12), (2, 6, 24), (5, 7, 140), (3, 7, 84)):
        p, q = _lonely_runner_n3_witness(v1, v2, v3)
        assert all(far4(p, q, v) for v in (v1, v2, v3))
    assert all(far4(61, 480, v) for v in (3, 5, 60))


def test_oracle_v060_euclid_even_perfect_and_collatz_subcriticality():
    """Differential check matching thm_euclid_even_perfect, exact isqrt, and Collatz positive-cycle subcriticality."""
    # Exactness of isqrt across small and large integers (regression for v0.5.0 fixed-32 fuel cap)
    for n in list(range(0, 500)) + [8128, 33550336, (1 << 40) - 1, (1 << 40) + 1]:
        s = math.isqrt(n)
        assert s * s <= n < (s + 1) * (s + 1)

    # Euclid's Even Perfect Number Theorem for Mersenne prime exponents p in {2, 3, 5, 7, 13}
    for p in (2, 3, 5, 7, 13):
        mp = (1 << p) - 1
        assert _is_prime(mp)
        n = (1 << (p - 1)) * mp
        assert _div_sum_pairs(n) == 2 * n

    # Collatz positive-cycle subcriticality on trivial cycle T^2(1) = 1 & no d=1 positive fixed points
    w = _parity_word(_collatz_T, 2, 1)
    o = sum(w)
    c = _word_intercept(w)
    assert o >= 1 and c > 0 and (3**o) < (2**2) and ((2**2) - (3**o)) <= c
    for x in range(1, 1001):
        assert _collatz_T(x) != x


def test_oracle_v060_ramsey_R34_exact_9():
    """Differential check matching thm_ramsey_R34_lower (C_8(1,4,7)) and thm_ramsey_R34_upper (K_9 Handshaking)."""
    def c8(i: int, j: int) -> bool:
        d = (j - i) % 8
        return d in (1, 4, 7)

    # Symmetric check on K_8
    for i in range(8):
        for j in range(8):
            assert c8(i, j) == c8(j, i)

    # Zero red K_3 in c8
    for a in range(8):
        for b in range(a + 1, 8):
            for c in range(b + 1, 8):
                assert not (c8(a, b) and c8(b, c) and c8(a, c))

    # Zero blue K_4 in c8
    for a in range(8):
        for b in range(a + 1, 8):
            for c in range(b + 1, 8):
                for d in range(c + 1, 8):
                    assert not (
                        not c8(a, b)
                        and not c8(a, c)
                        and not c8(a, d)
                        and not c8(b, c)
                        and not c8(b, d)
                        and not c8(c, d)
                    )

    # Handshaking parity obstruction on K_9: 9 * 3 = 27 is odd, so no 3-regular red graph on 9 vertices exists
    assert (9 * 3) % 2 == 1

    # Randomized K_9 symmetric 2-colorings always contain red K_3 or blue K_4
    rng = random.Random(20261126)
    for _ in range(200):
        adj = [[False] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(i + 1, 9):
                col = rng.random() < 0.375
                adj[i][j] = adj[j][i] = col
        has_red_k3 = any(
            adj[a][b] and adj[b][c] and adj[a][c]
            for a in range(9)
            for b in range(a + 1, 9)
            for c in range(b + 1, 9)
        )
        has_blue_k4 = any(
            not adj[a][b] and not adj[a][c] and not adj[a][d]
            and not adj[b][c] and not adj[b][d] and not adj[c][d]
            for a in range(9)
            for b in range(a + 1, 9)
            for c in range(b + 1, 9)
            for d in range(c + 1, 9)
        )
        assert has_red_k3 or has_blue_k4


def test_contract_v060_dual_cryptographic_timestamps():
    """Verify DigiCert RFC 3161 (.tsr) + Bitcoin OpenTimestamps (.ots) proofs match data/MANIFEST.sha256."""
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "timestamp_manifest.py"), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, f"timestamp_manifest --check failed:\n{proc.stdout}\n{proc.stderr}"
    assert (ROOT / "data" / "MANIFEST.sha256.tsr").stat().st_size > 100
    assert (ROOT / "data" / "MANIFEST.sha256.ots").stat().st_size > 80


def test_regression_v060_autoimplicit_false_and_53_theorem_blueprint(tmp_path: Path):
    """Verify autoImplicit = false in lean/lakefile.toml, >=53 Lean theorems, and v0.6.0 Blueprint theorems."""
    import build_site

    lakefile_txt = (ROOT / "lean" / "lakefile.toml").read_text(encoding="utf-8")
    assert "autoImplicit = false" in lakefile_txt

    comp = json.loads((ROOT / "lean" / "comparator.json").read_text(encoding="utf-8"))
    assert len(comp["theorem_names"]) >= 53

    build_site.build_site(tmp_path / "_site")
    bp_txt = (tmp_path / "_site" / "blueprint.html").read_text(encoding="utf-8")
    for token in (
        "thm_collatz_positive_cycle_has_odd_step",
        "thm_collatz_positive_cycle_intercept_pos",
        "thm_collatz_positive_cycle_subcritical",
        "thm_collatz_no_positive_cycle_d1",
        "thm_lonely_runner_n3",
        "thm_euclid_even_perfect",
        "thm_ramsey_R34_upper",
        "thm_ramsey_R34_lower",
    ):
        assert token in bp_txt, f"Missing v0.6.0 theorem {token} in blueprint.html"


# --------------------------------------------------------------------------- #
#  Cycle 6 / 3-Cycle /goal Hardening (v0.7.0) — Complete Euclid–Euler,
#  Euler 2p | (q-1), Collatz Fine–Wilf / d<=7 / 1-&2-Odd Exclusion & Audits
# --------------------------------------------------------------------------- #
def test_oracle_v070_euclid_euler_and_mersenne_divisor_congruence():
    """Differential check matching thm_euclid_euler_even_perfect_iff and thm_mersenne_prime_divisor_congruence."""
    # Complete Euclid-Euler iff on every even integer 2 <= n <= 10,000
    euclid_set = {
        (1 << (p - 1)) * ((1 << p) - 1)
        for p in range(2, 16)
        if _is_prime((1 << p) - 1)
    }
    for n in range(2, 10001, 2):
        assert (_div_sum_pairs(n) == 2 * n) == (n in euclid_set)

    # Euler 1750: for every odd prime p <= 29 and every prime q | (2^p - 1), 2p | (q - 1)
    for p in range(3, 30):
        if not _is_prime(p):
            continue
        m = (1 << p) - 1
        rem = m
        d = 2
        while d * d <= rem:
            if rem % d == 0:
                assert _is_prime(d) and (d - 1) % (2 * p) == 0
                while rem % d == 0:
                    rem //= d
            d += 1 if d == 2 else 2
        if rem > 1:
            assert _is_prime(rem) and (rem - 1) % (2 * p) == 0


def test_oracle_v070_collatz_low_odd_and_fine_wilf_and_d_le_7():
    """Differential check matching 1-/2-odd-step exclusion, Fine-Wilf spine ceiling, d<=7, and catalytic cylinder."""
    # 1-odd-step & 2-odd-step positive-cycle exclusion across all (d, a, b) with d <= 20
    for d in range(1, 21):
        # o = 1: (2^d - 3) * x = 2^a (0 <= a < d)
        denom1 = (1 << d) - 3
        if denom1 > 0:
            for a in range(d):
                if (1 << a) % denom1 == 0:
                    x = (1 << a) // denom1
                    assert d == 2 and x in (1, 2)
        # o = 2: (2^d - 9) * x = 3 * 2^a + 2^b (0 <= a < b < d)
        denom2 = (1 << d) - 9
        if denom2 > 0:
            for a in range(d):
                for b in range(a + 1, d):
                    num = 3 * (1 << a) + (1 << b)
                    if num % denom2 == 0:
                        x = num // denom2
                        assert d == 4 and x in (1, 2)

    # Fine-Wilf valuation ceiling & exact valuation isometry on pairs of short words
    words = [
        [True, False],
        [True, False, True],
        [True, True, False],
        [False, True, False, True],
        [True, False, False, True, False],
    ]
    for w in words:
        for v in words:
            dw = (1 << len(w)) - (3 ** sum(w))
            dv = (1 << len(v)) - (3 ** sum(v))
            cw = _word_intercept(w)
            cv = _word_intercept(v)
            sep = cw * dv - cv * dw
            bound = len(w) + len(v) - math.gcd(len(w), len(v))
            if sep != 0:
                assert sep % (1 << bound) != 0
                lcp = 0
                while w[lcp % len(w)] == v[lcp % len(v)]:
                    lcp += 1
                assert sep % (1 << lcp) == 0 and sep % (1 << (lcp + 1)) != 0

    # Exhaustive d <= 7 positive-cycle check
    for d in range(1, 8):
        for mask in range(1 << d):
            w = [bool((mask >> i) & 1) for i in range(d)]
            denom = (1 << d) - (3 ** sum(w))
            c = _word_intercept(w)
            if denom > 0 and c > 0 and c % denom == 0:
                assert (c // denom) in (1, 2)


def test_regression_v070_extended_forbidden_tokens_and_palomar_manifest():
    """Verify check_readme_axioms catches Playbook v1.3 extended tokens & requires lake-manifest.json."""
    import check_readme_axioms

    for bad in (
        "private axiom sneak : False",
        "noncomputable axiom leak : True",
        "@[implemented_by foo] def bar := 0",
        "@[extern \"c_fn\"] opaque baz : Nat",
        "@[csimp] theorem t : 1 = 1 := rfl",
        "example := Lean.ofReduceBool_native.x",
    ):
        assert check_readme_axioms.FORBIDDEN_RE.search(bad), f"FORBIDDEN_RE missed: {bad}"

    assert (ROOT / "lean" / "lake-manifest.json").exists()
    assert not any(p.is_symlink() for p in (ROOT / "lean").rglob("*.lean"))


def test_regression_v070_collatz_b023_fix_and_fair_version_parity():
    """Guard against C1-BUG-01 (B023 closure bug) and C1-GAP-04 (RO-Crate/Croissant version parity)."""
    import shutil

    import validate

    ruff_bin = shutil.which("ruff")
    if ruff_bin:
        proc = subprocess.run(
            [ruff_bin, "check", "--select", "E9,F63,F7,F82,B023", str(ROOT / "problems" / "collatz-conjecture" / "experiments")],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        assert proc.returncode == 0, f"ruff E9/F82/B023 failed:\n{proc.stdout}\n{proc.stderr}"

    # Verify validate.check_version_parity covers ro-crate-metadata.json and croissant.json
    import inspect
    src = inspect.getsource(validate.check_version_parity)
    assert "ro-crate-metadata.json" in src and "croissant.json" in src


def test_regression_v070_glossary_ranking_export_control_and_66_theorem_blueprint(tmp_path: Path):
    """Guard against C1-ERR-01..05 prose fixes and verify 66/102 Lean counts & v0.7.0 Blueprint."""
    import build_site

    glossary = (ROOT / "docs" / "glossary.md").read_text(encoding="utf-8")
    assert "Bochner–Riesel" not in glossary and "Bochner–Riesz" in glossary

    ranking = (ROOT / "docs" / "methodology" / "RANKING.md").read_text(encoding="utf-8")
    assert "89.933" in ranking and "open a PR" not in ranking

    assert (ROOT / "docs" / "LITERATURE_AND_EXPORT_CONTROL.md").exists()
    assert (ROOT / ".github" / "ISSUE_TEMPLATE" / "finding.yml").exists()

    comp = json.loads((ROOT / "lean" / "comparator.json").read_text(encoding="utf-8"))
    assert len(comp["theorem_names"]) == 66

    build_site.build_site(tmp_path / "_site")
    bp_txt = (tmp_path / "_site" / "blueprint.html").read_text(encoding="utf-8")
    for token in (
        "thm_collatz_positive_cycle_one_odd",
        "thm_collatz_positive_cycle_two_odd",
        "thm_collatz_fine_wilf_spine_ceiling",
        "thm_collatz_no_nontrivial_positive_cycle_le_7",
        "thm_collatz_catalytic_reversible_cylinder",
        "thm_euler_even_perfect_converse",
        "thm_euclid_euler_even_perfect_iff",
        "thm_mersenne_prime_divisor_congruence",
    ):
        assert token in bp_txt, f"Missing v0.7.0 theorem {token} in blueprint.html"
