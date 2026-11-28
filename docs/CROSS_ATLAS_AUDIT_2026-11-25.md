# Cross-Atlas Resolution & Progress Audit (Historical Snapshot: Mega-Atlas `v2.7.0`)

> **Snapshot boundary:** The baseline tables below record the reproducible historical snapshot synchronized against Mega-Atlas `v2.7.0` at commit `541f093` (1,900 problems, 16 companion archive entries). As of **2026-11-27**, the live canonical Mega-Atlas has advanced to **`v2.10.0`** (commit `9c543fc`: **2,000** deduplicated macro problems, **290**-problem curated Left to Solve crosswalk, `109` pytest tests), `0thernes/unsolved-mathematics` has expanded to **`120`** curated problems and **`69` Lean headline theorems / `109` audited declarations** (`v0.9.0`, plus the catalytic C17/BMI2 + safe Rust Collatz accelerator), and the live [0thernes research archive bridge](https://github.com/0thernes/0thernes-research-archive/blob/main/registry/SOLVED_AND_ATLAS_BRIDGE.md) (`e60a745`) tracks **56** public entries (**27** Tier I, **17** Tier II, **12** Tier III; **28** bridge rows) — with **`0 / 2,000` grand Mega-Atlas macro problems retired** (and **2** standalone preprint sub-conjectures proved in Lean: `0TH-2026-006` Banić–Elezović Conj. 7.7 and `0TH-2026-009` Track 2 Muller–Saniga Section 6 limit question, both unreviewed).

**Scope:** Primary-evidence cross-audit of:
1. **`0thernes/unsolved-problems-mega-atlas` (`v2.7.0` @ `541f093` frozen baseline; `v2.10.0` @ `9c543fc` live 2,000-problem catalog)** (`outputs/MegaAtlas_Unsolved_Problems_V2.json`, **1,900 → 2,000** deduplicated unsolved problems across 8 macro pillars and 28 superdomains, `103` Pure Lean 4.35.0 internal-invariant theorems across 6 kernels + live negative kernel rejection, plus 20 `recently_resolved_benchmarks`).
2. **`0thernes/unsolved-mathematics` (`v0.9.0`, archive ID `0TH-BUILD-004`)** (`data/problems.yaml`, **120** ranked open mathematical problems across 38 fields, plus its standalone zero-Mathlib Lean 4.35.0 6-kernel formal core in `lean/` with `autoImplicit = false` covering **69 headline theorems + 18 non-vacuity witnesses + 22 adversarial refutations = 109 audited declarations** across **8 open-problem domains** + live negative kernel rejection).
3. **All 16 companion `0thernes-research-archive` preprints & formal builds across 76 public `0thernes` repositories** audited from primary `CLAIMS.md`, `paper/main.tex`, and Lean 4.35.0 proof files as of **2026-11-26**.

---

## 1. Executive Verdict — Did `0thernes` Solve Any of the 1,900 Mega-Atlas Problems?

> **Strict Honest Answer:** **ZERO (`0 / 1,900`)** of the overarching macro-level problems cataloged in `0thernes/unsolved-problems-mega-atlas` (`v2.7.0`) have been completely solved or retired by `0thernes` repositories — independently confirmed by `unsolved-problems-mega-atlas` `CLAIMS.md` (`C10`) and every individual lab's `CLAIMS.md`.

Primary-evidence separation across **three strict epistemic tiers**:

### Tier A — 16 Companion Entries in `0thernes-research-archive` (76 Public Repos Audited; Self-Published, Pending Peer Review)

Synchronized verbatim with `unsolved-problems-mega-atlas v2.7.0` (`paper/main.tex` Table 6):

| Archive ID | Parent Mega-Atlas ID(s) | Verification | Narrowly Scoped Result | Overarching Parent Status |
|---|---|---|---|---|
| `0TH-2026-012` | `CS-053`, `CS-026`, `CS-004`, `CS-049`+ | Lean 4.35 (`6/6`, v4.0.0) | 27 thms (29 decls): Koszul–Veronese syzygy ($4/7 \to 10/17$), LFSR domination, Chen DFT, $8/13$ Matúš, $\mathrm{rank}_F(\langle 2,2,2\rangle)=7$, Koszul $\ge m^2+2$, $\mathbb{Z}[\sqrt{5}]$ SOS | **OPEN** |
| `0TH-2026-011` | 13 Crypto/QC IDs | Lean 4.35 (`6/6`, v2.5.0) | 28 algebraic/IT/QGT invariants (63 decls) incl. $c_{\mathrm{eff}}^2+C^2=1$, Toner CHSH, T7c Microcrypt EFI & FIPS 203 $|e|\le 831$ | **OPEN** |
| `0TH-2026-010` | `CS-005` | Lean 4.35 (`7` kernels) | Base-$p$ 2-register passive catalytic dichotomy and unique optimal 3-register exponent $\log_{13}(8) \approx 0.8107$ | **OPEN** |
| `0TH-2026-009` | `QM-011`, `QC-037`, `QC-013` | Lean 4.35 (`6/6`, v2.9.0) | Disjoint Mermin formulas $(7^k-5^k)/2$, Jonah Conjecture E (9 cases, $N \ge 4$), 4-qubit $C_3$ optima (2,206 decls) | **OPEN** |
| `0TH-2026-004` | `QM-011` | Lean 4.35 (`6/6`, v1.9.0) | Exact minimum KS ray counts inside restricted coordinate pools (`31, 33, 18, 29`; 149 decls + DRUP) | **OPEN** |
| `0TH-2026-006` | `STAT-001` (rel.) | Lean 4.35 (`6/6`, v2.2.0) | Resolved Banić–Elezović Conj. 7.7 ($a_\triangle = \frac{1}{32} - \frac{4\sqrt{3}}{243}$; 723 thms + dual TSA/OTS); standalone sub-conjecture | **N/A (not a macro entry)** |
| `0TH-2026-013` | `CS-001`, `CS-005`, `CS-010`, `CS-012` | Lean 4.35 (`6/6`, v1.1.0) | 14 unconditional complexity-barrier theorems (relativization, natural proofs, Schaefer, catalytic) + 4 heuristic refutations | **OPEN** |
| `0TH-2026-014` | `CM-018`, `FLD-060`, `CM-016`, `QM-011` | Lean 4.35 (`6/6`, v1.0.0) | 98 decls (6 pillars): non-Hermitian spectral knots, higher-order EP Petermann cancellation, GBZ collapse & dipole scars | **OPEN** |
| `0TH-2026-015` | `ALG-035`, `ANL-063`, `QC-032`, `CM-016`+ | Lean 4.35 (`6/6`, v1.0.0) | 20 decls: Hantzsche–Wendt group ring no-sign-lift, Hensel identity, all-prime Type-II fracton codes & 3D $B_4$ monodromy | **OPEN** |
| `0TH-2026-016` | `CS-049` | Lean 4.35 (`6/6`, v1.0.0) | 32 decls: coset-quotient compression, separation-graph barriers & chunked 81-ball certificates for finite odd-cycle/torus capacity | **OPEN** |
| `0TH-2026-007/8` | `NEURO-001`, `NEURO-019` | Lean 4.35 (`6/6`, v1.3.0) | 24 biophysical invariants (+ 26 witnesses + 6 checks) + refuted pre-registered 40 Hz ATP sustainability ($f_{\mathrm{crit}} = 29.5625$ Hz) | **OPEN** |
| `0TH-BUILD-003` | `SUB-032`, `GR-001..003` | Lean 4.35 (`6/6`, v1.5.0) | Discrete $p$-adic AdS/CFT multi-edge Kantorovich primal-dual Gauss–Bonnet & universal graph RT SSA (149 Palomar decls) | **OPEN** |
| `0TH-BUILD-004` | `NT-005`, `NT-066`, `NT-078`, `COMB-002` | Lean 4.35 (`6/6`, **`v0.9.0`**) | **This repository:** 120 dossiers + 8-domain math foundations (69 thms + 18 witnesses + 22 refutations = 109 decls; solves 0 conjectures) | **OPEN** |
| `0TH-BUILD-002` | `CS-053`, `SYS-001` | Lean 4.35 (`6/6`, v2.4.0) | 85 decls: $\mathrm{GF}(256)$ Cauchy/RS MDS, dual-path Merkle binding, unpinned quorums, 4-qubit unitarity + 8 refutations | **OPEN** |
| `0TH-BUILD-012` | `HW-001`, `HW-002`, `QM-011` | Lean 4.35 (`6/6`, v3.0.0) | 59 Palomar decls: silicon-to-quantum discrete PDE stability, unitary bounds & finite contextuality (+ 60-digit oracles) | **OPEN** |
| `0TH-BUILD-001/6/8+` | `BIO-001`, `BIO-022`, `SUB-001`, `GR-001..2` | Lean 4.35 (266+ decls) | A-Life Omega discrete invariants (`cellulogonic-mecha`, `cellular-engine-omega`) + 8 Schwarzschild limits | **OPEN** |

### Tier B — 8 Open-Problem Domains Formalized in `unsolved-mathematics` (`lean/`, `v0.9.0`, 69 Headline Theorems + 40 Checks = 109 Declarations)

| Mega-Atlas ID | `unsolved-mathematics` Slug (Rank) | Lean 4.35.0 Module (`lean/FormalAtlas/`) | Certified Structural Results (6/6 Kernels + Live Neg Rejection) | Macro Status |
|---|---|---|---|---|
| `NT-005` | `collatz-conjecture` (#28) | `Collatz.lean` (31 thms) | Terras bijection, affine & intercept laws, Böhm–Sontacchi cycle eq., positivity localization ($\rho_w \le -1$), negative cycles (`-5`, `-17`), $3n-1$ sibling cycles at `5` and `17` (no formal barrier theorem), positive-cycle subcriticality ($3^o < 2^d$), **unconditional 1-/2-/3-odd-step positive-cycle exclusion (all $d \ge 1$), sharp affine intercept upper bound, global Eliahou–Steiner cycle amplitude ceiling, 2-adic & Odd-Unit-Lock valuation isometries, Fine–Wilf spine valuation ceiling, exhaustive $d \le 7$ exclusion & catalytic reversible cylinder** | **OPEN** |
| `NT-078` | `erdos-straus-conjecture` (#97) | `ErdosStraus.lean` (5 thms) | Mordell mod-840 covering (834/840 = `99.29%`), multiplicative closure, symmetry, all $2 \le n \le 30$, and all 6 smallest exceptional squares `{121, 169, 289, 361, 529, 841}` | **OPEN** |
| `COMB-046` | `lonely-runner-conjecture` (#88) | `LonelyRunner.lean` (8 thms) | All-$n$ rational sharpness $\delta \le 1/(n+1)$, base cases $n \in \{1,2\}$, scaling/shift/negation symmetries, the $t=1/4$ family (27 of 64 speed-triple classes mod 4), and constructive $n=3$ (4 runners, a classical case: Betke–Wills 1972, Cusick 1973) for all positive integer speed triples; proved for up to 13 runners in recent preprints (`arXiv:2509.14111`, `arXiv:2511.22427`, `arXiv:2604.23906`) | **OPEN** |
| `NT-066` | `brocard-problem` (#79) | `Brocard.lean` (7 thms) | Brown pairs `{4,5,7}`, mod-3 / mod-4 / mod-10 invariants, and exhaustive classification through $n \le 20$ ($20!+1 = 2.43 \times 10^{18}$) | **OPEN** |
| `NT-004` | `twin-prime-conjecture` (#6) | `Primes.lean` (4 thms) | Euclid's infinitude of primes, arbitrary prime gaps via $(k+1)!+2$, oddness of primes $\ge 3$, and twin-prime mod-6 structure ($6 \mid p+1$ for $p \ge 4$) | **OPEN** |
| `NT-003` | `goldbach-conjecture` (#2) | `Goldbach.lean` (3 thms) | Finite strong Goldbach for every even $4 \le n \le 100$, odd binary obstruction ($p=2 \lor q=2$), and concrete failure at `11` | **OPEN** |
| `NT-076` / `NT-077` | `odd-perfect-numbers` (#8), `mersenne-primes-infinitude` (#9) | `PerfectNumbers.lean` (7 thms) | Algebraic Mersenne exponent necessity, `{6, 28, 496, 8128}`, odd-perfect exclusion $n \le 100$, **Complete Euclid–Euler biconditional theorem (all even $n$)**, and **Euler's 1750 Mersenne prime divisor congruence ($2p \mid q - 1$)** | **OPEN** |
| `COMB-002` | `ramsey-numbers` | `Ramsey.lean` (4 thms) | Exact Ramsey numbers **$R(3,3) = 6$** ($K_6$ pigeonhole + $C_5$ on $K_5$) and **$R(3,4) = 9$** (Handshaking Lemma on $K_9$ + circulant $C_8(1,4,7)$ on $K_8$) | **OPEN** |

### Tier C — Overlap & External Frontier Reconciliation

1. **Catalog overlap:** **99 / 106** problems in `unsolved-mathematics` map directly to entries in `unsolved-problems-mega-atlas` (`v2.7.0`), plus **2** (`moving-sofa-problem` `SOLV-05`, `connes-embedding-aftermath` `SOLV-11`) in its 20 `recently_resolved_benchmarks`; only 5 specialized problems have no standalone Mega-Atlas ID.
2. **Erdős Unit Distance (`GEOM-069` vs `unit-distance-problem`):** `unsolved-mathematics` integrates the live-verified May 2026 disproof preprint `arXiv:2605.20695` (Alon–Bloom–Gowers–Litt–Sawin–Shankar–Tsimerman–Wang–Wood) with explicit pending-peer-review caveats.
3. **12 Fall/Nov 2026 AI Proof Claims:** Both atlases strictly agree (`mega-atlas` `C6` and `unsolved-mathematics` `C-08`) that all 12 Fall/Nov 2026 AI proof claims (`NT-001` RH, `NT-002` GRH, `ANL-001` 3D Navier–Stokes, `QM-002` Yang–Mills, etc.) remain **unretired / `open`** pending human-readable exposition and community consensus.
