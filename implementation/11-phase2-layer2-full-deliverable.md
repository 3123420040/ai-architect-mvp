# 11 - Phase 2: Geometry Layer 2 & Full Deliverable Expansion

*Version: 1.0 FINAL*
*Ngay chot: Apr 12, 2026*
*Prerequisite: Layer 1.5 (CP7) phai hoan tat truoc khi bat dau Phase 2*
*Input: 05-system-design.md Q2/Q3, 10-p1-2d-deliverable-integration.md Bac 3, 19-p1-2d-deliverable-product-requirements.md*

---

## 1. Muc tieu Phase 2 Deliverable

Nang cap tu "schematic design package" (Layer 1.5, 2 elevations, 1 section) len **"design development package"** voi:

- Full geometry Layer 2 (wall assemblies, material properties, detailed openings)
- 4 exterior elevations (tat ca 4 mat)
- DXF export tu geometry (cho KTS/contractor dung trong CAD)
- Door/window schedules
- Room/area schedules
- Enhanced dimensioning (full dimension chains)
- IFC export foundation (cho BIM interop)

### Deliverable positioning

| | Phase 1 MVP | Phase 1 MVP+ (Layer 1.5) | **Phase 2 (Layer 2)** |
|---|---|---|---|
| Package type | Professional PDF | Schematic Design | **Design Development** |
| Geometry | Basic metadata | Walls, openings, rooms | **Full assemblies, materials, MEP zones** |
| Elevations | None | 2 principal | **4 full** |
| Sections | None | 1 key section | **2+ sections** |
| Dimensions | Room labels | Overall + key | **Full dimension chains** |
| Schedules | None | None | **Door, window, room, area** |
| Export formats | PDF + SVG | PDF + SVG (vector) | **PDF + SVG + DXF + IFC (basic)** |
| Interop | None | None | **CAD/BIM handoff** |

---

## 2. Geometry Layer 2 Schema

### 2.1 Tong quan thay doi tu Layer 1.5

```
Layer 1.5 (da co):                    Layer 2 (moi):
  walls: position + thickness          walls: + assembly, materials, fire_rating
  openings: position + size            openings: + model_id, frame, glazing, hardware
  rooms: polygon + name + area         rooms: + finish_floor, finish_wall, finish_ceiling
  levels: elevation + floor_to_floor   levels: + slab_thickness, ceiling_height
  site: boundary + orientation         site: + topography, utilities, landscape_zones
  roof: type + height                  roof: + layers, slope, drainage, material
  stairs: basic                        stairs: + tread/riser, handrail, landing
  fixtures: basic                      fixtures: + model_id, manufacturer, specs
  markers: section/elevation           markers: + detail markers, grid lines
  (KHONG CO)                           grids: structural grid system
  (KHONG CO)                           schedules_data: door/window/room data
  (KHONG CO)                           annotations: dimension chains, notes
```

### 2.2 Full Layer 2 JSON Schema

