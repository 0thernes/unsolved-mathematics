# Attempts — Carmichael's Totient Conjecture

_Notable attempts, near-misses, retracted proofs._

## Carmichael's own "proof" and retraction (1907, 1922)

The most consequential attempt is the originator's. In his 1907 _Bulletin of the AMS_ paper, **Carmichael presented an argument he believed established** that $A(n)\neq 1$ for all $n$. By 1922 he had identified a **gap** and published a correction reclassifying the assertion as a conjecture, simultaneously proving the first lower bound: any counterexample exceeds $10^{37}$. This is a textbook instance of an elementary-looking claim whose "obvious" proof silently assumes the very uniformity at issue. The retraction is universally accepted and is part of the standard account of the problem; no version of Carmichael's original argument has since been repaired.

## Klee's irreducibility criterion (1947) — a structural near-miss

Victor Klee did not claim a proof but produced the decisive partial result: a **finite criterion** that a minimal counterexample must satisfy, turning an existential question over all integers into a checkable condition. This both organized later computation and made precise just how special a counterexample would be. It falls short of a proof because the criterion can be satisfied in principle for arbitrarily large $m$; it cannot, by itself, exclude all of them.

## Pomerance's conditional structure theorem (1974)

Carl Pomerance's result — that a counterexample $m$ must have $p^2\mid m$ for every prime $p$ with $(p-1)\mid\varphi(m)$ — is the strongest known constraint. It is a genuine theorem, not a claimed resolution, but it is often read as a "near-miss": it shows a counterexample would be so heavily square-constrained that its existence seems to require an implausible conspiracy among shifted primes. It does not rule the conspiracy out, leaving the conjecture open.

## Computational certifications (1990s–2010s)

A sequence of careful computations established successive lower bounds: **Schlafly and Wagon (1994)** verified no counterexample below roughly $10^{10^{7}}$ using Klee-type criteria; **Ford (1998)** extended this to around $10^{10^{10}}$; later refinements pushed further still. These are rigorous within their finite range. The recurring "near-miss" temptation — that such gigantic bounds amount to a proof — is mistaken: each only certifies a finite interval, and the conjecture concerns all integers.

## Sierpiński's multiplicity question — resolved, but not Carmichael's

A frequent source of confusion is the closely related **Sierpiński conjecture**, that every integer $k\geq 2$ occurs as a multiplicity $A(n)$. This was **proved by Kevin Ford in 1998** (building on ideas of Erdős and earlier partial results). Because Sierpiński's problem was settled and looks almost identical, the Carmichael case ($k=1$) is sometimes loosely described as "nearly done." It is not: Ford's methods establish that the multiplicities $\geq 2$ are all realized but say nothing decisive about whether the multiplicity $1$ is ever realized — which is exactly Carmichael's conjecture, and remains open.

## Status of claimed elementary proofs

Because the statement is so accessible, short "proofs" circulate periodically in informal venues. None has survived scrutiny; the typical flaw mirrors Carmichael's own 1907 error — establishing a sibling construction that works for all but an unaddressed special class, then assuming that class is empty. No claimed resolution, in either direction, is accepted by the research community as of the present date.
