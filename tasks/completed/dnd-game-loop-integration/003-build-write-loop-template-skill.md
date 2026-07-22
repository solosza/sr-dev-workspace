# Write Loop Template SKILL.md

## Context
Write the generalized loop template SKILL.md. This is the DDD skeleton that all loops instantiate from. It defines the Declare-Determine-Describe workflow pattern, contract integration points, and composition interface.

## Type
BUILD

## Execution
inline

## Dependencies
- 002 (directory exists)

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/` exists

## Requirements
- Write to `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/SKILL.md`
- Must include DDD structure: DECLARE (load context, present state), DETERMINE (apply rules, route to sub-loops), DESCRIBE (validate output, narrate results)
- Must include contract references: input, output, rules, integration
- Must include composition section: how this loop integrates as inner loop (receives/returns) and as outer loop (invokes inner loops)
- Must include placeholders marked `[DOMAIN-SPECIFIC]` for domain content
- Reference: `D:/my_ai_projects/project_test_repos/dnd-game-engine-test/.claude/skills/ability-saves/SKILL.md` as gold standard

## Acceptance Criteria
- [ ] `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/loop-template/SKILL.md` exists
- [ ] File contains "DECLARE", "DETERMINE", "DESCRIBE" sections
- [ ] File contains contract references (input, output, rules, integration)
- [ ] File contains `[DOMAIN-SPECIFIC]` placeholders

## Gates Satisfied
- BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