```json
{
  "$schema": "ai-architect-geometry-v2",
  "version": "2.0",
  "units": "metric",
  "precision": 3,

  "project_info": {
    "name": "Nha pho Tan Binh",
    "address": "123 Nguyen Van Cu, Q. Tan Binh, TP.HCM",
    "lot_area_m2": 100,
    "building_area_m2": 80,
    "total_floor_area_m2": 320,
    "building_coverage_ratio": 0.8,
    "floor_area_ratio": 3.2
  },

  "grids": {
    "axes_x": [
      {"id": "A", "position": 0.0},
      {"id": "B", "position": 2.5},
      {"id": "C", "position": 5.0}
    ],
    "axes_y": [
      {"id": "1", "position": 0.0},
      {"id": "2", "position": 4.8},
      {"id": "3", "position": 8.0},
      {"id": "4", "position": 12.0},
      {"id": "5", "position": 16.0},
      {"id": "6", "position": 20.0}
    ]
  },

  "levels": [
    {
      "id": "L0",
      "name": "Mat dat",
      "elevation_m": 0.0,
      "type": "ground"
    },
    {
      "id": "L1",
      "name": "Tang 1",
      "elevation_m": 0.45,
      "floor_to_floor_m": 3.6,
      "slab_thickness_m": 0.15,
      "clear_height_m": 3.0,
      "ceiling_height_m": 2.8,
      "type": "floor"
    },
    {
      "id": "L2",
      "name": "Tang 2",
      "elevation_m": 4.05,
      "floor_to_floor_m": 3.3,
      "slab_thickness_m": 0.12,
      "clear_height_m": 2.85,
      "ceiling_height_m": 2.7,
      "type": "floor"
    },
    {
      "id": "L3",
      "name": "Tang 3",
      "elevation_m": 7.35,
      "floor_to_floor_m": 3.3,
      "slab_thickness_m": 0.12,
      "clear_height_m": 2.85,
      "ceiling_height_m": 2.7,
      "type": "floor"
    },
    {
      "id": "L4",
      "name": "Tang thuong",
      "elevation_m": 10.65,
      "floor_to_floor_m": 3.0,
      "slab_thickness_m": 0.12,
      "clear_height_m": 2.55,
      "ceiling_height_m": 2.4,
      "type": "floor"
    },
    {
      "id": "LR",
      "name": "Mai",
      "elevation_m": 13.65,
      "type": "roof"
    }
  ],

  "site": {
    "boundary": [[0,0], [5,0], [5,20], [0,20]],
    "orientation_north_deg": 180,
    "setbacks": {
      "front_m": 0,
      "back_m": 2,
      "left_m": 0,
      "right_m": 0
    },
    "access_points": [
      {"type": "main_entrance", "position": [2.5, 0], "width_m": 1.2},
      {"type": "garage", "position": [4.0, 0], "width_m": 2.4}
    ],
    "landscape_zones": [
      {"type": "front_yard", "polygon": [[0,0],[5,0],[5,-3],[0,-3]]},
      {"type": "rear_garden", "polygon": [[0,18],[5,18],[5,20],[0,20]]}
    ],
    "utilities": {
      "water_connection": [0, 10],
      "sewer_connection": [0, 12],
      "electrical_pole": [5, 0]
    }
  },

  "walls": [
    {
      "id": "w1",
      "level": "L1",
      "start": [0, 0],
      "end": [5, 0],
      "type": "exterior",
      "assembly": {
        "total_thickness_m": 0.2,
        "layers": [
          {"material": "plaster", "thickness_m": 0.015, "side": "exterior"},
          {"material": "brick_100", "thickness_m": 0.1},
          {"material": "insulation", "thickness_m": 0.05},
          {"material": "brick_100", "thickness_m": 0.1, "note": "inner leaf nha pho khong co"},
          {"material": "plaster", "thickness_m": 0.015, "side": "interior"}
        ]
      },
      "fire_rating": null,
      "structural": false,
      "extends_levels": ["L1", "L2", "L3", "L4"],
      "grid_reference": {"axis": "1", "offset": 0}
    },
    {
      "id": "w2",
      "level": "L1",
      "start": [0, 0],
      "end": [0, 20],
      "type": "party_wall",
      "assembly": {
        "total_thickness_m": 0.2,
        "layers": [
          {"material": "plaster", "thickness_m": 0.015},
          {"material": "reinforced_concrete", "thickness_m": 0.17},
          {"material": "plaster", "thickness_m": 0.015}
        ]
      },
      "fire_rating": "REI60",
      "structural": true,
      "extends_levels": ["L1", "L2", "L3", "L4"],
      "grid_reference": {"axis": "A", "offset": 0}
    },
    {
      "id": "w10",
      "level": "L1",
      "start": [0, 4.8],
      "end": [5, 4.8],
      "type": "interior",
      "assembly": {
        "total_thickness_m": 0.1,
        "layers": [
          {"material": "plaster", "thickness_m": 0.015},
          {"material": "brick_75", "thickness_m": 0.07},
          {"material": "plaster", "thickness_m": 0.015}
        ]
      },
      "fire_rating": null,
      "structural": false,
      "extends_levels": ["L1"]
    }
  ],

  "openings": [
    {
      "id": "D01",
      "wall_id": "w1",
      "type": "door",
      "subtype": "entrance_double",
      "position_along_wall_m": 1.5,
      "width_m": 1.2,
      "height_m": 2.4,
      "sill_height_m": 0.0,
      "level": "L1",
      "frame": {
        "material": "aluminum",
        "color": "dark_grey",
        "profile": "slim"
      },
      "panel": {
        "material": "tempered_glass",
        "type": "swing",
        "swing_direction": "inward",
        "leaves": 2
      },
      "hardware": {
        "handle": "lever",
        "lock": "multipoint"
      },
      "fire_rating": null,
      "schedule_mark": "D01",
      "schedule_group": "entrance_doors"
    },
    {
      "id": "W01",
      "wall_id": "w1",
      "type": "window",
      "subtype": "fixed_casement",
      "position_along_wall_m": 3.5,
      "width_m": 1.0,
      "height_m": 1.5,
      "sill_height_m": 0.9,
      "level": "L1",
      "frame": {
        "material": "aluminum",
        "color": "dark_grey",
        "profile": "slim"
      },
      "glazing": {
        "type": "double_low_e",
        "thickness_mm": 24,
        "u_value": 1.1,
        "solar_heat_gain": 0.25
      },
      "operation": {
        "type": "casement",
        "hinge_side": "left"
      },
      "schedule_mark": "W01",
      "schedule_group": "facade_windows"
    }
  ],

  "rooms": [
    {
      "id": "r1",
      "name": "Phong khach",
      "name_en": "Living Room",
      "type": "living",
      "level": "L1",
      "polygon": [[0.2, 0.2], [4.8, 0.2], [4.8, 4.6], [0.2, 4.6]],
      "area_m2": 20.24,
      "perimeter_m": 18.4,
      "clear_height_m": 2.8,
      "finishes": {
        "floor": {"material": "porcelain_tile", "size": "600x600", "color": "light_grey"},
        "wall": {"material": "painted_plaster", "color": "white", "code": "RAL9010"},
        "ceiling": {"material": "painted_plaster", "color": "white", "type": "flat"},
        "baseboard": {"material": "porcelain", "height_mm": 80}
      },
      "doors": ["D01", "D03"],
      "windows": ["W01"],
      "electrical": {
        "outlets": 6,
        "switches": 2,
        "lighting_points": 4
      }
    },
    {
      "id": "r2",
      "name": "Bep",
      "name_en": "Kitchen",
      "type": "kitchen",
      "level": "L1",
      "polygon": [[0.2, 5.0], [4.8, 5.0], [4.8, 7.8], [0.2, 7.8]],
      "area_m2": 12.88,
      "perimeter_m": 14.8,
      "clear_height_m": 2.8,
      "finishes": {
        "floor": {"material": "porcelain_tile", "size": "600x600", "color": "light_grey"},
        "wall": {"material": "ceramic_tile", "size": "300x600", "color": "white", "height_m": 1.2, "note": "backsplash"},
        "ceiling": {"material": "painted_plaster", "color": "white", "type": "flat"},
        "baseboard": {"material": "porcelain", "height_mm": 80}
      },
      "doors": ["D03"],
      "windows": ["W02"],
      "fixtures_refs": ["fix_kitchen_counter", "fix_sink", "fix_cooktop"],
      "plumbing": {
        "hot_water": true,
        "cold_water": true,
        "waste": true,
        "gas": true
      }
    }
  ],

  "stairs": [
    {
      "id": "s1",
      "from_level": "L1",
      "to_level": "L2",
      "type": "u_turn",
      "position": [[3.5, 8.5], [5.0, 12.0]],
      "direction": "up",
      "geometry": {
        "run_count": 20,
        "riser_height_mm": 165,
        "tread_depth_mm": 250,
        "width_m": 0.9,
        "landing_depth_m": 0.9,
        "turn_at_step": 10
      },
      "handrail": {
        "material": "steel",
        "height_mm": 900,
        "sides": ["left"]
      },
      "finish": {
        "tread": "granite",
        "riser": "painted_plaster"
      },
      "headroom_m": 2.1,
      "code_compliance": {
        "min_headroom_m": 2.0,
        "max_riser_mm": 180,
        "min_tread_mm": 220,
        "status": "pass"
      }
    }
  ],

  "fixtures": [
    {
      "id": "fix_kitchen_counter",
      "type": "kitchen_counter",
      "room_id": "r2",
      "level": "L1",
      "polygon": [[0.3, 5.1], [2.5, 5.1], [2.5, 5.7], [0.3, 5.7]],
      "height_m": 0.85,
      "material": "granite_black",
      "manufacturer": null,
      "model": null
    },
    {
      "id": "fix_toilet_1",
      "type": "toilet",
      "subtype": "wall_hung",
      "room_id": "r3",
      "level": "L1",
      "position": [4.2, 3.5],
      "rotation_deg": 0,
      "dimensions": {"width_m": 0.36, "depth_m": 0.54},
      "manufacturer": "TOTO",
      "model": "CW762B"
    },
    {
      "id": "fix_sink_1",
      "type": "sink",
      "subtype": "kitchen_single",
      "room_id": "r2",
      "level": "L1",
      "position": [1.5, 5.3],
      "dimensions": {"width_m": 0.6, "depth_m": 0.45},
      "plumbing_connection": true
    }
  ],

  "roof": {
    "type": "flat_with_parapet",
    "elevation_top_m": 13.95,
    "parapet_height_m": 0.6,
    "slope_percent": 2,
    "drainage_direction": "rear",
    "layers": [
      {"material": "waterproof_membrane", "thickness_mm": 3},
      {"material": "insulation_xps", "thickness_mm": 50},
      {"material": "reinforced_concrete_slab", "thickness_mm": 120},
      {"material": "plaster_ceiling", "thickness_mm": 15}
    ],
    "drainage_points": [
      {"position": [2.5, 19], "type": "internal_drain", "size_mm": 100}
    ],
    "terrace_zones": [
      {"polygon": [[1, 16], [4, 16], [4, 19], [1, 19]], "finish": "ceramic_tile", "use": "terrace"}
    ]
  },

  "markers": {
    "sections": [
      {"id": "S1", "start": [2.5, 0], "end": [2.5, 20], "direction": "east", "label": "Section A-A"},
      {"id": "S2", "start": [0, 10], "end": [5, 10], "direction": "north", "label": "Section B-B"}
    ],
    "elevations": [
      {"id": "E1", "face": "south", "label": "Mat dung chinh (South)"},
      {"id": "E2", "face": "north", "label": "Mat sau (North)"},
      {"id": "E3", "face": "east", "label": "Mat ben phai (East)"},
      {"id": "E4", "face": "west", "label": "Mat ben trai (West)"}
    ],
    "details": [
      {"id": "DT1", "position": [2.5, 0], "label": "Chi tiet lan can", "sheet_ref": "A7"},
      {"id": "DT2", "position": [0, 10], "label": "Chi tiet cau thang", "sheet_ref": "A8"}
    ]
  },

  "dimensions_config": {
    "style": "architectural",
    "text_height_mm": 2.5,
    "arrow_type": "tick",
    "extension_line_gap_mm": 2,
    "chains": {
      "exterior": true,
      "interior_major": true,
      "interior_minor": true,
      "openings": true,
      "grid_to_grid": true
    }
  }
}
```

