# Task 017: L1 Test — Verify All Files Exist

## Action
Verify all deliverable files from tasks 001-016 exist.

## Checks

### Platform-deepeval framework files
```bash
test -f "D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/__init__.py"
test -f "D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/variant_generator.py"
test -f "D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/runner.py"
test -f "D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/scorer.py"
test -f "D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/reporter.py"
test -f "D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/experiment_config.py"
```

### Eval skill step files
```bash
test -f ".claude/skills/eval/steps/step-ab-1-generate-variants.md"
test -f ".claude/skills/eval/steps/step-ab-2-build-prompt.md"
test -f ".claude/skills/eval/steps/step-ab-3-run-iterations.md"
test -f ".claude/skills/eval/steps/step-ab-4-score-outputs.md"
test -f ".claude/skills/eval/steps/step-ab-5-compare-report.md"
```

### Updated files contain AB content
```bash
grep -q "ab" ".claude/skills/eval/steps/step-00-resolve-source.md"
grep -q "ab" ".claude/skills/eval/workflow.md"
grep -q "ab" ".claude/skills/eval/SKILL.md"
grep -q "ab" ".claude/skills/eval/gate-contract.md"
grep -q "\-\-ab" ".claude/commands/kernel/eval.md"
```

## Acceptance Criteria
- All file existence checks pass
- All grep checks pass
- Report: N/N files present
