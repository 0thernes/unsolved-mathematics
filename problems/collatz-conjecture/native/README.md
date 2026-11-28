# Catalytic Native Collatz Accelerator (`native/`)

> **Epistemic Scope:** Exact finite computational acceleration and verification instruments for the Collatz research frontier (`problems/collatz-conjecture/`). **Proves zero part of the Collatz Conjecture** (status: `open`). Every mathematical reduction used here is machine-checked in [`lean/FormalAtlas/Collatz.lean`](../../../lean/FormalAtlas/Collatz.lean) (`thm_collatz_odd_unit_lock_valuation_isometry`, `thm_collatz_fine_wilf_spine_ceiling`, `thm_collatz_cylinder_affine_law`, `thm_collatz_catalytic_reversible_cylinder`) and differentially cross-verified bit-for-bit against exact Python `Fraction` and safe Rust oracles.

## Why This Exists (Solving the Laptop Speed & RAM Bottleneck)

The pure-Python experimental labs (`odd_unit_lock_target_tail_lab.py` and `collatz_residue_lab.py`) incurred severe single-core CPU and RAM overhead:
1. `odd_unit_lock_target_tail_lab.py` evaluated exact multi-precision `Fraction` subtractions `v2(rho_t - eta)` over all $|P| \times |T|$ pairs (and stored every `e` in a giant `e_values` list), requiring `~38.7 s` at tiny `s <= 10, t <= 18` and hours / gigabytes of RAM at `t >= 24`.
2. `collatz_residue_lab.py` stored the entire open frontier in a BFS `deque`, consuming hundreds of megabytes of RAM at depth 28 while recomputing `affine_for_low_bits` from scratch at every node.

By combining our **Lean-proved Terras 2-adic valuation isometry** ($v_2(\rho_w - \rho_v) = \operatorname{lcp}(w^\infty, v^\infty)$), our **Lean-proved Fine–Wilf spine ceiling** ($v_2 \le |w| + |v| - \gcd(|w|, |v|) - 1 \le 63$ for depths $\le 32$), **FKM supercritical Lyndon-word generation**, **catalytic in-place bit-reversed prefix slicing** ($O(|T|\log|T| + |P|\cdot 64\log|T|)$), and **catalytic fixed-stack DFS** (`4,096 B` fixed stack, $O(1)$ incremental cylinder lift), `collatz_catalytic.c` achieves **1,683×–7,137× measured 3-run median wall-clock speedups** (`123.134 s → 0.0173 s` on `s<=12, t<=20`) with constant/flat memory (`< 16 MiB` for `884.4M` pairs; `4,096 B` stack through $d=34$) and **zero accuracy or dynamic degradation**.

## Files

| File | Language | Role (Build Standard v1.2.0) |
|---|---|---|
| `collatz_catalytic.c` | C17 + BMI2 intrinsics | Primary exact Odd-Unit-Lock target-tail + catalytic DFS residue-certificate accelerator (`A37`, `B26`) |
| `collatz_catalytic_oracle.rs` | Safe Rust (zero `unsafe`) | Independent second-language cross-verifier (`B11`, `B12`, `B16`) |
| `fuzz_collatz_catalytic.c` | C17 (`libFuzzer` + standalone corpus) | 250,000-case deterministic & libFuzzer invariant fuzzer (`B15`, `B16`) |

## Build, Sanitize, Fuzz & Verify

```bash
# Release build (GCC / Clang, x86-64 BMI2)
gcc -O3 -std=c17 -mbmi2 -Wall -Wextra -Werror collatz_catalytic.c -o collatz_catalytic
./collatz_catalytic self-test

# Sanitizer verification (Linux GCC/Clang ASan+UBSan, or Windows `zig cc -fsanitize=undefined`)
gcc -O1 -g -std=c17 -fsanitize=address,undefined -Wall -Wextra -Werror collatz_catalytic.c -o collatz_catalytic_san
./collatz_catalytic_san self-test

# Fuzz harness (standalone 250k corpus with UBSan, or Clang -fsanitize=fuzzer,address,undefined)
gcc -O2 -std=c17 -DSTANDALONE_FUZZ_MAIN -fsanitize=address,undefined -Wall -Wextra -Werror fuzz_collatz_catalytic.c -o fuzz_collatz
./fuzz_collatz

# Independent safe-Rust cross-oracle
rustc -O collatz_catalytic_oracle.rs -o collatz_catalytic_oracle
./collatz_catalytic_oracle target-tail 3 10 1 18
./collatz_catalytic_oracle residue-mine 20
```

See [`docs/benchmarks.md`](../../../docs/benchmarks.md) and [`docs/COLLATZ-TOOLSTACK-AND-CATALYTIC-AUDIT.md`](../../../docs/COLLATZ-TOOLSTACK-AND-CATALYTIC-AUDIT.md) for measured timings, RAM budgets, differential oracle parity checks, and honest multi-language toolstack evaluation.
