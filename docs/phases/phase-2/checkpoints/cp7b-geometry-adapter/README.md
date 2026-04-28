# CP7.B — Geometry Adapter

**Code:** cp7b-geometry-adapter
**Parent CP:** cp7-pascal-editor-integration
**Order:** 7.B
**Depends On:** cp7a-pascal-spike PASS, cp1-geometry-layer2 PASS
**Estimated Effort:** 2 ngay

## Muc tieu

Co adapter round-trip on dinh giua canonical `geometry_json` Layer 2 va Pascal scene. Day la "ban le" moi cua CP7 — sai o day keo theo sai toan bo CP7.C/D.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-web/src/lib/pascal/geometry-adapter.ts` | created | `geometryJsonToPascalScene` + `pascalSceneToGeometryJson` |
| `../ai-architect-web/src/lib/pascal/geometry-adapter.test.ts` | created | Round-trip tests voi 3 fixtures |
| `../ai-architect-web/src/lib/pascal/fixtures/geometry-simple.json` | created | Fixture: 1 level, 4 walls, 1 room |
| `../ai-architect-web/src/lib/pascal/fixtures/geometry-medium.json` | created | 2 levels, 12 walls, 4 rooms, 3 openings, 2 slabs |
| `../ai-architect-web/src/lib/pascal/fixtures/geometry-complex.json` | created | 3 levels, wall mitering, nested rooms, furniture items |
| `docs/phase-1/24-pascal-integration-design.md` | created | Mapping table, metadata preservation rules |

## Mapping table (tom tat)

| Layer 2 | Pascal node | Ghi chu |
|---------|-------------|---------|
| `levels[]` | `Level` | 1-1 |
| `walls[].segment + thickness` | `Wall` | Mitering tu segment adjacency |
| `walls[].profile` | `Wall.profile` | Map theo enum |
| `openings[]` | `WallCutout + Item(door/window)` | Opening gan wall_id → cutout |
| `rooms[]` (polygon) | `Zone` | Label, color |
| `slabs[]` | `Slab` | 1-1 |
| `items[]` furniture | `Item(mount=floor)` | Placement anchor |
| `grids[]` | `geometry_v2_extra.grids` | Pascal khong ho tro → preserve qua metadata |
| `dimensions[]`, `annotations[]` | `geometry_v2_extra` | Same |

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | Test `geometry-adapter.test.ts` PASS het, round-trip deep-equal canonical keys | ✓ |
| CHECK-02 | Fixture "complex" round-trip bao toan wall mitering, nested rooms, openings | ✓ |
| CHECK-03 | Field `grids`, `dimensions`, `annotations` di vao `geometry_v2_extra` va ra lai nguyen | ✓ |
| CHECK-04 | Design doc `24-pascal-integration-design.md` co mapping table approved | ✓ |
| CHECK-05 | Adapter export TypeScript types tu Layer 2 schema chinh thong (khong redeclare) | warning |
