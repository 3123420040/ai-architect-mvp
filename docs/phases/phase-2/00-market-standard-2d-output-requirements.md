---
Feature: Phase 2 Market-Standard 2D Deliverable Requirements
Author:
Status: Draft
Last updated: 2026-04-12
---

# Phase 2 Market-Standard 2D Deliverable Requirements

## 1. Purpose

This document defines the detailed Phase 2 requirements required for the product to produce **market-credible 2D design deliverables** for residential architecture workflows.

It is intended as an **analysis handoff document** for downstream teams:
- product analysis,
- business analysis,
- architecture,
- data/geometry modeling,
- drawing/rendering,
- CAD/BIM interoperability,
- QA,
- and delivery operations.

This document is intentionally more detailed than the current execution checkpoint documents. It describes the **target requirement state** needed to meet market expectations, not just the current implementation scope.

## 2. Decision Framing

The product already has the ability to:
- collect a basic brief,
- generate option placeholders,
- persist a canonical geometry payload,
- export PDF/SVG/DXF/IFC artifacts,
- and move a version through review and handoff.

However, this is not yet sufficient to satisfy end users who expect:
- high-quality architectural 2D output,
- multiple usable output formats,
- multiple project and drawing types,
- disciplined technical documentation,
- and deep enough detail to support serious client review and professional trust.

The Phase 2 requirement is therefore not merely:

> "export more files"

It is:

> "produce professional, market-standard 2D deliverables from a reliable canonical design source, across multiple formats and project types, with consistent drawing quality and predictable handoff quality."

## 3. Target Deliverable Position

### 3.1 Selected market target

The required target for Phase 2 is:

> **A market-standard design-development-grade 2D package for residential projects**

This package must be stronger than a schematic client presentation set and must visibly move toward design-development quality, while still avoiding permit or construction-document claims unless separately qualified.

### 3.2 What the output must feel like

The output must feel like it came from a disciplined architecture or design-build team, not from:
- an AI concept board,
- a drafting placeholder,
- a graphic mockup,
- or a format conversion wrapper.

### 3.3 What success looks like

A paying residential client, architect, or design-build professional should be able to say:
- "This package looks serious."
- "The plans, elevations, sections, and schedules are coordinated."
- "The file exports are usable in real workflows."
- "This is detailed enough for design review and downstream collaboration."

## 4. Scope

## 4.1 In scope

Phase 2 requirements cover:
- input and brief quality sufficient for professional output,
- canonical design representation,
- typology-aware planning logic,
- sheet and annotation composition,
- drawing quality standards,
- package assembly,
- export formats and interoperability,
- versioning and issue management,
- and quality gates required before a package is issued.

## 4.2 Out of scope for this document

This document does not define:
- full jurisdiction-specific permit compliance,
- structural engineering design,
- MEP engineering design,
- stamped/sealed deliverables,
- consultant coordination workflows,
- or construction-detail completeness beyond the Phase 2 market target.

Those may become future requirements, but they are not assumed here.

## 5. Target Users and Stakeholders

### 5.1 Primary users

- Residential architects
- Design-build designers
- Boutique home design firms
- Remodel and renovation design teams
- Internal preconstruction design teams

### 5.2 Secondary users

- Paying homeowners and residential clients
- Project managers and coordinators
- Drafting teams
- Interior/facade collaborators
- External CAD/BIM operators consuming exported files

### 5.3 Internal stakeholders

- Product team
- Solution architecture team
- Backend/API team
- Geometry and planning engine team
- Drawing/rendering team
- Frontend delivery/review team
- QA and release team

## 6. Core Product Promise

Phase 2 must allow the product to make the following defensible claim:

> The product can generate a coordinated, review-ready, design-development-grade 2D package for residential projects, with professional sheets, disciplined annotations, and usable export handoff artifacts.

The product must not imply:
- permit-ready completeness,
- jurisdictional approval readiness,
- engineer-reviewed design,
- or construction documentation completeness,
unless separate validated workflows are added later.

## 7. Requirement Principles

All Phase 2 requirements must follow these principles:

### 7.1 Canonical-source principle

Every output sheet and export must derive from one coordinated canonical design source. Plans, elevations, sections, schedules, and interop exports must not be authored independently without shared geometry and metadata.

