# 005 — Write qa-platforms.js

**Type:** BUILD
**Depends on:** 003

## Goal
Write the JavaScript file for the QA platforms showcase page at `D:\my_ai_projects\isagawa-co.github.io\qa-platforms.js`.

## Requirements

1. **Terminal animation** — simulate a conversation where a user describes a test in plain English and the AI agent generates 4-layer test code:
   - Line 1: `$ describe "As a registered user, I want to login with valid credentials"`
   - Line 2: `> Discovering page elements...`
   - Line 3: `> Generating LoginPage (Page Object)...`
   - Line 4: `> Generating AuthTasks (Task)...`
   - Line 5: `> Generating RegisteredUser (Role)...`
   - Line 6: `> Generating test_valid_login (Test)...`
   - Line 7: `✓ 4 files generated. Running pytest...`
   - Line 8: `tests/auth/test_login.py::test_valid_login PASSED`
   - Typewriter effect with delays between lines

2. **Attested counter** — fetch `feed-count.txt` and update nav counter (same as attestation.html)

3. **Scroll reveal** — IntersectionObserver for `.reveal` class elements (same pattern as ssh-compliance.js)

Reference: `D:\my_ai_projects\isagawa-co.github.io\ssh-compliance.js` for terminal animation and scroll reveal patterns

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-co.github.io\qa-platforms.js` exists with terminal animation, counter fetch, and scroll reveal
