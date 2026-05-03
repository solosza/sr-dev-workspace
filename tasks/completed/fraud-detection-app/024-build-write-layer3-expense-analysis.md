# Write Layer 3 — Expense Analysis

## Type
BUILD

## Description
Layer 3: Analyze 990 expense categories, officer compensation, program spending ratios.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\pipeline\layer3_expense_analysis.py` with class `ExpenseAnalysis`:
- `__init__(self)` — initialize thresholds
- `analyze_expenses(self, entity_profile: EntityProfile) -> ExpenseReport` — full expense analysis
- `check_program_spending(self, filing) -> bool` — does program spending match award purpose? (e.g., $10M nutrition award but $0 food costs)
- `check_compensation_ratio(self, filing) -> float` — officer compensation as % of total expenses (flag if >40%)
- `check_rapid_spenddown(self, filings: list) -> bool` — did entity spend >80% of award within 6 months with no deliverables?
- `ExpenseReport` model: total_expenses, program_expenses, compensation_total, compensation_ratio, rapid_spenddown (bool), anomalies (list of str)

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/pipeline/layer3_expense_analysis.py`
- [ ] `grep -q "class ExpenseAnalysis" D:/my_ai_projects/fraud-detection-app/src/pipeline/layer3_expense_analysis.py`
