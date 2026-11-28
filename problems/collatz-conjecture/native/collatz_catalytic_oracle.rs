// SPDX-License-Identifier: MIT
//
// collatz_catalytic_oracle.rs — Independent Safe-Rust Cross-Verifier (Build Standard B11/B12/B16)
//
// Zero `unsafe` blocks. Independently implements:
//   1. Exact 128-bit Odd-Unit-Lock valuation & Fine-Wilf ceiling check
//   2. FKM supercritical Lyndon generator + bit-reversed prefix-slice histogram
//   3. Catalytic fixed-stack DFS finite-residue descent certificate miner
//
// Used to differentially cross-check BOTH `collatz_catalytic.c` (C17/BMI2) AND
// the exact Python `Fraction` oracle (`odd_unit_lock_target_tail_lab.py`,
// `collatz_residue_lab.py`). Proves NO part of the Collatz Conjecture (OPEN).

use std::env;
use std::time::Instant;

fn tile_lsb64(word_bits: u32, d: u32) -> u64 {
    let mut out = 0u64;
    let mut shift = 0u32;
    let block = word_bits as u64;
    while shift < 64 {
        out |= block << shift;
        shift += d;
    }
    out
}

fn min_supercritical_ones(d: u32) -> u32 {
    let two_d = 1u128 << d;
    let mut p3 = 1u128;
    let mut o = 0u32;
    while p3 <= two_d {
        p3 *= 3;
        o += 1;
    }
    o
}

fn fkm_gen<F: FnMut(u32, u32)>(
    n: u32,
    o_min: u32,
    t: u32,
    p: u32,
    ones: u32,
    a: &mut [u8; 36],
    cb: &mut F,
) {
    if ones + (n - t + 1) < o_min {
        return;
    }
    if t > n {
        if p == n && ones >= o_min {
            let mut bits = 0u32;
            for i in 1..=n {
                if a[i as usize] != 0 {
                    bits |= 1u32 << (i - 1);
                }
            }
            cb(bits, n);
        }
        return;
    }
    let bit = a[(t - p) as usize];
    a[t as usize] = bit;
    fkm_gen(n, o_min, t + 1, p, ones + bit as u32, a, cb);
    if bit == 0 {
        a[t as usize] = 1;
        fkm_gen(n, o_min, t + 1, t, ones + 1, a, cb);
    }
}

fn run_target_tail(s_min: u32, s_max: u32, t_min: u32, t_max: u32) {
    let t0 = Instant::now();
    let mut a = [0u8; 36];
    let mut phases: Vec<u64> = Vec::new();
    let mut src_cnt = 0usize;
    for d in s_min..=s_max {
        let o_min = min_supercritical_ones(d);
        a[0] = 0;
        fkm_gen(d, o_min, 1, 1, 0, &mut a, &mut |bits, len| {
            src_cnt += 1;
            let mask = if len == 32 { u32::MAX } else { (1u32 << len) - 1 };
            for rot_t in 0..len {
                let rot = if rot_t == 0 {
                    bits
                } else {
                    ((bits >> rot_t) | (bits << (len - rot_t))) & mask
                };
                phases.push(tile_lsb64(rot, len).reverse_bits());
            }
        });
    }

    let mut targets: Vec<u64> = Vec::new();
    for d in t_min..=t_max {
        let o_min = min_supercritical_ones(d);
        a[0] = 0;
        fkm_gen(d, o_min, 1, 1, 0, &mut a, &mut |bits, len| {
            targets.push(tile_lsb64(bits, len).reverse_bits());
        });
    }
    targets.sort_unstable();

    let mut hist = [0u64; 64];
    let mut pair_count = 0u64;
    let mut zero_skips = 0u64;
    let mut max_e = 0u32;

    for &pkey in &phases {
        let mut lo = 0usize;
        let mut hi = targets.len();
        let mut prefix = 0u64;
        for k in 0..64u32 {
            if lo >= hi {
                break;
            }
            let bit_mask = 1u64 << (63 - k);
            let split_key = prefix | bit_mask;
            let mid = lo + targets[lo..hi].partition_point(|&x| x < split_key);
            let (m_lo, m_hi) = if (pkey & bit_mask) == 0 {
                let r = (mid, hi);
                hi = mid;
                r
            } else {
                let r = (lo, mid);
                lo = mid;
                prefix |= bit_mask;
                r
            };
            let cnt = (m_hi - m_lo) as u64;
            if cnt > 0 {
                hist[k as usize] += cnt;
                pair_count += cnt;
                if k > max_e {
                    max_e = k;
                }
            }
        }
        if lo < hi {
            zero_skips += (hi - lo) as u64;
        }
    }

    let elapsed = t0.elapsed().as_secs_f64();
    println!("{{");
    println!("  \"engine\": \"collatz_catalytic_safe_rust\",");
    println!("  \"primitive_source_cycles\": {},", src_cnt);
    println!("  \"source_phases\": {},", phases.len());
    println!("  \"target_spines\": {},", targets.len());
    println!("  \"source_phase_target_pairs\": {},", pair_count);
    println!("  \"zero_separation_skips\": {},", zero_skips);
    println!("  \"max_valuation_e\": {},", max_e);
    print!("  \"valuation_histogram\": {{");
    let mut first = true;
    for (k, &v) in hist.iter().enumerate() {
        if v > 0 {
            if !first {
                print!(", ");
            }
            print!("\"{}\": {}", k, v);
            first = false;
        }
    }
    println!("}},");
    println!("  \"elapsed_seconds\": {:.6}", elapsed);
    println!("}}");
}

