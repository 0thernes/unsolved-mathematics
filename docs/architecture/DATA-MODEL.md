# 🧱 Data Model

A concise reference for the shapes that flow through the atlas. The
[ERD](ERD.md) gives the conceptual model; this document gives the concrete
serialized forms and the invariants the build enforces.

## Registry entry (`data/problems.yaml`)

```yaml
- slug: riemann-hypothesis          # PK, kebab-case, unique
  title: "The Riemann Hypothesis"
  field: "Analytic Number Theory"
  subfields: ["Complex Analysis", "L-functions"]
  year_posed: 1859                  # int, negative = BCE
  originators: ["Bernhard Riemann"]
  millennium_prize: true
  statement_plain: "Every non-trivial zero of ζ has real part 1/2."
  difficulty: 99                    # 0–100
  centrality: 100                   # 0–100
  tractability: 8                   # 0–100 (higher = closer to a proof)
  status: "open"                    # enum
  tags: ["primes", "zeta", "RH"]
```

Validated by [`schema/problem.schema.json`](../../schema/problem.schema.json).

## Computed record (`data/problems.json`)

The generator augments every entry with derived fields:

```jsonc
{
  "slug": "riemann-hypothesis",
  // ...all source fields...
  "css": 89.87,     // Composite Severity Score
  "rank": 1         // position by descending CSS
}
```

## Paper row (`papers.md` tables)

Each paper is a row with a mandatory verification flag, mappable to
[`schema/paper.schema.json`](../../schema/paper.schema.json):

```markdown
| # | Year | Title | Author(s) | Kind | Identifier | Verify |
|---|------|-------|-----------|------|-----------|--------|
| 1 | 1859 | Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse | B. Riemann | foundational | — | high-confidence |
```

## Person row (`mathematicians.md` tables)

```markdown
| # | Name | Era | Role | Contribution |
|---|------|-----|------|--------------|
| 1 | Bernhard Riemann | 19th c. | originator | Posed the hypothesis (1859) |
```

## Chunk record (`rag/corpus.jsonl`)

See [rag/README.md](../../rag/README.md) for the full schema. One JSON object per
retrieval chunk, carrying `slug`, `rank`, `section`, `heading`, `text`,
`source`, `tokens`.

## Invariants (enforced by build/CI)

1. **Unique slugs.** No two registry entries share a `slug`.
2. **Schema-valid registry.** Every entry passes `problem.schema.json`.
3. **Ranking is a pure function** of the registry — `generate.py --check`
   recomputes it and CI fails if committed views are stale.
4. **Every paper row has a verification flag.** No unflagged citations.
5. **`recently-resolved` ⇒ cited resolution.** A resolved status requires a
   resolving reference in `status.md`.
6. **Derived fields are never hand-edited.** `css`, `rank`, and `metadata.json`
   are always regenerated.

## Identity & keys

- **Problem identity** = `slug` (stable). The numeric folder prefix `NNN` is the
  *current rank* and may change as scores are refined; never key off it.
- **Cross-references** between problems use `slug` (e.g. RH ↔ Montgomery pair
  correlation ↔ Hardy–Littlewood).
