# Gate Contract — 231 "Kun" Dev-Workflow Tools Research

Deliverable: projects/kun-dev-workflow-tools/research-report.md

| Gate | Check | Method |
|------|-------|--------|
| RES-01 | Developer identified with evidence (handle + profile URL), or candidate list with evidence and a picked best match | grep report for "## Developer" section with at least one URL |
| RES-02 | Both remembered repos resolved: real names, purpose, capability summary, stars/activity, license — or explicitly reported not-found with the search trail | grep report for "## Confirmed Repos" section |
| RES-03 | Full repo survey with per-repo usefulness verdict mapped against: kernel loop, execute-pipeline/run-task.sh, worktree isolation (backlog 123), review flow, Claude Code usage | grep report for "## Repo Survey" section |
| RES-04 | Adoption shortlist with concrete integration notes + license check per shortlisted tool | grep report for "## Shortlist" section |
| RES-05 | Notes file at projects/kun-dev-workflow-tools/ contains raw findings (URLs visited, search queries) so conclusions are auditable | file_exists |

## Rules

- Web research only — do NOT install, clone-and-run, or execute code from found repos
- Fuzzy names ("lavish", "worktree") are HYPOTHESES to verify, not facts to assert — report actual names found
- If identity is ambiguous: present candidates with evidence, pick best match, say why — never stall, never silently guess
- Every claim in the report cites a URL
