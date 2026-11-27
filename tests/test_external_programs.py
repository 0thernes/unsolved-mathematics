# SPDX-License-Identifier: MIT
"""Offline tests for scripts/sync_external_programs.py (no network)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

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
    # known primary -> status signal; a site-solved flag on a *known* statement is formalization, not a signal
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


def test_committed_snapshot_passes_offline_check() -> None:
    if not sx.SNAPSHOT.exists():
        pytest.skip("no committed snapshot")
    assert sx.cmd_check() == 0


def test_committed_snapshot_respects_licensing_policy() -> None:
    if not sx.SNAPSHOT.exists():
        pytest.skip("no committed snapshot")
    snap = json.loads(sx.SNAPSHOT.read_text(encoding="utf-8"))
    for p in snap["programs"]:
        if p["name"] in sx.COUNTS_ONLY_PROGRAMS:
            assert p["mirrored"] is False
            assert not (sx.ITEMS_DIR / f"{p['slug']}.jsonl").exists()
    for f in sx.ITEMS_DIR.glob("*.jsonl"):
        for line in f.read_text(encoding="utf-8").splitlines():
            assert "excerpt" not in json.loads(line)
