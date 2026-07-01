# Extension List — Isagawa Kernel

Files in `isagawa-kernel` that are NOT in `kernel-manifest.json` core.

## Core (in manifest — DO NOT move)

| Category | Files |
|----------|-------|
| Commands | `session-start.md`, `anchor.md`, `learn.md`, `complete.md`, `fix.md`, `domain-setup.md` |
| Hooks | `universal-gate-enforcer.py`, `actions-log-appender.py`, `test-failure-detector.py`, `auto-approve-claude-writes.py` |
| Skills | `kernel-domain-setup/`, `autonomous-cycling/` |
| Scripts | `lib/common.sh` |
| Config | `CLAUDE.md`, `.claude/settings.local.json` |
| Lessons | `.claude/lessons/lessons.md` (index only) |

## Extensions (NOT in manifest)

### Commands

| Extension | Type | Current Location | Recommendation |
|-----------|------|-----------------|----------------|
| audit-workflow | Command | `.claude/commands/kernel/audit-workflow.md` | Remove from kernel repo |
| autonomous-cycle | Command | `.claude/commands/kernel/autonomous-cycle.md` | Remove from kernel repo |
| backlog | Command | `.claude/commands/kernel/backlog.md` | Remove from kernel repo |
| task-builder | Command | `.claude/commands/kernel/task-builder.md` | Remove from kernel repo |

### Skills

| Extension | Type | Current Location | Recommendation |
|-----------|------|-----------------|----------------|
| audit-workflow | Skill | `.claude/skills/audit-workflow/` (9 files) | Remove from kernel repo |
| task-builder | Skill | `.claude/skills/task-builder/` (13 files) | Remove from kernel repo |

### Libraries

| Extension | Type | Current Location | Recommendation |
|-----------|------|-----------------|----------------|
| attestation | Lib (6 modules) | `lib/attestation/` | Remove from kernel repo |
| validators | Lib (4 modules + doc) | `lib/validators/` | Remove from kernel repo |
| skill_extraction | Lib (1 module) | `lib/skill_extraction.py` | Remove from kernel repo |
| lib/__init__.py | Package init | `lib/__init__.py` | Remove from kernel repo (core only needs `lib/common.sh`) |

### Lesson Topic Files

| Extension | Type | Current Location | Recommendation |
|-----------|------|-----------------|----------------|
| 16 topic files | Lesson details | `.claude/lessons/*.md` (excluding `lessons.md` index) | Keep in kernel repo |

Rationale: Lesson topic files are workspace-specific — they accumulate through `/kernel/learn` and are referenced by the `lessons.md` index. They are an output of the kernel governance loop, not an extension. However, they are NOT in the manifest because they are generated per-workspace, not distributed as kernel core. They should stay in the repo but remain unlisted in the manifest (they're dynamic content, not distributable core).

### Infrastructure / Meta

| File | Type | Recommendation |
|------|------|----------------|
| `kernel-manifest.json` | Meta | Keep — defines the kernel boundary |
| `kernel-sync.sh` | Script | Keep — sync tool for the manifest |
| `.gitignore` | Config | Keep — repo hygiene |
| `CONTRIBUTING.md` | Doc | Keep — open-source standard |
| `LICENSE` | Doc | Keep — MIT license |
| `README.md` | Doc | Keep — repo docs |

### Stale / Orphaned

| File | Type | Recommendation |
|------|------|----------------|
| `delegation/__pycache__/` | Cache (no source files) | Delete — orphaned cache from removed module |
| `lessons/__pycache__/` | Cache (no source files) | Delete — orphaned cache from removed module |
| `scanner/__pycache__/` | Cache (no source files) | Delete — orphaned cache from removed module |
| `tests/test_decay/__pycache__/` | Cache (no source files) | Delete — orphaned test cache |
| `tests/test_delegation/__pycache__/` | Cache (no source files) | Delete — orphaned test cache |
| `tests/test_extraction/__pycache__/` | Cache (no source files) | Delete — orphaned test cache |
| `tests/test_recurrence/__pycache__/` | Cache (no source files) | Delete — orphaned test cache |
| `tests/test_scanner/__pycache__/` | Cache (no source files) | Delete — orphaned test cache |
| `tests/test_skill_extraction.py` | Test | Remove from kernel repo (follows `lib/skill_extraction.py`) |
| `backlog/one-shot-task-execution.md` | Doc | Remove from kernel repo — backlog items belong in workspace |
| `docs/research/zep-cloud-memory-analysis.md` | Research | Remove from kernel repo — research belongs in workspace |
| `.pytest_cache/` | Cache | Delete — not source code |

## Option Recommendation: Option B (Workspace-Local)

**Recommended: Option B** — extensions stay workspace-local.

### Rationale

1. **Simplest path.** No new repo to create/maintain (Option A adds sync complexity). No ambiguity about what the kernel repo contains (Option C still bundles everything).

2. **Matches how extensions are used.** Extensions like `task-builder`, `audit-workflow`, `attestation`, and `prod-test` are already workspace-specific — they're installed by copying into a workspace during `/kernel/domain-setup` or added manually. The kernel-sync.sh script already handles distributing core files.

3. **Extensions are sr_dev-workspace tools.** The attestation library, validator framework, task-builder, and audit-workflow are tools built in and for the sr_dev workspace. Other workspaces (QA platform, job-application-spec) don't need all of them — they pick what they need.

4. **Clean kernel boundary.** The kernel repo becomes truly minimal: 6 commands, 4 hooks, 2 skills, 1 script, config, and lessons index. Everything else lives where it was built and is manually installed when needed.

5. **Future extensibility.** If sharing extensions between workspaces becomes a real need (not hypothetical), Option A (extensions repo) can be added later. Option B doesn't preclude it.

### What changes

- Remove from `isagawa-kernel`: 4 extension commands, 2 extension skills, 3 lib packages, 1 test file, stale backlog/research docs
- Delete orphaned `__pycache__` directories
- Keep in `isagawa-kernel`: manifest, sync script, repo meta (README, LICENSE, CONTRIBUTING, .gitignore), lesson topic files
- Extensions continue to live in `sr_dev_workspace` (where they already exist as the working copies)
