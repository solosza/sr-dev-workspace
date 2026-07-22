---
name: command-skill-pattern
type: design-document
version: 1.2
date_created: 2026-06-14
date_updated: 2026-06-23
status: canonical-template
purpose: Template for designing command/skill/step/reference/contract/hook systems
---

# Command/Skill/Pattern Design — Index

<!-- INDEX file — points to payloads. Do not duplicate payload content here. -->
<!-- 200-line threshold: split when exceeded. -->

## Overview

Canonical architecture for all commands in the Isagawa kernel. Every new command follows this structure:

```
Command (user entry point)
  |
Skill (orchestrator)
  |-- Step 1 -> References
  |-- Step 2 -> References
  |-- Step N -> References
  +-- Contracts (validation rules)
       |
      Hooks (hard gates)
```

Modular and composable:
- **Outer loop** (standalone command, user-invoked)
- **Inner loop** (called by another skill)
- Scales to any number of steps
- Reusable across domains and projects

---

## Design Documents

| Topic | File | Contents |
|-------|------|----------|
| Architecture Layers | `references/layers.md` | Layer 1-6 definitions, responsibilities, structure templates |
| Contract Schema | `references/contract-schema.md` | JSON schema, dual validation (soft + hard gates), dependencies |
| Design Decisions | `references/design-decisions.md` | 8 baseline decisions from SMART-CONTRACTS-DESIGN.md |
| Completeness Checklist | `references/completeness-checklist.md` | Mandatory sections for design docs before implementation |
| File Structure | `references/file-structure.md` | Canonical tree, state persistence, expandability, examples |

---

## Quick Reference

| Layer | Location | Purpose |
|-------|----------|---------|
| 1. Command | `.claude/commands/kernel/[name].md` | User entry point |
| 2. Skill | `.claude/skills/[name]/SKILL.md` | Orchestrator |
| 3. Steps | `.claude/skills/[name]/steps/` | Per-step procedures |
| 4. References | `.claude/skills/[name]/references/` | Canonical examples |
| 5. Contracts | `.claude/skills/[name]/contracts/` | Validation rules |
| 6. Hooks | `.claude/hooks/[name].py` | Hard gate enforcement |

---

**Version:** 1.2
**Baseline:** SMART-CONTRACTS-DESIGN.md (all 8 decisions finalized)
**Changelog:**
- **v1.2 (2026-06-23):** Restructured to follow tiered-index architecture. Split into index + 5 payloads.
- **v1.1 (2026-06-19):** Added Design Doc Completeness Checklist. Added example instantiations.
- **v1.0 (2026-06-14):** Initial canonical template. 6 layers, 8 design decisions.
