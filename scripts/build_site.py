#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build a self-contained static HTML Atlas site + 8-domain Lean Proof Blueprint under _site/.

Zero third-party dependencies beyond Python stdlib: reads canonical generated
JSON/data files (data/problems.json, data/citation-verification-log.json,
data/retraction-audit.json, lean/comparator.json, lean/VerifyAxioms.lean, VERSION)
and emits:
  - _site/index.html         (searchable curated Atlas explorer)
  - _site/blueprint.html     (interactive 8-domain, 74-theorem Lean 4.35.0 Proof Blueprint & DAG)
  - _site/collatz-hydra.html (interactive 5-vector Asymmetric Hydra Collatz visual dashboard)
  - _site/problems.json
  - _site/social-preview.svg
  - _site/programs.html + external-programs.json + external-crosswalk.json
    (daily full Left to Solve mirror across all live programs from data/external/)
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
    ("thm_collatz_epsilon_invariance_barrier", "Collatz", "FormalAtlas/Collatz.lean", "TMinus Terras bijection + cycles 5, 17", "3n-1 sibling comparison (same Terras bijection + cycles 5, 17; heuristic reading, not a formal barrier theorem)"),
    ("thm_collatz_cycle_equation", "Collatz", "FormalAtlas/Collatz.lean", "T^d(x) = x => (2^d - 3^o) x = c(w)", "Bohm-Sontacchi (1978) exact cycle equation"),
    ("thm_collatz_parity_word_append", "Collatz", "FormalAtlas/Collatz.lean", "w_{d1+d2}(x) = w_{d1}(x) ++ w_{d2}(f^{d1}(x))", "Symbolic dynamics parity-word cocycle"),
    ("thm_collatz_negative_cycles", "Collatz", "FormalAtlas/Collatz.lean", "T^3(-5)=-5, T^11(-17)=-17", "Supercritical negative integer cycles of 3n+1"),
    ("thm_collatz_zero_fixed_point", "Collatz", "FormalAtlas/Collatz.lean", "T^d(0) = 0 & o(T,d,0) = 0", "Zero trivial fixed-point invariant"),
    ("thm_collatz_intercept_nonneg", "Collatz", "FormalAtlas/Collatz.lean", "0 <= wordIntercept w", "Non-negativity of affine intercept for all words"),
    ("thm_collatz_parity_word_length", "Collatz", "FormalAtlas/Collatz.lean", "(parityWord f d x).length = d", "Length preservation for arbitrary maps"),
    ("thm_collatz_positive_cycle_has_odd_step", "Collatz", "FormalAtlas/Collatz.lean", "d>=1 & x>0 & T^d(x)=x => oddCount >= 1", "Every positive Collatz cycle contains at least one odd step"),
    ("thm_collatz_positive_cycle_intercept_pos", "Collatz", "FormalAtlas/Collatz.lean", "d>=1 & x>0 & T^d(x)=x => wordIntercept w > 0", "Every positive Collatz cycle has strictly positive affine intercept"),
    ("thm_collatz_positive_cycle_subcritical", "Collatz", "FormalAtlas/Collatz.lean", "3^o < 2^d & 2^d - 3^o <= c(w)", "Every positive Collatz cycle is strictly subcritical (2^d > 3^o)"),
    ("thm_collatz_no_positive_cycle_d1", "Collatz", "FormalAtlas/Collatz.lean", "x > 0 => T(x) != x", "Elimination of all positive length-1 fixed points"),
    ("thm_collatz_positive_cycle_one_odd", "Collatz", "FormalAtlas/Collatz.lean", "d>=1 & x>0 & T^d(x)=x & o=1 => d=2 & x in {1,2}", "Unconditional 1-odd-step positive-cycle exclusion for all d >= 1"),
    ("thm_collatz_positive_cycle_two_odd", "Collatz", "FormalAtlas/Collatz.lean", "d>=1 & x>0 & T^d(x)=x & o=2 => d=4 & x in {1,2}", "Unconditional 2-odd-step positive-cycle exclusion for all d >= 1"),
    ("thm_collatz_2adic_isometry", "Collatz", "FormalAtlas/Collatz.lean", "parityWord T d x = parityWord T d y <-> 2^d | (x - y)", "Exact 2-adic cylinder isometry of shortcut Collatz map"),
    ("thm_collatz_periodic_spine_congruence", "Collatz", "FormalAtlas/Collatz.lean", "2^k | (D(w) x - c(w)) <-> parityWord T k x = periodicPrefix w k", "Periodic spine 2-adic congruence characterization"),
    ("thm_collatz_odd_unit_lock_valuation_isometry", "Collatz", "FormalAtlas/Collatz.lean", "2^k | (c(w)D(v) - c(v)D(w)) <-> prefix(w^inf, k) = prefix(v^inf, k)", "Exact Odd-Unit-Lock 2-adic valuation isometry v2(rho_w - rho_v) = lcp"),
    ("thm_collatz_fine_wilf_spine_ceiling", "Collatz", "FormalAtlas/Collatz.lean", "rho_w != rho_v => v2(rho_w - rho_v) < |w| + |v| - gcd(|w|,|v|)", "Unconditional Fine-Wilf Odd-Unit-Lock spine valuation ceiling"),
    ("thm_collatz_trivial_cycle_orbit", "Collatz", "FormalAtlas/Collatz.lean", "T^{2k}(1)=1, T^{2k+1}(1)=2, T^{2k}(2)=2, T^{2k+1}(2)=1", "Exact periodic orbit of the trivial positive cycle 1 <-> 2"),
    ("thm_collatz_no_nontrivial_positive_cycle_le_7", "Collatz", "FormalAtlas/Collatz.lean", "1<=d<=7 & x>0 & T^d(x)=x => x in {1, 2}", "Exhaustive low-period positive-cycle exclusion through d <= 7"),
    ("thm_collatz_no_positive_cycle_odd_le_7", "Collatz", "FormalAtlas/Collatz.lean", "odd d<=7 & x>0 => T^d(x) != x", "No positive odd-period Collatz cycles for d in {1, 3, 5, 7}"),
    ("thm_collatz_catalytic_reversible_cylinder", "Collatz", "FormalAtlas/Collatz.lean", "catCollatzStep d q r acc cat = (acc + T^d(2^d q + r), cat)", "Zero-workspace catalytic reversible evaluation of Collatz cylinders"),
    ("thm_collatz_positive_cycle_three_odd", "Collatz", "FormalAtlas/Collatz.lean", "d>=1 & x>0 & T^d(x)=x & o=3 => d=6 & x in {1,2}", "Unconditional 3-odd-step positive-cycle exclusion for all d >= 1"),
    ("thm_collatz_intercept_upper_bound", "Collatz", "FormalAtlas/Collatz.lean", "wordIntercept w <= 2^(|w|-o) * (3^o - 2^o)", "Sharp universal affine intercept upper bound for all parity words"),
    ("thm_collatz_cycle_amplitude_ceiling", "Collatz", "FormalAtlas/Collatz.lean", "T^d(x)=x => (2^d - 3^o) * x <= 2^(d-o) * (3^o - 2^o)", "Global Eliahou-Steiner positive-cycle Diophantine amplitude ceiling"),
    ("thm_collatz_sign_conjugacy", "Collatz", "FormalAtlas/Collatz.lean", "iter T d (-x) = -iter TMinus d x & oddCount equal", "Exact chiral sign-conjugacy involution between 3n+1 (Z<0) and 3n-1 (Z>0)"),
    ("thm_collatz_mod3_chiral_asymmetry", "Collatz", "FormalAtlas/Collatz.lean", "2 nmid x => T(x) mod 3 = 2 & TMinus(x) mod 3 = 1", "Exact epsilon-sensitive mod-3 phase-lock asymmetry breaking 2-adic mirror"),
    ("thm_collatz_intercept_not_div3", "Collatz", "FormalAtlas/Collatz.lean", "1 <= wordOddCount w => wordIntercept w mod 3 != 0", "Universal 3-adic unit law for affine intercepts and rational spines"),
    ("thm_collatz_cycle_no_div3", "Collatz", "FormalAtlas/Collatz.lean", "d>=1 & x!=0 & T^d(x)=x => x mod 3 != 0", "Global 3-adic exclusion: no nonzero multiple of 3 lies on any Collatz cycle"),
    ("thm_collatz_positive_cycle_four_odd", "Collatz", "FormalAtlas/Collatz.lean", "d>=1 & x>0 & T^d(x)=x & o=4 => d=8 & x in {1,2}", "Unconditional 4-odd-step positive-cycle exclusion for all periods d >= 1"),
    ("thm_erdos_straus_mordell_840", "Erdos-Straus", "FormalAtlas/ErdosStraus.lean", "n mod 840 not in {1,121,169,289,361,529}", "Mordell (1967) 834/840 modular reduction (99.29%)"),
    ("thm_erdos_straus_multiplicative_closure", "Erdos-Straus", "FormalAtlas/ErdosStraus.lean", "HasErdosStraus m => HasErdosStraus (m*k)", "Multiplicative closure / reduction to primes"),
    ("thm_erdos_straus_mordell_exceptions_small", "Erdos-Straus", "FormalAtlas/ErdosStraus.lean", "n in {121,169,289,361,529,841}", "Resolution of all 6 smallest exceptional squares"),
    ("thm_erdos_straus_symmetry", "Erdos-Straus", "FormalAtlas/ErdosStraus.lean", "IsErdosStrausSol n x y z => (n y z x)", "Cyclic denominator symmetry"),
    ("thm_erdos_straus_all_le_30", "Erdos-Straus", "FormalAtlas/ErdosStraus.lean", "2 <= n <= 30 => HasErdosStraus n", "Unconditional small-range verification"),
    ("thm_lonely_runner_sharpness_all_n", "Lonely Runner", "FormalAtlas/LonelyRunner.lean", "forall n>=1, t=p/q, exists i, ||t*i|| <= 1/(n+1)", "All-n rational optimality of 1/(n+1)"),
    ("thm_lonely_runner_n1", "Lonely Runner", "FormalAtlas/LonelyRunner.lean", "n = 1 (2 runners): gap >= 1/2", "Constructive base case n = 1"),
    ("thm_lonely_runner_n2", "Lonely Runner", "FormalAtlas/LonelyRunner.lean", "n = 2 (3 runners): gap >= 1/3", "Constructive base case n = 2"),
    ("thm_lonely_runner_speed_scaling", "Lonely Runner", "FormalAtlas/LonelyRunner.lean", "FarEnough m p q v => FarEnough m p (q*k) (v*k)", "Exact rational GCD speed-scaling invariance"),
    ("thm_lonely_runner_period_shift", "Lonely Runner", "FormalAtlas/LonelyRunner.lean", "FarEnough m p q v => FarEnough m (p+q) q v", "Unit circle time-periodicity mod 1"),
    ("thm_lonely_runner_neg_time", "Lonely Runner", "FormalAtlas/LonelyRunner.lean", "FarEnough m p q v => FarEnough m (-p) q v", "Time-reversal symmetry t -> -t"),
    ("thm_lonely_runner_n3_nondiv4", "Lonely Runner", "FormalAtlas/LonelyRunner.lean", "n = 3, 4 nmid v_i => gap >= 1/4 at t=1/4", "4-runner constructive coverage (27/64 mod-4 speed-triple classes at t=1/4)"),
    ("thm_lonely_runner_n3", "Lonely Runner", "FormalAtlas/LonelyRunner.lean", "forall v1,v2,v3 > 0, exists t=p/q, gap >= 1/4", "Complete constructive 4-runner Lonely Runner theorem (ALL triples)"),
    ("thm_brocard_brown_solutions", "Brocard", "FormalAtlas/Brocard.lean", "(4,5), (5,11), (7,71)", "Exact verification of all 3 known Brown pairs"),
    ("thm_brocard_exhaustive_le_12", "Brocard", "FormalAtlas/Brocard.lean", "n <= 12 => n in {4,5,7}", "Exhaustive classification through 12! + 1"),
    ("thm_brocard_mod4_ge_4", "Brocard", "FormalAtlas/Brocard.lean", "n >= 4 => (n! + 1) mod 4 = 1", "Odd-square modular constraint for all n >= 4"),
    ("thm_brocard_exhaustive_le_15", "Brocard", "FormalAtlas/Brocard.lean", "n <= 15 => n in {4,5,7}", "Exhaustive classification through 15! + 1"),
    ("thm_brocard_not_div3_ge_3", "Brocard", "FormalAtlas/Brocard.lean", "n >= 3 => (n! + 1) mod 3 = 1", "Non-divisibility by 3 for all n >= 3"),
    ("thm_brocard_mod10_ge_5", "Brocard", "FormalAtlas/Brocard.lean", "n >= 5 => (n! + 1) mod 10 = 1", "Terminal decimal digit = 1 for all n >= 5"),
    ("thm_brocard_exhaustive_le_20", "Brocard", "FormalAtlas/Brocard.lean", "n <= 20 => n in {4,5,7}", "Exhaustive classification through 20! + 1 (2.43e18)"),
    ("thm_euclid_infinitely_many_primes", "Primes", "FormalAtlas/Primes.lean", "forall N, exists p > N, IsPrime p", "Euclid's theorem on infinitude of primes"),
    ("thm_arbitrary_prime_gaps", "Primes", "FormalAtlas/Primes.lean", "forall k>=1, exists m, k consecutive composites", "Arbitrarily long composite runs via (k+1)! + 2"),
    ("thm_prime_odd_ge_3", "Primes", "FormalAtlas/Primes.lean", "IsPrime p & p >= 3 => p mod 2 = 1", "Oddness of all primes >= 3"),
    ("thm_twin_prime_mod6", "Primes", "FormalAtlas/Primes.lean", "IsPrime p & IsPrime(p+2) & p>=4 => p mod 6 = 5", "Twin-prime mod-6 rigidity (6 | p + 1)"),
    ("thm_goldbach_even_le_100", "Goldbach", "FormalAtlas/Goldbach.lean", "even 4 <= n <= 100 => p + q = n", "Finite strong Goldbach verified through 100"),
    ("thm_goldbach_odd_binary_obstruction", "Goldbach", "FormalAtlas/Goldbach.lean", "odd p + q => p = 2 or q = 2", "Structural binary parity obstruction on odd integers"),
    ("thm_goldbach_binary_fails_at_11", "Goldbach", "FormalAtlas/Goldbach.lean", "not exists primes p, q: p + q = 11", "Concrete binary Goldbach failure at 11"),
    ("thm_mersenne_exponent_prime", "Perfect-Mersenne", "FormalAtlas/PerfectNumbers.lean", "IsPrime (2^n - 1) => IsPrime n", "Algebraic factorization 2^a - 1 | 2^(ab) - 1"),
    ("thm_perfect_numbers_first_four", "Perfect-Mersenne", "FormalAtlas/PerfectNumbers.lean", "IsPerfect 6, 28, 496, 8128", "Exact sigma(n) = 2n for first four perfect numbers"),
    ("thm_no_odd_perfect_le_100", "Perfect-Mersenne", "FormalAtlas/PerfectNumbers.lean", "odd n <= 100 => not IsPerfect n", "Finite odd-perfect exclusion through 100"),
    ("thm_euclid_even_perfect", "Perfect-Mersenne", "FormalAtlas/PerfectNumbers.lean", "p>=2 & IsPrime(2^p-1) => IsPerfect(2^(p-1)*(2^p-1))", "Euclid's Elements IX.36 even perfect theorem for ALL p >= 2"),
    ("thm_euler_even_perfect_converse", "Perfect-Mersenne", "FormalAtlas/PerfectNumbers.lean", "even n & IsPerfect n => exists p>=2, IsPrime(2^p-1) & n=2^(p-1)(2^p-1)", "Euler's 1747 converse for ALL even perfect numbers"),
    ("thm_euclid_euler_even_perfect_iff", "Perfect-Mersenne", "FormalAtlas/PerfectNumbers.lean", "even n => (IsPerfect n <-> exists p>=2, Mersenne form)", "Complete Euclid-Euler biconditional characterization of even perfect numbers"),
    ("thm_mersenne_prime_divisor_congruence", "Perfect-Mersenne", "FormalAtlas/PerfectNumbers.lean", "IsPrime p & p>=3 & IsPrime q & q | (2^p-1) => 2p | (q-1)", "Euler's 1750 Mersenne prime divisor congruence via Fermat's Little Theorem"),
    ("thm_ramsey_R33_upper", "Ramsey", "FormalAtlas/Ramsey.lean", "forall c on K_6, HasMonoTriangle c", "Exact Ramsey upper bound R(3,3) <= 6"),
    ("thm_ramsey_R33_lower", "Ramsey", "FormalAtlas/Ramsey.lean", "exists symm c on K_5, not HasMonoTriangle c", "Explicit C_5 lower bound R(3,3) > 5 (proving R(3,3)=6)"),
    ("thm_ramsey_R34_upper", "Ramsey", "FormalAtlas/Ramsey.lean", "forall symm c on K_9, red K_3 or blue K_4", "Exact Ramsey upper bound R(3,4) <= 9 via Handshaking Lemma"),
    ("thm_ramsey_R34_lower", "Ramsey", "FormalAtlas/Ramsey.lean", "exists symm c on K_8, no red K_3 & no blue K_4", "Explicit C_8(1,4,7) coloring proving R(3,4) > 8 (exact R(3,4)=9)"),
]


