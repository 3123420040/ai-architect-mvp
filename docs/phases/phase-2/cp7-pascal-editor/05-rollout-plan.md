# 05 — Rollout Plan

## 1. Feature flag sequence

| Giai doan | `FF_PASCAL_VIEWER` | `FF_PASCAL_EDIT` | Dai tuong |
|----------|--------------------|------------------|-----------|
| Dev | on | on | Engineering |
| Sau CP7.C PASS — staging | on | off | KTS noi bo |
| Sau CP7.D PASS — staging | on | on | KTS noi bo + 1 beta studio |
| Sau 7 ngay soak staging | on | on | Beta cohort prod (feature flag override per account) |
| Sau 14 ngay soak prod | on | on | All users |
| T+30 ngay post-full-rollout | flag removed | flag removed | Default path, code cleanup |

## 2. Staging soak checklist (7 ngay)

| Day | Check |
|-----|-------|
| D+1 | Khong co crash report tu Sentry, WebGPU init success rate > 95% tren Chrome/Edge |
| D+3 | KTS test tao 5 revision `pascal_edit`, all lineage dung, 0 data loss |
| D+5 | Do bundle size thuc te, API latency `POST /revise-from-scene` p95 < 500ms |
| D+7 | Survey KTS nho (≥3 nguoi), NPS internal ≥ 4/5 moi duoc mo prod |

## 3. Rollback plan

### 3.1 Rollback ca phase (run-time)

- Set `NEXT_PUBLIC_FF_PASCAL_VIEWER=false` va `NEXT_PUBLIC_FF_PASCAL_EDIT=false` qua config + redeploy.
- Fallback tu dong ve `<model-viewer>` + legacy annotate path.
- Data: cac version `generation_source = pascal_edit` van o DB; KHONG xoa. Chi UI path fallback.

### 3.2 Rollback per request (runtime)

- Query param `?fallback=1` force UI sang model-viewer bat ke flag.
- Dung cho case demo client moi ma browser client khong ho tro WebGPU.

### 3.3 Rollback schema (han huu)

- Neu `pascal_edit` value trong enum gay break: migration down khong don gian vi du lieu da ghi.
- Workaround: read-side alias `pascal_edit → manual` khi decode, giu DB nguyen trang; chinh lai code UI chi lam readonly.

## 4. Monitoring

Sau khi bat flag, theo doi:

| Metric | Cong cu | Alert threshold |
|--------|---------|-----------------|
| Pascal viewer init error rate | Sentry tag `viewer=pascal` | > 2% → auto fallback |
| `POST /revise-from-scene` 4xx/5xx | APM | > 1% 5xx trong 1h → page on-call |
| Pascal bundle TTI tren route viewer | Web Vitals | p75 TTI > 4s → warning |
| WebGPU init fail / fall back | Client event `pascal.webgpu.fallback` | log only |
| Revision count split `pascal_edit` vs `ai_generated` | Analytics dashboard | - (KPI tracking) |

## 5. Communication

| Audience | Khi nao | Kenh | Noi dung |
|----------|---------|------|----------|
| KTS noi bo | Sau CP7.D PASS staging | Workspace + demo | Huong dan edit mode, tips undo/redo |
| Khach hang beta | Truoc full rollout 3 ngay | Email + inapp banner | Loi thay doi viewer, browser toi thieu |
| Engineering | Per PR | CODEOWNERS review | Diff review, migration dry-run |

## 6. Kill switch

- Flag off (3.1) la kill switch primary.
- Neu flag infra fail, tam thoi deploy build voi constant `FF_PASCAL_VIEWER=false`.
- Target: rollback toan cuc trong < 10 phut.

## 7. Post-rollout cleanup (T+30)

- Xoa flag va branch code legacy model-viewer.
- Giu `<model-viewer>` loader chi khi vai tro "fallback WebGPU-denied browser".
- Document final state tai `docs/phases/phase-2/cp7-pascal-editor/06-post-rollout-report.md` (tao sau).
