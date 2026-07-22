# Gate Contract — /summarize

## Per-Step Gates

| Step | Gate | Method | Pass Criteria |
|------|------|--------|--------------|
| 1 | Target resolved | Check | At least one source file path found |
| 2 | Sources gathered | Check | Backlog file read (if backlog mode) + at least one deliverable found |
| 3 | Requirements diffed | Check | Every backlog requirement has a status (met/partial/not addressed) |
| 4 | Findings classified | Check | Every finding in exactly one category (decision/informational/problem) |
| 5 | Summary formatted | Check | Output matches template sections from summary-format.md |
| 6 | Summary persisted | Check | Integrated: review-status.json updated. Standalone: displayed. |

## Exit Criteria

- Summary produced with all applicable sections
- If backlog mode: requirement diff table present with per-requirement status
- If integrated mode: review-status.json entry has `summary` key
- No artificial compression — all findings and files listed
