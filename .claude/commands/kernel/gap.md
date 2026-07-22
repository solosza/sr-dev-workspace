# /gap

Dynamic gap analysis for any corpus — skills, design docs, test cases, queries, or mixed file sets.

## Usage

```
/gap [target-path]
/gap [target-path] --fix
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `target-path` | Folder or file to check | `.claude/skills/spawn-agent-swarm/` |
| `--fix` | Enter fix mode after report | `/gap projects/30-day-readmissions/autopend/ --fix` |

## What It Does

Reads a target folder, auto-detects what kind of content it contains (skill, design doc, test cases, queries, or mixed), applies context-appropriate consistency checks, and reports every gap found with exact file path and line number. Optionally enters fix mode where each proposed fix requires user approval before being applied.

## Target Types (Auto-Detected)

- **Skill folder** (`.claude/skills/*/`) — reference, schema, count, terminology checks
- **Design doc** (`.claude/docs/design/*/`) — completeness checklist, reference resolution
- **Test artifacts** (contains `test-cases.md`, `tc-queries.sql`, etc.) — coverage, TC-AC, TC-query alignment
- **Onboard run** (contains `onboard-runs/`) — artifact completeness, cross-artifact consistency
- **Any folder** — best-effort: file references, wikilinks, mentioned paths

## Examples

```
/gap .claude/skills/build-command/
/gap .claude/docs/design/gap-check/
/gap projects/30-day-readmissions/autopend/ --fix
/gap projects/30-day-readmissions/exclusion-file/
```

## Design Reference

> `.claude/docs/design/gap-check/index.md`

## Skill Reference

> `.claude/skills/gap-check/`
