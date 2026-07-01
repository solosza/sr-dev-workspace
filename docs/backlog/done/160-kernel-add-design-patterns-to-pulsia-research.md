# Add Kernel Design Patterns to Pulsia Research

## Status
Open

## Priority
Medium — The pulsia research already has a harness-based architectural blueprint. Adding the formal design patterns (command-skill-pattern, tiered-index-architecture, loop-architecture) gives it the full theoretical foundation. Strengthens the research as a reference for the multi-vertical platform (158/159).

## Summary

Append the three core Isagawa kernel design patterns to the existing pulsia-research project folder. The pulsia research (backlog 128) already analyzed Pulsia's autonomous AI platform and proposed harness loop architectures. These design documents provide the formal specification of the patterns referenced in that research — how commands are structured, how files are organized, and how loops compose.

## What Gets Added

Three new documents appended to `projects/pulsia-research/`:

### 07-command-skill-pattern.md
- Source: `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\docs\design\command-skill-pattern`
- The 6-layer architecture: Command → Skill → Steps → References → Contracts → Hooks
- How the CEO orchestrator loop and primitive loops from `04-architectural-blueprint.md` map to this pattern
- Cross-reference with the existing harness loops in the blueprint

### 08-tiered-index-architecture.md
- Source: `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\docs\design\tiered-index-architecture`
- The three layers: Organization (index/payload), Pre-Generation Checkpoints (directed reading), Contracts & Dual Gates (enforcement)
- How this applies to the multi-tenant state management proposed in the blueprint
- 200-line threshold rule and its impact on scaling the harness design

### 09-loop-architecture.md
- Source: `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\docs\design\loop-architecture`
- The loop primitive: every capability is a loop, loops nest inside loops
- How the CEO orchestrator → primitive loop nesting in `04-architectural-blueprint.md` is a direct instance of this pattern
- Full system view: kernel → domain spec → commands → steps

## Requirements

- Read each source design doc fully (index + all sub-documents)
- Synthesize into pulsia-research context — don't just copy, explain how each pattern applies to the Pulsia-equivalent architecture
- Cross-reference with existing pulsia-research docs (especially `04-architectural-blueprint.md`)
- Update `README.md` to include the three new deliverables
- Update `research-report.md` with a new section referencing the design patterns

## References

- Existing pulsia research: `projects/pulsia-research/`
- Command-skill-pattern: `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\docs\design\command-skill-pattern`
- Tiered-index-architecture: `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\docs\design\tiered-index-architecture`
- Loop-architecture: `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\docs\design\loop-architecture`
- Backlog 128: Pulsia autonomous AI platform research (in done/)
- Backlog 158-159: Multi-vertical platform (these design patterns are foundational)

## Task Builder Input
- **Deliverable:** Three new research documents (07, 08, 09) in `projects/pulsia-research/`, updated README.md and research-report.md
- **Location:** `subproject:pulsia-research`
- **Scope:** RESEARCH
- **Constraints:** Must read full source design docs (not just index files). Must synthesize into pulsia context, not just copy. Must cross-reference with existing blueprint.
