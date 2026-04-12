# Checkpoint System — AI Architect MVP / Phase 1

## Tong quan luong lam viec

```text
[Implementation Agent]     [User]        [Validator Agent]
        |                    |                   |
        | implement CP-N     |                   |
        |------------------->|                   |
        | write result.json  |                   |
        | run notify.py      |                   |
        |------------------->| notification      |
        |                    | trigger validate  |
        |                    |------------------>|
        |                    |                   | run CHECKLIST
        |                    |                   | write validation.json
        |                    |<------------------|
        | trigger next CP    |                   |
```

## Gia dinh workspace

Chay cac lenh tu root cua repo nay: `/Users/nguyenquocthong/project/ai-architect-mvp`

Target repos duoc clone song song cung cap:

- `../ai-architect-web`
- `../ai-architect-api`
- `../ai-architect-gpu`

## Mapping voi `implementation/05-checkpoints.md`

| Macro CP | Sub CP |
|----------|--------|
| CP1 Foundation | CP0, CP1, CP2, CP3, CP4 |
| CP2 Intake & Brief | CP5, CP6 |
| CP3 Generation & Gallery | CP7, CP8 |
| CP4 Review & Revision | CP9, CP10 |
| CP5 3D, Export & Delivery | CP11, CP12 |
| CP6 Polish & Launch | CP13 |

## Checkpoints

| CP | Ten | Noi dung | Depends On | Effort |
|----|-----|----------|------------|--------|
| CP0 | Environment Setup | Tao workspace, env files, local dependencies, shared scripts | — | 0.5 ngay |
| CP1 | Backend Bootstrap | FastAPI skeleton, health, OpenAPI, Celery/storage skeleton | CP0 | 0.5-1 ngay |
| CP2 | Data/Auth/Permissions | Alembic, core tables, auth flow, roles, state machine, audit | CP1 | 1 ngay |
| CP3 | Frontend Shell/Auth | Next.js shell, tokens, auth UI, base query/socket setup | CP2 | 1 ngay |
| CP4 | Project Workspace/Contracts | Project CRUD UI+API, typed contracts, dashboard shell | CP3 | 1 ngay |
| CP5 | Intake Brief Backend | Query loop, brief tools, chat history, brief endpoints | CP4 | 1 ngay |
| CP6 | Intake UI/Brief Editor | Chat UI, form wizard, brief editor, intake E2E | CP5 | 1 ngay |
| CP7 | GPU Workflow Base | GPU wrapper, ComfyUI, workflow JSON, progress callback | CP6 | 1 ngay |
| CP8 | Generation/Gallery Selection | Queue -> generate -> 3 versions -> select option | CP7 | 1 ngay |
| CP9 | Review/Annotation/Approval | Review workspace, annotation CRUD, lock flow | CP8 | 1 ngay |
| CP10 | Share/Feedback/Revision | Share token, feedback, revision lineage, notifications | CP9 | 1 ngay |
| CP11 | Export/Bundle/Readiness | PDF/SVG export, readiness rules, handoff bundle | CP10 | 1 ngay |
| CP12 | 3D Derivation/Viewer | Locked version -> renders/GLTF -> viewer | CP11 | 1 ngay |
| CP13 | Hardening/Staging/Launch | CI/CD, staging, monitoring, QA gates, launch check | CP12 | 1 ngay |

## Cau truc moi CP folder

```text
docs/phases/phase-1/checkpoints/cpN-name/
├── README.md
├── INSTRUCTIONS.md
├── CHECKLIST.md
├── result.json
└── validation.json
```

## Setup

```bash
cp docs/phases/phase-1/checkpoints/config.example.json \
   docs/phases/phase-1/checkpoints/config.json

# Sua ntfy_topic va project_slug truoc khi dung notification/dashboard
```
