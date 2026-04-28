# CP1 — Semantic Model and Persistence

**Objective:** Add Program B persistence and semantic model backbone.
**Requires:** CP0 PASS.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp1-program-b-semantic-model-and-persistence/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP1 — Program B semantic model and persistence",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Add Program B persistence

Implement migrations and models for:

- `coordination_model_versions`
- `coordination_elements`
- `coordination_element_relationships`
- `coordination_handoff_bundles`
- `coordination_jobs`

Do not overload `design_versions` with full Program B runtime state.

## Step 2 — Implement semantic model generation

Create:

- `../ai-architect-api/app/services/coordination/semantic_model_builder.py`
- `../ai-architect-api/app/services/coordination/semantic_ids.py`
- `../ai-architect-api/app/services/coordination/relationships.py`

Builder responsibilities:

- normalize approved geometry into launch entity types
- assign stable semantic ids
- link relationships
- persist model artifact reference

## Step 3 — Add eligibility and typology blocking

In `coordination.py` and `eligibility.py`, block:

- unsupported typologies
- unresolved versions
- geometry missing required architectural fields

## Step 4 — Add tests

Create targeted tests for:

- deterministic semantic ids
- supported typology acceptance
- unsupported typology rejection

Suggested command:

```bash
cd ../ai-architect-api && .venv/bin/python -m pytest -q tests/coordination
```

## Step 5 — Record completion artifacts

Create:

- `artifacts/program-b/cp1-program-b-semantic-model-and-persistence/result.json`
- `artifacts/program-b/cp1-program-b-semantic-model-and-persistence/notes.md`
- `artifacts/program-b/cp1-program-b-semantic-model-and-persistence/schema-notes.md`

## Step 6 — Notify and post status

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp1-program-b-semantic-model-and-persistence \
  --role implementer \
  --status READY \
  --summary "CP1 complete. Program B persistence and semantic model backbone are in place." \
  --result-file artifacts/program-b/cp1-program-b-semantic-model-and-persistence/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp1-program-b-semantic-model-and-persistence/result.json
```
