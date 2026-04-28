# Program B: Feasible BIM and Construction Authoring Upgrade Analysis

*Status: Draft*
*Date: 2026-04-14*
*Scope: Program B only*

## 1. Purpose

This document analyzes the most feasible upgrade path for **Program B: BIM and construction authoring** for the current AI Architect project.

The goal is not to describe an idealized full BIM platform.

The goal is to recommend a Program B direction that:

- fits the real architecture and delivery maturity of the current project,
- increases end-user trust and satisfaction in a visible way,
- improves architect and consultant handoff quality,
- and avoids overcommitting the team to a native BIM authoring problem too early.

This document assumes:

- Phase 6 is locked to `Program A: Presentation-grade 3D`,
- Program B remains a separate next-stage program,
- and the current product already has a package-centric workflow with canonical design state, review gates, export baseline, and delivery workspace.

References:

- [implementation/phase-6/04-independent-research-requirements-for-bim-and-premium-cgi.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/04-independent-research-requirements-for-bim-and-premium-cgi.md:1)
- [implementation/phase-6/05-phase-6-scope-lock.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/05-phase-6-scope-lock.md:1)
- [implementation/phase-6/00-README.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-6/00-README.md:1)
- [implementation/phase-3/00-README.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/phase-3/00-README.md:1)
- [docs/phase-1/00-mvp-overview.md](/Users/nguyenquocthong/project/ai-architect-mvp/docs/phase-1/00-mvp-overview.md:1)
- [3d-deep-research-report (1).md](</Users/nguyenquocthong/Downloads/3d-deep-research-report (1).md:1>)

## 2. Executive Recommendation

The most feasible Program B direction for this project is:

**Build a coordination-grade BIM handoff lane on top of the existing canonical design state, not a native BIM authoring platform as the next step.**

In practical terms, Program B should initially mean:

- stronger semantic building model inside `M4`,
- coordination-grade IFC export instead of minimal interoperability IFC,
- trustworthy quantities and schedule snapshots,
- issue and review tracking for consultant and construction coordination,
- and a handoff package that architects and downstream authoring teams can continue from with low ambiguity.

It should **not** initially mean:

- replacing Revit/ArchiCAD/other authoring tools,
- building a browser-native BIM editor,
- promising one-click construction documents from vague prompts,
- or claiming fully editable native authoring files from day one.

## 3. What Will Actually Make End Users Happier

If Program B is framed only as "more BIM", it risks solving the wrong problem.

For end users in this product, satisfaction does not come from seeing IFC as a file format. It comes from:

- fewer late surprises after the concept is approved,
- clearer confidence that the design can move into real implementation,
- cleaner contractor and consultant handoff,
- less rework caused by missing dimensions, room intent, openings, or scope ambiguity,
- visible issue tracking instead of opaque redesign churn,
- and better continuity from approved concept to real project execution.

So the user-facing promise of Program B should be:

**"Your approved design can now move forward with more traceable, reviewable, and execution-ready information."**

That is much more valuable than:

**"We added BIM export."**

## 4. Current Project Baseline

The current project has already built several foundations that make Program B possible:

- a package-centric design workflow,
- a canonical design state,
- versioning and review gates,
- export and delivery baseline,
- DXF/IFC/SVG/PDF attachment to versions,
- and a product direction where all downstream outputs should trace back to approved truth.

That means Program B does **not** need to start from zero.

It can reuse:

- `M4 Canonical Design State` as the system of record,
- existing export and manifest logic in `M8/M9`,
- review and approval controls from `M6`,
- and the package issue/handoff framing already introduced in the project.

At the same time, the current system still has important limits:

- current IFC is still simplified and should not be treated as authoring-grade,
- current DXF/IFC outputs prove interoperability intent, not construction authoring maturity,
- current package layer is more "design development baseline" than full consultant-ready coordination system,
- and there is no proven native authoring continuation workflow yet.

So Program B should be treated as an upgrade of system truth and professional handoff quality, not as a total product reset.

## 5. Why Full Native BIM Authoring Is the Wrong Next Step

There are four reasons not to jump straight into native BIM authoring.

