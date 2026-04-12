# Phase 3 Scope Lock

*Status: Locked*
*Decision date: 2026-04-12*
*Authority: Sponsor direction captured in Codex implementation session*
*Supersedes: unresolved scope suggestions in `01-ba-analysis-brief.md` and default flag assumptions in `03-checkpoint-execution-plan.md` where they conflict*

---

## 1. Purpose

This document freezes the Phase 3 scope so architecture, product, engineering, and QA teams can execute without re-opening already-resolved decisions.

The goal of Phase 3 is to ship a market-standard design-development package for new projects, while hardening the remaining Phase 2 baseline gaps that are still required by the prerequisite checklist.

---

## 2. Executive Decision Summary

| Area | Locked decision |
|------|-----------------|
| Execution mode | Phase 3 is a hardening-first phase for the Phase 2 baseline |
| Typology support | Townhouse, villa, apartment renovation, shophouse, home-office |
| Launch presets | `technical_neutral`, `client_presentation` |
| DXF bar | Full contract: paper space, editable dimensions, hatch, 25+ layers |
| IFC bar | Follow the architecture contract as written |
| Detail sheets | Mandatory, but limited to DD key detail sheets only |
| Dimensioning | Rule-based in Phase 3 |
| Workflow | Package-centric `draft -> review -> issued` with mandatory KTS approval |
| Degraded policy | Preview export allowed with `DEGRADED`; package issue blocked until gates pass |
| Rollout | Phase 3 applies only to projects created after the Phase 3 flag opens |
| Studio identity | Use KTC KTS branding across issued packages |
| Validation tools | Team access to AutoCAD, DraftSight, and Solibri is confirmed |

---

## 3. Phase Objective

Phase 3 is not a greenfield redesign. It is the phase where the product must:

1. close prerequisite gaps left from the current Phase 2 baseline,
2. move from schematic-grade outputs to design-development-grade outputs,
3. make DXF and IFC credible downstream deliverables,
4. move issue control from version status to package status,
5. and introduce a premium, consistent client-facing package identity.

This means every Phase 3 checkpoint must be judged not only by new features but also by whether the prerequisite checklist is genuinely satisfied on the live implementation path.

---

## 4. Locked Scope

### 4.1 In-scope

- Brief v2 for all 5 typologies.
- Clarification gate that blocks generation when required fields are missing.
- Assumption review before issue.
- Canonical Layer 2 geometry for design-development outputs.
- Full package sheet set:
  - cover
  - site
  - floor plans
  - 4 elevations
  - 2 sections
  - schedules
  - mandatory DD key detail sheets
- Two launch presets: `technical_neutral`, `client_presentation`.
- Real DXF handoff meeting the full architecture contract.
- Real IFC foundation meeting the architecture contract.
- Package-centric issue workflow with immutable issued records.
- DEGRADED preview mode that can be exported and reviewed, but not issued.

### 4.2 Out-of-scope

- Full permit documentation.
- Full construction detail library.
- Structural, MEP, and consultant coordination packages.
- User-adjustable manual dimension editing.
- Automatic migration of all existing projects into Phase 3.
- `branded_studio` as a release preset.

---

## 5. Typology Policy

### 5.1 Supported typologies

The supported Phase 3 typology catalog is:

- `townhouse`
- `villa`
- `apartment_reno`
- `shophouse`
- `home_office`

### 5.2 Release quality tiers

Because the benchmark project pack is not yet frozen in this repository, release quality is split into two operational tiers:

- Tier 1 benchmark-critical: `townhouse`, `villa`
- Tier 2 supported with manual QA until benchmark pack matures: `apartment_reno`, `shophouse`, `home_office`

This does not remove Tier 2 from scope. It only changes validation sequencing.

---

## 6. Deliverable Preset Policy

### 6.1 Launch presets

Only the following presets are launch presets for Phase 3:

- `technical_neutral`
- `client_presentation`

### 6.2 Preset intent

