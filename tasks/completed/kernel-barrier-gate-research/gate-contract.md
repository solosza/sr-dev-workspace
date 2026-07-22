# Gate Contract — Barrier Gate Prerequisites Research

## Gates

| Gate | Type | Test | Pass Criteria |
|------|------|------|---------------|
| BUILD-01 | file_exists | `projects/kernel-barrier-gate-research/` | Directory exists |
| DOC-01 | file_exists | `projects/kernel-barrier-gate-research/01-prereq-format.md` | File exists |
| DOC-02 | word_count | `projects/kernel-barrier-gate-research/01-prereq-format.md` | >= 300 words |
| DOC-03 | file_exists | `projects/kernel-barrier-gate-research/02-wait-loop-design.md` | File exists |
| DOC-04 | word_count | `projects/kernel-barrier-gate-research/02-wait-loop-design.md` | >= 300 words |
| DOC-05 | file_exists | `projects/kernel-barrier-gate-research/03-deadlock-and-staleness.md` | File exists |
| DOC-06 | word_count | `projects/kernel-barrier-gate-research/03-deadlock-and-staleness.md` | >= 300 words |
| DOC-07 | file_exists | `projects/kernel-barrier-gate-research/research-report.md` | File exists |
| DOC-08 | grep | `projects/kernel-barrier-gate-research/research-report.md` | Contains "YAH\|NAY\|Verdict" |
