# Create Repo and Scaffolding

## Context
Create the `creative-finance-spec` repo as a spec-only repo under `specs/`. Follows the same pattern as `docker-spec`. The directory structure must accommodate all downstream tasks (006-016).

## Dependencies
- **001-004** — research must be complete so the agent understands full scope of what directories are needed

## Phase Gate
Before starting this task, verify:
- [ ] `research/001-lease-option-structure.md` exists and has content
- [ ] `research/002-buyer-types-matching.md` exists and has content
- [ ] `research/003-communication-patterns.md` exists and has content
- [ ] `research/004-integration-surface.md` exists and has content

If any research file is missing or empty, STOP and complete that task first.

## Requirements
- Create local directory at `D:\my_ai_projects\project_test_repos\specs\creative-finance-spec`
- `git init`, set branch to `main`
- Create GitHub repo `isagawa-co/creative-finance-spec` (private)
- Set remote: `git remote add origin git@github.com:isagawa-co/creative-finance-spec.git`
- Create base files:
  - `.gitignore` — Python, Node, `.env`, credentials, `__pycache__`, `.venv`
  - `requirements.txt` — minimal (no deps yet, placeholder)
  - `LICENSE` — MIT
  - `CONTRIBUTING.md` — standard contribution guidelines
- Create directory structure:
  ```
  creative-finance-spec/
  ├── research/                  ← copy research from sr_dev_test
  ├── pipeline/
  │   ├── interfaces/            ← schemas, gmail patterns, webhook schemas
  │   ├── seller/                ← qualification, scoring, outreach, follow-up
  │   ├── buyer/                 ← list management, matching, disposition, education
  │   ├── matching/              ← engine, ranking, outreach rules, response handling
  │   ├── config/                ← client config schema, sample, CSV template
  │   └── integration/           ← webhook receiver, gws CLI patterns
  ├── .claude/
  │   ├── skills/
  │   │   └── lease-option-pipeline/
  │   │       ├── steps/
  │   │       └── checkpoints/
  │   ├── commands/
  │   └── lessons/
  │       ├── lease-options/
  │       ├── communication/
  │       ├── integration/
  │       └── pipeline/
  ├── .gitignore
  ├── requirements.txt
  ├── LICENSE
  └── CONTRIBUTING.md
  ```
- Copy research files from `sr_dev_test/research/` into `creative-finance-spec/research/`
- Initial commit and push

## Output
- Local repo at `D:\my_ai_projects\project_test_repos\specs\creative-finance-spec`
- GitHub repo `isagawa-co/creative-finance-spec` (private)

## Validation (check ALL before completing)
- [ ] Local directory exists at expected path
- [ ] `git remote -v` shows `isagawa-co/creative-finance-spec`
- [ ] All directories from the structure above exist (use Glob to verify)
- [ ] `.gitignore`, `requirements.txt`, `LICENSE`, `CONTRIBUTING.md` exist
- [ ] All 4 research files copied into `creative-finance-spec/research/`
- [ ] Initial commit pushed to GitHub (verify with `git log --oneline -1`)

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