### 7.2 Market-credibility principle

If a feature creates more files but does not increase professional trust, it is lower priority than a feature that improves drawing credibility.

### 7.3 Usability principle

Formats such as PDF, SVG, DXF, and IFC must be evaluated not by existence alone, but by whether downstream users can meaningfully use them.

### 7.4 Typology principle

The system must support more than one hard-coded building pattern. Market-standard output requires controlled variation across project types and design intents.

### 7.5 Verified-vs-assumed principle

The package must distinguish between:
- user-provided verified data,
- inferred data,
- and default assumptions.

This is mandatory for professional trust.

## 8. End-to-End Capability Requirements

## 8.1 Input and requirement-capture capability

The system must collect enough information to support professional downstream output. A minimal lot-size and floor-count brief is not sufficient.

The system must capture, store, and expose:
- project type,
- site condition,
- program requirements,
- room counts and room priorities,
- adjacency intent,
- vertical circulation intent,
- parking/service requirements,
- facade style direction,
- material direction,
- opening preferences,
- target package type,
- expected formats,
- and acceptable assumption rules.

## 8.2 Canonical planning and geometry capability

The system must generate a geometry model that is:
- deterministic enough for repeatable sheets,
- rich enough for annotation and schedules,
- traceable back to the brief,
- and flexible enough for multiple typologies and option families.

## 8.3 Drawing-composition capability

The system must render coordinated plans, elevations, sections, details, and schedules with real drawing logic:
- visual hierarchy,
- annotation placement,
- dimension strategies,
- title block consistency,
- sheet composition,
- and cross-sheet references.

## 8.4 Package and delivery capability

The system must generate:
- issue-ready package metadata,
- version-aware exports,
- review-safe previews,
- and structured handoff bundles.

## 8.5 Interoperability capability

The system must export files that can be realistically consumed in downstream CAD/BIM workflows, not just satisfy a "file exists" check.

## 9. Detailed Functional Requirements

## 9.1 Brief and Design Intent Requirements

### REQ-BRIEF-001

The system must support a structured design-intent brief, not just freeform notes and basic dimensions.

### REQ-BRIEF-002

The structured brief must include, at minimum:
- project name,
- project type,
- renovation vs new-build flag,
- site width/depth/area,
- site orientation,
- verified survey availability,
- floor count target,
- target room program,
- room priority ranking,
- client lifestyle constraints,
- style/facade direction,
- material direction,
- budget band,
- and special requests.

### REQ-BRIEF-003

The brief model must support explicit room program requirements, including:
- room type,
- required count,
- target area range,
- preferred level,
- adjacency constraints,
- privacy constraints,
- daylight preference,
- and optionality.

### REQ-BRIEF-004

The system must support typology-specific brief fields for at least:
- townhouse / narrow-house,
- detached villa,
- apartment renovation,
- shophouse / mixed-use residential,
- and compact office/home-office hybrid.

### REQ-BRIEF-005

The system must persist the distinction between:
- user-confirmed inputs,
- system-inferred values,
- and defaults.

### REQ-BRIEF-006

The system must expose all unresolved assumptions before a package is issued.

### REQ-BRIEF-007

The system must support a "required clarifications" gate if the brief is insufficient for the requested output standard.

## 9.2 Typology and Planning Logic Requirements

### REQ-PLAN-001

The planning engine must support multiple project typologies rather than a single hard-coded room template.

### REQ-PLAN-002

The planning engine must support multiple option families per typology, not just cosmetic variations.

### REQ-PLAN-003

Each option must retain a machine-readable explanation of:
- program allocation,
- circulation strategy,
- zoning strategy,
- and major assumptions.

### REQ-PLAN-004

The planning engine must produce options that can vary by:
- stacking strategy,
- stair placement,
- front-core-rear zoning,
- service placement,
- facade openness,
- and terrace/yard relationship.

### REQ-PLAN-005

The planning engine must respect room count and key adjacency constraints when generating options.

### REQ-PLAN-006

The planning engine must support both deterministic rule-based layouts and model-assisted suggestions, provided the final canonical geometry is stable and analyzable.

## 9.3 Canonical Geometry Requirements

