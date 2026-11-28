// SPDX-License-Identifier: MIT
//
// collatz_hydra_oracle.rs — Independent Safe-Rust Cross-Verifier for
// `collatz_asymmetric_hydra.c` (Zero `unsafe` blocks, Build Standard B11/B12/B16).
//
// Independently reproduces key invariants across Vectors A, B, C, D, E:
//   - Vector A: mod-3 chiral asymmetry on odd x in [1, 100000) & zero div-3 intercepts
//   - Vector B: exact Minimax Demon n*_B (stopping time & total steps) + 3n-1 basins
//   - Vector C: exact carry-avalanche sum & sign-conjugacy T^d(-x) == -T_-^d(x)
//   - Vector D: exact Tropical Karp max cycle mean on Z/72Z, Z/144Z and positive box [1, 50]
//   - Vector E: exact LZ76 complexity on Demon n = 27 orbit word
//
// Explicit Non-Claim: Exact finite cross-verifier; proves NO part of Collatz (OPEN).

use std::env;

fn step_t(x: i64) -> i64 {
    if (x & 1) != 0 {
        (3 * x + 1) >> 1
    } else {
        x >> 1
    }
}

fn step_tminus(x: i64) -> i64 {
    if (x & 1) != 0 {
        (3 * x - 1) >> 1
    } else {
        x >> 1
    }
}

fn gcd_i64(mut a: i64, mut b: i64) -> i64 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    if a == 0 { 1 } else { a }
}

#[derive(Clone, Copy, PartialEq, Eq)]
struct Rat(i64, i64);

fn make_rat(mut n: i64, mut d: i64) -> Rat {
    if d < 0 {
        n = -n;
        d = -d;
    }
    let g = gcd_i64(n, d);
    Rat(n / g, d / g)
}

fn cmp_rat(a: Rat, b: Rat) -> i32 {
    let lhs = (a.0 as i128) * (b.1 as i128);
    let rhs = (b.0 as i128) * (a.1 as i128);
    if lhs < rhs { -1 } else if lhs > rhs { 1 } else { 0 }
}

fn karp_max_cycle_mean(v_cnt: usize, adj: &[[usize; 2]], deg: &[usize], wt: &[i32], active: &[bool]) -> Rat {
    let mut id_map = vec![usize::MAX; v_cnt];
    let mut rev_map = Vec::new();
    for u in 0..v_cnt {
        if active[u] {
            id_map[u] = rev_map.len();
            rev_map.push(u);
        }
    }
    let n = rev_map.len();
    if n == 0 {
        return Rat(-1, 1);
    }
    let neg_inf = -1_000_000_000i32;
    let mut dp = vec![neg_inf; (n + 1) * n];
    for i in 0..n {
        dp[i] = 0;
    }
    for k in 1..=n {
        let prev_off = (k - 1) * n;
        let cur_off = k * n;
        for ui in 0..n {
            let pval = dp[prev_off + ui];
            if pval <= neg_inf / 2 {
                continue;
            }
            let u = rev_map[ui];
            let cand = pval + wt[u];
            for e in 0..deg[u] {
                let vi = id_map[adj[u][e]];
                if vi != usize::MAX && cand > dp[cur_off + vi] {
                    dp[cur_off + vi] = cand;
                }
            }
        }
    }
    let mut found = false;
    let mut best = Rat(-1, 1);
    let last_off = n * n;
    for vi in 0..n {
        let lv = dp[last_off + vi];
        if lv <= neg_inf / 2 {
            continue;
        }
        let mut has_min = false;
        let mut vmin = Rat(0, 1);
        for k in 0..n {
            let pk = dp[k * n + vi];
            if pk <= neg_inf / 2 {
                continue;
            }
            let r = make_rat((lv - pk) as i64, (n - k) as i64);
            if !has_min || cmp_rat(r, vmin) < 0 {
                vmin = r;
                has_min = true;
            }
        }
        if has_min && (!found || cmp_rat(vmin, best) > 0) {
            best = vmin;
            found = true;
        }
    }
    if found { best } else { Rat(-1, 1) }
}

