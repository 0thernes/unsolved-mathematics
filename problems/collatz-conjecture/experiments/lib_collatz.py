#!/usr/bin/env python3
"""lib_collatz — canonical Collatz primitives for the experiments suite.

Single source of truth for the maps and cylinder algebra that ~90 scripts
had been re-implementing independently (repo audit 2026-07-02, roadmap #1).
New instruments should import from here; existing ones migrate
opportunistically. Pure stdlib, deterministic, exhaustively self-tested:

    python lib_collatz.py        # runs the self-test, exits nonzero on failure

Conventions. "Classic" map C(n): 3n+1 on odds, n/2 on evens. "Shortcut"
(Terras) map T(n): (3n+1)/2 on odds, n/2 on evens — every shortcut step
performs exactly one halving. Parity words are tuples of 0/1 (even/odd),
length d, with o = number of ones. On the cylinder {x ≡ r_w (mod 2^d)}:

    T^d(x) = (3^o · x + c(w)) / 2^d,   c accumulates c → 3c + 2^i at odd step i,

with fixed point ρ_w = c(w) / (2^d − 3^o) (odd denominator, hence in ℤ₂),
and the conjugation identity T^d(x) − ρ_w = (3^o/2^d)(x − ρ_w).
Nothing here proves any part of the conjecture; the conjecture is OPEN.
"""
from __future__ import annotations

from fractions import Fraction


def classic_step(n: int) -> int:
    """One step of the classic map C."""
    return 3 * n + 1 if n & 1 else n >> 1


def shortcut_step(n: int) -> int:
    """One step of the shortcut (Terras) map T."""
    return (3 * n + 1) >> 1 if n & 1 else n >> 1


def classic_stats(n: int) -> tuple[int, int]:
    """(total classic steps to 1, trajectory peak). n >= 1."""
    steps, peak = 0, n
    while n != 1:
        n = classic_step(n)
        steps += 1
        if n > peak:
            peak = n
    return steps, peak


def shortcut_stats(n: int) -> tuple[int, int]:
    """(total shortcut steps to 1, odd steps among them). n >= 1."""
    total = odd = 0
    while n != 1:
        if n & 1:
            odd += 1
        n = shortcut_step(n)
        total += 1
    return total, odd


def parity_word(x: int, d: int) -> tuple[int, ...]:
    """First d parities of x's shortcut orbit (depends only on x mod 2^d)."""
    w = []
    for _ in range(d):
        w.append(x & 1)
        x = shortcut_step(x)
    return tuple(w)


def affine_coeffs(w: tuple[int, ...]) -> tuple[int, int]:
    """(3^o, c(w)) with T^d(x) = (3^o·x + c(w)) / 2^d on w's cylinder."""
    three_o, c = 1, 0
    for i, bit in enumerate(w):
        if bit:
            c = 3 * c + (1 << i)
            three_o *= 3
    return three_o, c


def cylinder_residue(w: tuple[int, ...]) -> int:
    """The unique r mod 2^d whose orbit realizes parity word w (Terras
    bijection), by bit-lifting: choose each next bit to force the parity."""
    d = len(w)
    r = 0
    for k in range(d):
        # try current r; if the k-th parity is wrong, set bit k
        if parity_word(r, k + 1)[k] != w[k]:
            r |= 1 << k
    return r


def spine(w: tuple[int, ...]) -> Fraction:
    """ρ_w = c(w)/(2^d − 3^o), the affine fixed point of the word's block map.
    Requires d >= 1 and 2^d != 3^o (always true for d >= 1)."""
    d = len(w)
    if d < 1:
        raise ValueError("d >= 1 required")
    three_o, c = affine_coeffs(w)
    return Fraction(c, (1 << d) - three_o)


def is_supercritical(w: tuple[int, ...]) -> bool:
    """3^o > 2^d — the climbing corridors."""
    three_o, _ = affine_coeffs(w)
    return three_o > (1 << len(w))


def certificate_q0(w: tuple[int, ...]) -> int | None:
    """Descent-certificate threshold: for subcritical w (3^o < 2^d), all
    n = 2^d·q + r_w with q >= q0 satisfy T^d(n) < n. None if supercritical."""
    d = len(w)
    three_o, c = affine_coeffs(w)
    denom = (1 << d) - three_o
    if denom <= 0:
        return None
    r = cylinder_residue(w)
    tdr = (three_o * r + c) >> d  # = T^d(r), exact by the affine law
    return max(0, (tdr - r) // denom + 1)


def _self_test() -> None:
    # 1. Known trajectory facts for n = 27.
    assert classic_stats(27) == (111, 9232)
    assert shortcut_stats(27) == (70, 41)
    # 2. Affine law: exhaustive over all words of length <= 8, random q.
    import itertools
    for d in range(1, 9):
        for w in itertools.product((0, 1), repeat=d):
            three_o, c = affine_coeffs(w)
            r = cylinder_residue(w)
            assert parity_word(r, d) == w, (w, r)  # bijection realized
            for q in (0, 1, 7, 10 ** 6):
                n = (q << d) + r
                x = n
                for _ in range(d):
                    x = shortcut_step(x)
                assert x == (three_o * n + c) >> d, (w, q)
                assert (three_o * n + c) % (1 << d) == 0
    # 3. Spines of the three known negative cycles are their own members.
    assert spine((1,)) == Fraction(-1)                      # -1 cycle
    w5 = parity_word(-5, 3)
    assert spine(w5) == Fraction(-5) and is_supercritical(w5)
    w17 = parity_word(-17, 11)
    assert spine(w17) == Fraction(-17) and is_supercritical(w17)
    # 4. Conjugation identity spot-check on the -17 spine cylinder.
    d, (three_o, c) = 11, affine_coeffs(w17)
    rho = spine(w17)
    for n in (2 ** 11 * 5 - 17, 2 ** 30 * 3 - 17):
        x = n
        for _ in range(d):
            x = shortcut_step(x)
        assert Fraction(x) - rho == Fraction(three_o, 1 << d) * (Fraction(n) - rho)
    # 5. Certificate threshold sanity: word of 27 at depth 59 certifies with q0 = 0
    #    (session-verified fact: 3^37 < 2^59 and T^59(27) = 23 < 27).
    w27 = parity_word(27, 59)
    assert certificate_q0(w27) == 0
    print("lib_collatz self-test: all checks passed")


if __name__ == "__main__":
    _self_test()
