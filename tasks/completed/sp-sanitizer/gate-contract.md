# Gate Contract — SP Sanitizer Pipeline

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Repo exists on GitHub | run_code | `gh repo view solosza/sp-sanitizer` exits 0 | Create repo |
| BUILD-02 | Package dir exists | file_exists | `test -d D:/my_ai_projects/sp-sanitizer/sp_sanitizer` | Create dir |
| BUILD-03 | pyproject.toml exists | file_exists | `test -f D:/my_ai_projects/sp-sanitizer/pyproject.toml` | Create file |
| BUILD-04 | tsql_keywords.py exists | file_exists | `test -f D:/my_ai_projects/sp-sanitizer/sp_sanitizer/tsql_keywords.py` | Create file |
| BUILD-05 | contracts.py exists | file_exists | `test -f D:/my_ai_projects/sp-sanitizer/sp_sanitizer/contracts.py` | Create file |
| BUILD-06 | Sample fixture exists | file_exists | `test -f D:/my_ai_projects/sp-sanitizer/tests/fixtures/sample_sp.sql` | Create file |
| BUILD-07 | extract.py exists | file_exists | `test -f D:/my_ai_projects/sp-sanitizer/sp_sanitizer/extract.py` | Create file |
| BUILD-08 | catalog_replace.py exists | file_exists | `test -f D:/my_ai_projects/sp-sanitizer/sp_sanitizer/catalog_replace.py` | Create file |
| BUILD-09 | leak_detector.py exists | file_exists | `test -f D:/my_ai_projects/sp-sanitizer/sp_sanitizer/leak_detector.py` | Create file |
| BUILD-10 | refine.py exists | file_exists | `test -f D:/my_ai_projects/sp-sanitizer/sp_sanitizer/refine.py` | Create file |
| BUILD-11 | reverse.py exists | file_exists | `test -f D:/my_ai_projects/sp-sanitizer/sp_sanitizer/reverse.py` | Create file |
| BUILD-12 | runner.py exists | file_exists | `test -f D:/my_ai_projects/sp-sanitizer/sp_sanitizer/runner.py` | Create file |
| BUILD-13 | .gitignore has mapping pattern | grep | `grep -q 'mapping.json' D:/my_ai_projects/sp-sanitizer/.gitignore` | Add pattern |
| FUNC-01 | extract imports clean | run_code | `cd D:/my_ai_projects/sp-sanitizer && python -c "from sp_sanitizer.extract import extract_identifiers"` exits 0 | Fix imports |
| FUNC-02 | replace imports clean | run_code | `cd D:/my_ai_projects/sp-sanitizer && python -c "from sp_sanitizer.catalog_replace import replace_identifiers"` exits 0 | Fix imports |
| FUNC-03 | leak_detector imports clean | run_code | `cd D:/my_ai_projects/sp-sanitizer && python -c "from sp_sanitizer.leak_detector import detect_leaks"` exits 0 | Fix imports |
| FUNC-04 | refine imports clean | run_code | `cd D:/my_ai_projects/sp-sanitizer && python -c "from sp_sanitizer.refine import refine_replacements"` exits 0 | Fix imports |
| FUNC-05 | reverse imports clean | run_code | `cd D:/my_ai_projects/sp-sanitizer && python -c "from sp_sanitizer.reverse import reverse_sanitization"` exits 0 | Fix imports |
| FUNC-06 | runner imports clean | run_code | `cd D:/my_ai_projects/sp-sanitizer && python -c "from sp_sanitizer.runner import run_pipeline"` exits 0 | Fix imports |
| FUNC-07 | contracts validate | run_code | `cd D:/my_ai_projects/sp-sanitizer && python -c "from sp_sanitizer.contracts import *"` exits 0 | Fix models |
| FUNC-08 | keywords loadable + 200+ | run_code | `cd D:/my_ai_projects/sp-sanitizer && python -c "from sp_sanitizer.tsql_keywords import TSQL_KEYWORDS; assert len(TSQL_KEYWORDS) > 200"` exits 0 | Add keywords |
| TEST-01 | extract unit tests pass | run_test | `cd D:/my_ai_projects/sp-sanitizer && python -m pytest tests/test_extract.py -v` exits 0 | Fix tests |
| TEST-02 | replace unit tests pass | run_test | `cd D:/my_ai_projects/sp-sanitizer && python -m pytest tests/test_catalog_replace.py -v` exits 0 | Fix tests |
| TEST-03 | leak detector tests pass | run_test | `cd D:/my_ai_projects/sp-sanitizer && python -m pytest tests/test_leak_detector.py -v` exits 0 | Fix tests |
| TEST-04 | refine tests pass | run_test | `cd D:/my_ai_projects/sp-sanitizer && python -m pytest tests/test_refine.py -v` exits 0 | Fix tests |
| TEST-05 | reverse tests pass | run_test | `cd D:/my_ai_projects/sp-sanitizer && python -m pytest tests/test_reverse.py -v` exits 0 | Fix tests |
| TEST-06 | integration tests pass | run_test | `cd D:/my_ai_projects/sp-sanitizer && python -m pytest tests/test_integration.py -v` exits 0 | Fix tests |
| TEST-07 | L3 CLI end-to-end | run_code | `cd D:/my_ai_projects/sp-sanitizer && python -m sp_sanitizer.runner tests/fixtures/sample_sp.sql --output-dir output/` exits 0 + leak report CLEAN | Fix pipeline |
