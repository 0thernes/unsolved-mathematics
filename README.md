<div align="center">

# 🏔️ The Unsolved Mathematics Atlas

### *An audited, ranked, research-grade dossier & Lean 4.35.0 formal core of humanity's open mathematical problems.*

[![CI](https://github.com/0thernes/unsolved-mathematics/actions/workflows/ci.yml/badge.svg)](https://github.com/0thernes/unsolved-mathematics/actions/workflows/ci.yml)
[![Version](https://img.shields.io/badge/version-0.8.3-blue.svg)](VERSION)
[![Lean](https://img.shields.io/badge/Lean-4.35.0%20(6--kernel%20·%2066%20thms%20·%208%20domains)-7c3aed.svg)](lean/STATEMENT_FIDELITY.md)
[![Citations](https://img.shields.io/badge/API--verified%20citations-537%20(0%20retracted)-10b981.svg)](data/citation-verification-log.json)
[![Paper](https://img.shields.io/badge/White%20Paper-AMS--LaTeX%20PDF-b45309.svg)](paper/Donahue_2026_unsolved_mathematics_atlas.pdf)
[![Timestamps](https://img.shields.io/badge/Timestamps-RFC3161%20%2B%20Bitcoin%20OTS-0f766e.svg)](data/MANIFEST.sha256)
[![Pages](https://img.shields.io/badge/Live%20Atlas%20%26%20Blueprint-GitHub%20Pages-0284c7.svg)](https://0thernes.github.io/unsolved-mathematics/)
[![License: CC BY 4.0 / MIT](https://img.shields.io/badge/license-CC%20BY%204.0%20%2F%20MIT-slate.svg)](LICENSE)

**Each problem gets its own world — origin, the mind that posed it, every serious attack on it,
key papers with primary-source verification & retraction flags, key mathematicians, a deterministic RAG corpus,
FAIR RO-Crate 1.1 & Croissant 1.0 metadata, dual RFC 3161 + Bitcoin OpenTimestamps manifest proofs, a daily full mirror of all 26 Left to Solve programs (62,790 targets), a compiled AMS-LaTeX white paper, and a standalone
eight-domain, six-kernel Lean 4.35.0 formal verification core (`autoImplicit = false`).**

`v0.8.3` · branch `main` · **120 curated problems** (+ **62,790** daily-mirrored Left to Solve items across all 26 programs) · **66 Lean 4 theorems + 36 witnesses/refutations across 8 domains (102 decls; 0 `sorry` in proof modules, while `lean/Challenge.lean` holds the 66 `sorry`-stated comparator specifications by design; 6 kernels + live negative rejection)** · author **Alexander S. Donahue** ([ORCID 0009-0006-8168-9648](https://orcid.org/0009-0006-8168-9648)) · Status: `active`

[Live Web Atlas & Blueprint](https://0thernes.github.io/unsolved-mathematics/) · [Master Ranking](RANKING.md) · [White Paper PDF](paper/Donahue_2026_unsolved_mathematics_atlas.pdf) · [Formal Core (`lean/`)](lean/STATEMENT_FIDELITY.md) · [Cross-Atlas Audit (2,000)](docs/CROSS_ATLAS_AUDIT_2026-11-25.md) · [Claims Ledger](CLAIMS.md) · [Limitations](LIMITATIONS.md) · [Errata](ERRATA.md) · [Hardening Index](HARDENING_INDEX.md) · [Replication](REPLICATION.md) · [Indexes](docs/indexes/)

</div>

---

## What this is

The great open problems of mathematics are scattered across textbooks, survey
papers, MathOverflow threads, Wikipedia, and private notes. **This atlas gathers
120 of them into one rigorously organized, version-controlled, machine-readable
corpus** — ranked from the hardest and oldest down to those closest to a
resolution — paired with a daily full metadata mirror of **all 26 Left to Solve
research programs (62,790 targets)**, a standalone Lean 4.35.0 formal core, and
automated epistemic integrity gates.

For **every** problem you get a self-contained 7-section dossier:

- 📜 **`history.md`** — origin, formulation, and timeline of progress
- 👤 **`originator.md`** — the mathematician(s) who posed it
- 🧗 **`approaches.md`** — major lines of attack and partial results
- ⚰️ **`attempts.md`** — famous attempts, near-misses, and retracted "proofs"
- 📚 **`papers.md`** — key papers with primary-source verification flags (`verified`, `high-confidence`, `needs-verification`, `ai-suggested`)
- 🧠 **`mathematicians.md`** — the top minds who shaped the problem
- 🎯 **`status.md`** — the live mathematical frontier (updated through November 2026)
- 🤖 **`rag/`** — deterministic chunked corpus (`3,985` unique chunks across `822,714` tokens) with zero-dependency BM25 retrieval
- 🌐 **`data/external/` & `scripts/search_all_problems.py`** — daily full metadata mirror of **all 26 Left to Solve programs (62,790 targets across 27 `< 4 MB` shards, zero excerpts, carved out of CC BY 4.0)** with `solved_by_kind` disaggregation (review signals only; 0 Atlas statuses auto-changed) and unified offline search across both the 120 curated dossiers and all 62,790 mirrored items
- 🔬 **`lean/`** — standalone zero-Mathlib Lean 4.35.0 formal core (`autoImplicit = false`) proving **66 structural theorems** + **16 non-vacuity witnesses** + **20 adversarial false-variant refutations** (**102 audited declarations**, 14 zero-axiom) across **8 open-problem domains**: Collatz (28 thms, incl. Fine–Wilf Odd-Unit-Lock spine valuation ceiling, 2-adic isometry, exhaustive $d \le 7$ & unconditional 1-/2-odd-step positive-cycle exclusion, catalytic cylinder), Erdős–Straus (5), **constructive Lonely Runner through $n = 3$** (8, classical 4-runner case), Brocard $n \le 20$ (7), Primes/Twin Primes (4), Goldbach $4 \le n \le 100$ (3), **Complete Euclid–Euler biconditional even perfect number theorem (`divSum_eq_divSumLin` proved $\forall n$) & Euler's 1750 Mersenne prime divisor congruence $2p \mid (q-1)$** (7), and **exact Ramsey $R(3,3)=6$ and $R(3,4)=9$** (4) (0 `sorry`, 0 `admit`, 0 `native_decide` in the proof modules; `lean/Challenge.lean` is the `sorry`-stated comparator specification; standard axioms only, 6 independent kernels + live negative kernel rejection). These are classical, elementary, or bounded structural results; none settles an open conjecture.
- 📄 **`paper/`** — publication-grade AMS-LaTeX white paper ([PDF](paper/Donahue_2026_unsolved_mathematics_atlas.pdf) + clean-room-verified `arxiv_submission.tar.gz`)
- 🌐 **FAIR, Timestamps & Interactive Blueprint** — [RO-Crate 1.1](ro-crate-metadata.json), [MLCommons Croissant 1.0](croissant.json), dual DigiCert RFC 3161 (`.tsr`) + Bitcoin OpenTimestamps (`.ots`) proofs over `data/MANIFEST.sha256`, and live GitHub Pages [Atlas Explorer & 8-Domain Proof Blueprint](https://0thernes.github.io/unsolved-mathematics/blueprint.html)

## Quickstart

Clone and verify everything from a clean checkout (Python 3.11+ and optional Lean 4.35.0 via `elan`):

```bash
git clone https://github.com/0thernes/unsolved-mathematics.git
cd unsolved-mathematics
python -m pip install -r requirements-lock.txt

# Validate schema, deterministic views, citations, meta-analyses, proof-claim sweep, manifest & timestamps
python scripts/generate.py --check
python scripts/validate.py
python scripts/check_papers.py
python scripts/proof_claim_sweep.py
python scripts/build_data_manifest.py --check
python scripts/timestamp_manifest.py --check

# Run full verification test ladder (unit, negative, regression, Hypothesis, differential, metamorphic, mutation)
python -m pytest -v tests/
python tests/mutation_check.py
```

See [`REPLICATION.md`](REPLICATION.md) for full clean-clone replication commands including the 6-kernel Lean 4.35.0 verification pass and live negative kernel rejection test (`scripts/test_lean_negative.py`).

## Usage & Examples

```bash
# Query top problems, filter by field/status, search all 62,790 mirrored Left to Solve items, or run BM25 retrieval
python examples/query_atlas.py --top 10
python examples/query_atlas.py --field number-theory --status open
python examples/query_atlas.py --search "positivity localization collatz"
python scripts/search_all_problems.py --query "Sidon" --prize-only
python rag/retriever.py "why is P vs NP so hard"

# Rebuild generated views and RAG corpus after editing data/problems.yaml
python scripts/generate.py
python scripts/build_indexes.py
python rag/build_corpus.py
python scripts/build_data_manifest.py

# Build and verify the Lean 4.35.0 formal core (zero Mathlib, autoImplicit = false, 8 domains, 102 audited declarations)
cd lean
lake build Challenge Solution NonVacuity Adversarial
lake env lean VerifyAxioms.lean
python ../scripts/test_lean_negative.py
# On Linux with bubblewrap (all 6 independent Lean 4.35.0 kernels):
lake check --paranoid
lake comparator --config comparator.json --paranoid
```

## The Master Ranking

Problems are ordered by a transparent, reproducible **Composite Severity Score
(CSS)** that blends intrinsic difficulty, centrality to mathematics, age, and
how far a resolution still feels. The full formula lives in
[docs/methodology/RANKING.md](docs/methodology/RANKING.md). Hardest + oldest at
the top; most tractable at the bottom.

<!-- BEGIN:RANKING (auto-generated by scripts/generate.py — do not edit) -->

| # | Problem | Field | Posed | CSS | Difficulty | Status | 🏛️ |
|---|---------|-------|-------|-----|-----------|--------|----|
| 1 | [The Riemann Hypothesis](problems/riemann-hypothesis/README.md) | Analytic Number Theory | 1859 | 89.933 | 99 | `open` | ✅ |
| 2 | [Goldbach's Conjecture](problems/goldbach-conjecture/README.md) | Number Theory | 1742 | 87.933 | 92 | `open` |  |
| 3 | [The Grand Riemann Hypothesis](problems/grand-riemann-hypothesis/README.md) | Analytic Number Theory | 1884 | 84.967 | 98 | `open` |  |
| 4 | [Gauss's Class Number Problem for Real Quadratic Fields](problems/class-number-problem-real-quadratic/README.md) | Number Theory | 1801 | 83.4 | 91 | `open` |  |
| 5 | [P versus NP](problems/p-versus-np/README.md) | Computational Complexity Theory | 1971 | 81.967 | 98 | `open` | ✅ |
| 6 | [The Hodge Conjecture](problems/hodge-conjecture/README.md) | Algebraic Geometry | 1950 | 79.967 | 97 | `open` | ✅ |
| 7 | [The Twin Prime Conjecture](problems/twin-prime-conjecture/README.md) | Number Theory | 1849 | 79.6 | 90 | `active-progress` |  |
| 8 | [The Birch and Swinnerton-Dyer Conjecture](problems/birch-swinnerton-dyer/README.md) | Number Theory | 1965 | 78.867 | 96 | `open` | ✅ |
| 9 | [Existence of Odd Perfect Numbers](problems/odd-perfect-numbers/README.md) | Number Theory | 300 BCE | 78.3 | 85 | `open` |  |
| 10 | [The Dirichlet Divisor Problem](problems/dirichlet-divisor-problem/README.md) | Analytic Number Theory | 1849 | 77.4 | 88 | `active-progress` |  |
| 11 | [Infinitude of Mersenne Primes](problems/mersenne-primes-infinitude/README.md) | Number Theory | 1644 | 76.6 | 84 | `open` |  |
| 12 | [The Continuum Hypothesis](problems/continuum-hypothesis/README.md) | Set Theory & Mathematical Logic | 1878 | 76.267 | 90 | `independent` |  |
| 13 | [Hilbert's Sixteenth Problem (Second Part)](problems/hilbert-sixteenth-problem/README.md) | Dynamical Systems | 1900 | 76.1 | 94 | `open` |  |
| 14 | [Yang–Mills Existence and Mass Gap](problems/yang-mills-mass-gap/README.md) | Mathematical Physics | 2000 | 75.333 | 97 | `open` | ✅ |
| 15 | [Resolution of Singularities in Positive Characteristic](problems/resolution-of-singularities-char-p/README.md) | Algebraic Geometry | 1964 | 75.033 | 94 | `active-progress` |  |
| 16 | [Navier–Stokes Existence and Smoothness](problems/navier-stokes-smoothness/README.md) | Partial Differential Equations | 2000 | 74.733 | 95 | `open` | ✅ |
| 17 | [The Bateman–Horn Conjecture](problems/bateman-horn-conjecture/README.md) | Analytic Number Theory | 1962 | 74.467 | 93 | `open` |  |
| 18 | [Cramér's Conjecture on Prime Gaps](problems/cramer-conjecture/README.md) | Analytic Number Theory | 1936 | 74.3 | 91 | `open` |  |
| 19 | [The abc Conjecture](problems/abc-conjecture/README.md) | Number Theory | 1985 | 73.833 | 93 | `disputed-claim` |  |
| 20 | [The Tate Conjecture](problems/tate-conjecture/README.md) | Arithmetic Geometry | 1963 | 72.6 | 92 | `open` |  |
| 21 | [Legendre's Conjecture](problems/legendre-conjecture/README.md) | Number Theory | 1808 | 71.333 | 83 | `open` |  |
| 22 | [Erdős Problem 142 (Asymptotic Density of k-AP-Free Sets)](problems/erdos-szemeredi-asymptotic-bounds/README.md) | Extremal Combinatorics | 1973 | 71.133 | 91 | `active-progress` |  |
| 23 | [The Cohen–Lenstra Heuristics](problems/cohen-lenstra-heuristics/README.md) | Number Theory | 1984 | 70.5 | 91 | `active-progress` |  |
| 24 | [Polignac's Conjecture](problems/polignac-conjecture/README.md) | Number Theory | 1849 | 70.3 | 86 | `active-progress` |  |
| 25 | [Vojta's Conjecture](problems/vojta-conjecture/README.md) | Diophantine Geometry | 1987 | 70.3 | 93 | `open` |  |
| 26 | [The Inverse Galois Problem](problems/inverse-galois-problem/README.md) | Algebra | 1892 | 69.933 | 88 | `active-progress` |  |
| 27 | [The Hardy–Littlewood k-tuple Conjecture](problems/hardy-littlewood-k-tuple/README.md) | Analytic Number Theory | 1923 | 69.567 | 87 | `active-progress` |  |
| 28 | [The Collatz Conjecture](problems/collatz-conjecture/README.md) | Number Theory / Dynamical Systems | 1937 | 69.333 | 91 | `open` |  |
| 29 | [The Kakeya Conjecture](problems/kakeya-conjecture/README.md) | Harmonic Analysis | 1971 | 69.167 | 90 | `active-progress` |  |
| 30 | [The Erdős–Turán Conjecture on Additive Bases](problems/erdos-turan-additive-bases/README.md) | Number Theory | 1941 | 68.467 | 87 | `open` |  |
| 31 | [The Jacobian Conjecture](problems/jacobian-conjecture/README.md) | Algebraic Geometry | 1939 | 68.4 | 89 | `open` |  |
| 32 | [The Restriction Conjecture](problems/restriction-conjecture/README.md) | Harmonic Analysis | 1967 | 67.733 | 89 | `active-progress` |  |
| 33 | [The Bombieri–Lang Conjecture](problems/bombieri-lang-conjecture/README.md) | Diophantine Geometry | 1980 | 67.567 | 90 | `open` |  |
| 34 | [The Novikov Conjecture](problems/novikov-conjecture/README.md) | Geometric Topology | 1965 | 67.567 | 89 | `active-progress` |  |
| 35 | [Bunyakovsky's Conjecture](problems/bunyakovsky-conjecture/README.md) | Number Theory | 1857 | 67.367 | 85 | `open` |  |
| 36 | [Hadwiger's Conjecture (Graph Coloring)](problems/hadwiger-conjecture/README.md) | Graph Theory | 1943 | 67.133 | 87 | `active-progress` |  |
| 37 | [The Littlewood Conjecture](problems/littlewood-conjecture/README.md) | Diophantine Approximation | 1930 | 67.0 | 88 | `active-progress` |  |
| 38 | [The Happy Ending Problem (Erdős–Szekeres Conjecture)](problems/erdos-happy-ending-problem/README.md) | Combinatorial Geometry | 1935 | 66.967 | 83 | `active-progress` |  |
| 39 | [Schinzel's Hypothesis H](problems/schinzel-hypothesis-h/README.md) | Number Theory | 1958 | 66.733 | 88 | `open` |  |
| 40 | [The Invariant Subspace Problem](problems/invariant-subspace-problem/README.md) | Functional Analysis | 1935 | 66.567 | 88 | `active-progress` |  |
| 41 | [The Bochner–Riesz Conjecture](problems/bochner-riesz-conjecture/README.md) | Harmonic Analysis | 1936 | 66.4 | 87 | `active-progress` |  |
| 42 | [The Beck–Fiala Conjecture](problems/beck-fiala-conjecture/README.md) | Combinatorics | 1981 | 65.9 | 86 | `active-progress` |  |
| 43 | [Schanuel's Conjecture](problems/schanuel-conjecture/README.md) | Transcendental Number Theory | 1960 | 65.9 | 88 | `open` |  |
| 44 | [The Smooth 4-Dimensional Poincaré Conjecture](problems/smooth-4d-poincare-conjecture/README.md) | Geometric Topology | 1982 | 65.533 | 90 | `open` |  |
| 45 | [The Fontaine–Mazur Conjecture](problems/fontaine-mazur-conjecture/README.md) | Number Theory | 1995 | 65.467 | 90 | `active-progress` |  |
| 46 | [The Erdős–Turán Sidon Set Conjecture (Erdős Problem 30)](problems/erdos-sidon-sets-problem-30/README.md) | Combinatorics | 1941 | 65.367 | 84 | `active-progress` |  |
| 47 | [The Baum–Connes Conjecture](problems/baum-connes-conjecture/README.md) | Operator Algebras | 1982 | 64.733 | 88 | `active-progress` |  |
| 48 | [The Zilber–Pink Conjecture](problems/zilber-pink-conjecture/README.md) | Diophantine Geometry | 2005 | 64.4 | 90 | `open` |  |
| 49 | [The Borel Conjecture](problems/borel-conjecture/README.md) | Geometric Topology | 1953 | 64.167 | 86 | `active-progress` |  |
| 50 | [Grothendieck's Section Conjecture](problems/section-conjecture/README.md) | Arithmetic Geometry | 1983 | 64.167 | 89 | `open` |  |
| 51 | [The Unique Games Conjecture](problems/unique-games-conjecture/README.md) | Computational Complexity Theory | 2002 | 64.1 | 86 | `active-progress` |  |
| 52 | [The Elliott–Halberstam Conjecture](problems/elliott-halberstam-conjecture/README.md) | Analytic Number Theory | 1968 | 64.067 | 85 | `active-progress` |  |
| 53 | [The MLC Conjecture (Mandelbrot Locally Connected)](problems/mandelbrot-locally-connected/README.md) | Complex Dynamics | 1982 | 63.733 | 88 | `active-progress` |  |
| 54 | [The Chowla Conjecture](problems/chowla-conjecture/README.md) | Analytic Number Theory | 1965 | 63.667 | 86 | `active-progress` |  |
| 55 | [Arnold Diffusion (Genericity)](problems/arnold-diffusion/README.md) | Dynamical Systems | 1964 | 62.933 | 87 | `active-progress` |  |
| 56 | [The Dixmier Conjecture](problems/dixmier-conjecture/README.md) | Algebra | 1968 | 62.067 | 86 | `open` |  |
| 57 | [Montgomery's Pair Correlation Conjecture](problems/montgomery-pair-correlation/README.md) | Analytic Number Theory | 1973 | 62.033 | 84 | `open` |  |
| 58 | [The Birkhoff Conjecture (Integrable Billiards)](problems/birkhoff-conjecture/README.md) | Dynamical Systems | 1927 | 62.0 | 84 | `active-progress` |  |
| 59 | [The Černý Conjecture](problems/cerny-conjecture/README.md) | Combinatorics | 1964 | 61.933 | 82 | `active-progress` |  |
| 60 | [Furstenberg's ×2 ×3 Conjecture](problems/furstenberg-conjecture/README.md) | Ergodic Theory | 1967 | 61.933 | 85 | `active-progress` |  |
| 61 | [Artin's Primitive Root Conjecture](problems/artin-primitive-root-conjecture/README.md) | Number Theory | 1927 | 61.9 | 82 | `active-progress` |  |
| 62 | [Self-Avoiding Walk (Scaling & Connective Constant)](problems/self-avoiding-walk/README.md) | Probability Theory | 1947 | 61.667 | 84 | `active-progress` |  |
| 63 | [The Whitehead Asphericity Conjecture](problems/whitehead-asphericity-conjecture/README.md) | Algebraic Topology | 1941 | 61.467 | 84 | `open` |  |
| 64 | [Lehmer's Mahler Measure Conjecture](problems/lehmer-mahler-measure-conjecture/README.md) | Number Theory | 1933 | 61.4 | 83 | `open` |  |
| 65 | [The Weinstein Conjecture](problems/weinstein-conjecture/README.md) | Symplectic Geometry | 1979 | 61.033 | 85 | `active-progress` |  |
| 66 | [The KPZ Universality Conjecture](problems/kpz-universality/README.md) | Probability Theory | 1986 | 60.967 | 86 | `active-progress` |  |
| 67 | [Conway's 99-Graph Problem](problems/conway-99-graph-problem/README.md) | Graph Theory | 1970 | 60.933 | 84 | `open` |  |
| 68 | [The Hilbert–Smith Conjecture](problems/hilbert-smith-conjecture/README.md) | Geometric Topology | 1933 | 60.8 | 83 | `active-progress` |  |
| 69 | [The Zariski Cancellation Problem](problems/zariski-cancellation-problem/README.md) | Algebraic Geometry | 1949 | 60.733 | 84 | `active-progress` |  |
| 70 | [The Palis Conjecture (Finitude / Density of Attractors)](problems/palis-conjecture/README.md) | Dynamical Systems | 1995 | 60.467 | 86 | `open` |  |
| 71 | [The Inscribed Square Problem (Toeplitz)](problems/inscribed-square-problem/README.md) | Geometric Topology | 1911 | 60.267 | 80 | `active-progress` |  |
| 72 | [The Falconer Distance Conjecture](problems/falconer-distance-conjecture/README.md) | Geometric Measure Theory | 1985 | 60.033 | 85 | `active-progress` |  |
| 73 | [Pillai's Conjecture](problems/pillai-conjecture/README.md) | Number Theory | 1931 | 59.833 | 80 | `open` |  |
| 74 | [The Hadwiger Covering Conjecture](problems/hadwiger-covering-conjecture/README.md) | Discrete Geometry | 1957 | 59.6 | 83 | `open` |  |
| 75 | [Vaught's Conjecture](problems/vaught-conjecture/README.md) | Mathematical Logic | 1961 | 59.333 | 82 | `open` |  |
| 76 | [The Cherlin–Zilber Algebraicity Conjecture](problems/cherlin-zilber-conjecture/README.md) | Mathematical Logic | 1979 | 59.133 | 84 | `active-progress` |  |
| 77 | [Köthe's Conjecture](problems/kothe-conjecture/README.md) | Ring Theory | 1930 | 59.1 | 80 | `open` |  |
| 78 | [Sarnak's Möbius Disjointness Conjecture](problems/sarnak-mobius-conjecture/README.md) | Dynamical Systems | 2010 | 58.567 | 84 | `active-progress` |  |
| 79 | [Greenberg's Conjecture](problems/greenberg-conjecture/README.md) | Number Theory | 1976 | 58.533 | 83 | `open` |  |
| 80 | [The Sunflower Conjecture](problems/sunflower-conjecture/README.md) | Extremal Combinatorics | 1960 | 58.3 | 80 | `active-progress` |  |
| 81 | [The Four Exponentials Conjecture](problems/four-exponentials-conjecture/README.md) | Transcendental Number Theory | 1944 | 58.167 | 80 | `open` |  |
| 82 | [The Catalan–Dickson Conjecture (Aliquot Sequences)](problems/catalan-dickson-conjecture/README.md) | Number Theory | 1888 | 58.0 | 74 | `open` |  |
| 83 | [The Erdős Unit Distance Problem (Disproved 2026)](problems/unit-distance-problem/README.md) | Combinatorial Geometry | 1946 | 57.533 | 84 | `recently-resolved` |  |
| 84 | [The Volume Conjecture](problems/volume-conjecture/README.md) | Knot Theory | 1997 | 57.533 | 82 | `active-progress` |  |
| 85 | [The Hadwiger–Nelson Problem](problems/hadwiger-nelson-problem/README.md) | Combinatorial Geometry | 1950 | 57.367 | 78 | `active-progress` |  |
| 86 | [The Hadamard Matrix Conjecture](problems/hadamard-matrix-conjecture/README.md) | Combinatorics | 1893 | 57.167 | 76 | `active-progress` |  |
| 87 | [The Slice–Ribbon Conjecture](problems/slice-ribbon-conjecture/README.md) | Knot Theory | 1962 | 57.067 | 80 | `open` |  |
| 88 | [The Cycle Double Cover Conjecture](problems/cycle-double-cover-conjecture/README.md) | Graph Theory | 1973 | 57.033 | 80 | `open` |  |
| 89 | [Lehmer's Conjecture on the Ramanujan Tau Function](problems/lehmer-tau-conjecture/README.md) | Number Theory | 1947 | 56.967 | 78 | `open` |  |
| 90 | [Carmichael's Totient Conjecture](problems/carmichael-totient-conjecture/README.md) | Number Theory | 1907 | 56.933 | 75 | `open` |  |
| 91 | [The Erdős–Hajnal Conjecture](problems/erdos-hajnal-conjecture/README.md) | Graph Theory | 1989 | 56.867 | 80 | `active-progress` |  |
| 92 | [Brocard's Problem](problems/brocard-problem/README.md) | Number Theory | 1876 | 56.8 | 74 | `open` |  |
| 93 | [The Caccetta–Häggkvist Conjecture](problems/caccetta-haggkvist-conjecture/README.md) | Graph Theory | 1978 | 56.8 | 82 | `open` |  |
| 94 | [The Reconstruction Conjecture (Ulam)](problems/reconstruction-conjecture/README.md) | Graph Theory | 1941 | 56.567 | 78 | `open` |  |
| 95 | [Ryser's Conjecture (Hypergraph Covering)](problems/ryser-conjecture/README.md) | Combinatorics | 1971 | 56.567 | 80 | `active-progress` |  |
| 96 | [The Eilenberg–Ganea Conjecture](problems/eilenberg-ganea-conjecture/README.md) | Algebraic Topology | 1957 | 56.2 | 79 | `open` |  |
| 97 | [The Kelvin Problem (Optimal Space Partition)](problems/kelvin-problem/README.md) | Geometry | 1887 | 55.967 | 72 | `open` |  |
| 98 | [The Andrews–Curtis Conjecture](problems/andrews-curtis-conjecture/README.md) | Geometric Group Theory | 1965 | 55.667 | 81 | `active-progress` |  |
| 99 | [The Zeeman Conjecture](problems/zeeman-conjecture/README.md) | Geometric Topology | 1964 | 55.533 | 79 | `open` |  |
| 100 | [The Connes Embedding Problem (Resolved 2020)](problems/connes-embedding-aftermath/README.md) | Operator Algebras | 1976 | 55.433 | 80 | `recently-resolved` |  |
| 101 | [The Lonely Runner Conjecture](problems/lonely-runner-conjecture/README.md) | Number Theory / Combinatorics | 1967 | 55.333 | 79 | `active-progress` |  |
| 102 | [The Telescope Conjecture (Disproved 2023)](problems/telescope-conjecture/README.md) | Algebraic Topology | 1984 | 55.3 | 85 | `recently-resolved` |  |
| 103 | [The Riesel Problem](problems/riesel-problem/README.md) | Number Theory | 1956 | 55.267 | 76 | `active-progress` |  |
| 104 | [The Beal Conjecture](problems/beal-conjecture/README.md) | Number Theory | 1993 | 55.0 | 82 | `open` |  |
| 105 | [Giuga's Conjecture](problems/giuga-conjecture/README.md) | Number Theory | 1950 | 54.667 | 76 | `open` |  |
| 106 | [Lehmer's Totient Problem](problems/lehmer-totient-problem/README.md) | Number Theory | 1932 | 54.367 | 77 | `open` |  |
| 107 | [The Total Coloring Conjecture](problems/total-coloring-conjecture/README.md) | Graph Theory | 1965 | 54.067 | 76 | `active-progress` |  |
| 108 | [Hall's Conjecture](problems/hall-conjecture/README.md) | Number Theory | 1971 | 53.867 | 76 | `open` |  |
| 109 | [Brennan's Conjecture](problems/brennan-conjecture/README.md) | Complex Analysis | 1978 | 53.4 | 78 | `open` |  |
| 110 | [The Union-Closed Sets Conjecture (Frankl)](problems/union-closed-sets-conjecture/README.md) | Combinatorics | 1979 | 53.033 | 76 | `active-progress` |  |
| 111 | [The Erdős–Straus Conjecture](problems/erdos-straus-conjecture/README.md) | Number Theory | 1948 | 53.0 | 75 | `active-progress` |  |
| 112 | [The Graceful Tree Conjecture (Ringel–Kotzig)](problems/graceful-tree-conjecture/README.md) | Combinatorics | 1964 | 52.333 | 76 | `active-progress` |  |
| 113 | [Grimm's Conjecture](problems/grimm-conjecture/README.md) | Number Theory | 1969 | 51.3 | 78 | `open` |  |
| 114 | [Seymour's Second Neighborhood Conjecture](problems/seymour-second-neighborhood-conjecture/README.md) | Graph Theory | 1990 | 50.0 | 74 | `open` |  |
| 115 | [The 1/3–2/3 Conjecture](problems/one-third-two-thirds-conjecture/README.md) | Order Theory | 1968 | 49.867 | 72 | `active-progress` |  |
| 116 | [Singmaster's Conjecture](problems/singmaster-conjecture/README.md) | Combinatorics | 1971 | 48.067 | 73 | `active-progress` |  |
| 117 | [Gilbreath's Conjecture](problems/gilbreath-conjecture/README.md) | Number Theory | 1958 | 47.933 | 72 | `open` |  |
| 118 | [Sendov's Conjecture](problems/sendov-conjecture/README.md) | Complex Analysis | 1959 | 46.967 | 70 | `active-progress` |  |
| 119 | [The Moving Sofa Problem](problems/moving-sofa-problem/README.md) | Geometry | 1966 | 46.6 | 70 | `active-progress` |  |
| 120 | [Crouzeix's Conjecture](problems/crouzeix-conjecture/README.md) | Matrix Analysis | 2004 | 43.967 | 71 | `active-progress` |  |

<!-- END:RANKING -->

## Explore the atlas

Beyond the per-problem dossiers, the atlas ships cross-cutting views (generated
by `scripts/build_indexes.py`):

- 🗺️ [By field](docs/indexes/by-field.md) · [By status](docs/indexes/by-status.md) · [By era posed](docs/indexes/by-century.md)
- 👤 [Originators index](docs/indexes/originators.md) — every mathematician → the problems they posed
- ✅ [Verification dashboard](docs/indexes/verification.md) — provenance of all 2,782 citations (537 API-verified in exact 1-to-1 log bijection)
- 📖 [Glossary](docs/glossary.md) — the recurring concepts that thread the dossiers
- 🌐 [External research programs](docs/external/PROGRAMS.md) — daily full mirror of all 26 [Left to Solve](https://lefttosolve.com/programs) programs (62,790 targets across Erdős, OEIS, MathOverflow, arXiv Abstracts, Wikipedia, Millennium, Green's 100, Kourovka, …; metadata only, 27 `< 4 MB` shards, carved out of CC BY 4.0) with a `114/120` [Atlas crosswalk](docs/external/CROSSWALK.md) and unified offline search (`scripts/search_all_problems.py`); third-party data, review signals only, never auto-changes an Atlas status

## Repository map

```
unsolved-mathematics/
├── README.md                 ← you are here
├── RANKING.md                ← the full ranked table (generated)
├── ARCHITECTURE.md           ← how the whole machine fits together
├── PHILOSOPHY.md             ← why this exists and the principles behind it
├── data/
│   ├── problems.yaml         ← THE single source of truth
│   ├── problems.json         ← generated machine registry (computed ranks/CSS)
│   └── external/             ← daily Left to Solve program mirror + crosswalk (third-party)
├── schema/                   ← JSON Schemas for problems, papers, people
├── scripts/                  ← generate.py (build engine), validate, helpers
├── problems/
│   └── <slug>/               ← one self-contained dossier per problem (rank in metadata)
├── rag/                      ← corpus builder, embedder, retriever
├── meta-analyses/            ← AI-assisted meta-analysis write-ups, one per problem
├── docs/
│   ├── architecture/         ← ER model, data model, diagrams
│   ├── methodology/          ← ranking formula, sourcing standards
│   ├── review/               ← AI-review process, panel template, register, academic review
│   └── kanban/               ← the research board
├── AUTHORS.md · SUBMISSIONS.md · ERRATA.md  ← credit · outreach · post-release errata
├── ro-crate-metadata.json · croissant.json  ← FAIR RO-Crate 1.1 & Croissant 1.0 metadata
├── lean/                     ← standalone 8-domain, 6-kernel Lean 4.35.0 core (66 thms + 36 checks)
├── paper/                    ← compiled AMS-LaTeX white paper PDF & arXiv source bundle
└── .github/                  ← CI/CD, Pages blueprint, SLSA releases, 10-class issue forms
```

## Formal Verification Core (`lean/`)

`v0.8.3` ships the **zero-Mathlib, pure Lean 4.35.0** formal package (`autoImplicit = false`, commit `eb6cafb7`) verifying **66 headline theorems, 16 concrete non-vacuity witnesses, and 20 explicit adversarial false-variant refutations** (**102 audited declarations**, 14 requiring zero axioms) across **eight** canonical open-problem domains:

- **Collatz Conjecture (28 theorems):** affine cylinder law, exact intercept law, Terras parity-word bijection, descent certificate soundness, no finite subcritical cover, spine ladder identity, unconditional **Positivity Localization** ($\rho_w \le -1$), the **$3n-1$ sibling comparison** (`thm_collatz_epsilon_invariance_barrier`: the $3n-1$ map shares the Terras bijection and has positive cycles at `5` and `17`; the inference that arguments blind to the sign of $\varepsilon$ cannot settle $3n+1$ is a heuristic, not a formalized meta-theorem), Böhm–Sontacchi exact cycle equation, parity-word cocycle law, negative cycles of true $3n+1$ (`-5`, `-17`), zero/intercept/length invariants, positive-cycle subcriticality ($3^o < 2^d$), **unconditional 1- & 2-odd-step positive-cycle exclusion for ALL $d \ge 1$**, **2-adic cylinder isometry**, **periodic spine congruence**, **Odd-Unit-Lock exact periodic-echo valuation isometry** ($v_2(\rho_w - \rho_v) = \operatorname{lcp}(w^\infty, v^\infty)$), **unconditional Fine–Wilf spine valuation ceiling** ($v_2(\rho_w - \rho_v) < |w| + |v| - \gcd(|w|,|v|)$), **exhaustive $1 \le d \le 7$ positive-cycle classification & odd-period exclusion**, and **zero-workspace catalytic reversible cylinder evaluation**.
- **Erdős–Straus Conjecture (5 theorems):** Mordell mod-840 covering (`834/840 = 99.286%`), multiplicative closure (prime reduction), cyclic symmetry, base range $2 \le n \le 30$, and all 6 smallest exceptional squares $\{121, 169, 289, 361, 529, 841\}$.
- **Lonely Runner Conjecture (8 theorems — complete through $n = 3$):** all-$n$ rational sharpness $\delta \le 1/(n+1)$, constructive base cases $n \in \{1, 2\}$, symmetry group (speed scaling, period shift, time reversal), the $t = 1/4$ family (`thm_lonely_runner_n3_nondiv4`: speed triples with no speed divisible by 4, i.e. 27 of the 64 residue classes of speed triples mod 4), and a **4-runner Lonely Runner theorem (`thm_lonely_runner_n3`) for all positive integer speed triples** via 2-adic strong induction, quarter-shift counting, Bézout congruence, and exact rational nudging. The 4-runner case is a classical result (Betke–Wills 1972; Cusick 1973); the conjecture itself is proved for up to 13 runners in recent preprints (Rosenfeld, `arXiv:2509.14111`, 8 runners; Trakulthongchai, `arXiv:2511.22427`, 9 and 10; Sungkawichai & Trakulthongchai, `arXiv:2604.23906`, 11 to 13), well beyond the cases formalized here.
- **Brocard's Problem (7 theorems):** Brown solutions `(4,5), (5,11), (7,71)`, mod-3/4/10 modular invariants, and exhaustive classification through $n \le 20$ ($20!+1 = 2{,}432{,}902{,}008{,}176{,}640{,}001$, zero `native_decide`).
- **Primes & Twin Primes (4 theorems):** Euclid's infinitude of primes, arbitrary prime gaps via $(k+1)!+2$, oddness of primes $\ge 3$, and twin-prime mod-6 rigidity ($p \equiv 5 \pmod 6$ for $p \ge 4$).
- **Goldbach's Conjecture (3 theorems):** exhaustive certified prime-pair decomposition for all even $4 \le n \le 100$, odd binary prime-sum obstruction ($p=2 \lor q=2$), and binary Goldbach failure at $11$.
- **Odd Perfect Numbers & Mersenne Primes (7 theorems):** algebraic proof of Mersenne prime exponent necessity ($2^a - 1 \mid 2^{ab} - 1$), first four even perfect numbers $\{6, 28, 496, 8128\}$, exhaustive odd-perfect exclusion $n \le 100$, **Complete Euclid–Euler Biconditional Theorem** (`thm_euclid_even_perfect`, `thm_euler_even_perfect_converse`, `thm_euclid_euler_even_perfect_iff`) for ALL even perfect numbers (with `divSum_eq_divSumLin` proved unconditionally $\forall n \in \mathbb{N}$), and **Euler's 1750 Mersenne Prime Divisor Congruence (`thm_mersenne_prime_divisor_congruence`: $2p \mid q - 1$)** via Fermat's Little Theorem.
- **Ramsey Theory (4 theorems):** exact first-principles determinations of **$R(3,3) = 6$** ($K_6$ pigeonhole + $C_5$ on $K_5$) and **$R(3,4) = 9$** (Handshaking Lemma $9 \times 3 = 27$ odd contradiction on $K_9$ + explicit symmetric circulant $C_8(1,4,7)$ coloring on $K_8$).

The 66 headline theorems are checked against the specifications in [`lean/Challenge.lean`](lean/Challenge.lean) by `lake comparator --paranoid` (`lean/comparator.json` lists exactly these 66); the 16 witnesses and 20 refutations are covered by `lake build`, `leanchecker-paranoid --fresh`, and the six-kernel `lake check --paranoid`. The theorems are paired with concrete witnesses in [`lean/NonVacuity.lean`](lean/NonVacuity.lean), false-variant refutations in [`lean/Adversarial.lean`](lean/Adversarial.lean), and live negative kernel rejection (`scripts/test_lean_negative.py`), axiom-checked by [`lean/VerifyAxioms.lean`](lean/VerifyAxioms.lean), documented in [`lean/STATEMENT_FIDELITY.md`](lean/STATEMENT_FIDELITY.md), and replayed across all 6 independent Lean 4.35.0 kernels ([`lean/six_kernel_audit.txt`](lean/six_kernel_audit.txt) + `bwrap`-sandboxed Ubuntu CI). **None of these theorems claims to resolve the underlying open conjectures.**

An independent statement audit on 2026-11-26 ([audit log](https://github.com/0thernes/0thernes-research-archive/blob/main/docs/reviews/2026-11-26-statement-audit.md)) covered `v0.5.0` (commit `0604df5`, 69 declarations) and flagged six items (`3n-1` barrier overstatement, Lonely Runner 13-runner prior art & 27/64 mod-4 coverage, `Challenge.lean` `sorry` disclosure, `Collatz.lean` docstrings, and the missing Lean `divSum = ∑_{d|n} d` lemma). All six items are resolved in `v0.7.0` (including the unconditional Lean proof `divSum_eq_divSumLin` in `PerfectNumbers.lean`); the 33 declarations added in `v0.6.0`–`v0.7.0` have not yet undergone a separate independent statement audit. See [`ERRATA.md`](ERRATA.md).

### 5-Second Proof Audit (Verbatim `#print axioms`, CI-Checked by `scripts/check_readme_axioms.py`)

<!-- AXIOMS:START -->
```text
'FormalAtlas.Challenge.thm_collatz_cylinder_affine_law' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_exact_intercept_law' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_terras_parity_word_bijection' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_descent_certificate_sound' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_no_finite_subcritical_cover' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_spine_ladder_identity' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_positivity_localization' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_epsilon_invariance_barrier' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_cycle_equation' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_parity_word_append' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_negative_cycles' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_zero_fixed_point' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_intercept_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_parity_word_length' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_positive_cycle_has_odd_step' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_positive_cycle_intercept_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_positive_cycle_subcritical' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_no_positive_cycle_d1' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_positive_cycle_one_odd' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_positive_cycle_two_odd' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_2adic_isometry' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_periodic_spine_congruence' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_odd_unit_lock_valuation_isometry' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_fine_wilf_spine_ceiling' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_trivial_cycle_orbit' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_no_nontrivial_positive_cycle_le_7' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_no_positive_cycle_odd_le_7' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_catalytic_reversible_cylinder' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_erdos_straus_mordell_840' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_erdos_straus_multiplicative_closure' depends on axioms: [propext]
'FormalAtlas.Challenge.thm_erdos_straus_mordell_exceptions_small' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_erdos_straus_symmetry' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_erdos_straus_all_le_30' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_sharpness_all_n' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_n1' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_n2' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_speed_scaling' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_period_shift' depends on axioms: [propext]
'FormalAtlas.Challenge.thm_lonely_runner_neg_time' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_n3_nondiv4' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_n3' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_brocard_brown_solutions' does not depend on any axioms
'FormalAtlas.Challenge.thm_brocard_exhaustive_le_12' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_brocard_mod4_ge_4' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_brocard_exhaustive_le_15' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_brocard_not_div3_ge_3' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_brocard_mod10_ge_5' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_brocard_exhaustive_le_20' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_euclid_infinitely_many_primes' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_arbitrary_prime_gaps' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_prime_odd_ge_3' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_twin_prime_mod6' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_goldbach_even_le_100' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_goldbach_odd_binary_obstruction' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_goldbach_binary_fails_at_11' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_mersenne_exponent_prime' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_perfect_numbers_first_four' does not depend on any axioms
'FormalAtlas.Challenge.thm_no_odd_perfect_le_100' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_euclid_even_perfect' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_euler_even_perfect_converse' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_euclid_euler_even_perfect_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_mersenne_prime_divisor_congruence' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_ramsey_R33_upper' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_ramsey_R33_lower' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_ramsey_R34_upper' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_ramsey_R34_lower' depends on axioms: [propext, Quot.sound]
'FormalAtlas.NonVacuity.witness_descent_certificate' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.NonVacuity.witness_positivity_localization' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_subcritical_positive_cycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.NonVacuity.witness_erdos_straus_hypotheses' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_lonely_runner_concrete' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_brocard_non_solution' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_twin_primes_concrete' depends on axioms: [propext, Quot.sound]
'FormalAtlas.NonVacuity.witness_goldbach_100' depends on axioms: [propext, Quot.sound]
'FormalAtlas.NonVacuity.witness_mersenne_31' depends on axioms: [propext, Quot.sound]
'FormalAtlas.NonVacuity.witness_lonely_runner_n3_concrete' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_lonely_runner_n3_div4' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_euclid_perfect_28' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.NonVacuity.witness_mersenne_divisor_23_of_M11' depends on axioms: [propext, Quot.sound]
'FormalAtlas.NonVacuity.witness_collatz_two_odd_trivial_cycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.NonVacuity.witness_odd_unit_lock_fine_wilf' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_catalytic_cylinder' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_erdos_straus_zero_denom_blocked' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Adversarial.adv_erdos_straus_wrong_witness_refuted' does not depend on any axioms
'FormalAtlas.Adversarial.adv_collatz_no_universal_descent_d1' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_collatz_positivity_required_for_no_nontrivial_cycles' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_collatz_positivity_converse_false' does not depend on any axioms
'FormalAtlas.Adversarial.adv_lonely_runner_strict_threshold_fails' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_lonely_runner_bad_time_refuted' does not depend on any axioms
'FormalAtlas.Adversarial.adv_brocard_false_candidates_refuted' does not depend on any axioms
'FormalAtlas.Adversarial.adv_non_primes_refuted' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Adversarial.adv_mersenne_converse_false' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Adversarial.adv_non_perfect_refuted' does not depend on any axioms
'FormalAtlas.Adversarial.adv_twin_prime_mod6_needs_ge_4' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Adversarial.adv_ramsey_R33_not_le_5' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Adversarial.adv_goldbach_requires_even' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Adversarial.adv_ramsey_R34_not_le_8' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Adversarial.adv_collatz_no_d1_positive_fixed_point' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_collatz_no_nontrivial_low_odd_cycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_even_non_mersenne_not_perfect' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_collatz_no_odd_period_le_7' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_collatz_distinct_spines_bounded_v2' depends on axioms: [propext, Classical.choice, Quot.sound]
```
<!-- AXIOMS:END -->

## Integrity, Limitations & Honest Provenance

Mathematics has no tolerance for bluffing, and neither does this atlas.

- **Claims & Falsifiability:** Every substantive claim carries an explicit *"What would prove us wrong"* trigger in [`CLAIMS.md`](CLAIMS.md).
- **Known Limitations & Errata:** Read [`LIMITATIONS.md`](LIMITATIONS.md), [`ERRATA.md`](ERRATA.md), our Cross-Atlas audit ([`docs/CROSS_ATLAS_AUDIT_2026-11-25.md`](docs/CROSS_ATLAS_AUDIT_2026-11-25.md)), and our Master Hardening Index & three-cycle 10-class audits ([`HARDENING_INDEX.md`](HARDENING_INDEX.md), [`docs/reviews/2026-11-25-three-cycle-hardening-audit.md`](docs/reviews/2026-11-25-three-cycle-hardening-audit.md)) before citing any section.
- **Primary-Source Citation & Retraction Audit:** Of 646 identifier-bearing paper rows checked live against `export.arxiv.org` and `api.crossref.org` (`data/citation-verification-log.json`), **537 are API-verified in exact 1-to-1 bijection** with all 120 `problems/*/papers.md` tables (zero duplicate or bare arXiv IDs, enforced offline by `scripts/check_dossiers.py --strict`) and **109 invalid/hallucinated identifiers from the original corpus were stripped** (downgraded honestly to `—` / `needs-verification`). All **287 verified DOIs** were additionally audited against Crossref + DataCite retraction metadata (`data/retraction-audit.json`): **0 retractions**, **3 publisher errata/corrections** logged, `0` network errors. The remaining 2,245 pre-DOI / non-verified rows (`2,782` total) are research leads, not API-verified citations.
- **No problem is ever called "solved" without verified primary-source evidence:** `scripts/proof_claim_sweep.py` enforces zero unhedged proof claims across all active prose in CI.
- **Scores are editorial estimates**, documented and deterministic (`docs/methodology/RANKING.md`, `CURRENT_YEAR = 2026`) — never objective truth.

See [`PHILOSOPHY.md`](PHILOSOPHY.md), [`docs/methodology/SOURCING.md`](docs/methodology/SOURCING.md), and [`SECURITY.md`](SECURITY.md).

## Maintenance Status

**Status: active** (`v0.8.3`, updated `2026-11-27`). Planned milestones live in [`ROADMAP.md`](ROADMAP.md), operational tasks in [`docs/kanban/KANBAN.md`](docs/kanban/KANBAN.md), errata in [`ERRATA.md`](ERRATA.md), hardening index in [`HARDENING_INDEX.md`](HARDENING_INDEX.md), literature & export-control audit in [`docs/LITERATURE_AND_EXPORT_CONTROL.md`](docs/LITERATURE_AND_EXPORT_CONTROL.md), and verification history in [`docs/run-log.md`](docs/run-log.md) and [`CHANGELOG.md`](CHANGELOG.md).

## Author & Accreditation

**Alexander S. Donahue** ([@0thernes](https://github.com/0thernes), ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648), independent researcher) — author, curator, and **human-in-the-loop**. AI assistance (Claude, Codex/GPT, Gemini) is transparently disclosed in [`AUTHORS.md`](AUTHORS.md) and [`CITATION.cff`](CITATION.cff) using CRediT roles.

## AI-Reviewed Meta-Analyses & Academic Review

> **Honest Review Disclosure (`2026-11-27`):** While the review architecture ([`docs/review/AI-META-REVIEW.md`](docs/review/AI-META-REVIEW.md)) defines a four-model panel plus human peer review, **only 1 of 4 AI model passes (Claude self-review on 2026-06-14) has been executed across the original 106 meta-analyses, the 14 meta-analyses added in `v0.8.0` have all four AI panels `pending`, and 0 of 120 have received independent human mathematician peer review**. Treat `meta-analyses/` as AI-assisted working syntheses, never as peer-reviewed literature.

- 🧪 [AI Meta-Review process](docs/review/AI-META-REVIEW.md) — what AI review means (and what it does **not**)
- 🎓 [Request academic review](docs/review/ACADEMIC-REVIEW.md) — how mathematicians can audit or review entries
- 📄 [Meta-analyses](meta-analyses/) · [Review register](docs/review/REGISTER.md) · [Outreach tracker](SUBMISSIONS.md)

## License

Content under [CC BY 4.0](LICENSE) © **Alexander S. Donahue**; code under
[MIT](LICENSE-CODE); third-party notices in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md). Reuse freely **with attribution** — see [`CITATION.cff`](CITATION.cff).

<div align="center">

*"In mathematics the art of proposing a question must be held of higher value than solving it."* — **Georg Cantor**

</div>
