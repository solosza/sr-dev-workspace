# Gate Contract — Tiered Index Threshold Research

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Project dir exists | file_exists | `test -d projects/tiered-index-threshold-research/` | Create dir |
| BUILD-02 | Experiment dir exists | file_exists | `test -d D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/` | Create dir |
| BUILD-03 | Flat corpus exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/corpus-flat.md` | Build corpus |
| BUILD-04 | Tiered corpus exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/corpus-tiered.md` | Build corpus |
| BUILD-05 | Flat corpus ≥ 60K tokens | run_code | `python -c "c=open('D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/corpus-flat.md').read(); assert len(c)//4 >= 60000, f'Only {len(c)//4} tokens'"` | Add more skills |
| BUILD-06 | Sequential task prompt exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/task-sequential.md` | Write prompt |
| BUILD-07 | Precision task prompt exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/task-precision.md` | Write prompt |
| BUILD-08 | Cross-ref task prompt exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/task-crossref.md` | Write prompt |
| BUILD-09 | Experiment config exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/experiment-config.json` | Write config |
| BUILD-10 | All 6 prompt files exist | run_code | `python -c "import os; d='D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k'; files=['prompt-flat-sequential.md','prompt-tiered-sequential.md','prompt-flat-precision.md','prompt-tiered-precision.md','prompt-flat-crossref.md','prompt-tiered-crossref.md']; missing=[f for f in files if not os.path.exists(os.path.join(d,f))]; assert not missing, f'Missing: {missing}'"` | Build prompts |
| FUNC-01 | Sequential outputs exist (10 files) | run_code | `python -c "import glob; files=glob.glob('D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/sequential-*.txt'); assert len(files)>=10, f'Only {len(files)} files'"` | Rerun |
| FUNC-02 | Precision outputs exist (10 files) | run_code | `python -c "import glob; files=glob.glob('D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/precision-*.txt'); assert len(files)>=10, f'Only {len(files)} files'"` | Rerun |
| FUNC-03 | Cross-ref outputs exist (10 files) | run_code | `python -c "import glob; files=glob.glob('D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/crossref-*.txt'); assert len(files)>=10, f'Only {len(files)} files'"` | Rerun |
| FUNC-04 | Scores JSON exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/scores.json` | Rescore |
| BUILD-11 | Statistical report exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/statistical-report.md` | Generate |
| BUILD-12 | Baseline comparison exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/baseline-comparison.md` | Generate |
| BUILD-13 | Final report exists | file_exists | `test -f projects/tiered-index-threshold-research/final-report.md` | Write report |
