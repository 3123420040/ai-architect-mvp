# CP13 — Hardening + Staging + Launch

**Muc tieu:** Chot launch readiness cho MVP sau khi tat ca feature slice da xong
**Requires:** CP12 PASS

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp13-hardening-staging-launch/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Bat dau implement CP13 — Hardening + Staging + Launch",
    "readyForNextTrigger": false
  }' || true
```

## Buoc 1 — Chot CI/CD, monitoring, backup

Can cu:

- `implementation/08-deployment-guide.md` muc `4`, `5`, `6`, `7`, `8`, `9`
- `implementation/09-testing-strategy.md` muc `5`

Implement:

- GitHub Actions CI va deploy
- staging env
- Sentry/health checks
- backup script/hook
- alerting co ban
- `docs/launch-checklist.md` trong repo backend, danh dau lai tung gate launch that su

## Buoc 2 — Chot quality gates

```bash
cd ../ai-architect-api && pytest tests/ -q --cov=app
cd ../ai-architect-web && pnpm exec playwright test
test -f ../ai-architect-api/.github/workflows/ci.yml
test -f ../ai-architect-api/.github/workflows/deploy.yml
```

Neu staging da co:

```bash
curl -fsS https://staging.aiarchitect.vn
curl -fsS https://api-staging.aiarchitect.vn/health
```

## Buoc 3 — Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp13-hardening-staging-launch/result.json`.

```json
{
  "cp": "cp13-hardening-staging-launch",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "CI/CD, staging, monitoring, backup va launch checklist da xong.",
  "artifacts": [
    {"file": "../ai-architect-api/.github/workflows/ci.yml", "action": "created"},
    {"file": "../ai-architect-api/.github/workflows/deploy.yml", "action": "created"},
    {"file": "../ai-architect-web/e2e", "action": "updated"},
    {"file": "../ai-architect-api/scripts/backup.sh", "action": "created"},
    {"file": "../ai-architect-api/docs/launch-checklist.md", "action": "created"}
  ],
  "issues": [],
  "notes": "Neu staging URL khac, cap nhat config va checklist truoc launch."
}
```

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp13-hardening-staging-launch \
  --role implementer \
  --status READY \
  --summary "Hardening, staging va launch gates da xong." \
  --result-file docs/phases/phase-1/checkpoints/cp13-hardening-staging-launch/result.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp13-hardening-staging-launch/result.json
```
