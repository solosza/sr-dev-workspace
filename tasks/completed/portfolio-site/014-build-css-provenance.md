# Add Provenance Section CSS

## Context
The provenance section needs distinct styling: attestation cards with intent-led layout, verification badges, action buttons, and an expandable JSON viewer. The design emphasizes that intent text leads — it's the first thing the visitor sees in each card.

## Type
BUILD

## Execution
inline

## Dependencies
- 013-build-js-rekor-verification

## Phase Gate
- [ ] Provenance HTML and JS written in `index.html`

## Requirements
- Edit `D:\my_ai_projects\isagawa-portfolio-site\styles.css`
- Add CSS for:
  - `#provenance` — section padding, max-width container
  - `.attestation-cards` — flex or grid layout for 2 cards side by side (stack on mobile)
  - `.attestation-card` — card styling using existing `--card-*` tokens, left accent border
  - `.intent-text` — large, prominent text (leads the card). Font: `--font-body`, size: `--text-lg`, color: `--text-primary`
  - `.attestation-meta` — metadata row, mono font, muted color, small text
  - `.verification-badge` — inline badge with green/amber variants
  - `.verification-badge--verified` — green tint (`--badge-workspace-*` tokens)
  - `.verification-badge--pending` — amber tint (`--badge-operate-*` tokens)
  - `.attestation-actions` — flex row with two action buttons/links
  - `.attestation-actions a, .attestation-actions button` — mono font, accent color, transparent bg
  - `.bundle-viewer` — hidden by default, monospace pre block, overflow scroll, bg-elevated
  - `.bundle-viewer.open` — display block
- All styles use existing CSS custom properties

## Acceptance Criteria
- [ ] `styles.css` contains `.attestation-card` styles
- [ ] `styles.css` contains `.intent-text` styles
- [ ] `styles.css` contains `.verification-badge` styles
- [ ] `styles.css` contains `.bundle-viewer` styles

## Gates Satisfied
- BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
