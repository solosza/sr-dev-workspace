# State Schema: References Mapping

## Where State Lives

Inside each command's existing state file. Examples:
- `.claude/state/check-data-state.json` → `references` key
- `.claude/state/validate-tc-state.json` → `references` key

Each command manages its own reference mapping. The scanner writes to the `references` key; the command owns the rest of the file.

## JSON Schema

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

### Field Definitions

| Field | Type | Description |
|-------|------|-------------|
| `index_path` | string | Path to the root index.md that was scanned |
| `scan_timestamp` | string (ISO 8601) | When the scan was performed |
| `payload_catalog` | array of objects | Full catalog from `scan_index()` |
| `payload_catalog[].path` | string | Resolved absolute path to the payload file |
| `payload_catalog[].topics` | array of strings | Topic tokens extracted from headings, filenames, and context |
| `payload_catalog[].source_index` | string | Which index.md contained the link to this payload |
| `by_step` | object | Step-number-to-payload-paths mapping from `match_payloads_to_steps()` |
| `by_step.all` | array of strings | Payloads that match every step (topic "all") |
| `by_step[N]` | array of strings | Payloads matched to step N by topic intersection |

## Caching Rules

- **Skip re-scan** if `references` is populated and the index file has not been modified since `scan_timestamp`.
- Check: compare `os.path.getmtime(index_path)` against `scan_timestamp`. If mtime <= scan_timestamp, cache is valid.

## Invalidation

- User says "reconfigure" at Step 0 — forces full re-scan regardless of cache.
- Index file mtime > `scan_timestamp` — index was edited since last scan, re-scan required.
- No automatic re-scan per step. The index is scanned once at startup. If reference files change mid-session, the user must reconfigure.

## How Steps Use It

At the start of each step, the agent:
1. Reads `state.references.by_step["all"]` + `state.references.by_step[step_number]`
2. Reads each mapped payload file using the Read tool
3. Internalizes the rules/knowledge before proceeding

This is just-in-time loading — the agent reads only the payloads mapped to the current step, not the entire catalog.

## Dependencies

- `scan_index()` produces the `payload_catalog`
- `match_payloads_to_steps()` produces the `by_step` mapping
- Both live in `.claude/skills/reference-scanner/scanner.py`
