# Email Sent to Cousin (RT Domain Expert)

**Date Sent:** 2026-05-26
**To:** [Cousin - RT Partner]
**From:** Alain
**Status:** Awaiting response with domain expertise

---

I took your comments and did a little research and designed an AI automation system specifically for your RT workflow. I want to explain what we're building and let me know if it's different from the solutions that failed before.

---

## The Problem We're Solving

Right now, you're doing this manually: (let me know if any of this is wrong)
1. Patient filtering: Search census one-by-one, check eligibility mentally, write down who qualifies
2. Charting: Copy-paste templates, manually enter data, fill fields that could be auto-populated
3. Billing: Map charting to CPT codes, validate codes are justified, manually submit billing

This takes hours per day and has high error risk, one missed field = denied claim = lost revenue.

Competitors tried to automate this and failed because they didn't understand your compliance rules. They built generic solutions that don't know: (again correct me if im wrong)
- Which diagnoses actually qualify
- What charting justifies each billing code
- When to block billing (incomplete charting)
- Why a patient was rejected (can't defend to CMS)

Result: Their systems are incomplete, don't match your workflow, miss compliance details, and cost more than they save.

---

## What We're Building (In Plain Terms)

We're building a set of three automated commands that you'll run from your computer. Think of it like having an assistant who knows your rules perfectly and can't make mistakes.

### The Three Commands You'll Run:

**1. /rt/filter-patients**
- You: Upload patient census (CSV or point to your EMR)
- System: Automatically checks each patient against your eligibility rules
- You: See list of "qualified," "not qualified (reason)," and "edge cases for manual review"
- Result: No more manual one-by-one searching. 30 patients filtered in 2 minutes.

**2. /rt/chart-patient**
- System: Automatically pulls patient data from your EMR (demographics, vitals, meds, prior charting)
- System: Auto-fills template with that data
- You: Review auto-filled fields, enter only what can't be automated (your assessment, interventions, clinical note)
- You: Click submit
- System: Validates charting is complete before submission
- Result: Charting takes 2 minutes instead of 10. System prevents incomplete submissions.

**3. /rt/submit-billing**
- System: Reads all your charting from the date range
- System: Validates charting is complete (won't submit incomplete records)
- System: Automatically maps your charting to valid CPT codes based on your rules
- System: Shows audit trail (why CPT 94060 was chosen — because charting includes initial assessment)
- System: Submits to billing system or generates file for you
- Result: Billing submitted accurately with full audit trail. Defensible to CMS.

---

## How This Works (Non-Technical Explanation)

### What is "AI-Native"?

Think of it like this: I'm encoding your expertise into a system that runs inside VS Code (the app coders use to write code). It's powered by Claude (an AI assistant) that understands your rules and enforces them automatically.

Here's the flow:
1. You run a command (e.g., /rt/chart-patient 12345)
2. Claude (the AI) reads your rules (we'll document them together)
3. Claude uses Playwright (browser automation software) to navigate your EMR like a person would
4. Playwright clicks buttons, enters data, reads fields — just like you would, but instantly
5. The system validates everything against your rules
6. If something's wrong, it blocks the operation (e.g., "Can't submit billing — charting incomplete")
7. If everything's correct, it completes the operation

Why "AI-Native"? Because the AI is the core engine. It reads your rules, understands context, makes decisions, and never cuts corners. It's not a dumb script that follows steps blindly.

### What is "Playwright Automation"?

Playwright is software that automates web browser interactions. Imagine a robot that:
- Logs into your EMR
- Navigates to the right form
- Reads patient data from fields
- Enters data into other fields
- Clicks submit
- Confirms success

That's Playwright. It does what a human would do, but 100x faster and without mistakes.

---

## Why This Beats Competitors

1. **Rules are visible & auditable**
   - Your rules live in plain-text documents, not hidden in code
   - CMS can see exactly why a patient was billed (rule X applied)
   - Regulations change → we update the rules → done (no code rewrite)

2. **Can't skip compliance**
   - System has "gates" (checkpoints) that block non-compliant operations
   - Can't submit billing without complete charting (gate blocks it)
   - Can't chart ineligible patient (gate blocks it)
   - Competitors let people work around the rules, creating compliance gaps

3. **Self-improving**
   - If a rule is wrong, we update it
   - System learns from each failure
   - Gets better over time

4. **Portable**
   - Deploy to any SNF with the same rules
   - Easy to customize per SNF
   - No rebuilding code for each facility

---

## Now We Need Your Expertise

To build this system, we need to encode your knowledge. That means I ask you questions about your workflow, and we translate your answers into system rules.

Here's what we need:

---

### #1: Patient Filtering — Your Eligibility Rules

**The Question:**
When you look at a patient list, what makes you say "yes, this patient needs RT" vs. "no, skip this one"?

**What we need:** List every rule you use. Examples:
- Age? (must be 18+? any max?)
- Diagnosis? (which diagnoses qualify? COPD, asthma, post-op respiratory, pneumonia, etc.)
- Insurance? (Medicare yes, Medicaid yes, workers comp no?)
- Exclusions? (already getting RT, DNR, palliative care — skip these?)
- Location? (med-surg only, no ICU?)
- Anything else? (weight, comorbidities, prior visits?)

**Why we need it:** The system will check every patient against these rules. If you don't tell us the rules, the system can't automate the decision.

**Format you should send:** Just think out loud. Natural language is perfect.
```
- Age: must be 18+ (no upper limit)
- Diagnosis: COPD, asthma, post-op respiratory, acute pneumonia (NOT COPD exacerbation alone)
- Insurance: Medicare/Medicaid yes, workers comp no, private varies by SNF
- Exclusions: skip if already receiving RT, skip if DNR, skip if palliative
- Location: med-surg and telemetry only, NOT ICU
```

---

### #2: Charting — Your EMR & Template

**The Questions:**

**A) Your EMR System:**
- What system does your SNF use to chart? (Epic? Cerner? Something else?)
- How do you access it? (Web browser? App? Network?)

**B) Data we should auto-pull for you:**
Where in the EMR are these things?
- Patient name, DOB, admit date, room number
- Vital signs (SpO2, heart rate, breathing rate, blood pressure) — where does the monitor feed data?
- Medication list
- Any other data you always need when charting?

**C) Data you must enter (examples):**
- Assessment type (initial, follow-up, discharge, etc.)
- What you observe (breathing effort, oxygen saturation trend, response to treatment, etc.)
- Interventions you provided (nebulizer treatment, oxygen therapy, chest PT, etc.)
- Your clinical note/summary
- Outcome (improved, stable, declined)

