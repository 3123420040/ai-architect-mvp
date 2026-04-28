# Program B Implementation Detailed

## 1. Product Contract

Program B Release 1 introduces six implementation contracts:

1. semantic coordination model generation from approved architectural truth
2. schedule and quantity snapshot generation with verification markers
3. coordination issue registry
4. coordination-grade IFC export
5. handoff bundle, manifest, and readiness summary
6. delivery workspace visibility and release control

## 2. Entry Gate Contract

Program B may start only when:

- brief state is locked
- design version is approved and stable
- DD package baseline exists
- typology is launch-supported
- canonical geometry contains minimum architectural fields

Program B must block when:

- project is still clarifying
- version is draft or unresolved
- typology is roadmap-only
- geometry is insufficient for stable semantic mapping

## 3. Semantic Model Contract

The semantic coordination model is the core handoff object.

It must normalize:

- levels
- rooms
- walls
- slabs
- roofs
- openings
- doors and windows
- stairs
- core architectural relationships

It must also assign:

- stable semantic ids
- source geometry refs
- verification state
- source version lineage

Determinism rule:

Given the same approved version and same model schema version, semantic ids and exported structure must remain stable enough for schedules and issue links to survive reruns.

## 4. Quantity Contract

Schedule generation must be based on the semantic coordination model, not on presentation assets or prompt text.

Required launch outputs:

- room schedule
- door/window schedule
- area schedule

Optional launch-plus outputs:

- selected finish summary
- selected wall summary

Every schedule row must include:

- source bundle reference
- confidence or verification state
- source element linkage where available

## 5. Issue Contract

Coordination issues must be first-class data.

An issue must carry:

- issue identity
- severity
- status
- linked source version
- linked bundle
- linked room or element references
- source discipline
- owner
- resolution note

Issues must not exist only as loose comments inside notes or manifests.

## 6. IFC Contract

Program B Release 1 targets:

**architectural coordination IFC**

The export must:

- preserve key architectural objects
- preserve room and opening continuity
- attach selected properties
- and persist validation metadata

The export must not claim:

- authoring-grade round-trip safety
- full discipline completeness

## 7. Handoff Bundle Contract

Every successful bundle must register:

- semantic model artifact
- IFC artifact
- schedule artifacts
- issue register artifact
- manifest
- readiness summary

Each artifact must be tied to:

- project id
- version id
- bundle id
- schema or exporter version
- generation timestamp

Final artifacts must live in object storage.

## 8. Readiness Summary Contract

`readiness_summary.json` must act as the human-readable interpretation layer for Program B.

It must state:

- release intent
- launch typology support status
- verified vs review-required data
- open issue counts
- bundle release status
- explicit limitation notes

This artifact is mandatory because homeowner and manager value depends more on readable readiness than on raw IFC access.

## 9. Delivery Workspace Contract

The delivery workspace must behave as a coordination handoff surface, not as a raw asset list.

It must support:

- readiness summary card
- schedule preview
- issue summary and status
- bundle state label
- artifact download actions
- release controls for authorized users

## 10. Release Contract

No Program B bundle becomes officially released until:

- semantic model is built successfully
- schedule set is complete
- IFC export is generated
- QA passes or warning policy is explicitly accepted
- architect review is recorded

## 11. Implementation Slices

### Slice 1 - Persistence and API backbone

Includes:

- tables
- ORM
- API schemas
- bundle and job resources

### Slice 2 - Semantic model builder

Includes:

- architectural semantics normalization
- semantic ids
- relationship graph

### Slice 3 - Quantity and issue services

Includes:

- schedule extraction
- issue persistence
- review metadata

### Slice 4 - IFC export lane

Includes:

- model-to-IFC mapping
- property sets
- export validation

### Slice 5 - Bundle and readiness packaging

Includes:

- manifest
- readiness summary
- asset registry

### Slice 6 - Delivery workspace and release controls

Includes:

- UI updates
- status labels
- schedule preview
- issue summary

### Slice 7 - Downstream pilot validation and launch gate

Includes:

- benchmark fixture packs
- sample townhouse and villa packages
- downstream review evidence
- launch close-out

## 12. Lane Ownership

### Lane A - Backend persistence and APIs

Owns:

- migrations
- models
- schemas
- API endpoints

### Lane B - Semantic model and orchestration

Owns:

- model generation
- schedule extraction orchestration
- job tracking

### Lane C - Export and bundle packaging

Owns:

- IFC export
- manifest
- readiness summary
- storage registration

### Lane D - Frontend and delivery UX

Owns:

- delivery workspace
- issue and schedule presentation
- release controls

## 13. Explicit Out-of-Scope Engineering Work

Do not spend implementation time on:

- Revit connector work
- MCP tool connector work
- authoring seed file push workflows
- multi-discipline coordination
- code compliance automation
- permit sheet automation
