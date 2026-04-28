# CP7.A — Pascal Spike + Vendor

**Code:** cp7a-pascal-spike
**Parent CP:** cp7-pascal-editor-integration
**Order:** 7.A
**Depends On:** cp1-geometry-layer2 (schema only; spike khong can data that)
**Estimated Effort:** 1-2 ngay

## Muc tieu

Chung minh Pascal editor chay duoc trong monorepo `ai-architect-web` (Next.js 16, React 19), biet truoc browser compat va bundle rui ro.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-web/packages/pascal-editor/` | submodule | Vendor upstream `pascalorg/editor`, pin SHA |
| `../ai-architect-web/pnpm-workspace.yaml` | updated | Them `packages/*` neu chua co |
| `../ai-architect-web/src/app/lab/pascal/page.tsx` | created | Route test de mount editor |
| `../ai-architect-web/NOTICE` | created/updated | Attribution MIT cua Pascal |
| `docs/phase-1/23-pascal-spike-report.md` | created | Browser matrix, bundle, SSR pitfalls |

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | `pnpm install && pnpm build` PASS sau khi vendor Pascal | ✓ |
| CHECK-02 | Route `/lab/pascal` mount duoc Pascal editor (dynamic import, ssr=false) tren Chrome | ✓ |
| CHECK-03 | Browser compat matrix da do du 4 browser (Chrome, Edge, Safari 17+, Firefox 120+), bao cao co feature-detect ket luan | ✓ |
| CHECK-04 | Bundle size route `/lab/pascal` da do, document vao spike report (ngan sach se set o CP7.C) | warning |
| CHECK-05 | `NOTICE` co entry Pascal + LICENSE upstream van ton tai trong submodule | warning |

## Exit

CHECK-01 → CHECK-03 PASS + spike report approved → vao CP7.B.
