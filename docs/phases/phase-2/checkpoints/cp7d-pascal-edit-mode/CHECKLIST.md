# CP7.D — Validation Checklist

## CHECK-01: No GPU dispatch

```bash
cd ../ai-architect-api
pytest tests/integration/test_revise_from_scene.py::test_revise_from_scene_no_gpu -q
```

**Expected:** Mock Celery assert_not_called, version created voi `generation_source=pascal_edit`.
**Fail if:** GPU task spawn.

## CHECK-02: E2E edit → save

```bash
cd ../ai-architect-web
NEXT_PUBLIC_FF_PASCAL_EDIT=true pnpm exec playwright test e2e/pascal-edit.spec.ts
```

**Expected:** Version moi xuat hien lineage, parent dung, note preserved.
**Fail if:** Fail o bat ky step.

## CHECK-03: Schema validation

```bash
cd ../ai-architect-api
pytest tests/integration/test_revise_from_scene.py::test_revise_from_scene_invalid -q
```

**Expected:** 422 voi message chi ra field thieu.
**Fail if:** Accept invalid scene.

## CHECK-04: Readiness rule

Test positive: `pascal_edit` + locked + model_url → export ready.
Test negative: `pascal_edit` + locked + model_url=null → block export voi message "derive 3D truoc khi handoff".

```bash
cd ../ai-architect-api
pytest tests/integration/test_export_readiness.py -k pascal_edit -q
```

**Fail if:** Readiness rule cho phep export khi chua co model_url.

## CHECK-05: Migration

```bash
cd ../ai-architect-api
alembic upgrade head
# Test voi staging DB dump
alembic downgrade -1 # phai chay voi warning accept
alembic upgrade head
```

**Expected:** Enum `pascal_edit` present, downgrade lam sach (hoac co documented plan khong downgrade vi enum postgres).
**Fail if:** Migration vo DB.

## CHECK-06: Flag off no regression

```bash
cd ../ai-architect-web
NEXT_PUBLIC_FF_PASCAL_EDIT=false pnpm exec playwright test e2e/review.spec.ts
```

**Expected:** Tab "Chinh sua 3D" khong render, review workspace nhu cu.
**Fail if:** Regression hoac tab van xuat hien.

## CHECK-07 (warning): Analytics

Event `revision.created` co `generation_source`, dashboard tile count `pascal_edit` vs `ai_generated`.
**Warning if:** Thieu (khong block PASS, nhung set task cleanup).

## Blocker

CHECK-01..06 → all PASS → CP7.D ready. Sau do umbrella CP7 co the close (all 4 sub-CP done).

## Notify umbrella

Sau CP7.D PASS, notify umbrella CP7 va publish result hop:

```bash
uv run python docs/phases/phase-2/checkpoints/notify.py \
  --cp cp7-pascal-editor-integration --role validator --status PASS \
  --summary "CP7 umbrella: A/B/C/D all PASS, san sang staging soak" \
  --result-file docs/phases/phase-2/checkpoints/cp7-pascal-editor-integration/validation.json
```