### REQ-GEO-001

The canonical geometry model must be the source of truth for:
- plans,
- elevations,
- sections,
- schedules,
- quantity summaries,
- and interop exports.

### REQ-GEO-002

The canonical geometry model must support, at minimum:
- site boundary,
- setbacks,
- landscape zones,
- access points,
- grids,
- levels,
- structural/wall elements,
- openings,
- rooms,
- stairs,
- key fixtures,
- roof,
- section/elevation markers,
- detail markers,
- and annotation anchors.

### REQ-GEO-003

Each room must support:
- stable ID,
- room type,
- room name,
- polygon,
- area,
- perimeter,
- level,
- clear height,
- finish metadata,
- associated openings,
- and schedule eligibility.

### REQ-GEO-004

Each wall must support:
- stable ID,
- level,
- start/end points or geometric body,
- wall type,
- assembly,
- thickness,
- structural flag,
- fire-rating metadata where applicable,
- and cross-level behavior if relevant.

### REQ-GEO-005

Each opening must support:
- stable ID,
- parent wall reference,
- opening type,
- subtype,
- size,
- sill/head data,
- face/orientation,
- frame metadata,
- glazing or panel metadata,
- hardware metadata,
- and schedule mark.

### REQ-GEO-006

The geometry model must support annotation anchors for:
- room tags,
- dimension strings,
- section/elevation callouts,
- detail callouts,
- and schedule references.

### REQ-GEO-007

The geometry model must support verified-vs-assumed site and dimension flags.

### REQ-GEO-008

The geometry model must support typology extensions without breaking existing export contracts.

## 9.4 Drawing Sheet Requirements

### REQ-SHEET-001

The system must support sheet-native vector composition for each drawing sheet.

### REQ-SHEET-002

Each issued package must include, at minimum:
- cover / issue sheet,
- site / plot sheet,
- floor plan sheet per required level,
- principal elevation sheets,
- section sheets,
- opening schedule sheet,
- and room/area schedule sheet.

### REQ-SHEET-003

The cover sheet must include:
- package title,
- project name,
- version/issue label,
- issue date,
- sheet index,
- package type,
- disclaimer,
- and a representative preview graphic.

### REQ-SHEET-004

The site sheet must not simply reuse a floor plan. It must specifically render:
- site boundary,
- building footprint,
- orientation,
- access and landscape zones,
- setbacks if known,
- and assumed-vs-verified status where relevant.

### REQ-SHEET-005

Each floor plan sheet must include:
- exterior wall hierarchy,
- interior partitions,
- door and window symbols,
- stair direction,
- fixed bath/kitchen fixtures,
- optional furniture or zoning blocks,
- room tags,
- area values,
- major dimensions,
- and section/elevation/detail references.

### REQ-SHEET-006

Elevation sheets must support all principal building faces required by the selected package standard.

### REQ-SHEET-007

Elevation sheets must include:
- grade line,
- level markers,
- opening positions,
- roof/parapet outline,
- major vertical dimensions,
- and conceptual facade/material labels.

### REQ-SHEET-008

Section sheets must include:
- cut hierarchy,
- floor-to-floor relationships,
- slab and roof relationships,
- vertical dimensions,
- stair relationship if relevant,
- and major level labels.

### REQ-SHEET-009

The sheet engine must support optional enlarged detail sheets or detail callout placeholders for future expansion, even if only some detail types are implemented in Phase 2.

### REQ-SHEET-010

The package must support per-sheet metadata including:
- sheet number,
- sheet title,
- sheet type,
- scale,
- orientation,
- source level where relevant,
- and file references.

## 9.5 Annotation and Dimensioning Requirements

### REQ-ANNO-001

The system must include a real dimensioning engine, not just overall width/depth labels.

### REQ-ANNO-002

The dimensioning engine must support, at minimum:
- overall plan dimensions,
- grid dimensions,
- key internal room dimensions,
- opening dimensions where needed,
- stair dimensions,
- and elevation/section vertical dimensions.

### REQ-ANNO-003

The system must support dimension style controls:
- text height,
- arrow/tick style,
- extension gap,
- offset rules,
- units,
- and decimal precision.

### REQ-ANNO-004

