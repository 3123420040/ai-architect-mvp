# CP1 — Geometry Layer 2

**Mục tiêu:** Tao canonical Layer 2 geometry contract cho toan bo export lane.  
**Requires:** `cp0-phase2-readiness` PASS.

## Bước 1 — Lock Layer 2 schema surface

Implement a canonical schema aligned to Section 2 of the Phase 2 document:

- `project_info`
- `grids`
- `levels`
- `site`
- `walls`
- `openings`
- `rooms`
- `stairs`
- `fixtures`
- `roof`
- `markers`
- `dimensions_config`

## Bước 2 — Backward-compatible geometry builder

Implement a helper that:

- returns existing Layer 2 geometry untouched,
- upgrades old geometry / brief-only versions into a generated Layer 2 structure,
- keeps deterministic option variance for gallery generation.

## Bước 3 — Attach geometry on generation

Update generation persistence so every newly created version stores Layer 2 geometry and metadata needed by exports.

