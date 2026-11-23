"""Hypothesis property-based & numeric-stability tests (Build Standard B10 & B20)."""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

ROOT = Path(__file__).resolve().parent.parent
for _p in (ROOT, ROOT / "scripts", ROOT / "rag"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import build_corpus  # noqa: E402
import generate  # noqa: E402


def _T(x: int) -> int:
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def _word_intercept(w: list[bool]) -> int:
    if not w:
        return 0
    b, *ws = w
    if not b:
        return 2 * _word_intercept(ws)
    return (3 ** sum(ws)) + 2 * _word_intercept(ws)


@given(
    difficulty=st.integers(min_value=0, max_value=100),
    centrality=st.integers(min_value=0, max_value=100),
    tractability=st.integers(min_value=0, max_value=100),
    year_posed=st.integers(min_value=-500, max_value=2026),
)
@settings(max_examples=120, deadline=None)
def test_property_css_bounded_finite_and_monotone(
    difficulty: int, centrality: int, tractability: int, year_posed: int
):
    p = {
        "slug": "prop-test",
        "difficulty": difficulty,
        "centrality": centrality,
        "tractability": tractability,
        "year_posed": year_posed,
    }
    score = generate.composite_severity(p)
    assert math.isfinite(score)
    assert 0.0 <= score <= 100.0
    if difficulty < 100:
        assert generate.composite_severity({**p, "difficulty": difficulty + 1}) >= score
    if centrality < 100:
        assert generate.composite_severity({**p, "centrality": centrality + 1}) >= score
    if tractability > 0:
        assert generate.composite_severity({**p, "tractability": tractability - 1}) >= score


@given(
    x=st.integers(min_value=-10_000, max_value=100_000),
    d=st.integers(min_value=0, max_value=14),
)
@settings(max_examples=150, deadline=None)
def test_property_collatz_exact_affine_identity(x: int, d: int):
    """Exact integer affine identity 2^d * T^d(x) = 3^k * x + c(w) holds for ALL integers x."""
    cur = x
    w: list[bool] = []
    for _ in range(d):
        w.append((cur % 2) != 0)
        cur = _T(cur)
    k = sum(w)
    assert (2**d) * cur == (3**k) * x + _word_intercept(w)


@given(
    v1=st.integers(min_value=1, max_value=80),
    delta=st.integers(min_value=1, max_value=80),
)
@settings(max_examples=100, deadline=None)
def test_property_lonely_runner_n2_exact_rational_witness(v1: int, delta: int):
    """Exact rational Lonely Runner property for n=2: any v1 < v2 admits t with min ||t*v_i|| >= 1/3."""
    v2 = v1 + delta

    def cdist(val: Fraction) -> Fraction:
        f = val - math.floor(val)
        return min(f, 1 - f)

    # Check constructive candidate times matching standard n=2 proof (multiples of 1/(3*v1), 1/(3*v2), 1/(v1+v2))
    candidates = [Fraction(1, 3 * v1), Fraction(2, 3 * v1), Fraction(1, 3 * v2), Fraction(2, 3 * v2)]
    for k in range(1, min(2 * v2, 60)):
        candidates.append(Fraction(k, 3 * v2))
        candidates.append(Fraction(k, 3 * v1))
    assert any(
        cdist(t * v1) >= Fraction(1, 3) and cdist(t * v2) >= Fraction(1, 3)
        for t in candidates
    ), f"Failed Lonely Runner n=2 for ({v1}, {v2})"


@given(
    headings=st.lists(
        st.tuples(
            st.text(alphabet="abcdefghijklmnopqrstuvwxyz ", min_size=1, max_size=24),
            st.text(alphabet="abcdefghijklmnopqrstuvwxyz0123456789 \n", min_size=1, max_size=200),
        ),
        min_size=1,
        max_size=8,
    )
)
@settings(max_examples=80, deadline=None)
def test_property_split_and_window_deterministic(headings: list[tuple[str, str]]):
    md = "\n\n".join(f"## {h.strip() or 'sec'}\n\n{b.strip() or 'body'}" for h, b in headings)
    b1 = build_corpus.split_by_heading(md)
    b2 = build_corpus.split_by_heading(md)
    assert b1 == b2
    for _, body in b1:
        chunks = build_corpus.window(body)
        assert chunks
        for c in chunks:
            assert build_corpus.count_tokens(c) >= 1
