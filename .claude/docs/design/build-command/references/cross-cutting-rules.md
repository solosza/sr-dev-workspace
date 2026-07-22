# Cross-Cutting Rules

**Purpose:** Rules that apply to every step in the `/build-command` workflow. Read once before starting, apply throughout.

---

## No-Code Rule

This workflow is prose-driven. The agent reads design docs, extracts specifications, and generates files by writing — not by running code. No Python scaffolding scripts, no template engines, no code generation tools.

- **Read the design doc, write the files.** The agent reads each section of the design doc and writes the corresponding skill file directly.
- **The only exception is JSON contracts.** Contract files are JSON — the agent writes valid JSON by hand (or validates structure with a quick Python check if needed).
- **Why:** The agent understands the command-skill-pattern better than any script could. Scaffolding is translation, not computation.

---

## Name Extraction

The command name is the design doc's parent folder name. For path `.claude/docs/design/validate-tc/index.md`, extract `validate-tc`. This name drives all output paths.

---

## Existing Files (Rebuild)

Before Step 2, check if `.claude/skills/[name]/` exists.
- If yes → warn: "Skill package exists. Rebuild will overwrite all generated files."
- User confirms: `proceed` (overwrite) or `stop` (abort).
- Rebuild is a full regeneration — no merge, no diff. Design doc is always authoritative.

---

## Failure Recovery

Every step writes state before and after file creation:
- **Before:** set `current_step` in state file
- **After:** append to `steps_complete` and `files_written`
- **On failure:** state file shows which step failed and which files were written
- **Resume:** re-run same command. Agent reads state, skips completed steps, retries failed step.
- **Partial step failure** (e.g., 3 of 5 step files written): agent re-generates ALL files for that step (idempotent overwrite), not just missing ones.

---

## 200-Line Threshold

After writing any file, check line count. If > 200 lines:
- Extract the largest section into a sub-file
- Replace with a wikilink in the parent file
- This applies to SKILL.md, workflow.md, step files — everything.

---

## Design Doc References → Skill References

The design doc's `references/` folder is the source of truth. The skill's `references/INDEX.md` links back to design doc references via wikilinks — no content duplication.

```
Design doc:  .claude/docs/design/[name]/references/workflow.md  ← SOURCE
Skill ref:   .claude/skills/[name]/references/INDEX.md          ← LINKS TO SOURCE
```

If the design doc has canonical examples that the skill needs at runtime, the skill's INDEX.md points to them. The skill never copies design doc content into its own references.

---

## HITL in All Modes

HITL checkpoints (Step 1 and Step 2) fire in both outer loop (standalone) and inner loop (called by execute-pipeline) modes. The design doc is the corpus — the user must confirm the corpus is complete and the foundation is correct before generation proceeds. There is no autonomous bypass.
