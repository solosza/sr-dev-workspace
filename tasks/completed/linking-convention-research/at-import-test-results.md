# @path Import Test Results

## Summary

The `@path/to/file` syntax is **CLAUDE.md-specific**. It does NOT work as an auto-read mechanism in skill files, design docs, or any other markdown files.

## Test Results

| Context | @path Auto-Reads? | Notes |
|---------|-------------------|-------|
| **CLAUDE.md** | YES | Files referenced with `@path` are auto-loaded into conversation context at session start |
| **Skill files (.claude/skills/)** | NO | `@path` is treated as plain text when the agent reads the file |
| **Design docs** | NO | Same as skill files — no auto-read behavior |
| **Command files (.claude/commands/)** | NO | Commands are expanded into prompts but `@path` references inside them are not auto-resolved |
| **Protocol files** | NO | Agent must explicitly use Read tool to follow references |

## How @path Works in CLAUDE.md

Claude Code parses CLAUDE.md at startup and resolves `@path/to/file` references by reading those files and injecting their contents into the initial conversation context. This is a feature of the Claude Code client, not the LLM itself.

When the agent later reads other markdown files (skills, protocols, design docs), the Claude Code client does NOT parse those files for `@path` references. The agent sees the literal text `@path/to/file` and must decide whether to follow it using the Read tool.

## Implications for Linking Convention

- `@path` is NOT a viable general-purpose linking convention
- It only works in one specific file (CLAUDE.md) processed by the Claude Code client
- For skill files, protocols, and design docs, a different linking convention is needed
- The kernel already uses two alternatives: `→ [[file.md]]` (wikilinks) and `` `path/to/file` `` (code spans)
- These rely on the agent recognizing the pattern and following it, not on client-side auto-resolution

## Recommendation

Do not use `@path` as a linking convention outside CLAUDE.md. It creates a false expectation of auto-resolution that doesn't exist. Use wikilinks or code spans instead, which are agent-interpreted conventions (the agent reads and follows them by protocol).
