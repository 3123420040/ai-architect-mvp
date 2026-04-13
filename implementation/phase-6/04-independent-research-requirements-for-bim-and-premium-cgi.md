---
Feature: Independent Research Requirements for BIM / Construction Authoring and Premium CGI
Author:
Status: Draft
Last updated: 2026-04-13
---

# 1. Purpose

This document defines a separate research and planning brief for an independent technical team.

Its purpose is to let that team study, evaluate, and propose the right development direction for:

- **Program B: BIM and construction authoring**
- **Program C: Premium CGI**

This document is intentionally separate from the current Phase 6 execution scope.

## 1.1 Locked boundary

Phase 6 is now explicitly locked to:

**Program A: Presentation-grade 3D**

Program A target output is:

- `scene.glb`
- curated still renders
- `walkthrough.mp4`
- `presentation_manifest.json`
- architect approval gate

Program B and Program C are **not** to be folded into the current Phase 6 implementation.

Instead, they must be studied as separate programs with their own architecture, tooling, authoring model, team workflow, and delivery plan.

# 2. Decision This Research Must Support

At the end of this research, the product owner and architecture owner must be able to answer:

1. Whether Program B should become:
- a native BIM authoring lane,
- an IFC-first interoperability lane,
- or a hybrid authoring + exchange architecture

2. Whether Program C should become:
- an internal automated visualization lane,
- a DCC handoff lane for human viz artists,
- or a hybrid automation + artist polish workflow

3. Which parts of Program B and C should be built in-house versus integrated through commercial tools

4. What the realistic phased roadmap is for:
- semantic model core
- IFC/native authoring
- quantities and schedules
- issue management
- detailing and issued sheets
- BLEND/USD/FBX scene handoff
- premium material pipeline
- cinematic rendering and post-production

5. What the minimum viable architecture is for each program without overcommitting the current product

# 3. Current System Context

The independent team must start from the real current system context, not from a greenfield assumption.

## 3.1 What the current system already is

The current product is an AI-assisted architecture workflow centered around:

- client intake and brief clarification
- canonical design state
- 2D option generation
- review and approval flow
- package-centric export
- and a Phase 6 target for presentation-grade 3D

The current production stack is a Docker-based app with:

- Next.js web app
- FastAPI API
- background worker
- PostgreSQL
- Redis
- internal GPU boundary service

Reference:

- [implementation/03-architecture-blueprint.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/03-architecture-blueprint.md:100)
- [implementation/01-SRS-final.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/01-SRS-final.md:147)
- [implementation/06-api-contracts.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/06-api-contracts.md:398)
- [implementation/phase-6/03-3d-presentation-architecture-and-hosting.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/03-3d-presentation-architecture-and-hosting.md:22)

## 3.2 What the system already outputs

Today the system already has a package/export lane for:

- PDF
- SVG
- DXF
- IFC
- CSV schedules
- delivery manifest

But these outputs must not be over-interpreted.

The current export lane proves:

- package structure
- interoperability intent
- export attachment to canonical version

It does **not** yet prove:

- full BIM authoring semantics
- construction-grade detailing
- native authoring workflows
- or studio-grade CGI scene production

Important code evidence:

- current DXF export can fall back to a minimal payload if dependencies are absent at [app/services/exporter.py](/Users/nguyenquocthong/project/ai-architect-api/app/services/exporter.py:1062)
- current IFC export still uses simplified entities and proxy-based elements for walls and openings at [app/services/exporter.py](/Users/nguyenquocthong/project/ai-architect-api/app/services/exporter.py:1198)
- the current delivery UI already exposes PDF, SVG, DXF, IFC, schedules, and viewer links in one workspace at [src/components/delivery-client.tsx](/Users/nguyenquocthong/project/ai-architect-web/src/components/delivery-client.tsx:79)

## 3.3 What Program A is trying to solve

Program A is designed to solve:

- design-faithful client presentation
- reviewable 3D communication
- approval-gated delivery of GLB, renders, and MP4

Program A is **not** intended to solve:

- full BIM semantic modeling for all disciplines
- construction authoring
- marketing CGI at studio level

This has already been locked in:

- [implementation/phase-6/01-3d-output-research-and-direction.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/01-3d-output-research-and-direction.md:437)
- [implementation/phase-6/03-3d-presentation-architecture-and-hosting.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/03-3d-presentation-architecture-and-hosting.md:121)

## 3.4 Tooling context already known

The current broader project context indicates access to:

- AutoCAD
- DraftSight
- Solibri

This matters because:

- AutoCAD / DraftSight are relevant to CAD and DWG/DXF consumption
- Solibri is relevant to BIM review and validation
- none of these alone should be assumed to replace a full BIM authoring strategy or a premium DCC pipeline

