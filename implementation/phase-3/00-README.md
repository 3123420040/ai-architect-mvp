# Phase 3: Market-Standard Design Development Package

*Source: docs/phases/phase-2/00-market-standard-2d-output-requirements.md*
*Split date: Apr 12, 2026*

---

## Context

Day la bo tai lieu Phase 3 (Bac 3 cua deliverable roadmap). No nang cap output tu "schematic design package" (Phase 2 / Bac 2) len "design-development-grade package" dat chuan thi truong.

### Deliverable evolution

| Bac | Phase | Geometry | Output |
|-----|-------|----------|--------|
| 1 | Phase 1 MVP (CP5) | Layer 1 (basic metadata) | Professional PDF, title blocks |
| 2 | Phase 1 MVP+ (CP7) | Layer 1.5 (walls, openings, rooms) | Schematic package: 2 elevations, 1 section, vector SVG |
| **3** | **Phase 3 (day)** | **Layer 2 (full assemblies)** | **Design development: 4 elevations, schedules, DXF, IFC** |

---

## Thu tu doc

| # | File | Ai doc | Noi dung |
|---|------|--------|----------|
| 01 | `01-ba-analysis-brief.md` | **PM, BA, Product** | Phan tich business: user, scope, non-goals, open questions, deliverable positioning |
| 02 | `02-architecture-data-contract.md` | **Tech Lead, Backend, AI** | Data contract: geometry schema, sheet system, DXF/IFC contract, annotation engine, export pipeline |
| 03 | `03-checkpoint-execution-plan.md` | **PM, Tech Lead, All Teams** | Checkpoint breakdown: tasks by team, acceptance criteria, QA gates, verification strategy |
| 04 | `04-phase-3-scope-lock.md` | **Sponsor, PM, Tech Lead, Product** | Locked decisions for scope, workflow, interop quality bar, rollout, and degraded policy |
| 05 | `05-phase-3-branding-and-issue-standard.md` | **Design, FE, BE, QA** | KTC KTS branding, title block wording, disclaimers, issue presentation rules, DEGRADED treatment |

---

## Prerequisite

Phase 3 CHI bat dau khi:
- CP7 (Full Schematic Package) da hoan tat
- Layer 1.5 geometry da on dinh
- Sheet composition engine da hoat dong
- 2 principal elevations + 1 section da ship

## Decision Authority

Neu co xung dot giua de xuat mo trong `01/02/03` va quyet dinh da khoa:
- `04-phase-3-scope-lock.md` la single source of truth cho scope, workflow, degraded preview policy, typology support, va rollout rules.
- `05-phase-3-branding-and-issue-standard.md` la single source of truth cho KTC KTS wordmark, preset treatment, title block, va disclaimer wording.
