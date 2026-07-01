# Structural Verification — All Deliverables Exist

## Context

L1 structural verification. Confirms all 5 deliverable files exist, have required content markers, and satisfy the gate contract's structural checks. This is a mechanical check — no content quality judgment.

## Type
TEST

## Execution
agent

## Dependencies
- 001-research-write-command-skill-pattern
- 002-research-write-tiered-index-architecture
- 003-research-write-loop-architecture
- 004-research-update-readme
- 005-research-update-research-report

## Phase Gate
- [ ] All 5 deliverable files have been written (tasks 001-005 complete)

## Requirements

Run the following structural checks:

1. **File existence (BUILD-01 through BUILD-03):**
   - `test -f projects/pulsia-research/07-command-skill-pattern.md`
   - `test -f projects/pulsia-research/08-tiered-index-architecture.md`
   - `test -f projects/pulsia-research/09-loop-architecture.md`

2. **README update (BUILD-04):**
   - `grep -q '09-loop-architecture' projects/pulsia-research/README.md`

3. **Research report update (BUILD-05):**
   - `grep -q 'Design Patterns' projects/pulsia-research/research-report.md`

4. **Source references (DOC-01 through DOC-03):**
   - `grep -q 'command-skill-pattern' projects/pulsia-research/07-command-skill-pattern.md`
   - `grep -q 'tiered-index-architecture' projects/pulsia-research/08-tiered-index-architecture.md`
   - `grep -q 'loop-architecture' projects/pulsia-research/09-loop-architecture.md`

5. **Cross-references to blueprint (DOC-04 through DOC-06):**
   - `grep -q '04-architectural-blueprint' projects/pulsia-research/07-command-skill-pattern.md`
   - `grep -q '04-architectural-blueprint' projects/pulsia-research/08-tiered-index-architecture.md`
   - `grep -q '04-architectural-blueprint' projects/pulsia-research/09-loop-architecture.md`

6. **Synthesis markers (DOC-07 through DOC-09):**
   - `grep -q 'Pulsia' projects/pulsia-research/07-command-skill-pattern.md`
   - `grep -q 'Pulsia' projects/pulsia-research/08-tiered-index-architecture.md`
   - `grep -q 'Pulsia' projects/pulsia-research/09-loop-architecture.md`

Report PASS/FAIL for each check with the gate ID.

## Acceptance Criteria

- [ ] All 15 structural checks pass
- [ ] Report produced listing each gate ID and PASS/FAIL status

## Gates Satisfied
- BUILD-01, BUILD-02, BUILD-03, BUILD-04, BUILD-05, DOC-01, DOC-02, DOC-03, DOC-04, DOC-05, DOC-06, DOC-07, DOC-08, DOC-09

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
