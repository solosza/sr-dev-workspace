# DeepEval L3 Testing Build

Backlog: [[docs/backlog/154-kernel-build-deepeval-l3-testing]]
Design docs: [[docs/backlog/154-kernel-build-deepeval-l3-testing/composition-architecture]], [[docs/backlog/154-kernel-build-deepeval-l3-testing/golden-dataset-translator]], [[docs/backlog/154-kernel-build-deepeval-l3-testing/agent-output-capture]], [[docs/backlog/154-kernel-build-deepeval-l3-testing/metric-mapping]], [[docs/backlog/154-kernel-build-deepeval-l3-testing/iteration-tracking]], [[docs/backlog/154-kernel-build-deepeval-l3-testing/design-decisions]]

## Tasks

| # | Task | Type | Depends |
|---|------|------|---------|
| 001 | [[001-build-golden-translator]] | BUILD | none |
| 002 | [[002-build-output-capture]] | BUILD | none |
| 003 | [[003-build-metric-mapping]] | BUILD | none |
| 004 | [[004-build-iteration-tracking]] | BUILD | none |
| 005 | [[005-build-l3-composition]] | BUILD | 001, 002, 003 |
| 006 | [[006-build-prod-test-l3-step]] | BUILD | 005 |
| 007 | [[007-test-golden-translator]] | TEST | 001 |
| 008 | [[008-test-l3-pipeline]] | TEST | 006 |
