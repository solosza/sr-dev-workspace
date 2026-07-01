# Content Verification: References and Required Sections

## Context
L2 content verification -- confirms each design document has the required sections (especially `## References`) and that each document references 158's research output. Design documents that don't cite their research basis are assumptions, not grounded design.

## Type
TEST

## Execution
agent

## Dependencies
- 010 (structural verification passed)

## Phase Gate
- [ ] Task 010 passed (all 7 documents exist and are non-empty)

## Requirements
For each of the 7 design documents in `projects/eval-platform-design/`:

**Check 1: References section exists**
Run: `grep -q '## References' projects/eval-platform-design/[filename].md`
Must pass for all 7 files.

**Check 2: Each doc references 158's research**
Run: `grep -q 'eval-web-app-research' projects/eval-platform-design/[filename].md`
Must pass for all 7 files.

**Check 3: Prerequisite gate contains verdict**
Run: `grep -q 'Verdict:' projects/eval-platform-design/prerequisite-gate.md`

**Check 4: Key tech stack references present**
- `vertical-plugin-system.md` references `platform-deepeval`
- `execution-pipeline.md` references `Cloud Run`
- `byok-key-management.md` references `session-scoped`
- `api-and-frontend.md` references `FastAPI`
- `multi-tenancy-isolation.md` references `gVisor`

Report pass/fail for each check with evidence.

## Acceptance Criteria
- [ ] All 7 documents have `## References` section
- [ ] All 7 documents reference `eval-web-app-research`
- [ ] `prerequisite-gate.md` contains `Verdict:`
- [ ] Tech stack references present in the correct documents (5 checks)

## Gates Satisfied
- DOC-02, DOC-03, BUILD-10, BUILD-11, BUILD-12, BUILD-13, BUILD-14, BUILD-15

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
