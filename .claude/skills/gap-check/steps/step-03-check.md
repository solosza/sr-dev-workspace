# Step 3: Check

## Purpose

Apply corpus-appropriate gap checks against the internal model built in Step 2.

## Input

- Corpus type and internal reference model from Step 2
- Gap categories: -> `.claude/docs/design/gap-check/references/gap-categories.md`

## Output

- Findings list — each finding has: category, severity, file, line, description, proposed fix

## Acceptance Criteria

- [ ] All gap categories for the detected corpus type have been applied
- [ ] Universal categories (DEAD_REF, COUNT_MISMATCH) always applied
- [ ] Each finding includes: category, severity (ERROR/WARN), file path, line number, description, proposed fix
- [ ] No files modified (read-only phase)
- [ ] Check completed (0 findings is valid — means clean)

## References

- -> `.claude/docs/design/gap-check/references/gap-categories.md`
- -> `.claude/docs/design/gap-check/references/workflow.md` (Step 3)

## Procedure

For each detected corpus type, apply the relevant gap categories:

**For all corpus types:**
- DEAD_REF: wikilinks, paths that don't resolve
- COUNT_MISMATCH: index says N items, actual count differs

**For skill corpus, add:**
- SCHEMA_MISMATCH: JSON structure described differently in two places
- STALE_TERM: term used but not in vocabulary
- FLOW_GAP: step N says "proceed to step N+1" but N+1 doesn't exist

**For test case corpus, add:**
- COVERAGE_GAP: AC with no TC, TC with no AC
- QUERY_ALIGNMENT: TC exists but no matching query in tc-queries.sql
- TRACEABILITY_GAP: traceability matrix entries that don't match TC or AC IDs
- EXPECTED_RESULT_GAP: TC has no expected result, or result contradicts AC
- VERIFICATION_GAP: tc-queries.sql TCs not in verification-dump.sql UNION

**For design doc corpus, add:**
- COMPLETENESS_GAP: required sections missing per input-contract
- DEPTH_GAP: section present but below minimum depth

## Verification

- Every finding has all 6 fields populated (category, severity, file, line, description, proposed fix)
- Severity is strictly ERROR or WARN
- No false positives from misdetected corpus type

## Failure Recovery

| Condition | Action |
|-----------|--------|
| Check logic error | Log error, skip that category, continue with others |
| Large file causes timeout | Skip file with warning, note in report |
