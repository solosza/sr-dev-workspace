# RT Automation Architecture Analysis

**Comparison:** SSH Compliance Pattern + Playwright QA Pattern
**Framework Choice:** Playwright (analyzed both Selenium & Playwright)
**Date:** 2026-05-26

---

## Your Insight is Correct

You're seeing the right pattern decomposition:
- **Compliance:** SSH-style config + validators + hooks (rules are king)
- **Playwright Automation:** Page objects + tasks (workflows are king) - use Playwright, not Selenium

---

## Pattern 1: SSH Compliance (Compliance Rules)

```
platform-ssh/
├── framework/_reference/
│   └── validators/              ← Stateless validators
│       ├── package_validator.py
│       ├── kernel_validator.py
│       ├── service_validator.py
│       └── config_validator.py
│
├── fixtures/
│   └── host_configs.json        ← Declarative rules (WHAT to check)
│
└── hooks/
    └── compliance gates          ← Block non-compliant operations
```

**How it works:**
1. `host_configs.json` declares: "Package X must exist"
2. `PackageValidator` checks: "Does package X exist?"
3. Hooks enforce: "Can't deploy until PackageValidator passes"

**Key principle:** Rules are data (JSON), not code. Validators are stateless logic.

---

## Pattern 2: Playwright QA (Browser Automation)

```
platform-playwright/
├── framework/_reference/
│   ├── pages/                  ← Page Objects (locate elements, atomic actions)
│   │   ├── login-page.ts       ← Locators + atomic methods (click, fill) - TypeScript
│   │   ├── inventory-page.ts
│   │   └── tasks_page.py
│   │
│   ├── tasks/                  ← Task modules (orchestrate pages into workflows)
│   │   ├── login_task.py       ← Composes pages into domain operations
│   │   └── employee_management_tasks.py
│   │
│   └── roles/                  ← User personas (credentials, permissions)
│       ├── admin_role.py
│       └── user_role.py
│
├── .claude/skills/qa-management-layer/
│   ├── SKILL.md                ← Entry point
│   ├── workflow.md             ← 5-step workflow (input → pre-flight → AI processing → construction → execution)
│   └── steps/                  ← Detailed step criteria
│
└── tests/
    ├── test_login.py
    ├── test_employee_crud.py
    └── _state/workflow_state.json ← State tracking across steps
```

**How it works:**
1. LoginPage: Locators + atomic methods (wait, click, enter)
2. EmployeeManagementTasks: Orchestrates LoginPage + EmployeesPage
3. Test: Calls task, asserts outcome
4. Workflow: 5-step interactive process (validated at each step)

**Key principle:** Page Objects are low-level (UI + locators). Tasks are medium-level (domain operations). Tests are high-level (assertions).

---

## Pattern 3: RT Automation (Hybrid)

Combine both patterns:

```
rt-automation/
│
├── .claude/
│   ├── commands/rt/
│   │   ├── filter-patients.md         ← Entry point 1
│   │   ├── chart-patient.md           ← Entry point 2
│   │   └── submit-billing.md          ← Entry point 3
│   │
│   └── skills/rt-workflow/
│       ├── SKILL.md
│       └── references/
│           ├── eligibility-rules.json ← SSH pattern (declarative rules)
│           ├── charting-rules.json
│           ├── billing-codes.json
│           └── compliance-gates.md    ← What blocks what
│
├── framework/_reference/
│   │
│   ├── validators/                    ← SSH pattern (stateless validators)
│   │   ├── eligibility_validator.py   ← Check: does patient match rules?
│   │   ├── charting_validator.py      ← Check: is charting complete?
│   │   └── billing_validator.py       ← Check: does charting justify code?
│   │
│   ├── pages/                         ← Selenium pattern (page objects)
│   │   ├── emr_login_page.py          ← EMR login (locators + atomic methods)
│   │   ├── patient_search_page.py     ← Patient search (locators + atomic methods)
│   │   ├── charting_page.py           ← Charting form (locators + atomic methods)
│   │   └── billing_page.py            ← Billing form (locators + atomic methods)
│   │
│   ├── tasks/                         ← Selenium pattern (task orchestration)
│   │   ├── patient_filtering_tasks.py ← filter_patients() → Playwright + EligibilityValidator
│   │   ├── charting_tasks.py          ← chart_patient() → Playwright + ChartingValidator
│   │   └── billing_tasks.py           ← submit_billing() → Playwright + BillingValidator
│   │
│   └── roles/
│       └── respiratory_therapist_role.py ← RT user (credentials, permissions)
│
├── fixtures/
│   ├── snf_configs.json               ← SNF-specific config (EMR type, rules per SNF)
│   └── patient_test_data.json         ← Test patients (qualify, fail, edge cases)
│
└── hooks/
    ├── rt-charting-gate.py            ← Block if charting incomplete
    ├── rt-billing-gate.py             ← Block if charting doesn't justify code
    └── rt-audit-log.py                ← Log every operation
```

