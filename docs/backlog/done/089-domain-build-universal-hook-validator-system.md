# Build Universal Hook Validator System

**Comparison:** Refactor domain-specific hooks into shared, modular validators. Eliminate duplication across workspaces. Enable adding new workspaces with minimal setup.

**Date:** 2026-05-26

---

## Status
Open

## Priority
High — Reduces hook maintenance burden, enables new workspaces to adopt tested validation patterns immediately

## Summary

Create a shared `lib/validators/` library in isagawa-kernel with modular validators (code quality, state validation, bash validation) that all workspaces import. Replace domain-specific hook implementations with thin orchestrators that call the shared library. Refactor 4 critical workspaces (sr_dev, hmsa-healthcare-qa, game-dev, platform-ssh) to use the shared library and validate all changes via L1/L2/L3 testing. Prove the pattern so new workspaces can adopt in ~30 minutes.

---

## Design Documents

| Document | Purpose |
|----------|---------|
| [[089-domain-build-universal-hook-validator-system/phase-01-shared-lib-structure]] | Create lib/validators/ with 4 modular validators + extensibility pattern |
| [[089-domain-build-universal-hook-validator-system/phase-02-sr-dev-refactor]] | Extract validators from sr_dev-gate-enforcer.py, refactor to use shared lib, L1/L2/L3 test |
| [[089-domain-build-universal-hook-validator-system/phase-03-hmsa-refactor]] | Refactor hmsa-healthcare-qa workspace to use shared lib, validate |
| [[089-domain-build-universal-hook-validator-system/phase-04-gamedev-refactor]] | Refactor game-dev workspace to use shared lib, validate |
| [[089-domain-build-universal-hook-validator-system/phase-05-ssh-refactor]] | Refactor platform-ssh to use shared lib, validate |
| [[089-domain-build-universal-hook-validator-system/phase-06-integration-validation]] | Cross-workspace integration test: all 4 workspaces pass validator suite together |

---

## Architecture

### Shared Library Structure (Single Source of Truth)

```
isagawa-kernel/
├── lib/
│   └── validators/
│       ├── __init__.py
│       ├── code_quality.py         (debug, secrets, wildcards, skipped tests, file size)
│       ├── state_validation.py     (anchor ceremony state checks)
│       ├── bash_validation.py      (cd detection, future bash checks)
│       └── extensibility.md        (how to add new validators)
```

### Workspace Hook Pattern (Thin Orchestrator)

Each workspace has a ~40-line hook that:
1. Imports from shared lib
2. Configures which validators to run (per-domain config)
3. Calls validators and blocks/reports violations

```
[workspace]/.claude/hooks/
├── [domain]-gate-enforcer.py       (thin orchestrator)
└── validators/                     (REMOVED — now at isagawa-kernel/lib/validators/)
```

### Adding a New Workspace (Repeatable)

1. Copy thin orchestrator from existing workspace
2. Update domain name and config
3. Point sys.path to shared lib
4. Point to isagawa-kernel/lib/validators
5. Done (~30 minutes)

---

## Requirements

### Shared Library (Phase 1)
- Must be importable from any workspace via sys.path
- Each validator function has consistent signature: `check(tool_input, domain_config) -> list[violation]`
- Validators are composable (can be used independently)
- Documentation for adding new validators
- No hard-coded workspace names

### Workspace Refactoring (Phases 2-5)
- Extract existing validators from domain-specific hooks
- Replace with thin orchestrator that imports from shared lib
- Preserve all existing validation rules (no behavior changes)
- Test each workspace in isolation before integration test
- Verify hooks still work with Claude Code's PreToolUse invocation

### Integration Validation (Phase 6)
- Run all 4 workspaces through validator suite simultaneously
- Verify no conflicts or cross-workspace interference
- Validate performance (validators should be fast)

---

## Phases Overview

| Phase | Scope | Deliverable | Time |
|-------|-------|-------------|------|
| **0** | GIT | Create feature branch in isagawa-kernel | GIT |
| **1** | CREATE | lib/validators with 4 modules + extensibility guide | BUILD |
| **2** | BUILD + TEST | sr_dev refactored + L1/L2/L3 validated | BUILD + TEST |
| **3** | BUILD + TEST | hmsa-healthcare-qa refactored + validated | BUILD + TEST |
| **4** | BUILD + TEST | game-dev refactored + validated | BUILD + TEST |
| **5** | BUILD + TEST | platform-ssh refactored + validated | BUILD + TEST |
| **6** | TEST | Cross-workspace integration test | TEST |
| **7** | GIT | Merge feature branch to origin/main (after all tests pass) | GIT |

---

## Workspaces in Scope

| Workspace | Path | Domain | Current Hooks | Status |
|-----------|------|--------|----------------|--------|
| **sr_dev** | `sr_dev_workspace/` | sr_dev | sr_dev-gate-enforcer.py | Active |
| **hmsa-healthcare-qa** | `project_test_repos/hmsa-healthcare-qa/` | healthcare-qa | ? (to be discovered) | Active |
| **game-dev** | `project_test_repos/game-dev/` | game-dev | ? (to be discovered) | Active |
| **platform-ssh** | `project_test_repos/isagawa-qa/platform-ssh/` | ssh | ssh-gate-enforcer.py | Active |

---

## Testing Strategy (L1/L2/L3)

### Level 1: Does it exist?
- Shared lib modules exist and are importable
- Thin orchestrator files created in each workspace
- No import errors

### Level 2: Does it run?
- Invoke hook with sample input (valid code)
- Verify hook exits with code 0 (pass)
- Verify no runtime errors or exceptions

### Level 3: Does it catch violations?
- Feed known-bad code to each validator type
- Verify hook blocks (exit code 2)
- Verify error message is helpful
- Verify across all 4 workspaces simultaneously

---

## References

- Current sr_dev-gate-enforcer.py: `.claude/hooks/sr_dev-gate-enforcer.py`
- SOLID principles: Single Responsibility, Open/Closed (for extensibility)
- Backlog 085-086: SSH compliance research (will benefit from modular validators)
- Lesson 28: cd in bash recurrence (validator future enhancement)

---

## Task Builder Input

- **Deliverable:** Universal hook validator library + refactored hooks for 4 workspaces
- **Location:** `isagawa-kernel/lib/validators/` (shared) + workspace `.claude/hooks/` (thin orchestrators)
- **Scope:** BUILD (Phase 1) + REFACTOR (Phases 2-5) + TEST (Phase 6)
- **Constraints:**
  - No behavior changes (preserve all existing validation rules)
  - Hooks must remain compatible with Claude Code PreToolUse invocation
  - Modular design: new validators can be added without modifying core hook
  - Each phase must pass L1/L2/L3 before proceeding to next
  - Phase 1 must complete before Phases 2-5 can start (dependency)

---

## Future Extensions (After This Backlog)

These are intentionally OUT OF SCOPE but the design enables them:

- **More workspaces**: platform-selenium, platform-playwright, isagawa-kernel — repeat phase pattern
- **New validators**: git (force push detection), test-specific (test isolation), performance (timeout detection)
- **Validator configuration**: YAML per-workspace to enable/disable validators
- **Validator versioning**: Track validator changes, support multiple versions
- **Shared validator registry**: Central catalog of available validators per domain type

