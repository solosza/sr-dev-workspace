# Task 021: Test L3 — Verify Domain Content Preserved

## Objective
Verify domain-specific content was not deleted or overwritten during sync.

## Instructions

Check a sample of domain-specific content across repos:

```bash
FAILURES=0

# cognitive-agent: domain commands
for cmd in image-on-failure image-pre-construction image-workflow; do
  test -f "D:/my_ai_projects/project_test_repos/cognitive-agent/.claude/commands/$cmd.md" && echo "PASS: cognitive-agent/$cmd" || { echo "FAIL: cognitive-agent/$cmd"; FAILURES=$((FAILURES+1)); }
done

# domain-spec-factory: domain skill
test -d "D:/my_ai_projects/project_test_repos/domain-spec-factory/.claude/skills/spec-factory" && echo "PASS: domain-spec-factory/spec-factory skill" || { echo "FAIL"; FAILURES=$((FAILURES+1)); }

# game-dev: domain commands + skill
test -f "D:/my_ai_projects/project_test_repos/game-dev/.claude/commands/game-build.md" && echo "PASS: game-dev/game-build" || { echo "FAIL"; FAILURES=$((FAILURES+1)); }
test -d "D:/my_ai_projects/project_test_repos/game-dev/.claude/skills/game-engine" && echo "PASS: game-dev/game-engine skill" || { echo "FAIL"; FAILURES=$((FAILURES+1)); }

# hmsa-healthcare-qa: domain commands
test -f "D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/commands/qa-onboard.md" && echo "PASS: hmsa/qa-onboard" || { echo "FAIL"; FAILURES=$((FAILURES+1)); }

# platform-deepeval: domain skill
test -d "D:/my_ai_projects/project_test_repos/platform-deepeval/.claude/skills/deepeval-management-layer" && echo "PASS: platform-deepeval/deepeval skill" || { echo "FAIL"; FAILURES=$((FAILURES+1)); }

# test-content-production: domain commands
test -f "D:/my_ai_projects/project_test_repos/test-content-production/.claude/commands/content-calendar.md" && echo "PASS: test-content-production/content-calendar" || { echo "FAIL"; FAILURES=$((FAILURES+1)); }

# py_sel_framework_mcp: domain commands + skills
test -f "D:/my_ai_projects/py_sel_framework_mcp/.claude/commands/qa-workflow.md" && echo "PASS: py_sel/qa-workflow" || { echo "FAIL"; FAILURES=$((FAILURES+1)); }
test -d "D:/my_ai_projects/py_sel_framework_mcp/.claude/skills/qa-management-layer" && echo "PASS: py_sel/qa-management-layer" || { echo "FAIL"; FAILURES=$((FAILURES+1)); }

# Protocols preserved (spot check)
test -f "D:/my_ai_projects/project_test_repos/cognitive-agent/.claude/protocols/image_testing-protocol.md" && echo "PASS: cognitive-agent protocol" || { echo "FAIL"; FAILURES=$((FAILURES+1)); }

# State files untouched (spot check)
test -d "D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/state" && echo "PASS: hmsa state dir" || echo "SKIP: no state dir"

echo ""
echo "Failures: $FAILURES"
```

## Acceptance Criteria
- All domain-specific content preserved
- Zero failures

## Gate
TEST-21