---

## How the Three Commands Work

### `/rt/filter-patients`

```
1. User: uploads census CSV or points to EMR
2. Command:
   a. PatientSearchPage.navigate() + read_census()
   b. For each patient: EligibilityValidator.check(patient, rules)
   c. Output: qualified[], rejected[], edge_cases[]
   d. Gate: Can't proceed to charting without qualified list
```

### `/rt/chart-patient [PATIENT_ID]`

```
1. Command:
   a. Verify patient in qualified list (gate enforces)
   b. EMRLoginPage.login() + PatientSearchPage.search(patient_id)
   c. ChartingPage.read_patient_data() → auto-populate template
   d. User: manually enters assessment, interventions, clinical note
   e. ChartingPage.submit() → submit to EMR
   f. ChartingValidator.validate_completeness() → gate allows/blocks
2. Gate: Charting complete before billing enabled
```

### `/rt/submit-billing`

```
1. Command:
   a. Get all charted patients (date range)
   b. For each charting: BillingValidator.map_codes(charting, rules)
   c. Output: audit trail (why code X chosen → because charting includes Y)
   d. BillingPage.submit(billing_data)
   e. Gate: Won't submit if charting incomplete (validator blocks)
```

---

## Data & Validation Flow

```
USER REQUIREMENT (cousin's expertise)
    │
    └──► eligibility-rules.json      (SSH pattern: declarative)
    │
    ├──► eligibility_validator.py    (SSH pattern: check logic)
    │
    └──► EligibilityValidator in tasks (called by /rt/filter-patients)

CHARTING REQUIREMENTS
    │
    └──► charting-rules.json         (SSH pattern: declarative)
    │
    ├──► charting_validator.py       (SSH pattern: check logic)
    │
    ├──► Charting Page + Task        (Selenium pattern: UI automation)
    │
    └──► ChartingValidator in tasks (called by /rt/chart-patient)

BILLING REQUIREMENTS
    │
    └──► billing-codes.json          (SSH pattern: declarative)
    │
    ├──► billing_validator.py        (SSH pattern: check logic)
    │
    ├──► BillingPage + Task          (Selenium pattern: UI automation)
    │
    └──► BillingValidator in tasks (called by /rt/submit-billing)

ENFORCEMENT
    │
    └──► Gates/Hooks                 (SSH pattern: non-bypassable)
        ├── Can't chart ineligible patient (EligibilityValidator gate)
        ├── Can't submit billing without charting (ChartingValidator gate)
        └── Audit trail (every operation logged)
```

---

## Architecture Differences

| Aspect | SSH Platform | Selenium Platform | RT Automation |
|--------|---|---|---|
| **Rules Format** | JSON configs | Not applicable | JSON configs (eligibility, charting, billing) |
| **Validators** | Python validators (stateless) | Not applicable | Python validators (eligibility, charting, billing) |
| **Page Objects** | Not applicable | Python page objects | Python page objects (EMR pages) |
| **Task Orchestration** | N/A | Python task modules | Python task modules (filter, chart, bill) |
| **Workflow** | N/A | 5-step interactive process | 3 commands (simpler, direct) |
| **Testing** | Unit tests for validators | QA tests for tasks | Behavioral validation (rule-driven, not assertion-driven) |
| **Enforcement** | Hooks + protocol gates | Tests + assertions | Hooks + validators (gates) |
| **Audit Trail** | Logs (what passed/failed validation) | Test reports | Logs (why patient qualified, why code chosen, etc.) |

---

## Why This Works Better Than Alternatives

### ❌ Pure SSH (Compliance-Only)
- ✗ No UI automation
- ✗ RTs still manually navigate EMR, copy-paste charts
- ✗ System can validate rules but can't execute them

### ❌ Pure Selenium (QA-Only)
- ✗ Page objects + tasks without compliance enforcement
- ✗ Can automate charting but not prevent invalid billing
- ✗ No audit trail for CMS defense
- ✗ Easy to work around rules

### ✅ Hybrid (SSH + Selenium)
- ✓ Rules declared (JSON), validators enforce (Python), gates block (hooks)
- ✓ Page objects navigate EMR, tasks orchestrate workflows
- ✓ Compliance is non-negotiable (gates prevent mistakes)
- ✓ Every decision auditable (why patient rejected, why code chosen)
- ✓ Rules update without code changes (update JSON, redeploy)
- ✓ Portable (same validators + pages for multiple SNFs with config customization)

---

## File Generation Priority

When execute-pipeline builds this, order matters:

