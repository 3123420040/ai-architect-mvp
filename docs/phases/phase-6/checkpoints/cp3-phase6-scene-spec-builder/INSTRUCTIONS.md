# CP3 — Scene Spec Builder

**Objective:** Generate a deterministic renderer-independent scene handoff from approved design truth.  
**Requires:** `cp2-phase6-api-contracts-and-serializers` validator pass.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp3-phase6-scene-spec-builder/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP3 — Scene Spec Builder",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Build the source loader and validation path

Implement a builder path that reads:

- approved canonical geometry
- room semantics
- material directives
- render request preset
- locked shot priorities

Reject missing structural inputs before runtime dispatch.

## Step 2 — Implement mapping and shot planning

Create:

- `../ai-architect-api/app/services/presentation_3d/scene_spec_builder.py`
- `../ai-architect-api/app/services/presentation_3d/material_mapping.py`
- `../ai-architect-api/app/services/presentation_3d/shot_planner.py`

Lock the first required still set to:

- `exterior_hero_day`
- `exterior_entry`
- `living_room`
- `kitchen_dining`
- `master_bedroom`

## Step 3 — Persist the scene spec

The builder must persist a durable `scene_spec.json` artifact or stable reference that later checkpoints can hand to runtime.

Use fixture inputs from:

- `implementation/phase-6/mock-inputs/03-canonical-2d-design-input.json`
- `implementation/phase-6/mock-inputs/04-style-material-mapper-input.json`
- `implementation/phase-6/mock-inputs/05-presentation-scene-spec.json`

## Step 4 — Add tests

Create:

- `../ai-architect-api/tests/test_presentation_3d_scene_spec.py`

Cover:

- deterministic rerun behavior
- geometry-minimum failures
- shot coverage generation
- walkthrough sequence presence

## Step 5 — Run required commands

```bash
cd ../ai-architect-api && .venv/bin/python -m pytest tests/test_presentation_3d_scene_spec.py -q | tee ../ai-architect-mvp/artifacts/phase6/cp3-phase6-scene-spec-builder/scene-spec-fixtures.log
```

Save one representative generated spec to:

- `artifacts/phase6/cp3-phase6-scene-spec-builder/sample-scene-spec.json`

## Step 6 — Record completion and notify

Create:

- `artifacts/phase6/cp3-phase6-scene-spec-builder/result.json`
- `artifacts/phase6/cp3-phase6-scene-spec-builder/notes.md`

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp3-phase6-scene-spec-builder \
  --role implementer \
  --status READY \
  --summary "CP3 complete. Scene spec builder is deterministic and fixture-backed." \
  --result-file artifacts/phase6/cp3-phase6-scene-spec-builder/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp3-phase6-scene-spec-builder/result.json
```
