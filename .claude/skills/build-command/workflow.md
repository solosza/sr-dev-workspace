# Workflow

## Phases

### Phase 1: Validate Input
- Steps: 1
- Gate: Design doc passes completeness checklist (7/7 required sections present)
- HITL: **FULL STOP** — user reviews completeness report before proceeding

### Phase 2: Generate Foundation
- Steps: 2
- Gate: SKILL.md written and approved by user
- HITL: **CHECKPOINT** — user approves SKILL.md content before downstream generation

### Phase 3: Generate Layers
- Steps: 3, 4, 5, 6, 7
- Gate: All layer files written (workflow.md, gate-contract.md, step files, INDEX.md, contracts, command entry point)
- HITL: None — mechanical generation proceeds autonomously

### Phase 4: Verify
- Steps: 8
- Gate: All files pass command-skill-pattern checks and 200-line threshold
- HITL: Final report to user

## State Persistence

**Location:** `.claude/state/build-command-state.json`

```json
{
  "command_name": "[name]",
  "design_doc_path": "[path]",
  "current_step": 0,
  "steps_complete": [],
  "files_written": [],
  "last_updated": null
}
```

**Resume:** If interrupted, re-run `/build-command [same-path]`. Agent reads state, skips completed steps, continues from `current_step`. Files already written are overwritten (idempotent).

**Cleanup:** State file is deleted after Step 8 (Verify Build) passes.

## HITL Stops

| After Step | Why | User Options |
|-----------|-----|-------------|
| 1 | Design doc completeness — user must confirm corpus is valid | `proceed` / `update` / `stop` |
| 2 | SKILL.md foundation — identity, philosophy, rules must be correct | `approve` / `modify` / `stop` |

## Cross-Cutting Rules

> `.claude/docs/design/build-command/references/cross-cutting-rules.md`

Key rules applied throughout:
- **No-code rule** — prose-driven, no scaffolding scripts
- **Name extraction** — command name = design doc parent folder name
- **Rebuild** — full overwrite, no merge
- **200-line threshold** — extract to sub-files if exceeded
- **Design doc references → skill references** — link, don't copy
