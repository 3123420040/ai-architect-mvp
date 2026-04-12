# CP3 — Schedules

**Mục tiêu:** Hoan tat data-driven schedule lane cho package Phase 2.  
**Requires:** `cp2-elevations-dimensions` PASS.

## Bước 1 — Normalize schedule data

Derive schedule rows from Layer 2 geometry:

- `door.csv`
- `window.csv`
- `room.csv`

## Bước 2 — Render schedule sheets

Add SVG sheet output for:

- A9 Door + Window Schedule
- A10 Room / Area Schedule

## Bước 3 — Wire schedule references into manifest and handoff

Manifest and handoff bundle must expose CSV and schedule sheet assets.

