# Gate Contract — Hội An Leather Goods Research

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Project directory exists | file_exists | `test -d projects/hoi-an-leather/` | Create directory |
| BUILD-02 | README exists | file_exists | `test -f projects/hoi-an-leather/README.md` | Write file |
| BUILD-03 | Market analysis exists | file_exists | `test -f projects/hoi-an-leather/market-analysis.md` | Run task 003 |
| BUILD-04 | Supplier terms exists | file_exists | `test -f projects/hoi-an-leather/supplier-terms.md` | Run task 004 |
| BUILD-05 | Platform decision exists | file_exists | `test -f projects/hoi-an-leather/platform-decision.md` | Run task 005 |
| BUILD-06 | Logistics doc exists | file_exists | `test -f projects/hoi-an-leather/logistics-fulfillment.md` | Run task 006 |
| BUILD-07 | Pricing strategy exists | file_exists | `test -f projects/hoi-an-leather/pricing-strategy.md` | Run task 007 |
| BUILD-08 | GTM plan exists | file_exists | `test -f projects/hoi-an-leather/go-to-market-plan.md` | Run task 008 |
| FUNC-01 | Market analysis has competitor table | grep | `grep -q "Seller\|seller\|Etsy\|shop" projects/hoi-an-leather/market-analysis.md` | Expand research |
| FUNC-02 | Pricing doc has cost model | grep | `grep -q "Landed\|landed\|Cost\|cost" projects/hoi-an-leather/pricing-strategy.md` | Add cost model |
| FUNC-03 | Supplier terms has spec sheet | grep | `grep -q "Spec\|spec\|dimension\|hardware" projects/hoi-an-leather/supplier-terms.md` | Add spec template |
| FUNC-04 | GTM plan has action items | grep | `grep -q "Phase 1\|Action\|action\|Next step" projects/hoi-an-leather/go-to-market-plan.md` | Add action items |
| FUNC-05 | GTM plan is substantive | run_code | `test $(wc -l < projects/hoi-an-leather/go-to-market-plan.md) -gt 60` | Expand plan |
| DOC-01 | Platform recommendation is clear | manual | platform-decision.md names a winner (Etsy or Shopify) with rationale | Add recommendation |
| DOC-02 | Pricing model covers 3 SKUs | manual | pricing-strategy.md has rows for shoulder bag, duffel, and tote | Add missing SKUs |

## Requirements Coverage
- BUILD-01 → task 001
- BUILD-02 → task 002
- BUILD-03, FUNC-01 → task 003
- BUILD-04, FUNC-03 → task 004
- BUILD-05, DOC-01 → task 005
- BUILD-06 → task 006
- BUILD-07, FUNC-02, DOC-02 → task 007
- BUILD-08, FUNC-04, FUNC-05 → task 008