### 2.3 So sanh Layer 1 vs Layer 1.5 vs Layer 2

| Field | Layer 1 (MVP) | Layer 1.5 (MVP+) | Layer 2 (Phase 2) |
|-------|---------------|-------------------|---------------------|
| walls | Khong co | position, thickness, type | + assembly layers, materials, fire_rating, structural flag |
| openings | Khong co | position, size, type | + frame material, glazing spec, hardware, operation, schedule_mark |
| rooms | name, area (flat) | polygon, level | + finishes (floor/wall/ceiling), plumbing, electrical counts |
| levels | Khong co | elevation, floor_to_floor | + slab_thickness, clear_height, ceiling_height |
| site | Khong co | boundary, orientation | + topography, utilities, landscape_zones, access_points |
| roof | Khong co | type, height | + layers, slope, drainage, terrace_zones |
| stairs | Khong co | basic position, type | + tread/riser geometry, handrail, finish, code_compliance |
| fixtures | Khong co | basic position, type | + manufacturer, model, dimensions, plumbing_connection |
| grids | Khong co | Khong co | structural grid system (axes_x, axes_y) |
| schedules_data | Khong co | Khong co | door/window/room schedule data embedded in openings/rooms |
| dimensions_config | Khong co | Khong co | dimension chain configuration |
| project_info | basic (brief) | basic | lot_area, building_area, FAR, coverage ratio |

---

## 3. 4 Exterior Elevations

### 3.1 Yeu cau

Phase 2 generate 4 mat dung day du (thay vi 2 principal cua MVP+):

| Elevation | Face | Ten | Noi dung |
|-----------|------|-----|----------|
| E1 | South | Mat dung chinh | Full facade: cua chinh, cua so, ban cong, mai, ground line |
| E2 | North | Mat sau | Cua so phia sau, bep, san phoi, cau thang phia ngoai (neu co) |
| E3 | East | Mat ben phai | Gieng troi (neu co), cua so hong, tuong chung (neu nha pho) |
| E4 | West | Mat ben trai | Tuong chung/lan can, cua so, ong thoat nuoc |

### 3.2 Noi dung moi elevation sheet

```
Required cho moi elevation:
- Facade openings (doors, windows) dung vi tri va kich thuoc tu geometry
- Roof form / parapet line
- Ground line / grade line
- Floor level markers (elevation numbers)
- Vertical dimensions: floor-to-floor, tong chieu cao, parapet
- Material tags (conceptual -> chi tiet Phase 2)
  - Phase 2 tags: "Gach op 200x400", "Son Dulux RAL9010", "Kinh Low-E 24mm"
- Ban cong / lan can / logia
- Ong thoat nuoc / drainage
- Scale notation (1:100 hoac 1:50)
- Section markers pointing to section sheets
- Grid lines (structural grid overlay)
```

### 3.3 Elevation Renderer upgrade (tu MVP+)

