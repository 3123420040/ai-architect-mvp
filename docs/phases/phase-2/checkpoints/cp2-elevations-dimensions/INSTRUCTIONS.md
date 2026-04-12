# CP2 — 4 Elevations + Enhanced Dimensions

**Mục tiêu:** Mo rong sheet engine de render mat dung, section va full dimension chains.  
**Requires:** `cp1-geometry-layer2` PASS.

## Bước 1 — Build SVG sheet renderers

Add renderers for:

- site / plot plan
- floor plan per level
- south / north / east / west elevations
- section A-A and B-B

## Bước 2 — Add dimension engine

Dimension engine must support:

- overall dimensions,
- grid-to-grid,
- wall-to-wall,
- opening positions and widths,
- room internal dimensions,
- elevation vertical heights.

## Bước 3 — Ensure all drawings share canonical labels

Door/window `schedule_mark` values must appear consistently across plans, elevations, schedules, and DXF/IFC exports.

