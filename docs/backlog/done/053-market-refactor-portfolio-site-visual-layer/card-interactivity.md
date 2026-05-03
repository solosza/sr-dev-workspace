# Card Depth + Interactivity

## Status
EXISTS (needs enhancement)

## Location
`D:\my_ai_projects\isagawa-portfolio-site\styles.css`

## Applies to
- `.evidence-card` (Seed x4, Growth x3, Self-Extension x3)
- `.attestation-card` (Provenance x3)

## Current
- `background: var(--card-bg)`
- `border: 1px solid var(--card-border)`
- No hover effects

## Target
```css
.evidence-card,
.attestation-card {
  transition: transform 250ms ease, border-color 250ms ease, box-shadow 250ms ease;
  border-top: 1px solid var(--border-subtle);
}

.evidence-card:hover,
.attestation-card:hover {
  transform: translateY(-2px);
  border-color: rgba(252, 249, 243, 0.3);
  box-shadow: 0 4px 24px rgba(252, 249, 243, 0.06);
  border-top-color: var(--accent);
}
```
