# Step 7: Report

## Purpose

Summarize what was created and provide next steps for the user.

## Input

- Files written from Step 6
- Completeness results from Step 5
- Command name from Step 1

## Output

- Summary report to user
- State file cleaned up

## Acceptance Criteria

- [ ] Report includes: path, reference design used, completeness score, file count, step count
- [ ] Report includes next step: `/build-command .claude/docs/design/[name]/index.md`
- [ ] State file deleted on success

## References

- Design doc: `.claude/docs/design/design-command/references/workflow.md` (Step 7)

## Procedure

1. Compile report from completed steps:
   - Command name
   - Design doc path
   - Reference design used
   - Completeness score (N/7 required, N/5 optional)
   - Files written (count)
   - Workflow steps defined (count)
2. Present report to user
3. Delete `.claude/state/design-command-state.json` if it exists

## Verification

Report format:
```
DESIGN DOC CREATED: /[command-name]

Path: .claude/docs/design/[name]/index.md
Reference design: [which existing design was used as template]
Completeness: 7/7 required, N/5 optional
Files: N files written
Steps: M workflow steps defined

Ready for: /build-command .claude/docs/design/[name]/index.md
```

## Failure Recovery

| Situation | Action |
|-----------|--------|
| State file missing | Report without state cleanup (non-fatal) |
| Completeness was partial | Include warnings in report |
