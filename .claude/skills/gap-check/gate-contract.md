# Gate Contract

## Phase Gates

| Gate | Trigger | Check | On Fail |
|------|---------|-------|---------|
| Analysis -> Fix | After Step 4 report | Report presented to user; user explicitly enters fix mode | Stay in analysis; user may re-run or exit |
| Fix entry | Before Step 5 | `--fix` flag passed OR user typed `fix` after report | Skip Step 5; report is the final output |

## Step Gates

| Step | Output | Validation |
|------|--------|-----------|
| 1. Discover | File inventory list | At least 1 file found in target path |
| 2. Detect & Model | Corpus type + reference model | At least 1 corpus type detected; model has at least 1 entry |
| 3. Check | Findings list | Check completed (0 findings is valid — means clean) |
| 4. Report | Formatted gap report | Report printed to user (errors first, then warnings) |
| 5. Fix | Fix summary | Each applied fix verified (file re-read after edit confirms change) |

## Read-Only Constraint

Steps 1-4 are strictly read-only. The agent must not use Write, Edit, or Bash-with-side-effects during the analysis phase. This is enforced by protocol (Critical Rule 1), not by hook.

## Severity Rules

| Severity | Meaning | Examples |
|----------|---------|---------|
| ERROR | Something is broken — will cause failures | DEAD_REF, COVERAGE_GAP, ARTIFACT_MISSING, COMPLETENESS_GAP |
| WARN | Something is suspicious — may indicate drift | STALE_TERM, DEPTH_GAP, EXPECTED_RESULT_GAP |
