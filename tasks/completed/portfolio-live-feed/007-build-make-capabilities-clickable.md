# 007 — Make Capability List Clickable

**Type:** BUILD
**Depends on:** 001

## Requirements
Edit `D:\my_ai_projects\isagawa-co.github.io\index.html` in the Self-Extension section. The "Produced Capabilities" card has a text list:

```
Website Cloner · Attestation Pipeline · Production Test Framework · Autonomous Cycling · Fraud Detection Platform · Healthcare QA · SSH Compliance Testing
```

Convert each capability name into an anchor link:
- **Attestation Pipeline** → `href="attestation.html"` (placeholder — 071 will create this page)
- **SSH Compliance Testing** → `href="ssh-compliance.html"` (placeholder — 072)
- **Healthcare QA** → `href="#"` (no showcase page planned yet)
- **Fraud Detection Platform** → `href="#"` (no showcase page planned yet)
- Others → `href="#"` (placeholders)

Links to pages that don't exist yet use `#` as placeholder. The showcase pages (071-074) will create the actual files later.

Add a new entry: **AI Test Automation** → `href="qa-platforms.html"` (placeholder — 073)
Add a new entry: **Vibe Coder** → `href="vibe-coder.html"` (placeholder — 074)

## Acceptance Criteria
- [ ] `index.html` capability list contains `<a>` tags wrapping capability names
- [ ] At least "Attestation Pipeline" and "SSH Compliance Testing" have non-`#` hrefs
- [ ] "AI Test Automation" and "Vibe Coder" entries added to the list
