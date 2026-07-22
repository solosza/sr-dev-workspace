# Step 6: Write Files

## Purpose

Save the validated design doc to disk at `.claude/docs/design/[name]/`.

## Input

- Validated draft content from Step 5 (PASS result)
- Command name from Step 1

## Output

- Files on disk at `.claude/docs/design/[name]/`
- State file updated with files_written list

## Acceptance Criteria

- [ ] Directory created: `.claude/docs/design/[name]/references/`
- [ ] index.md written with YAML frontmatter
- [ ] references/workflow.md written with step details
- [ ] Any additional payload files written
- [ ] All files verified readable after write

## References

- Design doc: `.claude/docs/design/design-command/references/workflow.md` (Step 6)

## Procedure

1. Create directory: `.claude/docs/design/[name]/references/`
2. Write `index.md` (the index file)
3. Write `references/workflow.md` (step details)
4. Write any additional payload files identified in Step 4
5. Verify all files written successfully (read back each file)
6. Update state file with files_written list

## Verification

- All planned files exist on disk
- Each file is readable (no write errors)
- index.md has valid YAML frontmatter

## Failure Recovery

| Situation | Action |
|-----------|--------|
| Write fails (permissions) | Report error with path, stop |
| Partial write (some files written) | State tracks which files written, re-run writes missing |
