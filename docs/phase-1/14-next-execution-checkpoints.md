# 14 - Next Execution Checkpoints

*Updated: Apr 11, 2026*
*Purpose: checkpoint set toi se follow tiep theo de dua `kts.blackbirdzzzz.art` tu production-like MVP thanh public production candidate.*

## Executive Verdict

Tai thoi diem hien tai, du an da qua duoc 3 moc quan trong:

1. `production-like local stack` da pass 5 loops.
2. `LLM provider` da chot va verify duoc (`gpt-5.4` qua `https://llm.chiasegpu.vn/v1`).
3. `remote GPU runtime` da verify duoc tren ChiaseGPU A5000, va `Cloudflare runtime` da verify duoc tren host local.

Dieu nay co nghia la toi co the tiep tuc dev end to end ma khong can them thong tin truy cap moi cho:

- GPU container
- Cloudflare zone/tunnel runtime

## Current Truth By Original Checkpoint

### CP1 Foundation

Trang thai: `mostly done`

Da dat:

- auth
- project CRUD
- Alembic
- RBAC
- Celery
- MinIO presign
- OpenAPI
- web/app shell

Con thieu de close dep:

- Socket.io end-to-end
- FE OpenAPI type generation
- FE base system cleanup

### CP2 Intake & Brief

Trang thai: `partially done, now materially unblocked`

Da dat:

- intake chat shell
- brief save/edit
- provider LLM da verify

Con thieu:

- OpenAI-compatible runtime adapter that
- streaming chat
- Requirements Agent
- form wizard day du
- context management

### CP3 2D Generation & Gallery

Trang thai: `partially done, now partially unblocked`

Da dat:

- generate 3 options placeholder
- gallery
- selection flow
- remote GPU smoke
- PyTorch CUDA smoke on A5000

Con thieu:

- remote GPU integration that vao backend
- queue/progress realtime
- real generation pipeline
- recovery ladder

### CP4 Review & Revision

Trang thai: `MVP-usable`

Da dat:

- annotation
- approve/reject/revise
- share link
- feedback
- lineage
- review workspace

Con thieu:

- compare 2 versions
- notification panel polish
- revision intelligence nang hon

### CP5 3D, Export & Delivery

Trang thai: `usable but placeholder-heavy`

Da dat:

- PDF/SVG export
- placeholder derive 3D
- handoff creation
- viewer route

Con thieu:

- delivery workspace hoan chinh
- handoff browse/download polish
- Blender/render pipeline that neu bam dung CP5 goc

### CP6 Polish & Launch

Trang thai: `partially done, now materially unblocked`

Da dat:

- production-like deploy
- browser verification
- 5 loops pass
- Cloudflare runtime verified
- zone/tunnel verified
- hostname `kts.blackbirdzzzz.art` hien trong trang thai chua ton tai record

Con thieu:

- public onboarding cho hostname
- GHCR/linuxvm workflow alignment
- staging
- monitoring
- backup target
- load test

## Remaining Real Blockers

Chi con 4 blocker that can tac dong den toc do hoac scope:

### B1. GPU CPU quota

GPU container moi hien tai co:

- `1 x RTX A5000`
- `32 GB RAM`
- `80 GB disk`
- `1 vCPU` quota that

Tac dong:

- du cho smoke/integration
- khong ly tuong cho ComfyUI full setup

Khuyen nghi:

- resize len `4-8 vCPU` truoc khi toi dua ComfyUI/ControlNet vao critical path

### B2. Production secret persistence

Toi co the develop voi key da duoc cung cap trong chat.
Nhung de public production, key LLM van can duoc dat vao runtime secret store.

### B3. Monitoring + backup

Toi chua co:

- `Sentry DSN`
- backup target chot

### B4. CP5 strict scope

Neu ban bat buoc bam 100% CP5 goc theo nghia:

- Blender headless
- exterior/interior renders production quality

thi toi can them runtime thich hop hon hoac mot checkpoint nang rieng.

## New Execution Checkpoints

Toi chot bo checkpoint tiep theo nhu sau.
Day la bo toi se follow truc tiep trong nhung luot dev ke tiep.

## ECP-1 Runtime Wiring

### Goal

Dong cac lo hong nen tang con lai de repos co contract runtime nhat quan.

### Scope

