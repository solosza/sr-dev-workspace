# Gate Contract — Ephemeral Sub-Agent Execution Research

## Gates

| Gate | Type | Test | Pass Criteria |
|------|------|------|---------------|
| BUILD-01 | file_exists | `projects/kernel-ephemeral-subagents-research/` | Directory exists |
| DOC-01 | file_exists | `projects/kernel-ephemeral-subagents-research/01-current-ephemeral-surface.md` | File exists |
| DOC-02 | word_count | `projects/kernel-ephemeral-subagents-research/01-current-ephemeral-surface.md` | >= 300 words |
| DOC-03 | file_exists | `projects/kernel-ephemeral-subagents-research/02-industry-pattern-and-cost.md` | File exists |
| DOC-04 | word_count | `projects/kernel-ephemeral-subagents-research/02-industry-pattern-and-cost.md` | >= 300 words |
| DOC-05 | file_exists | `projects/kernel-ephemeral-subagents-research/03-integration-design.md` | File exists |
| DOC-06 | word_count | `projects/kernel-ephemeral-subagents-research/03-integration-design.md` | >= 300 words |
| DOC-07 | file_exists | `projects/kernel-ephemeral-subagents-research/research-report.md` | File exists |
| DOC-08 | grep | `projects/kernel-ephemeral-subagents-research/research-report.md` | Contains "YAH\|NAY\|Verdict" |
