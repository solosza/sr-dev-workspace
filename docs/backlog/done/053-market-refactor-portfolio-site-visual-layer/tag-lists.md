# Tag Lists Above Card Titles (Suero Pattern)

## Status
NEW

## Location
`D:\my_ai_projects\isagawa-portfolio-site\index.html` + `styles.css`

## What
Add a small tag line above each evidence card title. Communicates that each card is a typed/categorized concept.

## HTML
Add `<span class="card-tags">GOVERNANCE / PROTOCOL / TOKEN</span>` before each card's `<h3>`.

## Tag Content

### Seed cards
| Card | Tags |
|------|------|
| Anchor Token | GOVERNANCE / PROTOCOL / TOKEN |
| Gate Enforcer | HOOK / RUNTIME / WRITE-GATE |
| Learn Loop | LESSONS / MECHANICAL / PERSISTENCE |
| Session Protocol | STATE / LIFECYCLE / RECOVERY |

### Growth cards
| Card | Tags |
|------|------|
| Domain Specs | VERTICALS / CORPUS / CONVERSATIONAL |
| Spec Factory Steps | PIPELINE / COMPILER / MECHANICAL |
| Workspaces | ENVIRONMENTS / GOVERNANCE / INHERITANCE |

### Self-Extension cards
| Card | Tags |
|------|------|
| Task Builder | DECOMPOSITION / VERIFICATION / AUTONOMOUS |
| Website Cloner | EXTRACTION / PLAYWRIGHT / DESIGN-TOKENS |
| Attestation Pipeline | SIGSTORE / REKOR / CRYPTOGRAPHIC |

## CSS
```css
.card-tags {
  display: block;
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  letter-spacing: 0.1em;
  color: var(--text-secondary);
  text-transform: uppercase;
  margin-bottom: 0.5rem;
}
```
