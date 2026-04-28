# 02 — TO-BE (muc tieu sau CP7)

## 1. Kien truc tong quan

```
┌──────────────────────────────────────────────────────────────────────┐
│                       ai-architect-web (Next.js 16)                  │
│                                                                      │
│   ┌───────────────────────────┐   ┌──────────────────────────────┐   │
│   │ Viewer page               │   │ Review workspace             │   │
│   │ (readonly)                │   │ (KTS edit mode)              │   │
│   │                           │   │                              │   │
│   │  feature flag:            │   │  feature flag:               │   │
│   │   FF_PASCAL_VIEWER=on  → Pascal readonly  FF_PASCAL_EDIT=on  │   │
│   │   off → <model-viewer>    │   │   off → legacy annotate only │   │
│   └─────────────┬─────────────┘   └──────────────┬───────────────┘   │
│                 │                                │                   │
│                 │ geometryJsonToPascalScene()    │                   │
│                 ▼                                ▼                   │
│   ┌───────────────────────────────────────────────────────────────┐  │
│   │ packages/pascal-editor  (vendored submodule, pinned SHA)      │  │
│   │   three.js WebGPU + R3F + zustand + zundo                     │  │
│   └───────────────────────────────────────────────────────────────┘  │
│                 ▲                                ▲                   │
│                 │ scene (readonly)               │ scene (edited)    │
│                 │                                │                   │
│   ┌─────────────┴────────────┐      ┌────────────┴───────────────┐   │
│   │ src/lib/pascal/          │      │ POST /versions/{id}/       │   │
│   │  geometry-adapter.ts     │      │   revise-from-scene        │   │
│   │                          │      │                            │   │
│   │  geometryJsonToScene()   │      │  validate via Layer 2      │   │
│   │  sceneToGeometryJson()   │      │  create version (parent)   │   │
│   │  round-trip tested       │      │  generation_source =       │   │
│   │                          │      │    "pascal_edit"           │   │
│   └──────────────────────────┘      │  NO GPU pipeline call      │   │
│                                     └────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────┘
                               │
                               ▼
         ┌─────────────────────────────────────────┐
         │ ai-architect-api                        │
         │   Canonical geometry_json Layer 2       │
         │   (CP1 Phase 2)                         │
         └─────────────────────────────────────────┘
```

## 2. Thay doi chinh

### 2.1 Web deps

Them workspace dependency:

```json
{
  "dependencies": {
    "pascal-editor": "workspace:*"
  }
}
```

`packages/pascal-editor/` la git submodule pin commit upstream.

Transitively: `three`, `@react-three/fiber`, `@react-three/drei`, `zustand`, `zundo`, `three-bvh-csg` (hidden trong package).

### 2.2 Viewer

- Component `PascalViewer` (readonly) nhan `version: VersionCanonical` va render scene tu `geometry_json`.
- Thay `<model-viewer>` tai [viewer-client.tsx:416-443](../../../../../ai-architect-web/src/components/viewer-client.tsx) bang branch theo flag.
- Khi `FF_PASCAL_VIEWER=on`:
  - Dung Pascal `<Level>`, `<Wall>`, `<Slab>`, `<Zone>`, `<Item>` render tu scene.
  - Toolbar them: level mode (stacked/exploded/solo), toggle zones, toggle items.
- Khi off: giu model-viewer nhu cu.

### 2.3 Review workspace

- Them tab "Chinh sua 3D" canh "Annotation" va "Compare".
- Tab nay mount `PascalEditSurface` (full Pascal editor, not readonly).
- Toolbar: save (create revision), discard, compare-with-parent.
- Save → `POST /versions/{id}/revise-from-scene` → tao version moi, skip GPU.

### 2.4 Backend

- `POST /versions/{id}/revise-from-scene`:
  - Body: `{ scene: PascalSceneJSON, note?: string }`.
  - Server goi `sceneToGeometryJson` (Python port cua adapter hoac dung server-side JS runner).
  - Validate qua canonical Layer 2 validator.
  - Tao version moi: `parent_version_id = id`, `generation_source = "pascal_edit"`, `model_url = null` (se derive sau khi lock).
  - Emit WS event `version.created`.
  - **Khong** dispatch GPU task.

### 2.5 Version state

Mo rong `generation_source` enum:

```
ai_generated | manual | pascal_edit
```

Readiness rule cho CP11 update: version `pascal_edit` vao export bundle chi khi locked **va** co `model_url` (derive sau khi KTS OK).

### 2.6 3D derive sau edit

- Sau khi version `pascal_edit` duoc LOCKED, goi derive-3d nhu version binh thuong → Blender pipeline dung `geometry_json` moi sinh GLB + renders.
- `model_url` va `render_urls` se cap nhat vao version → ready for CP11 export.

## 3. Feature flag matrix

| Flag | Default prod | Default staging | Purpose |
|------|--------------|-----------------|---------|
| `NEXT_PUBLIC_FF_PASCAL_VIEWER` | off | on (sau CP7.C) | Bat Pascal readonly viewer |
| `NEXT_PUBLIC_FF_PASCAL_EDIT` | off | on (sau CP7.D) | Bat edit mode trong review workspace |

Rollout: `on tren staging ≥ 7 ngay soak` → `on tren prod voi 1 beta studio` → `on all`.

## 4. Contracts

### 4.1 Geometry adapter (TypeScript)

```ts
// ai-architect-web/src/lib/pascal/geometry-adapter.ts
export function geometryJsonToPascalScene(g: GeometryV2): PascalScene;
export function pascalSceneToGeometryJson(s: PascalScene): GeometryV2;
```

Invariants:

- Round-trip bao toan deep-equal tren canonical keys `levels`, `walls`, `openings`, `rooms`, `slabs`, `items`.
- Field Layer 2 khong map (`grids`, dimensions, annotations) luu vao `geometry_v2_extra`.

### 4.2 API

```
POST /versions/{id}/revise-from-scene
  body  { scene: PascalSceneJSON, note?: string }
  200   { version: Version }  # new version, generation_source = "pascal_edit"
  409   if parent not in state allowing revision
  422   if scene fails Layer 2 validation
```

## 5. TO-BE summary

| Muc | TO-BE |
|-----|-------|
| Viewer stack | Pascal readonly (WebGPU R3F), fallback model-viewer |
| 3D deps | `pascal-editor` workspace package (pinned submodule) |
| Revision path | Edit 3D → save → version moi, no GPU (neu "pascal_edit") |
| Edit surface cho KTS | Pascal edit mode trong review workspace |
| Level visualization | Stacked / exploded / solo |
| `generation_source` | `ai_generated` / `manual` / `pascal_edit` |
| Browser compat | Chrome/Edge WebGPU. Safari/Firefox cu → fallback model-viewer qua detect |
