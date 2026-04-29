# Concept 2D Market Quality 20-Case Matrix

Status: C2DQ1 baseline

This matrix is the shared fixture set for C2DQ2-C2DQ6. It covers the breadth
needed to move from technically openable Concept 2D artifacts to review-useful,
market-quality concept packages.

The cases are not construction documentation fixtures. They are concept-review
fixtures for homeowner readability, architect plausibility, spatial planning,
drawing craft, style expression, revision usefulness, and safety/truthfulness.

## How To Use This Matrix

For each case, downstream sessions should capture:

- input source: UI brief, API fixture, or revision fixture;
- selected generated option/version id;
- generated PDF path or URL;
- generated DXF sheet paths or URLs;
- artifact quality report path or URL;
- decision per rubric dimension: `ready`, `partial`, or `failed`;
- failure signals observed or explicitly not observed;
- any `NEEDS_ARCHITECT_DECISION`.

C2DQ2-C2DQ5 may run focused fixture/unit tests instead of full browser flows.
C2DQ6 owns integrated browser/artifact truth and should run the full matrix or an
integrator-approved representative subset plus the required fresh live flow.

## Case Summary

| ID | Fixture | Typology | Primary focus |
|---|---|---|---|
| C2D-MQ-01 | 5x20 minimal warm townhouse | Townhouse | baseline geometry, storage, 3 floors |
| C2D-MQ-02 | 5x20 modern tropical elder townhouse | Townhouse | elder access, 4 floors, wet core |
| C2D-MQ-03 | 7x25 garage garden townhouse | Townhouse | larger lot, garage, garden priority |
| C2D-MQ-04 | 4x18 compact narrow townhouse | Townhouse | narrow lot, stair/core efficiency |
| C2D-MQ-05 | 6x22 Indochine family townhouse | Townhouse | family program, children, style |
| C2D-MQ-06 | 8x20 courtyard villa-like house | House | larger lot, lightwell/courtyard |
| C2D-MQ-07 | 10x20 corner modern house | House | corner lot, two frontages |
| C2D-MQ-08 | 70m2 Indochine apartment | Apartment | reference descriptors, 2 bedrooms |
| C2D-MQ-09 | 95m2 minimal warm apartment | Apartment | work-from-home, storage |
| C2D-MQ-10 | compact studio apartment | Apartment | flexible furniture, small space |
| C2D-MQ-11 | less glass warmer townhouse | Townhouse | explicit dislike suppression |
| C2D-MQ-12 | avoid dark closed interior | Townhouse | explicit dislike, light/open interior |
| C2D-MQ-13 | low-communication townhouse | Townhouse | inferred defaults, essential assumptions |
| C2D-MQ-14 | multi-generation family | Townhouse | elder bedroom, accessible wet core |
| C2D-MQ-15 | young couple social living | Townhouse | open kitchen, social priority |
| C2D-MQ-16 | shophouse/home business | Townhouse | front service zone, privacy split |
| C2D-MQ-17 | budget-constrained concept | Townhouse | simple form, tradeoffs, assumptions |
| C2D-MQ-18 | reference descriptor style | Townhouse/apartment | arches, wood, rattan, neutral palette |
| C2D-MQ-19 | revision: kitchen/storage | Revision | enlarge kitchen, reduce bedroom, add storage |
| C2D-MQ-20 | revision: style change | Revision | modern tropical to minimal warm, geometry preserved |

## C2D-MQ-01 - 5x20 Minimal Warm Townhouse

Purpose:

- Keep the accepted technical baseline but raise market quality.

Expected inputs:

- Typology: townhouse.
- Lot: 5 m x 20 m.
- Orientation: south if the UI requires an orientation.
- Program: 3 floors, 3 bedrooms, 3 bathrooms.
- Style: minimal warm.
- Priorities: low maintenance, more storage, family living, budget awareness.

Expected outputs:

- Geometry remains 5 m x 20 m across PDF, DXF, metadata, and quality report.
- Plans show a believable narrow townhouse arrangement with entrance, living,
  kitchen/dining, stairs, wet areas, bedrooms, storage, laundry, and terrace.
- Internal dimensions and furniture/fixture intent make the layout reviewable.
- Minimal warm expression appears in facade rhythm and notes through warm neutral
  palette, restrained openings, shading, and low-maintenance materials as concept
  intent.
