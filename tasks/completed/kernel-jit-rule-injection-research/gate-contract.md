# Gate Contract — JIT Rule Injection Research

## Gates

| Gate | Type | Test | Pass Criteria |
|------|------|------|---------------|
| BUILD-01 | file_exists | `projects/kernel-jit-rule-injection-research/` | Directory exists |
| DOC-01 | file_exists | `projects/kernel-jit-rule-injection-research/01-rule-inventory.md` | File exists |
| DOC-02 | word_count | `projects/kernel-jit-rule-injection-research/01-rule-inventory.md` | >= 300 words |
| DOC-03 | file_exists | `projects/kernel-jit-rule-injection-research/02-injection-capability.md` | File exists |
| DOC-04 | word_count | `projects/kernel-jit-rule-injection-research/02-injection-capability.md` | >= 300 words |
| DOC-05 | file_exists | `projects/kernel-jit-rule-injection-research/03-rule-map-design.md` | File exists |
| DOC-06 | word_count | `projects/kernel-jit-rule-injection-research/03-rule-map-design.md` | >= 300 words |
| DOC-07 | file_exists | `projects/kernel-jit-rule-injection-research/research-report.md` | File exists |
| DOC-08 | grep | `projects/kernel-jit-rule-injection-research/research-report.md` | Contains "YAH\|NAY\|Verdict" |