```python
class ElevationRendererV2(ElevationRenderer):
    """Upgrade tu 2 principal -> 4 full elevations voi materials."""
    
    def render_elevation(self, geometry: dict, face: str) -> SVGSheet:
        svg = SVGCanvas(width=sheet_width, height=sheet_height)
        
        # 1. Ground line
        svg.add_ground_line(geometry["site"])
        
        # 2. Building outline tu walls
        walls = self._get_walls_for_face(geometry["walls"], face)
        svg.add_building_outline(walls, geometry["levels"])
        
        # 3. Openings (doors, windows) - dung schedule data
        for opening in self._get_openings_for_face(geometry["openings"], face):
            svg.add_opening(opening, style=self._opening_style(opening))
            # Phase 2: add schedule mark tag (D01, W01)
            svg.add_schedule_tag(opening["schedule_mark"], opening["position"])
        
        # 4. Floor level markers
        for level in geometry["levels"]:
            svg.add_level_marker(level["elevation_m"], level["name"])
        
        # 5. Roof / parapet
        svg.add_roof_profile(geometry["roof"], face)
        
        # 6. Material tags
        for wall in walls:
            if wall.get("assembly"):
                svg.add_material_tag(
                    wall["assembly"]["layers"],
                    position=self._tag_position(wall, face)
                )
        
        # 7. Dimensions
        svg.add_vertical_dimensions(geometry["levels"])
        svg.add_horizontal_dimensions(walls, geometry["openings"], face)
        
        # 8. Grid lines
        if geometry.get("grids"):
            svg.add_grid_overlay(geometry["grids"], face)
        
        # 9. Section markers
        for section in geometry["markers"]["sections"]:
            if self._section_visible_from(section, face):
                svg.add_section_marker(section)
        
        return svg
```

---

## 4. DXF Export

### 4.1 Tech stack

| Component | Library | Version | License |
|-----------|---------|---------|---------|
| DXF generation | `ezdxf` | >= 1.0 | MIT |
| Geometry processing | `shapely` | >= 2.0 | BSD |
| Coordinate transformation | `numpy` | >= 1.24 | BSD |

### 4.2 DXF Layer mapping

```python
DXF_LAYER_MAP = {
    # Architectural layers
    "A-WALL-EXTR": {"color": 7, "lineweight": 50, "description": "Exterior walls"},
    "A-WALL-INTR": {"color": 7, "lineweight": 30, "description": "Interior walls"},
    "A-WALL-PRTY": {"color": 7, "lineweight": 50, "description": "Party/shared walls"},
    "A-DOOR": {"color": 3, "lineweight": 25, "description": "Doors"},
    "A-GLAZ": {"color": 5, "lineweight": 25, "description": "Windows/glazing"},
    "A-STRS": {"color": 6, "lineweight": 25, "description": "Stairs"},
    "A-FLOR-FIXT": {"color": 8, "lineweight": 18, "description": "Floor fixtures"},
    "A-FLOR-FURN": {"color": 9, "lineweight": 13, "description": "Furniture"},
    "A-FLOR-PATT": {"color": 251, "lineweight": 5, "description": "Floor patterns/hatching"},
    
    # Annotation layers
    "A-ANNO-DIMS": {"color": 2, "lineweight": 13, "description": "Dimensions"},
    "A-ANNO-TEXT": {"color": 7, "lineweight": 13, "description": "General text/notes"},
    "A-ANNO-ROOM": {"color": 4, "lineweight": 13, "description": "Room tags"},
    "A-ANNO-SYMB": {"color": 1, "lineweight": 18, "description": "Symbols (north, section markers)"},
    "A-ANNO-GRID": {"color": 8, "lineweight": 9, "description": "Grid lines"},
    "A-ANNO-LEVL": {"color": 3, "lineweight": 13, "description": "Level markers"},
    
    # Site layers
    "A-SITE-BNDY": {"color": 1, "lineweight": 35, "description": "Site boundary"},
    "A-SITE-BLDG": {"color": 7, "lineweight": 50, "description": "Building footprint"},
    "A-SITE-PVMT": {"color": 252, "lineweight": 18, "description": "Paving/hardscape"},
    "A-SITE-LAND": {"color": 3, "lineweight": 13, "description": "Landscape"},
    
    # Elevation/Section layers
    "A-ELEV-OUTL": {"color": 7, "lineweight": 50, "description": "Elevation outline"},
    "A-ELEV-OPEN": {"color": 5, "lineweight": 25, "description": "Elevation openings"},
    "A-ELEV-MATL": {"color": 251, "lineweight": 9, "description": "Material hatching"},
    "A-SECT-CUT": {"color": 7, "lineweight": 70, "description": "Section cut (pochè)"},
    "A-SECT-BEYND": {"color": 253, "lineweight": 18, "description": "Section beyond"},
    
    # Title block
    "A-ANNO-TTLB": {"color": 7, "lineweight": 35, "description": "Title block border"},
    "A-ANNO-TTLB-TEXT": {"color": 7, "lineweight": 13, "description": "Title block text"},
}
```

### 4.3 DXF Export Pipeline