- Homeowner summary explains assumptions and next review questions.

Failure signals:

- Any stale 5 m x 15 m geometry.
- Oversized rooms that ignore the 5 m width.
- Generic box elevation with only a style label.
- Missing storage despite storage priority.
- Quality report marks review readiness while visual/design rubric dimensions fail.

Primary rubric dimensions:

- homeowner readability;
- spatial planning;
- drawing craft;
- style expression;
- safety.

## C2D-MQ-02 - 5x20 Modern Tropical Elder Townhouse

Purpose:

- Test vertical planning and elder-friendly ground-floor logic on a narrow lot.

Expected inputs:

- Typology: townhouse.
- Lot: 5 m x 20 m.
- Program: 4 floors, 4 bedrooms, 4 bathrooms.
- Style: modern tropical.
- Priorities: elder bedroom on ground floor, natural light, ventilation, shaded
  facade, family gathering.

Expected outputs:

- Ground floor includes an elder bedroom or clearly explained alternate location
  with nearby bathroom access.
- Stairs and wet core are placed plausibly without blocking living/service flow.
- Vertical stacking is coherent across 4 floors.
- Modern tropical facade includes shading, balconies/voids/greenery cues, and
  ventilation-oriented notes.
- Concept-only assumptions state any accessibility limitations without claiming
  code compliance.

Failure signals:

- Elder bedroom omitted or placed only on an upper floor without explanation.
- Bathroom access requires implausible circulation.
- Tropical style appears only as text.
- Section fails to communicate floor levels and vertical logic.
- Any accessibility/code-compliance claim.

Primary rubric dimensions:

- architect plausibility;
- spatial planning;
- style expression;
- safety.

## C2D-MQ-03 - 7x25 Garage Garden Townhouse

Purpose:

- Test a larger townhouse with both car and garden priorities.

Expected inputs:

- Typology: townhouse.
- Lot: 7 m x 25 m.
- Program: 3 floors, 4 bedrooms, 4 bathrooms.
- Style: modern tropical.
- Priorities: garage, small front or rear garden, natural light, family dining,
  storage.

Expected outputs:

- Site/floor plans show garage position, entrance sequence, garden/green area,
  and circulation around service zones.
- Room sizes use the wider lot without becoming wasteful.
- Drawing craft uses dimensions to clarify garage, garden, and building footprint.
- Facade notes connect tropical shading/greenery to the garage/garden concept.

Failure signals:

- Garage and garden priorities conflict without a stated tradeoff.
- Front access or main entrance is unclear.
- Page composition hides site planning.
- Garden appears in notes but not drawings.

Primary rubric dimensions:

- homeowner readability;
- spatial planning;
- drawing craft;
- style expression.

## C2D-MQ-04 - 4x18 Compact Narrow Townhouse

Purpose:

- Stress narrow-lot planning, compact stair/core rules, and furniture fit.

Expected inputs:

- Typology: townhouse.
- Lot: 4 m x 18 m.
- Program: 3 floors, 2 to 3 bedrooms, 3 bathrooms.
- Style: minimal warm.
- Priorities: compact stair, efficient wet core, avoid cramped circulation,
  storage where possible.

Expected outputs:

- Room widths, stairs, bathrooms, and furniture respect a very narrow footprint.
- The package explains tight-lot tradeoffs in customer language.
- Internal dimensions make tight spaces reviewable.
- No room is shown as unrealistically wide or oversized for the lot.

Failure signals:

- Furniture or bathroom symbols cannot plausibly fit.
- Stair/core consumes the plan with no design rationale.
- Plans are too small or under-dimensioned to judge.
- The system hides major compromises instead of naming them as assumptions.

Primary rubric dimensions:

- spatial planning;
- drawing craft;
- homeowner readability;
- safety.

## C2D-MQ-05 - 6x22 Indochine Family Townhouse

Purpose:

- Test family programming, children bedrooms, and Indochine expression.

Expected inputs:

- Typology: townhouse.
- Lot: 6 m x 22 m.
- Program: 3 floors, parents bedroom, two children bedrooms, shared study/play
  zone, 3 bathrooms.
- Style: Indochine.
- Priorities: family storage, soft natural materials, balanced privacy and shared
  spaces.

Expected outputs:

