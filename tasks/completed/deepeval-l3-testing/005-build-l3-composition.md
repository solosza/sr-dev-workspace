# Build L3 Composition Reference

## Type
BUILD

## Phase Gate
Tasks 001, 002, and 003 must be complete.

## Deliverable
`.claude/skills/prod-test/references/l3-deepeval-composition.md`

## Instructions
1. Read the composition-architecture design doc: `docs/backlog/154-kernel-build-deepeval-l3-testing/composition-architecture.md`
2. Create `.claude/skills/prod-test/references/l3-deepeval-composition.md` documenting:
   - How prod-test Step 6 detects L3 eligibility (contracts/ folder exists in source repo)
   - How to copy platform-deepeval spec into test repo (.claude/skills/deepeval-management-layer/ + framework/)
   - How to invoke golden dataset translator against contract JSONs
   - How to generate L3 inner tasks (eval suite generation, metric selection, test execution)
   - Composed test repo structure (showing eval/ directory alongside _test/)
   - Platform-deepeval source path: `D:\my_ai_projects\project_test_repos\platform-deepeval`
3. This is a reference file for the prod-test skill, following tiered-index pattern

## Verification
- File exists at `.claude/skills/prod-test/references/l3-deepeval-composition.md`
- Documents composition steps, detection logic, and composed repo structure
