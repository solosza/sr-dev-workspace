# Wikilinks vs Code Spans as Read Signals — Results

## Summary

Neither `→ [[path]]` (wikilinks) nor `` `path` `` (code spans) triggers automatic file reading by Claude Code. Both are **agent-interpreted conventions** — the agent sees the text and decides whether to follow it with the Read tool based on protocol instructions and context.

## How Claude Code Handles File References

Claude Code's Read tool is invoked **only when the agent explicitly calls it**. There is no client-side mechanism that auto-reads files referenced in markdown content (unlike `@path` in CLAUDE.md, which is client-parsed at startup).

When the agent encounters a file reference in any markdown file (skill, protocol, step file, lesson), the decision to read is driven by:
1. **Protocol instructions** — "Read this file" directives
2. **Pattern recognition** — familiar reference syntax signals "this file is relevant"
3. **Task context** — whether the referenced file seems necessary for the current action

## Format Comparison

| Format | Example | Signal Strength | Why |
|--------|---------|----------------|-----|
| `→ [[references/file.md]]` | Arrow + wikilink | **Strong** | Arrow prefix (`→`) acts as an explicit "follow this" directive. Double brackets (`[[]]`) are a universal hyperlink/reference convention (Obsidian, wiki systems). Combined: "go read this." |
| `` → `references/file.md` `` | Arrow + code span | **Strong** | Arrow provides the same directive. Backticks mark it as a path (monospace = file path convention). Used in SKILL.md step tables. |
| `` `references/file.md` `` | Bare code span | **Medium** | Visually distinguished as a path, but no directive to follow. Agent may or may not read it depending on context. Used in protocol table cells. |
| `[[references/file.md]]` | Bare wikilink | **Medium** | Recognizable as a cross-reference, but without the arrow directive, it's informational rather than imperative. |
| `references/file.md` | Plain text path | **Weak** | No visual distinction. Easy to miss in a paragraph. Agent unlikely to follow unless surrounding text explicitly says "read this file." |

## Observed Kernel Usage Patterns

### Pattern 1: SKILL.md Step Tables (arrow + code span)
```markdown
| 1 | Parse goal | → `references/step-01-parse-goal.md` |
```
The agent reads these during skill execution because the step table is the execution index — every row is a "do this" instruction.

### Pattern 2: Step File Cross-References (arrow + wikilink)
```markdown
→ [[references/verification-methods.md]] for details on each method.
```
Used inline within step files to point to supporting detail. The agent reads these when it hits the reference during sequential execution.

### Pattern 3: Protocol Reference Tables (bare code span)
```markdown
| Core Philosophy | `.claude/references/core-philosophy.md` |
```
The agent reads these during `/kernel/anchor` because the protocol explicitly says "Read entire file" and the table provides the path.

## Does the Arrow (`→`) Add Signal?

**Yes.** The arrow transforms a reference from informational ("this file exists") to directive ("go read this file"). It's the difference between a bibliography entry and an inline instruction.

Evidence:
- All kernel step files use `→` before cross-references that the agent MUST follow
- Protocol tables omit `→` because the anchor ceremony already instructs "read all referenced files"
- SKILL.md step tables use `→` because each row is an instruction to follow

## Does `[[]]` vs `` ` ` `` Matter?

**Minimally.** Both provide visual distinction from surrounding text. The choice is stylistic:
- `[[]]` — wiki/hyperlink convention, implies "this is a link to follow"
- `` ` ` `` — code/path convention, implies "this is a file path"

In practice, the kernel uses both interchangeably with the `→` prefix and the agent follows both equally.

## Recommendation

**Use `→ [[path]]` (arrow + wikilink) as the standard linking convention.**

Rationale:
1. **Lessons RULE ZERO mandates it** — "ALWAYS USE WIKILINK TIERED INDEXING" is already an enforced rule
2. **Wikilinks are semantically richer** — they imply "follow this link" rather than just "this is a path"
3. **Arrow prefix is the key signal** — it converts any reference from informational to directive
4. **Consistency** — the kernel step files already overwhelmingly use this format
5. **Code spans for non-directive references** — use `` `path` `` in tables and inline mentions where the reference is informational, not an instruction to read

### Proposed Convention

| Context | Format | Example |
|---------|--------|---------|
| "Read this file" directive | `→ [[path]]` | `→ [[references/step-01.md]]` |
| Step table (SKILL.md) | `→ \`path\`` | `→ \`references/step-01.md\`` |
| Informational mention | `` `path` `` | See `.claude/protocols/sr_dev-protocol.md` |
| Never use | Plain text paths | See references/step-01.md |
