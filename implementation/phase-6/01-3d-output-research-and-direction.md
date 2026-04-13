# Phase 6 - 3D Output Research and Direction

## 1. Purpose

This document researches the current 3D output lane using:

- the existing internal docs,
- the current production codebase,
- and official external references for presentation-grade 3D output.

The goal is to decide what a **professional, end-user-usable 3D deliverable** should be for this product, what the **required input contract** must contain, and what the **actual output contract** should be if the system is expected to generate meaningful client-facing 3D results, including a possible walkthrough video.

This is a direction-setting document, not an implementation slice.

## 2. Core Finding

The current system already has a `derive-3d` lane, but it is **not yet a real design-grade 3D output system**.

It is currently a **workflow stub** that proves:

- state gating from locked version,
- asset persistence,
- handoff manifest inclusion,
- and basic viewer plumbing.

It does **not** yet prove:

- design-faithful geometry reconstruction,
- material-accurate scene synthesis,
- room-specific interior composition,
- camera-authored presentation output,
- or video-grade end-user deliverables.

So the correct next step is **not** to market the current lane as professional 3D presentation.

The correct next step is to build a **design-accurate presentation lane** on top of the locked canonical version and the package-centric 2D truth already established.

## 3. Internal Evidence

### 3.1 Product intent in internal docs

The product already defines M7 as a real module:

- [implementation/03-architecture-blueprint.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/03-architecture-blueprint.md:108) states `M7 3D Derivation` should be a custom pipeline using `Blender headless + Three.js`.
- [implementation/01-SRS-final.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/01-SRS-final.md:147) defines:
  - derive 3D from locked 2D versions,
  - create `1 exterior + 3 interior rooms`,
  - minimum render resolution `1920x1080`,
  - and a `GLTF` interactive viewer.
- [implementation/06-api-contracts.md](/Users/nguyenquocthong/project/ai-architect-mvp/implementation/06-api-contracts.md:398) describes an intended async derivation contract with:
  - `render_rooms`,
  - `model_format`,
  - progress events,
  - and structured 3D asset retrieval.

### 3.2 Internal docs already admit quality is not finished

- [docs/phase-1/04-module-business-requirements.md](/Users/nguyenquocthong/project/ai-architect-mvp/docs/phase-1/04-module-business-requirements.md:540) explicitly places `M7 nâng chất lượng model 3D và trace sâu hơn` in a later phase.
- The same file asks whether the 3D viewer is even P0 or only render set + lightweight model in P1, which means the organization has already recognized the difference between a basic pipeline and a real deliverable.

### 3.3 Current code reality

The current code confirms the lane is placeholder-level:

- [app/api/v1/derivation.py](/Users/nguyenquocthong/project/ai-architect-api/app/api/v1/derivation.py:23) only gates by locked status, calls GPU, saves JSON/SVG payloads, and returns `model_url + render_urls`.
- [app/services/gpu_client.py](/Users/nguyenquocthong/project/ai-architect-api/app/services/gpu_client.py:92) falls back to a minimal synthetic glTF skeleton and SVG renders if the GPU call is unavailable.
- [ai-architect-gpu/api/server.py](/Users/nguyenquocthong/project/ai-architect-gpu/api/server.py:211) currently returns:
  - a trivial `model_gltf` structure,
  - and 3 SVG placeholders (`Ngoai that`, `Noi that phong khach`, `Noi that phong ngu`).
- [src/components/viewer-client.tsx](/Users/nguyenquocthong/project/ai-architect-web/src/components/viewer-client.tsx:51) is a verification page that shows raw model text and image previews, not a real end-user 3D experience.

## 4. As-Is Contract

### 4.1 Current input

Current `derive-3d` effectively receives:

- `version_id`
- `brief_json`
- first `floor_plan_url`

Implicitly it also depends on:

- version status being `locked | handoff_ready | delivered`
- whatever geometry survived into the selected version

### 4.2 Current output

Current output is:

- `model_url`
- `render_urls[]`

In practice this means:

- one saved JSON payload acting as a very thin glTF-like model file,
- two or three saved SVG render placeholders,
- no structured camera metadata,
- no scene package,
- no MP4 walkthrough,
- no panorama set,
- no presentation manifest,
- no interactive room-aware model behavior.

### 4.3 Why this is not end-user-grade

Because it does not yet encode enough truth about:

- geometry hierarchy,
- walls / slabs / roofs / openings,
- materials,
- interior furnishing,
- lighting,
- camera framing,
- and design intent per room.

Without those layers, the output is a pipeline proof, not a client-usable 3D deliverable.

## 5. What Professional End-User 3D Output Actually Means

Based on the internal direction plus official vendor patterns, professional client-facing 3D output is not just “a model file”.

It is usually a **presentation set** composed of multiple deliverables:

1. interactive real-time scene,
2. curated still images,
3. walkthrough video,
4. optional 360 panorama / cloud presentation / QR share.

