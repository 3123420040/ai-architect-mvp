# CP5 — Intake Query Loop + Brief Backend

**Muc tieu:** Hoan tat backend cho intake/chat/form -> brief
**Requires:** CP4 PASS

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp5-intake-brief-backend/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Bat dau implement CP5 — Intake Query Loop + Brief Backend",
    "readyForNextTrigger": false
  }' || true
```

## Buoc 1 — Dung query loop va tools

Can cu:

- `implementation/03-architecture-blueprint.md` muc `3.2`
- `implementation/04-implementation-directives.md` muc `3.6`
- `implementation/06-api-contracts.md` muc `4`, `5`

Implement:

- `query_loop.py`
- `requirements_agent.py`
- `BriefParse`, `BriefUpdate`
- `GET/PUT /projects/{id}/brief`
- `POST /projects/{id}/chat`
- `GET /projects/{id}/chat/history`

## Buoc 2 — Test query loop, brief va streaming

```bash
cd ../ai-architect-api
pytest tests/unit/test_query_loop.py tests/unit/test_brief_validation.py -q
pytest tests/integration/test_brief_api.py tests/integration/test_chat_history.py -q
pytest tests/integration/test_chat_stream.py -q
```

## Buoc 3 — Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp5-intake-brief-backend/result.json`.

```json
{
  "cp": "cp5-intake-brief-backend",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Query loop, brief tools, brief API va chat history da xong.",
  "artifacts": [
    {"file": "../ai-architect-api/app/engine/query_loop.py", "action": "created"},
    {"file": "../ai-architect-api/app/agents/requirements_agent.py", "action": "created"},
    {"file": "../ai-architect-api/app/tools/design_brief_tools.py", "action": "created"},
    {"file": "../ai-architect-api/app/api/v1/brief.py", "action": "created"}
  ],
  "issues": [],
  "notes": "Graph state chi giu conversation context; project truth nam trong DB."
}
```

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp5-intake-brief-backend \
  --role implementer \
  --status READY \
  --summary "Backend intake va brief flow da san sang." \
  --result-file docs/phases/phase-1/checkpoints/cp5-intake-brief-backend/result.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp5-intake-brief-backend/result.json
```
