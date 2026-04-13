# CP0 — Scope Lock and Production Truth

**Objective:** Lock the exact Phase 5 contract before code work starts.
**Requires:** None.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp0-phase5-scope-truth/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP0 — Scope Lock and Production Truth",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Review evidence

Read:

- `implementation/phase-3/06-status-audit-20260412.md`
- `implementation/phase-4/01-phase-4-analysis-brief.md`
- `implementation/phase-4/02-phase-4-implementation-detailed.md`
- the latest intake/designs production analysis notes

Lock the Phase 5 narrative around:

- intake clutter outside chat,
- brief-lock ambiguity,
- wrong generation/review sequence,
- weak Designs workspace UX.

## Step 2 — Write phase documents

Create or update:

- `implementation/phase-5/00-README.md`
- `implementation/phase-5/01-phase-5-analysis-brief.md`
- `implementation/phase-5/02-phase-5-implementation-detailed.md`
- `implementation/phase-5/03-phase-5-checkpoint-execution-plan.md`
- `docs/phases/phase-5/checkpoints/README.md`

## Step 3 — Record completion

Create `docs/phases/phase-5/checkpoints/cp0-phase5-scope-truth/result.json`.

```json
{
  "cp": "cp0-phase5-scope-truth",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Phase 5 scope and production-truth contract are locked.",
  "artifacts": [
    {"file": "implementation/phase-5/00-README.md", "action": "created"},
    {"file": "implementation/phase-5/01-phase-5-analysis-brief.md", "action": "created"},
    {"file": "implementation/phase-5/02-phase-5-implementation-detailed.md", "action": "created"},
    {"file": "implementation/phase-5/03-phase-5-checkpoint-execution-plan.md", "action": "created"},
    {"file": "docs/phases/phase-5/checkpoints/README.md", "action": "created"}
  ],
  "issues": [],
  "notes": "Phase 5 is intentionally limited to clarification and option-decision hardening."
}
```

```bash
uv run python docs/phases/phase-5/checkpoints/notify.py \
  --cp cp0-phase5-scope-truth \
  --role implementer \
  --status READY \
  --summary "Phase 5 scope and production-truth contract are locked." \
  --result-file docs/phases/phase-5/checkpoints/cp0-phase5-scope-truth/result.json

python3 docs/phases/phase-5/checkpoints/post-status.py \
  --result-file docs/phases/phase-5/checkpoints/cp0-phase5-scope-truth/result.json
```
