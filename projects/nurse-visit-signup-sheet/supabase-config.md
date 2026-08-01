# Supabase config — nurse-signup

Project created 2026-08-01 via browser automation (Playwright), account owner: solosza (GitHub login).

## Public values (safe to embed in the webpage / commit)
- **Project URL:** `https://toqcipuepxdmlhkpjozw.supabase.co`
- **Publishable (anon) key:** `sb_publishable_hKZKOQGTihooRc4InIU0VA_19KqKGoM`
- **Project ref:** `toqcipuepxdmlhkpjozw`
- **Region:** Canada (Central) / ca-central-1
- **Organization:** solosza's Org (Free plan)

## Secret values (NEVER put in the webpage — backend only)
- Secret API key: `sb_secret_...` (left hidden in dashboard; retrieve from Project Settings > API Keys if ever needed)
- Database password: generated at project creation; resettable in Project Settings > Database. Not used by the app.

## Dashboard
https://supabase.com/dashboard/project/toqcipuepxdmlhkpjozw

## Notes
- App talks to the DB using the **publishable key** + Row Level Security (RLS) policies.
- Legacy `anon` / `service_role` JWT keys also exist under Settings > API Keys > Legacy, if a library needs the old format.