```python
class DXFExporter:
    """Export geometry Layer 2 to DXF file."""
    
    def __init__(self, geometry: dict, config: DXFConfig):
        self.geometry = geometry
        self.config = config
        self.doc = ezdxf.new("R2018")  # AutoCAD 2018 format
        self._setup_layers()
        self._setup_styles()
    
    def _setup_layers(self):
        for name, props in DXF_LAYER_MAP.items():
            self.doc.layers.add(
                name,
                color=props["color"],
                lineweight=props["lineweight"]
            )
    
    def _setup_styles(self):
        # Text styles
        self.doc.styles.add("AI_ARCH_BODY", font="Arial")
        self.doc.styles.add("AI_ARCH_TITLE", font="Arial")
        self.doc.styles.add("AI_ARCH_DIM", font="Arial")
        
        # Dimension style
        dimstyle = self.doc.dimstyles.add("AI_ARCH_DIM")
        dimstyle.dxf.dimtxt = 2.5    # Text height 2.5mm
        dimstyle.dxf.dimasz = 2.0    # Arrow size 2mm
        dimstyle.dxf.dimtsz = 1.5    # Tick size (architectural)
        dimstyle.dxf.dimexe = 2.0    # Extension line extension
        dimstyle.dxf.dimexo = 2.0    # Extension line offset
    
    def export(self) -> bytes:
        """Generate complete DXF with all sheets in model space + paper space."""
        
        msp = self.doc.modelspace()
        
        # Model space: draw everything at 1:1 scale
        for level in self.geometry["levels"]:
            if level["type"] == "floor":
                self._draw_floor_plan(msp, level)
        
        self._draw_site_plan(msp)
        self._draw_elevations(msp)
        self._draw_sections(msp)
        
        # Paper space: create layout sheets with viewports
        for sheet_def in self._get_sheet_definitions():
            layout = self.doc.layouts.new(sheet_def["name"])
            self._setup_paper_sheet(layout, sheet_def)
            self._add_title_block(layout, sheet_def)
            self._add_viewport(layout, sheet_def)
        
        # Write to bytes
        buffer = io.BytesIO()
        self.doc.saveas(buffer)
        return buffer.getvalue()
    
    def _draw_floor_plan(self, msp, level: dict):
        """Draw one floor plan in model space."""
        level_id = level["id"]
        offset_y = self._level_offset(level_id)  # Offset each floor vertically
        
        # Walls
        for wall in self._walls_at_level(level_id):
            layer = self._wall_layer(wall)
            start = self._offset(wall["start"], offset_y)
            end = self._offset(wall["end"], offset_y)
            
            if wall["assembly"]["total_thickness_m"] > 0:
                # Draw as polyline with thickness (hatched for cut walls)
                self._draw_wall_poché(msp, wall, start, end, layer)
            else:
                msp.add_line(start, end, dxfattribs={"layer": layer})
        
        # Openings
        for opening in self._openings_at_level(level_id):
            self._draw_opening_plan(msp, opening, offset_y)
        
        # Room tags
        for room in self._rooms_at_level(level_id):
            centroid = self._room_centroid(room, offset_y)
            self._draw_room_tag(msp, room, centroid)
        
        # Fixtures
        for fixture in self._fixtures_at_level(level_id):
            self._draw_fixture(msp, fixture, offset_y)
        
        # Stairs
        for stair in self._stairs_at_level(level_id):
            self._draw_stair_plan(msp, stair, offset_y)
        
        # Dimensions
        self._draw_dimension_chains(msp, level_id, offset_y)
        
        # Grid lines
        if self.geometry.get("grids"):
            self._draw_grids(msp, level_id, offset_y)
    
    def _draw_elevations(self, msp):
        """Draw 4 elevations in model space."""
        faces = ["south", "north", "east", "west"]
        for i, face in enumerate(faces):
            offset_x = i * (self.config.elevation_spacing_m + 20)
            self._draw_single_elevation(msp, face, offset_x)
    
    def _draw_sections(self, msp):
        """Draw sections in model space."""
        for section in self.geometry["markers"]["sections"]:
            self._draw_single_section(msp, section)
    
    def _get_sheet_definitions(self) -> list:
        """Define paper space sheets."""
        sheets = [
            {"name": "A0-COVER", "type": "cover", "scale": None},
            {"name": "A1-SITE", "type": "site", "scale": "1:200"},
        ]
        for level in self.geometry["levels"]:
            if level["type"] == "floor":
                sheets.append({
                    "name": f"A2-{level['name'].upper().replace(' ','')}",
                    "type": "floor_plan",
                    "scale": "1:100",
                    "level": level["id"]
                })
        sheets.extend([
            {"name": "A4-ELEVATIONS", "type": "elevation", "scale": "1:100"},
            {"name": "A5-SECTIONS", "type": "section", "scale": "1:100"},
            {"name": "A6-SCHEDULES", "type": "schedule", "scale": None},
        ])
        return sheets
```

### 4.4 DXF Output Structure

```
Output file: {project_name}_v{version}_{revision}.dxf

Model Space:
  - All floor plans at 1:1 (offset vertically)
  - All elevations at 1:1 (offset horizontally)
  - All sections at 1:1
  - Site plan at 1:1

Paper Space Layouts:
  A0-COVER:      Cover sheet with project info
  A1-SITE:       Site plan viewport (1:200)
  A2-TANG1:      Floor plan Level 1 viewport (1:100)
  A2-TANG2:      Floor plan Level 2 viewport (1:100)
  A2-TANG3:      Floor plan Level 3 viewport (1:100)
  A2-TANG4:      Floor plan Level 4 viewport (1:100)
  A4-ELEVATIONS: 4 elevations viewport (1:100)
  A5-SECTIONS:   2 sections viewport (1:100)
  A6-SCHEDULES:  Door + Window + Room schedule tables

Each layout has:
  - Title block (xref or block)
  - Viewport(s) into model space at correct scale
  - Layer visibility control per viewport
```

---

## 5. Schedules

### 5.1 Door Schedule

```
+------+--------+-----------+----------+--------+--------+----------+--------+--------+
| Mark | Room   | Type      | Size WxH | Frame  | Panel  | Hardware | Fire   | Notes  |
+------+--------+-----------+----------+--------+--------+----------+--------+--------+
| D01  | r1     | Entrance  | 1200x2400| Alum.  | Glass  | Lever+MP | -      | Double |
|      | Living | Double    |          | Grey   | Temper.|          |        | leaf   |
+------+--------+-----------+----------+--------+--------+----------+--------+--------+
| D02  | r1-r2  | Interior  | 900x2100 | Wood   | Wood   | Lever    | -      | Single |
|      | Living | Single    |          | Oak    | Panel  |          |        | swing  |
|      | -Kitchn|           |          |        |        |          |        |        |
+------+--------+-----------+----------+--------+--------+----------+--------+--------+
| D03  | r3     | Bathroom  | 700x2100 | Alum.  | Alum.  | Privacy  | -      | Single |
|      | WC     | Single    |          | White  | Panel  | lock     |        |        |
+------+--------+-----------+----------+--------+--------+----------+--------+--------+
```

**Data source:** `geometry.openings` where `type == "door"`

**Columns:**
| Column | Source field | Required |
|--------|------------|----------|
| Mark | `schedule_mark` | Yes |
| Room | `room_id` -> room.name | Yes |
| Type | `subtype` | Yes |
| Size WxH | `width_m` x `height_m` (mm) | Yes |
| Frame Material | `frame.material` | Yes |
| Panel Material | `panel.material` | Yes |
| Hardware | `hardware.handle` + `hardware.lock` | Yes |
| Fire Rating | `fire_rating` | If applicable |
| Notes | `panel.leaves`, `panel.swing_direction` | Optional |

### 5.2 Window Schedule

```
+------+--------+-----------+----------+--------+-----------+-----------+--------+--------+
| Mark | Room   | Type      | Size WxH | Sill   | Frame     | Glazing   | U-val  | Notes  |
+------+--------+-----------+----------+--------+-----------+-----------+--------+--------+
| W01  | r1     | Fixed+    | 1000x1500| 900    | Alum.     | Dbl Low-E | 1.1    | Casem. |
|      | Living | Casement  |          |        | Grey Slim | 24mm      |        | Left   |
+------+--------+-----------+----------+--------+-----------+-----------+--------+--------+
| W02  | r2     | Sliding   | 1500x1500| 900    | Alum.     | Dbl Low-E | 1.1    | 2-trk  |
|      | Kitchen|           |          |        | Grey Slim | 24mm      |        |        |
+------+--------+-----------+----------+--------+-----------+-----------+--------+--------+
```