# 4. Scope of the Independent Research Team

The independent team must research and propose a path for two separate but related programs.

## 4.1 Program B — BIM and construction authoring

Program B scope includes:

- semantic model core
- IFC strategy
- native authoring strategy
- quantities and schedules
- issue management
- detailing workflows
- issued sheets
- construction and coordination handoff logic

Program B explicitly concerns:

- architectural element semantics
- model structure
- revision and authoring ownership
- interoperability and editability
- how a professional architect or BIM team would continue the work

## 4.2 Program C — Premium CGI

Program C scope includes:

- BLEND/USD/FBX scene handoff
- premium asset pipeline
- premium material pipeline
- camera and sequence planning
- lighting and environment strategy
- cinematic render and post-production workflow
- hybrid automation + artist polish options

Program C explicitly concerns:

- DCC scene quality
- visual storytelling
- handoff to visualization specialists
- the line between automation and manual polish

# 5. Core Research Questions

The team must answer the following in detail.

## 5.1 Program B questions

### A. Semantic model core

- What internal semantic model is required if the system is expected to evolve from canonical 2D geometry into BIM-grade authoring?
- What entities, relationships, classifications, and property sets are mandatory?
- What level of semantic richness is needed for:
  - concept BIM
  - coordination BIM
  - construction authoring

### B. IFC and exchange strategy

- Should the system target IFC-first, native-first, or hybrid exchange?
- What IFC export level is realistic:
  - interoperability-only
  - coordination-ready
  - authoring-grade
- Which IFC entities and property sets must be supported for architectural workflows?
- What are the hard limits of relying on IFC without a native authoring model?

### C. Native authoring strategy

- If the goal is direct editable authoring by architects, what native file strategy is realistic?
- Which authoring systems are the likely target environments?
- Should the system:
  - generate exchange models only,
  - generate editable authoring seed files,
  - or integrate with a dedicated authoring platform?

### D. Quantities and schedules

- What quantities and schedules are required to be genuinely useful in practice?
- Which quantities can be trusted from automated generation, and which require manual verification?
- How should schedules remain traceable to the canonical source and revisions?

### E. Issue management and review

- What issue model is required for BIM and coordination workflows?
- How should issue IDs, viewpoints, responsibilities, and statuses be tracked?
- What role should Solibri-style checking play in the target architecture?

### F. Detailing and issued sheets

- What detail level must exist before claiming a construction-authoring lane?
- Which sheet types and detail families are mandatory?
- What should remain manual or architect-authored versus automated?

## 5.2 Program C questions

### A. Scene handoff format

- Should the premium CGI lane center around:
  - `BLEND`
  - `USD`
  - `FBX`
  - or a layered combination?
- Which format should act as the canonical DCC handoff package?
- What metadata must travel with scene files?

### B. Premium asset pipeline

- Where should premium assets come from:
  - internal library
  - licensed libraries
  - manufacturer assets
  - artist-authored kitbash assets
- How should asset provenance, licensing, and quality be controlled?

### C. Premium material pipeline

- What material model is required for premium CGI:
  - representative design materials
  - physically based material sets
  - manufacturer-accurate materials
- How should material decisions trace back to approved design direction?

### D. Automation vs artist workflow

- What part of the premium CGI pipeline can be automated safely?
- What part should be left to visualization artists?
- What are the best hybrid operating models?

### E. Cinematic rendering and post

- What is required to move from presentation-grade MP4 into studio-grade output?
- What lighting, animation, environment, compositing, grading, and post steps are mandatory?
- What is the difference between:
  - automated walkthrough
  - premium real-time presentation
  - polished studio marketing film

# 6. Mandatory Output From the Independent Team

The team must not return a vague suggestion deck.

They must return a decision-grade package with the following outputs.

## 6.1 Required file set

The team should produce at least these files:

1. `program-b-bim-and-construction-research-report.md`
2. `program-b-bim-and-construction-architecture-options.md`
3. `program-b-bim-and-construction-phased-plan.md`
4. `program-c-premium-cgi-research-report.md`
5. `program-c-premium-cgi-architecture-options.md`
6. `program-c-premium-cgi-phased-plan.md`
7. `cross-program-decision-matrix.md`

## 6.2 What each file must contain

### Research reports

Must include:

- market-standard workflows
- toolchain and authoring reality
- build-vs-buy analysis
- constraints and risks
- evidence-backed conclusions

### Architecture options

Must include:

- at least 3 viable architecture options per program
- required modules and boundaries
- host/runtime implications
- file format strategy
- storage strategy
- review/approval strategy
- operational implications

### Phased plans

Must include:

- milestone sequence
- implementation slices
- dependencies
- required specialist roles
- expected timeline assumptions
- explicit out-of-scope items per phase

