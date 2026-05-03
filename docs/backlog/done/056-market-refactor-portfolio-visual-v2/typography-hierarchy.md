# Typography Hierarchy

## Status
NEW

## Changes

### Hero h1
- Size: `clamp(4rem, 9vw, 8rem)`
- Weight: 700
- Letter-spacing: `-0.04em`
- Line-height: `0.95`
- Linear gradient text: `#fcf9f3` to `#dcdce8` via `background-clip: text`

### Hero h2
- Size: `clamp(1.25rem, 2vw, 1.5rem)`
- Weight: 400
- Color: `--text-secondary`
- Max-width: `50ch`

### Hero p
- Add `max-width: 55ch`

### Section h2 titles
- Size: `clamp(2.75rem, 5.5vw, 5rem)`
- Weight: 600
- Letter-spacing: `-0.025em`
- Line-height: `1.0`

### Card h3 titles
- Size: `clamp(1.125rem, 2vw, 1.5rem)`
- Weight: 600
- Letter-spacing: `-0.01em`

### Body
- Line-height: `1.6` to `1.7`

### .reveal-text
- Bump to match or exceed section h2 size

### Media query cleanup
- Remove conflicting overrides at `1400px`, `767px`, `479px` that fight `clamp()`