The system must prevent label collisions and dimension overlap with critical geometry wherever possible.

### REQ-ANNO-005

The system must support symbol families for:
- north arrow,
- section marker,
- elevation marker,
- detail marker,
- stair up/down,
- and schedule tags.

### REQ-ANNO-006

Room tags must support:
- room name,
- room number or ID,
- area,
- and optional finish key.

### REQ-ANNO-007

The system must allow configurable detail density by deliverable preset:
- client presentation,
- schematic,
- design development,
- and CAD handoff.

## 9.6 Graphic Standards Requirements

### REQ-GRAPHIC-001

The package must apply a controlled line-weight hierarchy across all sheets.

### REQ-GRAPHIC-002

The package must use a controlled typography system with consistent:
- font family,
- title sizing,
- body note sizing,
- room tag sizing,
- and dimension text sizing.

### REQ-GRAPHIC-003

The package must maintain consistent white space, margins, title block position, and drawing viewport framing across the full issue set.

### REQ-GRAPHIC-004

The system must support at least one disciplined title block family and one extensible branding profile.

### REQ-GRAPHIC-005

The package must avoid obvious low-quality signals such as:
- random font changes,
- cropped text,
- misaligned titles,
- floating tags,
- inconsistent border spacing,
- and plan sheets that look like screenshots.

### REQ-GRAPHIC-006

The system must support different visual presets for at least:
- neutral technical,
- client presentation,
- and branded studio mode,
while preserving the same canonical geometry.

## 9.7 Schedule Requirements

### REQ-SCHED-001

The system must generate schedule rows from canonical geometry, not from sheet text.

### REQ-SCHED-002

Opening schedules must support, at minimum:
- mark,
- level,
- room or zone,
- type,
- size,
- frame,
- panel or glazing data,
- hardware or operation,
- fire-rating or thermal data where relevant,
- and notes.

### REQ-SCHED-003

Room schedules must support, at minimum:
- room ID,
- room name,
- level,
- area,
- clear height,
- finish fields,
- and notes.

### REQ-SCHED-004

The system must support both sheet-rendered schedules and machine-readable schedule exports.

### REQ-SCHED-005

Schedule marks must remain consistent across:
- plan sheets,
- elevation sheets,
- section references where applicable,
- schedule sheets,
- DXF,
- and IFC-derived references.

## 9.8 Export and Packaging Requirements

### REQ-EXPORT-001

The system must issue a single combined PDF package for each issue.

### REQ-EXPORT-002

The system must issue one SVG per sheet as the vector master for web and redline use.

### REQ-EXPORT-003

The system should issue PNG previews per sheet and a package-level contact-sheet preview for gallery and review UX.

### REQ-EXPORT-004

The package must include a machine-readable manifest with:
- package ID,
- project ID,
- version ID,
- issue type,
- revision label,
- issue date,
- generation timestamp,
- sheet list,
- and file references.

### REQ-EXPORT-005

The package must support a single downloadable bundle that groups PDF, SVG sheets, schedules, and machine-readable metadata.

### REQ-EXPORT-006

The package must support explicit issue states such as:
- draft,
- review,
- issued,
- superseded,
- and delivered.

## 9.9 DXF Requirements

### REQ-DXF-001

DXF export must represent real drawing structure, not only minimal placeholder geometry.

### REQ-DXF-002

DXF export must support, at minimum:
- model space geometry,
- layer mapping,
- readable text,
- schedule tags,
- and sheet or layout references consistent with the issued package.

### REQ-DXF-003

DXF layer names, colors, and lineweights must follow a documented export contract.

### REQ-DXF-004

DXF export must be validated by opening in a standard CAD viewer/editor and checking:
- geometry presence,
- text legibility,
- layer structure,
- and no catastrophic import errors.

### REQ-DXF-005

If the system claims CAD handoff quality, paper-space or equivalent layout structure must be supported for key sheets.

## 9.10 IFC Requirements

### REQ-IFC-001

IFC export must progress beyond simple proxy placeholders if it is presented as a real BIM handoff artifact.

### REQ-IFC-002

The IFC contract must define:
- minimum entity coverage,
- spatial structure,
- levels/storeys,
- room/space mapping,
- wall/opening semantics,
- and property-set scope.

