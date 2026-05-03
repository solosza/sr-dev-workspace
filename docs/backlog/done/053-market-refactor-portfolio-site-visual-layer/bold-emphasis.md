# Bold Word Emphasis (Suero Pattern)

## Status
NEW

## Location
`D:\my_ai_projects\isagawa-portfolio-site\index.html`

## What
Wrap load-bearing phrases in `<strong>` tags inside existing prose paragraphs. Suero uses bold words inside normal sentences to create reading rhythm and visual anchors.

## Changes (HTML only)

### Hero p (line 30)
- Bold **"natural language"**
- Bold **"become part of the factory"**
- Bold **"loop closes"**

### Seed narrative (line 38)
- Bold **"four mechanisms"**
- Bold **"cannot be bypassed"**

### Growth narrative (line 65)
- Bold **"None of this was hand-coded"**
- Bold **"compile natural language into structured specs automatically"**

### Self-Extension narrative (line 90)
- Bold **"loop becomes visible"**
- Bold **"producing itself"**

### This Page narrative (line 114)
- Bold **"built by the system it describes"**
- Bold **"produced from conversational intent, including this one"**

## CSS
```css
.anchor-section__narrative strong,
#hero p strong {
  font-weight: 700;
  color: var(--text-primary);
}
```

The surrounding prose is `--text-secondary`; the bolds pop at `--text-primary`.
