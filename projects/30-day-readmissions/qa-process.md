# QA Process

A systematic approach to testing any project. Follow it from the start. If you're joining mid-project, see "Joining Mid-Project" at the bottom — same steps, different order.

---

## When to Use This

Every time you start a new project, join an existing one, pick up a new phase, or take over someone else's test suite. The steps are the same. The depth depends on how much is already in place.

---

## Onboarding (before you test)

### 1. Business Context — WHY

Understand why this project exists before touching a single test case. What's the problem, who's affected, what's the financial impact, what happens if we get it wrong.

Without this, you're testing mechanics without understanding purpose. You won't catch business logic gaps because you won't know the business logic.

### 2. System Design — HOW

Map the components, data flow, integrations, environments. What talks to what, in what order, using what technology.

Draw it. If you can't draw the flow, you don't understand it well enough to test it.

### 3. Requirements — WHAT'S DEFINED

Read every story, every AC, every attachment. Note what's detailed vs what's vague, what's consistent vs what contradicts. Flag gaps before testing, not during.

Don't assume two stories that look similar have the same ACs. Read each one.

### 4. Existing Coverage — WHAT'S TESTED

Map the test plan. Every folder, every TC, every suite. Understand the structure — repo vs execution, how TCs flow into sprint runs.

Count what exists. You can't find gaps if you don't know the baseline.

### 5. Testing Layers — WHAT LEVELS APPLY

For every project or phase, identify which layers of testing apply. Not every project needs all layers, but you need to consciously decide which ones matter.

Common layers:

| Layer | Question |
|-------|----------|
| Input processing | Does the pipeline/workflow work end-to-end? |
| Input content / validation | Is the input data valid before it enters the system? |
| Data integrity | Is the output data correct after the system processes it? |
| Cross-system consistency | Do related datasets or systems agree with each other? |
| Business rule validation | Does the system make the right decision? |
| Integration | Do the systems talk to each other correctly? |
| Regression | Did the new change break something that used to work? |

### 6. Shift-Left Analysis — WHAT CAN BE CAUGHT EARLIER

For every testing layer, ask: can this be caught earlier in the process? Earlier is cheaper, faster, and less risky.

```
The Shift-Left Question (ask for EVERY layer):

  Current: test happens HERE ──→ problem found ──→ expensive to fix
                                                    (cleanup, re-run, investigate)

  Shift-left: test happens HERE ──→ problem caught ──→ cheap to fix
              (earlier)              (never entered the system)
```

Shift-left isn't just automation. It's also:

Reviewing requirements before they become code. Catching AC gaps before anyone writes a test case. Reviewing test data before execution so bad inputs don't waste a run. Understanding what the code already validates before writing redundant TCs. Asking questions in the morning so you have answers by standup instead of after.

If you find yourself cleaning up after a failed test, ask: could I have caught this before the test ran?

### 7. Gap Analysis — WHAT'S MISSING PER LAYER

For each testing layer, compare existing coverage against what should exist. Categorize gaps by confidence:

**Confirmed** means both the requirement and the missing TC are clear. **Likely** means the requirement exists but the AC detail is vague. **Unknown** means it depends on an unanswered question.

Don't write TCs for unknown gaps. Get the answer first. The gap resolves itself once the question is answered.

### 8. Dev Overlap Check — WHAT'S ALREADY VALIDATED IN CODE

Before writing TCs, find out what the code already validates. Stored procedures, ETL packages, application logic, unit tests. Your TCs should verify the system works end-to-end with real data in a real environment, not re-test what the code already handles internally.

Ask the dev team: what validation does the code already do? What does the ETL reject before data reaches the database? Is there unit test coverage I can review?

The answer determines your TC count. Don't write 35 TCs when 11 would cover it.

### 9. Ownership & Process — WHO DOES WHAT

Clarify before you start. Who owns which test level (SIT, UAT, regression)? What's the flow from dev through to production? Who wrote the existing TCs and why are they structured the way they are? What's the handoff between test levels? What environment does each level use?

If you don't ask, you'll either duplicate someone else's work or leave a gap both of you assumed the other was covering.

### 10. Environment Access — CAN I ACTUALLY RUN TESTS

