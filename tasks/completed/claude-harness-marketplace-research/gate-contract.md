# Gate Contract — Claude Code Harness Marketplace Research

## Verification Methods

**Structural:** `file_exists`, `grep` — checks that files exist and contain expected content
**Functional:** `run_code` — executes Python/shell to verify logic
**Semantic:** `manual` — LLM judgment on content quality and completeness

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Project dir exists | file_exists | `test -d projects/claude-harness-marketplace-research` | Create directory |
| DOC-01 | Platforms doc exists | file_exists | `test -f projects/claude-harness-marketplace-research/platforms.md` | Create file |
| DOC-02 | Platforms doc has summary | grep | `grep -q "Summary Table" projects/claude-harness-marketplace-research/platforms.md` | Add section |
| DOC-03 | 9+ platforms documented | grep | `grep -c "^##" projects/claude-harness-marketplace-research/platforms.md \| awk '{if ($1 >= 9) exit 0; else exit 1}'` | Add platform docs |
| DOC-04 | Competitive analysis exists | file_exists | `test -f projects/claude-harness-marketplace-research/competitive-analysis.md` | Create file |
| DOC-05 | 5 tiers documented | grep | `grep -q "Tier 1" projects/claude-harness-marketplace-research/competitive-analysis.md && grep -q "Tier 5" projects/claude-harness-marketplace-research/competitive-analysis.md` | Add tier analysis |
| DOC-06 | Gaps document exists | file_exists | `test -f projects/claude-harness-marketplace-research/gaps-and-opportunities.md` | Create file |
| DOC-07 | 6+ gaps identified | grep | `grep -c "^###" projects/claude-harness-marketplace-research/gaps-and-opportunities.md \| awk '{if ($1 >= 6) exit 0; else exit 1}'` | Add gap analysis |
| DOC-08 | Distribution strategy exists | file_exists | `test -f projects/claude-harness-marketplace-research/distribution-strategy.md` | Create file |
| DOC-09 | Multi-channel approach documented | grep | `grep -q "Channel 1\|Anthropic" projects/claude-harness-marketplace-research/distribution-strategy.md` | Add channels |
| DOC-10 | Final report exists | file_exists | `test -f projects/claude-harness-marketplace-research/RESEARCH-REPORT.md` | Create file |
| DOC-11 | Executive summary included | grep | `grep -q "Executive Summary" projects/claude-harness-marketplace-research/RESEARCH-REPORT.md` | Add summary |
| DOC-12 | Recommendation clear | grep | `grep -q "Recommendation\|Recommend" projects/claude-harness-marketplace-research/RESEARCH-REPORT.md` | Add recommendation |

## Requirements Coverage

- BUILD-01: 001-market-create-project-dir
- DOC-01, DOC-02, DOC-03: 002-market-document-platform-inventory
- DOC-04, DOC-05: 003-market-analyze-competitive-landscape
- DOC-06, DOC-07: 004-market-identify-gaps-opportunities
- DOC-08, DOC-09: 005-market-recommend-distribution-strategy
- DOC-10, DOC-11, DOC-12: 006-market-compile-research-report
