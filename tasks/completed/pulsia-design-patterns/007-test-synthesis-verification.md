# Synthesis Verification — Content Quality

## Context

L2 functional verification. Confirms the three design pattern documents actually synthesize the source patterns into Pulsia context rather than copying. Checks that cross-references are meaningful (not just name-drops) and that each document explains the mapping between the formal pattern and Pulsia's architecture.

## Type
TEST

## Execution
agent

## Dependencies
- 001-research-write-command-skill-pattern
- 002-research-write-tiered-index-architecture
- 003-research-write-loop-architecture

## Phase Gate
- [ ] `projects/pulsia-research/07-command-skill-pattern.md` exists
- [ ] `projects/pulsia-research/08-tiered-index-architecture.md` exists
- [ ] `projects/pulsia-research/09-loop-architecture.md` exists

## Requirements

For each of the three pattern documents (07, 08, 09), verify:

1. **Synthesis check** — The document explains how the pattern applies to Pulsia's architecture, not just what the pattern is. Look for:
   - Specific references to Pulsia components (CEO orchestrator, primitive loops, tenant isolation, hive mind, nightly cycle)
   - Mapping statements connecting pattern concepts to blueprint concepts
   - At least one concrete example showing how a Pulsia component instantiates the pattern

2. **Cross-reference quality** — References to `04-architectural-blueprint.md` are substantive:
   - Not just "see 04-architectural-blueprint.md" — the reference explains what it connects to
   - At least one specific blueprint concept is named (e.g., "CEO orchestrator loop", "tenant-scoped state", "hub-and-spoke composition")

3. **Completeness check per document:**
   - 07: Covers all 6 layers (Command, Skill, Steps, References, Contracts, Hooks) and maps at least the CEO orchestrator and one primitive loop
   - 08: Covers all 3 layers (Organization, Checkpoints, Contracts) and maps to multi-tenant state or shared lessons
   - 09: Covers the loop primitive, nesting/composition, and maps the full system view to Pulsia's tier structure

4. **No copy-paste** — Documents should not contain verbatim blocks from the source design docs that are not attributed as quotes. Paraphrasing and synthesis is required.

Report PASS/FAIL for each check with specific evidence.

## Acceptance Criteria

- [ ] All 3 documents pass synthesis check
- [ ] All 3 documents pass cross-reference quality check
- [ ] All 3 documents pass completeness check
- [ ] No verbatim copy-paste detected
- [ ] Report produced with evidence for each check

## Gates Satisfied
- DOC-10, DOC-11, DOC-12

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
