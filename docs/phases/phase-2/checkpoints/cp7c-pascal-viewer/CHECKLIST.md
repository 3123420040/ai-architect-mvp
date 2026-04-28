# CP7.C — Validation Checklist

## CHECK-01: Flag on E2E

```bash
cd ../ai-architect-web
NEXT_PUBLIC_FF_PASCAL_VIEWER=true pnpm exec playwright test e2e/pascal-viewer.spec.ts
```

**Expected:** Canvas render, level toggle hoat dong.
**Fail if:** Page trang, interaction fail.

## CHECK-02: Flag off fallback (CP12 baseline)

```bash
cd ../ai-architect-web
NEXT_PUBLIC_FF_PASCAL_VIEWER=false pnpm exec playwright test e2e/viewer-3d.spec.ts
```

**Expected:** `<model-viewer>` load GLB, orbit/zoom OK.
**Fail if:** Bat ky regression nao so voi CP12.

## CHECK-03: Bundle budget

```bash
cd ../ai-architect-web && pnpm build
# Validator doc bundle report, kiem tra route /projects/[id]/viewer < budget
```

**Expected:** Under budget theo spike report.
**Fail if:** Vuot.

## CHECK-04: WebGPU detection fallback

E2E voi Playwright: override `navigator.gpu = undefined` → confirm render model-viewer bat ke flag.

```ts
await page.addInitScript(() => { delete (navigator as any).gpu; });
```

**Expected:** Model-viewer active, Pascal skipped, console co event `pascal.webgpu.fallback`.
**Fail if:** Page crash hoac Pascal van thu khoi tao.

## CHECK-05 (warning): No blocking console error

Kiem E2E console log → khong co error fatal.
**Warning if:** Co warning WebGPU deprecation (chap nhan).

## Blocker

CHECK-01..04 → all PASS → trigger CP7.D.
