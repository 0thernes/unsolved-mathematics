#!/usr/bin/env python3
"""Build a self-contained static HTML Atlas site under _site/ for GitHub Pages.

Zero third-party dependencies beyond Python stdlib: reads canonical generated
JSON/data files (data/problems.json, data/citation-verification-log.json,
formal/comparator.json, VERSION) and emits _site/index.html + data copies.
"""

from __future__ import annotations

import html
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "_site"


def build_site(out_dir: Path = OUT_DIR) -> Path:
    reg = json.loads((ROOT / "data" / "problems.json").read_text(encoding="utf-8"))
    cit = json.loads((ROOT / "data" / "citation-verification-log.json").read_text(encoding="utf-8"))
    comp = json.loads((ROOT / "formal" / "comparator.json").read_text(encoding="utf-8"))
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

    problems = reg["problems"]
    meta = reg.get("meta", {})
    summary = cit.get("summary", {})
    n_verified = summary.get("verified", 0)
    n_stripped = summary.get("mismatch", 0) + summary.get("not_found", 0)
    n_theorems = len(comp.get("theorem_names", []))

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
    .sub {{ color:var(--muted); margin:0 0 1.5rem; }}
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
    <p class="sub">Audited, ranked corpus of {len(problems)} open mathematical problems · zero-Mathlib Lean 4.35.0 6-kernel formal core · primary-source verified citations · updated {html.escape(str(meta.get("updated", "")))}.</p>

    <div class="cards">
      <div class="card"><div class="num">{len(problems)}</div><div class="lbl">Ranked Problem Dossiers</div></div>
      <div class="card"><div class="num">{n_theorems}</div><div class="lbl">Lean 4.35.0 6-Kernel Theorems (0 sorry)</div></div>
      <div class="card"><div class="num">{n_verified}</div><div class="lbl">API-Verified Citations ({n_stripped} bad IDs stripped)</div></div>
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
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/CLAIMS.md">Claims Ledger</a> ·
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/formal/STATEMENT_FIDELITY.md">Lean Statement Fidelity</a> ·
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
    shutil.copy2(ROOT / "data" / "problems.json", out_dir / "problems.json")
    shutil.copy2(ROOT / "docs" / "media" / "social-preview.svg", out_dir / "social-preview.svg")
    return index_path


def main() -> int:
    out = build_site()
    print(f"Built static Atlas site -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
