# Benchmarks & Performance Budgets (`docs/benchmarks.md`)

> **Build Standard `v1.2.0` Items `A37`, `B26`, `B27`.** Every timing, speedup, memory bound, and hardware instruction claim below comes strictly from real measured runs on reproducible commands with independent bit-for-bit cross-oracle verification (zero synthetic benchmarks, zero approximations, zero loss of exactness).
>
> **Epistemic boundary:** Computational speedups expand finite Collatz measurement horizons ($t \le 26$, $d \le 34$) and eliminate laptop CPU/RAM bottlenecks; they do **not** prove the Collatz Conjecture.

---

## 1. Hardware, OS, and Toolchain Environment

| Parameter | Exact Measured Value |
|---|---|
| CPU | Intel Core Ultra 9 275HX (24 logical processors, x86-64 with BMI2) |
| RAM | 47.4 GiB physical RAM |
| OS | Windows 11 (x86-64) |
| C17 Compiler | GCC 16.1.0 (MinGW-W64 POSIX UCRT), flags `-O3 -std=c17 -mbmi2 -Wall -Wextra -Werror` |
| Rust Compiler | `rustc 1.94.1`, flags `-O` (100% safe Rust, `#![forbid(unsafe_code)]`-clean, zero `unsafe` blocks) |
| Sanitizer & Fuzz Compiler | Zig `0.17.0` (`zig cc -O1 -g -std=c17 -fsanitize=undefined -fno-sanitize-recover=all -Wall -Wextra -Werror`; Linux CI adds `-fsanitize=address,undefined`) |
| Python Interpreter | CPython `3.12.10` (`.venv`, pinned `requirements-lock.txt`) |
| Hardware BMI2 Verification (`objdump -d`) | Verified native emission in `collatz_catalytic`: `tzcnt` (2), `bswap` (4), `shlx` (16), `shrx` (6), `mulx` (2), `bsr` (3) — zero hand-written assembly needed |

---

## 2. Performance & Resource Budgets (`A37`)

To prevent heavy experiments from freezing or starving a laptop, native Collatz instruments in [`problems/collatz-conjecture/native/`](../problems/collatz-conjecture/native/README.md) enforce explicit single-thread, constant/flat-memory budgets:

| Workload | Execution Mode | Wall-Time Budget | Peak Memory / Stack Budget | CPU Footprint |
|---|---|---:|---:|---|
| Odd-Unit-Lock Target-Tail (`s<=12, t<=20`, 27.6M pairs) | Single-threaded C17 / Rust | `< 0.10 s` | `< 1 MiB` flat target buffer | 1 core (no thread-pool fanout) |
| Odd-Unit-Lock Target-Tail (`s<=12, t<=26`, 884.4M pairs) | Single-threaded C17 / Rust | `< 0.50 s` | `< 16 MiB` flat target buffer | 1 core |
| Catalytic DFS Residue Miner (`d = 24`) | Single-threaded C17 / Rust | `< 0.10 s` | **`4,096 B`** fixed DFS stack (zero heap) | 1 core |
| Catalytic DFS Residue Miner (`d = 34`, 174.4M leaves) | Single-threaded C17 / Rust | `< 5.00 s` | **`4,096 B`** fixed DFS stack (zero heap) | 1 core |
| Python `odd_unit_lock_target_tail_lab.py` (fixed `V90-BUG-01`) | Single-threaded Python | Reference oracle | $O(1)$ valuation-summary space (removed `e_values` list) | 1 core |

---

## 3. Measured 3-Run Wall-Clock Benchmarks (`B26`)

Every native and Python timing below is the **median / min / max** of 3 consecutive end-to-end wall-clock runs (including OS process spawn and JSON serialization). Python `s10_t20`, `s12_t20`, and `s10_t22` baselines are the exact committed `runtime_seconds` from the `2026-07-05` exact `Fraction` result files in `problems/collatz-conjecture/experiments/results/`.

### 3.1 Odd-Unit-Lock Target-Tail (`collatz_catalytic.c` vs Safe Rust vs Python `Fraction`)

| Experiment Window | Exact Spine Pairs | Python Baseline (`Fraction`) | C17 `-O3 -mbmi2` (3-run median [min, max]) | Safe Rust `-O` (single cutoff, 3-run median [min, max]) | Measured Wall Speedup (C17 vs Python) | Bit-Exact Parity |
|---|---:|---:|---:|---:|---:|---|
| `s<=10, t<=20` (5 cutoffs) | `6,214,555` | `35.678 s` | **`0.021196 s`** `[0.020455, 0.025650]` | `0.013015 s` `[0.012072, 0.014296]` | **1,683×** | C17 = Rust = Python JSON (`100%`) |
| `s<=12, t<=20` (3 cutoffs) | `27,611,340` | `123.134 s` | **`0.017253 s`** `[0.017250, 0.018840]` | `0.012748 s` `[0.012667, 0.015242]` | **7,137×** | C17 = Rust = Python JSON (`100%`) |
| `s<=10, t<=22` (3 cutoffs) | `20,385,387` | `114.270 s` | **`0.025172 s`** `[0.024606, 0.026209]` | `0.015701 s` `[0.014410, 0.016876]` | **4,540×** | C17 = Rust = Python JSON (`100%`) |
| `s<=10, t<=26` (new frontier) | `199,055,909` | N/A (est. `> 18 min`) | **`0.125655 s`** `[0.121616, 0.145092]` | `0.033906 s` `[0.032034, 0.041173]` | — | C17 = Rust (`100%`) |
| `s<=12, t<=26` (new frontier) | `884,406,475` | N/A (est. `> 65 min`) | **`0.133099 s`** `[0.126353, 0.134084]` | `0.039666 s` `[0.037279, 0.040205]` | — | C17 = Rust (`100%`, all `884.4M` pairs) |

