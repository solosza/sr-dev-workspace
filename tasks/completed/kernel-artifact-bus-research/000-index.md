# Inter-Agent Artifact Bus Research — Task Index

## Goal
Determine whether sub-agents should export structured manifests (exports/manifest.json) that downstream agents ingest, replacing convention-based output discovery. Owns the combined 241/242/243 recommendation. Verdict: YAH or NAY.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-project-dir]] | BUILD | none | pending |
| 002 | [[002-research-manifest-schema]] | RESEARCH | 001 | pending |
| 003 | [[003-research-consumer-and-overlap]] | RESEARCH | 001 | pending |
| 004 | [[004-research-combined-recommendation]] | RESEARCH | 001 | pending |
| 005 | [[005-build-write-research-report]] | BUILD | 002, 003, 004 | pending |

## Gate Contract
> [[gate-contract.md]]

## Deliverables
- `projects/kernel-artifact-bus-research/01-*.md`, `02-*.md`, `03-*.md` (task outputs)
- `projects/kernel-artifact-bus-research/research-report.md` (verdict: YAH or NAY)