List every tool, connection, and permission you need. Chase them all in parallel, not one at a time. You can't execute anything until every link in the chain is in place.

Don't wait until you're ready to run tests to discover you don't have access. Start this on day one.

---

## Test Categories & Priority

Before writing or executing TCs, know the categories and the order. This applies across every phase, every layer. Write and execute in this order — each category builds on the one before it.

### The Categories (in execution order)

**1. Happy Path** — normal expected behavior. The main workflow with valid data doing exactly what it's supposed to do. If happy path fails, nothing else matters. Always test this first.

**2. Negative** — invalid input and error conditions. What happens when things go wrong? Missing files, bad data, wrong formats, unauthorized access. The system should fail gracefully with clear error messages, not crash silently or corrupt data.

**3. Edge Cases** — unusual but valid inputs. Not wrong, just weird. A file with one row. A code at the boundary of two categories. A date of today. These are valid scenarios that developers often don't think about.

**4. Boundary** — at exact limits. The precise threshold where behavior changes. Day 30 vs day 31 of a time window. The maximum number of rows a file can have. The exact character limit on a field. Off-by-one errors live here.

**5. Parametric** — multiple parameter combinations. When inputs interact with each other. Same code but different business unit. Same category but different facility. An update action with a blank termination date. The matrix of combinations where one valid input paired with another valid input produces unexpected behavior.

**6. Concurrency** — race conditions and parallel safety. What happens when two jobs run at the same time? Two files placed simultaneously? A file being loaded while another is being archived? Not every system needs concurrency testing, but if batch jobs run in parallel, it matters.

**7. State** — state transitions and persistence. A record goes from active to terminated. A claim goes from pending to denied. A file goes from processing to archived. Does the system handle every valid state transition? Does it prevent invalid ones?

### Priority Model

Not every TC is equal. When time is limited, priority tells you what to run.

**P0 — Must Have.** Cannot ship without these. Blocks release. Happy path for critical flows, core business logic, data integrity checks that prevent corruption. If P0 fails, stop and fix before anything else.

**P1 — Should Have.** Should not ship without these. Risky to skip. Negative tests for common error scenarios, key boundary conditions, integration points between systems. If P1 fails, assess risk before proceeding.

**P2 — Nice to Have.** Ship if time permits. Edge cases for rare scenarios, parametric combinations that are unlikely in production, concurrency tests for low-volume operations. If P2 fails, log it and move on.

### Quality Gates

Each delivery stage has a minimum bar. Don't move to the next stage until the current gate passes.

| Stage | What Must Pass | When |
|-------|---------------|------|
| Function complete | Happy path + negative tests for the individual function | Before integrating with other components |
| Component complete | Above + integration tests between related functions | Before feature-level testing |
| Feature complete | Above + end-to-end tests for the full feature flow | Before release candidate |
| Release ready | Full suite passes, no open P0/P1 defects, coverage targets met | Before production deployment |

### How This Maps to Your TCs

When writing new TCs, tag each one with a category and priority. When executing, run in order: all P0 happy paths first, then P0 negatives, then P1 happy paths, and so on. This way if you run out of time, the most important tests ran first.

```
Writing order:        Execution order:
  1. Happy path         1. P0 Happy path
  2. Negative           2. P0 Negative
  3. Edge cases         3. P1 Happy path
  4. Boundary           4. P1 Negative
  5. Parametric         5. P1 Edge / Boundary
  6. Concurrency        6. P2 everything else
  7. State
```

---

## Execution (while you test)

### 11. Test Data Strategy — HOW TO CREATE AND MANAGE INPUT

Before executing, figure out who creates test data, whether templates exist, if the data is reusable across sprints, whether there are privacy or compliance constraints, and where test data is stored.

Bad test data wastes runs. Invest time here before executing.

### 12. Manual Execution — RUN EVERYTHING BY HAND FIRST

Execute every TC manually before automating anything. You need firsthand knowledge of how the system behaves — timing, quirks, error messages, things the TC steps don't mention.

Document everything during execution, not after. If you don't capture it in the moment, you'll forget.

### 13. Document Findings — FILL PLACEHOLDERS, CAPTURE EVIDENCE