def _build_blueprint_html(version: str, n_theorems: int, n_decls: int, n_problems: int) -> str:
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
    .filters {{ display:flex; gap:.45rem; flex-wrap:wrap; margin:1rem 0 1.25rem; }}
    button.fbtn {{ background:var(--card); color:var(--fg); border:1px solid var(--line); border-radius:999px; padding:.38rem .82rem; cursor:pointer; font-size:.85rem; }}
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
    .tag-primes {{ background:#0e7490; color:#cffafe; }}
    .tag-goldbach {{ background:#854d0e; color:#fef9c3; }}
    .tag-perfect-mersenne {{ background:#9d174d; color:#fce7f3; }}
    .tag-ramsey {{ background:#3f6212; color:#ecfccb; }}
    .kbadge {{ margin-left:auto; color:var(--ok); font-weight:600; }}
    .thm-name {{ font-size:.92rem; margin-bottom:.35rem; word-break:break-word; }}
    .thm-formula {{ font-size:.82rem; color:#cbd5e1; background:#0f172a; padding:.35rem .55rem; border-radius:6px; margin-bottom:.4rem; overflow-x:auto; }}
    .thm-desc {{ font-size:.87rem; color:var(--muted); }}
    footer {{ margin-top:2.5rem; color:var(--muted); font-size:.88rem; }}
  </style>
</head>
<body>
  <main>
    <nav>
      <a href="index.html">← Atlas Problem Explorer ({n_problems} Problems)</a>
      <a href="collatz-hydra.html">Asymmetric Collatz Hydra (5 Vectors)</a>
      <a href="programs.html">External Programs (Left to Solve · Daily)</a>
      <a href="https://github.com/0thernes/unsolved-mathematics/tree/main/lean">lean/ Source</a>
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/lean/STATEMENT_FIDELITY.md">Statement Fidelity Audit</a>
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/paper/Donahue_2026_unsolved_mathematics_atlas.pdf">White Paper PDF</a>
    </nav>
    <h1>FormalAtlas Lean 4.35.0 Proof Blueprint <small style="color:var(--muted)">v{html.escape(version)}</small></h1>
    <p class="sub">Standalone zero-Mathlib Lean 4.35.0 formal core (<code>autoImplicit = false</code>) across <strong>8 open-problem domains</strong>: <strong>{n_theorems} headline theorems</strong> + <strong>20 non-vacuity witnesses</strong> + <strong>24 adversarial false-variant refutations</strong> = <strong>{n_decls} audited declarations</strong> · axioms strictly within <code>&#123;propext, Classical.choice, Quot.sound&#125;</code> · verified across all <strong>6 independent kernels</strong> + live negative kernel rejection. <em>None of these theorems claims to solve an open conjecture.</em></p>

    <h2>Eight-Domain Dependency &amp; Multi-Kernel Verification DAG</h2>
    <div class="dag-box">
      <svg viewBox="0 0 1100 340" width="100%" height="340" role="img" aria-label="Lean 4.35.0 8-Domain FormalAtlas Dependency Graph">
        <defs>
          <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#60a5fa"/>
          </marker>
        </defs>
        <rect x="16" y="136" width="170" height="66" rx="10" fill="#0f172a" stroke="#60a5fa" stroke-width="2"/>
        <text x="101" y="164" fill="#f1f5f9" text-anchor="middle" font-size="13" font-weight="700">FormalAtlas.Defs</text>
        <text x="101" y="184" fill="#94a3b8" text-anchor="middle" font-size="11">202 LOC · Zero Mathlib</text>

        <rect x="248" y="8" width="206" height="34" rx="7" fill="#1e3a8a" stroke="#93c5fd"/>
        <text x="351" y="30" fill="#f1f5f9" text-anchor="middle" font-size="11.5" font-weight="700">Collatz (36 theorems)</text>
        <rect x="248" y="49" width="206" height="34" rx="7" fill="#065f46" stroke="#6ee7b7"/>
        <text x="351" y="71" fill="#f1f5f9" text-anchor="middle" font-size="11.5" font-weight="700">Erdős–Straus (5 theorems)</text>
        <rect x="248" y="90" width="206" height="34" rx="7" fill="#5b21b6" stroke="#c4b5fd"/>
        <text x="351" y="112" fill="#f1f5f9" text-anchor="middle" font-size="11.5" font-weight="700">Lonely Runner n≤3 (8 thms)</text>
        <rect x="248" y="131" width="206" height="34" rx="7" fill="#92400e" stroke="#fcd34d"/>
        <text x="351" y="153" fill="#f1f5f9" text-anchor="middle" font-size="11.5" font-weight="700">Brocard ≤ 20 (7 theorems)</text>
        <rect x="248" y="172" width="206" height="34" rx="7" fill="#0e7490" stroke="#67e8f9"/>
        <text x="351" y="194" fill="#f1f5f9" text-anchor="middle" font-size="11.5" font-weight="700">Primes / Twins (4 theorems)</text>
        <rect x="248" y="213" width="206" height="34" rx="7" fill="#854d0e" stroke="#fde047"/>
        <text x="351" y="235" fill="#f1f5f9" text-anchor="middle" font-size="11.5" font-weight="700">Goldbach ≤ 100 (3 theorems)</text>
        <rect x="248" y="254" width="206" height="34" rx="7" fill="#9d174d" stroke="#f9a8d4"/>
        <text x="351" y="276" fill="#f1f5f9" text-anchor="middle" font-size="11.5" font-weight="700">Euclid–Euler / Mersenne (7)</text>
        <rect x="248" y="295" width="206" height="34" rx="7" fill="#3f6212" stroke="#bef264"/>
        <text x="351" y="317" fill="#f1f5f9" text-anchor="middle" font-size="11.5" font-weight="700">Ramsey R(3,4)=9 (4 thms)</text>

        <rect x="524" y="30" width="192" height="52" rx="8" fill="#1e293b" stroke="#94a3b8"/>
        <text x="620" y="53" fill="#f1f5f9" text-anchor="middle" font-size="12" font-weight="700">Challenge.lean</text>
        <text x="620" y="70" fill="#94a3b8" text-anchor="middle" font-size="10.5">{n_theorems} isolated signatures</text>

        <rect x="524" y="102" width="192" height="52" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.6"/>
        <text x="620" y="125" fill="#f1f5f9" text-anchor="middle" font-size="12" font-weight="700">Solution.lean</text>
        <text x="620" y="142" fill="#6ee7b7" text-anchor="middle" font-size="10.5">{n_theorems} zero-sorry proofs</text>

        <rect x="524" y="174" width="192" height="52" rx="8" fill="#1e293b" stroke="#60a5fa"/>
        <text x="620" y="197" fill="#f1f5f9" text-anchor="middle" font-size="12" font-weight="700">NonVacuity.lean</text>
        <text x="620" y="214" fill="#93c5fd" text-anchor="middle" font-size="10.5">20 concrete witnesses</text>

        <rect x="524" y="246" width="192" height="52" rx="8" fill="#1e293b" stroke="#f87171"/>
        <text x="620" y="269" fill="#f1f5f9" text-anchor="middle" font-size="12" font-weight="700">Adversarial.lean</text>
        <text x="620" y="286" fill="#fca5a5" text-anchor="middle" font-size="10.5">24 false-variant refutations</text>

        <rect x="788" y="64" width="290" height="84" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
        <text x="933" y="92" fill="#34d399" text-anchor="middle" font-size="13" font-weight="700">6-Kernel bwrap Replay</text>
        <text x="933" y="113" fill="#cbd5e1" text-anchor="middle" font-size="10.8">lean · leanchecker-paranoid · lean4lean</text>
        <text x="933" y="131" fill="#cbd5e1" text-anchor="middle" font-size="10.8">nanoda_bin · con-leche · con-ron</text>

        <rect x="788" y="182" width="290" height="84" rx="10" fill="#0f172a" stroke="#60a5fa" stroke-width="2"/>
        <text x="933" y="210" fill="#93c5fd" text-anchor="middle" font-size="13" font-weight="700">VerifyAxioms + Neg Gate</text>
        <text x="933" y="231" fill="#cbd5e1" text-anchor="middle" font-size="10.8">{n_decls}/{n_decls} decls in &#123;propext, choice, Quot&#125;</text>
        <text x="933" y="249" fill="#cbd5e1" text-anchor="middle" font-size="10.8">README parity + 3/3 live neg rejection</text>

        <line x1="186" y1="150" x2="245" y2="25" stroke="#60a5fa" stroke-width="1.3" marker-end="url(#arr)"/>
        <line x1="186" y1="156" x2="245" y2="66" stroke="#60a5fa" stroke-width="1.3" marker-end="url(#arr)"/>
        <line x1="186" y1="162" x2="245" y2="107" stroke="#60a5fa" stroke-width="1.3" marker-end="url(#arr)"/>
        <line x1="186" y1="168" x2="245" y2="148" stroke="#60a5fa" stroke-width="1.3" marker-end="url(#arr)"/>
        <line x1="186" y1="172" x2="245" y2="189" stroke="#60a5fa" stroke-width="1.3" marker-end="url(#arr)"/>
        <line x1="186" y1="178" x2="245" y2="230" stroke="#60a5fa" stroke-width="1.3" marker-end="url(#arr)"/>
        <line x1="186" y1="184" x2="245" y2="271" stroke="#60a5fa" stroke-width="1.3" marker-end="url(#arr)"/>
        <line x1="186" y1="190" x2="245" y2="312" stroke="#60a5fa" stroke-width="1.3" marker-end="url(#arr)"/>

        <line x1="454" y1="25" x2="520" y2="118" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>
        <line x1="454" y1="66" x2="520" y2="122" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>
        <line x1="454" y1="107" x2="520" y2="126" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>
        <line x1="454" y1="148" x2="520" y2="130" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>
        <line x1="454" y1="189" x2="520" y2="134" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>
        <line x1="454" y1="230" x2="520" y2="196" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>
        <line x1="454" y1="271" x2="520" y2="268" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>
        <line x1="454" y1="312" x2="520" y2="276" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#arr)"/>

        <line x1="716" y1="56" x2="784" y2="210" stroke="#94a3b8" stroke-width="1.4" marker-end="url(#arr)"/>
        <line x1="716" y1="128" x2="784" y2="96" stroke="#34d399" stroke-width="1.6" marker-end="url(#arr)"/>
        <line x1="716" y1="200" x2="784" y2="108" stroke="#34d399" stroke-width="1.4" marker-end="url(#arr)"/>
        <line x1="716" y1="272" x2="784" y2="120" stroke="#34d399" stroke-width="1.4" marker-end="url(#arr)"/>
        <line x1="716" y1="128" x2="784" y2="220" stroke="#60a5fa" stroke-width="1.4" marker-end="url(#arr)"/>
      </svg>
    </div>

    <h2>Headline Theorems ({n_theorems} Across 8 Domains)</h2>
    <div class="filters">
      <button class="fbtn active" data-filter="all">All ({n_theorems})</button>
      <button class="fbtn" data-filter="collatz">Collatz (36)</button>
      <button class="fbtn" data-filter="erdos-straus">Erdős–Straus (5)</button>
      <button class="fbtn" data-filter="lonely-runner">Lonely Runner (8)</button>
      <button class="fbtn" data-filter="brocard">Brocard (7)</button>
      <button class="fbtn" data-filter="primes">Primes (4)</button>
      <button class="fbtn" data-filter="goldbach">Goldbach (3)</button>
      <button class="fbtn" data-filter="perfect-mersenne">Perfect / Mersenne (7)</button>
      <button class="fbtn" data-filter="ramsey">Ramsey (4)</button>
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


def _build_collatz_hydra_html(version: str) -> str | None:
    """Interactive 5-Vector Asymmetric Hydra Collatz Dashboard (self-contained SVG + vanilla JS)."""
    res_path = (
        ROOT
        / "problems"
        / "collatz-conjecture"
        / "experiments"
        / "results"
        / "collatz_asymmetric_hydra_20261127.json"
    )
    if not res_path.exists():
        return None
    d = json.loads(res_path.read_text(encoding="utf-8"))
    va = d["vector_a_adelic_pincer"]
    vb = d["vector_b_minimax_game"]
    vc = d["vector_c_carry_shockwave"]
    vd = d["vector_d_tropical_karp"]
    ve = d["vector_e_symbolic_lz76"]

    # SVG 1: Minimax Demon Excess V_+(B) vs bit width B (4..22)
    tiers = vb["tiers"]
    max_exc = max(t["demon_excess"]["max_excess"] for t in tiers)
    pts_exc = []
    bars_svg = []
    for idx, t in enumerate(tiers):
        x = 64 + idx * 52
        exc = t["demon_excess"]["max_excess"]
        y = 200 - int((exc / max(max_exc, 1.0)) * 155)
        pts_exc.append(f"{x},{y}")
        esc_pct = t["sibling_3n_minus_1"]["nontrivial_cycle_fraction"] * 100.0
        bh = int((esc_pct / 100.0) * 155)
        bars_svg.append(
            f'<rect x="{x - 14}" y="{200 - bh}" width="28" height="{bh}" rx="3" fill="#7f1d1d" opacity="0.55"/>'
            f'<circle cx="{x}" cy="{y}" r="4.5" fill="#60a5fa"/>'
            f'<text x="{x}" y="{y - 9}" fill="#93c5fd" text-anchor="middle" font-size="10">{exc:.1f}</text>'
            f'<text x="{x}" y="220" fill="#cbd5e1" text-anchor="middle" font-size="10.5">B={t["bits"]}</text>'
        )
    poly_exc = " ".join(pts_exc)

    # SVG 2: Tropical Karp mu*(2^a * 3^b) = (a+b-1)/(a+b) vs theta = log3(2) & Positive Box Break
    mods = vd["mixed_base_quotients"]
    karp_bars = []
    for idx, m in enumerate(mods):
        x = 58 + idx * 54
        mu = m["mu_pruned_plus_float"]
        bh = int(mu * 160)
        karp_bars.append(
            f'<rect x="{x - 15}" y="{195 - bh}" width="30" height="{bh}" rx="3" fill="#f59e0b" opacity="0.82"/>'
            f'<text x="{x}" y="{189 - bh}" fill="#fde68a" text-anchor="middle" font-size="9.5">{html.escape(m["mu_pruned_plus"])}</text>'
            f'<text x="{x}" y="213" fill="#cbd5e1" text-anchor="middle" font-size="9.5">M={m["M"]}</text>'
        )
    theta_y = 195 - int(0.63092975 * 160)
    box_p_y = 195 - int(0.5 * 160)
    box_m_y = 195 - int((2.0 / 3.0) * 160)

    # SVG 3: Mod-9 Chiral Intercept Pile-up Inversion (3n+1 vs 3n-1)
    h_plus = va["mod9_intercept_plus_hist"]
    h_minus = va["mod9_intercept_minus_hist"]
    m9_max = max(max(h_plus), max(h_minus), 1)
    m9_bars = []
    for r in range(9):
        x = 54 + r * 56
        hp = int((h_plus[r] / m9_max) * 145)
        hm = int((h_minus[r] / m9_max) * 145)
        m9_bars.append(
            f'<rect x="{x - 16}" y="{185 - hp}" width="15" height="{hp}" rx="2" fill="#38bdf8"/>'
            f'<rect x="{x + 1}" y="{185 - hm}" width="15" height="{hm}" rx="2" fill="#f43f5e"/>'
            f'<text x="{x}" y="204" fill="#cbd5e1" text-anchor="middle" font-size="10.5">r={r}</text>'
        )

    tier_rows = "".join(
        f"<tr><td>B={t['bits']}</td><td>{t['odd_starts_scanned']:,}</td>"
        f"<td><code>{t['demon_stop']['n']:,}</code> ({t['demon_stop']['steps']})</td>"
        f"<td><code>{t['demon_total']['n']:,}</code> ({t['demon_total']['steps']})</td>"
        f"<td><code>{t['demon_excess']['n']:,}</code> (+{t['demon_excess']['max_excess']:.3f})</td>"
        f"<td>2<sup>{t['demon_altitude']['log2_ratio']:.2f}</sup></td>"
        f"<td style=\"color:#fca5a5\"><strong>{t['sibling_3n_minus_1']['nontrivial_cycle_fraction']*100:.2f}%</strong> "
        f"({t['sibling_3n_minus_1']['to_5_cycle']:,} → 5 · {t['sibling_3n_minus_1']['to_17_cycle']:,} → 17)</td></tr>"
        for t in tiers
    )

    lz_rows = "".join(
        f"<tr data-eps=\"{p['eps']}\"><td><code>{html.escape(p['label'])}</code></td>"
        f"<td><code>{p['seed_n']:,}</code></td>"
        f"<td>{'3n+1' if p['eps'] == 1 else '3n-1'}</td>"
        f"<td>{p['word_len']}</td><td>{p['odd_density']:.4f}</td>"
        f"<td>{p['lz76_phrases']}</td><td><strong>{p['lz76_normalized']:.4f}</strong></td>"
        f"<td>{p['max_odd_run']}</td><td>{p['autocorr_lag1']:+.4f}</td></tr>"
        for p in ve["profiles"]
    )

    last_t = tiers[-1]
    carry_plus = vc["mean_carry_bits"]["3n+1"]
    carry_minus = vc["mean_carry_bits"]["3n-1"]
    carry_diff = carry_plus - carry_minus
    ham_drift = vc["mean_hamming_drift"]["3n+1"]
    gh = "https://github.com/0thernes/unsolved-mathematics/blob/main"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Asymmetric Collatz Hydra (5 Convergent Vectors) — Unsolved Mathematics Atlas v{html.escape(version)}</title>
  <style>
    :root {{ --bg:#0b1020; --card:#131c36; --line:#243259; --fg:#f1f5f9; --muted:#94a3b8; --accent:#60a5fa; --ok:#34d399; --warn:#f59e0b; --bad:#f43f5e; }}
    body {{ margin:0; font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif; background:var(--bg); color:var(--fg); line-height:1.5; }}
    main {{ max-width:1180px; margin:0 auto; padding:2rem 1.25rem 4rem; }}
    nav {{ margin-bottom:1.25rem; display:flex; gap:1rem; flex-wrap:wrap; font-size:.94rem; }}
    a {{ color:#93c5fd; text-decoration:none; }} a:hover {{ text-decoration:underline; }}
    h1 {{ font-size:2rem; margin:0 0 .35rem; }}
    h2 {{ font-size:1.28rem; margin:2rem 0 .7rem; }}
    .sub {{ color:var(--muted); margin:0 0 1.25rem; }}
    .note {{ background:#1e293b; border-left:4px solid var(--ok); padding:.85rem 1rem; border-radius:6px; margin-bottom:1.4rem; font-size:.92rem; }}
    .cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(210px,1fr)); gap:.85rem; margin-bottom:1.5rem; }}
    .card {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:.95rem; }}
    .card .num {{ font-size:1.48rem; font-weight:700; color:var(--accent); }}
    .card .lbl {{ font-size:.84rem; color:var(--muted); }}
    .charts {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(350px,1fr)); gap:1rem; margin:1rem 0 1.5rem; }}
    .panel {{ background:var(--card); border:1px solid var(--line); border-radius:12px; padding:1rem; }}
    .panel h3 {{ margin:0 0 .4rem; font-size:1.02rem; }}
    .panel p {{ margin:0 0 .6rem; color:var(--muted); font-size:.84rem; }}
    table {{ width:100%; border-collapse:collapse; background:var(--card); border:1px solid var(--line); margin-bottom:1.6rem; }}
    th, td {{ padding:.5rem .68rem; border-bottom:1px solid var(--line); text-align:left; font-size:.87rem; }}
    th {{ background:#0f172a; color:#cbd5e1; }}
    .pill {{ display:inline-block; padding:.12rem .52rem; border-radius:999px; font-size:.76rem; font-weight:700; }}
    .pass {{ background:#065f46; color:#d1fae5; }}
    .warn {{ background:#92400e; color:#fef3c7; }}
    .nogo {{ background:#7f1d1d; color:#fee2e2; }}
    .filters {{ display:flex; gap:.45rem; margin:.6rem 0 .9rem; }}
    button.fbtn {{ background:var(--card); color:var(--fg); border:1px solid var(--line); border-radius:999px; padding:.34rem .8rem; cursor:pointer; font-size:.84rem; }}
    button.fbtn.active {{ background:#1d4ed8; border-color:#60a5fa; }}
    footer {{ margin-top:2.4rem; color:var(--muted); font-size:.88rem; }}
  </style>
</head>
<body>
  <main>
    <nav>
      <a href="index.html">← Atlas Problem Explorer</a>
      <a href="blueprint.html">Lean 4.35.0 Proof Blueprint (74 Theorems)</a>
      <a href="programs.html">External Programs (Left to Solve)</a>
      <a href="{gh}/problems/collatz-conjecture/experiments/COLLATZ-ASYMMETRIC-HYDRA-2026-11-27.md">Full Technical Report</a>
      <a href="{gh}/problems/collatz-conjecture/native/collatz_asymmetric_hydra.c">C17 Source</a>
      <a href="{gh}/problems/collatz-conjecture/native/collatz_hydra_oracle.rs">Safe Rust Oracle</a>
    </nav>

    <h1>Operation Asymmetric Hydra <small style="color:var(--muted)">v{html.escape(version)}</small></h1>
    <p class="sub">Five independent, sibling-calibrated asymmetric &amp; game-theoretic Collatz instruments (Adelic Pincer · Minimax Carry-Adversary Game · Binary Carry-Avalanche Shockwave · Tropical Karp Quotient Automata · Symbolic LZ76 Complexity) anchored by 36 machine-checked Lean 4.35.0 Collatz theorems.</p>

    <div class="note"><strong>Strict Epistemic Boundary:</strong> Every measurement below is exact, deterministic, UBSan-fuzzed (250,000 cases, 0 traps), and bit-exact cross-checked between C17 and a zero-<code>unsafe</code> Rust oracle. <strong>The Collatz Conjecture remains OPEN.</strong> Every vector is calibrated against the &epsilon; = &minus;1 (<code>3n&minus;1</code>) sibling control; modular no-go walls are reported honestly alongside genuine asymmetries.</div>

    <div class="cards">
      <div class="card"><div class="num">{d['total_elapsed_seconds']:.2f} s</div><div class="lbl">Full 5-Vector Catalytic C17 Runtime (2.1M starts, zero heap explosion)</div></div>
      <div class="card"><div class="num">{last_t['sibling_3n_minus_1']['nontrivial_cycle_fraction']*100:.2f}% vs 0%</div><div class="lbl">3n&minus;1 Sibling Cycle Escape vs 3n+1 (B=22, 2,097,151 odd starts)</div></div>
      <div class="card"><div class="num">+{carry_diff:.3f} bits</div><div class="lbl">Exact Carry-Avalanche Excess ({carry_plus:.3f} vs {carry_minus:.3f} carry bits/step)</div></div>
      <div class="card"><div class="num">(a+b&minus;1)/(a+b)</div><div class="lbl">Exact Tropical Modular Mirror Law vs Box Break (1/2 &lt; &theta; &lt; 2/3)</div></div>
    </div>

    <h2>Visual Diagnostics Across Converging Vectors</h2>
    <div class="charts">
      <div class="panel">
        <h3>Vector B: Minimax Demon Excess V<sub>+</sub>(B) vs 3n&minus;1 Escape Basin</h3>
        <p>Blue line: peak supercritical excess max(o &minus; &theta;d) under 3n+1. Red bars: exact % of odd starts trapped in 3n&minus;1 nontrivial cycles &#123;5, 17&#125;.</p>
        <svg viewBox="0 0 600 235" width="100%" height="235" role="img" aria-label="Minimax Demon Excess vs 3n-1 Escape">
          <line x1="40" y1="200" x2="575" y2="200" stroke="#334155" stroke-width="1"/>
          {"".join(bars_svg)}
          <polyline fill="none" stroke="#60a5fa" stroke-width="2.5" points="{poly_exc}"/>
        </svg>
      </div>

      <div class="panel">
        <h3>Vector D: Tropical Karp &mu;*(2<sup>a</sup>3<sup>b</sup>) Mirror vs Archimedean Box Break</h3>
        <p>Amber bars: exact pruned modular Karp mean (a+b&minus;1)/(a+b) &rarr; 1 (identical for &plusmn;1!). Dashed lines: &theta; = log<sub>3</sub>(2), 3n+1 box (1/2), 3n&minus;1 box (2/3).</p>
        <svg viewBox="0 0 600 235" width="100%" height="235" role="img" aria-label="Tropical Karp Maximum Cycle Mean">
          <line x1="36" y1="195" x2="580" y2="195" stroke="#334155" stroke-width="1"/>
          {"".join(karp_bars)}
          <line x1="36" y1="{theta_y}" x2="580" y2="{theta_y}" stroke="#f1f5f9" stroke-dasharray="5,4" stroke-width="1.4"/>
          <text x="576" y="{theta_y - 4}" fill="#f1f5f9" text-anchor="end" font-size="9.5">&theta; = 0.6309</text>
          <line x1="36" y1="{box_p_y}" x2="580" y2="{box_p_y}" stroke="#34d399" stroke-dasharray="3,3" stroke-width="1.4"/>
          <text x="576" y="{box_p_y + 11}" fill="#34d399" text-anchor="end" font-size="9.5">Box 3n+1 = 1/2</text>
          <line x1="36" y1="{box_m_y}" x2="580" y2="{box_m_y}" stroke="#f43f5e" stroke-dasharray="3,3" stroke-width="1.4"/>
          <text x="576" y="{box_m_y - 4}" fill="#fca5a5" text-anchor="end" font-size="9.5">Box 3n&minus;1 = 2/3</text>
        </svg>
      </div>

      <div class="panel">
        <h3>Vector A: Mod-9 Chiral Intercept Pile-Up Inversion (491 Spines)</h3>
        <p>Cyan: 3n+1 intercept c(w) mod 9 (peaks at r=5: 208/491 = 42.4%). Rose: 3n&minus;1 mirror (inverts to r=4). Zero mass on &#123;0, 3, 6&#125; (Lean-proved 3 &nmid; c(w)).</p>
        <svg viewBox="0 0 560 225" width="100%" height="225" role="img" aria-label="Mod-9 Chiral Intercept Inversion">
          <line x1="30" y1="185" x2="535" y2="185" stroke="#334155" stroke-width="1"/>
          {"".join(m9_bars)}
        </svg>
      </div>
    </div>

    <h2>Honest Five-Vector Sibling-Control Convergence Matrix</h2>
    <table>
      <thead><tr><th>Vector</th><th>Breaks &epsilon;-Symmetry?</th><th>Lean 4.35.0 Anchor</th><th>C17 == Safe Rust</th><th>Key Verified Finding</th></tr></thead>
      <tbody>
        <tr><td><strong>A. Adelic Pincer</strong></td><td><span class="pill pass">YES (mod 3 &amp; 9)</span></td><td><code>thm_collatz_mod3_chiral_asymmetry</code>, <code>thm_collatz_cycle_no_div3</code></td><td>Bit-exact</td><td>500k/500k mod-3 lock; 0/491 div-3 intercepts; 42.4% chiral pile-up at 5 vs 4 mod 9; high-v2 pairs drop &minus;1.80 bits in log<sub>2</sub>|&Delta;|<sub>&infin;</sub>.</td></tr>
        <tr><td><strong>B. Minimax Game</strong></td><td><span class="pill pass">YES (V<sub>+</sub> vs &infin;)</span></td><td><code>thm_collatz_cycle_amplitude_ceiling</code>, <code>thm_collatz_positive_cycle_four_odd</code></td><td>Bit-exact</td><td>3n&minus;1 traps 67.23% of 2.1M odd starts into &#123;5, 17&#125; cycles; 3n+1 traps 0% with Demon n*=3,873,535 (+10.573 excess).</td></tr>
        <tr><td><strong>C. Carry Shockwave</strong></td><td><span class="pill warn">PARTIAL</span></td><td><code>thm_collatz_sign_conjugacy</code></td><td>Bit-exact</td><td>+{carry_diff:.3f} extra carry bits/step ({carry_plus:.3f} vs {carry_minus:.3f}) &amp; trailing-1 v<sub>2</sub> swap separate &plusmn;1; Hamming drift &Delta;H = {ham_drift:+.3f} is &epsilon;-blind.</td></tr>
        <tr><td><strong>D. Tropical Karp</strong></td><td><span class="pill nogo">NO mod M</span> / <span class="pill pass">YES box</span></td><td><code>thm_collatz_sign_conjugacy</code>, <code>thm_collatz_cycle_no_div3</code></td><td>Bit-exact</td><td>Proves exact modular mirror &mu;*(2<sup>a</sup>3<sup>b</sup>) = (a+b&minus;1)/(a+b) &rarr; 1; positive box [1, N] breaks mirror to 1/2 &lt; &theta; &lt; 2/3.</td></tr>
        <tr><td><strong>E. Symbolic LZ76</strong></td><td><span class="pill pass">YES</span></td><td>Empirical diagnostic</td><td>Bit-exact</td><td>3n+1 Demons stay pseudorandom (LZ76<sub>norm</sub> = 1.04&ndash;1.23, |r<sub>1</sub>| &lt; 0.02) vs collapsed 3n&minus;1 periodic attractors (0.09&ndash;0.16).</td></tr>
      </tbody>
    </table>

    <h2>Vector B: Exact Minimax Demon Frontier (B = 4 &hellip; 22)</h2>
    <table>
      <thead><tr><th>Bits</th><th>Odd Starts</th><th>Stop Demon (&sigma;)</th><th>Total Demon (&tau;)</th><th>Excess Demon (max o&minus;&theta;d)</th><th>Altitude Ratio</th><th>3n&minus;1 Sibling Escape</th></tr></thead>
      <tbody>{tier_rows}</tbody>
    </table>

    <h2>Vector E: Symbolic LZ76 Complexity &amp; Autocorrelation</h2>
    <div class="filters">
      <button class="fbtn active" data-eps="all">All Orbits (6)</button>
      <button class="fbtn" data-eps="1">3n+1 Demons &amp; Typical (4)</button>
      <button class="fbtn" data-eps="-1">3n&minus;1 Sibling Cycles (2)</button>
    </div>
    <table id="lztbl">
      <thead><tr><th>Profile</th><th>Seed n</th><th>Map</th><th>Len L</th><th>Odd Density</th><th>LZ76 Phrases</th><th>Normalized LZ76</th><th>Max Odd Run</th><th>Lag-1 r<sub>1</sub></th></tr></thead>
      <tbody>{lz_rows}</tbody>
    </table>

    <footer>
      Curated by <strong>Alexander S. Donahue</strong> (ORCID <a href="https://orcid.org/0009-0006-8168-9648">0009-0006-8168-9648</a>, independent researcher) ·
      <a href="index.html">Atlas Explorer</a> · <a href="blueprint.html">Lean Blueprint</a> · MIT / CC BY 4.0.
    </footer>
  </main>
  <script>
    const lbtns = Array.from(document.querySelectorAll('button.fbtn'));
    const lrows = Array.from(document.querySelectorAll('#lztbl tbody tr'));
    for (const b of lbtns) {{
      b.addEventListener('click', () => {{
        for (const o of lbtns) o.classList.remove('active');
        b.classList.add('active');
        const f = b.dataset.eps;
        for (const r of lrows) r.style.display = (f === 'all' || r.dataset.eps === f) ? '' : 'none';
      }});
    }}
  </script>
</body>
</html>
"""


def _fmt_sbk(sbk: dict[str, int]) -> str:
    parts = [f"{k}: {sbk.get(k, 0):,}" for k in ("open", "known", "warmup", "unformalized", "other") if sbk.get(k, 0) > 0]
    return ", ".join(parts) if parts else "0"


def _build_programs_html(version: str) -> str | None:
    """External research-program mirror page (lefttosolve.com, all live programs), if a snapshot is committed."""
    snap_path = ROOT / "data" / "external" / "lefttosolve" / "snapshot.json"
    cw_path = ROOT / "data" / "external" / "lefttosolve" / "crosswalk.json"
    if not snap_path.exists() or not cw_path.exists():
        return None
    snap = json.loads(snap_path.read_text(encoding="utf-8"))
    cw = json.loads(cw_path.read_text(encoding="utf-8"))
    t = snap["totals"]
    gh = "https://github.com/0thernes/unsolved-mathematics/blob/main"
    global_sbk = t.get("solved_by_kind") or {}
    global_kinds = t.get("kinds") or {}
    total_solved_flags = sum(global_sbk.values()) if global_sbk else sum(p.get("solved_here", 0) for p in snap["programs"])
    prog_rows = []
    for i, p in enumerate(snap["programs"], 1):
        k = p["kinds"]
        psbk = p.get("solved_by_kind") or {}
        shards = p.get("shards") or []
        shard_note = f" ({len(shards)} shards)" if len(shards) > 1 else ""
        idx = (
            f'<a href="{gh}/docs/external/programs/{html.escape(p["slug"])}.md">{p["mirrored_count"]:,} items{shard_note}</a>'
            if p.get("mirrored")
            else "counts only"
        )
        sbk_cell = _fmt_sbk(psbk) if psbk else f"{p['solved_here']:,}"
        prog_rows.append(
            f"<tr><td>{i}</td><td><a href=\"{html.escape(p['url'])}\">{html.escape(p['name'])}</a></td>"
            f"<td>{p['targets']:,}</td><td>{p['open']:,}</td><td>{html.escape(sbk_cell)}</td>"
            f"<td>{k.get('open', 0):,} / {k.get('known', 0):,} / {k.get('warmup', 0):,} / {k.get('unformalized', 0):,}</td>"
            f"<td>{idx}</td></tr>"
        )
    cw_rows = []
    for r in cw["problems"]:
        if not r["matches"]:
            continue
        items = "<br>".join(
            f"<code>{html.escape(m['id'])}</code> · {html.escape(m['relation'])} · {html.escape(m['kind'])}"
            + (" · <strong>site-solved flag</strong>" if m["site_solved_flag"] else "")
            for m in r["matches"]
        )
        sig = "<br>".join(html.escape(s) for s in r["signals"]) or "—"
        cw_rows.append(
            f"<tr><td>{html.escape(r['title'])}</td><td><span class=\"badge\">{html.escape(r['atlas_status'])}</span></td>"
            f"<td>{items}</td><td>{sig}</td></tr>"
        )
    s = cw["summary"]
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>External Research Programs (Full Left to Solve Mirror) · Unsolved Mathematics Atlas v{html.escape(version)}</title>
  <style>
    body {{ margin:0; font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif; background:#0b1020; color:#f1f5f9; line-height:1.5; }}
    main {{ max-width:1180px; margin:0 auto; padding:2rem 1.25rem 4rem; }}
    .note {{ background:#1e293b; border-left:4px solid #f59e0b; padding:.85rem 1rem; border-radius:6px; margin:1rem 0 1.4rem; }}
    .cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:.85rem; margin:1rem 0 1.5rem; }}
    .card {{ background:#131c36; border:1px solid #243259; border-radius:10px; padding:.9rem; }}
    .card .num {{ font-size:1.45rem; font-weight:700; color:#60a5fa; }}
    .card .lbl {{ font-size:.84rem; color:#94a3b8; }}
    input {{ background:#131c36; color:#f1f5f9; border:1px solid #243259; border-radius:6px; padding:.48rem .75rem; font-size:.92rem; width:100%; max-width:420px; margin-bottom:.85rem; }}
    table {{ width:100%; border-collapse:collapse; background:#131c36; border:1px solid #243259; margin-bottom:2rem; }}
    th, td {{ padding:.5rem .7rem; border-bottom:1px solid #243259; text-align:left; font-size:.88rem; vertical-align:top; }}
    th {{ background:#0f172a; color:#cbd5e1; }}
    a {{ color:#93c5fd; text-decoration:none; }} a:hover {{ text-decoration:underline; }}
    code {{ font-size:.82rem; }} .badge {{ padding:.1rem .45rem; border-radius:999px; background:#1e293b; font-size:.78rem; }}
    .muted {{ color:#94a3b8; }}
  </style>
</head>
<body>
  <main>
    <p><a href="index.html">← Atlas Problem Explorer</a> · <a href="blueprint.html">Lean Proof Blueprint</a></p>
    <h1>External Research Programs <small class="muted">Full Left to Solve Mirror (All {t['programs']} Programs)</small></h1>
    <div class="note"><strong>Third-party metadata mirror, refreshed daily (carved out of CC BY 4.0).</strong>
      Counts, kinds, and disaggregated “solved here” flags come from <a href="https://lefttosolve.com/programs">lefttosolve.com</a>
      (formal Lean statements from <a href="https://github.com/google-deepmind/formal-conjectures">google-deepmind/formal-conjectures</a>, Apache-2.0;
      titles from Wikipedia, MathOverflow, Math StackExchange, and OEIS retain their upstream CC BY-SA 4.0 / source licenses — zero statement excerpts are stored;
      see <a href="{gh}/THIRD_PARTY_NOTICES.md">THIRD_PARTY_NOTICES.md</a>).
      “Solved here” is disaggregated by <code>kind</code> so <code>known</code> literature theorems and <code>warmup</code> exercises are never confused with solved <code>open</code> conjectures.
      This Atlas has <strong>not</strong> verified external claims, and no Atlas status is changed automatically. Not affiliated with Left to Solve.</div>
    <div class="cards">
      <div class="card"><div class="num">{t['mirrored_items']:,}</div><div class="lbl">Mirrored Items across all {t['programs']} Programs (&lt;4 MB shards)</div></div>
      <div class="card"><div class="num">{global_kinds.get('open', 0):,}</div><div class="lbl">Lean-Stated <code>open</code> Targets ({global_kinds.get('known', 0):,} known · {global_kinds.get('warmup', 0):,} warmup)</div></div>
      <div class="card"><div class="num">{total_solved_flags:,}</div><div class="lbl">Site Solved Flags ({html.escape(_fmt_sbk(global_sbk))})</div></div>
      <div class="card"><div class="num">{s['problems_with_matches']} / {s['atlas_problems']}</div><div class="lbl">Curated Atlas Crosswalk ({s['problems_with_signals']} review signals)</div></div>
    </div>
    <p class="muted">Last content change <code>{html.escape(snap['last_changed_utc'])}</code> · upstream commit
      <code>{html.escape(str((snap.get('upstream') or {}).get('commit') or '')[:12])}</code> · content SHA-256
      <code>{html.escape(snap['content_sha256'][:16])}…</code> · offline search CLI:
      <code>python scripts/search_all_problems.py --query "prime"</code></p>
    <h2>All {t['programs']} Programs</h2>
    <input id="pq" type="search" placeholder="Filter programs by name or counts..." aria-label="Filter programs">
    <table id="ptbl">
      <thead><tr><th>#</th><th>Program</th><th>Targets</th><th>Open</th><th>Solved by kind (site claim)</th><th>Kinds: open / known / warmup / unformalized</th><th>Item index</th></tr></thead>
      <tbody>{"".join(prog_rows)}</tbody>
    </table>
    <h2>Curated Atlas Crosswalk <small class="muted">{s['problems_with_matches']}/{s['atlas_problems']} matched · {s['problems_with_signals']} review signals</small></h2>
    <p class="muted">{html.escape(cw['rule'])}</p>
    <input id="cq" type="search" placeholder="Filter crosswalk by Atlas problem or Lean ID..." aria-label="Filter crosswalk">
    <table id="ctbl">
      <thead><tr><th>Atlas problem</th><th>Atlas status</th><th>External items (relation · kind)</th><th>Review signals</th></tr></thead>
      <tbody>{"".join(cw_rows)}</tbody>
    </table>
    <p class="muted">Sources: <a href="{gh}/data/external/lefttosolve/snapshot.json">snapshot.json</a> ·
      <a href="{gh}/data/external/lefttosolve/crosswalk.json">crosswalk.json</a> ·
      <a href="{gh}/docs/external/PROGRAMS.md">PROGRAMS.md</a> · verified offline by
      <code>python scripts/sync_external_programs.py --check</code>.</p>
  </main>
  <script>
    function bindFilter(inputId, tableId) {{
      const inp = document.getElementById(inputId);
      const rows = Array.from(document.querySelectorAll('#' + tableId + ' tbody tr'));
      inp.addEventListener('input', () => {{
        const term = inp.value.trim().toLowerCase();
        for (const r of rows) r.style.display = (!term || r.textContent.toLowerCase().includes(term)) ? '' : 'none';
      }});
    }}
    bindFilter('pq', 'ptbl');
    bindFilter('cq', 'ctbl');
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
    <p class="sub">Audited, ranked corpus of {len(problems)} open mathematical problems · 8-domain zero-Mathlib Lean 4.35.0 6-kernel formal core · primary-source verified citations &amp; retraction audit · FAIR RO-Crate / Croissant · updated {html.escape(str(meta.get("updated", "")))}.</p>
    <nav>
      <a href="blueprint.html"><strong>→ Interactive Lean 4.35.0 Proof Blueprint ({n_theorems} Theorems / {n_decls} Decls)</strong></a>
      <a href="collatz-hydra.html"><strong>→ Asymmetric Collatz Hydra (5 Vectors)</strong></a>
      <a href="programs.html">External Programs (Left to Solve, daily)</a>
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/paper/Donahue_2026_unsolved_mathematics_atlas.pdf">White Paper PDF</a>
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/docs/CROSS_ATLAS_AUDIT_2026-11-25.md">Cross-Atlas Audit (2,000 Mega-Atlas Problems)</a>
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/CLAIMS.md">Claims Ledger</a>
      <a href="https://github.com/0thernes/unsolved-mathematics/blob/main/ERRATA.md">Errata</a>
    </nav>

    <div class="cards">
      <div class="card"><div class="num">{len(problems)}</div><div class="lbl">Ranked Problem Dossiers</div></div>
      <div class="card"><div class="num">{n_theorems} / {n_decls}</div><div class="lbl">Lean 4.35.0 Theorems / Audited Decls (8 Domains, 6 Kernels, 0 sorry in proof modules)</div></div>
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
        _build_blueprint_html(version, n_theorems, n_decls, len(problems)), encoding="utf-8", newline="\n"
    )
    hydra_page = _build_collatz_hydra_html(version)
    if hydra_page is not None:
        (out_dir / "collatz-hydra.html").write_text(hydra_page, encoding="utf-8", newline="\n")
    shutil.copy2(ROOT / "data" / "problems.json", out_dir / "problems.json")
    shutil.copy2(ROOT / "docs" / "media" / "social-preview.svg", out_dir / "social-preview.svg")
    programs_page = _build_programs_html(version)
    if programs_page is not None:
        (out_dir / "programs.html").write_text(programs_page, encoding="utf-8", newline="\n")
        ext = ROOT / "data" / "external" / "lefttosolve"
        shutil.copy2(ext / "snapshot.json", out_dir / "external-programs.json")
        shutil.copy2(ext / "crosswalk.json", out_dir / "external-crosswalk.json")
    return index_path


def main() -> int:
    out = build_site()
    print(f"Built static Atlas site + 8-domain Lean Proof Blueprint -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
