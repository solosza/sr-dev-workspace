# Output Contract: Design Doc Requirements

**Purpose:** Defines what the `/design` command must produce. Mirrors build-command's input-contract — the output of `/design` must pass the input validation of `/build-command`.

**Source:** `.claude/docs/design/build-command/references/input-contract.md`

---

## Required Sections (7 of 7 must be present)

| # | Section | Minimum Depth | Location in Design Doc |
|---|---------|---------------|----------------------|
| 1 | **Skill Identity** | One sentence: "You are a [role]." | index.md `## Skill Identity` |
| 2 | **Philosophy** | 3+ numbered principles | index.md `## Philosophy` |
| 3 | **Vocabulary** | 3+ terms in Term/Meaning table | index.md `## Vocabulary` |
| 4 | **Critical Rules** | 2+ numbered hard constraints | index.md `## Critical Rules` |
| 5 | **Workflow Summary** | 2+ steps with Step/Responsibility/Output/HITL columns | index.md `## Workflow Summary` |
| 6 | **Step File Specs** | Per-step: Purpose + Procedure minimum | references/workflow.md |
| 7 | **Complete File Structure** | Shows `.claude/skills/[name]/` tree | index.md `## Complete File Structure` |

## Optional Sections (enhance build quality)

| # | Section | Impact if Missing |
|---|---------|-------------------|
| 8 | **Reference File Frontmatter** | Layer 4 references generated as stubs |
| 9 | **INDEX.md Structure** | Layer 4 INDEX generated with default layout |
| 10 | **Contract Definitions** | Layer 5 skipped entirely |
| 11 | **State Persistence Schema** | No resume support in generated workflow.md |
| 12 | **Hook Specifications** | Layer 6 skipped entirely |

## Structural Requirements

- **Tiered index format:** index.md is an index (links to payloads). No monolithic files.
- **200-line threshold:** index.md must stay under 200 lines. Overflow → extract to payload.
- **Design Documents table:** index.md must have a wikilink table pointing to all payload files.
- **Frontmatter:** index.md must have YAML frontmatter with name, type, version, date_created, status, purpose.
- **Position diagram:** index.md should show where this command sits in the pipeline.

## Validation Procedure

For each required section:

1. Search index.md for section header
2. If not in index, follow wikilinks to payload files
3. Check minimum depth (see table above)
4. Mark pass/fail

**Pass:** 7/7 required sections present with minimum depth.
**Fail:** Any required section missing or below minimum depth → loop back to interview.
