# Research Unified File Linking Convention for Tiered Index Architecture

## Status
Open

## Priority
Medium — inconsistency causes agent drift; not blocking but compounds over time

## Summary
The tiered index architecture currently uses three different linking conventions across layers: skills use wikilinks (`→ [[path]]`), indexes use code spans (`` `path` ``), and CLAUDE.md supports `@path` imports. This inconsistency means the agent gets mixed signals about how to navigate references. Research should evaluate all options and propose a single convention (or a deliberate layered convention with clear rules for when to use which).

## Prior Research (completed)

### Conventions Found

| Convention | Syntax | Where Used | Pros | Cons |
|-----------|--------|-----------|------|------|
| Wikilinks | `[[path]]` or `→ [[path]]` | Skills layer (SKILL.md, workflow.md, step files) | Clear "read this" signal, Obsidian graph view, Karpathy LLM Wiki standard | Not standard markdown, GitHub/CommonMark won't render |
| Code spans | `` `references/rules.md` `` | Index tables (tiered index design doc, reference indexes) | Standard markdown, renders everywhere | Weaker signal to agent — looks like a label, not an action |
| @imports | `@path/to/file` | CLAUDE.md (Claude Code native) | First-class Claude Code feature, auto-reads file | Only documented for CLAUDE.md, not general-purpose |
| Typed relationships | `derived_from::[[Source]]` | LLM Wiki v2 | Semantic meaning on edges, not just existence | Complex, may be overkill for index navigation |

### Key Sources

- **Karpathy LLM Wiki** — uses `[[wikilinks]]`, minimum 2 outbound links per page, dangling links are "write this later" markers. Schema is intentionally abstract — co-evolved with your LLM. ([gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f))
- **LLM Wiki v2** — extends wikilinks with typed relationships (`derived_from::[[Source]]`, `contradicts::[[Page]]`). Not all connections are equal — edge type carries semantic weight. ([gist](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2))
- **Claude Code Best Practices** — `@path/to/file` is native import syntax for CLAUDE.md. Skills use `SKILL.md` files in `.claude/skills/`. No explicit linking convention specified beyond @imports. ([docs](https://code.claude.com/docs/en/best-practices))
- **Augment AGENTS.md Research** — format matters less than discoverability. "AGENTS.md is the only documentation location with reliable discovery." Keep each reference's scope clear. Max 10-15 references per file. ([blog](https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files))
- **Obsidian + Claude Code** — wikilinks become edges in graph view, giving live knowledge map. But not standard markdown — won't render on GitHub. ([essay](https://kennethreitz.org/essays/2026-03-06-obsidian_vaults_and_claude_code))

### Open Questions

1. Does Claude Code treat `[[wikilinks]]` differently than `` `code spans` `` when deciding what to Read?
2. Does `@path` work outside CLAUDE.md (in skill files, design docs)?
3. Should the convention differ by layer (CLAUDE.md vs skills vs indexes vs design docs)?
4. Is dual-linking (both formats) worth the maintenance cost?
5. Should we adopt typed relationships for certain edge types (e.g., `supersedes::`, `requires::`)?

## Requirements
- Evaluate which format gives the strongest "read this file" signal to Claude Code specifically
- Test whether `@path` works in skill files and design docs (not just CLAUDE.md)
- Propose either a single convention or a deliberate layered convention with clear rules
- Update tiered index architecture design doc with the chosen convention
- Provide migration path for existing files

## References
- Tiered index architecture design: `.claude/docs/design/tiered-index-architecture/` (in hmsa-healthcare-qa)
- Current skills convention: `→ [[path]]` pattern in `.claude/skills/*/SKILL.md`
- Current index convention: `` `path` `` in table cells
- Triggered by: TC-002 check-data session where index update missed convention check

## Task Builder Input
- **Deliverable:** Design decision document with chosen convention + migration checklist
- **Location:** `workspace:.claude/docs/design/tiered-index-architecture/`
- **Scope:** RESEARCH
- **Constraints:** Must work with Claude Code's tool system (Read tool). Must not break GitHub rendering for files that need it. Convention must be teachable in < 3 rules.
