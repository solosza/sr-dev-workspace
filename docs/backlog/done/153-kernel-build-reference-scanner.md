# Reference Scanner: Kernel Primitive for Just-in-Time Knowledge Loading

## Status
Open

## Priority
High — Cross-cutting gap: every command that interacts with project data needs reference knowledge (rules, mappings, constraints), but currently each command hardcodes its own references or misses them entirely. Discovered when DOS overlap rule (added to reference docs) was invisible to check-data until manually wired in. This pattern will only get worse as reference docs grow.

## Summary

Build a reusable reference scanning loop that any kernel command can invoke to discover and load applicable project knowledge from tiered-index reference structures. The scanner reads index files, follows wikilinks to payloads, maps payloads to command steps by topic tags, and stores the mapping in state for just-in-time loading. This eliminates hardcoded reference paths in skills and ensures new rules/knowledge are automatically picked up by all commands.

## Origin

Discovered during `/check-data` development in `hmsa-healthcare-qa`. The DOS date overlap rule was added to `test-workflow/references/rules.md` (Rule 14) after Drop 1 caused duplicates. But `check-data` didn't know to read that file — its steps had hardcoded paths to only SP, DRG mapping, and exclusion list. The rule was invisible until manually wired into step-03. Every other command (validate-tc, create-sit-xlsx, verify-sit-xlsx) has the same blind spot.

The tiered-index architecture (`index.md` → payload files, 200-line threshold, recursive splitting) was designed specifically to make knowledge scannable. But without a scanner, the structure is inert — agents still need to be told exactly which files to read.

## Architecture

```
Command invocation
    │
    ▼
Step 0: Scanner
    │
    ├── 1. Receive reference index path
    ├── 2. Read index, follow wikilinks to sub-indexes
    ├── 3. Catalog all payload files with topic metadata
    ├── 4. Match payloads to step topic tags (pull model)
    ├── 5. Store mapping in state.references.by_step
    │
    ▼
Step N: Execute
    │
    ├── Read state.references.by_step[N]
    ├── Load mapped payloads (just-in-time)
    └── Apply rules/knowledge during execution
```

## Design Documents

| Document | Purpose |
|----------|---------|
| [[153-kernel-build-reference-scanner/scanner-loop]] | Core scanner algorithm: index traversal, wikilink following, payload cataloging |
| [[153-kernel-build-reference-scanner/pull-model]] | How steps declare topic interests and how the scanner matches payloads to steps |
| [[153-kernel-build-reference-scanner/build-command-integration]] | How /build-command auto-generates topic declarations when scaffolding steps |
| [[153-kernel-build-reference-scanner/state-schema]] | State persistence: references mapping, caching, invalidation |
| [[153-kernel-build-reference-scanner/design-decisions]] | Resolved and open design decisions with rationale |

## Requirements

- Scanner must work with any tiered-index structure (not healthcare-specific)
- Steps declare interests via topic tags (pull model, not push)
- Payloads loaded just-in-time per step, not all at startup
- `/build-command` should auto-generate topic tag declarations in step files
- Scanner runs once at command startup (Step 0), mapping persists in state
- Must handle recursive sub-indexes (index → sub-index → payload)
- New rules added to reference docs are automatically visible to all commands on next run
- No changes required to existing reference index files (scanner adapts to them)

## References

- Tiered-index architecture design: `hmsa-healthcare-qa/.claude/docs/design/tiered-index-architecture/`
- Current check-data implementation (prototype): `hmsa-healthcare-qa/.claude/skills/check-data/steps/step-00-date-registry.md` (step 4)
- Example reference structure: `hmsa-healthcare-qa/projects/30-day-readmissions/reference/`
- Commands that need this: check-data, validate-tc, create-sit-xlsx, verify-sit-xlsx, gap-check

## Task Builder Input
- **Deliverable:** Reusable scanner loop (skill fragment or kernel primitive) + /build-command integration
- **Location:** workspace:.claude/skills/ (scanner) + workspace:.claude/skills/build-command/ (integration)
- **Scope:** BUILD
- **Constraints:** Must not break existing commands. Pull model chosen over push model. Must integrate with existing tiered-index architecture without requiring index file modifications.
