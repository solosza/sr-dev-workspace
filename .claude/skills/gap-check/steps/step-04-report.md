# Step 4: Report

## Purpose

Present findings in a scannable, actionable format grouped by severity and category.

## Input

- Findings list from Step 3
- Target path and corpus type from Steps 1-2

## Output

- Formatted gap report printed to user

## Acceptance Criteria

- [ ] Report includes header: target path, corpus type, files scanned count
- [ ] Errors listed first, then warnings
- [ ] Within each severity, findings ordered by file path
- [ ] Each finding shows: number, category tag, file:line, description, proposed fix
- [ ] Summary line at bottom: "N errors, M warnings"
- [ ] Clean report format if no gaps found

## References

- -> `.claude/docs/design/gap-check/references/workflow.md` (Step 4)

## Procedure

1. Sort findings: errors first, then warnings; within each, by file path
2. Print report header:
   ```
   GAP REPORT: [target-path]
   Corpus type: [detected type(s)]
   Files scanned: N
   ```
3. Print each finding:
   ```
   ERRORS (must fix):
     1. [CATEGORY] file_path:line
        Description text
        Fix: Proposed fix text

   WARNINGS (should review):
     N. [CATEGORY] file_path:line
        Description text
        Fix: Proposed fix text
   ```
4. Print summary: `Summary: N errors, M warnings`
5. If no gaps found, print: `No gaps found. Clean.`

## Verification

- Report is printed (not written to file)
- Findings are numbered sequentially
- No findings are omitted from report

## Failure Recovery

| Condition | Action |
|-----------|--------|
| Findings list is empty | Print clean report (no gaps found) |
| Finding missing a field | Print what's available, mark missing field as "[unknown]" |
