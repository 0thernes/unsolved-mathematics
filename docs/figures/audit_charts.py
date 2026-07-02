#!/usr/bin/env python3
"""Dependency-free SVG charts for the 2026-07-02 repo audit.
fig_a: repo composition by top-level directory (bytes, log10 scale)
fig_b: collatz experiments composition (file counts by class)
fig_c: 25-point audit scorecard (0-10 bars, banded colors)
Run: python docs/figures/audit_charts.py
"""
import math
from pathlib import Path

OUT = Path(__file__).parent
W = 760


def header(h, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" '
            f'font-family="Georgia, serif" font-size="12">'
            f'<rect width="{W}" height="{h}" fill="white"/>'
            f'<text x="{W/2}" y="20" text-anchor="middle" font-size="14" font-weight="bold">{title}</text>')


def hbars(rows, h, title, xmax, fmt, colors=None, x0=200):
    s = header(h, title)
    bh, gap, y = 20, 8, 40
    for i, (label, val) in enumerate(rows):
        w = max(2, (W - x0 - 30) * val / xmax)
        c = (colors[i] if colors else '#2c3e50')
        s += (f'<text x="{x0-8}" y="{y+14}" text-anchor="end">{label}</text>'
              f'<rect x="{x0}" y="{y}" width="{w:.1f}" height="{bh}" fill="{c}"/>'
              f'<text x="{x0+w+6:.1f}" y="{y+14}" font-size="11">{fmt(val)}</text>')
        y += bh + gap
    return s + '</svg>'


# fig_a — repo composition (log10 bytes)
dirs = [('problems', 10_634_999), ('rag', 4_361_280), ('meta-analyses', 1_449_405),
        ('docs', 204_802), ('data', 191_280), ('(root files)', 72_257),
        ('scripts', 33_023), ('.github', 8_277), ('schema', 5_071), ('tests', 1_828)]
rows = [(k, math.log10(v)) for k, v in dirs]
raw = dict(dirs)
fig = hbars([(k, v) for k, v in rows], 40 + len(rows) * 28 + 20,
            'Repository composition by top-level directory (log10 bytes; labels show raw size)',
            8.0, lambda v: f"{raw[[k for k,_ in rows][[v2 for _,v2 in rows].index(v)]]:,} B")
(OUT / 'fig_a_repo_composition.svg').write_text(fig, encoding='utf-8')

# fig_b — collatz experiments composition
comp = [('instrument scripts (.py)', 92), ('research/audit docs (.md)', 68),
        ('results artifacts (.json)', 134), ('quarantined claims', 19),
        ('stray scripts (relocated)', 3)]
colors_b = ['#2c3e50', '#2980b9', '#7f8c8d', '#c0392b', '#e67e22']
fig = hbars(comp, 40 + len(comp) * 28 + 20,
            'problems/collatz-conjecture/experiments — composition (2026-07-02)',
            140, lambda v: str(int(v)), colors_b)
(OUT / 'fig_b_experiments_composition.svg').write_text(fig, encoding='utf-8')

# fig_c — 25-point scorecard
SCORES = [
    ('1 Repo structure & modularity', 8), ('2 Naming & org consistency', 6),
    ('3 Documentation coverage', 9), ('4 Code health (parse/syntax)', 9),
    ('5 Code duplication', 4), ('6 Test coverage', 3),
    ('7 CI/CD pipelines', 7), ('8 Local reproducibility', 6),
    ('9 Data hygiene (results sprawl)', 5), ('10 Artifact provenance', 7),
    ('11 Staleness / synchronization', 6), ('12 Version-control discipline', 4),
    ('13 Kanban / status tooling', 7), ('14 Schema & validation gates', 8),
    ('15 RAG pipeline health', 5), ('16 Citation integrity', 9),
    ('17 Math verification depth', 9), ('18 Claim containment process', 6),
    ('19 External review integration', 9), ('20 Licensing & attribution', 9),
    ('21 Secrets / security hygiene', 8), ('22 Instrument efficiency', 8),
    ('23 Scalability', 6), ('24 PM maturity (PRD/process)', 7),
    ('25 Collatz-pursuit fitness', 9),
]


def band(v):
    return '#c0392b' if v <= 4 else ('#e67e22' if v <= 6 else '#27ae60')


h = 40 + len(SCORES) * 22 + 30
s = header(h, 'Audit scorecard — 25 dimensions, 0-10 (total 174/250 = 69.6%)')
y = 36
for label, v in SCORES:
    w = (W - 260 - 60) * v / 10
    s += (f'<text x="252" y="{y+11}" text-anchor="end" font-size="10.5">{label}</text>'
          f'<rect x="260" y="{y}" width="{w:.0f}" height="14" fill="{band(v)}"/>'
          f'<rect x="260" y="{y}" width="{W-260-60}" height="14" fill="none" stroke="#ccc" stroke-width="0.5"/>'
          f'<text x="{260+(W-260-60)+6}" y="{y+11}" font-size="10.5">{v}</text>')
    y += 22
(OUT / 'fig_c_scorecard.svg').write_text(s + '</svg>', encoding='utf-8')
print('wrote fig_a, fig_b, fig_c')
