# Analyze Isagawa Codebase for Swarm Patterns

## Type
RESEARCH

## Description
Read the existing harness code — run-task.sh, execute-pipeline skill, prod-test skill, autonomous-cycling skill. Map each component to swarm concepts: is run-task.sh a swarm orchestrator? Are one-shot agents "swarm workers"? Is the gate contract a handoff protocol? Document what Isagawa already does that qualifies as "agent teams" and what the delta is vs a purpose-built swarm framework.

## Deliverable
`projects/kernel-architecture/swarms-codebase-mapping.md`

## Files to Read
- `run-task.sh`
- `.claude/skills/execute-pipeline/SKILL.md`
- `.claude/skills/prod-test/SKILL.md`
- `.claude/skills/autonomous-cycling/SKILL.md`

## Acceptance Criteria
- [ ] `projects/kernel-architecture/swarms-codebase-mapping.md` exists
- [ ] Maps run-task.sh, execute-pipeline, prod-test to swarm concepts
- [ ] Identifies the delta between "pipeline of one-shot agents" and "team of persistent agents"
