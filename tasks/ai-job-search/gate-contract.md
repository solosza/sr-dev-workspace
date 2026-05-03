# Gate Contract — AI Job Search

## Verification Methods
-> `.claude/skills/task-builder/references/verification-methods.md`

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Resume profile JSON exists | file_exists | `test -f tasks/ai-job-search/output/resume-profile.json` | Create file |
| BUILD-02 | Resume profile has skills array | grep | `grep -q '"skills"' tasks/ai-job-search/output/resume-profile.json` | Add field |
| BUILD-03 | Resume profile has target_roles array | grep | `grep -q '"target_roles"' tasks/ai-job-search/output/resume-profile.json` | Add field |
| BUILD-04 | Anthropic raw results exist | file_exists | `test -f tasks/ai-job-search/output/raw-results/anthropic.json` | Run search |
| BUILD-05 | OpenAI raw results exist | file_exists | `test -f tasks/ai-job-search/output/raw-results/openai.json` | Run search |
| BUILD-06 | Google DeepMind raw results exist | file_exists | `test -f tasks/ai-job-search/output/raw-results/google-deepmind.json` | Run search |
| BUILD-07 | Meta AI raw results exist | file_exists | `test -f tasks/ai-job-search/output/raw-results/meta-ai.json` | Run search |
| BUILD-08 | xAI raw results exist | file_exists | `test -f tasks/ai-job-search/output/raw-results/xai.json` | Run search |
| BUILD-09 | Cohere raw results exist | file_exists | `test -f tasks/ai-job-search/output/raw-results/cohere.json` | Run search |
| BUILD-10 | Mistral raw results exist | file_exists | `test -f tasks/ai-job-search/output/raw-results/mistral.json` | Run search |
| BUILD-11 | Databricks raw results exist | file_exists | `test -f tasks/ai-job-search/output/raw-results/databricks.json` | Run search |
| BUILD-12 | Scale AI raw results exist | file_exists | `test -f tasks/ai-job-search/output/raw-results/scale-ai.json` | Run search |
| BUILD-13 | Hugging Face raw results exist | file_exists | `test -f tasks/ai-job-search/output/raw-results/hugging-face.json` | Run search |
| BUILD-14 | Compiled results JSON exists | file_exists | `test -f tasks/ai-job-search/output/compiled-results.json` | Compile results |
| BUILD-15 | Final output JSON exists | file_exists | `test -f tasks/ai-job-search/output/job-search-results.json` | Write output |
| FUNC-01 | Final output is valid JSON | run_code | `python -c "import json; json.load(open('tasks/ai-job-search/output/job-search-results.json'))"` exits 0 | Fix JSON |
| FUNC-02 | Each job has required fields | run_code | `python -c "import json; data=json.load(open('tasks/ai-job-search/output/job-search-results.json')); assert all(all(k in j for k in ['url','company','title','location','remote','match_score']) for j in data['jobs'])"` exits 0 | Add missing fields |
| FUNC-03 | Match scores are numeric 0-100 | run_code | `python -c "import json; data=json.load(open('tasks/ai-job-search/output/job-search-results.json')); assert all(0<=j['match_score']<=100 for j in data['jobs'])"` exits 0 | Fix scores |

## Requirements Coverage
Each gate maps to task acceptance criteria. All tasks have at least one corresponding gate.