### 5.1 It does not fit the current product advantage

The project's current advantage is:

- AI-assisted intake,
- option generation,
- canonical truth management,
- package-centric review,
- and presentation plus handoff continuity.

It is **not**:

- parametric authoring UX,
- discipline-heavy BIM editing,
- or DCC/BIM desktop replacement.

If Program B starts by copying authoring software behavior, it will move the product away from its strongest advantage.

### 5.2 It creates the most expensive engineering problem first

Native BIM authoring requires:

- editable object graph behavior,
- constraint-safe modifications,
- view regeneration,
- dimension associativity,
- schedule associativity,
- issue-aware revision ownership,
- and often discipline-specific semantics beyond architecture.

That is a much larger commitment than the current system architecture justifies.

### 5.3 It does not maximize user satisfaction soonest

Most end users will feel value earlier from:

- more reliable handoff,
- clearer quantities,
- better issue tracking,
- stronger consultant packaging,
- and fewer downstream misunderstandings.

Those gains come before native authoring.

### 5.4 The repo research already points toward a better path

The attached research favors:

- strong `M4` truth,
- minimal-to-growing IFC via IfcOpenShell,
- ThatOpen and three.js for viewer layers,
- Speckle as optional collaboration backbone,
- and Autodesk APS/Revit automation later rather than as the first dependency.

That supports a staged coordination/handoff strategy much more than a direct native authoring bet.

## 6. Recommended Definition of Program B

For this project, Program B should be defined as:

**A semantic design-to-coordination upgrade that turns approved design truth into consultant-usable BIM exchange, quantities, issue tracking, and handoff continuity.**

This definition has six parts.

### 6.1 Semantic model core

The current canonical design state must evolve from geometry-plus-package truth into a stronger semantic building model.

Minimum architectural entities should include:

- project
- site
- level
- grid or structural alignment reference
- space or room
- wall
- slab
- roof surface or roof assembly
- opening
- door
- window
- stair
- facade zone
- finish zone
- annotation anchor
- quantity snapshot
- issue
- handoff package

Minimum relationship types should include:

- room belongs to level
- wall bounds room
- opening hosted by wall
- door or window linked to opening
- material or finish assigned by zone or element
- issue linked to element, room, sheet, or viewpoint
- quantity snapshot linked to version and package
- export artifact linked to semantic source objects

### 6.2 IFC exchange lane

The first real target should be:

**coordination-grade IFC**

not:

- view-only IFC,
- and not authoring-grade round-trip IFC.

That means IFC should support enough structure for:

- space and room recognition,
- wall, slab, roof, stair, door, and window continuity,
- basic classifications and selected property sets,
- consultant review and model checking,
- and issue creation against identifiable model objects.

### 6.3 Quantities and schedules

Program B should introduce **trusted quantity snapshots**, not a promise that every quantity is instantly construction-final.

The product should first support:

- room schedule
- door and window schedule
- area schedule
- finish summary
- opening counts
- selected wall length and area summaries

Each schedule should show:

- source version,
- package revision,
- extraction timestamp,
- confidence or verification state,
- and whether manual verification is required.

### 6.4 Issue and review model

Program B should add a first-class issue layer for coordination.

Core issue fields should include:

- issue id
- issue type
- severity
- status
- due owner
- source discipline
- linked version
- linked package
- linked room or element ids
- viewpoint or screenshot references
- resolution notes

This matters because end-user trust increases when handoff changes and conflicts are visible rather than hidden in offline consultant loops.

### 6.5 Sheet and handoff continuity

Program B should not initially promise full construction documentation.

It should instead produce a stronger issued handoff package with:

- DD-plus architectural sheets,
- schedule set,
- IFC coordination file,
- DXF continuation file,
- issue register,
- and a handoff manifest that explains what is approved, what is provisional, and what still needs consultant authoring.

### 6.6 Native authoring bridge, not native authoring core

The first authoring strategy should be:

**seed downstream authoring tools**

not:

**become the authoring tool**

That means:

- improve exports so downstream BIM teams can continue efficiently,
- optionally provide connector-based push into Revit or similar environments later,
- and keep authorship boundaries explicit.

