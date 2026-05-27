# Run spec factory for SSH domain with platform-docker template

## Context
The real test: spawn agent to run the full 12-step factory pipeline. This is Execution: factory.

## Type
TEST

## Execution
agent

## Dependencies
- 009

## Phase Gate
- [ ] Old output cleaned (009)

## Requirements
- Spawn agent with prompt:
- You are operating in the domain-spec-factory at C:/Users/solos/my_ai_projects/domain-spec-factory/
- Read C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/SKILL.md for the 12-step pipeline
- Read C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/workflow.md for data flow
- Your goal: run the spec factory for ssh-image-testing domain
- Template platform: C:/Users/solos/my_ai_projects/platform-docker/ (read FRAMEWORK.md, framework/ structure, tests/)
- Execute steps 1-10 (research, score, design, build spec files)
- Skip steps 11-12 (validation + package) for now
- Write all output to C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/
- Report what you produced

## Acceptance Criteria
- [ ] SKILL.md exists at C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/.claude/skills/*/SKILL.md (verify: file_exists)

## Gates Satisfied
PROD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
