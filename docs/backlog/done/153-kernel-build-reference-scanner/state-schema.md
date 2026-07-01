# State Schema: References Mapping

## Status
NEW

## Purpose

Define how the scanner's output is persisted in command state so steps can load their mapped payloads just-in-time across session boundaries.

## Schema

```json
{
  "references": {
    "index_path": "projects/30-day-readmissions/reference/index.md",
    "scan_timestamp": "2026-06-23T00:00:00Z",
    "payload_catalog": [
      {
        "path": "references/test-workflow/references/rules.md",
        "topics": ["rules", "dos-overlap", "member-uniqueness"],
        "source_index": "references/test-workflow/index.md"
      }
    ],
    "by_step": {
      "all": ["references/test-workflow/references/rules.md"],
      "1": ["references/test-workflow/references/reference-tables.md"],
      "4": ["references/test-workflow/references/reference-tables.md"],
      "5": ["references/test-workflow/references/reference-tables.md"],
      "6": ["references/test-workflow/references/tools.md"],
      "7": [
        "references/test-workflow/references/qrs-columns.md",
        "references/sit-xlsx/references/format.md",
        "references/sit-xlsx/references/automation.md"
      ]
    }
  }
}
```

## Where It Lives

Inside the command's existing state file. For check-data: `.claude/state/check-data-state.json`. For validate-tc: `.claude/state/validate-tc-state.json`. Each command manages its own reference mapping.

## Caching and Invalidation

- **Cache:** The `by_step` mapping persists across sessions. On resume, the scanner skips re-scanning if `references` is populated (same as sheets/corpus).
- **Invalidation:** User says "reconfigure" at Step 0, or the index file's modification time is newer than `scan_timestamp`.
- **No automatic re-scan per step.** The index is scanned once at startup. If reference files change mid-session, the user must reconfigure. This keeps the loop lightweight.

## How Steps Use It

At the start of each step, the agent:
1. Reads `state.references.by_step["all"]` + `state.references.by_step[step_number]`
2. Reads each mapped payload file
3. Internalizes the rules/knowledge before proceeding

This is just-in-time loading — the agent doesn't read all payloads upfront, only the ones mapped to the current step.

## Dependencies

- Scanner loop must produce the payload_catalog
- Pull model must resolve by_step mapping from step topics
