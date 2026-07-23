# platform-hybrid Finalize + Private Push (Factory Step 12, Supervised)

## Status
Open (in progress — supervised, partially staged)

## Priority
High — platform-hybrid's spec is built (factory steps 1-11) and the framework is staged; this closes it out into a real, private, clean-room standalone platform. It's the generic base the whole product line builds toward, then customizes per client.

## Summary
Complete the factory's Step 12 (Package + Push) for platform-hybrid, supervised, ending in a **private** `isagawa-qa/platform-hybrid` repo. This was being done ad-hoc outside a backlog; capturing it. platform-hybrid = the generic, clean-room, standalone multi-transport QA platform (framework + governance spec + Orderly demo) — the **product/asset** the line is built toward; HMSA (and future clients) are private *customizations* of it. The framework is copied from the proven base and must be sanitized clean-room (zero client tokens) before any push.

## State so far (this session, supervised)
- Factory steps 1-11 complete: governance spec (workflow.md, gate-contract.md, step files, commands, lessons), `_test/validation-report.json` (15 PASS / 0 FAIL / 16 DEFERRED — the deferred gates resolve at packaging).
- Framework copied into `output/platform-hybrid/framework/` (caches/.pyc/.db excluded).
- Client leaks identified (small): a few `HMSA`/`QNXT` mentions in `docs/5-layer-contract.md` + a `grid_component.py` comment + hardcoded `hmsa-qa-platform` test paths + one `_reference/__init__.py` docstring. The clean-room lexicon test names tokens by design (checker, excluded).
- NOTHING pushed; repo does not exist yet.

## Requirements
- **Sanitize clean-room:** strip every real client token from the packaged framework — genericize the `5-layer-contract.md` HMSA/QNXT references, the `grid_component.py` comment, and the `_reference/__init__.py` docstring; make the hardcoded `hmsa-qa-platform` test paths generic/configurable. Keep generic commerce terms (Orderly, "eligible orders") — they are not leaks.
- **Zero-leak verification (hard gate):** grep the ENTIRE `output/platform-hybrid/` for client identifiers (`hmsa|qnxt|healthcare|insurance|member|patient|subscriber|eligib`-as-domain) → must be zero real hits (excluding checker files that name tokens by design). The orchestrator verifies this independently before any push.
- **Package:** write the README (per factory `references/readme-template.md`), verify YAML frontmatter on skill/command files, resolve the deferred gates that packaging owns (framework present, demo present, tests wired).
- **Private push:** `gh repo create isagawa-qa/platform-hybrid --private --source=. --push` (QA org, **private** per owner; NOT the factory default `isagawa-co/{domain}-spec`). The push is outward-facing/irreversible — requires the owner's explicit sign-off AFTER the zero-leak proof.
- **Runner bug caveat:** the factory runner (run-spec-factory.sh) false-fails on empty-output (see 281) and its step-11 skip-check reads `g['status']` vs the report's `g['result']` — so Step 12 won't auto-advance; do it supervised/manually, not by re-running the raw pipeline.

## References
- `domain-spec-factory/.claude/skills/spec-factory/steps/step-12.md` (package+push spec — defaults to `isagawa-co/{domain}-spec --private`; override to `isagawa-qa/platform-hybrid`)
- `domain-spec-factory/output/platform-hybrid/` (staged output + `_test/validation-report.json`)
- Base: `hmsa-qa-platform/framework` (the proven framework being packaged, clean-room already except the flagged residuals)
- `docs/backlog/281-kernel-fix-factory-runner-empty-output-hardening.md` (the runner bug that makes auto-step-12 unreliable)

## Task Builder Input
- **Deliverable:** A private `isagawa-qa/platform-hybrid` repo — full standalone platform (framework + governance spec + Orderly demo + README), clean-room verified (zero client leaks), pushed after owner sign-off.
- **Location:** new-repo:isagawa-qa/platform-hybrid (private)
- **Scope:** BUILD
- **Constraints:** SUPERVISED — clean-room sanitization + zero-leak verification done/verified by the orchestrator (not trusted to a headless runner), and the push gated on the owner's explicit sign-off after the zero-leak proof. Private repo (owner directive). Keep the meta-factory that built it private — only platform-hybrid (clean-room) is the shareable asset.
