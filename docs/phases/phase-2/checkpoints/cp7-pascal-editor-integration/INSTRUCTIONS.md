# CP7 — Pascal Editor Integration (Instructions)

**Muc tieu:** Tich hop Pascal editor lam viewer + edit surface, qua 4 phase A → D.
**Requires:** `cp1-geometry-layer2` PASS (geometry Layer 2 canonical). `cp6-integration-qa` (soft).

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp7-pascal-editor-integration/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Bat dau CP7 Pascal editor integration (Phase A spike)",
    "readyForNextTrigger": false
  }' || true
```

---

## Phase A — Spike + vendor (Day 1-2)

### A.1 Vendor Pascal vao monorepo

Quyet dinh vendoring strategy:

- **Uu tien:** `git subtree` hoac `git submodule` vao `ai-architect-web/packages/pascal-editor/`, pin commit SHA.
- **Phuong an 2:** Fork sang org noi bo, thiet lap pnpm workspace dependency.

```bash
cd ../ai-architect-web
git submodule add https://github.com/pascalorg/editor packages/pascal-editor
cd packages/pascal-editor && git checkout <SHA_PINNED> && cd -
```

Cap nhat `pnpm-workspace.yaml` de workspace recognize.

### A.2 Local boot + load sample GLTF

- Chay Pascal editor local theo README upstream.
- Xuat 1 GLTF mau tu 1 version locked trong `ai-architect-api` (qua `GET /versions/{id}/3d`).
- Load GLTF vao Pascal editor, xac nhan render va level stacked hoat dong.

### A.3 Ghi spike report

Tao `docs/phase-1/23-pascal-spike-report.md` voi:

- Browser compat matrix (Chrome/Safari/Firefox, WebGPU on/off).
- Pascal scene nodes lien quan den domain cua minh (walls/slabs/items/rooms).
- Gaps so voi geometry Layer 2.

**Exit Phase A:** Pascal load duoc trong Next.js dev shell, spike report da viet.

---

## Phase B — Geometry adapter (Day 3-4)

### B.1 Design scene mapping

Tao `docs/phase-1/24-pascal-integration-design.md`, muc `Scene Mapping`:

| `geometry_json` Layer 2 | Pascal scene node |
|-------------------------|-------------------|
| `levels[]` | `Level` |
| `walls[]` (segment + thickness) | `Wall` (mitering) |
| `openings[]` (door/window) | `WallCutout` + `Item` (door/window) |
| `rooms[]` (polygon + label) | `Zone` |
| `slabs[]` | `Slab` |
| `items[]` (furniture) | `Item` (floor-mount) |
| `grids[]` | Overlay layer (khong map qua Pascal) |

### B.2 Implement adapter

```bash
cd ../ai-architect-web
# Implement src/lib/pascal/geometry-adapter.ts
```

- `geometryJsonToPascalScene(geometry: GeometryV2): PascalScene`
- `pascalSceneToGeometryJson(scene: PascalScene): GeometryV2`
- Preserve custom metadata `geometry_v2_extra` cho field Pascal khong ho tro (grids, dimensions).

### B.3 Round-trip tests

```bash
cd ../ai-architect-web && pnpm test src/lib/pascal/geometry-adapter.test.ts
```

- Input: 3 fixture geometry Layer 2 (simple / medium / complex).
- Assert: `toPascal → toGeometry` deep-equal canonical keys.

**Exit Phase B:** Adapter tests PASS, design doc review xong.

---

## Phase C — Viewer replacement (Day 5)

### C.1 Component `PascalViewer`

Tao `src/components/viewer/pascal-viewer.tsx`:

- Prop: `version: VersionCanonical`, `mode: "readonly"`.
- Load `geometry_json` → `geometryJsonToPascalScene` → render.
- Ho tro level stacked / exploded / solo toggle.

### C.2 Feature flag branch

Update `src/components/viewer/viewer-3d.tsx`:

```ts
if (process.env.NEXT_PUBLIC_FF_PASCAL_VIEWER === "true") {
  return <PascalViewer version={version} mode="readonly" />;
}
return <LegacyGLTFViewer version={version} />;
```

### C.3 E2E test

```bash
cd ../ai-architect-web
NEXT_PUBLIC_FF_PASCAL_VIEWER=true pnpm exec playwright test e2e/pascal-viewer.spec.ts
```

**Exit Phase C:** CHECK-03, CHECK-05 PASS.

---

## Phase D — KTS edit mode (Day 6-7)

### D.1 Backend endpoint

`POST /versions/{id}/revise-from-scene`:

- Body: `{ scene: PascalSceneJSON, note?: string }`
- Goi `pascalSceneToGeometryJson` (share logic qua Python port hoac goi FE truoc roi gui geometry).
- Validate qua canonical Layer 2 validator (CP1).
- Tao version moi, `generation_source = "pascal_edit"`, parent = version id, bypass GPU pipeline.

### D.2 Edit surface component

Tao `src/components/review/pascal-edit-surface.tsx`:

- Mode `edit`, su dung Pascal editor that (khong chi viewer).
- Toolbar: save / discard / compare voi parent.
- Undo/redo qua `zundo` store.

### D.3 Wire vao review workspace

Update `src/components/review-client.tsx`:

- Them tab "Edit 3D" khi `NEXT_PUBLIC_FF_PASCAL_EDIT=true` va current version co 3D.
- Save → goi `POST /versions/{id}/revise-from-scene` → reload version lineage.

### D.4 E2E test

```bash
cd ../ai-architect-web
NEXT_PUBLIC_FF_PASCAL_EDIT=true pnpm exec playwright test e2e/pascal-edit.spec.ts
```

**Exit Phase D:** CHECK-04 PASS.

---

## Buoc 3 — Ghi ket qua

Tao `docs/phases/phase-2/checkpoints/cp7-pascal-editor-integration/result.json`:

```json
{
  "cp": "cp7-pascal-editor-integration",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Pascal editor da integrate: viewer readonly + KTS edit surface sau feature flag.",
  "artifacts": [
    {"file": "../ai-architect-web/packages/pascal-editor", "action": "vendored"},
    {"file": "../ai-architect-web/src/lib/pascal/geometry-adapter.ts", "action": "created"},
    {"file": "../ai-architect-web/src/components/viewer/pascal-viewer.tsx", "action": "created"},
    {"file": "../ai-architect-web/src/components/review/pascal-edit-surface.tsx", "action": "created"},
    {"file": "../ai-architect-api/app/api/v1/versions.py", "action": "updated"},
    {"file": "docs/phase-1/23-pascal-spike-report.md", "action": "created"},
    {"file": "docs/phase-1/24-pascal-integration-design.md", "action": "created"}
  ],
  "issues": [],
  "notes": "Flag mac dinh off tren production, bat tren staging truoc rollout."
}
```

```bash
uv run python docs/phases/phase-2/checkpoints/notify.py \
  --cp cp7-pascal-editor-integration \
  --role implementer \
  --status READY \
  --summary "Pascal integration da xong 4 phase" \
  --result-file docs/phases/phase-2/checkpoints/cp7-pascal-editor-integration/result.json

python3 docs/phases/phase-2/checkpoints/post-status.py \
  --result-file docs/phases/phase-2/checkpoints/cp7-pascal-editor-integration/result.json
```
