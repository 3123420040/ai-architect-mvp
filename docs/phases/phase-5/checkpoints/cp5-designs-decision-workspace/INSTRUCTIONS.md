# CP5 — Designs Decision Workspace

**Objective:** Rebuild the Designs screen into a decision workspace that helps the user compare and choose.
**Requires:** CP4 PASS.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp5-designs-decision-workspace/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP5 — Designs Decision Workspace",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Change the page role

Read first:

- `implementation/phase-5/04-phase-5-option-generation-deep-dive.md`
- `implementation/phase-5/05-phase-5-option-strategy-decision-metadata-slice.md`

Update `../ai-architect-web/src/components/designs-client.tsx` so the page communicates:

- current stage,
- what the user should decide,
- what makes each option different,
- what happens after selection.

The page should no longer feel like a raw gallery.

## Step 2 — Enrich option cards

Each option card should have:

- preview,
- localized title,
- strategy summary,
- a short metrics block,
- strengths,
- caveats,
- compare action,
- primary select action.

The card content must be derived from generation metadata that expresses:

- strategy,
- rationale,
- metrics,
- strengths,
- caveats,
- and fit-to-brief explanation where feasible.

Prioritize the serialized top-level fields defined by the implementation slice.

If missing metadata is needed, update backend payloads in:

- `../ai-architect-api/app/api/v1/projects.py`
- `../ai-architect-api/app/api/v1/generation.py`

Do not stop at simple relabeling. The output should stop reading like `Option A for <project_id>`.

## Step 3 — Add compare support

Implement at least a lightweight compare mode for two options.

It can be:

- side-by-side expanded cards,
- or a dedicated compare panel.

The compare view must use meaningful differences, not just duplicate thumbnails.

## Step 4 — Verify locally

```bash
cd ../ai-architect-web && pnpm build
```

Also verify that the backend still returns the metadata the frontend expects.
The page must visibly consume strategy profile and decision metadata, not just pass them through the response.

## Step 5 — Record completion

Create `docs/phases/phase-5/checkpoints/cp5-designs-decision-workspace/result.json`.

```json
{
  "cp": "cp5-designs-decision-workspace",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Designs is now a decision workspace with compare and clearer review handoff.",
  "artifacts": [
    {"file": "../ai-architect-web/src/components/designs-client.tsx", "action": "updated"},
    {"file": "../ai-architect-api/app/api/v1/projects.py", "action": "updated"},
    {"file": "../ai-architect-api/app/api/v1/generation.py", "action": "updated"},
    {"file": "../ai-architect-web/src/components/status-badge.tsx", "action": "updated"}
  ],
  "issues": [],
  "notes": "The final page should support option choice, not just option browsing, and the options must stop looking like placeholder variants."
}
```

```bash
uv run python docs/phases/phase-5/checkpoints/notify.py \
  --cp cp5-designs-decision-workspace \
  --role implementer \
  --status READY \
  --summary "Designs is now a decision workspace with compare and clearer review handoff." \
  --result-file docs/phases/phase-5/checkpoints/cp5-designs-decision-workspace/result.json

python3 docs/phases/phase-5/checkpoints/post-status.py \
  --result-file docs/phases/phase-5/checkpoints/cp5-designs-decision-workspace/result.json
```
