# CP1 — Persistence and Migrations

**Objective:** Add the Phase 6 database and ORM backbone without overloading current design tables.  
**Requires:** `cp0-phase6-scope-lock-and-baseline-audit` validator pass.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp1-phase6-persistence-and-migrations/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP1 — Persistence and Migrations",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Implement the migration slice

Add an additive Alembic migration in `../ai-architect-api/alembic/versions/` for:

- `presentation_3d_bundles`
- `presentation_3d_jobs`
- `presentation_3d_assets`
- `presentation_3d_approvals`

Include only the minimal `DesignVersion.current_presentation_3d_bundle_id` linkage.

## Step 2 — Wire ORM and schema layer

Update:

- `../ai-architect-api/app/models.py`
- `../ai-architect-api/app/schemas.py`

Ensure the exact enum values from the checkpoint root README are used and not renamed locally.

## Step 3 — Add persistence tests

Create:

- `../ai-architect-api/tests/test_presentation_3d_persistence.py`

Cover:

- ORM row creation for bundle, job, asset, approval
- enum serialization
- upgrade and downgrade safety

## Step 4 — Run required commands

```bash
cd ../ai-architect-api && alembic upgrade head | tee ../ai-architect-mvp/artifacts/phase6/cp1-phase6-persistence-and-migrations/migration-up.log
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_persistence.py -q | tee ../ai-architect-mvp/artifacts/phase6/cp1-phase6-persistence-and-migrations/persistence-tests.log
cd ../ai-architect-api && alembic downgrade -1 | tee ../ai-architect-mvp/artifacts/phase6/cp1-phase6-persistence-and-migrations/migration-down.log
cd ../ai-architect-api && alembic upgrade head >> ../ai-architect-mvp/artifacts/phase6/cp1-phase6-persistence-and-migrations/migration-up.log
```

## Step 5 — Record completion

Create:

- `artifacts/phase6/cp1-phase6-persistence-and-migrations/result.json`
- `artifacts/phase6/cp1-phase6-persistence-and-migrations/notes.md`

In `notes.md`, record:

- final table list
- enum definitions
- downgrade caveats if any
- why extra 3D fields were not added directly to `DesignVersion`

## Step 6 — Notify and post status

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp1-phase6-persistence-and-migrations \
  --role implementer \
  --status READY \
  --summary "CP1 complete. Phase 6 persistence backbone and migrations are ready." \
  --result-file artifacts/phase6/cp1-phase6-persistence-and-migrations/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp1-phase6-persistence-and-migrations/result.json
```
