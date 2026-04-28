# CP7 — Release Readiness and Launch Gate

**Objective:** Freeze Program B Release 1 launch readiness with explicit evidence.
**Requires:** CP6 PASS.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp7-program-b-release-readiness-and-launch-gate/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP7 — Program B release readiness and launch gate",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Evaluate launch thresholds

Use CP6 evidence and mark each threshold:

- `PASS`
- `FAIL`
- `PASS_WITH_LIMITATION`

Thresholds must include:

- benchmark bundle success
- semantic id stability
- schedule completeness
- IFC usefulness for continuation
- issue and readiness visibility
- release wording honesty

## Step 2 — Record remaining blockers and accepted risks

In `closeout.md`, capture:

- blockers still open
- risks accepted for launch
- roadmap items explicitly deferred

## Step 3 — Freeze launch readiness

Create:

- `artifacts/program-b/cp7-program-b-release-readiness-and-launch-gate/result.json`
- `artifacts/program-b/cp7-program-b-release-readiness-and-launch-gate/launch-readiness.json`
- `artifacts/program-b/cp7-program-b-release-readiness-and-launch-gate/closeout.md`

## Step 4 — Notify and post status

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp7-program-b-release-readiness-and-launch-gate \
  --role implementer \
  --status READY \
  --summary "CP7 complete. Program B Release 1 launch readiness is frozen with explicit evidence." \
  --result-file artifacts/program-b/cp7-program-b-release-readiness-and-launch-gate/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp7-program-b-release-readiness-and-launch-gate/result.json
```