## 7. Recommended Architecture Direction

## 7.1 Core thesis

Program B should be architected as:

`approved canonical version -> semantic coordination model -> exchange package -> issue/quantity layer -> downstream authoring continuation`

not:

`approved version -> browser BIM editor`

## 7.2 Proposed subsystem breakdown

### A. Semantic coordination model service

Responsibilities:

- normalize geometry into architectural semantics,
- assign persistent semantic ids,
- store element relationships,
- and support downstream export, issue linking, and schedule extraction.

Primary ownership:

- app host
- database-backed
- version-aware

### B. IFC export service

Responsibilities:

- map semantic model to coordination-grade IFC,
- attach selected property sets,
- preserve stable ids where possible,
- and produce validation metadata.

Primary ownership:

- worker-side service
- IfcOpenShell-backed

### C. Quantity extraction service

Responsibilities:

- derive repeatable schedule snapshots,
- persist quantity tables by version and package,
- expose review flags for uncertain or derived values.

Primary ownership:

- app-side worker

### D. Coordination issue registry

Responsibilities:

- register review findings from internal KTS, consultants, or model checking,
- link issues to version, room, sheet, and IFC object ids,
- track resolution states across revisions.

Primary ownership:

- app host
- web consumption

### E. Handoff package composer

Responsibilities:

- package IFC, DXF, sheets, schedules, issue list, and manifest,
- expose release states,
- clarify package intent and limitations.

Primary ownership:

- `M8/M9` extension

### F. Optional collaboration connector layer

Responsibilities:

- push approved packages to Speckle streams,
- integrate with Solibri-style review or Autodesk workflows later,
- preserve ownership boundaries between product truth and external tools.

Primary ownership:

- later-phase connector work

## 7.3 Recommended technology stance

Recommended near-term choices:

- `M4` remains the primary system of record.
- IfcOpenShell is used for IFC generation and validation-oriented workflows.
- ezdxf remains for 2D continuation where needed.
- Speckle is optional as a collaboration/exchange layer, not the canonical core.
- Solibri remains a review/checking complement, not an authoring core.
- APS/Revit connectors remain later integrations, not phase-1 dependencies of Program B.

Avoid as core for now:

- AGPL viewer/server dependencies as primary product architecture,
- native browser BIM editing,
- mandatory dependence on vendor betas,
- and round-trip authoring claims that the current semantics cannot honestly support.

## 8. End-User-Centered Product Outcomes

If Program B is executed this way, the end user should experience five concrete improvements.

### 8.1 More confidence after concept approval

The end user no longer feels that approval is followed by a black box.

They can see:

- what information is now locked,
- what can move into coordination,
- what remains provisional,
- and what is being handed to architects, consultants, or contractors.

### 8.2 Fewer downstream surprises

Because quantities, openings, room data, and issues become explicit earlier, fewer problems appear only after external teams start redrawing.

### 8.3 Better delivery transparency

The handoff package becomes easier to understand because it contains:

- release intent,
- schedules,
- issue status,
- and a clear "approved vs not yet approved" boundary.

### 8.4 Stronger trust in professional continuation

The end user sees that the product does not stop at pretty images.

It can continue into a more serious execution-preparation lane.

### 8.5 Higher satisfaction without false promises

The product can say:

- "this package is coordination-ready"

before it says:

- "this is full construction authoring"

That honesty protects trust better than overclaiming BIM maturity.

## 9. Recommended User-Facing Additions

To maximize visible value, Program B should not stay only in backend exports.

It should surface new user-facing capabilities in the delivery workspace.

Recommended additions:

- `construction readiness` summary panel
- schedule preview tab
- quantity confidence labels
- issue tracker summary
- consultant handoff package card
- revision-to-revision change summary for coordination-impacting elements
- explicit status labels such as `Concept Approved`, `Coordination Package Ready`, `Consultant Review Open`, `Handoff Released`

These are the parts end users will actually feel.

Without them, Program B risks becoming an internal technical upgrade with limited visible product value.

## 10. Phased Plan

## 10.1 Phase B0 - Foundation hardening

