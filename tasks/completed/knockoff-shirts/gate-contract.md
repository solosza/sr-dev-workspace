# Gate Contract — Hoi An Knockoff Shirts

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Project dir exists | file_exists | `test -d projects/hoi-an-knockoff-shirts/` | Run task 001 |
| DOC-01 | market-analysis.md exists | file_exists | `test -f projects/hoi-an-knockoff-shirts/market-analysis.md` | Run task 002 |
| DOC-02 | market-analysis has platform map | grep | `grep -qi "platform" projects/hoi-an-knockoff-shirts/market-analysis.md` | Complete research |
| DOC-03 | market-analysis has competitor table | grep | `grep -qi "competitor\|seller" projects/hoi-an-knockoff-shirts/market-analysis.md` | Complete research |
| DOC-04 | sourcing-suppliers.md exists | file_exists | `test -f projects/hoi-an-knockoff-shirts/sourcing-suppliers.md` | Run task 003 |
| DOC-05 | sourcing-suppliers has quality tier | grep | `grep -qi "quality\|grade\|tier" projects/hoi-an-knockoff-shirts/sourcing-suppliers.md` | Complete research |
| DOC-06 | legal-compliance.md exists | file_exists | `test -f projects/hoi-an-knockoff-shirts/legal-compliance.md` | Run task 004 |
| DOC-07 | legal-compliance has risk rating | grep | `grep -qi "risk" projects/hoi-an-knockoff-shirts/legal-compliance.md` | Complete research |
| DOC-08 | legal-compliance has private label | grep | `grep -qi "private label" projects/hoi-an-knockoff-shirts/legal-compliance.md` | Complete research |
| DOC-09 | logistics-fulfillment.md exists | file_exists | `test -f projects/hoi-an-knockoff-shirts/logistics-fulfillment.md` | Run task 005 |
| DOC-10 | logistics-fulfillment has HTS code | grep | `grep -qi "HTS\|duty\|chapter 61\|chapter 62" projects/hoi-an-knockoff-shirts/logistics-fulfillment.md` | Complete research |
| DOC-11 | pricing-strategy.md exists | file_exists | `test -f projects/hoi-an-knockoff-shirts/pricing-strategy.md` | Run task 006 |
| DOC-12 | pricing-strategy has landed cost | grep | `grep -qi "landed cost" projects/hoi-an-knockoff-shirts/pricing-strategy.md` | Complete research |
| DOC-13 | gtm-recommendation.md exists | file_exists | `test -f projects/hoi-an-knockoff-shirts/gtm-recommendation.md` | Run task 007 |
| DOC-14 | gtm-recommendation has recommendation | grep | `grep -qi "recommend\|path\|go-to-market" projects/hoi-an-knockoff-shirts/gtm-recommendation.md` | Complete synthesis |

## Requirements Coverage

| Gate | Task |
|------|------|
| BUILD-01 | 001-market-build-create-project-dir |
| DOC-01, DOC-02, DOC-03 | 002-market-research-market-analysis |
| DOC-04, DOC-05 | 003-market-research-sourcing-suppliers |
| DOC-06, DOC-07, DOC-08 | 004-market-research-legal-compliance |
| DOC-09, DOC-10 | 005-market-research-logistics-fulfillment |
| DOC-11, DOC-12 | 006-market-research-pricing-strategy |
| DOC-13, DOC-14 | 007-market-build-gtm-recommendation |