fn adelic_pruned_karp(m: usize, eps: i64) -> Rat {
    let half = m / 2;
    let mut adj = vec![[0usize; 2]; m];
    let mut deg = vec![0usize; m];
    let mut wt = vec![0i32; m];
    let mut active = vec![false; m];
    for u in 0..m {
        if (u & 1) == 0 {
            wt[u] = 0;
            let v0 = u / 2;
            let v1 = (v0 + half) % m;
            adj[u][0] = v0;
            adj[u][1] = v1;
            deg[u] = if v0 == v1 { 1 } else { 2 };
        } else {
            wt[u] = 1;
            let raw = (3 * (u as i64) + eps) / 2;
            let v0 = (((raw % (m as i64)) + (m as i64)) % (m as i64)) as usize;
            let v1 = (v0 + half) % m;
            adj[u][0] = v0;
            adj[u][1] = v1;
            deg[u] = if v0 == v1 { 1 } else { 2 };
        }
        active[u] = (u % 3 != 0) && if eps == 1 { u != m - 1 } else { u != 1 };
    }
    karp_max_cycle_mean(m, &adj, &deg, &wt, &active)
}

fn box_karp(lo: usize, hi: usize, eps: i64) -> Rat {
    let v = hi + 1;
    let mut adj = vec![[0usize; 2]; v];
    let mut deg = vec![0usize; v];
    let mut wt = vec![0i32; v];
    let mut active = vec![false; v];
    for x in lo..=hi {
        active[x] = true;
        wt[x] = (x & 1) as i32;
        let nxt = if (x & 1) != 0 { (3 * (x as i64) + eps) >> 1 } else { (x as i64) >> 1 };
        if nxt >= lo as i64 && nxt <= hi as i64 {
            adj[x][0] = nxt as usize;
            deg[x] = 1;
        }
    }
    karp_max_cycle_mean(v, &adj, &deg, &wt, &active)
}

fn classify_tminus(start: u64) -> i32 {
    let mut x = start as u128;
    for _ in 0..50000 {
        if x == 1 { return 1; }
        if x == 5 || x == 7 || x == 10 { return 5; }
        if matches!(x, 17 | 25 | 37 | 55 | 82 | 41 | 61 | 91 | 136 | 68 | 34) {
            return 17;
        }
        x = if (x & 1) != 0 { (3 * x - 1) >> 1 } else { x >> 1 };
    }
    0
}

