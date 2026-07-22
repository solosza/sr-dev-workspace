# Gate Contract: Execute-Pipeline Command Routing

## Gates

| Gate | Task | Method | Check |
|------|------|--------|-------|
| READ-01 | 001 | file_exists | `.claude/skills/execute-pipeline/SKILL.md` |
| BUILD-02 | 002 | grep | `grep -l "command.*route\|routing\|design.*build" ".claude/skills/execute-pipeline/SKILL.md"` |
| GAP-03 | 003 | grep | `grep -rL "ERROR" "tasks/execute-pipeline-command-routing/"` |
| BACKLOG-04 | 004 | file_exists | Backlog file created (number determined at runtime) |
| TEST-05 | 005 | file_exists | `.claude/skills/review-queue/SKILL.md` |