- Children bedrooms and shared family zones are easy to identify.
- Plans include storage/service assumptions.
- Indochine style affects facade/notes through arches or vertical rhythm,
  timber/rattan/neutral palette descriptors, and softer shading language as
  concept intent.
- Schedules use polished customer-facing names.

Failure signals:

- Style label changes but facade and notes remain generic.
- Children bedrooms are missing, duplicated ambiguously, or implausibly sized.
- Raw internal data appears in schedules.
- Storage priority is ignored.

Primary rubric dimensions:

- spatial planning;
- style expression;
- drawing craft;
- homeowner readability.

## C2D-MQ-06 - 8x20 Courtyard Villa-Like House

Purpose:

- Test larger-lot planning with courtyard/lightwell intent.

Expected inputs:

- Typology: villa-like urban house.
- Lot: 8 m x 20 m.
- Program: 2 to 3 floors, 3 bedrooms, 3 bathrooms.
- Style: modern tropical.
- Priorities: courtyard or lightwell, indoor-outdoor living, shaded outdoor space,
  natural ventilation.

Expected outputs:

- Site/floor plans show courtyard/lightwell location and relationship to living
  spaces.
- Elevation/section explain void, shade, roof/parapet, or terrace intent at a
  concept level.
- Homeowner summary explains why the courtyard/lightwell is placed there.
- Drawing composition gives enough space to read the larger plan.

Failure signals:

- Courtyard appears only as a note.
- Void/lightwell breaks circulation or bedroom privacy.
- Section remains generic floor lines.
- Modern tropical expression lacks shading/greenery/opening cues.

Primary rubric dimensions:

- architect plausibility;
- spatial planning;
- style expression;
- drawing craft.

## C2D-MQ-07 - 10x20 Corner Modern House

Purpose:

- Test corner-lot handling and two-frontage communication.

Expected inputs:

- Typology: corner-lot urban house.
- Lot: 10 m x 20 m.
- Context: two street fronts if the system supports descriptors; otherwise
  capture as an assumption.
- Program: 2 to 3 floors, 3 to 4 bedrooms.
- Style: modern minimalist.
- Priorities: two-frontage facade, privacy, parking, clear main entrance.

Expected outputs:

- Site plan identifies primary and secondary frontage as assumptions or brief
  facts.
- Main entrance and parking/service access are clear.
- Facade/elevation notes distinguish primary and secondary frontage at concept
  level.
- Privacy tradeoffs are explained.

Failure signals:

- The package treats the corner context as verified without input/provenance.
- Two-frontage priority has no drawing impact.
- Main entrance is ambiguous.
- Facade remains a single generic front.

Primary rubric dimensions:

- homeowner readability;
- architect plausibility;
- style expression;
- safety.

## C2D-MQ-08 - 70m2 Indochine Apartment With Reference Descriptors

Purpose:

- Test apartment planning and reference descriptors without real image-analysis
  claims.

Expected inputs:

- Typology: apartment.
- Area: about 70 m2.
- Program: 2 bedrooms, 2 bathrooms if plausible.
- Style: Indochine.
- Reference descriptors: arches, wood accents, rattan texture, neutral palette,
  soft lighting.
- Priorities: practical storage, calm living room, compact dining.

Expected outputs:

- Apartment plan does not show site/lot assumptions irrelevant to an apartment.
- Rooms fit within about 70 m2 with realistic bedroom/living/kitchen/storage
  proportions.
- Reference descriptors influence style notes and interior/facade-equivalent
  presentation without claiming measured image analysis.
- Schedules and assumptions state descriptors are homeowner-provided style hints.

Failure signals:

- Apartment treated as a townhouse with floors/site boundary.
- Reference descriptors ignored or overclaimed as image recognition.
- Room areas exceed the apartment size.
- Storage and compact dining priorities are absent.

Primary rubric dimensions:

- spatial planning;
- style expression;
- safety;
- homeowner readability.

## C2D-MQ-09 - 95m2 Minimal Warm Apartment For Work From Home

Purpose:

- Test larger apartment planning with work and storage priorities.

Expected inputs:

- Typology: apartment.
- Area: about 95 m2.
- Program: 2 to 3 bedrooms, 2 bathrooms.
- Style: minimal warm.
- Priorities: work-from-home nook or room, acoustic/privacy separation, storage,
  uncluttered living.

Expected outputs:

