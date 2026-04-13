# CP2 — API Contracts and Serializers

**Objective:** Introduce the new bundle-oriented API surface and typed frontend consumption path.  
**Requires:** `cp1-phase6-persistence-and-migrations` validator pass.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp2-phase6-api-contracts-and-serializers/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP2 — API Contracts and Serializers",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Add the router and serializers

Implement:

- `../ai-architect-api/app/api/v1/presentation_3d.py`
- router registration in `../ai-architect-api/app/api/v1/router.py`

Support the locked endpoints from the checkpoint root README.

## Step 2 — Implement serializer contracts

Expose:

- latest bundle summary
- bundle detail
- job detail
- retry response
- approval and rejection responses

Return explicit `409` and `422` responses where the Phase 6 contract requires them.

## Step 3 — Add frontend typed consumption

Create:

- `../ai-architect-web/src/lib/presentation-3d.ts`

Update generated or handwritten API types as needed so future UI work reads bundle-first payloads.

## Step 4 — Add contract tests and snapshot

Create:

- `../ai-architect-api/tests/test_presentation_3d_api.py`

Cover:

- all seven endpoints
- serializer field names
- eligibility failures
- approval blocked before QA pass

Capture the current API shape into:

- `artifacts/phase6/cp2-phase6-api-contracts-and-serializers/openapi-snapshot.json`

## Step 5 — Run required commands

```bash
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_api.py -q | tee ../ai-architect-mvp/artifacts/phase6/cp2-phase6-api-contracts-and-serializers/api-tests.log
cd ../ai-architect-web && pnpm build
```

## Step 6 — Record completion and notify

Create:

- `artifacts/phase6/cp2-phase6-api-contracts-and-serializers/result.json`
- `artifacts/phase6/cp2-phase6-api-contracts-and-serializers/notes.md`

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp2-phase6-api-contracts-and-serializers \
  --role implementer \
  --status READY \
  --summary "CP2 complete. Phase 6 API contracts and typed serializers are ready." \
  --result-file artifacts/phase6/cp2-phase6-api-contracts-and-serializers/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp2-phase6-api-contracts-and-serializers/result.json
```
