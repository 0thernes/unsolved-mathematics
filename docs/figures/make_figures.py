#!/usr/bin/env python3
"""Dependency-free SVG figures for the Collatz multi-model white paper.
Figure 1: exact certificate-frontier density S(d)/2^d (odd-count DP, exact
integers) vs the proved entropy bound 2^{-(1-H(theta))d}  [Theorem C].
Figure 2: total-stopping-time records (measured 2026-07-01, N<=5e6) vs the
stochastic-model mean slope 2/ln(4/3) and the Lagarias-Weiss limsup 41.677647.
Run:  python docs/figures/make_figures.py
"""
import math
from pathlib import Path

OUT = Path(__file__).parent
W, H_PX, ML, MR, MT, MB = 720, 430, 62, 16, 34, 46


def svg_header(title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H_PX}" '
            f'font-family="Georgia, serif" font-size="12">'
            f'<rect width="{W}" height="{H_PX}" fill="white"/>'
            f'<text x="{W/2}" y="20" text-anchor="middle" font-size="14" font-weight="bold">{title}</text>')


def axes(x0, x1, y0, y1, xlab, ylab, xticks, yticks, ylog=False):
    px = lambda x: ML + (x - x0) / (x1 - x0) * (W - ML - MR)
    py = lambda y: H_PX - MB - (y - y0) / (y1 - y0) * (H_PX - MT - MB)
    s = f'<line x1="{ML}" y1="{H_PX-MB}" x2="{W-MR}" y2="{H_PX-MB}" stroke="black"/>'
    s += f'<line x1="{ML}" y1="{MT}" x2="{ML}" y2="{H_PX-MB}" stroke="black"/>'
    for xv, lab in xticks:
        s += (f'<line x1="{px(xv)}" y1="{H_PX-MB}" x2="{px(xv)}" y2="{H_PX-MB+4}" stroke="black"/>'
              f'<text x="{px(xv)}" y="{H_PX-MB+17}" text-anchor="middle">{lab}</text>')
    for yv, lab in yticks:
        s += (f'<line x1="{ML-4}" y1="{py(yv)}" x2="{ML}" y2="{py(yv)}" stroke="black"/>'
              f'<text x="{ML-7}" y="{py(yv)+4}" text-anchor="end">{lab}</text>'
              f'<line x1="{ML}" y1="{py(yv)}" x2="{W-MR}" y2="{py(yv)}" stroke="#ddd" stroke-dasharray="2,3"/>')
    s += f'<text x="{(ML+W-MR)/2}" y="{H_PX-8}" text-anchor="middle">{xlab}</text>'
    s += (f'<text x="16" y="{(MT+H_PX-MB)/2}" text-anchor="middle" '
          f'transform="rotate(-90 16 {(MT+H_PX-MB)/2})">{ylab}</text>')
    return s, px, py


def polyline(pts, px, py, color, dash=None, width=1.6):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    p = " ".join(f"{px(x):.1f},{py(y):.1f}" for x, y in pts)
    return f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{width}"{d}/>'


def fig1():
    surv, depths, log10dens = {0: 1}, [], []
    for d in range(1, 129):
        nxt = {}
        for o, c in surv.items():
            for b in (0, 1):
                oo = o + b
                if 3 ** oo >= 2 ** d:
                    nxt[oo] = nxt.get(oo, 0) + c
        surv = nxt
        depths.append(d)
        total = sum(surv.values())
        log10dens.append(math.log10(total) - d * math.log10(2))
    theta = math.log(2, 3)
    Hth = -(theta * math.log2(theta) + (1 - theta) * math.log2(1 - theta))
    rate = 1 - Hth
    bound = [(d, -rate * d * math.log10(2)) for d in depths]
    s = svg_header("Certificate-frontier density: exact DP count vs proved entropy bound (Thm C)")
    ax, px, py = axes(0, 130, -8.5, 0, "depth d (shortcut steps)", "log10 density",
                      [(0, "0"), (32, "32"), (64, "64"), (96, "96"), (128, "128")],
                      [(0, "1"), (-2, "1e-2"), (-4, "1e-4"), (-6, "1e-6"), (-8, "1e-8")])
    s += ax
    s += polyline(bound, px, py, "#c0392b", dash="6,4")
    s += polyline(list(zip(depths, log10dens)), px, py, "#2c3e50", width=1.2)
    for d, v in zip(depths, log10dens):
        if d % 8 == 0 or d == 1:
            s += f'<circle cx="{px(d):.1f}" cy="{py(v):.1f}" r="2.6" fill="#2c3e50"/>'
    s += (f'<text x="{px(70)}" y="{py(-2.1)}" fill="#2c3e50">exact S(d)/2^d  (measured slope -0.108 at d=128)</text>'
          f'<text x="{px(28)}" y="{py(-4.6)}" fill="#c0392b">bound 2^(-0.05004 d)  [Thm C]</text>')
    (OUT / "fig1_frontier_density.svg").write_text(s + "</svg>", encoding="utf-8")


def fig2():
    rec = [(2, 1), (3, 5), (7, 11), (9, 13), (27, 70), (230631, 278), (626331, 319),
           (837799, 329), (1723519, 349), (3732423, 374)]
    s = svg_header("Total-stopping-time records vs stochastic-model extremes (measured 2026-07-01)")
    ax, px, py = axes(0, 17, 0, 720, "ln n", "sigma_inf(n)  (shortcut steps)",
                      [(0, "0"), (4, "4"), (8, "8"), (12, "12"), (16, "16")],
                      [(0, "0"), (200, "200"), (400, "400"), (600, "600")])
    s += ax
    s += polyline([(0, 0), (17, 6.9521 * 17)], px, py, "#2980b9")
    s += polyline([(0, 0), (17, 41.677647 * 17)], px, py, "#c0392b", dash="6,4")
    for n, sig in rec:
        s += f'<rect x="{px(math.log(n))-3:.1f}" y="{py(sig)-3:.1f}" width="6" height="6" fill="#2c3e50"/>'
    for n, sig in rec[-3:]:
        s += f'<text x="{px(math.log(n))+5:.1f}" y="{py(sig)+12:.1f}" font-size="10">{n}</text>'
    s += (f'<text x="{px(9.3)}" y="{py(120)}" fill="#2980b9">mean slope 2/ln(4/3) = 6.952</text>'
          f'<text x="{px(2.2)}" y="{py(640)}" fill="#c0392b">Lagarias-Weiss limsup slope 41.678</text>'
          f'<text x="{px(8.0)}" y="{py(470)}" fill="#2c3e50">records reach only ~24.7 ln n at N = 5e6:</text>'
          f'<text x="{px(8.0)}" y="{py(430)}" fill="#2c3e50">the extreme tail is computationally unreachable</text>')
    (OUT / "fig2_gamma_records.svg").write_text(s + "</svg>", encoding="utf-8")


fig1()
fig2()
print("wrote", OUT / "fig1_frontier_density.svg", "and fig2_gamma_records.svg")
