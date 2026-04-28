# CP7.C — Pascal Viewer (readonly)

**Code:** cp7c-pascal-viewer
**Parent CP:** cp7-pascal-editor-integration
**Order:** 7.C
**Depends On:** cp7b-geometry-adapter PASS
**Estimated Effort:** 1 ngay

## Muc tieu

Thay viewer `<model-viewer>` (CDN) tai [viewer-client.tsx:416-443](../../../../../ai-architect-web/src/components/viewer-client.tsx) bang Pascal readonly viewer duoi feature flag `NEXT_PUBLIC_FF_PASCAL_VIEWER`, khong regression khi flag off.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-web/src/components/viewer/pascal-viewer.tsx` | created | Readonly Pascal viewer, props {version, geometry} |
| `../ai-architect-web/src/components/viewer-client.tsx` | updated | Flag branch thay modelViewer block |
| `../ai-architect-web/e2e/pascal-viewer.spec.ts` | created | Playwright: load project → open viewer → orbit + level toggle |
| `../ai-architect-web/e2e/viewer-3d.spec.ts` | updated | Bo sung test flag=off fallback |
| `docs/phase-1/24-pascal-integration-design.md` | updated | Them section "Viewer flag strategy" |

## Behavior

- `FF_PASCAL_VIEWER=on`: render `PascalViewer` tu `version.geometry_json`. Toolbar: level stacked / exploded / solo, toggle zones, toggle items.
- `FF_PASCAL_VIEWER=off`: render `<model-viewer>` CDN nhu cu — identical CP12 baseline.
- Browser khong ho tro WebGPU: detect → fallback `<model-viewer>` BAT KE flag (tu dong), log client event `pascal.webgpu.fallback`.

## Bundle budget

Theo spike report CP7.A, ngan sach route viewer: **< `<T>` KB** sau Pascal (se chot sau khi A done). Violation blocks CHECK.

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | Flag on: Playwright E2E load viewer, orbit + level toggle hoat dong | ✓ |
| CHECK-02 | Flag off: viewer-3d.spec.ts (CP12 baseline) PASS | ✓ |
| CHECK-03 | Bundle route viewer `< budget` xac dinh tu spike | ✓ |
| CHECK-04 | Browser khong WebGPU (simulate qua `navigator.gpu=undefined`): tu dong fallback model-viewer | ✓ |
| CHECK-05 | Khong loi console blocking (WebGPU init warning cho phep, fatal khong cho phep) | warning |
