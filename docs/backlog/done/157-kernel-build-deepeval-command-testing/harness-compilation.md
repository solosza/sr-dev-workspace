# Harness Compilation: Kernel + DeepEval Spec + Domain Setup

## Status
NEW

## Purpose

Define how Step 2 compiles the test repo into a live agent harness. This is not file copy — it's full kernel initialization so the agent running inside has protocol, hooks, and enforcement active.

## What Gets Copied

### From Kernel (golden master or workspace)

```
.claude/
├── commands/kernel/          ← all kernel commands
├── protocols/                ← protocol template or sr_dev protocol
├── hooks/                    ← universal-gate-enforcer.py, domain enforcer, etc.
├── state/                    ← fresh state files (session_state.json, workflow.json)
├── skills/
│   ├── kernel-domain-setup/  ← so domain-setup can run
│   └── autonomous-cycling/   ← for task execution
├── lessons/                  ← lessons.md (RULE ZERO template)
└── settings.local.json       ← hook registrations

run-task.sh                   ← task execution script
CLAUDE.md                     ← kernel CLAUDE.md
```

### From Platform-DeepEval

```
.claude/skills/deepeval-management-layer/
├── SKILL.md
├── workflow.md
├── gate-contract.md
├── steps/
└── references/

framework/
├── interfaces/deepeval_interface.py
├── _reference/
│   ├── metrics/
│   ├── tests/
│   ├── tasks/
│   ├── roles/
│   └── fixtures/
└── resources/
```

## Compilation (Domain Setup)

After copying, run domain-setup inside the test repo:

1. Domain-setup reads the repo structure
2. Discovers platform-deepeval as the domain spec
3. Creates/updates protocol for the test repo
4. Wires hooks in settings.local.json
5. Initializes state files
6. The repo is now a **compiled agent harness** — kernel enforcement is active

This mirrors exactly how any new repo gets set up with the kernel. The test repo is a real, governed environment.

## Why Full Compilation

- Hooks enforce quality gates during test generation
- Protocol governs the eval agent's behavior
- Lessons capture failures during eval runs
- The learn loop works inside the test repo
- Without compilation, it's just files in a folder — no enforcement, no governance

## Dependencies

- Kernel golden master or workspace kernel
- Platform-deepeval at known path
- Domain-setup skill must handle deepeval as a recognized domain spec
