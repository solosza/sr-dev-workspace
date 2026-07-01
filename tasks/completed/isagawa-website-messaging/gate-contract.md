# Gate Contract — Isagawa Website Messaging

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Project dir exists | file_exists | `test -d projects/isagawa-website-messaging/` | Create dir |
| BUILD-02 | Messaging audit exists | file_exists | `test -f projects/isagawa-website-messaging/messaging-audit.md` | Create file |
| BUILD-03 | Positioning report exists | file_exists | `test -f projects/isagawa-website-messaging/positioning-report.md` | Create file |
| BUILD-04 | Variant A exists | file_exists | `test -f projects/isagawa-website-messaging/copy-variants/variant-a-technical.md` | Create file |
| BUILD-05 | Variant B exists | file_exists | `test -f projects/isagawa-website-messaging/copy-variants/variant-b-business.md` | Create file |
| BUILD-06 | Variant C exists | file_exists | `test -f projects/isagawa-website-messaging/copy-variants/variant-c-future.md` | Create file |
| BUILD-07 | Supporting copy exists | file_exists | `test -f projects/isagawa-website-messaging/supporting-copy.md` | Create file |
| BUILD-08 | Audience alignment exists | file_exists | `test -f projects/isagawa-website-messaging/audience-alignment.md` | Create file |
| BUILD-09 | Final recommendation exists | file_exists | `test -f projects/isagawa-website-messaging/final-recommendation.md` | Create file |
| FUNC-01 | Audit has current copy section | grep | `grep -q "Current Copy" projects/isagawa-website-messaging/messaging-audit.md` | Add section |
| FUNC-02 | Audit has gaps section | grep | `grep -q "Gaps" projects/isagawa-website-messaging/messaging-audit.md` | Add section |
| FUNC-03 | Positioning has alternatives | grep | `grep -q "Positioning Alternative" projects/isagawa-website-messaging/positioning-report.md` | Add section |
| FUNC-04 | Variants have hero copy | grep | `grep -q "Hero" projects/isagawa-website-messaging/copy-variants/variant-a-technical.md` | Add section |
| FUNC-05 | Final has recommended copy | grep | `grep -q "Recommended" projects/isagawa-website-messaging/final-recommendation.md` | Add section |
| TEST-01 | Cross-ref with 138 audiences | manual | Messaging addresses all 3 audiences from backlog 138 | Update copy |

## Requirements Coverage
Each gate maps to task acceptance criteria. All acceptance criteria have corresponding gates.