### REQ-IFC-003

IFC must be validated in at least one standard IFC viewer before being classified as production-ready.

### REQ-IFC-004

If IFC remains a foundation artifact in Phase 2, the UI and documentation must label it clearly as limited-scope interoperability output.

## 9.11 Versioning, Revision, and Audit Requirements

### REQ-VERSION-001

A package must only be issued from a locked source version.

### REQ-VERSION-002

Issued package metadata must be immutable after issue.

### REQ-VERSION-003

New revisions must produce new issue records rather than overwriting old exports.

### REQ-VERSION-004

Revision labels, issue dates, and change summaries must stay consistent across:
- title block,
- manifest,
- delivery UI,
- and handoff bundle metadata.

### REQ-VERSION-005

The system must retain package lineage from:
- source brief,
- source design version,
- issued package,
- revision chain,
- and handoff bundle.

## 9.12 Delivery and Review Requirements

### REQ-DELIVERY-001

The delivery UI must present the package as a coherent issue set, not just a list of files.

### REQ-DELIVERY-002

Users must be able to preview:
- cover sheet,
- plan sheets,
- elevations,
- sections,
- schedules,
- and model/render companions where applicable.

### REQ-DELIVERY-003

The system must expose which exports are:
- presentation assets,
- technical drawing assets,
- CAD handoff assets,
- and limited-scope interop assets.

### REQ-DELIVERY-004

The review flow must support annotation and issue gating before final package issue.

## 10. Non-Functional Requirements

## 10.1 Quality requirements

### NFR-QUALITY-001

No package may be considered market-standard if its sheets are internally inconsistent.

### NFR-QUALITY-002

No package may be considered market-standard if one or more claimed exports are placeholder-grade while being labeled as production-grade.

### NFR-QUALITY-003

Professional appearance must be treated as a verifiable quality gate, not as a subjective post-hoc preference.

## 10.2 Performance requirements

### NFR-PERF-001

The system must define target generation times for:
- option generation,
- sheet composition,
- PDF assembly,
- vector export,
- and CAD/BIM export.

### NFR-PERF-002

The system must support preview generation separately from final package issue when full export cost is high.

## 10.3 Reliability requirements

### NFR-REL-001

Export operations must be repeatable from the same locked canonical source.

### NFR-REL-002

If generation falls back to a degraded pipeline, the resulting package must be explicitly marked as degraded or blocked from issue, depending on policy.

## 10.4 Traceability requirements

### NFR-TRACE-001

Every issued package must be traceable to:
- source version,
- source geometry schema version,
- export pipeline version,
- and issue timestamp.

## 11. Package-Level Acceptance Criteria

A package passes the market-standard gate only if all criteria below are met.

### AC-PACK-001

The package contains all required sheet types for the selected deliverable preset.

### AC-PACK-002

All sheets are derived from the same locked canonical source version.

### AC-PACK-003

All sheets include consistent issue metadata and title block structure.

### AC-PACK-004

Dimensioning is present beyond overall site width/depth and is legible on the main drawing sheets.

### AC-PACK-005

Plans, elevations, sections, and schedules are cross-consistent for room names, level names, and schedule marks.

### AC-PACK-006

The package looks like a coordinated professional set and does not visibly resemble a screenshot wrapper or placeholder board.

### AC-PACK-007

The package includes a manifest that matches the actual issued files.

## 12. Sheet-Level Acceptance Criteria

### AC-SHEET-001 Cover sheet

Must include:
- package title,
- project name,
- revision label,
- issue date,
- sheet index,
- disclaimer,
- and preview graphic.

### AC-SHEET-002 Site sheet

Must include:
- site boundary,
- building footprint,
- north arrow,
- scale notation or scale bar,
- and clear site-specific information beyond a level plan redraw.

### AC-SHEET-003 Floor plan sheets

Must include:
- wall hierarchy,
- openings,
- stairs,
- fixed fixtures,
- room labels,
- room areas,
- and multiple meaningful dimension strings.

### AC-SHEET-004 Elevation sheets

Must include:
- building outline,
- level cues,
- opening positions,
- roof/parapet logic,
- and conceptual facade/material information.

### AC-SHEET-005 Section sheets

