# CP7.D — KTS Edit Mode + API

**Code:** cp7d-pascal-edit-mode
**Parent CP:** cp7-pascal-editor-integration
**Order:** 7.D
**Depends On:** cp7c-pascal-viewer PASS
**Estimated Effort:** 2 ngay

## Muc tieu

Mo edit mode cho KTS: chinh sua 3D truc tiep trong review workspace → save thanh version moi KHONG qua GPU pipeline.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-web/src/components/review/pascal-edit-surface.tsx` | created | Pascal edit mode, toolbar save/discard/compare |
| `../ai-architect-web/src/components/review-client.tsx` | updated | Them tab "Chinh sua 3D" gated by flag |
| `../ai-architect-web/e2e/pascal-edit.spec.ts` | created | E2E edit → save → revision |
| `../ai-architect-api/app/api/v1/versions.py` | updated | `POST /versions/{id}/revise-from-scene` |
| `../ai-architect-api/app/services/geometry_service.py` | updated | Scene→geometry conversion, Layer 2 validation |
| `../ai-architect-api/app/models/version.py` | updated | `generation_source` enum them `pascal_edit` |
| `../ai-architect-api/alembic/versions/<hash>_add_pascal_edit.py` | created | Migration enum |
| `../ai-architect-api/tests/integration/test_revise_from_scene.py` | created | Integration tests |

## Behavior

- Tab "Chinh sua 3D" xuat hien sau flag `NEXT_PUBLIC_FF_PASCAL_EDIT=on` va current version co `geometry_json`.
- KTS mo tab → Pascal editor full mount.
- Save → `POST /versions/{id}/revise-from-scene` body `{ scene, note? }`:
  - Server goi `pascalSceneToGeometryJson` (server-side port hoac receive `geometry` tu client truc tiep — se chot trong design).
  - Validate qua Layer 2 validator.
  - Tao version moi, `parent_version_id = id`, `generation_source = pascal_edit`, `model_url = null`, `render_urls = []`.
  - KHONG dispatch Celery task GPU.
  - Emit WS `version.created`.
- Sau khi lock version `pascal_edit`, derive-3d flow CP12 van hoat dong de sinh `model_url`.

## Decision: scene→geometry chay o client hay server

Design doc chot 1 trong 2:

- **Client-first (uu tien):** Web goi `pascalSceneToGeometryJson`, POST body la `geometry_json`. Server chi validate.
- **Server-side:** Server chay JS runner hoac re-implement Python. Phuc tap hon, tranh de the.

Chot trong design doc CP7.B; mac dinh client-first.

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | Integration test: POST tao version moi, parent dung, source = `pascal_edit`, mock Celery NOT called | ✓ |
| CHECK-02 | E2E: edit 1 wall trong tab "Chinh sua 3D" → save → version moi xuat hien lineage, note preserved | ✓ |
| CHECK-03 | Validator reject scene sai Layer 2 schema (422) voi message ro | ✓ |
| CHECK-04 | Readiness rule (CP11): version `pascal_edit` chi export duoc khi LOCKED va co `model_url` (derive-3d sau lock) | ✓ |
| CHECK-05 | Migration enum `pascal_edit` apply + rollback test tren staging DB dump | ✓ |
| CHECK-06 | Flag off: tab "Chinh sua 3D" khong xuat hien, review workspace cu khong regression | ✓ |
| CHECK-07 | Analytics event `revision.created` co field `generation_source`, dashboard tile hien counts | warning |