**Data source:** `geometry.openings` where `type == "window"`

**Columns:**
| Column | Source field | Required |
|--------|------------|----------|
| Mark | `schedule_mark` | Yes |
| Room | `room_id` -> room.name | Yes |
| Type | `subtype` | Yes |
| Size WxH | `width_m` x `height_m` (mm) | Yes |
| Sill Height | `sill_height_m` (mm) | Yes |
| Frame | `frame.material`, `frame.color`, `frame.profile` | Yes |
| Glazing | `glazing.type`, `glazing.thickness_mm` | Yes |
| U-value | `glazing.u_value` | Phase 2+ |
| Notes | `operation.type`, `operation.hinge_side` | Optional |

### 5.3 Room / Area Schedule

```
+------+--------------+-------+------+--------+--------+---------+--------+---------+
| ID   | Room Name    | Level | Area | Height | Floor  | Wall    | Ceiling | Notes   |
|      |              |       | (m2) | (m)    | Finish | Finish  | Finish  |         |
+------+--------------+-------+------+--------+--------+---------+--------+---------+
| r1   | Phong khach  | L1    | 20.2 | 2.80   | Porce. | Paint   | Paint   | 6 plugs |
| r2   | Bep          | L1    | 12.9 | 2.80   | Porce. | Tile    | Paint   | Gas     |
| r3   | WC Tang 1    | L1    | 3.5  | 2.80   | Porce. | Tile    | Paint   | Wet     |
+------+--------------+-------+------+--------+--------+---------+--------+---------+
| LEVEL L1 TOTAL:            | 80.0 |        |        |         |         |         |
+----------------------------+------+--------+--------+---------+---------+---------+
| r4   | Phong ngu 1  | L2    | 16.0 | 2.70   | Wood   | Paint   | Paint   | Master  |
| r5   | Phong ngu 2  | L2    | 12.0 | 2.70   | Wood   | Paint   | Paint   |         |
+------+--------------+-------+------+--------+--------+---------+--------+---------+
| LEVEL L2 TOTAL:            | 80.0 |        |        |         |         |         |
+----------------------------+------+--------+--------+---------+---------+---------+
| BUILDING TOTAL:            |320.0 |        |        |         |         |         |
+----------------------------+------+--------+--------+---------+---------+---------+
```

**Data source:** `geometry.rooms`

### 5.4 Schedule Renderer

```python
class ScheduleRenderer:
    """Generate schedule tables as SVG or for PDF/DXF embedding."""
    
    def render_door_schedule(self, geometry: dict) -> SVGTable:
        doors = [o for o in geometry["openings"] if o["type"] == "door"]
        doors.sort(key=lambda d: d["schedule_mark"])
        
        columns = [
            TableColumn("Mark", width=40),
            TableColumn("Room", width=80),
            TableColumn("Type", width=80),
            TableColumn("Size WxH", width=80),
            TableColumn("Frame", width=70),
            TableColumn("Panel", width=70),
            TableColumn("Hardware", width=70),
            TableColumn("Fire", width=40),
            TableColumn("Notes", width=100),
        ]
        
        rows = []
        for door in doors:
            room = self._find_room(geometry["rooms"], door)
            rows.append(DoorScheduleRow(door, room))
        
        return SVGTable(columns=columns, rows=rows, title="DOOR SCHEDULE")
    
    def render_window_schedule(self, geometry: dict) -> SVGTable:
        windows = [o for o in geometry["openings"] if o["type"] == "window"]
        windows.sort(key=lambda w: w["schedule_mark"])
        # ... similar pattern
    
    def render_room_schedule(self, geometry: dict) -> SVGTable:
        rooms = geometry["rooms"]
        rooms_by_level = groupby(rooms, key=lambda r: r["level"])
        # ... with level subtotals and building total
```

---

## 6. Enhanced Dimensioning

### 6.1 Dimension Chain Types

| Type | Mo ta | Vi du |
|------|-------|-------|
| **Overall** | Tong kich thuoc ngoai cung | 5000 (chieu rong nha) |
| **Grid-to-grid** | Khoang cach giua cac truc | A-B: 2500, B-C: 2500 |
| **Wall-to-wall** | Khoang cach giua cac tuong | Phong khach: 4600 |
| **Opening** | Vi tri va kich thuoc cua | D01: 1200 wide @ 1500 from axis A |
| **Room** | Kich thuoc phong | 4600 x 4400 |
| **Vertical** | Cao do cac tang | +0.45, +4.05, +7.35, +10.65, +13.65 |
| **Stair** | Riser/tread | 20R x 165 = 3300 |

### 6.2 Dimension Placement Rules

```python
class DimensionEngine:
    """Auto-place dimension chains following architectural conventions."""
    
    # Spacing rules (mm at drawing scale)
    FIRST_CHAIN_OFFSET = 10    # mm from building edge
    CHAIN_SPACING = 7          # mm between chains
    TEXT_HEIGHT = 2.5           # mm
    
    def generate_plan_dimensions(self, geometry: dict, level_id: str) -> list[DimensionChain]:
        chains = []
        
        # Chain 1 (outermost): Overall building dimensions
        chains.append(self._overall_dims(geometry, level_id))
        
        # Chain 2: Grid-to-grid (if grids exist)
        if geometry.get("grids"):
            chains.append(self._grid_dims(geometry))
        
        # Chain 3: Wall-to-wall (exterior to first interior, etc.)
        chains.append(self._wall_to_wall_dims(geometry, level_id))
        
        # Chain 4 (innermost): Opening positions and widths
        chains.append(self._opening_dims(geometry, level_id))
        
        # Internal room dimensions (placed inside rooms)
        chains.extend(self._room_internal_dims(geometry, level_id))
        
        return chains
    
    def generate_elevation_dimensions(self, geometry: dict, face: str) -> list[DimensionChain]:
        chains = []
        
        # Vertical: floor-to-floor heights
        chains.append(self._level_dims(geometry))
        
        # Vertical: total building height
        chains.append(self._total_height_dim(geometry))
        
        # Horizontal: opening positions
        chains.append(self._elevation_opening_dims(geometry, face))
        
        # Vertical: sill heights, head heights
        chains.append(self._opening_height_dims(geometry, face))
        
        return chains
```