**D) Required fields:**
- Which of these fields MUST be filled? (Can't submit without them?)
- Any fields with rules? (e.g., clinical note must be at least 100 characters, assessment type limited to 3 options)

**Why we need it:** The system will auto-fill what it can from your EMR, so you only type what can't be automated. This cuts charting time from 10 minutes to 2 minutes.

**Format:** Just describe where things are. Be specific.
```
EMR: Epic
Access: Web browser, VPN required

Auto-pull:
  - Patient name, DOB from demographics tab
  - Vitals from monitor integration (real-time)
  - Meds from medication list

RT must enter:
  - Assessment type (dropdown: initial, follow-up, discharge)
  - Respiratory findings (free text, must be >50 chars)
  - Interventions (checkboxes: nebulizer, O2, chest PT, etc.)
  - Clinical note (free text, must be >100 chars)
  - Outcome (dropdown: improved, stable, declined)
```

---

### #3: Billing — Your CPT Code Rules

**The Question:**
For each CPT code you bill, what charting must exist to justify that code?

**What we need:** For each code you bill, provide:
- The CPT code number
- What it covers (description)
- What charting must document it
- How often you can bill it (once per stay, daily, weekly?)
- Any special rules (modifiers, prior auth, frequency caps?)

**Why we need it:** The system will automatically map your charting to valid codes. It won't let you bill a code unless the charting supports it. This prevents denials.

**Format:** Just list it out. Examples:
```
CPT 94060 - Initial Respiratory Evaluation
  Requires: Assessment type = "Initial" + respiratory findings documented + clinical note
  Frequency: Once per stay
  Modifiers: -25 if billed same day as another eval

CPT 93000 - EKG
  Requires: SpO2 < 88 OR HR > 110 + charting mentions "EKG ordered"
  Frequency: Daily
  Modifiers: None

CPT 99205 - Established Patient Office Visit
  Requires: [your criteria]
  Frequency: [your frequency]
  Modifiers: [any special rules]
```

---

## One More Thing

**Do your rules change by SNF?**
- If you work at multiple facilities, do all SNFs have the same eligibility rules?
- Or does each one do it differently?

(Helps us know if we build one universal system or customize per facility)

Is there anything else we are missing? If so add it here.

---

## What Happens Next

1. You reply with your answers (rough is perfectly fine)
2. I translate your answers into system rules
3. I run my platform that generates 70%+ of the code automatically
4. We review the auto-generated system and say "yes that's right" or "no, change this"
5. We customize the remaining 30% based on your feedback
6. Test at your SNF when we're done.

**Total timeline: 6-8 weeks from now to a working system. Most likely sooner. I can have our system coded up to 70% done probably within a week. We would just need to fine tune and iterate through the rest until we get it right.**

---

## Why This Matters

The three companies that tried this before failed because: (is this correct?)
- They didn't have a respiratory therapist building it
- They guessed at the rules instead of asking you
- Their systems had gaps in compliance
- They couldn't explain why the system made decisions (bad for CMS reviews)

You're different. You know the rules perfectly. You've run these programs. You know what breaks and why. That's worth a lot.

By encoding your expertise into a system, we make it:
- Portable (deploy to other SNFs)
- Defensible (CMS can see every decision)
- Updatable (regulations change → update rules → done)
- Profitable (scales without adding staff)

---

## Send Your Answers

Just reply to this email with what you know. If you're not sure about something, say so, we can figure it out together.

Let's do this!

**Also, I'm assuming I'm going to get an equity stake in this, right?**

Regards,
Alain

---

## Summary

- **Email Status:** Sent
- **Awaiting:** Cousin's response with domain expertise (eligibility rules, charting requirements, CPT code mappings)
- **Next Step:** Once cousin responds, translate answers into system rules and create backlog item for execute-pipeline
- **Equity Question:** Addressed in email — waiting for discussion
