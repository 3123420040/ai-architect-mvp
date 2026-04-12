# 09 - Checkpoint Unblock Matrix

*Updated: Apr 11, 2026*
*Source of truth: [implementation/05-checkpoints.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/05-checkpoints.md:1)*

## How To Read This

- `Implemented now`: da co trong code va da duoc verify.
- `I can continue directly`: khong can them input tu ban, toi co the tiep tuc lam tiep trong workspace.
- `Blocked by external input`: can ban cung cap ha tang, credential, quyet dinh, hoac quyen truy cap de toi dong tiep checkpoint.

## CP1 - Foundation

### Implemented now

- FastAPI project structure + `/health`
- PostgreSQL model layer
- Alembic migration baseline
- Auth register/login/refresh
- Project CRUD
- RBAC dependency + admin route
- Redis + Celery worker + real task execution
- MinIO presigned upload service
- OpenAPI export
- Docker local + production-like compose

### I can continue directly

- Socket.io server/client setup end-to-end
- FE OpenAPI type generation script
- FE base component system cleanup theo checkpoint

### Blocked by external input

- Khong co blocker bat buoc o CP1.
- Local MinIO presign tren Docker Desktop can 1 endpoint chung cho ca host va container.

Ban can lam gi de unblock hoan toan:

1. Cung cap hoac chap nhan 1 LAN endpoint on dinh cho local MinIO presign, vi du `MINIO_INTERNAL_ENDPOINT_URL=http://192.168.1.88:19000` va `MINIO_PUBLIC_ENDPOINT_URL=http://192.168.1.88:19000`.

## CP2 - Intake & Brief

### Implemented now

- Chat intake page
- Brief JSON parse/update/save
- Brief editor
- Backend websocket stub cho chat stream

### I can continue directly

- Form wizard day du
- Sidebar/project nav polish
- Brief summary card refinement
- OpenAI-compatible LLM adapter cho `https://llm.chiasegpu.vn/v1`
- GPT-5.4 intake/runtime wiring cho development

### Blocked by external input

- LangGraph + Requirements Agent that
- LLM streaming chat that
- Context management L1/L2 dung spec

Ban can lam gi de unblock:

1. Nha cung cap LLM da co the chot: OpenAI-compatible endpoint `https://llm.chiasegpu.vn/v1`.
2. Model da verify duoc tren endpoint: `gpt-5.4`.
3. Development co the tiep tuc bang key da cung cap trong chat, nhung production van can dat key vao runtime secret store.
4. Neu co rate limit/budget, gui them cho toi de toi dat policy retry/timeouts dung.

## CP3 - 2D Generation & Gallery

### Implemented now

- Generate 3 options
- Option gallery
- Selection flow
- Version status transitions
- ChiaseGPU A5000 remote GPU smoke da verify
- PyTorch CUDA smoke da pass tren container A5000

### I can continue directly

- Progress UI polish
- Error state/recovery UI
- Metadata logging mo rong
- Remote GPU boundary integration vao backend
- Minimal GPU runtime bring-up tren A5000

### Blocked by external input

- ComfyUI / ControlNet / SDXL pipeline that
- Queue/progress realtime dung spec
- Recovery Level 1-4 based on model/pipeline that

Ban can lam gi de unblock:

1. GPU target da chot: ChiaseGPU `1 x RTX A5000`.
2. Container moi hien co `32 GB RAM`, `80 GB disk`, nhung CPU quota that la `1 vCPU`; du cho smoke/integration, chua tot cho ComfyUI full stack. Neu muon toi di thang vao pipeline that, nen resize len it nhat `4-8 vCPU`.
3. Cung cap model artifact path va license approval.
4. Chot workflow repo / checkpoint JSON cho ComfyUI neu muon toi implement dung stack da chon.

## CP4 - Review & Revision

### Implemented now

- Annotation CRUD
- Approve / reject / revise
- Share link + token auth
- Feedback submission
- Version lineage
- Notification backend
- Review workspace frontend

### I can continue directly

- Compare 2 versions
- Notification bell/dropdown full feature
- Review UX polish

### Blocked by external input

- Khong co blocker ha tang bat buoc cho phan review core.

## CP5 - 3D, Export & Delivery

### Implemented now

- PDF export
- SVG export
- 3D derivation placeholder
- Handoff creation
- Viewer route

### I can continue directly

- Delivery workspace UI
- Handoff listing/download endpoints
- Viewer polish

### Blocked by external input

- Blender headless pipeline that
- Exterior/interior renders production quality
- GLTF optimization dung target

Ban can lam gi de unblock:

1. Cung cap GPU/Blender runtime target.
2. Chot acceptable 3D scope cho Phase 1: placeholder geometry hay photoreal pipeline.
3. Chot render quality target va thời gian render chap nhan duoc.

## CP6 - Polish & Launch

### Implemented now

- Production-like Docker deployment qua Caddy
- Browser verification tren production build
- 5 production-like loops pass
- Runtime bugfix loop duoc thuc hien lien tuc
- Cloudflare runtime credentials verified locally
- Cloudflare zone va ca primary/standby tunnel da verify bang API
- `kts.blackbirdzzzz.art` hien chua co DNS record, san sang cho onboarding

### I can continue directly

- Staging compose/profile
- Backup scripts
- Load-test script
- Security checklist doc va hardening tiep
- Cloudflare hostname onboarding cho `kts.blackbirdzzzz.art`
- GHCR/linuxvm production workflow alignment

### Blocked by external input

- Sentry / monitoring account
- Backup storage target
- Staging domain

Ban can lam gi de unblock:

1. Production path chuan cua Blackbird da chot la `GitHub main -> GHCR -> linuxvm -> Cloudflare Tunnel`.
2. Cloudflare access da co san tren host nay; toi co the tu tiep tuc phan DNS/tunnel onboarding.
3. Cung cap DSN/credential cho monitoring.
4. Cung cap dich den backup: S3 / R2 / Drive / server.
5. Neu ban van muon bam dung CP6 goc thay vi platform chuan hien tai, khi do moi can cap credential rieng cho:
   - web: Vercel
   - api: Railway
   - gpu: RunPod

## My Responsibility vs Your Responsibility

### Toi se tiep tuc chiu trach nhiem

- implementation code
- bugfix loop
- deploy script / Docker path
- staging/prod-like verification
- checkpoint tracking va readiness report

### Ban can cung cap de toi dong cac checkpoint bi block

- domain/DNS access
- cloud credentials
- LLM/API keys
- GPU runtime that
- model/workflow artifact duoc phep dung

## Immediate Next Best Route

Neu ban muon toi tiep tuc theo dung tinh than “end to end toi production”, thu tu unblock tot nhat la:

1. Toi tiep tuc wiring LLM va remote GPU runtime that.
2. Neu can pipeline generation full, ban resize GPU container len it nhat `4-8 vCPU`.
3. Toi thay deterministic placeholders bang runtime that.
4. Toi onboard public hostname, deploy production, chay lai validation, va cap nhat readiness report.
