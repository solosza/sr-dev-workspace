# Gate Contract — DAG Wave Execution Engine Research

## Gates

| Gate | Type | Test | Pass Criteria |
|------|------|------|---------------|
| BUILD-01 | file_exists | `projects/kernel-dag-wave-research/` | Directory exists |
| DOC-01 | file_exists | `projects/kernel-dag-wave-research/01-metadata-and-sorting.md` | File exists |
| DOC-02 | word_count | `projects/kernel-dag-wave-research/01-metadata-and-sorting.md` | >= 300 words |
| DOC-03 | file_exists | `projects/kernel-dag-wave-research/02-barrier-monitor-and-failures.md` | File exists |
| DOC-04 | word_count | `projects/kernel-dag-wave-research/02-barrier-monitor-and-failures.md` | >= 300 words |
| DOC-05 | file_exists | `projects/kernel-dag-wave-research/03-lesson-reconciliation-and-comparison.md` | File exists |
| DOC-06 | word_count | `projects/kernel-dag-wave-research/03-lesson-reconciliation-and-comparison.md` | >= 300 words |
| DOC-07 | file_exists | `projects/kernel-dag-wave-research/research-report.md` | File exists |
| DOC-08 | grep | `projects/kernel-dag-wave-research/research-report.md` | Contains "YAH\|NAY\|Verdict" |