- `technical_neutral` is the primary issue-safe preset for technical review and downstream CAD/BIM handoff.
- `client_presentation` is the premium client-facing preset with the same geometry truth, but lighter annotation density and approved accent styling.

### 6.3 Non-launch preset

- `branded_studio` is not a release preset in Phase 3.

Brand identity for KTC KTS still applies to issued sheets in both launch presets through the title block, wordmark, and disclaimer standard.

---

## 7. Detail Sheet Decision

Detail sheets are mandatory in Phase 3, but they are intentionally limited to DD-level key details.

The minimum issue-safe requirement is:

- at least 2 key detail sheets, or
- 1 combined key-detail sheet containing at least 4 clearly readable DD detail views.

Accepted detail families:

- typical wall / facade build-up
- wet-area threshold / floor transition
- stair section / guard interface
- roof edge / parapet condition
- window sill / jamb / head pattern

Not required in Phase 3:

- full permit-ready construction detail library
- jurisdiction-specific compliance details
- fabrication-ready shop detail depth

---

## 8. Interoperability Bar

### 8.1 DXF

DXF is locked to the full architecture contract. Phase 3 DXF is considered complete only if it includes:

- model space at 1:1,
- paper space layouts,
- editable dimension entities,
- wall hatching / poché,
- 25+ named layers,
- and validation in AutoCAD, LibreCAD, and DraftSight.

### 8.2 IFC

IFC is locked to the architecture contract. Phase 3 IFC is considered complete only if it includes:

- IFC4x3,
- correct spatial structure,
- typed core entities,
- required property sets and quantities,
- and validation in Solibri, BIMVision, and IfcOpenShell.

This is a real interoperability export, not a placeholder file.

---

## 9. Workflow and Status Model

### 9.1 Canonical flow

Phase 3 must replace the current issue flow with a package-centric workflow:

`draft -> review -> issued`

### 9.2 Rules

- `draft`: package can be generated, previewed, and iterated.
- `review`: package is under architect review and assumption confirmation.
- `issued`: immutable released package with synchronized title block, manifest, and delivery record.

### 9.3 Approval gate

- KTS approval is mandatory before `issued`.
- A package with unresolved critical QA failures cannot advance to `issued`.
- Version state can still exist for generation/revision tracking, but package issue is the authoritative delivery milestone.

---

## 10. DEGRADED Preview Policy

DEGRADED is allowed only as a preview state.

Allowed:

- preview export for review,
- QA inspection,
- stakeholder discussion inside the team,
- debugging incomplete outputs.

Not allowed:

- client issue,
- marking package as issued,
- replacing the current issued package,
- using degraded output as official handoff.

Mandatory DEGRADED language:

`DEGRADED PREVIEW. QUALITY GATES NOT PASSED. PREVIEW ONLY. ISSUE BLOCKED.`

---

## 11. Rollout Policy

Phase 3 applies only to projects created after the Phase 3 feature flag is enabled.

Implications:

- No mandatory migration of the existing project base in this phase.
- Existing projects may remain on the current path unless explicitly recreated or upgraded later.
- QA, analytics, and support must be able to distinguish Phase 2 and Phase 3 projects by creation path and feature flags.

---

## 12. Quality and Validation Policy

### 12.1 Hard requirements before issue

- prerequisite checklist satisfied on the active code path
- no unresolved P0 package bugs
- package consistency checks pass
- assumption review completed
- KTS approval recorded
- DXF validation passed
- IFC validation passed
- issue-safe branding and disclaimer applied

### 12.2 Tooling baseline

The team has access to:

- AutoCAD
- DraftSight
- Solibri

LibreCAD, BIMVision, and IfcOpenShell should still remain in the automated/manual validation stack for compatibility and CI coverage.

---

## 13. Operational Follow-ups

The following items are still required operationally, but they no longer block scope definition:

- freeze benchmark project IDs and source files
- attach real reference packages for each launch preset
- nominate the first Tier 2 typology benchmark order
- define who records KTS approvals in production operations

These are execution inputs, not open scope questions.
