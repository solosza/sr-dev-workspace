# Task 020: Test L2 — Verify Content Match Across All Repos

## Objective
Verify all kernel files in target repos are identical to the master versions.

## Instructions

For each of the 17 repos, diff all kernel commands, hooks, and key infrastructure files against the master:

```bash
MASTER="D:/my_ai_projects/isagawa-kernel"
# Same REPOS array as task 019

FAILURES=0
for repo in "${REPOS[@]}"; do
  name=$(basename "$repo")
  repo_fails=0

  # Diff kernel commands
  for f in "$MASTER/.claude/commands/kernel/"*.md; do
    fname=$(basename "$f")
    if ! diff -q "$f" "$repo/.claude/commands/kernel/$fname" > /dev/null 2>&1; then
      echo "DIFF: $name — commands/kernel/$fname"
      repo_fails=$((repo_fails+1))
    fi
  done

  # Diff hooks (kernel hooks only)
  for h in actions-log-appender.py agent-inline-execution-blocker.py auto-approve-claude-writes.py domain-gate-enforcer.template.py test-failure-detector.py universal-gate-enforcer.py; do
    if ! diff -q "$MASTER/.claude/hooks/$h" "$repo/.claude/hooks/$h" > /dev/null 2>&1; then
      echo "DIFF: $name — hooks/$h"
      repo_fails=$((repo_fails+1))
    fi
  done

  # Diff run-task.sh
  if ! diff -q "$MASTER/run-task.sh" "$repo/run-task.sh" > /dev/null 2>&1; then
    echo "DIFF: $name — run-task.sh"
    repo_fails=$((repo_fails+1))
  fi

  if [[ $repo_fails -eq 0 ]]; then
    echo "MATCH: $name"
  else
    FAILURES=$((FAILURES+repo_fails))
  fi
done
echo "Total diffs: $FAILURES"
```

## Acceptance Criteria
- All kernel files match master exactly
- Zero diffs

## Gate
TEST-20