### 6.3 Dimension Chain Rendering

```
PLAN DIMENSION EXAMPLE (looking at south face):

                    5000
    |<--------------------------------->|
         2500              2500
    |<-------------->|<---------------->|
     500  1200  800   500  1000  500
    |<->|<---->|<-->|<-->|<----->|<--->|
    +===+======+====+====+=======+====+
    |   | D01  |    |    | W01   |    |    <- openings
    +===+======+====+====+=======+====+
    A                B                C    <- grid axes
```

---

## 7. IFC Export Foundation

### 7.1 Scope Phase 2

Phase 2 chi lam IFC **foundation** - du de mo file trong BIM viewer, chua du cho full BIM coordination.

| Feature | Phase 2 | Phase 3+ |
|---------|---------|----------|
| IfcWall | Basic geometry + type | + assembly layers, materials |
| IfcDoor | Position + size | + operation, hardware sets |
| IfcWindow | Position + size | + glazing properties |
| IfcSpace (room) | Boundary + name + area | + finish properties |
| IfcSlab | Per level | + edge conditions |
| IfcStairFlight | Basic | + detailed geometry |
| IfcSite | Boundary | + topography |
| IfcBuildingStorey | Elevation + name | + containment hierarchy |
| Property Sets | Basic | + full Pset coverage |
| Quantity Sets | Area, length | + detailed quantities |

### 7.2 Tech stack

```python
# pip install ifcopenshell
import ifcopenshell
import ifcopenshell.api

class IFCExporter:
    """Export geometry Layer 2 to IFC 4x3."""
    
    def __init__(self, geometry: dict):
        self.geometry = geometry
        self.model = ifcopenshell.api.run("project.create_file", version="IFC4X3")
        self._setup_project()
    
    def _setup_project(self):
        project = ifcopenshell.api.run("root.create_entity", self.model, ifc_class="IfcProject")
        project.Name = self.geometry["project_info"]["name"]
        
        # Units: metric
        ifcopenshell.api.run("unit.assign_unit", self.model, length={"is_metric": True, "raw": "METRE"})
        
        # Site
        site = ifcopenshell.api.run("root.create_entity", self.model, ifc_class="IfcSite")
        
        # Building
        building = ifcopenshell.api.run("root.create_entity", self.model, ifc_class="IfcBuilding")
        ifcopenshell.api.run("aggregate.assign_object", self.model, relating_object=site, product=building)
        
        self.building = building
    
    def export(self) -> bytes:
        # Create storeys
        for level in self.geometry["levels"]:
            if level["type"] == "floor":
                self._create_storey(level)
        
        # Create walls
        for wall in self.geometry["walls"]:
            self._create_wall(wall)
        
        # Create openings
        for opening in self.geometry["openings"]:
            self._create_opening(opening)
        
        # Create spaces (rooms)
        for room in self.geometry["rooms"]:
            self._create_space(room)
        
        buffer = io.BytesIO()
        self.model.write(buffer)
        return buffer.getvalue()
```

---

## 8. Full Sheet Set Phase 2

### 8.1 Sheet set mo rong

```
Phase 2 target: 8-12 sheets (tu 4-6 cua MVP+)

  A0:  Cover / Issue Sheet
  A1:  Site / Plot Plan
  A2:  Floor Plan - Tang 1 (1:100)
  A3:  Floor Plan - Tang 2 (1:100)
  A4:  Floor Plan - Tang 3 (1:100)
  A5:  Floor Plan - Tang 4 / Tang thuong (1:100)
  A6:  Elevation South + North (1:100)
  A7:  Elevation East + West (1:100)
  A8:  Section A-A + Section B-B (1:100)
  A9:  Door Schedule + Window Schedule
  A10: Room / Area Schedule + Area Summary
  A11: General Notes + Legend + Abbreviations (optional)
```

### 8.2 Export output Phase 2

```
Per version export:
  1. Combined PDF (8-12 pages, professional sheets)
  2. Per-sheet SVG (native vector)
  3. Per-sheet PNG preview (for gallery/thumbnail)
  4. DXF file (full model + paper space layouts)
  5. IFC file (basic BIM)
  6. Package manifest JSON (updated schema)
  7. Schedule data CSV (door, window, room - for spreadsheet use)
```

---

## 9. Database Changes Phase 2

### 9.1 geometry_json migration

```sql
-- Migration: upgrade geometry_json from Layer 1.5 to Layer 2
-- This is a DATA migration, not schema migration
-- geometry_json column is already JSONB, just richer content

-- Add validation function
CREATE OR REPLACE FUNCTION validate_geometry_v2(geom JSONB)
RETURNS BOOLEAN AS $$
BEGIN
    -- Check required Layer 2 fields
    RETURN (
        geom ? '$schema' AND
        geom->>'$schema' = 'ai-architect-geometry-v2' AND
        geom ? 'grids' AND
        geom ? 'levels' AND
        geom ? 'walls' AND
        geom ? 'openings' AND
        geom ? 'rooms' AND
        jsonb_array_length(geom->'walls') > 0 AND
        -- Check wall assemblies exist
        (geom->'walls'->0) ? 'assembly'
    );
END;
$$ LANGUAGE plpgsql;
```

### 9.2 Export packages upgrade

```sql
-- Add DXF and IFC support to export_packages
ALTER TABLE export_packages 
    ADD COLUMN dxf_url TEXT,
    ADD COLUMN ifc_url TEXT,
    ADD COLUMN schedule_csv_urls JSONB;  -- {"door": "url", "window": "url", "room": "url"}
```

---

## 10. Implementation Checkpoints Phase 2

### CP-P2-1: Geometry Layer 2 (Week 1-4)

| # | Task | Priority | DoD |
|---|------|----------|-----|
| 1 | Design + validate Layer 2 schema | P0 | JSON Schema + 3 sample files |
| 2 | Canonicalization pipeline upgrade (image -> Layer 2) | P0 | AI extracts wall assemblies, opening details, room finishes |
| 3 | geometry_json migration strategy (L1.5 -> L2) | P0 | Backward compatible, old projects still work |
| 4 | Geometry validation API | P0 | validate_geometry_v2() passes for all test cases |
| 5 | Structural grid system | P1 | Grid axes render on plan |

