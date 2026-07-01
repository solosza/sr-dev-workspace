# Dependency Resolution — Step 3 Reference

How to scan a target artifact's files and resolve all external references so the artifact is fully self-contained in the test repo.

---

## Scan Order

Scan the artifact in this exact sequence:

| Order | What to Scan | What to Extract |
|-------|-------------|-----------------|
| 1 | SKILL.md File Index | Every file path listed in the index table |
| 2 | Each step file's References section | External paths, wikilinks, file references |
| 3 | Contract JSONs | Referenced schemas, data files, external paths |
| 4 | Design docs | Any external paths referenced by the artifact |

**Rule:** Complete each scan level before moving to the next. A reference found at level 2 may itself contain references — add those to the level-2 queue, do not jump to level 3.

---

## Resolution Strategy

For each external path found during scanning:

1. **Resolve the path** — determine the absolute source path
2. **Compute the target path** — preserve relative structure inside the test repo
3. **Copy the file/directory** — into the test repo at the computed target path
4. **Record the copy** — add to a dependency manifest for verification

### Path Types

| Path Type | Example | Resolution |
|-----------|---------|------------|
| Relative within skill | `references/step-01/config.md` | Already inside artifact — no copy needed |
| Relative within repo | `projects/30-day-readmissions/reference/` | Copy preserving repo-relative path |
| Absolute local path | `D:\my_ai_projects\...\some-file.md` | Copy to equivalent repo-relative path |
| Wikilink | `[[157-kernel-build-.../artifact-isolation]]` | Resolve to actual file, copy if external |

---

## Artifact Type Table

What to scan for each artifact type:

| Artifact Type | Primary Entry | Scan Targets |
|---------------|--------------|--------------|
| Kernel command | `.claude/commands/kernel/[name].md` | Command file, referenced skill folder, design docs |
| Skill | `.claude/skills/[name]/SKILL.md` | SKILL.md, workflow.md, all steps/, references/, contracts/ |
| Harness | Multiple skills + framework | Each skill folder, framework/, interfaces/, shared references |
| Agent workflow | `.claude/skills/[name]/SKILL.md` | SKILL.md, workflow.md, state schemas, referenced protocols |

### Per-Type Scan Checklist

**Command:**
1. Read command entry point — extract skill path reference
2. Read SKILL.md — extract file index, all step paths
3. Read each step — extract external references
4. Read contracts — extract schema/data references
5. Check for design docs folder (`[repo]/.claude/docs/design/[name]/`)

**Skill:**
1. Read SKILL.md — extract file index
2. Read workflow.md — extract state schema references
3. Read each step file — extract external references
4. Read each reference file — extract nested references
5. Read contracts — extract schema/data references

**Harness:**
1. Enumerate all skill folders in the harness
2. Run the Skill scan for each
3. Scan framework/ for shared utilities and references
4. Scan interfaces/ for external integrations

**Agent Workflow:**
1. Read SKILL.md — extract file index
2. Read workflow.md — extract state file schemas
3. Scan for protocol references (`.claude/protocols/`)
4. Scan for hook references (`.claude/hooks/`)

---

## Verification Checklist

After all copies complete, verify:

| Check | Method | Pass Condition |
|-------|--------|----------------|
| File index entries exist | Read SKILL.md, check each path | All listed files exist in test repo |
| Step references resolve | Grep each step for file paths | All referenced files exist in test repo |
| Contract JSONs parse | `python -c "import json; json.load(open(f))"` | No parse errors |
| No broken wikilinks | Grep all `.md` files for `[[...]]` | Each wikilink target exists |
| Dependency manifest complete | Compare manifest to actual copies | 1:1 match |

---

## Edge Cases

| Scenario | Handling |
|----------|----------|
| Circular references | Track copied paths in a set; skip if already copied |
| Optional references | Log warning, continue — do not fail the copy |
| Path does not exist | Log warning with the missing path, continue — do not fail |
| Nested skill references | Follow the reference chain — copy the nested skill too |
| Binary files (xlsx, pdf) | Copy as-is if referenced by the artifact |
| Large directories | Copy only files actually referenced, not entire trees |

---

## Dependency Manifest

Maintain a manifest during resolution:

```json
{
  "artifact": "check-data",
  "source_repo": "D:\\my_ai_projects\\...\\hmsa-healthcare-qa",
  "dependencies": [
    {
      "source": ".claude/skills/check-data/SKILL.md",
      "target": ".claude/skills/check-data/SKILL.md",
      "type": "primary",
      "status": "copied"
    },
    {
      "source": "projects/30-day-readmissions/reference/schema.json",
      "target": "projects/30-day-readmissions/reference/schema.json",
      "type": "external_reference",
      "status": "copied"
    }
  ],
  "warnings": [
    "Optional reference not found: docs/design/check-data/overview.md"
  ]
}
```

The manifest is used by the verification checklist and logged in the eval report.
