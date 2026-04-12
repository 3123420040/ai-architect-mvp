# 12 - Production Direction Decision

*Updated: Apr 11, 2026*
*Supersedes CP6 hosting assumptions where they conflict with the current Blackbird deploy platform.*

## Final Decision

### 1. Production path

Production chuan cho `kts.blackbirdzzzz.art` se la:

`GitHub main -> GHCR image -> linuxvm primary runtime -> Cloudflare Tunnel ingress`

Day la huong dung voi deploy control-plane hien tai cua Blackbird, khong phai `Vercel + Railway + RunPod` la default nua.

Co so de chot huong nay:

- Deploy platform noi bo da mac dinh `linuxvm` la primary runtime, `GHCR` la registry, va `Cloudflare` la public ingress.
- Platform automation hien tai da co onboarding flow cho hostname, tunnel route, GitHub bootstrap, standby sync, backup, va production audit.
- Tai lieu platform hien tai ghi ro cac duong deploy cu qua ChiaseGPU/host khac la historical, khong dung lam instruction production.

Internal references:

- [Shared deploy platform README](/Users/nguyenquocthong/project/openclaw/topics/deploy-platform/README.md:1)
- [Platform automation guide](/Users/nguyenquocthong/project/openclaw/topics/deploy-platform/AUTOMATION.md:1)

### 2. DNS / domain decision

Khong chot theo huong `A/AAAA` tro thang vao host neu khong co ly do dac biet.

Huong chuan la:

- `kts.blackbirdzzzz.art` duoc map vao `Cloudflare Tunnel`
- Cloudflare tao DNS record tro toi tunnel subdomain
- traffic vao Cloudflare truoc, sau do moi vao service tren `linuxvm`

He qua thuc thi:

- Thu ban can cap cho toi khong phai chi la public IP cua host.
- Thu toi can de unblock la Cloudflare zone/tunnel access, cu the:
  - `CF_ACCOUNT_ID`
  - `CF_ZONE_ID`
  - `CF_TUNNEL_ID`
  - `CF_API_TOKEN`
- Quyen toi thieu khuyen nghi cho `CF_API_TOKEN`:
  - `Account -> Cloudflare Tunnel -> Edit`
  - `Zone -> DNS -> Edit`

Neu ban muon tu lam phan nay:

1. Tao hoac chon tunnel dang dung cho domain `blackbirdzzzz.art`.
2. Publish hostname `kts.blackbirdzzzz.art` vao local service tren `linuxvm`.
3. Tao DNS route/CNAME qua Cloudflare Tunnel cho hostname do.
4. Gui lai cho toi xac nhan hostname da route xong de toi tiep tuc deploy app.

## Legacy CP6 Stack

`Vercel + Railway + RunPod` khong bi loai bo hoan toan, nhung chi nen xem la legacy reference hoac fallback deployment model neu ban co ly do rieng de bam dung tài liệu cu.

Khi nao nen dung fallback nay:

- Ban muon tach web/api/gpu thanh 3 nen tang hosting doc lap.
- Ban khong muon dua app vao `linuxvm`.
- Ban muon bam sat document CP6 goc hon la shared platform hien tai.

Neu di theo fallback nay, ban moi can cap credential rieng cho `Vercel`, `Railway`, `RunPod`.

## LLM Decision

### Chot provider

CP2 se di theo huong `OpenAI-compatible endpoint`, su dung:

- Base URL: `https://llm.chiasegpu.vn/v1`
- Model da probe duoc: `gpt-5.4`
- Secret: key ban vua gui

Toi khong lap lai day du key trong docs/chat va khong commit key vao repo.

### Cach toi se implement

- Them provider adapter OpenAI-compatible trong backend
- Doc secret tu runtime env/secret store
- Dat `gpt-5.4` lam model mac dinh cho CP2/CP3 phan text orchestration
- Dung provider nay cho intake chat, brief parsing, va LangGraph streaming

Ban can lam de unblock phan nay:

1. Dat key vao runtime secret store cua nen tang deploy, khong dua vao git.
2. Neu co rate limit/budget, gui them cho toi de toi dat policy retry/timeouts dung.
3. Neu ban muon model khac `gpt-5.4`, gui lai ket qua `/models` sau khi cap them model o endpoint.