- Work zone is visible and plausibly separated from noisy/social areas.
- Storage is present and named.
- Minimal warm palette and low-clutter concept appear in notes.
- Internal dimensions or areas make the apartment plan reviewable.

Failure signals:

- No dedicated work zone despite priority.
- Storage appears only in generic text.
- Plan area/math is inconsistent.
- Layout cannot be understood without technical handholding.

Primary rubric dimensions:

- homeowner readability;
- spatial planning;
- drawing craft;
- style expression.

## C2D-MQ-10 - Compact Studio Apartment

Purpose:

- Test flexible furniture and small-space clarity.

Expected inputs:

- Typology: studio apartment.
- Area: 30 m2 to 40 m2.
- Program: combined living/sleeping, compact kitchen, 1 bathroom.
- Style: minimal warm.
- Priorities: flexible furniture, storage, open feel, avoid clutter.

Expected outputs:

- Plan shows sleeping/living/kitchen zones without pretending separate rooms
  exist.
- Flexible furniture or convertible use is noted and drawn at concept level.
- Circulation to bathroom/kitchen remains legible.
- Assumptions explain small-space tradeoffs.

Failure signals:

- The package invents too many enclosed rooms.
- Furniture does not fit the area.
- No storage/flexible-use response.
- Labels overlap in the compact plan.

Primary rubric dimensions:

- spatial planning;
- drawing craft;
- homeowner readability.

## C2D-MQ-11 - Explicit Dislike: Less Glass, Warmer Facade

Purpose:

- Test dislike suppression against style defaults.

Expected inputs:

- Typology: townhouse.
- Lot: 5 m x 20 m or 6 m x 20 m.
- Program: 3 floors, 3 bedrooms.
- Style: modern minimalist or minimal warm.
- Explicit dislikes: too much glass, cold facade, glossy dark finishes.
- Priorities: warmer facade, privacy, easy maintenance.

Expected outputs:

- Facade/elevation reduces glassy expression and uses warmer concept material
  notes.
- Dislikes appear in assumptions or style rationale as suppressed features.
- Openings remain plausible for daylight/ventilation without ignoring privacy.
- Homeowner summary explains the tradeoff.

Failure signals:

- Facade is mostly glass or dark despite dislikes.
- Dislikes are captured in text but not reflected in drawings/notes.
- The package overcorrects into a closed/dark interior.
- Materials are stated as final specifications.

Primary rubric dimensions:

- style expression;
- revision usefulness if run as feedback;
- homeowner readability;
- safety.

## C2D-MQ-12 - Explicit Dislike: Avoid Dark Or Closed Interior

Purpose:

- Test light/open interior preference and conflict handling.

Expected inputs:

- Typology: townhouse.
- Lot: 5 m x 20 m.
- Program: 3 floors, 3 bedrooms.
- Style: minimal warm or modern tropical.
- Explicit dislikes: dark interior, closed kitchen, narrow corridors.
- Priorities: daylight, open social space, ventilation, family interaction.

Expected outputs:

- Plans support an open social zone where plausible.
- Openings/lightwell/balcony/window notes support daylight intent.
- Circulation avoids unnecessary corridor-heavy layouts.
- Assumptions explain any tight-lot constraints.

Failure signals:

- Closed/dark interior language remains.
- Kitchen/living are unnecessarily isolated.
- No daylight/ventilation design response.
- Tight-lot tradeoffs are hidden.

Primary rubric dimensions:

- spatial planning;
- style expression;
- homeowner readability.

## C2D-MQ-13 - Low-Communication Townhouse Brief

Purpose:

- Test conservative defaults and assumption provenance.

Expected inputs:

- Typology: townhouse.
- Brief: "Need a 5x20 family house, simple, bright, enough bedrooms, not too
  expensive."
- Missing details: exact floor count, room count, style, orientation, budget,
  timeline.

Expected outputs:

- System infers only safe concept defaults, such as likely 3 floors and 3
  bedrooms, with clear assumptions.
- It asks or records only essential confirmations where the product flow supports
  that behavior.
- Package remains honest about unknowns.
- Drawings are still reviewable enough for the homeowner to correct assumptions.

Failure signals:

- Missing facts are presented as verified.
- The system invents precise site/legal/code constraints.
- Output is too generic to review.
- The user must read chat history to understand assumptions.

Primary rubric dimensions:

- homeowner readability;
- safety;
- spatial planning;
- revision usefulness.

