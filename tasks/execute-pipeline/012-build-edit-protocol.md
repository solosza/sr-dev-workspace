# Edit Protocol — Add Execute-Pipeline Skill Reference

## Context
The sr_dev protocol is an index that lists all kernel skills. The new execute-pipeline skill must be registered there.

## Type
BUILD

## Execution
inline

## Dependencies
- 004 (SKILL.md must exist)

## Requirements
- Edit `.claude/protocols/sr_dev-protocol.md`
- Add execute-pipeline skill to the Kernel references table:
  `| Execute Pipeline Skill | .claude/skills/execute-pipeline/SKILL.md |`
- Place it in alphabetical order among the other skill entries
- Do NOT modify any other content in the protocol

## Acceptance Criteria
- [ ] `grep -q 'execute-pipeline' .claude/protocols/sr_dev-protocol.md` exits 0
- [ ] Entry appears in the Kernel references table

## Gates Satisfied
- BUILD-12

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
