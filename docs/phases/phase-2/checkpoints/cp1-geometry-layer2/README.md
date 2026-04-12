# CP1 — Geometry Layer 2

**Code:** cp1-geometry-layer2  
**Order:** 1  
**Depends On:** cp0-phase2-readiness  
**Estimated Effort:** 4 days

## Mục tiêu

Nang `geometry_json` len Layer 2 theo tai lieu Phase 2, giu backward compatibility cho project cu, va bao dam tat ca export/render lane dung chung mot canonical geometry contract.

## Artifacts dự kiến

| File/Path | Action | Mô tả |
|-----------|--------|-------|
| `../ai-architect-api/app/services/*geometry*` | created/updated | Canonical Layer 2 builder + validation helpers |
| `../ai-architect-api/app/api/v1/generation.py` | updated | Persist geometry Layer 2 cho version moi |
| `../ai-architect-api/tests/*` | updated | Test geometry generation / compatibility |

## Checklist Validator

| ID | Mô tả | Blocker |
|----|-------|---------|
| CHECK-01 | Version generate moi co `geometry_json.$schema = ai-architect-geometry-v2` | ✓ |
| CHECK-02 | Geometry co du `grids`, `levels`, `walls`, `openings`, `rooms` | ✓ |
| CHECK-03 | Project cu khong co geometry van export duoc qua fallback builder | ✓ |

