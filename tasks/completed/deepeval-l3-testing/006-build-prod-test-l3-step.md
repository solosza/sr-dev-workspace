# Build prod-test L3 Step Integration

## Type
BUILD

## Phase Gate
Task 005 must be complete.

## Deliverable
Updated `.claude/skills/prod-test/references/step-06-inner-tasks.md` with L3 deepeval section.

## Instructions
1. Read the current step-06 reference: `.claude/skills/prod-test/references/step-06-inner-tasks.md`
2. Read the new L3 composition reference: `.claude/skills/prod-test/references/l3-deepeval-composition.md` (from task 005)
3. Add an L3 section to step-06-inner-tasks.md that:
   - Checks for L3 eligibility (contracts/ exists)
   - If eligible, references l3-deepeval-composition.md for composition steps
   - Defines L3 inner task templates: translate contracts, generate eval suite, run deepeval tests
   - Specifies L3 task ordering: after L1 and L2 tasks
   - Includes score collection in Step 8 report
4. Do NOT remove or modify existing L1/L2 sections

## Verification
- `grep -l "L3\|deepeval" .claude/skills/prod-test/references/step-06-inner-tasks.md` returns match
- Existing L1/L2 content preserved
