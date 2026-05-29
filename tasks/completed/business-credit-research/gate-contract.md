# Gate Contract — Business Credit Stacking Research

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Project directory exists | file_exists | `test -d projects/business-credit-research` | Create directory |
| DOC-01 | Credit products doc exists | file_exists | `test -f projects/business-credit-research/01-credit-products.md` | Write file |
| DOC-02 | Credit products covers cards vs LOC | grep | `grep -q 'credit card\|line of credit' projects/business-credit-research/01-credit-products.md` | Add content |
| DOC-03 | Credit stacking doc exists | file_exists | `test -f projects/business-credit-research/02-credit-stacking.md` | Write file |
| DOC-04 | Credit stacking covers realistic limits | grep | `grep -q '250\|limit\|realistic' projects/business-credit-research/02-credit-stacking.md` | Add content |
| DOC-05 | Risks doc exists | file_exists | `test -f projects/business-credit-research/03-risks-and-costs.md` | Write file |
| DOC-06 | Risks covers personal guarantee | grep | `grep -q 'personal guarantee\|personal liability' projects/business-credit-research/03-risks-and-costs.md` | Add content |
| DOC-07 | Alternatives doc exists | file_exists | `test -f projects/business-credit-research/04-alternatives.md` | Write file |
| DOC-08 | Alternatives covers SBA loans | grep | `grep -q 'SBA\|microloan' projects/business-credit-research/04-alternatives.md` | Add content |
| DOC-09 | Research report exists | file_exists | `test -f projects/business-credit-research/research-report.md` | Write file |
| DOC-10 | Report has recommendation section | grep | `grep -q 'Recommendation\|Verdict\|Decision' projects/business-credit-research/research-report.md` | Add section |
| DOC-11 | Report has actionable next steps | grep | `grep -q 'next step\|Next Step\|action' projects/business-credit-research/research-report.md` | Add section |
