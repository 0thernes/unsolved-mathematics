# 🧭 Philosophy

> *Why this atlas exists, what it refuses to do, and the principles that govern
> every entry in it.*

## The premise

Open problems are the growth tips of mathematics. They are where the subject is
still alive — unfinished, contested, and human. Yet the knowledge about them is
fragmented: a definition on Wikipedia, the real ideas in a survey behind a
paywall, the live frontier in a seminar nobody recorded, the history in a
biography out of print. **A person trying to understand *why* the Riemann
Hypothesis is hard has to assemble that picture themselves, every time.**

This atlas is an attempt to do that assembly once, carefully, and in the open —
and to keep it current as a versioned, reproducible artifact.

## Five principles

### 1. Honesty over hype
Mathematics is the one domain where you cannot bluff a result into existence.
We carry that ethic into the documentation itself:

- Scores are **editorial estimates**, labeled as such, with a published formula.
- Every paper and person carries a **verification flag**. AI-suggested
  scaffolding is never disguised as a checked citation.
- We never write that a problem is solved unless it is, with a reference. Where a
  claimed proof is **disputed** (the abc conjecture's IUT saga is the canonical
  case), we present the disagreement faithfully and take no side the community
  has not taken.

### 2. Structure is understanding
A flat list teaches nothing. By forcing every problem into the same eight-part
dossier — origin, originator, approaches, attempts, papers, people, status,
corpus — the *shape* of each problem becomes comparable. You can see that
Goldbach and Twin Primes share a sieve-theoretic frontier; that BSD and RH are
both really about L-functions; that P vs NP's difficulty is a *barrier* result
(relativization, natural proofs, algebrization), not just an absence of effort.

### 3. Built for two kinds of reader
Humans read prose; machines read structure. The atlas serves both without
compromise: the same dossier that a person reads is chunked into a retrieval
corpus an AI can reason over. The goal is a knowledge base you can *ask
questions of* — "what links the Riemann Hypothesis to random matrix theory?" —
not just one you can scroll.

### 4. Reproducibility is a feature, not overhead
The ranking is a pure function of the registry. The folders are generated. The
README table regenerates itself. This is deliberate: a knowledge base you cannot
rebuild is a knowledge base you cannot trust. Anyone can clone the repo, run one
command, and get *byte-identical* generated artifacts.

### 5. Ranking is an argument, not a verdict
Ordering 40 of the deepest questions ever asked is inherently presumptuous. We
do it anyway — because a defensible, transparent ordering is more useful than no
ordering — but we treat the ranking as a **falsifiable claim**. Disagree with
where the Jacobian Conjecture sits? Change its `difficulty` in the registry,
rerun, and argue from the diff. The methodology is in
[docs/methodology/RANKING.md](docs/methodology/RANKING.md).

## On the ambition

The brief that started this project asked for something on the scale of a "world-
class mathematics institute": exhaustive, cutting-edge, uncompromising. We take
that seriously *and* literally about the one thing that matters most — **rigor**.
The flashiest possible version of this project would be one that overstated its
own certainty. The actually-elite version is one that an expert can audit line by
line and find honest. That is the standard here.

## What this atlas is not

- It is **not** a claim to have solved or to be solving these problems. It is
  research infrastructure — a map, not a conquest.
- It is **not** a substitute for primary sources. It is a structured index *into*
  them, with provenance.
- It is **not** finished. It is a living instrument, tracked on the
  [Kanban board](docs/kanban/KANBAN.md).

## A note on the "RAG for us" goal

Turning these findings into a retrieval-augmented knowledge base is not a
gimmick bolted on at the end — it is the reason for the structure. A well-formed
dossier *is* a well-formed corpus. When you ask the atlas a question, it should
answer from sourced, chunked, attributable text, and tell you exactly which
problem and which file the answer came from. That is the difference between a
search engine and an understanding engine, and it is the long arc of this work.

---

*"The important thing is not to stop questioning. Curiosity has its own reason
for existing."* — attributed to **Albert Einstein**
