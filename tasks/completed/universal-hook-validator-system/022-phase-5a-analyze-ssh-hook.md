# Task 022: Phase 5a - Analyze platform-ssh Hook

**Type:** BUILD (analysis) | **Dependencies:** 008 | **Status:** DONE

Review current ssh-gate-enforcer.py to identify shared vs SSH-specific validators.

**Location:** `D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh\.claude\hooks\ssh-gate-enforcer.py`

## Analysis Results

### Current State

1. **platform-ssh (base repo):** Has NO `.claude/hooks/` directory, NO `settings.local.json`, NO domain gate enforcer
2. **platform-ssh-master (prod-test assembled):** Has hooks copied from sr_dev workspace:
   - `universal-gate-enforcer.py` (shared kernel hook)
   - `sr_dev-gate-enforcer.py` (wrong domain — sr_dev, not ssh)
   - `actions-log-appender.py`, `auto-approve-claude-writes.py`, `test-failure-detector.py`
   - `agent-inline-execution-blocker.py`
3. **No ssh-gate-enforcer.py exists anywhere** — the task reference is aspirational
4. **platform-ssh has its own validators** at `framework/_reference/validators/` but these are domain-specific (config_validator, kernel_validator, package_validator, service_validator) for SSH compliance testing — NOT code-quality gate enforcement

### What Needs to Happen (Phase 5b)

Create `ssh-gate-enforcer.py` as a thin orchestrator (same pattern as game-dev/hmsa):
- Import shared validators from `isagawa-kernel/lib/validators/`
- Wire in `platform-ssh/.claude/settings.local.json`
- The framework validators stay where they are — they serve a different purpose

### Files Examined

- `isagawa-qa/platform-ssh/.claude/` — commands, skills, state (no hooks)
- `isagawa-qa/platform-ssh-master/.claude/hooks/` — 6 files (all copied from sr_dev)
- `isagawa-qa/platform-ssh-master/.claude/settings.local.json` — wires universal-gate-enforcer only (no domain enforcer)
- `isagawa-qa/platform-ssh/framework/_reference/validators/` — 4 domain-specific validators (not gate enforcement)