Goal:

- prepare the current platform truth for Program B without changing the user promise yet

Main work:

- strengthen semantic ids and element lineage in canonical state
- define coordination-ready entity schema
- add property-set strategy
- add issue object model
- define quantity extraction rules

Exit condition:

- semantic model can support repeatable export and issue linkage

## 10.2 Phase B1 - Coordination-ready handoff

Goal:

- deliver the first real Program B value to users

Main work:

- coordination-grade IFC export
- schedule snapshots
- issue register
- stronger manifest and handoff package
- delivery workspace updates for readiness and issue visibility

Exit condition:

- architects and consultants can continue work with materially less re-modeling ambiguity

This is the first phase that should be sold as Program B.

## 10.3 Phase B2 - Authoring seed workflow

Goal:

- reduce friction for downstream BIM authoring teams

Main work:

- authoring seed conventions
- connector prototypes for Revit or equivalent target tools
- controlled import or push workflows
- better object identity preservation across revisions

Exit condition:

- downstream authoring continuation becomes efficient and traceable

## 10.4 Phase B3 - Advanced authoring and coordination expansion

Goal:

- consider whether deeper native authoring features are commercially justified

Main work:

- richer assemblies
- deeper consultant workflows
- selective edit workflows
- more advanced checking and coordination logic

Exit condition:

- only proceed if product traction proves the operating model is worth the cost

## 11. Trade-Off Analysis

### Option 1: Native BIM authoring first

Pros:

- maximum long-term control
- strongest differentiation if successful

Cons:

- highest cost
- slowest time to user value
- biggest UX and data-model burden
- highest risk of failing to satisfy professionals

Verdict:

- not recommended as the next step

### Option 2: IFC-first interoperability only

Pros:

- fastest technically
- simple to message internally

Cons:

- limited visible value to end users
- weak continuity if semantic core is shallow
- risks becoming "just another export"

Verdict:

- too narrow on its own

### Option 3: Hybrid coordination-grade semantic core plus exchange

Pros:

- fits the current architecture
- improves user-visible trust
- supports later connectors and authoring bridges
- grows toward BIM without pretending to already be there

Cons:

- still requires meaningful semantic modeling work
- requires discipline in scope control

Verdict:

- recommended

## 12. Main Risks

### 12.1 Semantic ambition outruns data quality

If the semantic model becomes more detailed than the canonical source can honestly support, the product will generate misleading BIM outputs.

Mitigation:

- separate required, inferred, and manually verified fields
- expose confidence and verification states

### 12.2 Team accidentally mixes Program B into active Phase 6

Because Program A and Program B share 3D/export/handoff concerns, scope bleed is likely.

Mitigation:

- keep Program B docs, tickets, and checkpoints separate from Phase 6 execution

### 12.3 Handoff claims exceed legal or professional reality

If the product markets coordination outputs as construction-authoring truth too early, trust damage will be severe.

Mitigation:

- explicit package labels
- explicit approval boundaries
- explicit consultant or architect verification ownership

### 12.4 Connector dependency creates false urgency

It will be tempting to jump early into Revit/APS/MCP integration.

Mitigation:

- do not depend on connectors before the internal semantic and exchange contract is stable

## 13. Decision

Program B should proceed only if the team accepts these three rules:

1. `M4` semantic strengthening is the real core investment.
2. The first saleable version of Program B is a **coordination-grade handoff lane**, not a native authoring lane.
3. User satisfaction comes from clearer continuity, lower ambiguity, and stronger handoff confidence, not from exposing BIM terminology alone.

## 14. Final Recommendation

The most feasible Program B upgrade for this project is:

**turn the current package-centric system into a coordination-grade BIM handoff platform before attempting native BIM authoring.**

That means:

- strengthen canonical semantics,
- produce better IFC and schedule outputs,
- add first-class issue and coordination tracking,
- improve delivery transparency,
- and introduce downstream authoring bridges only after the semantic core is proven.

This path best matches:

- the current architecture,
- the current product maturity,
- the attached research,
- and the objective of maximizing end-user satisfaction without making promises the product cannot yet keep.
