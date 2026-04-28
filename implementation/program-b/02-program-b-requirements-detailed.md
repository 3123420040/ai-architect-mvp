# Program B Detailed Requirements

## 1. Purpose

This document defines the detailed product requirements for Program B Release 1.

Program B Release 1 is the first execution-worthy scope of Program B after critique and narrowing.

Its purpose is to provide a **coordination-ready architectural handoff lane** on top of the existing package-centric system.

## 2. Product Truth

The current product was originally optimized for:

- concept generation,
- architectural review,
- export and package handoff,
- and presentation-grade communication.

Program B Release 1 must not pretend the product is already a full BIM authoring system.

So the requirement set is built around one principle:

**improve professional continuation quality without claiming native BIM authoring maturity.**

## 3. Primary Users

### 3.1 Primary operational users

1. Project architect or design lead
2. Internal documentation or BIM continuation staff
3. Downstream consultant-facing coordinator

### 3.2 Secondary visibility users

1. Homeowner or client reviewer
2. Design firm manager tracking release readiness

### 3.3 User-value truth

For Program B, "end-user satisfaction" means different things by role:

- professional users want lower ambiguity and less re-modeling effort
- homeowner users want confidence, traceability, and fewer late surprises

Program B Release 1 should optimize for the first while exposing digestible value to the second.

## 4. Scope Contract

### 4.1 In scope

- architectural semantic coordination model
- coordination-grade IFC export
- schedule snapshots
- coordination issue registry
- handoff manifest and readiness summary
- delivery workspace visibility for readiness, schedules, issues, and release state

### 4.2 Out of scope

- native BIM editing
- full construction authoring
- multi-discipline BIM
- clash automation across structure and MEP
- permit set generation
- connector-dependent workflows as launch prerequisites

## 5. Launch Typology Contract

Launch-supported typologies:

- `townhouse`
- `villa`

Non-launch typologies:

- `apartment_reno`
- `shophouse`
- `home_office`

If a requirement needs broader typology support, it must be explicitly marked roadmap-only.

## 6. Core User Journeys

## 6.1 Architect releases a coordination package

1. Architect opens an approved version with issued DD baseline.
2. Architect starts Program B handoff generation.
3. System builds semantic coordination model.
4. System generates schedules and coordination IFC.
5. Architect reviews readiness summary, schedules, and issue state.
6. Architect releases the consultant handoff bundle.

Success condition:

- architect can explain what is ready, what still needs verification, and what downstream teams can continue from.

## 6.2 Documentation team continues from handoff

1. Team opens the released coordination bundle.
2. Team downloads IFC, DXF, schedules, and issue register.
3. Team can identify rooms, openings, and key elements with stable references.
4. Team continues authoring with materially less ambiguity than starting from only concept package output.

Success condition:

- downstream continuation does not require blind re-interpretation of the approved design intent.

## 6.3 Homeowner checks execution readiness

1. Homeowner opens delivery workspace.
2. Homeowner sees readiness summary, package state, and major open coordination issues.
3. Homeowner understands whether the design is still conceptual, internally coordinated, or released for external continuation.

Success condition:

- homeowner gains confidence without needing to inspect BIM files directly.

## 7. Functional Requirements

## FR-B1: Eligibility and Trigger

| ID | Requirement | Priority |
|---|---|---|
| FR-B1.1 | Program B generation may start only from a locked brief + approved canonical version + issued DD package | P0 |
| FR-B1.2 | System must block draft, unstable, or review-pending versions | P0 |
| FR-B1.3 | System must block unsupported typologies from release flow | P0 |
| FR-B1.4 | System must show why a version is not eligible | P0 |
| FR-B1.5 | System must record who triggered the bundle generation | P1 |

## FR-B2: Semantic Coordination Model

| ID | Requirement | Priority |
|---|---|---|
| FR-B2.1 | System must generate a first-class semantic coordination model from approved architectural truth | P0 |
| FR-B2.2 | Semantic model must assign stable element identifiers for launch-supported typologies | P0 |
| FR-B2.3 | Semantic model must support at least: level, room, wall, slab, roof, opening, door, window, stair | P0 |
| FR-B2.4 | Semantic relationships must be queryable for export, schedules, and issues | P0 |
| FR-B2.5 | Semantic model must preserve lineage back to source version and package | P0 |
| FR-B2.6 | Unsupported or low-confidence semantics must be marked rather than silently assumed | P0 |

## FR-B3: Quantity and Schedule Snapshots

