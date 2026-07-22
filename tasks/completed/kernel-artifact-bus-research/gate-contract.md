# Gate Contract — Inter-Agent Artifact Bus Research

## Gates

| Gate | Type | Test | Pass Criteria |
|------|------|------|---------------|
| BUILD-01 | file_exists | `projects/kernel-artifact-bus-research/` | Directory exists |
| DOC-01 | file_exists | `projects/kernel-artifact-bus-research/01-manifest-schema.md` | File exists |
| DOC-02 | word_count | `projects/kernel-artifact-bus-research/01-manifest-schema.md` | >= 300 words |
| DOC-03 | file_exists | `projects/kernel-artifact-bus-research/02-consumer-and-overlap.md` | File exists |
| DOC-04 | word_count | `projects/kernel-artifact-bus-research/02-consumer-and-overlap.md` | >= 300 words |
| DOC-05 | file_exists | `projects/kernel-artifact-bus-research/03-combined-recommendation.md` | File exists |
| DOC-06 | word_count | `projects/kernel-artifact-bus-research/03-combined-recommendation.md` | >= 300 words |
| DOC-07 | file_exists | `projects/kernel-artifact-bus-research/research-report.md` | File exists |
| DOC-08 | grep | `projects/kernel-artifact-bus-research/research-report.md` | Contains "YAH\|NAY\|Verdict" |
