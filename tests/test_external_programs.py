# SPDX-License-Identifier: MIT
"""Offline tests for scripts/sync_external_programs.py and scripts/search_all_problems.py (no network)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import search_all_problems as sap  # noqa: E402
import sync_external_programs as sx  # noqa: E402

CARD_HTML = (
    '<main><a href="/programs/Erd%C5%91s%20Problems" class="rec" style="text-decoration:none">'
    '<div class="k"><span class="dot"></span> <!-- -->70<!-- --> live</div>'
    '<div style="font-weight:650;font-size:1.1rem">Erdős Problems</div>'
    '<div style="color:var(--muted);font-size:.88rem">Paul Erdős&#x27;s problems, many with cash prizes.</div>'
    '<div class="diff">2068<!-- --> targets · <!-- -->837<!-- --> open · <!-- -->602<!-- --> solved here</div></a>'
    '<a href="/programs/Green&#x27;s%20100%20Open%20Problems" class="rec" style="text-decoration:none">'
    '<div class="k">front</div><div style="font-weight:650;font-size:1.1rem">Green&#x27;s 100 Open Problems</div>'
    '<div style="color:var(--muted);font-size:.88rem">Ben Green&#x27;s list.</div>'
    '<div class="diff">285<!-- --> targets · <!-- -->128<!-- --> open · <!-- -->67<!-- --> solved here</div></a></main>'
)


def test_parse_programs_html_extracts_cards_and_ignores_live_counter() -> None:
    progs = sx.parse_programs_html(CARD_HTML)
    assert [p["name"] for p in progs] == ["Erdős Problems", "Green's 100 Open Problems"]
    assert progs[0]["slug"] == "erdos-problems"
    assert (progs[0]["targets"], progs[0]["open"], progs[0]["solved_here"]) == (2068, 837, 602)
    assert progs[1]["description"] == "Ben Green's list."
    assert all("live" not in p for p in progs)


def test_normalize_item_drops_volatile_and_licensed_fields() -> None:
    raw = {"id": "X.y", "title": "T", "kind": "open", "fields": ["B", "A"], "prize": None, "solved": 0,
           "excerpt": "CC BY-SA text", "liveAgents": 3, "claimed": True, "difficulty": 70}
    item = sx.normalize_item(raw)
    assert set(item) == set(sx.ITEM_FIELDS)
    assert item["fields"] == ["A", "B"] and item["solved"] is False


def test_norm_title_and_generic_strip() -> None:
    assert sx.norm_title("The Collatz Conjecture") == "collatz conjecture"
    assert sx.strip_generic(sx.norm_title("Goldbach's Conjecture")) == "goldbach"
    assert sx.norm_title("Erdős–Straus Conjecture") == "erdos straus conjecture"


def test_shard_jsonl_splits_cleanly_under_cap() -> None:
    rows = [{"id": f"id-{i:04d}", "title": "x" * 100, "kind": "unformalized", "fields": [], "prize": None, "solved": False} for i in range(40)]
    shards = sx.shard_jsonl_lines("big-prog", rows, max_bytes=1200)
    assert len(shards) >= 4
    assert all(name.startswith("big-prog.part-") and name.endswith(".jsonl") for name, _ in shards)
    assert all(len(body.encode("utf-8")) <= 1200 for _, body in shards)
    reconstructed = [json.loads(ln) for _, body in shards for ln in body.splitlines()]
    assert reconstructed == rows


def test_summarize_rows_disaggregates_solved_by_kind() -> None:
    rows = [
        {"id": "a", "title": "A", "kind": "open", "fields": [], "prize": None, "solved": False},
        {"id": "b", "title": "B", "kind": "known", "fields": [], "prize": None, "solved": True},
        {"id": "c", "title": "C", "kind": "warmup", "fields": [], "prize": None, "solved": True},
        {"id": "d", "title": "D", "kind": "unformalized", "fields": [], "prize": None, "solved": False},
    ]
    kinds, sbk = sx.summarize_rows(rows)
    assert kinds == {"open": 1, "known": 1, "warmup": 1, "unformalized": 1, "other": 0}
    assert sbk == {"open": 0, "known": 1, "warmup": 1, "unformalized": 0, "other": 0}
    assert sx.format_solved_by_kind(sbk) == "known: 1, warmup: 1"


def _fixture_snapshot() -> tuple[dict, dict]:
    items = {"wikipedia": [
        {"id": "CollatzConjecture.collatz_conjecture", "title": "Collatz conjecture", "kind": "open",
         "fields": ["Number Theory"], "prize": None, "solved": False},
        {"id": "Kakeya.kakeya_3d", "title": "Kakeya problem — kakeya 3d", "kind": "known",
         "fields": [], "prize": None, "solved": False},
        {"id": "Foo.bar", "title": "Union-closed sets conjecture", "kind": "known",
         "fields": [], "prize": None, "solved": True},
        {"id": "Beal.claimed", "title": "Beal conjecture", "kind": "open",
         "fields": [], "prize": None, "solved": True},
    ]}
    snap = {"programs": [{"name": "Wikipedia", "slug": "wikipedia"}], "upstream": {"commit": "abc"}}
    return snap, items


def test_crosswalk_rule_primary_variant_and_signals() -> None:
    snap, items = _fixture_snapshot()
    problems = [
        {"slug": "collatz-conjecture", "title": "The Collatz Conjecture", "status": "open"},
        {"slug": "union-closed-sets-conjecture", "title": "Union-Closed Sets Conjecture", "status": "open"},
        {"slug": "kakeya-conjecture", "title": "Kakeya Problem", "status": "recently-resolved"},
        {"slug": "beal-conjecture", "title": "Beal Conjecture", "status": "open"},
    ]
    cw = sx.build_crosswalk(snap, items, problems, {"include": {}, "exclude": {}})
    rows = {r["slug"]: r for r in cw["problems"]}
    assert [m["id"] for m in rows["collatz-conjecture"]["matches"]] == ["CollatzConjecture.collatz_conjecture"]
    assert rows["collatz-conjecture"]["signals"] == []
    uc = rows["union-closed-sets-conjecture"]
    assert uc["matches"][0]["relation"] == "primary"
    assert len(uc["signals"]) == 1 and "`known`" in uc["signals"][0]
    assert any("unverified third-party" in s for s in rows["beal-conjecture"]["signals"])
    assert rows["kakeya-conjecture"]["matches"][0]["relation"] == "variant"


def test_crosswalk_override_relation_and_related_never_signals() -> None:
    snap, items = _fixture_snapshot()
    problems = [{"slug": "beal-conjecture", "title": "Beal Conjecture", "status": "open"}]
    cw = sx.build_crosswalk(snap, items, problems,
                            {"include": {"beal-conjecture": [{"id": "Beal.claimed", "relation": "related"}]}, "exclude": {}})
    row = cw["problems"][0]
    assert row["matches"][0]["relation"] == "related" and row["signals"] == []
    with pytest.raises(ValueError):
        sx.build_crosswalk(snap, items, problems,
                           {"include": {"beal-conjecture": [{"id": "Beal.claimed", "relation": "bogus"}]}, "exclude": {}})


def test_crosswalk_overrides_validated() -> None:
    snap, items = _fixture_snapshot()
    problems = [{"slug": "collatz-conjecture", "title": "The Collatz Conjecture", "status": "open"}]
    with pytest.raises(ValueError):
        sx.build_crosswalk(snap, items, problems, {"include": {"no-such-slug": []}, "exclude": {}})
    with pytest.raises(ValueError):
        sx.build_crosswalk(snap, items, problems, {"include": {"collatz-conjecture": ["Missing.id"]}, "exclude": {}})
    cw = sx.build_crosswalk(snap, items, problems,
                            {"include": {}, "exclude": {"collatz-conjecture": ["CollatzConjecture.collatz_conjecture"]}})
    assert cw["problems"][0]["matches"] == []


def test_content_hash_is_order_independent_over_programs_dict_keys() -> None:
    snap, items = _fixture_snapshot()
    h1 = sx.content_hash(snap, items)
    h2 = sx.content_hash(dict(reversed(list(snap.items()))), dict(items))
    assert h1 == h2 and len(h1) == 64


def test_committed_snapshot_passes_offline_check_and_full_coverage() -> None:
    if not sx.SNAPSHOT.exists():
        pytest.skip("no committed snapshot")
    assert sx.cmd_check() == 0
    snap = json.loads(sx.SNAPSHOT.read_text(encoding="utf-8"))
    assert snap["totals"]["mirrored_items"] == snap["totals"]["api_total"]
    assert snap["totals"]["mirrored_items"] >= 50000
    assert all(p["mirrored"] for p in snap["programs"])


def test_committed_snapshot_respects_no_excerpts_and_5mb_cap() -> None:
    if not sx.SNAPSHOT.exists():
        pytest.skip("no committed snapshot")
    for f in sx.ITEMS_DIR.glob("*.jsonl"):
        assert f.stat().st_size < 5 * 1024 * 1024
        with f.open("r", encoding="utf-8") as fh:
            first_line = fh.readline()
            if first_line.strip():
                assert "excerpt" not in json.loads(first_line)


def test_unified_search_hits_both_curated_atlas_and_all_59k_external() -> None:
    if not sx.SNAPSHOT.exists():
        pytest.skip("no committed snapshot")
    atlas_hits = sap.search_atlas(query="Collatz", limit=5)
    assert any(h["id"] == "collatz-conjecture" for h in atlas_hits)
    ext_hits = sap.search_external(query="Collatz", limit=10)
    assert any(h["id"] == "CollatzConjecture.collatz_conjecture" for h in ext_hits)
    mo_hits = sap.search_external(program="MathOverflow (not formalized)", query="Riemann", limit=5)
    assert len(mo_hits) >= 1
    oeis_hits = sap.search_external(program="OEIS conjectures (not formalized)", query="Mersenne", limit=5)
    assert len(oeis_hits) >= 1
