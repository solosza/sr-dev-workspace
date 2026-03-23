# Create Meta-Spec Repo

## Context
Create the meta-spec repo that houses the spec factory — a domain spec that teaches the agent how to build other domain specs autonomously.

## Dependencies
- **030** — meta-spec schema and scoring model designed

## Phase Gate
- [ ] `research/030-meta-spec-scoring-model.md` exists with scoring model and factory loop design

## Requirements

### Create local repo
- Location: `D:\my_ai_projects\project_test_repos\specs\meta-spec`
- `git init`
- Create `.gitignore` (Python-standard + `.claude/state/`)
- Create `requirements.txt` (minimal — no heavy dependencies)
- Create `LICENSE` (MIT)
- Create `CONTRIBUTING.md`

### Create GitHub repo
- Org: `isagawa-co`
- Name: `meta-spec`
- Visibility: **private**
- Command: `gh repo create isagawa-co/meta-spec --private`
- Add remote: `git remote add origin https://github.com/isagawa-co/meta-spec.git`

### Create directory structure
```
meta-spec/
├── .claude/
│   ├── commands/
│   ├── lessons/
│   └── skills/
│       └── spec-factory/
├── templates/
│   ├── skill/
│   ├── commands/
│   ├── lessons/
│   └── framework/
├── scoring/
├── research/
├── output/
└── tests/
```

### Initial commit
- Commit message: `init: meta-spec repo scaffolding`
- Push to `isagawa-co/meta-spec`

## Output
- Local repo at `D:\my_ai_projects\project_test_repos\specs\meta-spec`
- GitHub repo at `isagawa-co/meta-spec` (private)
- Directory structure ready for spec factory files

## Validation
- [ ] Local repo exists with git initialized
- [ ] GitHub repo exists (private)
- [ ] Remote connected
- [ ] Directory structure matches plan
- [ ] Initial commit pushed

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
