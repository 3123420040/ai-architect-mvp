# CP7 — Pascal Editor Integration

**Code:** cp7-pascal-editor-integration
**Order:** 7
**Depends On:** cp1-geometry-layer2, cp6-integration-qa (soft)
**Estimated Effort:** 7 days (4 phases A→D)
**Date added:** 2026-04-19

## Muc tieu

Tich hop `pascalorg/editor` (React Three Fiber + WebGPU, MIT) vao `ai-architect-web` de:

1. Thay viewer GLTF read-only hien tai (`viewer-3d.tsx`) bang Pascal scene graph viewer — level stacked/exploded, room zones, tot hon cho client presentation.
2. Mo edit mode cho KTS trong review workspace: chinh wall / slab / item truc tiep tren 3D thay vi feedback text → AI regenerate full model. Muc tieu: giam revision cycle xuong < 3 vong, giam GPU cost cho cac revision nho.
3. Chuan hoa bridge giua canonical `geometry_json` Layer 2 (CP1) va Pascal scene nodes, mo duong cho Phase 2 export DXF/IFC.

## Nguon tham chieu

- Upstream repo: https://github.com/pascalorg/editor (MIT)
- Homepage: https://editor.pascal.app
- Stack: React 19, Next.js 16, three.js (WebGPU), `@react-three/fiber`, `@react-three/drei`, `zustand`, `zundo`, `three-bvh-csg`.
- Pascal scene model: walls (mitering + cutouts), slabs/ceilings, rooms/zones, items (wall/ceiling/floor mount), levels, spatial grid.

## Scope theo phase

| Phase | Ten | Ngay | Dinh huong |
|-------|-----|------|------------|
| A | Spike + vendor | 1-2 | Vendor Pascal vao monorepo hoac install as workspace dep, chay duoc local, load 1 sample GLTF cua pipeline AI hien tai |
| B | Geometry adapter | 3-4 | Map `geometry_json` Layer 2 → Pascal scene nodes (walls, slabs, openings, rooms, items). Bi-directional: Pascal scene → `geometry_json` |
| C | Viewer replacement | 5 | Thay `viewer-3d.tsx` bang Pascal readonly mode sau feature flag `NEXT_PUBLIC_FF_PASCAL_VIEWER`. Giu flag cu `NEXT_PUBLIC_FF_VIEWER_3D` cho fallback |
| D | KTS edit mode | 6-7 | Review workspace: edit mode luu scene thanh revision moi (bypass GPU regenerate). Undo/redo dung `zundo` san co. Gate bang feature flag `NEXT_PUBLIC_FF_PASCAL_EDIT` |

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-web/packages/pascal-editor/` | created | Vendored hoac fork cua Pascal editor (submodule hoac pnpm workspace) |
| `../ai-architect-web/src/lib/pascal/geometry-adapter.ts` | created | `geometryJsonToPascalScene()` + `pascalSceneToGeometryJson()` |
| `../ai-architect-web/src/lib/pascal/geometry-adapter.test.ts` | created | Round-trip tests (geometry → scene → geometry) |
| `../ai-architect-web/src/components/viewer/pascal-viewer.tsx` | created | Readonly Pascal viewer component |
| `../ai-architect-web/src/components/viewer/viewer-3d.tsx` | updated | Branch theo feature flag: Pascal vs three.js GLTF cu |
| `../ai-architect-web/src/components/review/pascal-edit-surface.tsx` | created | Edit surface trong review workspace |
| `../ai-architect-api/app/api/v1/versions.py` | updated | `POST /versions/{id}/revise-from-scene` — nhan scene JSON, tao version moi |
| `../ai-architect-api/app/services/geometry_service.py` | updated | Validate scene-derived geometry dung canonical Layer 2 |
| `../ai-architect-mvp/docs/phase-1/24-pascal-integration-design.md` | created | Design doc: scene mapping rules, edit-to-revision state flow, feature flag matrix |
| `../ai-architect-web/e2e/pascal-viewer.spec.ts` | created | Playwright: load project → open Pascal viewer → orbit |
| `../ai-architect-web/e2e/pascal-edit.spec.ts` | created | Playwright: edit mode → move wall → save → revision appears |

## Feature flags

| Flag | Default | Muc dich |
|------|---------|----------|
| `NEXT_PUBLIC_FF_PASCAL_VIEWER` | off | Bat Pascal viewer thay three.js GLTF |
| `NEXT_PUBLIC_FF_PASCAL_EDIT` | off | Bat edit surface trong review workspace |

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | Pascal package build duoc trong monorepo (`pnpm build`) va khong vo tsc | ✓ |
| CHECK-02 | Geometry adapter round-trip: `geometry_json` → scene → `geometry_json` bao toan walls/openings/rooms/slabs (deep-equal qua canonical keys) | ✓ |
| CHECK-03 | Pascal viewer load duoc 1 project canonical Layer 2 that, orbit/level-toggle hoat dong (Playwright) | ✓ |
| CHECK-04 | Edit mode: di chuyen 1 wall, save → version moi xuat hien, lineage tro ve parent, KHONG goi GPU pipeline | ✓ |
| CHECK-05 | Khi 2 flag off, UI fallback ve viewer three.js cu, khong regression CP12 | ✓ |
| CHECK-06 | License compliance: `LICENSE` cua Pascal duoc include trong vendored folder, `NOTICE` update | warning |

## Rui ro va mitigation

| Rui ro | Mitigation |
|--------|------------|
| WebGPU chua on dinh tren Safari/Firefox cu | Pascal co fallback WebGL qua three.js? Neu khong, giu viewer cu sau feature flag cho browser compat |
| Pascal scene model khong du giau cho Layer 2 (grids, dimensions) | Phase 2 CP1 geometry Layer 2 da co `grids`/`levels`. Adapter chi map subset Pascal ho tro; phan con lai overlay rieng hoac defer qua CP sau |
| Edit-derived revision tao skew giua AI-generated va human-edited versions | Danh dau `generation_source = "pascal_edit"` trong metadata, ap dung rieng vao readiness rules cua CP11 |
| Upstream Pascal breaking change | Vendor (submodule pin) thay vi npm dependency tu registry chinh thong; pin commit SHA |

## Exit criteria

- Tat ca CHECK-01 → CHECK-05 PASS.
- Design doc `24-pascal-integration-design.md` da duoc review.
- Ke hoach rollout: flag off tren production, bat tren staging 1 tuan truoc khi chuyen mac dinh.
