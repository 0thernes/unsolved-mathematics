#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build a self-contained static HTML Atlas site + Lean Proof Blueprint under _site/.

Zero third-party dependencies beyond Python stdlib: reads canonical generated
JSON/data files (data/problems.json, data/citation-verification-log.json,
data/retraction-audit.json, lean/comparator.json, lean/VerifyAxioms.lean, VERSION)
and emits:
  - _site/index.html      (searchable 106-problem Atlas explorer)
  - _site/blueprint.html  (interactive Lean 4.35.0 6-kernel Proof Blueprint & DAG)
  - _site/problems.json
  - _site/social-preview.svg
"""

from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "_site"

THEOREM_CATALOG: list[tuple[str, str, str, str, str]] = [
    ("thm_collatz_cylinder_affine_law", "Collatz", "FormalAtlas/Collatz.lean", "T^d(2^d q + r) = 3^{o(r,d)} q + T^d(r)", "Terras (1976) affine cylinder law"),
    ("thm_collatz_exact_intercept_law", "Collatz", "FormalAtlas/Collatz.lean", "2^d T^d(x) = 3^o x + c(w)", "Exact Bernstein-Lagarias intercept identity"),
    ("thm_terras_parity_word_bijection", "Collatz", "FormalAtlas/Collatz.lean", "{0..2^d-1} <-> {0,1}^d", "Terras (1976) parity-word bijection"),
    ("thm_collatz_descent_certificate_sound", "Collatz", "FormalAtlas/Collatz.lean", "3^o < 2^d & threshold => T^d(x) < x", "Soundness of finite descent certificates"),
    ("thm_collatz_no_finite_subcritical_cover", "Collatz", "FormalAtlas/Collatz.lean", "T^d(-1) = -1, o(-1,d) = d", "No finite 2-adic subcritical cover of Z"),
    ("thm_collatz_spine_ladder_identity", "Collatz", "FormalAtlas/Collatz.lean", "2^d((2^d-3^o)T^d(x)-c) = 3^o((2^d-3^o)x-c)", "Cleared-denominator spine recurrence"),
    ("thm_collatz_positivity_localization", "Collatz", "FormalAtlas/Collatz.lean", "3^o > 2^d => c(w) >= 3^o - 2^d", "Unconditional supercritical localization (rho_w <= -1)"),
    ("thm_collatz_epsilon_invariance_barrier", "Collatz", "FormalAtlas/Collatz.lean", "TMinus Terras bijection + cycles 5, 17", "No-go barrier against sign-blind 2-adic proofs"),
    ("thm_collatz_cycle_equation", "Collatz", "FormalAtlas/Collatz.lean", "T^d(x) = x => (2^d - 3^o) x = c(w)", "Bohm-Sontacchi (1978) exact cycle equation"),
    ("thm_collatz_parity_word_append", "Collatz", "FormalAtlas/Collatz.lean", "w_{d1+d2}(x) = w_{d1}(x) ++ w_{d2}(f^{d1}(x))", "Symbolic dynamics parity-word cocycle"),
    ("thm_collatz_negative_cycles", "Collatz", "FormalAtlas/Collatz.lean", "T^3(-5)=-5, T^11(-17)=-17", "Supercritical negative integer cycles of 3n+1"),
    ("thm_erdos_straus_mordell_840", "Erdos-Straus", "FormalAtlas/ErdosStraus.lean", "n mod 840 not in {1,121,169,289,361,529}", "Mordell (1967) 834/840 modular reduction (99.29%)"),
    ("thm_erdos_straus_multiplicative_closure", "Erdos-Straus", "FormalAtlas/ErdosStraus.lean", "HasErdosStraus m => HasErdosStraus (m*k)", "Multiplicative closure / reduction to primes"),
    ("thm_erdos_straus_mordell_exceptions_small", "Erdos-Straus", "FormalAtlas/ErdosStraus.lean", "n in {121,169,289,361,529,841}", "Resolution of all 6 smallest exceptional squares"),
    ("thm_lonely_runner_sharpness_all_n", "Lonely Runner", "FormalAtlas/LonelyRunner.lean", "forall n>=1, t=p/q, exists i, ||t*i|| <= 1/(n+1)", "All-n rational optimality of 1/(n+1)"),
    ("thm_lonely_runner_n1", "Lonely Runner", "FormalAtlas/LonelyRunner.lean", "n = 1 (2 runners): gap >= 1/2", "Constructive base case n = 1"),
    ("thm_lonely_runner_n2", "Lonely Runner", "FormalAtlas/LonelyRunner.lean", "n = 2 (3 runners): gap >= 1/3", "Constructive base case n = 2"),
    ("thm_lonely_runner_speed_scaling", "Lonely Runner", "FormalAtlas/LonelyRunner.lean", "FarEnough m p q v => FarEnough m p (q*k) (v*k)", "Exact rational GCD speed-scaling invariance"),
    ("thm_brocard_brown_solutions", "Brocard", "FormalAtlas/Brocard.lean", "(4,5), (5,11), (7,71)", "Exact verification of all 3 known Brown pairs"),
    ("thm_brocard_exhaustive_le_12", "Brocard", "FormalAtlas/Brocard.lean", "n <= 12 => n in {4,5,7}", "Exhaustive classification through 12! + 1"),
    ("thm_brocard_mod4_ge_4", "Brocard", "FormalAtlas/Brocard.lean", "n >= 4 => (n! + 1) mod 4 = 1", "Odd-square modular constraint for all n >= 4"),
    ("thm_brocard_exhaustive_le_15", "Brocard", "FormalAtlas/Brocard.lean", "n <= 15 => n in {4,5,7}", "Exhaustive classification through 15! + 1"),
]


def _build_blueprint_html(version: str, n_theorems: int, n_decls: int) -> str:
    gh_base = "https://github.com/0thernes/unsolved-mathematics/blob/main/lean/"
    cards = []
    for idx, (name, group, src_file, formula, desc) in enumerate(THEOREM_CATALOG, 1):
        grp_slug = group.lower().replace(" ", "-")
        cards.append(
            f'<div class="thm-card" data-group="{html.escape(grp_slug)}">'
            f'<div class="thm-hdr"><span class="idx">#{idx}</span>'
            f'<span class="tag tag-{html.escape(grp_slug)}">{html.escape(group)}</span>'
            f'<span class="kbadge">6/6 kernels</span></div>'
            f'<div class="thm-name"><a href="{gh_base}{html.escape(src_file)}"><code>{html.escape(name)}</code></a></div>'
            f'<div class="thm-formula"><code>{html.escape(formula)}</code></div>'
            f'<div class="thm-desc">{html.escape(desc)}</div>'
            f"</div>"
        )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Lean 4.35.0 Proof Blueprint — The Unsolved Mathematics Atlas (v{html.escape(version)})</title>
  <style>
    :root {{ --bg:#0b1020; --card:#131c36; --line:#243259; --fg:#f1f5f9; --muted:#94a3b8; --accent:#60a5fa; --ok:#34d399; }}
    body {{ margin:0; font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif; background:var(--bg); color:var(--fg); line-height:1.5; }}
    main {{ max-width:1180px; margin:0 auto; padding:2rem 1.25rem 4rem; }}
    h1 {{ font-size:2rem; margin:0 0 .4rem; }}
    h2 {{ font-size:1.3rem; margin:2rem 0 .8rem; }}
    .sub {{ color:var(--muted); margin:0 0 1.4rem; }}
    nav {{ margin-bottom:1.25rem; display:flex; gap:1rem; flex-wrap:wrap; font-size:.95rem; }}
    a {{ color:#93c5fd; text-decoration:none; }}
    a:hover {{ text-decoration:underline; }}
    .dag-box {{ background:var(--card); border:1px solid var(--line); border-radius:12px; padding:1rem; overflow-x:auto; }}
    .filters {{ display:flex; gap:.5rem; flex-wrap:wrap; margin:1rem 0 1.25rem; }}
    button.fbtn {{ background:var(--card); color:var(--fg); border:1px solid var(--line); border-radius:999px; padding:.4rem .9rem; cursor:pointer; font-size:.88rem; }}
    button.fbtn.active {{ background:#1d4ed8; border-color:#60a5fa; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(310px,1fr)); gap:1rem; }}
    .thm-card {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:1rem; }}
    .thm-hdr {{ display:flex; align-items:center; gap:.5rem; margin-bottom:.45rem; font-size:.8rem; }}
    .idx {{ color:var(--muted); font-weight:700; }}
    .tag {{ padding:.12rem .5rem; border-radius:999px; background:#1e293b; color:#e2e8f0; }}
    .tag-collatz {{ background:#1e3a8a; color:#dbeafe; }}
    .tag-erdos-straus {{ background:#065f46; color:#d1fae5; }}
    .tag-lonely-runner {{ background:#5b21b6; color:#ede9fe; }}
    .tag-brocard {{ background:#92400e; color:#fef3c7; }}
    .kbadge {{ margin-left:auto; color:var(--ok); font-weight:600; }}
    .thm-name {{ font-size:.94rem; margin-bottom:.35rem; word-break:break-word; }}
    .thm-formula {{ font-size:.82rem; color:#cbd5e1; background:#0f172a; padding:.35rem .55rem; border-radius:6px; margin-bottom:.4rem; overflow-x:auto; }}
    .thm-desc {{ font-size:.87rem; color:var(--muted); }}
    footer {{ margin-top:2.5rem; color:var(--muted); font-size:.88rem; }}
  </style>
</head>
<body>
  <main>
    <nav>
      <a href="index.html">← Atlas Problem Explorer (106 Problems)</a>
      <a href="https://github.com/0thernes/unsolved-mathematics/tree/main/lean">lean/ Source</a>
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/lean/STATEMENT_FIDELITY.md">Statement Fidelity Audit</a>
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/paper/Donahue_2026_unsolved_mathematics_atlas.pdf">White Paper PDF</a>
    </nav>
    <h1>FormalAtlas Lean 4.35.0 Proof Blueprint <small style="color:var(--muted)">v{html.escape(version)}</small></h1>
    <p class="sub">Standalone zero-Mathlib Lean 4.35.0 formal core: <strong>{n_theorems} headline theorems</strong> + <strong>6 non-vacuity witnesses</strong> + <strong>8 adversarial false-variant refutations</strong> = <strong>{n_decls} audited declarations</strong> · axioms strictly within <code>&#123;propext, Classical.choice, Quot.sound&#125;</code> · verified across all <strong>6 independent kernels</strong>. <em>None of these theorems claims to solve an open conjecture.</em></p>

    <h2>Module Dependency &amp; Multi-Kernel Verification DAG</h2>
    <div class="dag-box">
      <svg viewBox="0 0 1080 260" width="100%" height="260" role="img" aria-label="Lean 4.35.0 FormalAtlas Dependency Graph">
        <defs>
          <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#60a5fa"/>
          </marker>
        </defs>
        <!-- Layer 1: Defs -->
        <rect x="20" y="95" width="170" height="62" rx="10" fill="#0f172a" stroke="#60a5fa" stroke-width="2"/>
        <text x="105" y="122" fill="#f1f5f9" text-anchor="middle" font-size="13" font-weight="700">FormalAtlas.Defs</text>
        <text x="105" y="142" fill="#94a3b8" text-anchor="middle" font-size="11">111 LOC · Zero Mathlib</text>

        <!-- Layer 2: Problem Modules -->
        <rect x="255" y="12" width="195" height="48" rx="8" fill="#1e3a8a" stroke="#93c5fd"/>
        <text x="352" y="34" fill="#f1f5f9" text-anchor="middle" font-size="12" font-weight="700">FormalAtlas.Collatz</text>
        <text x="352" y="50" fill="#bfdbfe" text-anchor="middle" font-size="10.5">11 headline theorems</text>

        <rect x="255" y="74" width="195" height="48" rx="8" fill="#065f46" stroke="#6ee7b7"/>
        <text x="352" y="96" fill="#f1f5f9" text-anchor="middle" font-size="12" font-weight="700">FormalAtlas.ErdosStraus</text>
        <text x="352" y="112" fill="#a7f3d0" text-anchor="middle" font-size="10.5">3 theorems (834/840 + sqs)</text>

        <rect x="255" y="136" width="195" height="48" rx="8" fill="#5b21b6" stroke="#c4b5fd"/>
        <text x="352" y="158" fill="#f1f5f9" text-anchor="middle" font-size="12" font-weight="700">FormalAtlas.LonelyRunner</text>
        <text x="352" y="174" fill="#ddd6fe" text-anchor="middle" font-size="10.5">4 theorems (sharpness + n<=2)</text>

        <rect x="255" y="198" width="195" height="48" rx="8" fill="#92400e" stroke="#fcd34d"/>
        <text x="352" y="220" fill="#f1f5f9" text-anchor="middle" font-size="12" font-weight="700">FormalAtlas.Brocard</text>
        <text x="352" y="236" fill="#fde68a" text-anchor="middle" font-size="10.5">4 theorems (mod-4 + n<=15)</text>

        <!-- Layer 3: Challenge/Solution/NonVacuity/Adversarial -->
        <rect x="520" y="18" width="185" height="46" rx="8" fill="#1e293b" stroke="#94a3b8"/>
        <text x="612" y="39" fill="#f1f5f9" text-anchor="middle" font-size="12" font-weight="700">Challenge.lean</text>
        <text x="612" y="54" fill="#94a3b8" text-anchor="middle" font-size="10.5">22 isolated signatures</text>

        <rect x="520" y="78" width="185" height="46" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.6"/>
        <text x="612" y="99" fill="#f1f5f9" text-anchor="middle" font-size="12" font-weight="700">Solution.lean</text>
        <text x="612" y="114" fill="#6ee7b7" text-anchor="middle" font-size="10.5">22 zero-sorry proofs</text>

        <rect x="520" y="138" width="185" height="46" rx="8" fill="#1e293b" stroke="#60a5fa"/>
        <text x="612" y="159" fill="#f1f5f9" text-anchor="middle" font-size="12" font-weight="700">NonVacuity.lean</text>
        <text x="612" y="174" fill="#93c5fd" text-anchor="middle" font-size="10.5">6 concrete witnesses</text>

        <rect x="520" y="198" width="185" height="46" rx="8" fill="#1e293b" stroke="#f87171"/>
        <text x="612" y="219" fill="#f1f5f9" text-anchor="middle" font-size="12" font-weight="700">Adversarial.lean</text>
        <text x="612" y="234" fill="#fca5a5" text-anchor="middle" font-size="10.5">8 false-variant refutations</text>

        <!-- Layer 4: VerifyAxioms + 6 Kernels -->
        <rect x="780" y="38" width="275" height="72" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
        <text x="917" y="64" fill="#34d399" text-anchor="middle" font-size="13" font-weight="700">6-Kernel bwrap Replay</text>
        <text x="917" y="83" fill="#cbd5e1" text-anchor="middle" font-size="10.5">lean · leanchecker-paranoid · lean4lean</text>
        <text x="917" y="99" fill="#cbd5e1" text-anchor="middle" font-size="10.5">nanoda_bin · con-leche · con-ron</text>

        <rect x="780" y="142" width="275" height="72" rx="10" fill="#0f172a" stroke="#60a5fa" stroke-width="2"/>
        <text x="917" y="168" fill="#93c5fd" text-anchor="middle" font-size="13" font-weight="700">VerifyAxioms + Comparator</text>
        <text x="917" y="187" fill="#cbd5e1" text-anchor="middle" font-size="10.5">36/36 decls in &#123;propext, choice, Quot&#125;</text>
        <text x="917" y="203" fill="#cbd5e1" text-anchor="middle" font-size="10.5">README parity checked in CI</text>

        <!-- Edges -->
        <line x1="190" y1="115" x2="252" y2="38" stroke="#60a5fa" stroke-width="1.5" marker-end="url(#arr)"/>
        <line x1="190" y1="122" x2="252" y2="98" stroke="#60a5fa" stroke-width="1.5" marker-end="url(#arr)"/>
        <line x1="190" y1="130" x2="252" y2="160" stroke="#60a5fa" stroke-width="1.5" marker-end="url(#arr)"/>
        <line x1="190" y1="138" x2="252" y2="222" stroke="#60a5fa" stroke-width="1.5" marker-end="url(#arr)"/>
        <line x1="450" y1="36" x2="517" y2="98" stroke="#60a5fa" stroke-width="1.4" marker-end="url(#arr)"/>
        <line x1="450" y1="98" x2="517" y2="101" stroke="#60a5fa" stroke-width="1.4" marker-end="url(#arr)"/>
        <line x1="450" y1="160" x2="517" y2="104" stroke="#60a5fa" stroke-width="1.4" marker-end="url(#arr)"/>
        <line x1="450" y1="222" x2="517" y2="108" stroke="#60a5fa" stroke-width="1.4" marker-end="url(#arr)"/>
        <line x1="450" y1="160" x2="517" y2="160" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>
        <line x1="450" y1="222" x2="517" y2="222" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>
        <line x1="705" y1="41" x2="777" y2="166" stroke="#94a3b8" stroke-width="1.4" marker-end="url(#arr)"/>
        <line x1="705" y1="101" x2="777" y2="74" stroke="#34d399" stroke-width="1.6" marker-end="url(#arr)"/>
        <line x1="705" y1="161" x2="777" y2="82" stroke="#34d399" stroke-width="1.4" marker-end="url(#arr)"/>
        <line x1="705" y1="221" x2="777" y2="90" stroke="#34d399" stroke-width="1.4" marker-end="url(#arr)"/>
        <line x1="705" y1="101" x2="777" y2="176" stroke="#60a5fa" stroke-width="1.4" marker-end="url(#arr)"/>
      </svg>
    </div>

    <h2>Headline Theorems ({n_theorems})</h2>
    <div class="filters">
      <button class="fbtn active" data-filter="all">All ({n_theorems})</button>
      <button class="fbtn" data-filter="collatz">Collatz (11)</button>
      <button class="fbtn" data-filter="erdos-straus">Erdős–Straus (3)</button>
      <button class="fbtn" data-filter="lonely-runner">Lonely Runner (4)</button>
      <button class="fbtn" data-filter="brocard">Brocard (4)</button>
    </div>

    <div class="grid" id="grid">
      {"".join(cards)}
    </div>

    <footer>
      Curated by <strong>Alexander S. Donahue</strong> (ORCID <a href="https://orcid.org/0009-0006-8168-9648">0009-0006-8168-9648</a>, independent researcher) ·
      <a href="index.html">Atlas Explorer</a> ·
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/CLAIMS.md">Claims Ledger</a> ·
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/ERRATA.md">Errata</a> ·
      MIT / CC BY 4.0.
    </footer>
  </main>
  <script>
    const btns = Array.from(document.querySelectorAll('button.fbtn'));
    const cards = Array.from(document.querySelectorAll('.thm-card'));
    for (const b of btns) {{
      b.addEventListener('click', () => {{
        for (const o of btns) o.classList.remove('active');
        b.classList.add('active');
        const f = b.dataset.filter;
        for (const c of cards) c.style.display = (f === 'all' || c.dataset.group === f) ? '' : 'none';
      }});
    }}
  </script>
</body>
</html>
"""