*Why the 1,683×–7,137× speedup is mathematically exact:* By our Lean-verified Odd-Unit-Lock Valuation Isometry (`thm_collatz_odd_unit_lock_valuation_isometry`), $v_2(\rho_w - \rho_v) = \operatorname{lcp}(w^\infty, v^\infty)$. Sorting bit-reversed infinite periodic extensions of all unique target spines in place replaces $O(|S| \cdot |T|)$ arbitrary-precision rational subtractions with $O(|S| \cdot \log |T|)$ exact binary-search prefix slices (zero precision loss, verified bit-for-bit against exact `fractions.Fraction` on `s<=10, t<=22`, `s<=12, t<=20`, `s<=10, t<=14`, and 15,876-pair 128-bit exact spine arithmetic in `self-test`). Note: the C17 engine writes full multi-cutoff JSON including top-witness extraction and echo counts; the Rust oracle computes the single top cutoff directly to stdout.

### 3.2 Catalytic Fixed-Stack DFS Residue Miner (`collatz_residue_lab.py` vs C17 vs Safe Rust)

| Depth `d` | Certified Leaves | Frontier Leaves | Frontier Density | Python BFS (`collatz_residue_lab.py`) | C17 Catalytic DFS (`4,096 B` stack) | Safe Rust Catalytic DFS (`4,096 B` stack) | Wall Speedup | Bit-Exact Parity |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `20` | `4,404` | `27,328` | `0.0260620117` | `0.190875 s` `[0.187, 0.215]` | **`0.014195 s`** `[0.013, 0.016]` (internal `0.0003 s`) | `0.015969 s` `[0.011, 0.017]` | **13.4×** (wall) | C17 = Rust = Python (`100%`) |
| `24` | `81,119` | `286,581` | `0.0170815587` | `1.343228 s` `[1.282, 1.401]` | **`0.016061 s`** `[0.016, 0.017]` (internal `0.0028 s`) | `0.014090 s` `[0.013, 0.016]` | **83.6×** (C17) / **95.3×** (Rust) | C17 = Rust = Python (`100%`) |
| `30` | `1,166,059` | `12,771,274` | `0.0118941758` | OOM/slow BFS frontier | **`0.119756 s`** `[0.118, 0.121]` | `0.081800 s` `[0.076, 0.088]` | — | C17 = Rust (`100%`) |
| `34` | `22,475,498` | `151,917,636` | `0.0088427702` | OOM/slow BFS frontier | **`1.646759 s`** `[1.479, 1.684]` | `1.681337 s` `[1.350, 1.731]` | — | C17 = Rust (`100%`, `max_q = 1`) |

*Space breakthrough:* Python's BFS materializes all `151.9M` frontier leaves simultaneously in heap memory (multi-gigabyte RSS); catalytic fixed-stack DFS reuses a **4,096-byte** stack frame (`64` depth frames $\times 64$ bytes, zero `malloc`) in strict $O(d)$ space while checking every single residue class exactly.

---

## 4. Sanitizer, Fuzzing & Regression Tracking (`B15`, `B16`, `B27`)

Every commit to `main` runs the native verification pipeline in `.github/workflows/ci.yml` (`native-catalytic-audit` job) and locally via:

```bash
# 1. Production C17 + BMI2 build & 15,876-pair exact 128-bit self-test
gcc -O3 -std=c17 -mbmi2 -Wall -Wextra -Werror \
  problems/collatz-conjecture/native/collatz_catalytic.c -o collatz_catalytic
./collatz_catalytic self-test

# 2. ASan + UBSan sanitized build (Linux GCC/Clang; Windows Zig CC UBSan)
gcc -O1 -g -std=c17 -fsanitize=address,undefined -fno-sanitize-recover=all -Wall -Wextra -Werror \
  problems/collatz-conjecture/native/collatz_catalytic.c -o collatz_catalytic_san
./collatz_catalytic_san self-test

# 3. 250,000-case deterministic SplitMix64 differential fuzzer under ASan + UBSan
gcc -O2 -g -std=c17 -DSTANDALONE_FUZZ_MAIN -fsanitize=address,undefined -fno-sanitize-recover=all \
  -Wall -Wextra -Werror problems/collatz-conjecture/native/fuzz_collatz_catalytic.c -o fuzz_collatz
./fuzz_collatz

# 4. Independent safe Rust cross-oracle (zero unsafe)
rustc -O problems/collatz-conjecture/native/collatz_catalytic_oracle.rs -o collatz_catalytic_oracle
```

- **Performance regression gate (`B27`):** `tests/test_collatz_instruments.py` verifies exact differential parity between C17, Safe Rust, and Python on deterministic workloads and checks that `s10_t20` completes well under its `2.0 s` CI wall-time ceiling when native toolchains are installed.
- **Sanitizer & fuzz status (`v0.9.0`):** `0` compiler warnings (`-Wall -Wextra -Werror`), `0` UBSan traps across `15,876`-pair `self-test` and `250,000`-case deterministic fuzzer (`zig cc -fsanitize=undefined -fno-sanitize-recover=all`), and `100%` bit-for-bit parity across C17, Safe Rust, and Python `Fraction`.
