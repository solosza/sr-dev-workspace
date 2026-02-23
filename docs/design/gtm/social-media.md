# Social Media GTM Content

Launch content for Isagawa QA Platform across LinkedIn, Reddit, Twitter, and Product Hunt.

---

## 1. LinkedIn Post (200-300 words)

**Target:** Engineering managers, QA leads, SDETs

---

AI can generate tests. But the output is inconsistent, hard to maintain, and impossible to scale.

Solving this requires building agent harnesses that enforce consistency — bespoke engineering most teams don't have in-house, and no commercial tool provides.

I built an enforcement system that manages how AI works — so every test follows a Screenplay-inspired architecture automatically, streamlined with fewer abstractions and a dedicated WebInterface layer. The AI can only do it right.

This isn't AI governance. It's AI execution management.

I deliver a highly scalable, maintainable, enterprise-grade test automation framework powered by an AI agent managed by my own enforcement kernel. I build the entire test solution — login credentials, data management, environment configuration, and page object architecture. Your team owns the entire tech stack: a true AI-native test automation framework built on Claude Code. I also train your team to create and maintain test scripts on their own.

What I deliver:
-> Login/auth credential management
-> Test data management
-> Environment configuration
-> Page object architecture
-> AI-powered test generation with human-in-the-loop pair programming
-> Training so your team owns it

Open source: github.com/isagawa-qa/platform
See it in action: Watch the demo pinned in my Featured section

DM "demo" — I build working tests on YOUR site in 60 minutes. You keep the code.

---

## 2. Reddit Posts (4 subreddits)

### r/QualityAssurance

**Title:** Open-sourced our AI-native QA framework — enforces test architecture so AI-generated tests are actually maintainable

---

I've been using Claude Code to generate Selenium tests for about six months. The velocity was incredible — until month three, when I realized the codebase was unmaintainable. Every test was structured differently. The AI would "forget" patterns between sessions.

I tried docs. I tried detailed prompts. Nothing stuck.

So I built enforcement at the agent level and today I open-sourced the entire thing.

**The architecture (Screenplay-inspired, 5 layers):**

```
Test (Arrange / Act / Assert)
  └─> Role (multi-task workflow, user persona)
       └─> Task (single domain operation)
            └─> Page Object (one page, atomic actions, fluent API)
                 └─> BrowserInterface (Selenium wrapper, waits, logging)
```

**How enforcement works:**

Every action the AI takes is validated against the architecture rules before code is written. If the AI tries to put locators in a test file, or skip decorators, or mix business logic into page objects — the action is blocked and the AI is told exactly how to fix it.

When a test fails, the system captures the root cause and prevents that failure mode permanently. By session 10, 15+ mistake categories can't happen again.

**Why this matters:**

If you're using AI for test automation, you're probably hitting the same wall — the AI is fast, but the output drifts. This gives you a way to lock in quality without constant human review.

**What you get:**
- 5-layer Screenplay-inspired architecture
- Reference implementations for every layer
- Runtime enforcement — AI can't violate architecture
- Self-improving — gets smarter after every failure
- Human-in-the-loop pair programming model

Repo: github.com/isagawa-qa/platform
MIT license, Python + Selenium + pytest

DM me or email alain@isagawa.co if you want a free demo on your site.

---

### r/selenium

**Title:** 5-layer Screenplay-inspired Selenium architecture with AI-powered test generation (open source)

---

I've been building Selenium frameworks for years, and the same problem always comes up: tests get brittle, PageObjects get bloated, and maintenance becomes a full-time job.

Then I started using AI to generate tests. The speed was incredible, but it introduced a new problem: **consistency**. The AI would write tests differently every session. Some put waits in PageObjects. Some put selectors in test files. After three months, the codebase was chaos.

So I built an enforcement layer — and today I open-sourced it.

**The architecture (5 layers, Screenplay-inspired):**

```
Test (assertions only)
  └─> Role (workflow orchestration — coordinates Tasks)
       └─> Task (domain operation — one logical action)
            └─> Page Object (locators as class constants, atomic methods, fluent API)
                 └─> BrowserInterface (Selenium wrapper — click, type, wait, navigate)
```

**Key rules:**
- Locators live *only* in Page Objects — never in Tasks, Roles, or Tests
- Tasks and Roles never return values — Tests assert through POM state-check methods
- `@autologger` decorator on every Task, Role, and Test method
- Page Objects return `self` for fluent chaining

**Example:**

```python
# framework/pages/login_page.py
class LoginPage:
    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, browser: BrowserInterface):
        self.browser = browser

    def enter_email(self, email):
        self.browser.type(*self.EMAIL_INPUT, email)
        return self

    def click_submit(self):
        self.browser.click(*self.SUBMIT_BTN)
        return self

    def is_logged_in(self):
        return self.browser.is_element_displayed(*self.DASHBOARD_HEADER)
```