| ID | Requirement | Priority |
|---|---|---|
| FR-B3.1 | System must generate room schedule snapshot | P0 |
| FR-B3.2 | System must generate door/window schedule snapshot | P0 |
| FR-B3.3 | System must generate area schedule snapshot | P0 |
| FR-B3.4 | System may generate selected wall length/area and finish summaries where semantic confidence is sufficient | P1 |
| FR-B3.5 | Every schedule row must carry verification or confidence metadata | P0 |
| FR-B3.6 | Schedule snapshots must remain tied to source version and released bundle id | P0 |

## FR-B4: Coordination Issue Registry

| ID | Requirement | Priority |
|---|---|---|
| FR-B4.1 | System must store coordination issues as first-class records | P0 |
| FR-B4.2 | Issue must be linkable to project, version, bundle, room, and element ids | P0 |
| FR-B4.3 | Issue must support severity, status, owner, source discipline, and resolution note | P0 |
| FR-B4.4 | Delivery workspace must show issue summary before release | P0 |
| FR-B4.5 | Released bundle must include issue register artifact | P0 |
| FR-B4.6 | System must support resolve and waive states with audit trail | P1 |

## FR-B5: Coordination IFC Export

| ID | Requirement | Priority |
|---|---|---|
| FR-B5.1 | System must generate `architectural_coordination.ifc` from the semantic coordination model | P0 |
| FR-B5.2 | IFC export must preserve room, wall, slab, roof, opening, door, window, and stair continuity where available | P0 |
| FR-B5.3 | IFC export must include selected classifications and property sets required for launch workflows | P0 |
| FR-B5.4 | IFC export must not be marketed as authoring-grade round-trip by default | P0 |
| FR-B5.5 | Export validation metadata must be persisted with the bundle | P1 |

## FR-B6: Handoff Manifest and Bundle

| ID | Requirement | Priority |
|---|---|---|
| FR-B6.1 | System must package the released handoff artifacts into a single bundle identity | P0 |
| FR-B6.2 | Bundle must include manifest with release intent, verification state, and disclaimers | P0 |
| FR-B6.3 | Bundle must include readiness summary for non-BIM stakeholders | P0 |
| FR-B6.4 | Bundle must expose stable signed URLs for released assets | P0 |
| FR-B6.5 | Preview bundles must remain clearly labeled and blocked from release if QA fails | P0 |

## FR-B7: Delivery Workspace Visibility

| ID | Requirement | Priority |
|---|---|---|
| FR-B7.1 | Delivery workspace must show Program B status separately from raw file links | P0 |
| FR-B7.2 | Delivery workspace must show readiness summary panel | P0 |
| FR-B7.3 | Delivery workspace must show schedule preview tab | P0 |
| FR-B7.4 | Delivery workspace must show issue summary and issue detail access | P0 |
| FR-B7.5 | Delivery workspace must show release status using plain-language labels | P0 |
| FR-B7.6 | Homeowner-visible copy must explain coordination state without using opaque BIM jargon as the primary message | P1 |

## FR-B8: Review and Release Control

| ID | Requirement | Priority |
|---|---|---|
| FR-B8.1 | Bundle may not be released until QA passes or is explicitly accepted with warning policy | P0 |
| FR-B8.2 | Bundle may not be released until architect review is completed | P0 |
| FR-B8.3 | Release action must record actor, timestamp, and version identity | P0 |
| FR-B8.4 | Release action must freeze the released artifact set referenced by the manifest | P0 |
| FR-B8.5 | System must block language that implies construction-authoring certainty beyond verified scope | P0 |

## 8. Non-Functional Requirements

| ID | Requirement | Target |
|---|---|---|
| NFR-B1 | Bundle generation time for benchmark townhouse/villa projects | < 120s target |
| NFR-B2 | Schedule extraction time | < 20s target |
| NFR-B3 | IFC export time | < 60s target |
| NFR-B4 | Delivery workspace bundle detail load | < 1s p95 excluding file download |
| NFR-B5 | Release artifact storage | object storage only, no local-volume-only release |
| NFR-B6 | Semantic id stability across reruns on same source version | deterministic for launch-supported typologies |
| NFR-B7 | Auditability | every schedule, issue, and bundle row traceable to version and actor |

## 9. Launch Acceptance Gates

Program B Release 1 is launch-ready only if:

1. `townhouse` and `villa` benchmark packs pass bundle generation,
2. semantic element ids are stable enough for schedule and issue linkage,
3. coordination IFC export is accepted as continuation-helpful in downstream pilot review,
4. readiness summary correctly expresses verified vs review-required data,
5. delivery workspace exposes value without requiring users to inspect raw BIM files.

## 10. Explicit Non-Goals

Program B Release 1 must not promise:

- full construction documentation,
- one-click consultant-ready all-discipline models,
- editable BIM authoring inside the browser,
- or universal downstream compatibility without manual review.
