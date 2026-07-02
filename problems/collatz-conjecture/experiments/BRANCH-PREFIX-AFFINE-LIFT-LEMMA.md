# Branch-Prefix Affine Lift Lemma

Date: 2026-07-02

This note records a proved local lemma for the shortcut Collatz map

```text
T(n) = n / 2            if n is even
T(n) = (3n + 1) / 2    if n is odd.
```

It is not a proof of the Collatz conjecture. Its role is narrower: it removes
one empirical part of the retimed tight-layer analysis by proving the exact
parent/upper-child lift law used there.

## Lemma 1: Prefix stability modulo powers of two

If `m == n mod 2^d`, then for every `0 <= j <= d`,

```text
T^j(m) == T^j(n) mod 2^(d-j).
```

Consequently, for every `0 <= j < d`, the two states `T^j(m)` and `T^j(n)`
have the same parity.

### Proof

The claim is trivial for `j = 0`. Suppose

```text
T^j(m) - T^j(n) == 0 mod 2^(d-j)
```

with `j < d`. Since the difference is divisible by at least `2`, the two
states have the same parity `p in {0,1}`. If `p = 0`, both states take an
even shortcut step and

```text
T^(j+1)(m) - T^(j+1)(n) = (T^j(m) - T^j(n)) / 2.
```

If `p = 1`, both states take an odd shortcut step and

```text
T^(j+1)(m) - T^(j+1)(n) = 3(T^j(m) - T^j(n)) / 2.
```

In either case the next difference is divisible by `2^(d-j-1)`. Induction
proves the congruence through `j = d`, and the same-parity statement follows
for all `j < d`. QED.

## Lemma 2: Exact affine delta for an upper lift

Let

```text
m = n + 2^d.
```

For `0 <= j <= d`, let `o_j` be the number of odd shortcut steps among the
first `j` steps of either orbit. This is well-defined by Lemma 1. Then

```text
T^j(m) - T^j(n) = 3^o_j 2^(d-j).
```

### Proof

At `j = 0`, the difference is `2^d`, so the formula holds. Each shared even
shortcut step divides the current difference by `2`; each shared odd shortcut
step multiplies it by `3` and then divides by `2`. After `j` shared steps,
there have been `o_j` odd multipliers by `3` and `j` divisions by `2`, hence

```text
T^j(m) - T^j(n) = 2^d * 3^o_j / 2^j = 3^o_j 2^(d-j).
```

QED.

## Boundary parity corollary

At the boundary `j = d`, the difference is

```text
T^d(m) - T^d(n) = 3^o_d,
```

which is odd. Therefore `T^d(m)` and `T^d(n)` have opposite parity. There are
only two boundary types:

```text
E -> O: parent even, upper child odd
O -> E: parent odd, upper child even
```

The retimed tight surplus-`1` records are all of type `E -> O`.

## Excess-jump corollary

Let

```text
E_j(x) = odd_count_j(x) - theta * j,
theta = log(2) / log(3).
```

For an upper lift, the first `d` parities match. At step `d`, the boundary
parity is opposite. Therefore, at step `d+1`:

```text
E -> O  implies  E_(d+1)(m) - E_(d+1)(n) =  1
O -> E  implies  E_(d+1)(m) - E_(d+1)(n) = -1
```

This explains the one-unit pressure jump observed in the tight records: the
checked tight cases are all `E -> O`, so the child has exactly one more odd
shortcut step than the parent at `d+1`.

## Connection to the tight retimed layer-one records

The exact run

```text
experiments/results/branch_prefix_retimed_tight_lift_algebra_d18_d25_20260702.json
```

verified these proved lemmas on the five tight records and found:

```text
all parities are shared before depth d:          true
all affine lift laws hold to depth:              true
all boundary pairs are parent even -> child odd: true
all child excess gaps at pressure are 1:         true
```

The first two lines are no longer empirical mysteries; they are instances of
Lemmas 1 and 2. The remaining proof target is sharper:

```text
For a live upper-lift retimed transition with surplus 1 at its first
above-parent pressure event, prove the boundary type is E->O and the boundary
odd step lies inside an align-3 local word OOO or OOOEOO.
```

That remaining statement is not proved here. The current repo evidence says it
holds for the checked exact window `18 -> 19` through `25 -> 26`.
