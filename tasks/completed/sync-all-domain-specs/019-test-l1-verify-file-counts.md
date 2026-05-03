# Task 019: Test L1 — Verify File Counts Across All Repos

## Objective
Verify all 17 target repos have the correct kernel file counts.

## Instructions

For each of the 17 repos, verify:
1. 15 kernel commands in `.claude/commands/kernel/`
2. 7 kernel skill folders in `.claude/skills/` (audit-workflow, autonomous-cycling, execute-pipeline, kernel-domain-setup, prod-test, task-builder, website-cloner)
3. 6 kernel hooks in `.claude/hooks/` (actions-log-appender.py, agent-inline-execution-blocker.py, auto-approve-claude-writes.py, domain-gate-enforcer.template.py, test-failure-detector.py, universal-gate-enforcer.py)
4. Infrastructure files exist: `run-task.sh`, `lib/common.sh`, `lib/attestation/intent.py`

```bash
MASTER="D:/my_ai_projects/isagawa-kernel"
REPOS=(
  "D:/my_ai_projects/project_test_repos/cognitive-agent"
  "D:/my_ai_projects/project_test_repos/domain-spec-factory"
  "D:/my_ai_projects/project_test_repos/game-dev"
  "D:/my_ai_projects/project_test_repos/game-engine-master"
  "D:/my_ai_projects/project_test_repos/healthcare-qa-spec-master"
  "D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa"
  "D:/my_ai_projects/project_test_repos/isagawa-qa-zentyant"
  "D:/my_ai_projects/project_test_repos/platform-deepeval"
  "D:/my_ai_projects/project_test_repos/platform-playwright"
  "D:/my_ai_projects/project_test_repos/platform-selenium"
  "D:/my_ai_projects/project_test_repos/test-content-production"
  "D:/my_ai_projects/project_test_repos/test-kernel-bootstrap"
  "D:/my_ai_projects/project_test_repos/test-platform-deepeval"
  "D:/my_ai_projects/isagawa-kernel-a"
  "D:/my_ai_projects/isagawa-kernel-b"
  "D:/my_ai_projects/py_sel_framework_mcp"
  "D:/my_ai_projects/qa_kernel_test"
)

FAILURES=0
for repo in "${REPOS[@]}"; do
  name=$(basename "$repo")
  cmd_count=$(ls "$repo/.claude/commands/kernel/"*.md 2>/dev/null | wc -l)
  hook_count=$(ls "$repo/.claude/hooks/"*.py 2>/dev/null | wc -l)
  # Check 7 specific kernel skill folders
  skill_count=0
  for s in audit-workflow autonomous-cycling execute-pipeline kernel-domain-setup prod-test task-builder website-cloner; do
    test -d "$repo/.claude/skills/$s" && skill_count=$((skill_count+1))
  done

  if [[ "$cmd_count" -ne 15 || "$skill_count" -ne 7 || "$hook_count" -lt 6 ]]; then
    echo "FAIL: $name — cmds=$cmd_count skills=$skill_count hooks=$hook_count"
    FAILURES=$((FAILURES+1))
  else
    echo "PASS: $name"
  fi
done
echo "Failures: $FAILURES"
```

## Acceptance Criteria
- All 17 repos report PASS
- Zero failures

## Gate
TEST-19
