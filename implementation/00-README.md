# AI Architect MVP - Implementation Package

*Ngay chot: Apr 11, 2026*
*Author: System Architect*
*Status: FINAL - Ready for Development*

---

## Muc dich

Day la bo tai lieu duy nhat doi dev can doc de trien khai AI Architect MVP. Moi quyet dinh ky thuat da duoc chot. Dev KHONG can doc lai cac tai lieu research/analysis truoc do.

---

## Thu tu doc

| # | File | Ai doc | Muc dich |
|---|------|--------|----------|
| 01 | `01-SRS-final.md` | **Tat ca** | Yeu cau phan mem cuoi cung - scope, features, constraints |
| 02 | `02-tech-stack-decisions.md` | **Tat ca** | Stack cu the cho tung phan, version, ly do |
| 03 | `03-architecture-blueprint.md` | **Tech Lead + Senior** | Kien truc tong the, module boundaries, data flow |
| 04 | `04-implementation-directives.md` | **Tat ca dev** | Coding standards, patterns bat buoc, do/don't |
| 05 | `05-checkpoints.md` | **PM + Tech Lead** | Checkpoint phat trien, team assignment, merge strategy |
| 06 | `06-api-contracts.md` | **Frontend + Backend** | API endpoints, request/response schemas |
| 07 | `07-database-schema.md` | **Backend** | Database tables, relations, migrations |
| 08 | `08-deployment-guide.md` | **DevOps + Tech Lead** | Infrastructure, CI/CD, production checklist |
| 09 | `09-testing-strategy.md` | **Tat ca dev** | Test strategy, quality gates, coverage targets |
| 10 | `10-p1-2d-deliverable-integration.md` | **Tech Lead + PM** | P1 2D deliverable integration: 3-bac roadmap, geometry Layer 1.5, sheet composition engine |
| 11 | `11-phase2-layer2-full-deliverable.md` | **Tech Lead** | Phase 2 spec: Layer 2 geometry, 4 elevations, DXF, IFC, schedules, full dimension chains |

---

## 3 Git Repos

| Repo | Tech | Team |
|------|------|------|
| `ai-architect-web` | Next.js 14 + React 18 + TypeScript | Frontend Team |
| `ai-architect-api` | FastAPI + Python 3.11 + LangGraph | Backend Team |
| `ai-architect-gpu` | ComfyUI + Diffusers + Blender headless | AI/GPU Team |

---

## Nguyen tac chung

1. **Doc 01-SRS truoc** - Hieu scope truoc khi code
2. **Khong lam ngoai scope** - Neu khong co trong SRS, khong lam
3. **Theo dung checkpoint** - Moi checkpoint co definition of done ro rang
4. **API-first** - Frontend va backend thoa thuan API contract truoc khi code
5. **Test truoc merge** - Khong merge PR khong co test
6. **Review bat buoc** - Moi PR can it nhat 1 approval

---

## Lien he

- System Architect: Chot moi quyet dinh ky thuat
- PM: Chot scope va priority
- Tech Lead Frontend: Chot UI/UX implementation
- Tech Lead Backend: Chot API va domain logic
- Tech Lead AI/GPU: Chot generation pipeline
