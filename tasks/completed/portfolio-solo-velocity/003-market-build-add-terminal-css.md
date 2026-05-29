# Build: Add Terminal CSS Modifier Classes

**Type:** BUILD
**Phase:** 2
**Depends on:** 002

## Goal

Add 3 new terminal line modifier classes to `D:\my_ai_projects\isagawa-co.github.io\styles.css`. These are needed by the Section 6 provenance terminal in story.html.

## Existing classes (already in styles.css, lines 751-762):
- `.terminal__line--prompt` — accent color
- `.terminal__line--success` — badge text color
- `.terminal__line--emphasis` — white + bold

## Classes to Add

Insert immediately after `.terminal__line--emphasis` block (after line 762):

```css
.terminal__line--user {
  color: var(--text-secondary);
  opacity: 0.85;
}

.terminal__line--hash {
  color: var(--accent);
  opacity: 0.6;
  font-size: 0.9em;
}

.terminal__line--comment {
  color: var(--text-secondary);
  opacity: 0.5;
  font-style: italic;
}
```

## File to Edit

`D:\my_ai_projects\isagawa-co.github.io\styles.css`

## Acceptance Criteria
- [ ] `.terminal__line--user` class exists in styles.css
- [ ] `.terminal__line--hash` class exists in styles.css
- [ ] `.terminal__line--comment` class exists in styles.css
- [ ] No existing classes modified
