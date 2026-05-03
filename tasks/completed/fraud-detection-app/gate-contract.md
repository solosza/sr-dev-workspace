# Gate Contract — Fraud Detection App

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Repo directory exists | file_exists | `test -d D:/my_ai_projects/fraud-detection-app` | Create dir |
| BUILD-02 | Git initialized | file_exists | `test -d D:/my_ai_projects/fraud-detection-app/.git` | git init |
| BUILD-03 | requirements.txt exists | file_exists | `test -f D:/my_ai_projects/fraud-detection-app/requirements.txt` | Create file |
| BUILD-04 | src/ directory structure | file_exists | `test -d D:/my_ai_projects/fraud-detection-app/src/apis` | Create dirs |
| BUILD-05 | settings.py exists | file_exists | `test -f D:/my_ai_projects/fraud-detection-app/config/settings.py` | Create file |
| BUILD-06 | USASpending API client | file_exists | `test -f D:/my_ai_projects/fraud-detection-app/src/apis/usaspending.py` | Create file |
| BUILD-07 | ProPublica 990 client | file_exists | `test -f D:/my_ai_projects/fraud-detection-app/src/apis/propublica_990.py` | Create file |
| BUILD-08 | SAM.gov client | file_exists | `test -f D:/my_ai_projects/fraud-detection-app/src/apis/sam_gov.py` | Create file |
| BUILD-09 | Fraud patterns JSON | file_exists | `test -f D:/my_ai_projects/fraud-detection-app/src/patterns/fraud_patterns.json` | Create file |
| BUILD-10 | Pattern scanner | file_exists | `test -f D:/my_ai_projects/fraud-detection-app/src/patterns/pattern_scanner.py` | Create file |
| BUILD-11 | Risk scorer | file_exists | `test -f D:/my_ai_projects/fraud-detection-app/src/scoring/risk_scorer.py` | Create file |
| BUILD-12 | Evidence archiver | file_exists | `test -f D:/my_ai_projects/fraud-detection-app/src/evidence/evidence_archiver.py` | Create file |
| BUILD-13 | Package builder | file_exists | `test -f D:/my_ai_projects/fraud-detection-app/src/evidence/package_builder.py` | Create file |
| BUILD-14 | Pipeline runner | file_exists | `test -f D:/my_ai_projects/fraud-detection-app/src/pipeline/pipeline_runner.py` | Create file |
| BUILD-15 | CLAUDE.md for repo | file_exists | `test -f D:/my_ai_projects/fraud-detection-app/CLAUDE.md` | Create file |
| BUILD-16 | run-task.sh copied | file_exists | `test -f D:/my_ai_projects/fraud-detection-app/run-task.sh` | Copy file |
| FUNC-01 | All patterns have required fields | run_code | `python -c "import json; d=json.load(open('src/patterns/fraud_patterns.json')); assert all('id' in p and 'name' in p for p in d)"` | Fix JSON |
| FUNC-02 | Python imports clean | run_code | `cd D:/my_ai_projects/fraud-detection-app && python -c "from src.apis import usaspending; from src.patterns import pattern_scanner; from src.scoring import risk_scorer"` | Fix imports |
| TEST-01 | Pytest passes | run_test | `cd D:/my_ai_projects/fraud-detection-app && python -m pytest tests/ -v` exits 0 | Fix tests |
| DOC-01 | Attorney outreach doc | file_exists | `test -f D:/my_ai_projects/fraud-detection-app/research/attorney-outreach.md` | Create file |