def build_site(out_dir: Path = OUT_DIR) -> Path:
    reg = json.loads((ROOT / "data" / "problems.json").read_text(encoding="utf-8"))
    cit = json.loads((ROOT / "data" / "citation-verification-log.json").read_text(encoding="utf-8"))
    comp = json.loads((ROOT / "lean" / "comparator.json").read_text(encoding="utf-8"))
    ret_path = ROOT / "data" / "retraction-audit.json"
    ret = json.loads(ret_path.read_text(encoding="utf-8")) if ret_path.exists() else {}
    verify_txt = (ROOT / "lean" / "VerifyAxioms.lean").read_text(encoding="utf-8")
    n_decls = len(re.findall(r"^\s*#print\s+axioms\s+", verify_txt, re.M))
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

    problems = reg["problems"]
    meta = reg.get("meta", {})
    summary = cit.get("summary", {})
    n_verified = summary.get("verified", 0)
    n_stripped = summary.get("mismatch", 0) + summary.get("not_found", 0)
    n_theorems = len(comp.get("theorem_names", []))
    n_ret_checked = ret.get("summary", {}).get("dois_checked", 0)
    n_retracted = ret.get("summary", {}).get("retracted", 0)

    rows_html = []
    for p in problems:
        slug = html.escape(p["slug"])
        title = html.escape(p["title"])
        field = html.escape(p["field"])
        status = html.escape(p["status"])
        year = html.escape(str(p["year_posed"]))
        css = html.escape(str(p["css"]))
        rank = html.escape(str(p["rank"]))
        mp = "Millennium" if p.get("millennium_prize") else ""
        url = f"https://github.com/0thernes/unsolved-mathematics/tree/main/problems/{slug}"
        rows_html.append(
            f'<tr data-field="{field.lower()}" data-status="{status.lower()}">'
            f"<td>{rank}</td>"
            f'<td><a href="{url}">{title}</a></td>'
            f"<td>{field}</td>"
            f"<td>{year}</td>"
            f"<td><strong>{css}</strong></td>"
            f'<td><span class="badge status-{status}">{status}</span></td>'
            f"<td>{mp}</td>"
            f"</tr>"
        )

    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>The Unsolved Mathematics Atlas (v{html.escape(version)})</title>
  <style>
    :root {{ --bg:#0b1020; --card:#131c36; --line:#243259; --fg:#f1f5f9; --muted:#94a3b8; --accent:#60a5fa; }}
    body {{ margin:0; font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif; background:var(--bg); color:var(--fg); line-height:1.5; }}
    main {{ max-width:1160px; margin:0 auto; padding:2rem 1.25rem 4rem; }}
    h1 {{ font-size:2.1rem; margin:0 0 .4rem; }}
    .sub {{ color:var(--muted); margin:0 0 1.2rem; }}
    nav {{ margin-bottom:1.4rem; display:flex; gap:1rem; flex-wrap:wrap; font-size:.95rem; }}
    .cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(210px,1fr)); gap:1rem; margin-bottom:1.5rem; }}
    .card {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:1rem; }}
    .card .num {{ font-size:1.6rem; font-weight:700; color:var(--accent); }}
    .card .lbl {{ font-size:.9rem; color:var(--muted); }}
    .controls {{ display:flex; flex-wrap:wrap; gap:.75rem; margin-bottom:1rem; }}
    input, select {{ background:var(--card); color:var(--fg); border:1px solid var(--line); border-radius:6px; padding:.5rem .75rem; font-size:.95rem; }}
    table {{ width:100%; border-collapse:collapse; background:var(--card); border:1px solid var(--line); border-radius:10px; overflow:hidden; }}
    th, td {{ padding:.6rem .75rem; border-bottom:1px solid var(--line); text-align:left; font-size:.92rem; }}
    th {{ background:#0f172a; color:#cbd5e1; }}
    a {{ color:#93c5fd; text-decoration:none; }}
    a:hover {{ text-decoration:underline; }}
    .badge {{ display:inline-block; padding:.15rem .5rem; border-radius:999px; font-size:.78rem; background:#1e293b; color:#e2e8f0; }}
    .status-recently-resolved {{ background:#065f46; color:#d1fae5; }}
    .status-disputed-claim {{ background:#7c2d12; color:#ffedd5; }}
    footer {{ margin-top:2rem; color:var(--muted); font-size:.88rem; }}
  </style>
</head>
<body>
  <main>
    <h1>The Unsolved Mathematics Atlas <small style="color:var(--muted)">v{html.escape(version)}</small></h1>
    <p class="sub">Audited, ranked corpus of {len(problems)} open mathematical problems · zero-Mathlib Lean 4.35.0 6-kernel formal core · primary-source verified citations &amp; retraction audit · updated {html.escape(str(meta.get("updated", "")))}.</p>
    <nav>
      <a href="blueprint.html"><strong>→ Interactive Lean 4.35.0 Proof Blueprint ({n_theorems} Theorems)</strong></a>
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/paper/Donahue_2026_unsolved_mathematics_atlas.pdf">White Paper PDF</a>
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/docs/CROSS_ATLAS_AUDIT_2026-11-25.md">Cross-Atlas Audit (1,900 Problems)</a>
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/CLAIMS.md">Claims Ledger</a>
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/ERRATA.md">Errata</a>
    </nav>

    <div class="cards">
      <div class="card"><div class="num">{len(problems)}</div><div class="lbl">Ranked Problem Dossiers</div></div>
      <div class="card"><div class="num">{n_theorems} / {n_decls}</div><div class="lbl">Lean 4.35.0 Theorems / Audited Decls (6 Kernels, 0 sorry)</div></div>
      <div class="card"><div class="num">{n_verified}</div><div class="lbl">API-Verified Citations ({n_stripped} bad IDs stripped · {n_retracted}/{n_ret_checked} retracted DOIs)</div></div>
      <div class="card"><div class="num">0 / {len(problems)}</div><div class="lbl">Human Peer Reviews (honestly disclosed)</div></div>
    </div>

    <div class="controls">
      <input id="q" type="search" placeholder="Filter by title, field, or status..." aria-label="Filter problems" style="flex:1;min-width:240px;">
      <select id="st" aria-label="Filter by status">
        <option value="">All statuses</option>
        <option value="open">open</option>
        <option value="active-progress">active-progress</option>
        <option value="recently-resolved">recently-resolved</option>
        <option value="disputed-claim">disputed-claim</option>
        <option value="independent">independent</option>
      </select>
    </div>

    <table id="tbl">
      <thead>
        <tr><th>#</th><th>Problem</th><th>Field</th><th>Posed</th><th>CSS</th><th>Status</th><th>Prize</th></tr>
      </thead>
      <tbody>
        {"".join(rows_html)}
      </tbody>
    </table>

    <footer>
      Curated by <strong>Alexander S. Donahue</strong> (ORCID <a href="https://orcid.org/0009-0006-8168-9648">0009-0006-8168-9648</a>, independent researcher) ·
      <a href="https://github.com/0thernes/unsolved-mathematics">GitHub Repository</a> ·
      <a href="blueprint.html">Lean Proof Blueprint</a> ·
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/lean/STATEMENT_FIDELITY.md">Statement Fidelity</a> ·
      CC BY 4.0 / MIT.
    </footer>
  </main>
  <script>
    const q = document.getElementById('q'), st = document.getElementById('st');
    const rows = Array.from(document.querySelectorAll('#tbl tbody tr'));
    function filter() {{
      const term = q.value.trim().toLowerCase(), sv = st.value.toLowerCase();
      for (const r of rows) {{
        const okQ = !term || r.textContent.toLowerCase().includes(term);
        const okS = !sv || r.dataset.status === sv;
        r.style.display = (okQ && okS) ? '' : 'none';
      }}
    }}
    q.addEventListener('input', filter);
    st.addEventListener('change', filter);
  </script>
</body>
</html>
"""

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    index_path = out_dir / "index.html"
    index_path.write_text(page, encoding="utf-8", newline="\n")
    (out_dir / "blueprint.html").write_text(
        _build_blueprint_html(version, n_theorems, n_decls), encoding="utf-8", newline="\n"
    )
    shutil.copy2(ROOT / "data" / "problems.json", out_dir / "problems.json")
    shutil.copy2(ROOT / "docs" / "media" / "social-preview.svg", out_dir / "social-preview.svg")
    return index_path


def main() -> int:
    out = build_site()
    print(f"Built static Atlas site + Lean Proof Blueprint -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
