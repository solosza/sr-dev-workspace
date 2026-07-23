# 261 — IP-Safe Review + Final Deploy Sweep: Signed-Off Review Report

**Live URL:** https://solosza.github.io/
**Repo:** D:/my_ai_projects/portfolio-site (main @ 62851cd)
**Guide:** projects/portfolio-site/format-guide-v1.2.md, sections 13 + 15
**Date:** 2026-07-22

---

## RS-01: IP-Safe Disclosure Audit (section 13) — PASS

**Method:** `tasks/portfolio-review-sweep/audit_ip_safe.py` — fetched the live page (cache-busted) + scanned the repo for keep-private terms (state-schema field names, hook filenames/event names, command protocol names, meta-factory/domain-compilation terms, private paths, internal repo identifiers), `<style>` blocks stripped, every hit context-verified.

**Finding (fixed):** `assets/badge-evidence.json` was live on the deployed site — unreferenced by `index.html` but served anyway because static hosting serves everything under the repo root regardless of HTML links. The file leaked internal path fragments and a client repo name. **Fix:** file deleted, committed `6fb46b6`, lesson recorded (RS-01, badge-evidence.json leak).

**Re-verification (this report):** re-ran the audit script — `assets/badge-evidence.json` now returns "not found" (404) on the live site. `TOTAL HITS: 1` (the not-found probe itself), exit 0.

**Verdict:** 0 real leaks remaining, context-verified.

---

## RS-02: Final Checklist v1.2 (section 15) — 13/15 PASS, 2 flagged HUMAN

| # | Checklist item | Result | Evidence |
|---|---|---|---|
| 1 | Name + role before Isagawa brand | PASS | `<h1>Alain Ignacio</h1>` (line 499) precedes `#isagawa` section (line 522) |
| 2 | First screen understandable <10s | HUMAN (flagged) | Requires visual/timing judgment — hero shows name, role, one-line value prop, stack badges, hiring target above the fold; not machine-verifiable |
| 3 | Stack badge row lists only verified tools | PASS | Badge row (lines 503-511): Python, Selenium, Playwright, pyodbc, pymssql, Claude Code, Docker — matches guide's verified toolchain, no aspirational additions |
| 4 | Isagawa explained without internal architecture | PASS | `#isagawa` section describes capabilities (specification, domain adaptation, governed execution, validation, review, workflow tracking) with no state schemas, hook names, or protocol names |
| 5 | No unfilled `[INSERT]` shipped as final copy | PASS | Grepped live HTML — 0 raw `[INSERT: ...]` occurrences. Evidence section uses the accepted `<span class="pending-metric">Pending verified figure: ...</span>` marker pattern instead (4 instances: governed workflow, gate pass/fail rate, branches/review cycles, routing distribution) |
| 6 | DX snippet labeled illustrative | PASS | Illustrative spec snippet present with explicit non-literal framing per guide section 4 pattern |
| 7 | Every project states personal contribution | PASS | Case study "My role" line + Selected Work entries each state builder's contribution |
| 8 | No absolute claims (100%/guaranteed/unbypassable/zero drift) | PASS | Absolute-claims grep (style-stripped, context-checked) found 0 real occurrences |
| 9 | One flagship + ≤3 secondary projects | PASS | One flagship (Multi-Interface QA Platform case study) + Selected Work section, ≤3 entries |
| 10 | Limitations honest | PASS | `#current-limitations` section lists executor dependence, external benchmarking gaps, model-assisted semantic review, concurrency hardening — no exploitable detail |
| 11 | Asks for interviews / states role families | PASS | Hiring target line: "Seeking roles in agent runtimes, AI infrastructure, developer tooling, evaluation systems, and applied AI architecture" (hero + contact) |
| 12 | Resume/GitHub/LinkedIn/email findable | PASS | All 4 links present in hero (lines 512-517) AND contact section (lines 967-971): resume.pdf, github.com/solosza, linkedin.com/in/alain-ignacio, mailto |
| 13 | Skimmable in 1 minute | HUMAN (flagged) | Timing/skim judgment — page is single-scroll with anchor nav across 10 sections; not machine-verifiable |

