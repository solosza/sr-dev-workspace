# Gate Contract

| Gate ID | Task | Method | Check | Expected |
|---------|------|--------|-------|----------|
| BUILD-01 | 001 | file_exists | `framework/golden_dataset_translator.py` | exists |
| BUILD-02 | 002 | file_exists | `framework/agent_output_capture.py` | exists |
| BUILD-03 | 003 | file_exists | `framework/metric_mapping.py` | exists |
| BUILD-04 | 004 | file_exists | `framework/iteration_tracking.py` | exists |
| BUILD-05 | 005 | file_exists | `.claude/skills/prod-test/references/l3-deepeval-composition.md` | exists |
| BUILD-06 | 006 | grep | `grep -l "L3\|deepeval" .claude/skills/prod-test/references/step-06-inner-tasks.md` | match |
| TEST-07 | 007 | run_code | `python -c "import ast; ast.parse(open('framework/golden_dataset_translator.py').read()); print('OK')"` | exit 0 |
| TEST-08 | 008 | file_exists | `eval/results/score-history.json` OR test verification output | exists |