```python
# tests/test_login.py
@autologger.automation_logger("Test")
def test_successful_login(self):
    self.user_role.login_and_verify(email, password)
    assert self.login_page.is_logged_in()
```

**AI enforcement:**

The framework includes a system that validates every file the AI writes against the architecture rules. If the AI puts locators in a test file or skips decorators, the write is blocked. It physically can't create violations.

**Repo:** github.com/isagawa-qa/platform (MIT license)

If you're interested in the pattern but not the AI part, the architecture still applies — it's standard Screenplay-inspired POM with strict layer boundaries.

---

### r/softwaretesting

**Title:** Built a self-improving QA agent — learns from every test failure and never repeats mistakes

---

I've been using AI to write Selenium tests for six months. The productivity was unreal — what used to take a day now takes 20 minutes.

But I hit a problem: **the AI doesn't remember**. Every session, it would make the same mistakes. Put selectors in test files. Skip waits. Forget naming conventions.

So I built a self-improving system. Today I open-sourced the whole thing.

**How it works:**

1. **Agent generates tests** following a 5-layer Screenplay-inspired architecture
2. **Architecture is enforced at runtime** — if the AI tries to violate layer boundaries, the action is blocked before code is written
3. **Test runs** — if it fails, the system captures the root cause
4. **Lesson is captured permanently** — that failure mode can never happen again
5. **Next session** — the system is smarter. Enforcement is tighter.

**Example:**

We had a bug where tests would fail intermittently because the AI wasn't waiting for elements to be visible. After the fix, the lesson was captured:

- "Always use BrowserInterface wait methods before interacting with dynamic elements"
- The system now blocks any code that uses `time.sleep()` or skips visibility waits

That failure mode is permanently impossible.

**Why this matters:**

Most QA frameworks are static. They encode what you knew on Day 1. This framework evolves — every failure makes it permanently smarter.

**Human-in-the-loop:**

This isn't autonomous AI. It's pair programming. After a test failure, the system proposes a fix. You review and approve. Then it's enforced permanently. You're always in control.

**Repo:** github.com/isagawa-qa/platform
Stack: Python, Selenium, pytest, Claude Code
License: MIT

DM me or email alain@isagawa.co — I offer free demos on your actual site. You keep the code.

---

### r/ClaudeAI

**Title:** Built an enforcement system on Claude Code that prevents AI from violating architecture patterns

---

I've been using Claude Code for test automation, and it's been incredible — until the codebase hit about 200 files. Then I noticed:

- Every session, Claude would "forget" our architecture patterns
- Some tests put selectors in test files, some in PageObjects
- Some used waits, some didn't
- Naming conventions drifted constantly

I tried adding detailed instructions to CLAUDE.md. It helped for one session, then drifted again.

So I built an enforcement system that gates every action Claude takes — and today I open-sourced it.

**What it does:**

Before Claude writes any file, the system validates the content against architecture rules. If there's a violation — wrong layer, missing decorator, locator in the wrong place — the write is blocked. Claude gets a clear message explaining what's wrong and how to fix it.

After Claude runs tests, if a test fails, the system captures the lesson. That failure mode is prevented in all future sessions. The enforcement gets tighter over time, not looser.

**The result:**

By session 10, 15+ mistake categories are permanently prevented. Claude can't:
- Put locators outside Page Objects
- Skip `@autologger` decorators
- Use `time.sleep()` instead of proper waits
- Import from the wrong layer
- Skip reference implementations before writing code

**The architecture it enforces (5 layers):**

```
Test → Role → Task → Page Object → BrowserInterface
```

Each layer has strict boundaries. Claude can't cross them.

**Why not just CLAUDE.md?**

CLAUDE.md is suggestions. This is enforcement. CLAUDE.md says "please follow these patterns." This system says "you cannot violate these patterns." The difference is night and day for long-term codebase quality.

**Repo:** github.com/isagawa-qa/platform

We use it for QA, but the pattern applies to any domain where you need AI to produce consistent, maintainable output.

MIT license. Built on Claude Code.

---

## 3. Twitter/X Thread (8 tweets)

> **TODO:** Create @isagawa X account with Premium (business expense). Posts are drafted and ready.

**Thread:**

---

**Tweet 1 (Hook):**

AI can generate tests. But the output is inconsistent, hard to maintain, and impossible to scale.

Solving this requires agent harnesses most teams can't build — and no commercial tool provides.

Here's how we solved it (open source):

---

**Tweet 2:**

AI governance tools monitor, document, and alert.

