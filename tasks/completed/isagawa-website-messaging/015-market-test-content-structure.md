# L2 Test: Verify Content Structure and Key Terms

## Context
Level 2 functional verification — confirm deliverable files have required sections and key terms that indicate substantive content.

## Type
TEST

## Execution
agent

## Dependencies
- 013-market-build-final-recommendation

## Phase Gate
- [ ] `projects/isagawa-website-messaging/final-recommendation.md` exists

## Requirements
- Run grep checks for required sections:
  1. `messaging-audit.md` contains "Current Copy" and "Gaps"
  2. `positioning-report.md` contains "Positioning Alternative"
  3. `variant-a-technical.md` contains "Hero"
  4. `variant-b-business.md` contains "Hero"
  5. `variant-c-future.md` contains "Hero"
  6. `final-recommendation.md` contains "Recommended"
- Verify minimum content length (each file > 20 lines)
- Verify key Isagawa terms appear across deliverables: "kernel", "enforcement", "governance"
- Report pass/fail for each check

## Acceptance Criteria
- [ ] All grep checks pass
- [ ] All files exceed 20 lines minimum
- [ ] Key terms present in deliverables
- [ ] Test report produced with pass/fail per check

## Gates Satisfied
FUNC-01 through FUNC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
