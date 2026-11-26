# Cross-Atlas Resolution & Progress Audit (2026-11-25, Synchronized to Mega-Atlas `v2.4.0`)

**Scope:** Primary-evidence cross-audit of:
1. **`0thernes/unsolved-problems-mega-atlas` (`v2.4.0`)** (`outputs/MegaAtlas_Unsolved_Problems_V2.json`, **1,900** deduplicated unsolved problems across 8 macro pillars and 28 superdomains, `5,808` biconnected graph edges, `92` Pure Lean 4.35.0 internal-invariant theorems across 6 kernels, plus 20 `recently_resolved_benchmarks`).
2. **`0thernes/unsolved-mathematics` (`v0.5.0`)** (`data/problems.yaml`, **106** ranked open mathematical problems across 38 fields, plus its standalone zero-Mathlib Lean 4.35.0 6-kernel formal core in `lean/` covering **45 headline theorems + 10 non-vacuity witnesses + 14 adversarial refutations = 69 audited declarations** across **8 open-problem domains**).
3. **All companion `0thernes` research repositories & `0thernes-research-archive` preprints** audited from primary `CLAIMS.md`, `paper/main.tex`, and Lean 4.35.0 proof files as of **2026-11-25**.

---

## 1. Executive Verdict — Did `0thernes` Solve Any of the 1,900 Mega-Atlas Problems?

> **Strict Honest Answer:** **ZERO (`0 / 1,900`)** of the overarching macro-level problems cataloged in `0thernes/unsolved-problems-mega-atlas` (`v2.4.0`) have been completely solved or retired by `0thernes` repositories — independently confirmed by `unsolved-problems-mega-atlas` `CLAIMS.md` (`C10`) and every individual lab's `CLAIMS.md`.

Primary-evidence separation across **three strict epistemic tiers**:

### Tier A — 7 Companion Independent Preprints in `0thernes-research-archive` (Narrowly Scoped Results; Self-Published, Pending Peer Review)

Synchronized verbatim with `unsolved-problems-mega-atlas v2.4.0` (`paper/main.tex` Table 6):

| Archive ID | Repository | Parent Mega-Atlas ID(s) | Verification | Narrowly Scoped Result | Overarching Parent Status |
|---|---|---|---|---|---|
| `0TH-2026-012` | `coded-pir-mlwe-complexity-lab` | `CS-053`, `CS-026`, `CS-001`, `CS-051` | Lean 4.35.0 (`6/6` kernels) | Koszul–Veronese syzygy rank ($4/7 \to 10/17$), LFSR domination, Chen Step 9 DFT cancellation, Luo refutation, $8/13$ polymatroid barrier, $\mathbb{F}_{11}$ Byzantine witness | **OPEN** |
| `0TH-2026-011` | `secmesh-pqsi` | 13 Crypto / QC IDs (`CS-026`, etc.) | Lean 4.35.0 (`6/6` kernels) | 27 algebraic/IT/QGT invariants including $c_{\mathrm{eff}}^2 + C^2 = 1$ and sharp FIPS 203 $|e| \le 831$ | **OPEN** |
| `0TH-2026-010` | `catalytic-register-frontiers` | `CS-005` (rel.) | Lean 4.35.0 (`7` kernels; Zenodo `10.5281/zenodo.24517198`) | Resolved Vinciguerra (`arXiv:2609.18692`) base-$p$ 2-register passive catalytic dichotomy and unique optimal 3-register powering exponent $\log_{13}(8) \approx 0.810714$ | **OPEN** |
| `0TH-2026-009` | `pauli-contextuality-lab` | `QM-011` | Lean 4.35.0 / Mathlib (`6/6`) | Resolved Jonah's Conjecture E (9 vertex cases, $N \ge 4$, citing single-orbit transitivity as preprint input), disjoint Mermin degrees $(7^k-5^k)/2$, 4-qubit $C_3$ optima (`368` vs `344`) | **OPEN** |
| `0TH-2026-004` | `kochen-specker-extremal-lab` | `QM-011` | Lean 4.35.0 (`6/6`) + DRUP | Exact minimum KS ray counts inside restricted pools (`31, 33, 18, 29`) | **OPEN** |
| `0TH-2026-006` | `multinomial-tv-conjecture` | `STAT-001` (rel.; standalone) | Lean 4.35.0 / Mathlib | Resolved Banić–Elezović Conjecture 7.7 (`arXiv:2610.17046v1` / `arXiv:2611.14735v1`): $a_\triangle = \frac{1}{32} - \frac{4\sqrt{3}}{243}$ | **N/A (not a macro entry)** |
| `0TH-2026-007/8` | `human-synapse-bouton-lab` | `NEURO-001`, `NEURO-019`, `NEURO-027` | Lean 4.35.0 (`6/6`) | 18 biophysical invariants + refuted pre-registered 40 Hz ATP sustainability ($f_{\mathrm{crit}} = 29.5625$ Hz) | **OPEN** |

