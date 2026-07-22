# Gate Contract — Rolling Summarization Research

## Gates

| Gate | Type | Test | Pass Criteria |
|------|------|------|---------------|
| BUILD-01 | file_exists | `projects/kernel-rolling-summarization-research/` | Directory exists |
| DOC-01 | file_exists | `projects/kernel-rolling-summarization-research/01-compaction-survival-audit.md` | File exists |
| DOC-02 | word_count | `projects/kernel-rolling-summarization-research/01-compaction-survival-audit.md` | >= 300 words |
| DOC-03 | file_exists | `projects/kernel-rolling-summarization-research/02-gap-analysis-and-design.md` | File exists |
| DOC-04 | word_count | `projects/kernel-rolling-summarization-research/02-gap-analysis-and-design.md` | >= 300 words |
| DOC-05 | file_exists | `projects/kernel-rolling-summarization-research/03-portfolio-ranking.md` | File exists |
| DOC-06 | word_count | `projects/kernel-rolling-summarization-research/03-portfolio-ranking.md` | >= 300 words |
| DOC-07 | file_exists | `projects/kernel-rolling-summarization-research/research-report.md` | File exists |
| DOC-08 | grep | `projects/kernel-rolling-summarization-research/research-report.md` | Contains "YAH\|NAY\|Verdict" |
