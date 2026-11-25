# Cross-Atlas Resolution & Progress Audit (2026-11-25)

**Scope:** Primary-evidence cross-audit of:
1. **`0thernes/unsolved-problems-mega-atlas`** (`outputs/MegaAtlas_Unsolved_Problems_V2.json`, **1,900** unsolved problems across 8 macro pillars and 28 superdomains, plus 20 `recently_resolved_benchmarks`).
2. **`0thernes/unsolved-mathematics`** (`data/problems.yaml`, **106** ranked open mathematical problems across 38 fields, plus its Lean 4.35.0 6-kernel formal core in `lean/`).
3. **All 11 `0thernes` research repositories** audited from their primary `CLAIMS.md`, `README.md`, and Lean 4.35.0 proof files as of **2026-11-25**.

---

## 1. Executive Verdict — Did `0thernes` Solve Any of the 1,900 Mega-Atlas Problems?

> **Strict Honest Answer:** **ZERO (0 / 1,900)** of the flagship macro-level problems cataloged in `0thernes/unsolved-problems-mega-atlas` have been completely solved or closed by `0thernes` repositories. Every matched macro problem (`CS-001`, `CS-026`, `CS-051`, `CS-053`, `QM-011`, `SUB-032`, `NEURO-027`, `NT-005`, `NT-066`, `NT-078`, `COMB-046`) remains **OPEN** at the general level — exactly as each lab's own `CLAIMS.md` ledger transparently states.

However, the primary-evidence audit separates **three distinct epistemic tiers** of genuine `0thernes` contributions:

### Tier A — 3 Specific Published 2026 Sub-Conjectures Completely Proved (Lean 4.35.0 Verified Preprints, Pending Peer Review)

None of these three specific sub-conjectures is broken out as its own standalone macro entry among the 1,900 Mega-Atlas IDs (one sits strictly inside the `QM-011` sub-frontier; the other two sit in discrete probability and catalytic computing frontiers not separately indexed in Mega-Atlas V2):

| # | Repository | Specific Sub-Conjecture Resolved | Verification Status | Relation to Mega-Atlas (1,900) |
|---|---|---|---|---|
| 1 | `0thernes/multinomial-tv-conjecture` | **Conjecture 7.7 of Banić & Elezović** (`arXiv:2610.17046v1` / `arXiv:2611.14735v1`): exact multinomial discrete total-variation adjacent constant $a_\triangle = \frac{1}{32} - \frac{4\sqrt{3}}{243}$ | Machine-checked in Lean 4.35.0 (author preprint; not yet peer-reviewed) | Not listed among the 1,900 Mega-Atlas macro entries (`0` hits for `multinomial`) |
| 2 | `0thernes/pauli-contextuality-lab` | **Jonah's Conjecture E** (all 9 vertex cases for $N \ge 4$), exact Case C3 optima (`368` vs `344`), and disjoint Mermin degrees $(7^k - 5^k)/2$ | Machine-checked in Lean 4.35.0 (note: single-orbit transitivity [J3 Thm B4] is a cited paper input; Jonah's preprints are unrefereed Zenodo preprints) | Strict sub-frontier of **`QM-011`** (*Quantum Contextuality, Ontological Models & Psi-Ontic vs. Psi-Epistemic*); does NOT close macro `QM-011` |
| 3 | `0thernes/catalytic-register-frontiers` | **Vinciguerra (`arXiv:2609.18692`)** 2-register positive-characteristic dichotomy (`T1`) and optimal 3-register powering exponent $\log_{13}(8) \approx 0.810714$ (`T3d`/`T3f`/`T3h`/`T3i`) | Machine-checked in Lean 4.35.0 (Zenodo DOI `10.5281/zenodo.24517198`; not yet peer-reviewed) | Pure-CS catalytic-register frontier not listed in Mega-Atlas (all chemistry hits for `catalytic` are chemical catalysis; `CS-005` is macro P vs PSPACE) |

### Tier B — 11 Mega-Atlas Macro IDs With Certified Lean 4.35.0 Partial Progress, Exact Finite Minima, Refutations, or Formal Barriers

