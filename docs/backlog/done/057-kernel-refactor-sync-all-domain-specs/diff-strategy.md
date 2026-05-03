# Diff Strategy — How to Sync Each Feature Category

## Status
NEW

## Approach

For each repo, run a 3-pass sync:

### Pass 1: Kernel Commands
- Copy all 15 master kernel commands to `.claude/commands/kernel/`
- If the target repo has commands in `.claude/commands/` (flat, not in kernel/ subfolder), move kernel-equivalent commands to `kernel/` and keep domain-specific commands at the top level
- Version comparison: even if a command exists by the same name, replace it with the master version (master is authoritative)

### Pass 2: Kernel Skills
- Copy all 7 master skills to `.claude/skills/`
- If a skill folder already exists (e.g., `autonomous-cycling/`), replace contents with master version
- Domain-specific skills (e.g., `game-engine/`, `healthcare-qa/`) are preserved untouched
- `kernel-domain-setup/` is always replaced (it's kernel infrastructure)

### Pass 3: Hooks
- Copy all 6 master hooks to `.claude/hooks/`
- Rename domain-specific gate enforcers: `[old-name]-gate-enforcer.py` to match the pattern `[domain]-gate-enforcer.py`
- Remove legacy hooks that have no master equivalent (e.g., `code-quality-enforcer.py`, `audit-trail-writer.py`, `qa-gate-enforcer.py`, `playwright-gate-enforcer.py`)
- Or: if legacy hooks serve a real domain purpose, keep them alongside the master hooks

### Post-Sync
- Update CLAUDE.md to list the full command set
- Update `.claude/settings.json` (or `.claude/settings.local.json`) to register new hooks
- Update protocol file to reference new commands/skills
- Copy `run-task.sh` and `lib/common.sh` if not present
- Copy `lib/attestation/intent.py` if not present

## Decision: Replace vs Merge

| Category | Strategy |
|----------|----------|
| Kernel commands | **Replace** — master version always wins |
| Kernel skills | **Replace** — master version always wins |
| Domain commands | **Preserve** — these are domain-specific |
| Domain skills | **Preserve** — these are domain-specific |
| Hooks (kernel) | **Replace** — master version always wins |
| Hooks (domain) | **Evaluate** — keep if serves real purpose, remove if superseded |
| Protocol | **Update** — add references to new commands, don't overwrite domain content |
| CLAUDE.md | **Regenerate** — include full command table + domain-specific additions |
| State files | **Don't touch** — these are runtime state |
