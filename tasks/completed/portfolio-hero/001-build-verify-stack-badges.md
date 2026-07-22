# Task 001: Verify Stack Badge List

**Type:** BUILD | **Gates:** PH-01

## Action
ONE verification script producing the evidence-backed badge list. For each candidate tool (Python, TypeScript, Selenium, Playwright, Docker, Paramiko, pyodbc, mssql-python, Claude Code): grep the real repos (D:/my_ai_projects/portfolio-site excluded): D:/my_ai_projects/project_test_repos/hmsa-qa-platform, D:/my_ai_projects/project_test_repos/isagawa-qa-platform, D:/my_ai_projects/isagawa-kernel, D:/my_ai_projects/project_test_repos/sr_dev_workspace. Write the verified list + one evidence path per tool to D:/my_ai_projects/portfolio-site/assets/badge-evidence.json (repo-internal note, not rendered).

## Acceptance
badge-evidence.json exists; every listed tool has a real evidence path; unverified tools excluded.
