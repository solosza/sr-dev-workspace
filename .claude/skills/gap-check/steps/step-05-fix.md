# Step 5: Fix

## Purpose

Apply fixes to discovered gaps with user approval. Only runs if `--fix` flag was passed or user requests fix mode after seeing the report.

## Input

- Findings list from Step 3 (with proposed fixes)
- User approval per finding

## Output

- Modified files (only approved fixes applied)
- Fix summary: applied count vs skipped count

## Acceptance Criteria

- [ ] Only triggered by `--fix` flag or explicit user request after report
- [ ] Each finding presented one at a time with proposed fix
- [ ] User must approve each fix (or use `approve all` for batch)
- [ ] Fix applied via Edit tool (not Write — preserves file context)
- [ ] Fix summary printed after all findings processed

## References

- -> `.claude/docs/design/gap-check/references/workflow.md` (Step 5)

## Procedure

1. Present each finding one at a time:
   ```
   Finding 1/N: [CATEGORY] file_path:line
   Description text
   Proposed fix: Fix text

   [approve / modify / skip / approve all / stop]
   ```
2. Handle user response:
   - `approve`: Apply the proposed fix using Edit tool
   - `modify`: User provides alternative fix text, apply that
   - `skip`: Move to next finding without change
   - `approve all`: Apply all remaining fixes without asking
   - `stop`: Exit fix mode immediately
3. After all findings processed (or stopped), print summary:
   ```
   FIXES APPLIED: X/N
     Applied: findings 1, 3, 5
     Skipped: findings 2, 4

   Re-run /gap to verify fixes.
   ```

## Verification

- Each applied fix verified by re-reading the file after edit
- Fix summary counts match actual changes
- Skipped findings noted in summary

## Failure Recovery

| Condition | Action |
|-----------|--------|
| Edit fails (old_string not found) | Report "Fix could not be applied — file may have changed", skip to next |
| User provides invalid response | Re-prompt with valid options |
| File is read-only | Report permission error, skip to next |
