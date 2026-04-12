# ECP Execution Status

*Date: Apr 12, 2026*
*Product: `kts.blackbirdzzzz.art`*

## Summary

Execution track `ECP-1 -> ECP-8` da duoc day toi public production candidate.
He thong hien tai da co public route that tai `https://kts.blackbirdzzzz.art`, remote GPU lane dang tro toi `ChiaseGPU RTX A5000`, va flow core `intake -> generate -> review -> export -> derive 3D -> handoff` da pass tren production-like va dang duoc verify lai tren public hostname.

## Checkpoint Status

| ECP | Status | Notes |
| --- | --- | --- |
| ECP-1 Runtime Wiring | Done | OpenAPI type generation script, WebSocket chat stream, env contract cleanup, remote GPU env wiring da khop runtime that. |
| ECP-2 LLM Intake v1 | Done | Adapter OpenAI-compatible, model `gpt-5.4`, brief parse/update, chat stream, intake form wizard da hoat dong. |
| ECP-3 Remote GPU Integration v1 | Done | Backend dang goi `GPU_SERVICE_URL=http://e1.chiasegpu.vn:10925`, co metadata `generation_source`, va smoke test qua remote endpoint da pass. |
| ECP-4 Generation Pipeline v1 | Done | GPU lane tra output image raster that, gallery nhan progress stream, va loop generation 3 options dang hoat dong. |
| ECP-5 Review Completion | Done | Review workspace co compare, revision lineage, notifications, feedback loop, va browser flow da chay qua. |
| ECP-6 Delivery Lane | Done | Delivery workspace UI, handoff listing, PDF/SVG/GLTF delivery manifest, viewer polish va export reliability da co. |
| ECP-7 Public Production | Done | Public hostname, Cloudflare tunnel rieng, public health check va `5 public loops` da pass. |
| ECP-8 Hardening | Partial | Backup baseline va public load baseline da chay. Sentry event delivery chua the close vi chua co DSN that. |

## Evidence

- Public homepage: `https://kts.blackbirdzzzz.art`
- Public backend health: `https://kts.blackbirdzzzz.art/backend-health`
- Production-like 5 loops:
  - [public-five-loops-20260411.json](/Users/nguyenquocthong/project/ai-architect-mvp/artifacts/production-checks/public-five-loops-20260411.json)
  - [five-loops-20260411.json](/Users/nguyenquocthong/project/ai-architect-mvp/artifacts/production-checks/five-loops-20260411.json)
- Public single debug loop:
  - [public-single-debug-20260411.json](/Users/nguyenquocthong/project/ai-architect-mvp/artifacts/production-checks/public-single-debug-20260411.json)
- Backup baseline:
  - [20260412-002328](/Users/nguyenquocthong/project/ai-architect-mvp/artifacts/backups/20260412-002328)
- Public load baseline:
  - [public-baseline-20260411.json](/Users/nguyenquocthong/project/ai-architect-mvp/artifacts/load-tests/public-baseline-20260411.json)

## Remaining Blockers

### Sentry DSN

Khong the tu dong dong ECP-8 phan monitoring without:

- `SENTRY_DSN` that cho project nay

Neu ban muon close tron ven muc nay, can cung cap DSN de toi:

- cau hinh runtime production
- phat event test
- xac nhan event den dashboard monitoring

### Backup destination policy

Hien tai script backup tao artifact local tren may runtime.
Neu ban muon backup off-host / off-machine dung nghia production, can chot target nhu:

- Cloudflare R2
- S3-compatible bucket
- standby VM / NAS

## Current Runtime Files

- Compose public deploy:
  - [docker-compose.production.yml](/Users/nguyenquocthong/project/ai-architect-mvp/docker-compose.production.yml:1)
- Tunnel bootstrap:
  - [configure_public_tunnel.sh](/Users/nguyenquocthong/project/ai-architect-mvp/scripts/configure_public_tunnel.sh:1)
- Public deploy runner:
  - [deploy_public_production.sh](/Users/nguyenquocthong/project/ai-architect-mvp/scripts/deploy_public_production.sh:1)
- Backup baseline:
  - [backup_production.sh](/Users/nguyenquocthong/project/ai-architect-mvp/scripts/backup_production.sh:1)
- Load baseline:
  - [load_test_public.py](/Users/nguyenquocthong/project/ai-architect-mvp/scripts/load_test_public.py:1)

## Decision

Toi chot rang san pham da dat muc `public production candidate` cho `kts.blackbirdzzzz.art`.
Hang muc chua the dong 100% la `ECP-8 / Sentry monitoring event confirmation` vi thieu secret dau vao that.

## Notes on Verification Topology

`5 public loops` va load baseline public da duoc chay tu host ngoai origin (`ChiaseGPU` container) de tranh hien tuong hairpin transport khi may deploy tu goi nguoc qua Cloudflare roi quay lai chinh no.
Day la evidence sat production hon cho public hostname.
