# Verify factory-produced SSH spec has correct structure

## Context
Check the output matches platform-docker's architecture, not the old invented structure.

## Type
TEST

## Execution
agent

## Dependencies
- 010

## Phase Gate
- [ ] Factory run completed (010)

## Requirements
- Spawn agent to verify C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/:
- Has .claude/skills/ with SKILL.md
- Has framework/ directory matching platform-docker structure (image_objects/, tasks/, roles/, tests/)
- Has ImageInterface (not SSHInterface) or equivalent Docker-based foundation
- References CIS/STIG compliance
- Does NOT have paramiko references (that was the old invented spec)

## Acceptance Criteria
- [ ] Output follows platform-docker architecture (verify: agent report)

## Gates Satisfied
PROD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