| Mega-Atlas ID | Mega-Atlas Problem | Mega-Atlas `status_2026` | `0thernes` Repository | Certified Partial Progress / Barrier / Refutation | Macro Problem Status |
|---|---|---|---|---|---|
| **`CS-053`** | Exact Capacity Region of Colluding, Coded & Byzantine PIR | Partially Solved / Special Cases | `coded-pir-mlwe-complexity-lab` | `T1a`–`T1f`: Koszul–Veronese domination, $\mathbb{F}_{11}$ Byzantine $2/5$, scale-128 polymatroid barrier $8/13 > 3/5$, $\mathbb{P}^3$ impossibility | **OPEN** |
| **`CS-026`** | Exact Quantum & Classical Hardness of Post-Quantum Lattice Problems | Active Breakthroughs / Frontier | `coded-pir-mlwe-complexity-lab`, `secmesh-pqsi` | `T2a`–`T2d`: Refutation of Luo `arXiv:2604.15858`, Chen Step 9 DFT cancellation, FIPS 203 $\mathrm{CBD}_2/\mathrm{CBD}_3$ $4.96\times$ Rényi-2 cliff, QGTL Berry curvature; 27 Lean theorems in `secmesh-pqsi` | **OPEN** |
| **`CS-001`** | P versus NP Problem | Completely Open | `coded-pir-mlwe-complexity-lab`, `p-vs-np-frontier-lab` | `T3a`–`T3d`, `C1`–`C14` structural barrier & circuit-complexity formalizations | **OPEN** |
| **`CS-051`** | Optimal Length of Constant-Query (3-Query) Locally Decodable Codes | Active Breakthroughs / Frontier | `coded-pir-mlwe-complexity-lab`, `p-vs-np-frontier-lab` | Related complexity/coding barrier checks | **OPEN** |
| **`QM-011`** | Quantum Contextuality, Ontological Models & Psi-Ontic vs. Psi-Epistemic | Partially Solved / Special Cases | `kochen-specker-extremal-lab`, `pauli-contextuality-lab` | Certified pool minima `31` in $B(3,2)$ and `18` in $B(4,1)$ + Jonah Conjecture E sub-frontier | **OPEN** |
| **`SUB-032`** | Non-Archimedean / $p$-adic AdS/CFT Holography Continuum Limit | Active Breakthroughs / Frontier | `ultrametrica` | 101 Lean proofs including curved discrete Gauss–Bonnet identities on ultrametric trees | **OPEN** |
| **`NEURO-027`** | Working Memory Maintenance: Persistent Spiking vs. Activity-Silent | Active Breakthroughs / Frontier | `human-synapse-bouton-lab` | Lean 4.35.0 biophysical synaptic-bouton modeling workbench | **OPEN** |
| **`NT-005`** | Collatz Conjecture ($3n+1$) | Independent / Undecidable Suspected | `unsolved-mathematics` (`lean/`) | 6-kernel Lean 4.35.0 structural core: Terras bijection, affine orbit law, cycle numerator identity, no finite 2-adic cover, positivity localization, parity-word composition, negative cycles (`-5`, `-17`), $3n-1$ $\varepsilon$-invariance barrier | **OPEN** |
| **`NT-078`** | Erdős–Straus Conjecture ($4/n$ Egyptian Fractions) | Partially Solved / Special Cases | `unsolved-mathematics` (`lean/`) | 6-kernel Lean 4.35.0 Mordell mod-840 reduction covering 834/840 classes (99.29%), multiplicative closure, and certified witnesses for the 6 smallest exceptional squares $\{121, 169, 289, 361, 529, 841\}$ | **OPEN** |
| **`COMB-046`** | Lonely Runner Conjecture (Wills–Cusick) | Active Breakthroughs / Frontier | `unsolved-mathematics` (`lean/`) | 6-kernel Lean 4.35.0 all-$n$ rational sharpness of $\frac{1}{n+1}$, speed-scaling invariance, and base cases $n \in \{1, 2\}$ | **OPEN** |
| **`NT-066`** | Brocard's Problem ($n! + 1 = m^2$) | Completely Open | `unsolved-mathematics` (`lean/`) | 6-kernel Lean 4.35.0 exhaustive classification for $n \le 15$ (`{4, 5, 7}` only) + modular constraint $n \ge 4 \Rightarrow n! + 1 \equiv 1 \pmod 4$ | **OPEN** |

### Tier C — External Mathematical Literature Discrepancies Identified Between the Two Atlases

Comparing the 106 problems in `unsolved-mathematics` against the 1,900 entries in `unsolved-problems-mega-atlas` (`V2`, 2026-11-21 snapshot):

1. **Corpus overlap:** **96 / 106** problems in `unsolved-mathematics` match directly (score ≥ 15) to entries in `unsolved-problems-mega-atlas`, plus **3** more (`erdos-straus-conjecture` → `NT-078`, `caccetta-haggkvist-conjecture` → `COMB-017`, `erdos-hajnal-conjecture` → `COMB-003`) matched by title/diacritic normalization (**99 / 106** direct catalog overlap), plus **`moving-sofa-problem`** (`SOLV-05`) and **`connes-embedding-aftermath`** (`SOLV-11`) appearing in `recently_resolved_benchmarks`. Only **5** specialized entries in `unsolved-mathematics` (`hilbert-sixteenth-problem`, `mandelbrot-locally-connected`, `one-third-two-thirds-conjecture`, `kothe-conjecture`, `telescope-conjecture`) have no direct standalone match in Mega-Atlas V2.
2. **Erdős Unit Distance (`GEOM-069` vs `unit-distance-problem`):** Mega-Atlas V2 (`2026-11-21`) still lists `GEOM-069` as `Partially Solved / Special Cases` citing the 1984 $O(n^{4/3})$ bound, whereas `unsolved-mathematics` (`v0.3.0+`) integrates the live-verified May 2026 disproof preprint `arXiv:2605.20695` (with explicit pending-peer-review caveat).
3. **12 Fall/Nov 2026 AI Proof Claims in Mega-Atlas (`status_2026: "AI Proof Claim (Fall/Nov 2026) — Under Verification"`):** Mega-Atlas tracks 12 unrefereed Fall/Nov 2026 AI-assisted proof claims (`NT-001` RH, `NT-002` GRH, `NT-023` Chowla, `NT-060` Artin, `ALG-010` Alperin, `ALG-011` Donovan, `ALG-045` Auslander–Reiten, `ALG-048` Lech, `ANL-001` 3D Navier–Stokes, `CS-017` APSP, `CS-018` ETH/SETH/3SUM, `QM-002` Yang–Mills). Consistent with `unsolved-mathematics`'s strict epistemic policy (`CLAIMS.md`, `LIMITATIONS.md`), **none of these 12 problems is promoted to `recently-resolved` until independent community verification and peer-reviewed consensus occur.**

---

## 2. Reproducibility

This cross-audit was produced directly from:
- `https://raw.githubusercontent.com/0thernes/unsolved-problems-mega-atlas/main/outputs/MegaAtlas_Unsolved_Problems_V2.json` (`1,900` problem records, `20` resolved benchmarks)
- `data/problems.yaml` (`106` problem records)
- Local verified `CLAIMS.md` and Lean 4.35.0 proof manifests across all 11 sibling `0thernes` repositories as of `2026-11-25`.
