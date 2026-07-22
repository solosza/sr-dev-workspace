# Download Engine

## Status
NEW

## What It Does
Downloads mod files via Playwright MCP, extracts archives, and places files in the correct game mod folders. Handles large multi-part downloads with progress tracking.

## Capabilities
- Download via Playwright browser (handles JS-gated downloads, CAPTCHAs, wait timers)
- Extract ZIP, RAR, 7z archives
- Map archive contents to correct mod subfolder (editor data, graphics/faces, skins, etc.)
- Handle multi-part downloads (some megapacks split into 10+ parts)
- Progress tracking for large files (10GB+ facepacks)
- Resume interrupted downloads where possible

## Folder Mapping Logic
```
Archive structure detected → map to game mod folders

Example (FM24):
  zip contains "Football Manager 2024/editor data/*.fmf"
  → extract to {documents}/Sports Interactive/Football Manager 2024/editor data/

  zip contains "faces/*.png" + "config.xml"
  → extract to {graphics}/faces/

  zip contains "*.fmf" (skin file)
  → extract to {skins}/
```

## Dependencies
- Playwright MCP (browser downloads)
- unzip, 7z CLI tools for extraction
- Game detection (for target paths)