They watch the AI work, log what happened, and tell you when something goes wrong.

That's useful. But it doesn't stop the AI from doing the wrong thing in the first place.

---

**Tweet 3:**

The real problem: AI doesn't remember.

Every session, it forgets your patterns. Docs drift. Code quality degrades. After 3 months, your codebase is unmaintainable.

Monitoring tells you it happened. It doesn't prevent it.

---

**Tweet 4:**

What if the AI couldn't make mistakes?

Not "we'll review it later."
Not "we'll train it better."
But: the system blocks bad code at runtime, before it's written.

That's AI Execution Management.

---

**Tweet 5:**

We built a 5-layer Screenplay-inspired architecture:

Test → Role → Task → Page Object → BrowserInterface

Every layer has strict boundaries. The AI can't cross them. Locators only in POMs. Decorators required. No time.sleep().

The enforcement is automatic and self-improving.

---

**Tweet 6:**

When a test fails, the system captures the root cause and prevents it permanently.

By session 10: 15+ mistake categories are impossible to repeat.

Static rules don't do this. Self-improving enforcement does.

---

**Tweet 7:**

Open-sourced today. MIT license.

- Screenplay-inspired 5-layer architecture
- Runtime enforcement
- Self-improving quality
- Human-in-the-loop pair programming
- Python + Selenium + pytest

Repo: github.com/isagawa-qa/platform

---

**Tweet 8:**

If you're using AI to write code — any code — you'll hit this wall.

The AI is fast. The output drifts. Maintenance becomes impossible.

I offer free 60-min demos on your actual site. You keep the code.

DM me or email alain@isagawa.co

---

## 4. Product Hunt Listing

### Title:
Isagawa QA — AI Execution Management for Test Automation

### Tagline:
AI that can only do QA right — enforced at runtime, not monitored after the fact

### Description:

**The Problem**

AI can generate tests in seconds. But the output is inconsistent, hard to maintain, and impossible to scale. Every session, the AI forgets your patterns. Code quality degrades. After three months, your codebase is unmaintainable.

Documentation doesn't help. The AI reads it once, then drifts. Code review catches mistakes too late. Traditional governance tools monitor what happened — they don't prevent it.

Solving this requires building agent harnesses that enforce consistency — bespoke engineering most teams don't have in-house, and no commercial tool provides.

**The Category: AI Execution Management**

We're not building AI governance (monitoring, documentation, alerts). We're building **AI Execution Management** — enforcement at the point of execution.

The system doesn't watch the AI work. It controls how the AI works. Every action is validated against architecture rules before code is written. If the AI tries to violate a pattern, the action is blocked. The AI physically can't create bad code.

When a test fails, the system captures the root cause and prevents that failure mode permanently. The enforcement gets smarter with every session.

**5-Layer Screenplay-Inspired Architecture**

```
Test → Role → Task → Page Object → BrowserInterface
```

Every layer has strict boundaries. Locators only in Page Objects. Decorators required on every method. No time.sleep(). Tests interact through Roles only.

The AI can't violate these rules. They're enforced at runtime.

**What You Get**

- 5-layer Screenplay-inspired architecture (Python + Selenium + pytest)
- Reference implementations for every layer
- Runtime enforcement — AI can't violate architecture
- Self-improving — gets smarter after every failure
- Human-in-the-loop pair programming model
- MIT license — you own everything

**Services**

I deliver a highly scalable, maintainable, enterprise-grade test automation framework. I build the entire test solution and train your team to own it.

Free 60-minute demo on your site. You keep the code.

---

### First Comment (Maker):

Hey Product Hunt! I'm the maker of Isagawa QA.

**The "aha" moment:**

Six months ago, I started using Claude Code to automate Selenium tests. The first month was magic — what used to take a day took 20 minutes. By month three, the codebase was chaos. Every test looked different. The AI would forget my architecture between sessions.

I tried documentation. I tried detailed prompts. Nothing stuck.

Then I realized: I was managing AI like I manage humans. With docs, reviews, and hope.

But AI doesn't work like humans. It doesn't remember. It doesn't learn implicitly. It needs enforcement at the execution layer.

So I built a system that gates every action the AI takes, validates against architecture rules, and captures lessons permanently. The AI can't skip steps. It can't drift from patterns. It can only do QA right.

**What's next:**

The enforcement pattern is domain-agnostic. We built it for QA, but it applies to any domain where AI needs to produce consistent, maintainable output:
- API test automation
- Frontend testing
- Data pipelines
- Any codebase where AI generates code

The category we're creating — **AI Execution Management** — is bigger than QA. It's the missing layer between your AI and your code.

Free demo: DM me or email alain@isagawa.co. I'll build working tests on your site in 60 minutes. You keep the code.