### Cross-program decision matrix

Must compare:

- Program A only
- Program A + Program B
- Program A + Program C
- Program A + Program B + Program C

On these dimensions:

- user value
- revenue potential
- implementation cost
- operational complexity
- reliability risk
- team skill requirements
- vendor lock-in risk

# 7. Required Evaluation Lens

The independent team must evaluate all recommendations through these lenses.

## 7.1 Commercial realism

- Is the proposed path realistic for a product team of this size?
- Does it create a support burden that the current organization cannot sustain?

## 7.2 Professional credibility

- Would architects, BIM coordinators, and visualization teams consider the output credible?
- Which outputs are presentation-grade, coordination-grade, authoring-grade, or marketing-grade?

## 7.3 Editability

- Which outputs are truly editable?
- In which tools?
- By which roles?
- With what degree of loss or round-tripping risk?

## 7.4 Data integrity

- Can the proposed path preserve traceability from approved design truth to downstream outputs?
- Where does semantic drift happen?

## 7.5 Operating model fit

- Does the recommended architecture fit a software product team?
- Or does it require a service-delivery or studio-production operating model?

# 8. System Information the Team Must Respect

The independent team must not ignore the current architecture constraints.

## 8.1 Known source-of-truth principle

This product is moving toward a package-centric architecture where downstream outputs must trace back to:

- locked brief
- approved canonical design state
- issued package metadata

The team must not propose a solution that bypasses this source-of-truth chain.

## 8.2 Known boundary between review and authoring

Review tools and authoring tools are not the same.

Example:

- Solibri is useful in BIM review and checking, not as the authoring core
- GLB is useful for presentation and review, not as a serious authoring format

## 8.3 Known boundary between concept presentation and construction truth

The team must explicitly separate:

- concept presentation outputs
- BIM/co-ordination outputs
- construction authoring outputs
- premium marketing CGI outputs

They must not blur these categories in their recommendation.

# 9. Non-Goals

The independent team should not spend time proposing:

- a fully autonomous architect replacement
- instant one-click construction documents from vague client prompts
- a marketing promise that hides the need for authoring and review labor
- a monolithic system that forces one file format to solve all downstream use cases

# 10. Research Constraints

The team must assume:

- Program A is already chosen as the current next implementation target
- Program B and C are exploratory, not yet approved for build
- recommendations must be independent enough that another team could own them
- the final recommendation must identify what should remain:
  - software platform capability
  - architect workflow
  - BIM specialist workflow
  - viz artist workflow

# 11. Required Quality Bar

The team’s output must be:

- concrete
- technically credible
- operationally realistic
- explicit about trade-offs
- explicit about human roles
- explicit about editability and file ownership
- explicit about which deliverables are truly feasible in production

The output must not be:

- generic
- tool-name-only
- architecture-diagram theater
- or blind optimism about BIM/CGI automation

# 12. Recommended Starting Context to Read

At minimum, the independent team should read:

- [implementation/01-SRS-final.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/01-SRS-final.md)
- [implementation/03-architecture-blueprint.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/03-architecture-blueprint.md)
- [implementation/06-api-contracts.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/06-api-contracts.md)
- [implementation/phase-6/01-3d-output-research-and-direction.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/01-3d-output-research-and-direction.md)
- [implementation/phase-6/02-3d-module-input-contracts.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/02-3d-module-input-contracts.md)
- [implementation/phase-6/03-3d-presentation-architecture-and-hosting.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/03-3d-presentation-architecture-and-hosting.md)
- [app/services/exporter.py](/Users/nguyenquocthong/project/ai-architect-api/app/services/exporter.py:1036)
- [src/components/delivery-client.tsx](/Users/nguyenquocthong/project/ai-architect-web/src/components/delivery-client.tsx:73)

# 13. Acceptance Criteria for This Research Brief

This brief is successful only if the independent team can use it to work without hidden context from the current team.

That means the team must be able to answer, from this brief and the listed source docs:

1. what the current product already does
2. what Phase 6 is and is not trying to solve
3. what Program B and Program C each mean in concrete terms
4. what exact questions they are responsible for answering
5. what final deliverables they must hand back

# 14. Final Instruction to the Independent Team

Treat Program B and Program C as serious product and architecture programs, not as “just future extensions”.

Program B may require:

- a semantic modeling core
- a BIM exchange strategy
- and possibly a native authoring strategy

Program C may require:

- a dedicated DCC handoff architecture
- a premium asset and material operation
- and a hybrid human-in-the-loop visualization workflow

Your job is not to make these sound easy.

Your job is to determine the most credible, economically sensible, and operationally realistic path for this product if it chooses to expand beyond Program A.