1. **Validators** (SSH pattern) — define what's valid
   ```
   framework/_reference/validators/
   ├── eligibility_validator.py
   ├── charting_validator.py
   └── billing_validator.py
   ```

2. **Page Objects** (Selenium pattern) — define how to interact with EMR
   ```
   framework/_reference/pages/
   ├── emr_login_page.py
   ├── patient_search_page.py
   ├── charting_page.py
   └── billing_page.py
   ```

3. **Tasks** (Selenium pattern) — combine validators + pages
   ```
   framework/_reference/tasks/
   ├── patient_filtering_tasks.py   (uses EligibilityValidator + PatientSearchPage)
   ├── charting_tasks.py            (uses ChartingValidator + ChartingPage)
   └── billing_tasks.py             (uses BillingValidator + BillingPage)
   ```

4. **Commands** (Isagawa kernel) — entry points
   ```
   .claude/commands/rt/
   ├── filter-patients.md           (calls patient_filtering_tasks)
   ├── chart-patient.md             (calls charting_tasks)
   └── submit-billing.md            (calls billing_tasks)
   ```

5. **References** (Rules + Config)
   ```
   .claude/skills/rt-workflow/references/
   ├── eligibility-rules.json
   ├── charting-rules.json
   ├── billing-codes.json
   └── compliance-gates.md
   ```

---

## Execution Plan

### Phase 1: Design (Done ✓)
- Design baseline (you created it)
- Architecture analysis (this doc)
- Requirements capture questions (sent to cousin)

### Phase 2: Build (1-2 weeks)
1. Cousin provides rules (eligibility, charting, CPT mappings)
2. Create backlog item referencing:
   - Design baseline
   - Requirements
   - This architecture document
3. Run `/kernel/execute-pipeline`
   - Auto-generates validators
   - Auto-generates page objects
   - Auto-generates tasks
   - Auto-generates commands
4. Customize 20-30%:
   - Adjust validators based on cousin feedback
   - Tweak EMR selectors based on actual system
   - Update rules JSON with real CPT codes

### Phase 3: Testing (2-4 weeks)
- Test with 1-2 SNFs
- Iterate on rules and selectors
- Document edge cases

---

## Playwright vs Selenium: Which Framework?

**Analysis result:** Examined both platform-selenium (Python) and platform-playwright (TypeScript).

### Decision: Use Playwright

For RT automation, **Playwright > Selenium** because:

| Factor | Playwright | Selenium |
|--------|-----------|----------|
| Auto-waiting | Built-in ✅ | Manual (flaky) |
| EMR UI complexity | Robust ✅ | Requires waits |
| Debugging | Inspector+traces ✅ | Basic screenshots |
| Isagawa integration | Native MCP ✅ | Needs wrapper |
| Modern stack | TypeScript ✅ | Python (legacy) |

### Why Playwright for EMR Systems

EMRs have complex UIs (JS rendering, modal dialogs, slow networks).

**Playwright handles this automatically:**
- Auto-waiting: intelligent waits for visibility, stability, enabled state
- Smart retries: handles network latency
- Superior debugging: Inspector + trace recordings
- Isagawa native: Playwright MCP built-in

**Selenium would require:**
- Manual `.wait_for_element_visible()` calls (flaky)
- Explicit timeout configuration
- More boilerplate code
- Basic debugging only

### Code Comparison

**Selenium (Python):**
```python
def click_log_in(self):
    self.browser.wait_for_element_visible(*self.LOG_IN_BUTTON, timeout=10)  # Manual
    self.browser.click(*self.LOG_IN_BUTTON)
    return self
```

**Playwright (TypeScript):**
```typescript
async clickLogin(): Promise<LoginPage> {
  await this.browser.click(LoginPage.LOGIN_BUTTON);  // Auto-waiting built-in
  return this;
}
```

---

## Your Design is Correct

**No.** Your current design is exactly right. Here's why:

1. **You identified the SSH pattern for compliance** ✓
2. **You identified the Playwright pattern for automation** ✓
3. **You're combining them correctly** ✓
4. **3 commands are simpler than 5-step workflow** ✓ (appropriate for RT use case)

The clarity adds:
- **Compliance rules** = JSON + validators (SSH)
- **Playwright automation** = TypeScript page objects + tasks (use Playwright, not Selenium)
- **Gating** = hooks (Isagawa kernel)

This helps execute-pipeline know what to generate and in what order.

---

## Recommendation

Update your design baseline to include this architecture diagram. When cousin provides rules, you'll be ready to:
1. Translate rules to JSON (eligibility-rules.json, charting-rules.json, billing-codes.json)
2. Run execute-pipeline with reference to SSH + Selenium patterns
3. Get 70%+ auto-generated
4. Customize 30% with cousin's feedback

You're on the right track. This hybrid approach is why the system will beat competitors.
