# Gate Contract — Self-Improvement Observability

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Observatory repo exists | file_exists | `test -d D:/my_ai_projects/kernel-observatory` | Create directory |
| BUILD-02 | metrics.jsonl schema exists | file_exists | `test -f D:/my_ai_projects/kernel-observatory/schemas/metrics.jsonl.schema.json` | Create file |
| BUILD-03 | experiments.jsonl schema exists | file_exists | `test -f D:/my_ai_projects/kernel-observatory/schemas/experiments.jsonl.schema.json` | Create file |
| BUILD-04 | learn-events.jsonl schema exists | file_exists | `test -f D:/my_ai_projects/kernel-observatory/schemas/learn-events.jsonl.schema.json` | Create file |
| BUILD-05 | aggregate.py exists | file_exists | `test -f D:/my_ai_projects/kernel-observatory/lib/aggregate.py` | Create file |
| BUILD-06 | learn.md has emission hook | grep | `grep -q 'metrics.jsonl' D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/learn.md` | Add emission |
| BUILD-07 | complete.md has emission hook | grep | `grep -q 'metrics.jsonl' D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/complete.md` | Add emission |
| BUILD-08 | anchor.md has emission hook | grep | `grep -q 'metrics.jsonl' D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/anchor.md` | Add emission |
| BUILD-09 | learn.md has baseline snapshot step | grep | `grep -q 'pre_learn_baseline' D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/learn.md` | Add baseline step |
| BUILD-10 | learn.md has regression check step | grep | `grep -q 'regression' D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/learn.md` | Add regression check |
| BUILD-11 | eval-results logging in learn.md | grep | `grep -q 'eval-results.jsonl' D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/learn.md` | Add logging |
| BUILD-12 | evaluate_experiments.py exists | file_exists | `test -f D:/my_ai_projects/kernel-observatory/lib/evaluate_experiments.py` | Create file |
| BUILD-13 | learn event recording in learn.md | grep | `grep -q 'learn-events.jsonl' D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/learn.md` | Add recording |
| BUILD-14 | eval command exists | file_exists | `test -f D:/my_ai_projects/kernel-observatory/commands/kernel/eval.md` | Create file |
| BUILD-15 | rollback command exists | file_exists | `test -f D:/my_ai_projects/kernel-observatory/commands/kernel/rollback.md` | Create file |
| BUILD-16 | Observatory README exists | file_exists | `test -f D:/my_ai_projects/kernel-observatory/README.md` | Create file |
| FUNC-01 | aggregate.py runs | run_code | `python D:/my_ai_projects/kernel-observatory/lib/aggregate.py --help` exits 0 | Fix script |
| FUNC-02 | evaluate_experiments.py runs | run_code | `python D:/my_ai_projects/kernel-observatory/lib/evaluate_experiments.py --help` exits 0 | Fix script |
| FUNC-03 | aggregate.py reads sample metrics | run_code | `python D:/my_ai_projects/kernel-observatory/lib/aggregate.py --file _test/fixtures/DATA-01-input.jsonl` exits 0 | Fix processing |
| TEST-01 | Tier 1 emission produces valid JSONL | run_test | Emission hooks append valid JSON lines | Fix emission |
| TEST-02 | Tier 2 regression gate detects changes | run_test | Baseline → modify → post-check classifies correctly | Fix classification |
| TEST-03 | Tier 3 experiment evaluation works | run_test | evaluate_experiments.py produces verdicts | Fix evaluation |
| TEST-04 | End-to-end pipeline test | run_test | Full learn→emit→aggregate cycle works | Fix integration |

## Requirements Coverage
Each gate maps to task acceptance criteria. All BUILD tasks have structural gates.
All functional deliverables (aggregate.py, evaluate_experiments.py) have run_code gates.
