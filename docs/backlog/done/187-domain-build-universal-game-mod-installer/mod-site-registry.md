# Mod Site Registry

## Status
NEW

## What It Does
Maps each game to its community mod sites and defines navigation patterns for Playwright MCP to find, authenticate, and download mods.

## Site Config Schema
```json
{
  "site_id": "sortitoutsi",
  "base_url": "https://sortitoutsi.net",
  "auth": {
    "type": "form",
    "login_url": "/auth/login",
    "fields": ["username", "password"]
  },
  "games": ["fm24", "fm26"],
  "mod_categories": [
    {
      "category": "data_update",
      "url_pattern": "/football-manager-data-update/fm24-transfer-update",
      "download_selector": "link containing 'Free Download'",
      "priority": 1
    }
  ]
}
```

## Supported Sites (Initial)
| Site | Games | Auth Required |
|------|-------|---------------|
| sortitoutsi.net | FM24, FM26 | Yes (form login) |
| Nexus Mods | Skyrim, Stardew Valley, Cities Skylines | Yes (OAuth) |
| Steam Workshop | Any Steam game | Via Steam client |
| CurseForge | Minecraft, various | Optional |
| fmscout.com | FM series | No |
| df11faces.com | FM series | No |

## Dependencies
- Playwright MCP for site navigation
- Credential storage (user provides credentials per site)
