# Linking Convention — Migration Checklist

**Convention:** → [[references/linking-convention.md]]
**Approach:** Fix on touch + prioritized batch for high-traffic files

---

## Priority 1: High-Traffic Kernel Files

These files are read every session (anchor ceremony, skill execution). Fixing them first maximizes convention consistency.

### 1.1 Lessons Index — Topic File Links

**File:** `.claude/lessons/lessons.md`

**Before:**
```markdown
| Kernel Compliance | `kernel-compliance.md` | Hook bypass, ... |
| Git & Branching | `git-and-branching.md` | Golden master, ... |
```

**After:**
```markdown
| Kernel Compliance | → [[kernel-compliance.md]] | Hook bypass, ... |
| Git & Branching | → [[git-and-branching.md]] | Golden master, ... |
```

**Verification:**
```bash
grep -c '→ \[\[' .claude/lessons/lessons.md
# Expected: matches topic file count in index table
```

### 1.2 SKILL.md Step Tables (All Skills)

**Files:**
- `.claude/skills/task-builder/SKILL.md`
- `.claude/skills/audit-workflow/SKILL.md`
- `.claude/skills/prod-test/SKILL.md`
- `.claude/skills/kernel-domain-setup/SKILL.md`
- `.claude/skills/execute-pipeline/SKILL.md`
- `.claude/skills/eval/SKILL.md`

**Before (mixed — some use code spans, some wikilinks):**
```markdown
| 1 | Parse goal | `references/step-01-parse-goal.md` |
```

**After:**
```markdown
| 1 | Parse goal | → [[references/step-01-parse-goal.md]] |
```

**Verification:**
```bash
grep -c '→ \[\[references/' .claude/skills/*/SKILL.md
# Each SKILL.md should show matches equal to its step count
```

---

## Priority 2: Protocol and CLAUDE.md

These are structural indexes — every reference is a "read this" directive during anchor.

### 2.1 Protocol Reference Tables

**File:** `.claude/protocols/hmsa-protocol.md`

**Before:**
```markdown
| Core Philosophy | `.claude/references/core-philosophy.md` |
```

**After (keep code spans — anchor ceremony provides the "read" instruction):**
```markdown
| Core Philosophy | `.claude/references/core-philosophy.md` |
```

**Decision:** No change. Protocol tables are read under the anchor ceremony's explicit "read all referenced files" instruction. The ceremony itself is the directive — adding `→ [[]]` would be redundant. Code spans are correct here per Rule 2 of the linking convention.

### 2.2 CLAUDE.md Reference Tables

**File:** `CLAUDE.md`

**Decision:** No change. Same rationale as protocol — CLAUDE.md tables list files for reference, and the protocol/anchor provides the "read" instruction. Code spans are correct.

---

## Priority 3: Step File Cross-References

These are inline references within step files where the agent should follow the link.

### 3.1 Step Files Missing Arrow + Wikilink

**Files:** Any `.claude/skills/*/references/step-*.md` that uses bare code spans for cross-references.

**Before:**
```markdown
See `references/verification-methods.md` for details.
```

**After:**
```markdown
See → [[references/verification-methods.md]] for details.
```

**Verification:**
```bash
# Find step files with bare code-span references to other reference files (candidates for migration)
grep -rn '`references/[^`]*`' .claude/skills/*/references/step-*.md | grep -v '→'
# Expected: 0 matches after migration
```

---

## Priority 4: Task Index Files

### 4.1 000-index.md Gate Contract Links

**Files:** `tasks/*/000-index.md`

**Before:**
```markdown
Gate Contract: `gate-contract.md`
```

**After:**
```markdown
Gate Contract: → [[gate-contract.md]]
```

**Verification:**
```bash
grep -c '→ \[\[gate-contract.md\]\]' tasks/*/000-index.md
# Expected: matches count of task folders with 000-index.md
```

---

## What NOT to Migrate

These uses are correct as code spans (Rule 2 — informational):

| Pattern | Example | Why Keep |
|---------|---------|----------|
| Inline path mentions in prose | "Edit `config.json`" | Informational — not a read directive |
| Paths in code blocks/examples | `` `pytest --rootdir=...` `` | Literal code, not a reference |
| Protocol/CLAUDE.md tables | `` `.claude/references/...` `` | Anchor ceremony provides directive |
| Command invocation references | `` `/kernel/anchor` `` | Command name, not a file reference |

---

## Migration Strategy

1. **Fix on touch** — When editing any file, update its linking convention as part of the change
2. **Batch Priority 1** — Lessons index and SKILL.md files are high-impact, low-effort
3. **Skip Priority 2** — Protocol and CLAUDE.md are correct as-is (code spans appropriate)
4. **Incremental Priority 3-4** — Fix step files and task indexes during normal cycling

**Global verification after batch migration:**
```bash
# Count directive references using wikilinks (should increase)
grep -rc '→ \[\[' .claude/skills/ .claude/lessons/ tasks/*/000-index.md

# Count bare code-span cross-references in step files (should be 0)
grep -rn '`references/[^`]*`' .claude/skills/*/references/step-*.md | grep -v '→' | wc -l
```