Every unknown you fill in during manual execution is one less blocker for automation. Capture real values — table names, paths, job names, connection strings. Capture actual system behavior — timing, error messages, edge cases. Capture evidence — screenshots, query results, logs. Capture anything unexpected.

### 14. Defect Management — FILE BUGS PROPERLY

Know the process before you find your first defect. Where to file, what fields are required, who to assign, what evidence to attach, what makes something a blocker vs a known issue.

Figure this out on day one. Not when you're staring at your first failed test wondering what to do next.

### 15. Sign-Off / Exit Criteria — WHAT DOES "DONE" LOOK LIKE

Define before you start, not when you're trying to finish. What pass rate is required? What's a blocker vs a known issue? Who approves test completion? What evidence or report is needed?

---

## Transition (after you test)

### 16. Regression Plan — WHAT RE-RUNS NEXT SPRINT

When the next sprint changes something, which TCs from this sprint need to re-run? Define the regression suite before moving on, while it's fresh.

### 17. Automation Plan — WHAT TO AUTOMATE, WHAT STAYS MANUAL

Only after manual execution is complete. You now know which TCs are high-ROI for automation (frequent, stable, time-consuming), which should stay manual (rare, unstable, requires judgment), and what tool stack works based on actual system behavior rather than guessing.

### 18. Handoff & Dependency Mapping — WHO'S WAITING ON YOU

Your testing feeds downstream work. Map which phases or items depend on your results, who needs to know when you're done, and what artifacts they need from you.

---

## The System at a Glance

```
ONBOARDING (before you test):
  1.  Business context         → why does this exist
  2.  System design            → how does it work
  3.  Requirements             → what's defined, what's vague
  4.  Existing coverage        → what's already tested
  5.  Testing layers           → what levels apply
  6.  Shift-left analysis      → what can be caught earlier
  7.  Gap analysis             → what's missing per layer
  8.  Dev overlap check        → what's already in the code
  9.  Ownership & process      → who does what
  10. Environment access       → can I run tests

EXECUTION (while you test):
  11. Test data strategy       → how to create/manage input
  12. Manual execution         → run everything by hand first
  13. Document findings        → capture real values and evidence
  14. Defect management        → file bugs properly
  15. Sign-off                 → what "done" looks like

TRANSITION (after you test):
  16. Regression plan          → what re-runs next sprint
  17. Automation plan          → what to automate
  18. Handoff                  → who's waiting on your results
```

---

## Joining Mid-Project

When you join a project that's already in progress, you run the same 18 steps but the priorities shift. Some things are already decided, some are in-flight, and you're catching up while the train is moving.

```
Joining mid-project vs starting fresh:

  FRESH START:                         MID-PROJECT:
  ┌──────────────────────┐            ┌──────────────────────┐
  │ You define everything│            │ Things already exist: │
  │ from scratch.        │            │ test plan, TCs, maybe │
  │ Steps 1-10 in order. │            │ some executed, some   │
  │                      │            │ passed. People have   │
  │                      │            │ assumptions about     │
  │                      │            │ what's covered.       │
  └──────────────────────┘            └──────────────────────┘
                                       Your job: verify those
                                       assumptions are correct.
```

**What changes when joining mid-project:**

Steps 1-3 (business, system, requirements) become a catch-up exercise. Read everything, ask questions, don't assume the docs are complete or current. The project has context that lives in people's heads, not in the stories.

Step 4 (existing coverage) becomes your most critical step. You need to understand what was tested, by whom, to what standard. Don't trust pass/fail status at face value — understand what was actually verified.

Steps 5-7 (layers, shift-left, gap analysis) are where you add the most value. The team has been heads-down building and testing. A fresh set of eyes sees gaps they've gone blind to. This is your leverage.

Steps 8-9 (dev overlap, ownership) may have informal answers that nobody documented. Ask explicitly. "Who owns UAT?" might get a different answer from different people.

Step 10 (access) is urgent. Start chasing this immediately, in parallel with everything else. Access requests take time and you can't afford to wait.

**The mid-project trap:** You feel pressure to start executing immediately because the sprint is already running. Resist. Spending 2-3 days on Steps 1-10 before executing saves weeks of rework, missed gaps, and "I thought someone else was covering that" conversations.
