# Verify Loop Template

## Context
Verify all Phase 1 generalized loop template files exist, have non-zero content, valid JSON, and correct structure.

## Type
TEST

## Execution
inline

## Dependencies
- 003, 004, 005, 006, 007, 008, 009

## Requirements
- All 7 template files exist with non-zero content
- SKILL.md contains DECLARE, DETERMINE, DESCRIBE sections
- SKILL.md contains contract references (input, output, rules, integration)
- SKILL.md contains [DOMAIN-SPECIFIC] placeholders
- All 5 JSON files parse successfully
- Gate-contract-template.md exists with non-zero content
- Scenario-template.json has test_cases array

## Acceptance Criteria
- [x] 7 template files exist with non-zero content
- [x] SKILL.md has DDD sections (6 matches)
- [x] SKILL.md has contract references (10 matches)
- [x] SKILL.md has [DOMAIN-SPECIFIC] placeholders (5 matches)
- [x] All 5 JSON files are valid
- [x] Gate-contract-template.md exists (4010 bytes)
- [x] Scenario-template.json exists (2962 bytes)

## Gates Satisfied
- TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
