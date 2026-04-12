# 08 - Production Readiness Report

*Updated: Apr 11, 2026*
*Product: `kts.blackbirdzzzz.art`*

## Verdict

Trang thai hien tai la **release candidate production-like da chay duoc** tren Docker stack local qua Caddy, khong phai production public Internet hoan chinh.

Da dat duoc:

- web, api, gpu, postgres, redis chay on dinh qua `docker-compose.production.yml`
- worker Celery that chay tren local va production-like stack
- gateway Caddy route duoc theo host `kts.blackbirdzzzz.art`
- browser flow production build di duoc den review workspace
- 5/5 production-like loops pass lien tiep
- Alembic migration upgrade/downgrade pass trong test
- RBAC middleware duoc enforce va co test
- MinIO presigned upload round-trip pass tren local stack

Chua dat duoc:

- DNS public cho `kts.blackbirdzzzz.art`
- SSL/HTTPS that cho domain public
- deploy len Vercel/Railway/RunPod theo CP6 goc
- monitoring/alerting, backup automation, staging env, load test 50 concurrent

## Evidence

- Production-like compose: [docker-compose.production.yml](/Users/nguyenquocthong/project/ai-architect-mvp/docker-compose.production.yml:1)
- Gateway config: [infra/Caddyfile](/Users/nguyenquocthong/project/ai-architect-mvp/infra/Caddyfile:1)
- 5-loop report: [latest-report.json](/Users/nguyenquocthong/project/ai-architect-mvp/artifacts/production-checks/latest-report.json:1)
- Browser screenshot: [review-screenshot](/Users/nguyenquocthong/project/ai-architect-mvp/.playwright-cli/page-2026-04-11T13-44-48-193Z.png)
- Repeatable loop runner: [production_check_loops.py](/Users/nguyenquocthong/project/ai-architect-mvp/scripts/production_check_loops.py:1)
- Alembic config: [alembic.ini](/Users/nguyenquocthong/project/ai-architect-api/alembic.ini:1)
- Foundation tests: [test_foundation.py](/Users/nguyenquocthong/project/ai-architect-api/tests/test_foundation.py:1)

## What Was Verified

### Automated API / asset loop

Da verify end-to-end qua host header `kts.blackbirdzzzz.art`:

1. homepage
2. backend health
3. auth register/login/refresh
4. create project
5. update brief
6. chat intake
7. generate 3 options
8. select option
9. create annotation
10. approve + lock
11. create share link
12. public share view
13. submit feedback
14. create revision
15. export PDF + SVG
16. fetch exported assets
17. derive 3D
18. fetch model + render assets
19. create handoff
20. read notifications

Ket qua: **5/5 loops passed**.

### Browser flow on production build

Da verify bang Playwright tren `http://localhost` (artifact production build sau Caddy):

1. register workspace
2. vao dashboard
3. tao project
4. chat intake
5. generate 3 options
6. select option
7. vao review workspace va thay floor plan

### Foundation runtime verification

Da verify them:

1. Alembic `upgrade head` va `downgrade base`
2. RBAC chan `user` o write endpoints va chi cho `admin` vao admin endpoints
3. Celery worker ket noi Redis va xu ly `system.ping`
4. MinIO presign tao duoc URL, upload file that, download lai duoc file

## Bugs Fixed During Release Hardening

1. Feedback API response thieu `status`, lam production loop va UI khong co contract nhat quan.
2. Share-link validation crash do compare `datetime` aware/naive giua SQLite/Postgres behavior.
3. Caddy auto-HTTPS bi ACME fail vi domain chua co DNS public.
4. Frontend production build bake sai `NEXT_PUBLIC_API_URL`, dan den browser prod-like goi `localhost:18000` va bi CORS.
5. ORM defaults dung `datetime.utcnow()` gay warning timezone va tang risk drift.
6. Worker Docker image chay root gay warning Celery; da chuyen sang ha quyen qua `--uid/--gid` ma khong pha storage volume.
7. MinIO presigned URL bi sai trong Docker Desktop khi ky bang host noi bo; da xac dinh va verify cach dung LAN endpoint.

## Checkpoint Status Against `implementation/05-checkpoints.md`

| Checkpoint | Status | Note |
|---|---|---|
| CP1 Foundation | Partial | Da co auth, project CRUD, app shell, OpenAPI, Alembic, RBAC, Celery worker that, MinIO presign. Chua co Socket.io end-to-end, FE socket client, shadcn/base system day du, OpenAPI type generation script. |
| CP2 Intake & Brief | Partial | Co chat intake, brief JSON, brief edit/save. Chua co LangGraph, streaming WebSocket, context management L1-L2, form wizard day du. |
| CP3 2D Generation & Gallery | Partial | Co generate 3 options, gallery, selection, version statuses. Chua co queue/progress realtime, fallback recovery, ComfyUI/ControlNet that. |
| CP4 Review & Revision | Mostly done cho MVP | Co annotation, approve/reject/revise, share link, feedback, notifications, review workspace. Chua co compare 2 versions va notification panel day du. |
| CP5 3D, Export & Delivery | Partial | Co export PDF/SVG, derive 3D placeholder, handoff, viewer route. Chua co Blender headless, production render quality, delivery workspace. |
| CP6 Polish & Launch | Partial | Co production-like deploy, browser verification, 5 loops pass, bugfix release hardening. Chua co public DNS/SSL, Sentry, backup automation, staging, load test 50 concurrent. |

## Current Release Boundary

Ban co the coi san pham hien tai la:

- mot **Phase 1 MVP runnable**
- co **frontend + backend + gpu boundary + storage assets**
- co **production-like deployment path qua Docker + Caddy**
- co **repeatable verification loop**

Ban khong nen coi no la:

- public SaaS da launch
- he thong da dat toan bo CP6 goc
- deployment public domain da xong

## Recommended Next Steps

1. Cap DNS `A/AAAA` cho `kts.blackbirdzzzz.art`.
2. Chon dich vu production that cho web/api/gpu va cap credentials deploy.
3. Them Sentry, backup script, staging compose/env.
4. Them load test script 50 concurrent users.
5. Replace deterministic AI placeholder bang ComfyUI/ControlNet pipeline that neu muon dung dung vision CP3-CP5.
