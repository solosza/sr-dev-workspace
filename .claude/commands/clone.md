# /clone — Clone a Website

Clone any website into clean HTML + CSS using Playwright MCP browser automation.

## Usage

```
/clone <url>
/clone <url> <output-dir>
```

**Arguments:**
- `<url>` (required): The website URL to clone (e.g., `https://example.com`)
- `<output-dir>` (optional): Where to save the clone. Defaults to `cloned-sites/[domain]/`

## Instructions

1. **Read the skill:** Open and follow `.claude/skills/website-cloner/SKILL.md`
2. **Read extraction reference:** `.claude/skills/website-cloner/references/extraction.md`
3. **Read generation reference:** `.claude/skills/website-cloner/references/generation.md`

## Pipeline Summary

1. Navigate to the URL using `browser_navigate`
2. Take reference screenshots (desktop + mobile)
3. Extract page structure via `browser_snapshot`
4. Extract styles, fonts, colors, images via `browser_evaluate` (JS snippets in extraction.md)
5. Generate clean semantic HTML in `index.html`
6. Generate organized CSS with variables in `styles.css`
7. Download images/assets to `assets/` folder
8. Visual QA: open clone in browser, compare with original screenshots

## Output

```
[output-dir]/
  index.html
  styles.css
  assets/
    images/
    fonts/
```

## Example

```
/clone https://example.com
```

Creates `cloned-sites/example.com/index.html` with a clean HTML/CSS clone of the page.
