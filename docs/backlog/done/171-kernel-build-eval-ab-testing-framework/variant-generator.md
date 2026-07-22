# Variant Generator

## Status
NEW

## Location
`platform-deepeval/framework/ab_testing/variant_generator.py`

## What It Does

Takes any tiered artifact (SKILL.md → steps/ → references/) and produces two variants:

- **Variant A (flat):** All content concatenated into a single markdown file, preserving logical order but removing all index structure, wikilinks, checkpoints, and contracts
- **Variant B (tiered):** The original tiered structure copied as-is

## Flattening Algorithm

```
1. Read the root file (SKILL.md or command .md)
2. Parse all internal references (→ links, wikilinks, "Read and follow:" directives)
3. Topological sort by dependency (parent before child)
4. For each file in order:
   a. Strip index-only content (file tables, "Reading Order" sections, navigation)
   b. Keep payload content (rules, steps, criteria, examples)
   c. Append to flat output with section headers preserving hierarchy
5. Remove checkpoint directives ("Pre-Generation Checkpoint", "Directed Reading")
6. Remove contract references (gate-contract.md, dual gate sections)
7. Output: single .md file with all knowledge, no structure
```

## Key Design Decisions

- **Preserve content, remove structure** — the flat variant must have the SAME knowledge, just organized differently. This isolates the variable (structure) from confounds (missing information).
- **Deterministic** — same input always produces same flat output. No LLM in the flattening step.
- **Reference resolution** — inline references like "see step-03.md" become inline content. External references (URLs, repo paths) stay as-is.

## Input/Output

| Field | Type | Description |
|-------|------|-------------|
| `artifact_path` | Path | Root of the tiered artifact (directory containing SKILL.md or command .md) |
| `output_dir` | Path | Where to write both variants |

Output:
```
output_dir/
├── flat/
│   └── artifact-flat.md        ← all content in one file
└── tiered/
    ├── SKILL.md                ← original structure preserved
    ├── steps/
    └── references/
```

## Dependencies
- None (pure file processing, no LLM calls)