fn lz76(s: &[u8]) -> usize {
    let n = s.len();
    if n == 0 { return 0; }
    let mut c = 1usize;
    let mut i = 0usize;
    let mut l = 1usize;
    let mut k = 1usize;
    let mut k_max = 1usize;
    while l + k <= n {
        if s[i + k - 1] == s[l + k - 1] {
            k += 1;
            if l + k > n {
                c += 1;
                break;
            }
        } else {
            if k > k_max { k_max = k; }
            i += 1;
            if i == l {
                c += 1;
                l += k_max;
                if l >= n { break; }
                i = 0;
                k = 1;
                k_max = 1;
            } else {
                k = 1;
            }
        }
    }
    c
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let max_b: u32 = if args.len() >= 2 { args[1].parse().unwrap_or(16) } else { 16 };

    // Vector A: mod-3 chiral check
    let mut mod3_ok = 0u64;
    for x in (1..100000i64).step_by(2) {
        if step_t(x).rem_euclid(3) == 2 && step_tminus(x).rem_euclid(3) == 1 {
            mod3_ok += 1;
        }
    }

    // Vector B: exact Minimax Demons up to 2^max_b
    let limit = 1u64 << max_b;
    let mut best_stop_n = 3u64;
    let mut best_stop_v = 0u32;
    let mut best_tot_n = 3u64;
    let mut best_tot_v = 0u32;
    let mut sib_1 = 0u64;
    let mut sib_5 = 0u64;
    let mut sib_17 = 0u64;
    for n in (3..limit).step_by(2) {
        let mut x = n as u128;
        let mut steps = 0u32;
        let mut stop = 0u32;
        let mut stopped = false;
        while x != 1 {
            x = if (x & 1) != 0 { (3 * x + 1) >> 1 } else { x >> 1 };
            steps += 1;
            if !stopped && x < n as u128 {
                stop = steps;
                stopped = true;
            }
        }
        if !stopped { stop = steps; }
        if stop > best_stop_v { best_stop_v = stop; best_stop_n = n; }
        if steps > best_tot_v { best_tot_v = steps; best_tot_n = n; }
        match classify_tminus(n) {
            1 => sib_1 += 1,
            5 => sib_5 += 1,
            17 => sib_17 += 1,
            _ => {}
        }
    }

    // Vector C: carry-avalanche sum & sign conjugacy
    let mut carry_p = 0u64;
    let mut carry_m = 0u64;
    for x in (1..(1u64 << 16)).step_by(2) {
        carry_p += ((x << 1) ^ x ^ (3 * x + 1)).count_ones() as u64;
        carry_m += ((x << 1) ^ (x - 1) ^ (3 * x - 1)).count_ones() as u64;
    }
    let mut conj_bad = 0u64;
    for x in -5000..5000i64 {
        let (mut a, mut b) = (-x, x);
        for _ in 0..12 {
            a = step_t(a);
            b = step_tminus(b);
        }
        if a != -b { conj_bad += 1; }
    }

    // Vector D: exact Tropical Karp on M = 72, 144 and box [1, 50]
    let m72_p = adelic_pruned_karp(72, 1);
    let m72_m = adelic_pruned_karp(72, -1);
    let m144_p = adelic_pruned_karp(144, 1);
    let m144_m = adelic_pruned_karp(144, -1);
    let box_p = box_karp(1, 50, 1);
    let box_m = box_karp(2, 50, -1);

    // Vector E: LZ76 on n = 27
    let mut bits27 = Vec::new();
    let mut x27 = 27u128;
    while x27 != 1 {
        bits27.push((x27 & 1) as u8);
        x27 = if (x27 & 1) != 0 { (3 * x27 + 1) >> 1 } else { x27 >> 1 };
    }
    let lz27 = lz76(&bits27);

    println!("{{");
    println!("  \"engine\": \"collatz_hydra_safe_rust_oracle\",");
    println!("  \"max_bits\": {},", max_b);
    println!("  \"vector_a_mod3_ok\": {},", mod3_ok);
    println!("  \"vector_b_demon_stop_n\": {},", best_stop_n);
    println!("  \"vector_b_demon_stop_steps\": {},", best_stop_v);
    println!("  \"vector_b_demon_total_n\": {},", best_tot_n);
    println!("  \"vector_b_demon_total_steps\": {},", best_tot_v);
    println!("  \"vector_b_sibling_basins\": {{\"to_1\": {}, \"to_5\": {}, \"to_17\": {}}},", sib_1, sib_5, sib_17);
    println!("  \"vector_c_carry_sum_16bit\": {{\"3n+1\": {}, \"3n-1\": {}}},", carry_p, carry_m);
    println!("  \"vector_c_sign_conjugacy_mismatches\": {},", conj_bad);
    println!("  \"vector_d_karp_72\": {{\"plus\": \"{}/{}\", \"minus\": \"{}/{}\"}},", m72_p.0, m72_p.1, m72_m.0, m72_m.1);
    println!("  \"vector_d_karp_144\": {{\"plus\": \"{}/{}\", \"minus\": \"{}/{}\"}},", m144_p.0, m144_p.1, m144_m.0, m144_m.1);
    println!("  \"vector_d_box_50\": {{\"plus\": \"{}/{}\", \"minus_no1\": \"{}/{}\"}},", box_p.0, box_p.1, box_m.0, box_m.1);
    println!("  \"vector_e_n27\": {{\"word_len\": {}, \"lz76_phrases\": {}}}", bits27.len(), lz27);
    println!("}}");
}