fn run_residue_mine(max_depth: u32) {
    let t0 = Instant::now();
    let mut pow3 = [1u128; 64];
    for i in 1..=(max_depth as usize) {
        pow3[i] = pow3[i - 1] * 3;
    }
    let mut stack: [(u32, u32, u64, u128); 128] = [(0, 0, 0, 0); 128];
    let mut sp = 0usize;
    stack[sp] = (1, 1, 1, 2);
    sp += 1;
    stack[sp] = (1, 0, 0, 0);
    sp += 1;

    let mut certified_leaves = 0u64;
    let mut frontier_leaves = 0u64;
    let mut certified_units = 0u128;
    let mut frontier_units = 0u128;
    let scale = 1u128 << max_depth;
    let mut max_q_thresh = 0u128;

    while sp > 0 {
        sp -= 1;
        let (depth, odd_count, residue, image) = stack[sp];
        let two_d = 1u128 << depth;
        let p3 = pow3[odd_count as usize];
        if p3 < two_d {
            certified_leaves += 1;
            certified_units += scale >> depth;
            let denom = two_d - p3;
            let q_thresh = if image >= residue as u128 {
                ((image - residue as u128) / denom) + 1
            } else {
                0
            };
            if q_thresh > max_q_thresh {
                max_q_thresh = q_thresh;
            }
            continue;
        }
        if depth >= max_depth {
            frontier_leaves += 1;
            frontier_units += 1;
            continue;
        }
        let nd = depth + 1;
        let r0 = residue;
        let r1 = residue | (1u64 << depth);
        let o0 = odd_count + (image & 1) as u32;
        let img0 = if (image & 1) != 0 { (3 * image + 1) >> 1 } else { image >> 1 };
        let raw1 = image + p3;
        let o1 = odd_count + (raw1 & 1) as u32;
        let img1 = if (raw1 & 1) != 0 { (3 * raw1 + 1) >> 1 } else { raw1 >> 1 };
        stack[sp] = (nd, o1, r1, img1);
        sp += 1;
        stack[sp] = (nd, o0, r0, img0);
        sp += 1;
    }

    let elapsed = t0.elapsed().as_secs_f64();
    println!("{{");
    println!("  \"engine\": \"collatz_catalytic_safe_rust_dfs\",");
    println!("  \"max_depth\": {},", max_depth);
    println!("  \"certified_leaves\": {},", certified_leaves);
    println!("  \"frontier_leaves\": {},", frontier_leaves);
    println!("  \"certified_units_mod_2^max_depth\": {},", certified_units);
    println!("  \"frontier_units_mod_2^max_depth\": {},", frontier_units);
    println!("  \"max_q_threshold\": {},", max_q_thresh);
    println!("  \"elapsed_seconds\": {:.6}", elapsed);
    println!("}}");
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: collatz_catalytic_oracle target-tail s_min s_max t_min t_max | residue-mine max_depth");
        std::process::exit(1);
    }
    match args[1].as_str() {
        "target-tail" => {
            let s_min = args[2].parse().unwrap();
            let s_max = args[3].parse().unwrap();
            let t_min = args[4].parse().unwrap();
            let t_max = args[5].parse().unwrap();
            run_target_tail(s_min, s_max, t_min, t_max);
        }
        "residue-mine" => {
            let d = args[2].parse().unwrap();
            run_residue_mine(d);
        }
        _ => std::process::exit(2),
    }
}
