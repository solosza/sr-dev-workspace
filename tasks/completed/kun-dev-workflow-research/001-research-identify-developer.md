# Research: Identify the Developer + Confirm the Two Remembered Repos

## Context
Backlog 231. The user knows a developer as "Kun" who publishes his own dev-workflow tools. Fuzzy recall (HYPOTHESES to verify, not facts): a visual editor possibly named "lavish", a git-worktrees tool possibly named "worktree". The handle may only resemble "Kun".

## Type
RESEARCH
## Execution
inline
## Dependencies
- None

## Requirements
- WebSearch angles (run several, don't stop at one): GitHub user search for handles like kun/kunn/kun-*/…; `"lavish" visual editor github`; `git worktree tool github "kun"`; HN/X/blog mentions pairing a "Kun" with worktree tooling or a visual editor; if "lavish" misses, try near-names (lavish/lavash/lav…)
- Deliver into `projects/kun-dev-workflow-tools/notes-identity.md`:
  - Developer identity: handle, profile URL, evidence trail (or candidate list with evidence + picked best match and why)
  - The two repos confirmed: REAL names, repo URLs, purpose, README-level capabilities, stars/last-commit activity, license
  - Every claim cites a URL; log the search queries used
- Do NOT install or execute anything from found repos

## Acceptance Criteria
- [ ] notes-identity.md exists with identity evidence + both repos resolved (or explicit not-found with search trail)

## Gates Satisfied
- RES-01, RES-02 (evidence layer), RES-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