- FE OpenAPI type generation
- backend/frontend socket or websocket end-to-end
- env contract cleanup cho local, production-like, remote GPU
- GPU SSH/passwordless access harden

### Done when

- FE build doc type tu OpenAPI that
- event channel chat/progress di duoc tu backend toi frontend
- env examples khop runtime that

## ECP-2 LLM Intake v1

### Goal

Bien CP2 tu placeholder thanh runtime that.

### Scope

- adapter OpenAI-compatible cho `llm.chiasegpu.vn`
- model mac dinh `gpt-5.4`
- chat streaming
- brief parse/update
- Requirements Agent MVP
- form wizard hoan chinh

### Done when

- user co the chat that voi AI
- brief duoc tao/sua that bang LLM
- frontend intake co chat va form deu dung duoc

## ECP-3 Remote GPU Integration v1

### Goal

Noi backend voi GPU boundary remote thay vi placeholder local.

### Scope

- config `GPU_SERVICE_URL` tro toi ChiaseGPU
- health/progress/error handling
- fallback local mode
- metadata logging

### Done when

- backend generate flow goi duoc remote GPU
- browser flow van pass sau khi doi boundary
- health va smoke tests chay qua remote endpoint

## ECP-4 Generation Pipeline v1

### Goal

Co generation that tren GPU cho CP3, khong con chi la SVG placeholder.

### Scope

- uu tien practical path:
  - bat dau bang minimal real pipeline tren A5000
  - sau do moi nang cap len ComfyUI/ControlNet
- progress reporting
- retry/recovery co ban

### Done when

- `POST /generate` tra ve output image that
- 3 option generation chay duoc o quy mo test
- progress UI nhan duoc stage/progress that

### Gate

Neu `1 vCPU` lam nghen runtime, resize container truoc khi dong checkpoint nay.

## ECP-5 Review Completion

### Goal

Close CP4 cho ban MVP release manh hon.

### Scope

- compare 2 versions
- notification bell/dropdown
- review UX polish
- revision loop reliability

### Done when

- review + feedback + revision + lineage di duoc trong 1 loop browser that

## ECP-6 Delivery Lane

### Goal

Close CP5 theo lane co gia tri giao hang truoc.

### Scope

- delivery workspace UI
- handoff listing/download
- viewer polish
- export/handoff reliability

### Done when

- handoff bundle tao/xem/tai duoc
- export PDF/SVG/model placeholder on dinh

### Note

Neu ban yeu cau CP5 strict full render:

- tao them `ECP-6B Blender Render`
- khong chen vao critical path cua launch MVP neu chua can

## ECP-7 Public Production

### Goal

Chuyen tu production-like sang public production candidate.

### Scope

- align GHCR/linuxvm deploy files
- onboard `kts.blackbirdzzzz.art` vao Cloudflare Tunnel
- deploy public
- public health check
- 5 production loops tren public candidate

### Done when

- `kts.blackbirdzzzz.art` co public route
- health checks pass public
- 5 loops pass

## ECP-8 Hardening

### Goal

Close CP6 con lai sau khi public candidate da song.

### Scope

- Sentry
- backup automation
- staging/domain conventions
- load test
- security checklist

### Done when

- monitoring nhan duoc event
- backup path chay duoc
- load script co baseline

## What I Need From You Only If We Hit A Gate

Mac dinh toi co the tiep tuc ngay.
Chi can ban can thiep neu gap 1 trong cac gate sau:

1. GPU container can resize CPU len `4-8 vCPU`.
2. Ban muon CP5 strict full Blender/render thay vi lane MVP.
3. Ban cung cap `Sentry DSN`.
4. Ban chot backup target.

## Recommended Order

Thu tu toi se follow:

1. `ECP-1 Runtime Wiring`
2. `ECP-2 LLM Intake v1`
3. `ECP-3 Remote GPU Integration v1`
4. `ECP-4 Generation Pipeline v1`
5. `ECP-5 Review Completion`
6. `ECP-6 Delivery Lane`
7. `ECP-7 Public Production`
8. `ECP-8 Hardening`

## Final Decision

Toi se dung bo checkpoint `ECP-1 -> ECP-8` nay lam execution track moi.

Ly do:

- bam sat spirit cua `CP1 -> CP6`
- phan biet ro cai da verify that va cai moi la assumption
- giu duoc duong ra san pham end-to-end thay vi bi ket o nhung phan render nang khong can block launch