*(Additional formal companion: `ultrametrica` — 101 Lean proofs including curved discrete Gauss–Bonnet on ultrametric trees related to `SUB-032`, parent **OPEN**.)*

### Tier B — 8 Open-Problem Domains Formalized in `unsolved-mathematics` (`lean/`, `v0.5.0`, 45 Headline Theorems + 24 Checks = 69 Declarations)

| Mega-Atlas ID | `unsolved-mathematics` Slug (Rank) | Lean 4.35.0 Module (`lean/FormalAtlas/`) | Certified Structural Results (6/6 Kernels) | Macro Status |
|---|---|---|---|---|
| `NT-005` | `collatz-conjecture` (#21) | `Collatz.lean` (14 thms) | Terras bijection, affine & intercept laws, Böhm–Sontacchi cycle eq., parity-word cocycle, zero fixed point, non-negativity, positivity localization ($\rho_w \le -1$), negative cycles (`-5`, `-17`), $3n-1$ $\varepsilon$-invariance barrier | **OPEN** |
| `NT-078` | `erdos-straus-conjecture` (#97) | `ErdosStraus.lean` (5 thms) | Mordell mod-840 covering (834/840 = `99.29%`), multiplicative closure, symmetry, all $2 \le n \le 30$, and all 6 smallest exceptional squares `{121, 169, 289, 361, 529, 841}` | **OPEN** |
| `COMB-046` | `lonely-runner-conjecture` (#88) | `LonelyRunner.lean` (7 thms) | All-$n$ rational sharpness $\delta \le 1/(n+1)$, base cases $n \in \{1,2\}$, scaling invariance, period shift, time reversal, and $n=3$ across all non-div-4 triples (7/8 parity classes) | **OPEN** |
| `NT-066` | `brocard-problem` (#79) | `Brocard.lean` (7 thms) | Brown pairs `{4,5,7}`, mod-3 / mod-4 / mod-10 invariants, and exhaustive classification through $n \le 20$ ($20!+1 = 2.43 \times 10^{18}$) | **OPEN** |
| `NT-004` | `twin-prime-conjecture` (#6) | `Primes.lean` (4 thms) | Euclid's infinitude of primes, arbitrary prime gaps via $(k+1)!+2$, oddness of primes $\ge 3$, and twin-prime mod-6 structure ($6 \mid p+1$ for $p \ge 4$) | **OPEN** |
| `NT-003` | `goldbach-conjecture` (#2) | `Goldbach.lean` (3 thms) | Finite strong Goldbach for every even $4 \le n \le 100$, odd binary obstruction ($p=2 \lor q=2$), and concrete failure at `11` | **OPEN** |
| `NT-076` / `NT-077` | `odd-perfect-numbers` (#8), `mersenne-primes-infinitude` (#9) | `PerfectNumbers.lean` (3 thms) | Algebraic proof of Mersenne exponent necessity ($2^n-1$ prime $\Rightarrow n$ prime), first 4 even perfect numbers `{6, 28, 496, 8128}`, and finite odd-perfect exclusion for $n \le 100$ | **OPEN** |
| `COMB-002` | `ramsey-numbers` | `Ramsey.lean` (2 thms) | Exact Ramsey number $R(3,3) = 6$ from first principles (upper bound on $K_6$ + explicit symmetric $C_5$ lower bound on $K_5$) | **OPEN** |

### Tier C — Overlap & External Frontier Reconciliation

1. **Catalog overlap:** **99 / 106** problems in `unsolved-mathematics` map directly to entries in `unsolved-problems-mega-atlas` (`v2.4.0`), plus **2** (`moving-sofa-problem` `SOLV-05`, `connes-embedding-aftermath` `SOLV-11`) in its 20 `recently_resolved_benchmarks`; only 5 specialized problems have no standalone Mega-Atlas ID.
2. **Erdős Unit Distance (`GEOM-069` vs `unit-distance-problem`):** `unsolved-mathematics` integrates the live-verified May 2026 disproof preprint `arXiv:2605.20695` (Alon–Bloom–Gowers–Litt–Sawin–Shankar–Tsimerman–Wang–Wood) with explicit pending-peer-review caveats.
3. **12 Fall/Nov 2026 AI Proof Claims:** Both atlases strictly agree (`mega-atlas` `C6` and `unsolved-mathematics` `C-08`) that all 12 Fall/Nov 2026 AI proof claims (`NT-001` RH, `NT-002` GRH, `ANL-001` 3D Navier–Stokes, `QM-002` Yang–Mills, etc.) remain **unretired / `open`** pending human-readable exposition and community consensus.
