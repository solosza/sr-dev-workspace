# Task 016: Write Ability Saves Input Contract

## Type
BUILD

## Dependencies
- 010 (loop template verified)

## Action
Write `input-contract.json` for the ability-saves loop at:
`D:/my_ai_projects/project_test_repos/dnd-game-engine-test/.claude/skills/ability-saves/contracts/input-contract.json`

Extract the input section from the existing `ability-saves-contract.json` into the separated DDD input contract format, following the template at `.claude/skills/loop-template/contracts/input-template.json`.

## Acceptance Criteria
- [ ] File exists at `ability-saves/contracts/input-contract.json`
- [ ] Valid JSON (parseable)
- [ ] Contains `loop_name: "ability-saves"`
- [ ] Contains `receives` object with all input fields from existing contract
- [ ] Contains `required_context` array
- [ ] Contains `validation` object with required_fields, type_checks, constraints
- [ ] Follows input-template.json structure

## Status
pending