This is consistent with official vendor patterns:

- Twinmotion supports stills, panoramas, videos, presentations, and cloud sharing with links or QR codes. Sources:
  - [Creating Presentations](https://dev.epicgames.com/documentation/tr-tr/twinmotion/creating-presentations)
  - [Images and Panoramas](https://dev.epicgames.com/documentation/ja-jp/twinmotion/images-and-panoramas)
  - [Panorama Sets](https://dev.epicgames.com/documentation/twinmotion/panorama-sets)
  - [Twinmotion Cloud Web Drive overview](https://dev.epicgames.com/documentation/fr-fr/twinmotion/an-overview-of-the-twinmotion-cloud-web-drive-in-twinmotion)
- Enscape supports walkthrough-oriented visualization, named views, video export, web standalones, panoramas, QR sharing, and virtual tours. Sources:
  - [Feature Highlights for Enscape](https://docs.chaos.com/display/EREVIT/Feature%2BHighlights)
  - [Rendering](https://docs.chaos.com/display/ERHINO/Rendering)
  - [Panorama and Cardboard](https://docs.chaos.com/display/ERHINO/Panorama%2Band%2BCardboard)
  - [Manage Uploads](https://docs.chaos.com/display/ERHINO/Manage%2BUploads)
  - [Web Standalone Export](https://docs.chaos.com/display/EREVIT/Web%2BStandalone%2BExport)
- glTF is an appropriate runtime delivery format for real-time presentation because it supports scene structure, materials, cameras, and animation. Sources:
  - [glTF 2.0 Specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
  - [glTF overview](https://www.khronos.org/gltf/)

## 6. Recommended End-User Target

### 6.1 The correct near-term target

The best near-term target is:

**Design-accurate presentation package**, not “marketing CGI” and not “BIM-grade digital twin”.

That means the system should aim to produce 3D outputs that are:

- faithful to the approved spatial layout,
- faithful to the approved facade and opening logic,
- materially consistent with the approved design direction,
- believable enough for client decision-making,
- and packaged in presentation formats that non-technical end users can consume directly.

### 6.2 What should explicitly be avoided

Do not promise:

- construction-accurate visualization,
- exact procurement-level material fidelity,
- exact FF&E specification fidelity,
- or photoreal marketing film quality

until the input contract includes those layers explicitly.

## 7. Recommended Input Contract

If the product wants professional 3D output, the input can no longer be just:

- `brief_json`
- plus one floor plan image.

It needs a proper **3D scene input contract**.

### 7.1 Required upstream object

The true source should be:

`locked canonical version + issued review-ready geometry package`

not raw intake brief and not unstructured render prompts.

### 7.2 Minimum required input fields

The 3D scene builder should receive:

1. Project metadata
- project id
- version id
- revision label
- project type
- presentation mode

2. Canonical geometry
- levels
- floor-to-floor heights
- wall centerlines or solids
- slabs
- roof form
- openings with width / height / sill / head
- stair geometry
- room polygons and room names
- exterior footprint and site boundary

3. Architectural semantics
- room type taxonomy
- primary facade designation
- circulation spine
- public/private zoning
- key view axes

4. Design direction
- approved style profile
- facade language
- material palette
- color palette
- must-have visual cues
- must-avoid visual cues

5. Presentation directives
- target output set
- target rooms to visualize
- preferred camera narrative
- day / dusk / night mode
- hero shot priorities

6. Optional but high-value inputs
- furniture density preset
- landscaping preset
- lighting preset
- neighborhood context preset
- branding / title card / watermark rules

### 7.3 Required new internal artifact

To support the above, the product should introduce a new internal artifact:

`presentation_scene_spec`

This should be a structured JSON contract generated from:

- locked canonical geometry,
- style direction,
- and room-level scene rules.

This artifact becomes the handoff object to the 3D renderer.

## 8. Recommended Output Contract

### 8.1 Minimum professional output set

The system should output a bundled 3D presentation set:

1. `scene.glb`
- runtime web model
- optimized for browser viewing

2. `renders/`
- `exterior_hero_day.png`
- `exterior_entry.png`
- `living_room.png`
- `kitchen_dining.png`
- `master_bedroom.png`

3. `walkthrough.mp4`
- 1080p minimum
- 30 fps
- client-facing camera path
- 45 to 90 seconds

4. `presentation_manifest.json`
- scene metadata
- camera shot list
- room mapping
- output resolutions
- asset generation timestamp
- degraded flags

5. Optional premium outputs
- `panorama_set/`
- `web_presentation_url`
- `storyboard.pdf`

### 8.2 Minimum API response shape

The future API should return something closer to:

```json
{
  "version_id": "uuid",
  "scene_url": "/media/.../scene.glb",
  "render_urls": {
    "exterior": [
      "/media/.../exterior_hero_day.png",
      "/media/.../exterior_entry.png"
    ],
    "interiors": [
      { "room": "living_room", "url": "/media/.../living_room.png" },
      { "room": "kitchen_dining", "url": "/media/.../kitchen_dining.png" },
      { "room": "master_bedroom", "url": "/media/.../master_bedroom.png" }
    ]
  },
  "video_url": "/media/.../walkthrough.mp4",
  "panorama_urls": [],
  "presentation_manifest_url": "/media/.../presentation_manifest.json",
  "generation_metadata": {
    "renderer": "blender-headless",
    "scene_spec_version": "v1",
    "quality_tier": "client_presentation",
    "degraded": false
  }
}
```

## 9. Recommended Technical Direction

## 9.1 Best-fit architecture direction

The most reasonable direction, given the current stack and docs, is:

**Blender-first deterministic presentation pipeline**

with:

- `presentation_scene_spec` as the intermediate contract,
- `GLB` as the runtime model output,
- `PNG/EXR` still renders,
- and `MP4` walkthrough output.

This is the best fit because:

- the architecture blueprint already points to Blender headless,
- the current product already owns the canonical design state,
- the web app already has a viewer route and delivery bundle model,
- and a deterministic internal pipeline is easier to align with package-centric truth than prompt-only image generation.

### 9.2 Why not make Twinmotion/Enscape the primary engine now

Twinmotion and Enscape are strong references for the **output standard** and user expectations, but they are not the best primary engine for this product’s first production 3D lane because:

- they sit best on top of mature authored models,
- they are excellent for presentation and sharing,
- but the current product still needs a strong machine-owned scene synthesis contract first.

So the right sequencing is:

1. build internal deterministic scene synthesis,
2. output presentation-grade assets from Blender,
3. only then consider an optional Twinmotion / Enscape bridge for premium visualization tiers.

### 9.3 Role of Solibri

Solibri is useful for validation / BIM review workflows, not for client-facing presentation output.

It should remain in the interoperability / checking lane, not the end-user 3D presentation lane.

## 10. What “Video Demo Accurate to the Design” Requires

If the product wants to claim:

“video 3D demo chinh xac design”

then the system must lock these items first:

1. geometric truth
- room sizes
- openings
- facade proportions
- ceiling heights
- stair positions

2. material truth
- wall / floor / ceiling families
- facade materials
- key accent materials

3. scene truth
- required furniture proxies by room type
- lighting mode
- exterior entourage policy

4. camera truth
- shot list
- path timing
- camera height
- target focal points

Without these four layers, the video is only “visual flavor”, not “accurate design presentation”.

## 11. Recommended Delivery Tiers

### Tier A - End-user concept presentation

Use when:

- the client needs to understand the space,
- compare design direction,
- and validate the concept emotionally and spatially.

Outputs:

- 1 GLB scene
- 4 to 6 still renders
- 1 MP4 walkthrough

This should be the recommended Phase 6 target.

### Tier B - Premium immersive sharing

Adds:

- panorama set
- web presentation
- QR sharing
- optional voiceover / captions

This is Phase 6.5 or Phase 7.

### Tier C - Marketing CGI

Adds:

- high-detail entourage
- advanced post-processing
- polished cinematic edit

This should not be promised in the next phase.

## 12. Proposed Phase 6 Scope

### 12.1 What to build

1. `presentation_scene_spec`
2. deterministic scene builder from locked canonical version
3. Blender headless render pipeline
4. GLB export
5. still-render pack
6. MP4 walkthrough generation
7. presentation manifest
8. real viewer page, not debug viewer

### 12.2 What not to build yet

1. full BIM semantic model for all disciplines
2. photoreal marketing-grade animation system
3. editable CAD-to-DCC live sync
4. furniture design-grade interior styling engine

## 13. Decisions Still Needed

The product owner should explicitly choose:

1. Is Phase 6 target `Tier A` only, or `Tier A + panorama/web presentation`?
2. Should the first video be:
- exterior-only,
- exterior + core public interior,
- or full room sequence?
3. Is material accuracy expected at:
- style-direction level,
- or near-specification level?
4. Is the first end-user 3D deliverable meant for:
- client approval,
- sales/demo,
- or contractor coordination?

If the answer is “client approval”, the recommended scope is:

- `GLB + 5 still renders + 1 walkthrough MP4 + manifest`

from a locked version only.

## 14. Final Recommendation

The right direction is:

- do not treat the current `derive-3d` lane as finished,
- do not jump directly to photoreal marketing output,
- and do not anchor the first serious 3D phase on a prompt-only renderer.

The most defensible next step is:

**build a package-centric, deterministic 3D presentation lane from locked canonical geometry into `scene spec -> Blender -> GLB + renders + MP4 walkthrough`.**

That is the shortest path from the current architecture to a professional end-user output that is credible, demoable, and aligned with the existing product truth model.
