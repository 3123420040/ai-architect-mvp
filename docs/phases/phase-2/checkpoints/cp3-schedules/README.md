# CP3 — Schedules

**Code:** cp3-schedules  
**Order:** 3  
**Depends On:** cp2-elevations-dimensions  
**Estimated Effort:** 2 days

## Mục tiêu

Generate door, window, room/area schedules from canonical geometry and embed them into export package plus CSV files.

## Artifacts dự kiến

| File/Path | Action | Mô tả |
|-----------|--------|-------|
| `../ai-architect-api/app/services/exporter.py` | updated | Schedule renderers + CSV generation |
| `../ai-architect-api/tests/*` | updated | Test manifests and schedule exports |

## Checklist Validator

| ID | Mô tả | Blocker |
|----|-------|---------|
| CHECK-01 | Door schedule co mark, room, type, size, frame, panel, hardware | ✓ |
| CHECK-02 | Window schedule co sill, frame, glazing, U-value | ✓ |
| CHECK-03 | Room schedule co subtotals theo tang va building total | ✓ |

