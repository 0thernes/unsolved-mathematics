"""
Smoke + invariant tests for the Atlas build.
Run: python -m pytest -q   (or simply: python tests/test_atlas.py)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import generate  # noqa: E402


def load():
    return generate.yaml.safe_load(generate.REGISTRY_YAML.read_text(encoding="utf-8"))


def test_registry_parses_and_validates():
    data = load()
    errors = [e for e in generate.validate(data["problems"]) if not e.startswith("WARN")]
    assert errors == [], errors


def test_slugs_unique():
    slugs = [p["slug"] for p in load()["problems"]]
    assert len(slugs) == len(set(slugs))


def test_css_monotonic_ranking():
    problems = load()["problems"]
    ranked = sorted(problems, key=generate.composite_severity, reverse=True)
    scores = [generate.composite_severity(p) for p in ranked]
    assert scores == sorted(scores, reverse=True)


def test_age_score_bounds():
    assert generate.age_score(-300) == 100.0          # ancient saturates
    assert generate.age_score(2025) == 0.0            # current year
    assert 0 <= generate.age_score(1859) <= 100


def test_riemann_is_top_tier():
    problems = load()["problems"]
    ranked = sorted(problems, key=generate.composite_severity, reverse=True)
    top5 = {p["slug"] for p in ranked[:5]}
    assert "riemann-hypothesis" in top5


def test_scores_in_range():
    for p in load()["problems"]:
        for k in ("difficulty", "centrality", "tractability"):
            assert 0 <= p[k] <= 100, (p["slug"], k, p[k])


if __name__ == "__main__":
    n = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"ok  {name}")
            n += 1
    print(f"\n{n} tests passed.")
