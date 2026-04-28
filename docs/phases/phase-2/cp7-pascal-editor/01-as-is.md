# 01 — AS-IS (hien trang, 2026-04-19)

## 1. 3D Viewer surface

**Evidence:** [ai-architect-web/src/components/viewer-client.tsx:320-342](../../../../../ai-architect-web/src/components/viewer-client.tsx).

- Render qua Web Component `<model-viewer>` cua Google, load script tu CDN `https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js` (dong ~342).
- Input: `model_url` (GLB) tu `version.model_url` (Celery + Blender pipeline dung tai CP12 Phase 1).
- Tuong tac co san: orbit, zoom, AR (neu device ho tro). **Khong co:** level toggle, room highlight, item inspection, edit.
- Fallback: neu khong co GLB → placeholder "Chua co scene GLB de xem truoc".
- Ngoai ra co 1 gallery `render_urls` (anh still) hien thi song song o same page ([viewer-client.tsx:463](../../../../../ai-architect-web/src/components/viewer-client.tsx)).

## 2. Web deps

**Evidence:** [ai-architect-web/package.json](../../../../../ai-architect-web/package.json).

```json
"dependencies": {
  "next": "16.2.3",
  "react": "19.2.4",
  "react-dom": "19.2.4"
}
```

Khong co three.js, `@react-three/fiber`, `@react-three/drei`, `zustand`, `zundo` — toan bo Pascal stack chua co.

Next.js 16 + React 19 la breaking-change branch (xem [AGENTS.md](../../../../../ai-architect-web/AGENTS.md)). Phai doc `node_modules/next/dist/docs/` truoc khi viet code.

## 3. Review workspace

**Evidence:** `ai-architect-web/src/components/review-client.tsx` (673 dong).

- Workspace la UI annotation + approve/reject/compare.
- Feedback chi di qua 2 con duong:
  1. Annotate (text trigger) → save review → KTS ky duyet.
  2. Create revision → POST tao version moi → GPU pipeline chay lai (CP3 Generation + CP12 Derivation).
- Khong co surface chinh sua 3D truc tiep. Tat ca chinh sua hinh dang di qua GPU.

## 4. Canonical geometry

Phase 2 CP1 `cp1-geometry-layer2` dang nang `geometry_json` len Layer 2 — xem [cp1-geometry-layer2/README.md](../checkpoints/cp1-geometry-layer2/README.md). Layer 2 schema chua:

- `levels[]`
- `walls[]` (segment + thickness + profile)
- `openings[]` (door/window voi reference toi wall)
- `rooms[]` (polygon + label)
- `slabs[]`
- `grids[]`

AS-IS tai thoi diem nay: CP1 Phase 2 chua PASS toan bo (theo [README sequence](../checkpoints/README.md)), cac project cu van o Layer 1.5 — tat ca cai nay la prerequisite cho CP7.B.

## 5. GPU pipeline

**Evidence:** `ai-architect-gpu/pipelines/blender_3d_pipeline.py` + CP12 Phase 1.

- Input: locked version + geometry_json + scene spec.
- Output: `model_url` (GLB), `render_urls` (still images), metadata.
- Thoi gian: minutes/version tuy scene.
- Moi revision nho deu tra 1 vong full pipeline.

## 6. Version state & revision flow

**Evidence:** [phase-1/05-system-design.md](../../../phase-1/05-system-design.md) muc 4.3 UC-03.

- Version states: `generated → under_review → locked → superseded`.
- Revision tao version moi voi parent = current version, trigger GPU pipeline.
- `generation_source` trong metadata co gia tri `ai_generated` (Celery) hoac `manual` (uploaded).
- Readiness rule cua CP11 yeu cau version locked moi export duoc.

## 7. Tom tat AS-IS

| Muc | Hien tai |
|-----|----------|
| Viewer stack | `<model-viewer>` CDN, read-only |
| 3D deps trong web | Khong co three.js / R3F |
| Revision path | Moi edit → GPU regenerate |
| Canonical geometry | Phase 2 CP1 dang nang Layer 2 (chua PASS) |
| `generation_source` | `ai_generated` / `manual` |
| Edit surface cho KTS | Khong co (chi annotation text) |
| Level visualization | Khong co |
| Browser compat | model-viewer tot tren Chrome/Safari/Firefox moi |
