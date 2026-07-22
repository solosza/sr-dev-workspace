# Research: "Kun"'s Dev-Workflow Repos (visual editor + git worktrees + more)

## Status
Open

## Priority
Medium — workflow tooling that could feed the kernel/pipeline workflow directly

## Summary
A developer the user knows of as "Kun" publishes tools he uses for his own dev workflow. The user recalls two by fuzzy name: a visual editor possibly called "lavish" and a git-worktrees tool possibly called "worktree." Find the actual person/handle and repos, confirm the real names, then survey his other published apps for anything useful to this workspace's workflow (kernel loop, parallel pipelines, worktree isolation, review flow).

## Requirements
- Identify the developer (handle likely resembles "Kun" — search GitHub users/orgs, blog posts, HN/X mentions; the fuzzy names "lavish" (visual editor) and "worktree" (git worktrees tool) are the strongest search keys)
- Confirm the two remembered repos: real names, purpose, README-level capability summary, stars/activity/maintenance state, license
- Enumerate his OTHER public repos/apps; for each: one-paragraph what-it-does + a "useful for my workflow?" verdict (map against: kernel loop, execute-pipeline/run-task.sh, git worktree isolation (backlog 123 research), code review flow, Claude Code usage)
- Recommend a shortlist: which tools to adopt/trial, with concrete integration notes (install, where it plugs into the workflow)
- If "Kun" is ambiguous (multiple candidate developers), present the candidates with evidence and pick the best match — don't stall

## References
- docs/backlog/done/123-kernel-research-worktree-pipeline-isolation.md (worktree isolation research — related)
- User's fuzzy recall: visual editor "lavish"(?), worktrees tool "worktree"(?)

## Task Builder Input
- **Deliverable:** Research report at projects/kun-dev-workflow-tools/research-report.md — developer identified, both remembered repos confirmed with real names + capabilities, full repo survey with usefulness verdicts, adoption shortlist with integration notes
- **Location:** subproject:kun-dev-workflow-tools
- **Scope:** RESEARCH
- **Constraints:** Web research only (GitHub, blogs, HN/X) — no installs, no code execution from found repos during research. License check for anything shortlisted. If the developer can't be conclusively identified, report best candidates with evidence rather than guessing silently.
