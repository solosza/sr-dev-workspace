# Gate Contract — AI UGC Content Pipeline Research

## Gates

| Gate | Type | Test | Pass Criteria |
|------|------|------|---------------|
| BUILD-01 | file_exists | `projects/ai-ugc-research/` | Directory exists |
| DOC-01 | file_exists | `projects/ai-ugc-research/01-seedance-ai-video.md` | File exists |
| DOC-02 | word_count | `projects/ai-ugc-research/01-seedance-ai-video.md` | >= 300 words |
| DOC-03 | file_exists | `projects/ai-ugc-research/02-brand-market-economics.md` | File exists |
| DOC-04 | word_count | `projects/ai-ugc-research/02-brand-market-economics.md` | >= 300 words |
| DOC-05 | file_exists | `projects/ai-ugc-research/03-competition-platforms.md` | File exists |
| DOC-06 | word_count | `projects/ai-ugc-research/03-competition-platforms.md` | >= 300 words |
| DOC-07 | file_exists | `projects/ai-ugc-research/research-report.md` | File exists |
| DOC-08 | grep | `projects/ai-ugc-research/research-report.md` | Contains "Go/No-Go\|Decision\|Recommendation" |