### CP-P2-2: 4 Elevations + Enhanced Dimensions (Week 5-8)

| # | Task | Priority | DoD |
|---|------|----------|-----|
| 1 | ElevationRendererV2 (4 faces) | P0 | 4 SVG elevations from geometry |
| 2 | Material tags on elevations | P0 | Exterior finish labels visible |
| 3 | Grid overlay on elevations | P0 | Structural axes shown |
| 4 | Enhanced DimensionEngine (full chains) | P0 | 4 chain types: overall, grid, wall, opening |
| 5 | 2nd section (Section B-B) | P1 | Perpendicular to S1 |
| 6 | Schedule mark tags on plans + elevations | P0 | D01, W01 visible and consistent |

### CP-P2-3: Schedules (Week 9-10)

| # | Task | Priority | DoD |
|---|------|----------|-----|
| 1 | DoorScheduleRenderer | P0 | SVG table + PDF integration |
| 2 | WindowScheduleRenderer | P0 | SVG table + PDF integration |
| 3 | RoomScheduleRenderer | P0 | SVG table with level subtotals + building total |
| 4 | Schedule sheet(s) in PDF package | P0 | A9, A10 sheets added |
| 5 | Schedule CSV export | P1 | door.csv, window.csv, room.csv |

### CP-P2-4: DXF Export (Week 11-14)

| # | Task | Priority | DoD |
|---|------|----------|-----|
| 1 | ezdxf integration + layer setup | P0 | 25+ layers created correctly |
| 2 | Floor plan DXF (walls, openings, fixtures) | P0 | Opens in AutoCAD/LibreCAD correctly |
| 3 | Elevation DXF (4 faces) | P0 | Correct geometry in model space |
| 4 | Section DXF | P0 | Cut vs beyond correctly differentiated |
| 5 | Paper space layouts with viewports | P0 | Each sheet as named layout at correct scale |
| 6 | Title block as block/xref | P0 | Reusable across layouts |
| 7 | Dimension DXF (proper dimstyle) | P0 | Dimensions editable in CAD |
| 8 | Schedule tables in DXF | P1 | Tables or text blocks |
| 9 | DXF validation (open in 3 CAD tools) | P0 | AutoCAD, LibreCAD, DraftSight pass |

### CP-P2-5: IFC Foundation (Week 15-16)

| # | Task | Priority | DoD |
|---|------|----------|-----|
| 1 | IfcOpenShell integration | P0 | IFC4X3 file created |
| 2 | IfcWall + IfcDoor + IfcWindow export | P0 | Geometry correct in BIM viewer |
| 3 | IfcSpace (rooms) export | P0 | Room boundaries + properties |
| 4 | IfcBuildingStorey hierarchy | P0 | Correct containment |
| 5 | Basic property sets | P1 | Name, area, type for each element |
| 6 | IFC validation (IFC checker) | P0 | No critical errors |

### CP-P2-6: Integration + QA (Week 17-18)

| # | Task | Priority | DoD |
|---|------|----------|-----|
| 1 | Full package export (PDF + SVG + DXF + IFC + CSV) | P0 | All formats from one button |
| 2 | Package manifest v2 (include DXF, IFC, CSV refs) | P0 | JSON manifest covers all files |
| 3 | Export progress UI upgrade | P0 | Shows per-format progress |
| 4 | Regression testing (Layer 1.5 projects still work) | P0 | Old projects export correctly |
| 5 | Performance testing (4-floor house < 30s total export) | P0 | All formats generated within budget |
| 6 | KTS/architect user testing | P0 | 3 architects confirm DXF usable |

---

## 11. Acceptance Criteria Phase 2 Deliverable

### Package-level
- [ ] PDF package has 8-12 sheets
- [ ] DXF file opens correctly in AutoCAD, LibreCAD, DraftSight
- [ ] IFC file opens in BIM viewer (Solibri, BIMvision, xBIM)
- [ ] All formats derive from same canonical geometry (no inconsistency)
- [ ] Package manifest JSON covers all exported files

### Elevation
- [ ] 4 exterior elevations (S, N, E, W)
- [ ] Each elevation shows: openings, roof line, grade line, floor levels
- [ ] Material tags visible on each elevation
- [ ] Grid lines overlaid
- [ ] Vertical dimensions (floor-to-floor + total height)
- [ ] Schedule marks (D01, W01) visible on elevations

### DXF
- [ ] 25+ layers correctly named and colored
- [ ] Model space: all drawings at 1:1
- [ ] Paper space: named layouts for each sheet
- [ ] Viewports at correct scale (1:100, 1:200)
- [ ] Title blocks present on each layout
- [ ] Dimensions use proper dimstyle (editable in CAD)
- [ ] Text uses defined text styles (not random fonts)
- [ ] Wall hatching/poché correct for cut walls
- [ ] Opening swings drawn correctly

### Schedules
- [ ] Door schedule: all doors listed with mark, room, type, size, frame, panel, hardware
- [ ] Window schedule: all windows with mark, room, type, size, sill, frame, glazing, U-value
- [ ] Room schedule: all rooms per level with area, height, finishes, subtotals
- [ ] Schedule marks on plan/elevation match schedule tables exactly
- [ ] CSV export available for spreadsheet use

### Dimensions
- [ ] Overall building dimensions on all plan sheets
- [ ] Grid-to-grid dimensions (if grid exists)
- [ ] Wall-to-wall major dimensions
- [ ] Opening position + width dimensions
- [ ] Room internal dimensions
- [ ] Elevation vertical dimensions (levels + total)
- [ ] Stair dimensions (riser x count = rise)

---

## 12. Risks va Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Canonicalization pipeline khong extract du chi tiet cho Layer 2 | DXF/IFC output thieu element | Cho phep KTS manually edit geometry JSON qua UI form |
| DXF khong tuong thich het cac CAD tools | KTS khong mo duoc file | Test voi 3+ CAD tools, chon R2018 format (widely supported) |
| IFC export co errors | Khong mo duoc trong BIM viewer | Dung IfcOpenShell validation + buildingSMART IFC checker |
| Schedule data khong day du | Schedule tables thieu thong tin | Default values cho cac field chua co, mark "TBD" |
| Performance: export qua cham voi nha 4 tang | User cho lau | Background job + progress bar, target < 30s |
| Backward compatibility: old Layer 1.5 projects bi loi | User mat du lieu | Migration script L1.5 -> L2 voi default values |
