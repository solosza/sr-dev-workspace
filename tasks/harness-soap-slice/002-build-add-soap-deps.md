# Task 002: Add SOAP Dependencies
**Type:** BUILD | **Gates:** SO-02
## Action
ONE action: pip install spyne zeep lxml, and record them in the harness's requirements file (create/append D:/my_ai_projects/project_test_repos/hmsa-qa-platform/harness/requirements.txt or the project's dep manifest with pinned versions). PyPI is reachable (only the Docker registry is blocked).
## Acceptance
`python -c "import spyne, zeep"` succeeds; versions pinned in the manifest.
