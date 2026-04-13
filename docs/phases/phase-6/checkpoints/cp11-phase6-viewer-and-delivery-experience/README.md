# CP11 — Viewer and Delivery Experience

**Code:** `cp11-phase6-viewer-and-delivery-experience`  
**Order:** 11  
**Depends On:** `cp10-phase6-approval-gate-and-manifest`  
**Estimated Effort:** 2 days

## Objective

Replace the current debug-oriented 3D viewer with a presentation workspace that communicates progress, preview state, approval state, and released deliverables in Vietnamese.

## Locked Slices

1. bundle summary fetch
2. status and progress components
3. GLB, gallery, and video panels
4. approval panel
5. released vs preview UX

## Interfaces and States Touched

- frontend states:
  - `idle`
  - `queued`
  - `running`
  - `preview_degraded`
  - `awaiting_approval`
  - `released`
  - `failed`
- Vietnamese status labels
- delivery workspace release labels
- manifest download and model actions

## Modules Expected to Change

| Repo | File/Path | Action | Notes |
|---|---|---|---|
| web | `../ai-architect-web/src/components/viewer-client.tsx` | updated | Main presentation viewer |
| web | `../ai-architect-web/src/components/delivery-client.tsx` | updated | Delivery workspace integration |
| web | `../ai-architect-web/src/components/status-badge.tsx` | updated | Compact status chips if reused |
| web | `../ai-architect-web/src/lib/presentation-3d.ts` | updated | Bundle fetch and approval actions |

## Expected Handoff Artifacts

| File/Path | Action | Description |
|---|---|---|
| `artifacts/phase6/cp11-phase6-viewer-and-delivery-experience/result.json` | created | Implementation result |
| `artifacts/phase6/cp11-phase6-viewer-and-delivery-experience/notes.md` | created | UX decisions and string policy |
| `artifacts/phase6/cp11-phase6-viewer-and-delivery-experience/web-build.log` | created | Frontend build output |
| `artifacts/phase6/cp11-phase6-viewer-and-delivery-experience/screenshots/` | created | Desktop and mobile acceptance screenshots |

## Exit / DoD

| ID | Description | Blocker |
|---|---|---|
| CHECK-01 | The page no longer presents raw model payloads or debug-oriented wording as primary UI | ✓ |
| CHECK-02 | UI clearly distinguishes `Bản xem trước`, `Cần KTS duyệt`, `Đã duyệt`, and blocked release states | ✓ |
| CHECK-03 | Hero still, gallery, video, model action, QA status, and approval actions are all in the main experience | ✓ |
| CHECK-04 | User-facing copy is Vietnamese with diacritics and consistent across viewer and delivery workspace | ✓ |