## C2D-MQ-14 - Multi-Generation Family

Purpose:

- Test elder access and family privacy without unsafe accessibility claims.

Expected inputs:

- Typology: townhouse.
- Lot: 5 m x 20 m or 6 m x 22 m.
- Program: 3 to 4 floors, parents/young family/elder member, 4 bedrooms.
- Priorities: elder bedroom on low floor, nearby bathroom, family gathering,
  privacy between generations.

Expected outputs:

- Elder room and wet area access are legible.
- Stairs/core do not create implausible movement paths.
- Bedroom privacy and shared zones are distinguishable.
- Notes avoid claiming accessibility/code compliance.

Failure signals:

- Elder priority ignored.
- Bathroom is far from elder room or placed implausibly.
- Multi-generation privacy is not reflected in zoning.
- Any code/medical/accessibility compliance claim.

Primary rubric dimensions:

- spatial planning;
- architect plausibility;
- homeowner readability;
- safety.

## C2D-MQ-15 - Young Couple Open Kitchen And Social Living

Purpose:

- Test lifestyle-driven planning for social use.

Expected inputs:

- Typology: townhouse or apartment.
- Lot/area: townhouse 5 m x 20 m or apartment about 70 m2.
- Household: young couple.
- Style: minimal warm or modern tropical.
- Priorities: open kitchen, dining/social living, flexible guest/work area,
  storage.

Expected outputs:

- Open kitchen/living/dining relationship is visible.
- Guest/work flexibility is included where space allows.
- Storage/service tradeoffs are named.
- Homeowner review questions ask whether to prioritize entertaining, storage, or
  privacy.

Failure signals:

- Kitchen is isolated without explanation.
- Social area is undersized or unclear.
- Flexible use is only a note with no plan impact.
- Drawings do not support lifestyle feedback.

Primary rubric dimensions:

- homeowner readability;
- spatial planning;
- revision usefulness.

## C2D-MQ-16 - Shophouse Or Home Business

Purpose:

- Test front service zone, privacy split, and circulation separation.

Expected inputs:

- Typology: townhouse/shophouse.
- Lot: 5 m x 25 m or 6 m x 22 m.
- Program: front business/service zone, family living, 3 bedrooms, 3 bathrooms.
- Style: modern minimalist or modern tropical.
- Priorities: customer-facing front, private family circulation, storage, service
  access.

Expected outputs:

- Ground floor clearly separates front service/business zone from private living
  areas where plausible.
- Plans show customer/family circulation intent.
- Assumptions state this is a concept zoning proposal, not legal/business
  licensing guidance.
- Facade and signage-like cues remain concept-level and do not imply permit
  readiness.

Failure signals:

- Business and private zones conflict without explanation.
- No privacy transition.
- Output claims legal/commercial suitability.
- Service/storage is omitted.

Primary rubric dimensions:

- spatial planning;
- architect plausibility;
- safety;
- homeowner readability.

## C2D-MQ-17 - Budget-Constrained Concept

Purpose:

- Test simple form, honest tradeoffs, and cost-aware concept language.

Expected inputs:

- Typology: townhouse.
- Lot: 5 m x 20 m or 6 m x 18 m.
- Program: 3 floors, 3 bedrooms.
- Style: minimal warm.
- Priorities: simple massing, avoid expensive complexity, clear assumptions,
  practical storage.
- Budget: constrained relative to requested program.

Expected outputs:

- Package favors simple massing and compact wet-core logic at concept level.
- Assumptions explain cost-related tradeoffs without claiming cost certainty.
- Drawings avoid unnecessary facade complexity.
- Homeowner review questions ask which priorities can flex if budget is tight.

Failure signals:

- Overly complex facade/form despite budget constraint.
- Budget is presented as a guaranteed estimate.
- Tradeoffs are hidden.
- Storage/practicality ignored.

Primary rubric dimensions:

- homeowner readability;
- spatial planning;
- style expression;
- safety.

## C2D-MQ-18 - Reference Descriptor Style Case

Purpose:

- Test structured style descriptors independent of real image analysis.

Expected inputs:

- Typology: townhouse or apartment.
- Base style: Indochine or minimal warm.
- Reference descriptors: arches, wood, rattan, neutral palette, soft contrast,
  plants, textured screens.
- Explicit constraint: use descriptors as inspiration only.

