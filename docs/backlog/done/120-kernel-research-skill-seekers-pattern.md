# Research: Skill Seekers Pattern — Auto-Package Research Into Callable Skills

## Status
Open

## Priority
Medium — `projects/` now contains 10+ research deliverables (govcon, business credit, ugc, geo services, hoi-an knockoff shirts, etc.) that are inert markdown. A pattern for turning accumulated research into callable kernel skills would make this knowledge reusable across future pipelines.

## Summary
The "Skill Seekers" pattern is a proposed mechanism for auto-packaging completed research deliverables (stored in `projects/`) into callable `.claude/skills/` entries. When research produces structured findings (market analysis, pricing strategy, GTM recommendation), those findings should be referenceable by future pipelines without re-running the research. The pattern defines how to package, index, and invoke accumulated knowledge as skills.

## Requirements
- Survey existing `projects/` deliverables — what research outputs exist, what format are they in, are they structured enough to be indexed?
- Define what a "research skill" looks like: SKILL.md that indexes findings, key facts as structured data, callable via `/kernel/task-builder` context injection
- Assess auto-packaging feasibility: can a script scan `projects/*/` and generate skill stubs automatically, or does each one need manual curation?
- Evaluate the invocation model: how would a future pipeline reference "use findings from hoi-an-knockoff-shirts research"?
- Compare to retrieval-augmented approaches (RAG, vector search) — is a skill-based index better than embedding search for this use case?
- Identify the minimum viable pattern: what's the smallest implementation that makes research reusable?

## References
- Existing research deliverables: `projects/hoi-an-knockoff-shirts/`, `projects/govcon-research/`, `projects/business-credit-research/`, `projects/ai-ugc-research/`, `projects/geo-services-research/`
- Existing skill format: `.claude/skills/task-builder/SKILL.md`, `.claude/skills/autonomous-cycling/SKILL.md`
- Backlog 116: Superpowers integration (skills ecosystem context)

## Task Builder Input
- **Deliverable:** Research report — pattern design for research-to-skill packaging, auto-packaging feasibility assessment, and a minimal spec for the Skill Seekers pattern (or recommendation to skip if complexity outweighs value)
- **Location:** `subproject:skill-seekers-research`
- **Scope:** RESEARCH
- **Constraints:** Must fit existing `.claude/skills/` format. Auto-packaging should not require external dependencies beyond Python stdlib. If a manual curation step is unavoidable, that's acceptable — document the workflow.
