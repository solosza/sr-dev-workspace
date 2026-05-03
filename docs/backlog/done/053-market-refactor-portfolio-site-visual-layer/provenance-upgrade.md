# Provenance Section Upgrade

## Status
EXISTS (needs enhancement)

## Location
`D:\my_ai_projects\isagawa-portfolio-site\index.html` + `styles.css`

## Changes

### Third attestation card
- Embed #047 bundle from `.claude/state/attestations/047-20260426T071022Z.json`
- Add as `<script type="application/json" id="attestation-bundle-3">`
- Add third `.attestation-card` div with `data-bundle="attestation-bundle-3"`
- Rekor index: #1387966928

### Attestation grid
- Desktop: `grid-template-columns: repeat(3, 1fr)` (was 2)
- Mobile: single column (unchanged)

### Subtitle text
- `font-size: clamp(1.125rem, 2vw, 1.375rem)`
- `color: var(--text-secondary)`
- `max-width: 60ch`

### Verification badge pulse
```css
@keyframes badge-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.7; }
}

.verification-badge--verified {
  animation: badge-pulse 1.5s ease-in-out infinite;
}
```
Makes the verified state feel live rather than static.