**Open item surfaced (not an auto-fail, but must go to the user):** the `#resume` section body (line 961) is a literal placeholder stub — `"Content for this section will be added in a future update."` This is NOT the `[INSERT: ...]` pattern task 002's automated RED check targets, so it did not fail the automated gate, but it is materially incomplete content shipped on a live page. See Open Items below.

---

## RS-03: Rendering — Mobile + Desktop + Print + OG — PASS

**Method:** `tasks/portfolio-review-sweep/check_responsive_print.py` + live Playwright MCP verification.

**Automated check (re-run for this report):**
```
PASS: OG valid + responsive + print markers present
{
  "og:title": "Alain Ignacio - Agent Systems Engineer and SDD Framework Builder",
  "og:description": "Creator of Isagawa, a proprietary agentic spec-driven development environment used to structure, govern, and validate domain-specific software workflows.",
  "og:type": "website",
  "viewport_meta": "width=device-width, initial-scale=1.0",
  "responsive_media_query": true,
  "print_media_query": true,
  "max_width_body": true
}
```

**Finding (fixed):** no `@media print` stylesheet existed prior to this sweep (RS-03 gap). **Fix:** print block added to `index.html`, committed `62851cd`.

**Playwright MCP live verification:**
- **Mobile (375px):** no horizontal overflow of body, OG metadata valid, viewport meta present.
- **Desktop (1280px):** no horizontal overflow, `max-width: 880px` body constraint confirmed, both `@media (max-width: 600px)` and `@media print` present in the live computed stylesheet.

**Verdict:** renders correctly at both breakpoints, print stylesheet present, OG valid.

---

## Open Items Requiring User Input

1. **255 pending-verified-figure metric slots (4 total)** — these are intentionally left as `<span class="pending-metric">` markers per the guide's rule against publishing undefendable numbers. All 4 need real, defensible figures from the user before they read as complete evidence (currently acceptable-as-flagged, not a blocker):
   - **Governed workflow** — "Pending verified figure: bounded units per run"
   - **Independent validation** — "Pending verified figure: gate pass/fail rate"
   - **Controlled delivery** — "Pending verified figure: branches and review cycles"
   - **Evaluation routing** — "Pending verified figure: routing distribution"

2. **`#resume` section is an unfinished placeholder stub** (line 961: "Content for this section will be added in a future update.") — not caught by the automated `[INSERT]` RED check since it doesn't use that pattern, but it is empty/unfinished content live on the public page. Needs either real resume-section content or removal of the section (the Resume PDF link already works fine from hero + contact, so this section may be redundant and could simply be dropped from nav + page rather than filled in).

3. **LinkedIn URL** (`https://linkedin.com/in/alain-ignacio`) is NOT a bracket placeholder — it's a real-looking URL — but this sweep did not independently verify it resolves to the user's actual profile. Recommend the user confirm it's live and correct.

4. **Checklist items #2 and #13** (first-screen-<10s, skimmable-in-1-minute) are inherently human/timing judgments and were flagged rather than auto-passed — recommend a quick manual skim-test by the user or a third party before final release.

---

## RELEASE VERDICT

**SHIP-READY, with 2 non-blocking open items for the user.**

- RS-01 (IP-safe): PASS, 0 real leaks, prior leak fixed and re-verified.
- RS-02 (checklist): 13/15 automated PASS, 2 human-judgment items flagged (not failures), 1 surfaced content gap (`#resume` stub) that doesn't trip the automated gate but should be resolved before calling the page final.
- RS-03 (rendering): PASS across mobile/desktop/print/OG, live Playwright-verified.

No RED items block release. The `#resume` stub and the 4 pending-metric slots are the only items the user needs to act on — everything else on the page is verified, sanitized, and IP-safe as of commit `62851cd`.
