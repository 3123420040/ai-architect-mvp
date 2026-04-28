# 03 — Gap Analysis

## 1. Bang gap

| # | AS-IS | TO-BE | Gap / work item | Owner | Sub-CP |
|---|-------|-------|------------------|-------|--------|
| G1 | `<model-viewer>` CDN, no 3D deps | Pascal R3F + WebGPU, vendored package | Vendor Pascal, wire workspace, build OK trong Next.js 16 | Web | CP7.A |
| G2 | Khong co browser-compat matrix cho WebGPU | Matrix do kiem + detect runtime | Spike report voi table Chrome/Edge/Safari/Firefox, feature-detect helper | Web | CP7.A |
| G3 | Khong co adapter geometry ↔ scene | Round-trip geometryJson ↔ PascalScene | Thiet ke mapping table, implement 2 ham + 3 fixture tests | Web | CP7.B |
| G4 | Layer 2 geometry co `grids`, dimensions, Pascal khong ho tro | Luu vao `geometry_v2_extra` metadata, adapter preserve | Mo rong Pascal scene wrapper de carry extra payload | Web | CP7.B |
| G5 | Viewer khong co level mode, room highlight | Toolbar level stacked/exploded/solo + zone toggle | `PascalViewer` component + toolbar | Web | CP7.C |
| G6 | Viewer hien tai duoi model-viewer; khong co flag branch | Flag branch `FF_PASCAL_VIEWER`, fallback model-viewer | Thay block tai [viewer-client.tsx:416-443](../../../../../ai-architect-web/src/components/viewer-client.tsx) bang conditional render | Web | CP7.C |
| G7 | Edit surface khong ton tai | `PascalEditSurface` trong review workspace | Component + tab moi trong `review-client.tsx` | Web | CP7.D |
| G8 | Revision chi qua GPU regenerate | Revision tu scene edit, khong GPU | `POST /versions/{id}/revise-from-scene`, skip Celery dispatch | API | CP7.D |
| G9 | `generation_source` enum chua co `pascal_edit` | Them value `pascal_edit`, migrate schema | Alembic migration + enum update + readiness rule adjust | API | CP7.D |
| G10 | Export bundle readiness yeu cau locked + model_url | Pascal-edited version van phai qua derive-3d de co model_url | Khong doi contract CP11; document ly do trong rollout | API | CP7.D |
| G11 | Khong co license/attribution cho Pascal | Include LICENSE + update NOTICE | File copy + text edit | Web | CP7.A |
| G12 | Khong co metric tracking cho revision source | Count `pascal_edit` vs `ai_generated` per project | Them field vao analytics event, dashboard tile | API + Web | CP7.D |
| G13 | Next.js 16 App Router breaking changes | Pascal dung Next 16 rieng — phai test ssr/dynamic | `dynamic(() => import("pascal-viewer"), { ssr: false })` + verify tree shaking | Web | CP7.A / CP7.C |
| G14 | Bundle size chua biet | Pascal + three.js ~ MB, can tach vao route segment | Route-level code split, verify bundle budget `pnpm build` | Web | CP7.C |

## 2. Rui ro tu gap

| Rui ro | Muc | Mitigation |
|--------|-----|-----------|
| WebGPU khong on dinh Safari 17- | Med | Feature-detect + fallback model-viewer qua flag override |
| Bundle size tang vuot ngan sach route | Med | Dynamic import, loading shell, verify qua `pnpm build` output |
| Pascal upstream breaking change | Low | Pin SHA qua submodule, update co kiem soat |
| Scene ↔ geometry information loss | High | Fixture round-trip tests bao quat edge cases (wall mitering, slant walls, nested rooms); assert deep-equal |
| Pascal scene schema thay doi khi upgrade | Med | Dat `PascalSceneJSON` version header, adapter check |
| `generation_source = pascal_edit` lam export bundle sai | High | CP7.D phai update readiness rule test (positive + negative) |
| GPU lane phai derive 3D sau edit → lai ve GPU | Low | Chap nhan: edit tiet kiem GPU cho iteration loop, derive cuoi cung van qua GPU 1 lan khi lock |

## 3. Dependencies

- `cp1-geometry-layer2` PASS — bat buoc truoc khi vao CP7.B (adapter dua tren Layer 2 schema).
- `cp6-integration-qa` PASS — soft dependency, can de khong lam rong bundle QA.
- Pascal upstream repo (external) — no control, vendor hoa.