## Minimal GPU For Real Test

### Neu chi giu stack deterministic hien tai

Khong can GPU. Ban production-like local hien tai van chay duoc de kiem tra flow nghiep vu.

### Neu chay CP3 that voi ComfyUI + SDXL + 1 ControlNet

Toi chot cau hinh toi thieu de test that:

- `1 x GPU 24 GB VRAM`
- `8 vCPU`
- `32 GB RAM`
- `80-100 GB SSD`

Class GPU phu hop:

- `RTX 4090`
- `RTX 3090`
- `L4`
- `RTX A5000`

### Neu muon day them sang CP5 3D/render nang

Khuyen nghi nang len:

- `1 x GPU 48 GB VRAM`
- `12+ vCPU`
- `48-64 GB RAM`

Class GPU phu hop:

- `A40`
- `A6000`
- `L40`
- `L40S`

Ly do:

- 24 GB la moc toi thieu hop ly de chay SDXL + ControlNet o muc test/on-demand.
- 48 GB se an toan hon cho workflow nang, queue song song, va Blender/3D render.

## How To Get Legacy Credentials If Needed

### Vercel

Ban can:

1. Tao hoac dang nhap tai khoan Vercel.
2. Tao project, link repo web vao project.
3. Tao token trong `tokens page`.
4. Co the dung `vercel login` cho local interactive, hoac `--token` cho CI.

Thu toi can neu dung Vercel:

- `VERCEL_TOKEN`
- `VERCEL_ORG_ID`
- `VERCEL_PROJECT_ID`

### Railway

Ban can:

1. Tao account/workspace tren Railway.
2. Tao project cho API/worker.
3. Tao `workspace token` hoac `project token` tu dashboard.
4. Luu y `project token` dung header rieng `Project-Access-Token`.

Thu toi can neu dung Railway:

- `RAILWAY_TOKEN` hoac project token tuong ung
- project/environment IDs neu can automation

### RunPod

Ban can:

1. Tao account RunPod.
2. Nap billing neu can deploy GPU that.
3. Vao `Settings -> API Keys -> Create API Key`.
4. Chon permission toi thieu can thiet; khuyen nghi khong dung full-access neu khong can.

Thu toi can neu dung RunPod:

- `RUNPOD_API_KEY`
- target loai runtime: `Pod` hay `Serverless Endpoint`
- GPU class ban chot

## What You Need To Do Now

Toi chot thu tu unblock tot nhat nhu sau:

1. Chon production path chuan: `linuxvm + Cloudflare Tunnel`.
2. Cap Cloudflare runtime access hoac tu route `kts.blackbirdzzzz.art` vao tunnel.
3. Dat LLM key vao production secret store cho provider `llm.chiasegpu.vn`.
4. Chot GPU test that toi thieu: `1 x 24 GB VRAM`.
5. Neu ban khong di theo platform chuan ma van muon CP6 legacy, khi do moi di lay token Vercel/Railway/RunPod.

## Sources

- [Shared deploy platform README](/Users/nguyenquocthong/project/openclaw/topics/deploy-platform/README.md:1)
- [Platform automation guide](/Users/nguyenquocthong/project/openclaw/topics/deploy-platform/AUTOMATION.md:1)
- [Cloudflare Tunnel overview](https://developers.cloudflare.com/tunnel/)
- [Cloudflare published application routing](https://developers.cloudflare.com/tunnel/routing/)
- [Cloudflare Tunnel setup](https://developers.cloudflare.com/tunnel/setup/)
- [Vercel CLI auth and tokens](https://vercel.com/docs/cli)
- [Railway Public API and token types](https://docs.railway.com/guides/public-api)
- [RunPod API key management](https://docs.runpod.io/get-started/api-keys)
- [RunPod GPU types](https://docs.runpod.io/references/gpu-types)

Runtime verification performed on Apr 11, 2026:

- `GET https://llm.chiasegpu.vn/v1/models` -> `gpt-5.4`
- `POST https://llm.chiasegpu.vn/v1/chat/completions` with model `gpt-5.4` -> success
