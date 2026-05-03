# 004 — Add Political Corruption & Financial Fraud Patterns to fraud_patterns.json

## Type
BUILD

## Action
Add 3 new patterns to `D:\my_ai_projects\fraud-detection-app\src\patterns\fraud_patterns.json` for political corruption and financial fraud.

## Patterns to Add

**PATTERN-032: Gift Card Skimming to Foreign Military**
- Signal: Retail gift card barcode theft with funds routed to foreign military units
- Source: ICE / Chinese CCP scheme
- check_logic: "gift_card_fraud_reports clustered_by geography AND fund_transfers to overseas_accounts within 24h_of card_activation AND destination_country is adversary_nation"
- data_sources: ["Retail fraud reports", "FinCEN SARs", "SWIFT transaction logs", "ICE intelligence"]
- sector: "financial crime"
- severity: HIGH

**PATTERN-033: Municipal Pension Book-Cooking**
- Signal: Double-counting pension payments to inflate budget shortfall
- Source: Sacramento / $2B discrepancy — CalPERS payment duplication ($1.6B), future rate miscalculation ($450M)
- check_logic: "pension_payment_records has duplicate_entries AND discrepancy_amount > 0.01 * total_pension_fund AND correction_delayed > 12_months"
- data_sources: ["CalPERS/pension fund records", "Municipal budget filings", "State controller audits", "GASB compliance reports"]
- sector: "government pensions"
- severity: HIGH

**PATTERN-034: Developer-Government Loan Collusion**
- Signal: Private developer seeks federal loan, local official secretly pledges public funds without council vote
- Source: Utah Lake scheme — $1B EPA loan, mayor pledged $5M without council vote, developer bankruptcy after project blocked
- check_logic: "federal_loan_application contains support_letter from local_official AND municipal_council_minutes has no_recorded_vote for fund_commitment AND developer has bankruptcy_filing within 24_months"
- data_sources: ["EPA/federal loan applications (FOIA)", "Municipal council minutes", "State FOIA responses", "Federal bankruptcy filings"]
- sector: "government development"
- severity: HIGH

## Target File
`D:\my_ai_projects\fraud-detection-app\src\patterns\fraud_patterns.json`

## Acceptance
- [ ] 3 new patterns added (PATTERN-032, 033, 034)
- [ ] Each has all required fields (id, name, description, source_case, severity, data_sources, check_logic, sector)
- [ ] JSON remains valid after edit

## Dependencies
None
