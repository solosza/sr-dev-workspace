# Templates & Location Decision Tree

---

## Simple Item Template

```markdown
# [Title]

## Status
Open

## Priority
[High | Medium | Low] — [one-line reason]

## Summary
[2-3 sentences explaining what this is and why it matters]

## Requirements
- [Key requirement or question 1]
- [Key requirement or question 2]
- [Key requirement or question 3]

## References
- [Any relevant links, repos, contacts, backlog items]

## Task Builder Input
- **Deliverable:** [What must exist when done]
- **Location:** [workspace | new-repo:[path] | subproject:[name]]
- **Scope:** [BUILD | RESEARCH | TEST | REFACTOR]
- **Constraints:** [Repos, dependencies, human decisions, blockers]
```

---

## Complex Item Index Template

```markdown
# [Title]

## Status
Open

## Priority
[High | Medium | Low] — [one-line reason]

## Summary
[2-3 sentences explaining what this is and why it matters]

## Design Documents

| Document | Purpose |
|----------|---------|
| [[NNN-tag-verb-object/component-a]] | One-line description |
| [[NNN-tag-verb-object/component-b]] | One-line description |

## Architecture

[Flow diagram or component relationship overview]

## Requirements
- [High-level requirements — don't duplicate sub-docs]

## References
- [Any relevant links, repos, contacts, backlog items]

## Task Builder Input
- **Deliverable:** [What must exist when done]
- **Location:** [workspace | new-repo:[path] | subproject:[name]]
- **Scope:** [BUILD | RESEARCH | TEST | REFACTOR]
- **Constraints:** [Repos, dependencies, human decisions, blockers]
```

---

## Sub-Document Template

```markdown
# [Component Name]

## Status
[NEW | exists — needs enhancement | future]

## Location
[Where the code lives or will live]

## What It Does
[Description of this component's responsibility]

## Input/Output
- **Input:** [what this component receives]
- **Output:** [what this component produces]

## Dependencies
- [Other components this depends on]

## Requirements
- [Detailed requirements for task-builder to create granular tasks]
```

Common sub-document types:
- `pipeline.md` — execution architecture / data flow
- `spec-architecture.md` — file structure, required artifacts
- `design-decisions.md` — resolved decisions with rationale
- `design-principles.md` — guiding principles and trade-offs
- `open-gaps.md` — unresolved questions, blockers
- `gaps-analysis.md` — identified gaps and risks

---

## Location Decision Tree

Every backlog item must specify WHERE the deliverable goes. Three location types:

| Type | Format | When to Use |
|------|--------|-------------|
| `workspace` | `workspace` or `workspace:[path]` | Feature, fix, or enhancement in this repo |
| `new-repo` | `new-repo:[path]` | Standalone app, library, or spec that gets its own repo |
| `subproject` | `subproject:[name]` | Multi-file deliverable under `projects/` in this workspace |

### Auto-Resolution Rules

| Deliverable Type | Auto-Resolved Path |
|-----------------|-------------------|
| New app, tool, or standalone project | `new-repo:D:\my_ai_projects\[project-name-kebab]` |
| New domain spec, or testing a domain spec | `new-repo:D:\my_ai_projects\project_test_repos\[project-name-kebab]` |
| Feature/fix/enhancement to this workspace | `workspace` (or `workspace:[subpath]` if scoped) |
| Research, notes, or multi-file non-code project | `subproject:[name]` → `projects/[name]/` |

### Decision Procedure

1. Does the deliverable say "spec", "domain spec", "test repo", or "testing platform"?
   → `new-repo:D:\my_ai_projects\project_test_repos\[name]`
2. Does it say "app", "repo", "tool", "pipeline", "platform", or "library"?
   → `new-repo:D:\my_ai_projects\[name]`
3. Is it a change to existing files in this workspace (commands, protocols, skills, fixes)?
   → `workspace`
4. Is it research, notes, or a multi-file deliverable that belongs alongside other projects?
   → `subproject:[name]`
5. Fallback: `workspace`

**Rule:** NEVER ask the user for paths. Apply this tree deterministically.
