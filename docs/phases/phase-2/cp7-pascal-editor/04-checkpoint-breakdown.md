# 04 — Checkpoint Breakdown

CP7 monolith (7 ngay) duoc chia thanh 4 sub-checkpoints doc lap, moi sub-CP co README + INSTRUCTIONS + CHECKLIST rieng de track va validate doc lap.

## 1. Sequence

```
cp1-geometry-layer2 (Phase 2 CP1)
         │
         ▼
┌────────────────┐        ┌────────────────────┐
│ CP7.A          │        │ CP7.B              │
│ Pascal Spike   │──────▶ │ Geometry Adapter   │
│ + Vendor       │        │ (round-trip)       │
│ 1-2 ngay       │        │ 2 ngay             │
└────────────────┘        └─────────┬──────────┘
                                    │
                                    ▼
                          ┌────────────────────┐
                          │ CP7.C              │
                          │ Pascal Viewer      │
                          │ (readonly + flag)  │
                          │ 1 ngay             │
                          └─────────┬──────────┘
                                    │
                                    ▼
                          ┌────────────────────┐
                          │ CP7.D              │
                          │ Edit Mode + API    │
                          │ 2 ngay             │
                          └────────────────────┘
```

Tong: **6-7 ngay** effort.

## 2. Tom tat moi sub-CP

| Sub-CP | Code | Ngay | Exit criteria chinh |
|--------|------|------|---------------------|
| CP7.A | `cp7a-pascal-spike` | 1-2 | Pascal load duoc trong Next.js dev shell, browser compat matrix, spike report |
| CP7.B | `cp7b-geometry-adapter` | 2 | Adapter round-trip PASS tren 3 fixtures, design doc mapping table approved |
| CP7.C | `cp7c-pascal-viewer` | 1 | `PascalViewer` readonly hoat dong qua flag, no regression model-viewer fallback |
| CP7.D | `cp7d-pascal-edit-mode` | 2 | `POST /revise-from-scene` tao version moi khong goi GPU, E2E edit → save → revision appears |

## 3. Chi tiet sub-CP

### CP7.A — Pascal Spike + Vendor

**Folder:** [`checkpoints/cp7a-pascal-spike/`](../checkpoints/cp7a-pascal-spike/)

**Muc tieu:** Prove Pascal chay duoc trong monorepo cua ta, biet truoc bundle/browser rui ro.

**Deliverables:**

- `ai-architect-web/packages/pascal-editor/` (git submodule, SHA pinned)
- `ai-architect-web/NOTICE` (update attribution)
- [docs/phase-1/23-pascal-spike-report.md](../../../phase-1/23-pascal-spike-report.md) — browser matrix, bundle size, ssr pitfalls

**Blocker checks:**

- `pnpm build` PASS voi package vendored
- Pascal editor mount duoc trong 1 route test (`/lab/pascal`) voi dynamic import SSR off
- Browser compat matrix do duoc tren 4 browser

### CP7.B — Geometry Adapter

**Folder:** [`checkpoints/cp7b-geometry-adapter/`](../checkpoints/cp7b-geometry-adapter/)

**Muc tieu:** Co adapter round-trip on dinh giua canonical `geometry_json` Layer 2 va Pascal scene.

**Deliverables:**

- `src/lib/pascal/geometry-adapter.ts`
- `src/lib/pascal/geometry-adapter.test.ts` voi 3 fixture (simple / medium / complex)
- [docs/phase-1/24-pascal-integration-design.md](../../../phase-1/24-pascal-integration-design.md) — mapping table, metadata preservation rules

**Blocker checks:**

- Round-trip deep-equal tren canonical keys
- Fixture "complex" co wall mitering, nested room, openings, slabs — round-trip van PASS
- Field khong map luu vao `geometry_v2_extra`, verified

### CP7.C — Pascal Viewer (readonly)

**Folder:** [`checkpoints/cp7c-pascal-viewer/`](../checkpoints/cp7c-pascal-viewer/)

**Muc tieu:** Thay viewer mac dinh bang Pascal readonly sau feature flag, khong regression.

**Deliverables:**

- `src/components/viewer/pascal-viewer.tsx` (readonly wrapper)
- `src/components/viewer-client.tsx` update: flag branch tai [dong 416-443](../../../../../ai-architect-web/src/components/viewer-client.tsx)
- `e2e/pascal-viewer.spec.ts`
- Route-level code split xac nhan bundle size OK

**Blocker checks:**

- Flag on → Pascal render, level toggle hoat dong
- Flag off → model-viewer nhu cu (no regression)
- Bundle budget tren route viewer khong vuot han muc tu spike report

### CP7.D — KTS Edit Mode + API

**Folder:** [`checkpoints/cp7d-pascal-edit-mode/`](../checkpoints/cp7d-pascal-edit-mode/)

**Muc tieu:** KTS chinh sua 3D → save thanh revision moi khong qua GPU.

**Deliverables:**

- `src/components/review/pascal-edit-surface.tsx`
- `src/components/review-client.tsx` update: them tab "Chinh sua 3D" dat sau flag
- `ai-architect-api/app/api/v1/versions.py`: `POST /versions/{id}/revise-from-scene`
- `ai-architect-api/app/services/geometry_service.py`: validator + `generation_source = pascal_edit`
- Alembic migration cho `generation_source` enum
- `e2e/pascal-edit.spec.ts`
- `ai-architect-api/tests/integration/test_revise_from_scene.py`

**Blocker checks:**

- API tao version moi voi parent dung, `generation_source = pascal_edit`, KHONG goi GPU (assert mock Celery not called)
- E2E: edit wall → save → version moi xuat hien
- Readiness rule update: `pascal_edit` version van phai qua derive-3d truoc khi export
- Validator reject scene sai schema (422)

## 4. Umbrella CP7

[`checkpoints/cp7-pascal-editor-integration/`](../checkpoints/cp7-pascal-editor-integration/) giu lai lam umbrella tracking:

- `result.json` cho CP7 = hop cua 4 sub-CP result.
- `validation.json` = all 4 sub-CP PASS.
- Meta-checklist (xem CHECKLIST cua umbrella CP) kiem tra tong the sau 4 phase.

## 5. Khi nao split ra PR?

- Moi sub-CP = 1 PR tren branch `cp7-pascal-editor-integration`.
- PR order tuong ung A → B → C → D.
- Merge sub-CP vao branch CP7 truoc, cuoi cung merge branch CP7 vao `main` sau khi all sub-CP PASS.