Must include:
- section cut hierarchy,
- vertical relationships,
- slab/roof logic,
- and major heights or levels.

### AC-SHEET-006 Schedule sheets

Must include:
- readable table structure,
- stable schedule marks,
- and values that match the canonical model.

## 13. Export Acceptance Criteria

### AC-EXPORT-001 PDF

The combined PDF must be printable, complete, and page-ordered correctly.

### AC-EXPORT-002 SVG

Per-sheet SVG files must be crisp, structured, and suitable for zoom and annotation workflows.

### AC-EXPORT-003 DXF

DXF must open successfully in a standard CAD tool and preserve core geometry, text, and layer structure.

### AC-EXPORT-004 IFC

IFC must open successfully in a standard IFC viewer and preserve the declared minimum spatial and element structure.

### AC-EXPORT-005 Machine-readable manifest

The manifest must reference all issued files accurately and expose enough metadata for downstream automation.

## 14. QA and Verification Requirements

## 14.1 Automated verification

The system must support automated checks for:
- schema validity,
- cross-sheet metadata consistency,
- schedule consistency,
- file existence,
- SVG validity,
- PDF creation,
- DXF openability,
- IFC openability,
- and export manifest completeness.

## 14.2 Visual regression

The system must include visual regression checks for representative package types and typologies, covering:
- site sheet,
- plan sheet,
- elevation sheet,
- section sheet,
- and schedule sheet.

## 14.3 Human review checklist

The system must include a manual review checklist for:
- graphic hierarchy,
- annotation overlap,
- typography consistency,
- title block correctness,
- dimension readability,
- and deliverable credibility.

## 14.4 Benchmark set

The team must maintain a benchmark library of representative projects and issued sample packages to evaluate whether quality is improving or regressing.

## 15. Explicit Non-Goals

The following are not required for Phase 2 unless a separate requirement package adds them:
- full permit documentation,
- structural engineering documents,
- MEP plans,
- reflected ceiling plans,
- framing plans,
- foundation plans,
- construction details for every condition,
- consultant coordination packages,
- stamped/sealed workflows,
- and full code-jurisdiction automation.

## 16. Dependencies for Downstream Analysis

The following workstreams must analyze and refine this requirements document before implementation is considered complete:

### Analysis Workstream A — Brief and requirements model

Must define:
- full field model,
- validation rules,
- assumption policy,
- and typology-specific brief extensions.

### Analysis Workstream B — Canonical geometry contract

Must define:
- versioned schema,
- extensibility model,
- stable IDs,
- and mapping rules from brief to geometry.

### Analysis Workstream C — Drawing engine and sheet system

Must define:
- renderer responsibilities,
- annotation engine,
- title block system,
- style presets,
- and sheet metadata contract.

### Analysis Workstream D — Interoperability

Must define:
- DXF contract,
- IFC contract,
- validation tools,
- and supported downstream use cases.

### Analysis Workstream E — QA and release gates

Must define:
- package pass/fail criteria,
- automated and manual checks,
- benchmark samples,
- and release blocking rules.

## 17. Open Questions for Follow-Up Analysis

1. Which deliverable presets must be officially supported in Phase 2 launch, and which should remain internal or beta?
2. Which residential typologies are launch-blocking versus roadmap-only?
3. What is the minimum acceptable DXF contract for external CAD users in the first production release?
4. What minimum IFC semantics are required before the product can describe IFC as usable handoff rather than foundation export?
5. Should detail sheets be mandatory for design-development output, or can detail callouts be issued first with future detail expansion?
6. Which parts of dimensioning must be deterministic rule-based versus user-adjustable?
7. What branding flexibility is required for studios without breaking drawing consistency?
8. Which issue states and approval gates are required before package issue in production?
9. What benchmark projects should be frozen as release-quality reference cases?
10. What degraded-mode policy should apply when generation or geometry confidence is below the market-standard threshold?

## 18. Recommended Next Deliverables

The downstream teams should convert this document into:
- a detailed business analysis brief,
- a canonical geometry schema specification,
- a drawing/rendering architecture document,
- a DXF/IFC interoperability contract,
- a QA acceptance matrix,
- and an execution plan aligned with Phase 2 checkpoints.