Expected outputs:

- Style notes map descriptors to concept features.
- Elevation/interior-equivalent drawing language changes visibly where supported.
- Assumptions state descriptors are homeowner-provided style hints.
- No measurement, material finalization, or real image-analysis claim appears.

Failure signals:

- Descriptors ignored.
- Descriptors are treated as exact extracted image facts.
- Output claims final materials.
- All styles still look visually identical.

Primary rubric dimensions:

- style expression;
- safety;
- revision usefulness.

## C2D-MQ-19 - Revision: Enlarge Kitchen, Reduce Bedroom, Add Storage

Purpose:

- Test natural-language revision truth loop and visible plan changes.

Expected inputs:

- Start from a generated townhouse concept, preferably C2D-MQ-01 or C2D-MQ-15.
- Feedback: "Make the kitchen/dining larger, reduce the secondary bedroom if
  needed, and add more storage near the entry and bedrooms."

Expected outputs:

- Revision interpreter produces changed fields for kitchen/dining priority,
  secondary bedroom tradeoff, and storage additions.
- Original geometry, floor count, and fixed requirements remain preserved.
- Regenerated package shows visible plan/schedule/assumption changes.
- Notes explain what changed and why.

Failure signals:

- Feedback is recorded but drawings do not change.
- Original selected geometry or core program is lost.
- Bedroom reduction violates minimum plausibility without a warning/tradeoff.
- Storage is only mentioned in text and not represented in plan/schedule.

Primary rubric dimensions:

- revision usefulness;
- spatial planning;
- homeowner readability;
- safety.

## C2D-MQ-20 - Revision: Modern Tropical To Minimal Warm

Purpose:

- Test style revision without geometry drift.

Expected inputs:

- Start from a modern tropical townhouse concept, preferably C2D-MQ-02 or
  C2D-MQ-03.
- Feedback: "Change the style to minimal warm. Keep the same lot, number of
  floors, and room program. Make the facade calmer and warmer."

Expected outputs:

- Style fields change from modern tropical to minimal warm.
- Lot, floor count, rooms, and selected-version identity remain stable unless the
  product creates a new traceable revision version.
- Facade/elevation and material notes visibly become calmer/warmer.
- Change summary states that geometry/program were preserved.

Failure signals:

- Geometry drifts during style-only revision.
- Style changes only in title text.
- Modern tropical features remain dominant despite the new style.
- The package claims final material specification.

Primary rubric dimensions:

- revision usefulness;
- style expression;
- drawing craft;
- safety.

## Required Coverage Check

This matrix covers:

- townhouse cases: C2D-MQ-01 through C2D-MQ-07 and C2D-MQ-11 through C2D-MQ-17;
- apartment cases: C2D-MQ-08 through C2D-MQ-10 and optionally C2D-MQ-15/C2D-MQ-18;
- narrow lots: C2D-MQ-01, C2D-MQ-02, C2D-MQ-04, C2D-MQ-11, C2D-MQ-12,
  C2D-MQ-13, C2D-MQ-14, C2D-MQ-16, C2D-MQ-17;
- larger lots: C2D-MQ-03, C2D-MQ-06, C2D-MQ-07;
- low-communication brief: C2D-MQ-13;
- explicit dislikes: C2D-MQ-11 and C2D-MQ-12;
- reference descriptors: C2D-MQ-08 and C2D-MQ-18;
- revision cases: C2D-MQ-19 and C2D-MQ-20;
- safety/truthfulness checks: every case, with focused pressure in C2D-MQ-07,
  C2D-MQ-08, C2D-MQ-13, C2D-MQ-14, C2D-MQ-16, C2D-MQ-17, C2D-MQ-18, and
  C2D-MQ-20.

## Minimum C2DQ6 Artifact Evidence

For each executed case, C2DQ6 should record:

- case id and fixture title;
- project id and selected version id;
- generated package job/bundle id;
- PDF URL/path and rendered page directory;
- DXF URL/path list and `ezdxf` openability result;
- quality report URL/path;
- package readiness fields, including `construction_ready=false`;
- geometry truth check;
- homeowner readability decision;
- architect plausibility decision;
- spatial planning decision;
- drawing craft decision;
- style expression decision;
- revision usefulness decision when applicable;
- safety/truthfulness decision;
- failure signals observed;
- final case decision.
