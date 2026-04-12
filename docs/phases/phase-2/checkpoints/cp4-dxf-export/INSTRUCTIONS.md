# CP4 — DXF Export

**Mục tiêu:** Dua canonical package sang CAD handoff format.  
**Requires:** `cp3-schedules` PASS.

## Bước 1 — Add DXF dependency and layer map

Set up `ezdxf` and define the architectural layer contract aligned to the Phase 2 document.

## Bước 2 — Draw model space content

Model space must contain:

- site plan,
- one floor plan cluster per level,
- 4 elevations,
- 2 sections.

## Bước 3 — Create paper space layouts

Create named layouts with title blocks and viewport framing for the main sheets.

