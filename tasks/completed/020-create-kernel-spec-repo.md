# Create Kernel Spec Repo

## Context
Create the `kernel-spec` repo as a spec-only repo. This is the bootstrap spec — it teaches domain-setup how to build the Isagawa Kernel.

## Dependencies
- **019** — kernel spec design must be complete (file structure defined)

## Phase Gate
- [ ] `research/019-kernel-spec-design.md` exists with file structure

## Requirements

### Create local repo
- Create directory at `D:\my_ai_projects\project_test_repos\specs\kernel-spec`
- `git init`, set branch to `main`

### Create GitHub repo
- Create `isagawa-co/kernel-spec` (private) using `gh repo create`
- Set remote: `git remote add origin git@github.com:isagawa-co/kernel-spec.git`

### Create base files
- `.gitignore` — Python, Node, `.env`, credentials, `__pycache__`, `.venv`
- `LICENSE` — MIT
- `CONTRIBUTING.md` — standard contribution guidelines

### Create directory structure
Use the file structure from 019 design document. At minimum:
```
kernel-spec/
├── .claude/
│   ├── skills/
│   │   └── kernel-build-guidance/
│   │       ├── steps/
│   │       └── checkpoints/
│   ├── commands/
│   └── lessons/
├── reference/
│   ├── commands/
│   ├── hooks/
│   └── skills/
├── .gitignore
├── LICENSE
└── CONTRIBUTING.md
```

### Initial commit and push

## Output
- Local repo at `D:\my_ai_projects\project_test_repos\specs\kernel-spec`
- GitHub repo `isagawa-co/kernel-spec` (private)

## Validation
- [ ] Local directory exists at expected path
- [ ] `git remote -v` shows `isagawa-co/kernel-spec`
- [ ] All directories from the structure exist
- [ ] `.gitignore`, `LICENSE`, `CONTRIBUTING.md` exist
- [ ] Initial commit pushed to GitHub

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
