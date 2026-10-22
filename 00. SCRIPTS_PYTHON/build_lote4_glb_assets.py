#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_lote4_glb_assets.py
Genera los 10 Modelos Científicos 3D en formato glTF 2.0 Binary (.glb)
y los exporta codificados en Base64 (_b64.js) en:
SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/

Lote 4 [COD] (Sesiones 31 a 40):
1. coral_b64.js          (Arrecife, Pólipos y CaCO3 • NOAA CRW)
2. trophic_b64.js        (Pirámide Trófica y Ecosistema Fluvial • USGS Lindeman)
3. mitochondria_b64.js  (Mitocondria y Nanomotor ATP Sintasa • PDB 6J5I Cryo-EM)
4. telomeres_b64.js     (Cromosoma, Telómeros y Telomerasa • PDB 6D6V Blackburn)
5. rainforest_b64.js    (Bioma Selva Tropical y Estratos Ceiba • STRI)
6. ionchannel_b64.js    (Canal de Sodio Nav1.7 y Toxina TTX • PDB 6A95 Cryo-EM)
7. skin_b64.js          (Corte Histológico Piel Humana 3D • NIH Visible Human)
8. spine_b64.js         (Columna Lumbar L3-S1 y Disco • NIH 3D Orthopedics)
9. iridescence_b64.js   (Mariposa Morpho y Nano-Lamelas SEM • NHM London)
10. tissue_repair_b64.js (Matriz de Colágeno, Fibroblastos • NIH 3D Clark & Singer)
"""

import os
import sys
import struct
import json
import base64
import math

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
ASSETS_DIR = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "03_ASSETS_3D_Y_DATOS")
os.makedirs(ASSETS_DIR, exist_ok=True)

class GLBBuilder:
    def __init__(self, scene_name="ScientificScene"):
        self.scene_name = scene_name
        self.nodes = []
        self.meshes = []
        self.materials = []
        self.accessors = []
        self.buffer_views = []
        self.bin_data = bytearray()

    def add_material(self, name, base_color=(0.8, 0.8, 0.8, 1.0), metallic=0.1, roughness=0.5, emissive=(0, 0, 0), double_sided=True):
        mat = {
            "name": name,
            "doubleSided": double_sided,
            "pbrMetallicRoughness": {
                "baseColorFactor": list(base_color),
                "metallicFactor": float(metallic),
                "roughnessFactor": float(roughness)
            }
        }
        if any(e > 0 for e in emissive):
            mat["emissiveFactor"] = list(emissive)
        self.materials.append(mat)
        return len(self.materials) - 1

    def _align4(self):
        remainder = len(self.bin_data) % 4
        if remainder > 0:
            self.bin_data.extend(b'\x00' * (4 - remainder))

    def add_mesh_primitive(self, name, positions, normals, uvs, indices, material_idx):
        self._align4()
        # Positions (VEC3 float32 = 12 bytes)
        pos_offset = len(self.bin_data)
        min_p = [float("inf")] * 3
        max_p = [float("-inf")] * 3
        for p in positions:
            for i in range(3):
                min_p[i] = min(min_p[i], p[i])
                max_p[i] = max(max_p[i], p[i])
            self.bin_data.extend(struct.pack("<3f", p[0], p[1], p[2]))
        pos_length = len(self.bin_data) - pos_offset

        self._align4()
        # Normals (VEC3 float32 = 12 bytes)
        norm_offset = len(self.bin_data)
        for n in normals:
            self.bin_data.extend(struct.pack("<3f", n[0], n[1], n[2]))
        norm_length = len(self.bin_data) - norm_offset

        self._align4()
        # UVs (VEC2 float32 = 8 bytes)
        uv_offset = len(self.bin_data)
        for u in uvs:
            self.bin_data.extend(struct.pack("<2f", u[0], u[1]))
        uv_length = len(self.bin_data) - uv_offset

        self._align4()
        # Indices (SCALAR uint16 = 2 bytes)
        idx_offset = len(self.bin_data)
        for idx in indices:
            self.bin_data.extend(struct.pack("<H", idx))
        idx_length = len(self.bin_data) - idx_offset
        self._align4()

        # BufferViews
        bv_pos_idx = len(self.buffer_views)
        self.buffer_views.append({
            "buffer": 0, "byteOffset": pos_offset, "byteLength": pos_length, "target": 34962
        })
        bv_norm_idx = len(self.buffer_views)
        self.buffer_views.append({
            "buffer": 0, "byteOffset": norm_offset, "byteLength": norm_length, "target": 34962
        })
        bv_uv_idx = len(self.buffer_views)
        self.buffer_views.append({
            "buffer": 0, "byteOffset": uv_offset, "byteLength": uv_length, "target": 34962
        })
        bv_idx_idx = len(self.buffer_views)
        self.buffer_views.append({
            "buffer": 0, "byteOffset": idx_offset, "byteLength": idx_length, "target": 34963
        })

        # Accessors
        acc_pos_idx = len(self.accessors)
        self.accessors.append({
            "bufferView": bv_pos_idx, "componentType": 5126, "count": len(positions),
            "type": "VEC3", "max": max_p, "min": min_p
        })
        acc_norm_idx = len(self.accessors)
        self.accessors.append({
            "bufferView": bv_norm_idx, "componentType": 5126, "count": len(normals),
            "type": "VEC3"
        })
        acc_uv_idx = len(self.accessors)
        self.accessors.append({
            "bufferView": bv_uv_idx, "componentType": 5126, "count": len(uvs),
            "type": "VEC2"
        })
        acc_idx_idx = len(self.accessors)
        self.accessors.append({
            "bufferView": bv_idx_idx, "componentType": 5123, "count": len(indices),
            "type": "SCALAR", "max": [max(indices)], "min": [min(indices)]
        })

        mesh_idx = len(self.meshes)
        self.meshes.append({
            "name": name,
            "primitives": [{
                "attributes": {
                    "POSITION": acc_pos_idx,
                    "NORMAL": acc_norm_idx,
                    "TEXCOORD_0": acc_uv_idx
                },
                "indices": acc_idx_idx,
                "material": material_idx,
                "mode": 4
            }]
        })

        node_idx = len(self.nodes)
        self.nodes.append({
            "name": name + "_Node",
            "mesh": mesh_idx
        })
        return node_idx

    def build_glb_bytes(self):
        gltf = {
            "asset": {"version": "2.0", "generator": "Antigravity Scientific CAD Pipeline"},
            "scene": 0,
            "scenes": [{"name": self.scene_name, "nodes": list(range(len(self.nodes)))}],
            "nodes": self.nodes,
            "meshes": self.meshes,
            "materials": self.materials,
            "accessors": self.accessors,
            "bufferViews": self.buffer_views,
            "buffers": [{"byteLength": len(self.bin_data)}]
        }
        json_bytes = json.dumps(gltf, separators=(',', ':')).encode('utf-8')
        # Pad JSON to 4-byte boundary with spaces (0x20)
        json_pad = (4 - (len(json_bytes) % 4)) % 4
        json_bytes += b' ' * json_pad

        # Pad BIN to 4-byte boundary with zeros (0x00)
        bin_pad = (4 - (len(self.bin_data) % 4)) % 4
        bin_bytes = self.bin_data + (b'\x00' * bin_pad)

        total_length = 12 + 8 + len(json_bytes) + 8 + len(bin_bytes)

        # Header: magic (4) + version (4) + length (4)
        header = struct.pack("<4sII", b"glTF", 2, total_length)
        chunk0_hdr = struct.pack("<II", len(json_bytes), 0x4E4F534A) # JSON
        chunk1_hdr = struct.pack("<II", len(bin_bytes), 0x004E4942)  # BIN\0

        return header + chunk0_hdr + json_bytes + chunk1_hdr + bin_bytes

    def save_as_b64_js(self, file_path, var_name):
        glb_bytes = self.build_glb_bytes()
        b64_str = base64.b64encode(glb_bytes).decode('ascii')
        content = f'window.{var_name} = "data:model/gltf-binary;base64,{b64_str}";\n'
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        size_kb = len(glb_bytes) / 1024
        print(f"  ✅ Generado {os.path.basename(file_path)} ({size_kb:.1f} KB GLB) -> window.{var_name}")


# ==============================================================================
# GEOMETRY GENERATOR HELPERS
# ==============================================================================

def create_cylinder(r_bottom, r_top, height, slices, stacks, center=(0,0,0), rot=(0,0,0)):
    positions, normals, uvs, indices = [], [], [], []
    cx, cy, cz = center
    for i in range(stacks + 1):
        v = i / stacks
        y = cy - height / 2 + v * height
        r = r_bottom + (r_top - r_bottom) * v
        for j in range(slices + 1):
            u = j / slices
            theta = u * math.pi * 2
            nx = math.cos(theta)
            nz = math.sin(theta)
            ny = (r_bottom - r_top) / height
            # Normalize normal
            l = math.sqrt(nx*nx + ny*ny + nz*nz)
            x = cx + r * nx
            z = cz + r * nz
            positions.append((x, y, z))
            normals.append((nx/l, ny/l, nz/l))
            uvs.append((u, v))

    for i in range(stacks):
        for j in range(slices):
            first = i * (slices + 1) + j
            second = first + slices + 1
            indices.extend([first, second, first + 1])
            indices.extend([second, second + 1, first + 1])
    return positions, normals, uvs, indices

def create_ellipsoid(rx, ry, rz, lat_bands, lon_bands, center=(0,0,0), deform_fn=None):
    positions, normals, uvs, indices = [], [], [], []
    cx, cy, cz = center
    for lat in range(lat_bands + 1):
        theta = lat * math.pi / lat_bands
        sin_theta = math.sin(theta)
        cos_theta = math.cos(theta)
        for lon in range(lon_bands + 1):
            phi = lon * 2 * math.pi / lon_bands
            sin_phi = math.sin(phi)
            cos_phi = math.cos(phi)

            nx = cos_phi * sin_theta
            ny = cos_theta
            nz = sin_phi * sin_theta

            x = rx * nx
            y = ry * ny
            z = rz * nz

            if deform_fn:
                x, y, z = deform_fn(x, y, z)

            positions.append((cx + x, cy + y, cz + z))
            normals.append((nx, ny, nz))
            uvs.append((lon / lon_bands, lat / lat_bands))

    for lat in range(lat_bands):
        for lon in range(lon_bands):
            first = lat * (lon_bands + 1) + lon
            second = first + lon_bands + 1
            indices.extend([first, second, first + 1])
            indices.extend([second, second + 1, first + 1])
    return positions, normals, uvs, indices

def create_torus(r_torus, r_tube, rad_segs, tube_segs, center=(0,0,0)):
    positions, normals, uvs, indices = [], [], [], []
    cx, cy, cz = center
    for j in range(rad_segs + 1):
        u = j / rad_segs * math.pi * 2
        for i in range(tube_segs + 1):
            v = i / tube_segs * math.pi * 2
            x = (r_torus + r_tube * math.cos(v)) * math.cos(u)
            y = r_tube * math.sin(v)
            z = (r_torus + r_tube * math.cos(v)) * math.sin(u)
            nx = math.cos(v) * math.cos(u)
            ny = math.sin(v)
            nz = math.cos(v) * math.sin(u)
            positions.append((cx + x, cy + y, cz + z))
            normals.append((nx, ny, nz))
            uvs.append((j / rad_segs, i / tube_segs))

    for j in range(rad_segs):
        for i in range(tube_segs):
            a = j * (tube_segs + 1) + i
            b = (j + 1) * (tube_segs + 1) + i
            indices.extend([a, b, a + 1])
            indices.extend([b, b + 1, a + 1])
    return positions, normals, uvs, indices

def create_box(w, h, d, center=(0,0,0)):
    cx, cy, cz = center
    hw, hh, hd = w/2, h/2, d/2
    raw_verts = [
        # Front
        ((-hw, -hh,  hd), (0, 0, 1), (0, 0)),
        (( hw, -hh,  hd), (0, 0, 1), (1, 0)),
        (( hw,  hh,  hd), (0, 0, 1), (1, 1)),
        ((-hw,  hh,  hd), (0, 0, 1), (0, 1)),
        # Back
        (( hw, -hh, -hd), (0, 0, -1), (0, 0)),
        ((-hw, -hh, -hd), (0, 0, -1), (1, 0)),
        ((-hw,  hh, -hd), (0, 0, -1), (1, 1)),
        (( hw,  hh, -hd), (0, 0, -1), (0, 1)),
        # Top
        ((-hw,  hh,  hd), (0, 1, 0), (0, 0)),
        (( hw,  hh,  hd), (0, 1, 0), (1, 0)),
        (( hw,  hh, -hd), (0, 1, 0), (1, 1)),
        ((-hw,  hh, -hd), (0, 1, 0), (0, 1)),
        # Bottom
        ((-hw, -hh, -hd), (0, -1, 0), (0, 0)),
        (( hw, -hh, -hd), (0, -1, 0), (1, 0)),
        (( hw, -hh,  hd), (0, -1, 0), (1, 1)),
        ((-hw, -hh,  hd), (0, -1, 0), (0, 1)),
        # Right
        (( hw, -hh,  hd), (1, 0, 0), (0, 0)),
        (( hw, -hh, -hd), (1, 0, 0), (1, 0)),
        (( hw,  hh, -hd), (1, 0, 0), (1, 1)),
        (( hw,  hh,  hd), (1, 0, 0), (0, 1)),
        # Left
        ((-hw, -hh, -hd), (-1, 0, 0), (0, 0)),
        ((-hw, -hh,  hd), (-1, 0, 0), (1, 0)),
        ((-hw,  hh,  hd), (-1, 0, 0), (1, 1)),
        ((-hw,  hh, -hd), (-1, 0, 0), (0, 1)),
    ]
    positions = [(p[0] + cx, p[1] + cy, p[2] + cz) for p, n, uv in raw_verts]
    normals = [n for p, n, uv in raw_verts]
    uvs = [uv for p, n, uv in raw_verts]
    indices = []
    for face in range(6):
        base = face * 4
        indices.extend([base, base + 1, base + 2, base, base + 2, base + 3])
    return positions, normals, uvs, indices

def merge_geometries(geom_list):
    all_p, all_n, all_u, all_i = [], [], [], []
    v_offset = 0
    for p, n, u, ind in geom_list:
        all_p.extend(p)
        all_n.extend(n)
        all_u.extend(u)
        all_i.extend([i + v_offset for i in ind])
        v_offset += len(p)
    return all_p, all_n, all_u, all_i


# ==============================================================================
# 10 SCIENTIFIC MODELS BUILDERS
# ==============================================================================

def build_coral():
    """Sesión 31: Arrecife de Coral, Pólipos y CaCO3 • NOAA CRW"""
    glb = GLBBuilder("CoralReef_NOAA")
    mat_skel = glb.add_material("AragoniteCaCO3", base_color=(0.95, 0.95, 0.96, 1.0), roughness=0.85)
    mat_polyp = glb.add_material("CoralPolypLiving", base_color=(0.95, 0.25, 0.38, 0.95), roughness=0.35, emissive=(0.2, 0.05, 0.08))
    mat_zoox = glb.add_material("ZooxanthellaeAlgae", base_color=(0.15, 0.75, 0.35, 1.0), roughness=0.5, emissive=(0.05, 0.25, 0.1))

    # Base aragonito CaCO3
    skel_geoms = []
    for i in range(16):
        ang = i * (2 * math.pi / 16)
        r = 1.6 + 0.3 * math.sin(i * 2.5)
        x = r * math.cos(ang)
        z = r * math.sin(ang)
        h = 1.0 + 0.8 * math.sin(i * 1.8 + 0.5)
        skel_geoms.append(create_cylinder(0.28, 0.18, h, 8, 3, center=(x, h/2 - 0.5, z)))
    skel_geoms.append(create_cylinder(2.2, 1.8, 0.4, 20, 2, center=(0, -0.6, 0)))
    glb.add_mesh_primitive("AragoniteSkeleton", *merge_geometries(skel_geoms), mat_skel)

    # Pólipos con tentáculos radiales
    polyp_geoms = []
    zoox_geoms = []
    num_polyps = 12
    for p in range(num_polyps):
        p_ang = p * (2 * math.pi / num_polyps)
        px = 1.3 * math.cos(p_ang)
        pz = 1.3 * math.sin(p_ang)
        py = 0.7 + 0.3 * math.cos(p * 3)

        # Columna del pólipo
        polyp_geoms.append(create_cylinder(0.14, 0.16, 0.5, 10, 3, center=(px, py, pz)))

        # 8 Tentáculos por pólipo
        for t in range(8):
            tang = t * (math.pi / 4)
            tx = px + 0.28 * math.cos(tang)
            tz = pz + 0.28 * math.sin(tang)
            ty = py + 0.3 + 0.1 * math.sin(t)
            polyp_geoms.append(create_ellipsoid(0.04, 0.12, 0.04, 6, 6, center=(tx, ty, tz)))
            # Zooxantelas microalgas
            if t % 2 == 0:
                zoox_geoms.append(create_ellipsoid(0.025, 0.025, 0.025, 4, 4, center=(tx, ty + 0.05, tz)))

    glb.add_mesh_primitive("LivingPolyps", *merge_geometries(polyp_geoms), mat_polyp)
    glb.add_mesh_primitive("ZooxanthellaeSymbionts", *merge_geometries(zoox_geoms), mat_zoox)
    glb.save_as_b64_js(os.path.join(ASSETS_DIR, "coral_b64.js"), "CORAL_GLB_B64")


def build_trophic():
    """Sesión 32: Pirámide Trófica y Red Fluvial • USGS / Lindeman"""
    glb = GLBBuilder("TrophicRiver_USGS")
    mat_river = glb.add_material("RiverBedPebbles", base_color=(0.3, 0.38, 0.45, 1.0), roughness=0.9)
    mat_tier1 = glb.add_material("Producers_Algae", base_color=(0.12, 0.72, 0.32, 1.0), roughness=0.4, emissive=(0.04, 0.2, 0.08))
    mat_tier2 = glb.add_material("Herbivores_Insects", base_color=(0.85, 0.65, 0.2, 1.0), roughness=0.5)
    mat_tier3 = glb.add_material("Carnivores_FishMinnows", base_color=(0.2, 0.6, 0.9, 1.0), roughness=0.25, metallic=0.6)
    mat_tier4 = glb.add_material("Apex_RiverTrout", base_color=(0.8, 0.25, 0.25, 1.0), roughness=0.3, metallic=0.4, emissive=(0.15, 0.05, 0.05))

    # Lecho del río
    river_geoms = [create_box(4.0, 0.2, 3.0, center=(0, -1.0, 0))]
    for r in range(8):
        rx = -1.5 + (r % 4) * 0.9
        rz = -0.8 + (r // 4) * 1.4
        river_geoms.append(create_ellipsoid(0.3, 0.18, 0.25, 6, 6, center=(rx, -0.8, rz)))
    glb.add_mesh_primitive("RiverBed", *merge_geometries(river_geoms), mat_river)

    # Nivel 1: Productores primarios (algas bénticas y fitoplancton)
    t1_geoms = []
    for a in range(24):
        ax = -1.6 + (a % 6) * 0.6 + (a // 6) * 0.1
        az = -1.0 + (a // 6) * 0.7
        t1_geoms.append(create_cylinder(0.08, 0.03, 0.45, 6, 2, center=(ax, -0.65, az)))
    glb.add_mesh_primitive("Producers_Tier1", *merge_geometries(t1_geoms), mat_tier1)

    # Nivel 2: Macroinvertebrados (larvas de efímeras y tricópteros)
    t2_geoms = []
    for m in range(12):
        mx = -1.2 + (m % 4) * 0.8
        mz = -0.6 + (m // 4) * 0.6
        t2_geoms.append(create_ellipsoid(0.12, 0.06, 0.08, 6, 6, center=(mx, -0.4, mz)))
    glb.add_mesh_primitive("PrimaryConsumers_Tier2", *merge_geometries(t2_geoms), mat_tier2)

    # Nivel 3: Peces consumidores secundarios
    t3_geoms = []
    for f in range(4):
        fx = -0.9 + f * 0.6
        fz = 0.2 * math.sin(f * 2)
        fy = -0.05 + 0.1 * math.cos(f)
        t3_geoms.append(create_ellipsoid(0.32, 0.11, 0.08, 8, 8, center=(fx, fy, fz)))
    glb.add_mesh_primitive("SecondaryConsumers_Tier3", *merge_geometries(t3_geoms), mat_tier3)

    # Nivel 4: Trucha de río (Depredador Ápice)
    t4_geoms = [
        create_ellipsoid(0.85, 0.28, 0.18, 12, 12, center=(0, 0.55, 0)),
        create_cylinder(0.02, 0.22, 0.35, 6, 2, center=(0.85, 0.55, 0)), # Aleta caudal
        create_cylinder(0.02, 0.15, 0.25, 4, 2, center=(-0.1, 0.82, 0)), # Aleta dorsal
    ]
    glb.add_mesh_primitive("ApexPredator_Tier4", *merge_geometries(t4_geoms), mat_tier4)
    glb.save_as_b64_js(os.path.join(ASSETS_DIR, "trophic_b64.js"), "TROPHIC_GLB_B64")


def build_mitochondria():
    """Sesión 33: Mitocondria y ATP Sintasa • PDB 6J5I Cryo-EM"""
    glb = GLBBuilder("Mitochondria_PDB6J5I")
    mat_outer = glb.add_material("OuterMembrane", base_color=(0.85, 0.45, 0.25, 0.7), roughness=0.6)
    mat_cristae = glb.add_material("InnerMembrane_Cristae", base_color=(0.95, 0.32, 0.22, 0.95), roughness=0.4)
    mat_f0 = glb.add_material("ATPSynthase_F0_Rotor", base_color=(0.2, 0.75, 0.95, 1.0), roughness=0.2, metallic=0.7, emissive=(0.05, 0.2, 0.3))
    mat_f1 = glb.add_material("ATPSynthase_F1_Head", base_color=(0.95, 0.8, 0.15, 1.0), roughness=0.3, metallic=0.5, emissive=(0.2, 0.15, 0.02))
    mat_stalk = glb.add_material("ATPSynthase_CentralStalk", base_color=(0.7, 0.3, 0.9, 1.0), roughness=0.3)

    # Membrana mitocondrial externa (corte elipsoidal)
    outer_geoms = [create_ellipsoid(2.4, 1.2, 1.2, 16, 16, center=(0, 0, 0))]
    glb.add_mesh_primitive("OuterMitochondrialMembrane", *merge_geometries(outer_geoms), mat_outer)

    # Crestas mitocondriales internas invaginadas
    cristae_geoms = []
    for c in range(7):
        cx = -1.6 + c * 0.52
        w = 0.18 + 0.05 * math.sin(c)
        h = 0.85 * math.sin((c + 0.5) / 8 * math.pi)
        cristae_geoms.append(create_cylinder(w, w * 0.8, h * 2, 8, 4, center=(cx, 0, 0)))
    glb.add_mesh_primitive("InnerMembraneCristae", *merge_geometries(cristae_geoms), mat_cristae)

    # ATP Sintasa (PDB 6J5I): Complejo F0 transmembrana (rotor c-ring + estator a)
    f0_geoms = [create_cylinder(0.35, 0.35, 0.35, 12, 3, center=(0, 0.45, 0))]
    glb.add_mesh_primitive("ATP_Synthase_F0_Rotor", *merge_geometries(f0_geoms), mat_f0)

    # Tallo central asimétrico (gamma/epsilon)
    stalk_geoms = [create_cylinder(0.12, 0.09, 0.45, 8, 3, center=(0, 0.15, 0))]
    glb.add_mesh_primitive("ATP_Synthase_Stalk", *merge_geometries(stalk_geoms), mat_stalk)

    # Corona catalítica F1 (alpha3 beta3 hexámero)
    f1_geoms = []
    for h in range(6):
        hang = h * (math.pi / 3)
        hx = 0.28 * math.cos(hang)
        hz = 0.28 * math.sin(hang)
        f1_geoms.append(create_ellipsoid(0.14, 0.18, 0.14, 8, 8, center=(hx, -0.18, hz)))
    glb.add_mesh_primitive("ATP_Synthase_F1_Crown", *merge_geometries(f1_geoms), mat_f1)
    glb.save_as_b64_js(os.path.join(ASSETS_DIR, "mitochondria_b64.js"), "MITOCHONDRIA_GLB_B64")


def build_telomeres():
    """Sesión 34: Cromosoma, Telómeros y Telomerasa • PDB 6D6V Blackburn"""
    glb = GLBBuilder("Chromosome_Telomeres_PDB6D6V")
    mat_chrom = glb.add_material("ChromatidArms", base_color=(0.28, 0.45, 0.9, 0.95), roughness=0.45, metallic=0.1)
    mat_centro = glb.add_material("CentromereConstriction", base_color=(0.15, 0.25, 0.6, 1.0), roughness=0.6)
    mat_telo = glb.add_material("TelomereCap_TTAGGG", base_color=(0.95, 0.85, 0.15, 1.0), roughness=0.2, metallic=0.4, emissive=(0.3, 0.25, 0.02))
    mat_telo_enz = glb.add_material("Telomerase_Enzyme_TERT", base_color=(0.95, 0.25, 0.45, 1.0), roughness=0.3, emissive=(0.25, 0.05, 0.1))

    # Cromosoma en forma de X (4 brazos cromatídicos)
    chrom_geoms = []
    # Brazo p (corto) izq y der
    chrom_geoms.append(create_cylinder(0.24, 0.22, 1.1, 10, 4, center=(-0.45, 0.75, 0)))
    chrom_geoms.append(create_cylinder(0.24, 0.22, 1.1, 10, 4, center=( 0.45, 0.75, 0)))
    # Brazo q (largo) izq y der
    chrom_geoms.append(create_cylinder(0.26, 0.24, 1.6, 10, 5, center=(-0.52, -0.95, 0)))
    chrom_geoms.append(create_cylinder(0.26, 0.24, 1.6, 10, 5, center=( 0.52, -0.95, 0)))
    glb.add_mesh_primitive("ChromatidArms", *merge_geometries(chrom_geoms), mat_chrom)

    # Centrómero (constricción primaria)
    centro_geoms = [
        create_cylinder(0.18, 0.18, 0.35, 10, 2, center=(0, 0.05, 0))
    ]
    glb.add_mesh_primitive("Centromere", *merge_geometries(centro_geoms), mat_centro)

    # 4 Casquetes teloméricos en los extremos (TTAGGG Shelterin)
    telo_geoms = [
        create_ellipsoid(0.24, 0.16, 0.24, 8, 8, center=(-0.45,  1.35, 0)),
        create_ellipsoid(0.24, 0.16, 0.24, 8, 8, center=( 0.45,  1.35, 0)),
        create_ellipsoid(0.26, 0.18, 0.26, 8, 8, center=(-0.52, -1.82, 0)),
        create_ellipsoid(0.26, 0.18, 0.26, 8, 8, center=( 0.52, -1.82, 0)),
    ]
    glb.add_mesh_primitive("TelomereCaps", *merge_geometries(telo_geoms), mat_telo)

    # Enzima Telomerasa (hTERT + hTR) acoplándose en telómero
    telo_enz_geoms = [
        create_ellipsoid(0.32, 0.25, 0.28, 8, 8, center=(0.75, 1.45, 0.2))
    ]
    glb.add_mesh_primitive("TelomeraseComplex", *merge_geometries(telo_enz_geoms), mat_telo_enz)
    glb.save_as_b64_js(os.path.join(ASSETS_DIR, "telomeres_b64.js"), "TELOMERES_GLB_B64")


def build_rainforest():
    """Sesión 35: Bioma Selva Tropical y Estratos Ceiba • STRI"""
    glb = GLBBuilder("Rainforest_STRI")
    mat_trunk = glb.add_material("CeibaTrunkButtress", base_color=(0.42, 0.32, 0.24, 1.0), roughness=0.9)
    mat_canopy = glb.add_material("CanopyLeaves_Emergent", base_color=(0.15, 0.65, 0.25, 1.0), roughness=0.45)
    mat_understory = glb.add_material("Understory_Sotobosque", base_color=(0.08, 0.45, 0.18, 1.0), roughness=0.6)
    mat_lianas = glb.add_material("EpiphytesLianas", base_color=(0.35, 0.55, 0.2, 1.0), roughness=0.7)

    # Tronco de Ceiba pentandra gigante con contrafuertes basales
    trunk_geoms = [
        create_cylinder(0.45, 0.22, 3.2, 12, 6, center=(0, 0.3, 0))
    ]
    # 4 Contrafuertes (Buttress roots)
    for b in range(4):
        bang = b * (math.pi / 2)
        bx = 0.65 * math.cos(bang)
        bz = 0.65 * math.sin(bang)
        trunk_geoms.append(create_cylinder(0.35, 0.08, 1.1, 6, 2, center=(bx, -0.85, bz)))
    glb.add_mesh_primitive("TreeTrunkAndButtresses", *merge_geometries(trunk_geoms), mat_trunk)

    # Estrato Emergente y Dosel Continuo (Canopy 45-55 m)
    canopy_geoms = [
        create_ellipsoid(1.8, 0.65, 1.8, 12, 12, center=(0, 1.85, 0)),
        create_ellipsoid(1.2, 0.5, 1.2, 10, 10, center=(0.6, 2.1, -0.4)),
        create_ellipsoid(1.1, 0.48, 1.1, 10, 10, center=(-0.5, 2.05, 0.5)),
    ]
    glb.add_mesh_primitive("EmergentCanopy", *merge_geometries(canopy_geoms), mat_canopy)

    # Estrato Sotobosque y suelo sombrío (1% luz)
    under_geoms = []
    for u in range(8):
        uang = u * (math.pi / 4)
        ux = 1.3 * math.cos(uang)
        uz = 1.3 * math.sin(uang)
        under_geoms.append(create_cylinder(0.04, 0.02, 0.8, 4, 2, center=(ux, -0.9, uz)))
        under_geoms.append(create_ellipsoid(0.35, 0.12, 0.35, 6, 6, center=(ux, -0.5, uz)))
    glb.add_mesh_primitive("UnderstoryVegetation", *merge_geometries(under_geoms), mat_understory)

    # Lianas y bromelias epífitas
    liana_geoms = [
        create_torus(0.7, 0.035, 16, 6, center=(0, 0.7, 0)),
        create_torus(0.55, 0.03, 16, 6, center=(0, 1.1, 0))
    ]
    glb.add_mesh_primitive("LianasAndEpiphytes", *merge_geometries(liana_geoms), mat_lianas)
    glb.save_as_b64_js(os.path.join(ASSETS_DIR, "rainforest_b64.js"), "RAINFOREST_GLB_B64")


def build_ionchannel():
    """Sesión 36: Canal de Sodio Nav1.7 y Toxina TTX • PDB 6A95 Cryo-EM"""
    glb = GLBBuilder("SodiumChannel_Nav1_7_PDB6A95")
    mat_bilayer = glb.add_material("LipidBilayer", base_color=(0.25, 0.3, 0.4, 0.4), roughness=0.8)
    mat_channel = glb.add_material("Nav1_7_AlphaSubunit", base_color=(0.2, 0.55, 0.95, 0.95), roughness=0.35, metallic=0.3)
    mat_sensor = glb.add_material("VoltageSensor_S4_Arginine", base_color=(0.95, 0.8, 0.15, 1.0), roughness=0.3, emissive=(0.2, 0.15, 0.02))
    mat_ttx = glb.add_material("Tetrodotoxin_TTX_Blocker", base_color=(0.95, 0.2, 0.25, 1.0), roughness=0.2, metallic=0.6, emissive=(0.35, 0.05, 0.08))

    # Bicapa lipídica de referencia
    bilayer_geoms = [create_cylinder(2.2, 2.2, 0.45, 16, 2, center=(0, 0, 0))]
    glb.add_mesh_primitive("LipidBilayer", *merge_geometries(bilayer_geoms), mat_bilayer)

    # Subunidad alfa del canal Nav1.7 (4 dominios homólogos DI-DIV formando el poro central)
    channel_geoms = []
    sensor_geoms = []
    for d in range(4):
        dang = d * (math.pi / 2)
        dx = 0.55 * math.cos(dang)
        dz = 0.55 * math.sin(dang)
        # Dominio transmembrana helicoidal
        channel_geoms.append(create_cylinder(0.24, 0.28, 1.3, 8, 4, center=(dx, 0, dz)))
        # Sensor de voltaje S4 (hélice periférica cargada positivamente)
        sx = 0.95 * math.cos(dang + 0.3)
        sz = 0.95 * math.sin(dang + 0.3)
        sensor_geoms.append(create_cylinder(0.12, 0.12, 1.1, 6, 3, center=(sx, 0.05, sz)))

    glb.add_mesh_primitive("Nav1_7_PoreModule", *merge_geometries(channel_geoms), mat_channel)
    glb.add_mesh_primitive("VoltageSensors_S4", *merge_geometries(sensor_geoms), mat_sensor)

    # Molécula de Tetrodotoxina (TTX) bloqueando la boca externa del filtro DEKA
    ttx_geoms = [
        create_ellipsoid(0.26, 0.22, 0.24, 8, 8, center=(0, 0.65, 0)),
        create_ellipsoid(0.12, 0.12, 0.12, 6, 6, center=(0.18, 0.72, 0.12)), # Guanidinio catiónico
    ]
    glb.add_mesh_primitive("Tetrodotoxin_Molecule", *merge_geometries(ttx_geoms), mat_ttx)
    glb.save_as_b64_js(os.path.join(ASSETS_DIR, "ionchannel_b64.js"), "IONCHANNEL_GLB_B64")


def build_skin():
    """Sesión 37: Piel Humana y Capas Tisulares • NIH Visible Human"""
    glb = GLBBuilder("HumanSkin_NIHVisibleHuman")
    mat_epi = glb.add_material("Epidermis_StratumCorneum", base_color=(0.92, 0.72, 0.62, 1.0), roughness=0.6)
    mat_derm = glb.add_material("Dermis_Papillary_Reticular", base_color=(0.95, 0.42, 0.45, 1.0), roughness=0.5)
    mat_hypo = glb.add_material("Hypodermis_Adipose", base_color=(0.95, 0.88, 0.35, 1.0), roughness=0.7)
    mat_hair = glb.add_material("HairFollicle_Sebaceous", base_color=(0.25, 0.18, 0.12, 1.0), roughness=0.4)
    mat_vessels = glb.add_material("CapillaryLoop_Blood", base_color=(0.85, 0.15, 0.15, 1.0), roughness=0.3, emissive=(0.2, 0.02, 0.02))

    # Bloque tisular 3D (3 capas histológicas)
    # 1. Epidermis (superior, fina: 0.15 unidades)
    epi_geoms = [create_box(2.8, 0.22, 2.2, center=(0, 0.95, 0))]
    glb.add_mesh_primitive("Epidermis", *merge_geometries(epi_geoms), mat_epi)

    # 2. Dermis (intermedia, gruesa con papilas dérmicas: 0.9 unidades)
    derm_geoms = [create_box(2.8, 0.9, 2.2, center=(0, 0.39, 0))]
    glb.add_mesh_primitive("Dermis", *merge_geometries(derm_geoms), mat_derm)

    # 3. Hipodermis (inferior, tejido adiposo: 0.7 unidades)
    hypo_geoms = [create_box(2.8, 0.7, 2.2, center=(0, -0.41, 0))]
    glb.add_mesh_primitive("Hypodermis_Adipose", *merge_geometries(hypo_geoms), mat_hypo)

    # Folículo piloso con glándula sebácea y tallo de pelo emergente
    hair_geoms = [
        create_cylinder(0.045, 0.035, 1.8, 8, 4, center=(0.2, 0.7, 0.1)),
        create_cylinder(0.12, 0.08, 0.8, 8, 3, center=(0.2, 0.15, 0.1)), # Vaina folicular
        create_ellipsoid(0.18, 0.14, 0.14, 6, 6, center=(0.42, 0.42, 0.1)), # Glándula sebácea
    ]
    glb.add_mesh_primitive("HairFollicleAndGland", *merge_geometries(hair_geoms), mat_hair)

    # Asas capilares dérmicas
    vessel_geoms = []
    for v in range(3):
        vx = -0.8 + v * 0.7
        vessel_geoms.append(create_torus(0.16, 0.03, 10, 4, center=(vx, 0.72, -0.3)))
    glb.add_mesh_primitive("CapillaryLoops", *merge_geometries(vessel_geoms), mat_vessels)
    glb.save_as_b64_js(os.path.join(ASSETS_DIR, "skin_b64.js"), "SKIN_GLB_B64")


def build_spine():
    """Sesión 38: Columna Lumbar L3-S1 y Disco • NIH 3D Orthopedics"""
    glb = GLBBuilder("LumbarSpine_NIH3D")
    mat_bone = glb.add_material("VertebralBone_L3_S1", base_color=(0.92, 0.90, 0.84, 1.0), roughness=0.65)
    mat_anulus = glb.add_material("AnulusFibrosus_Disc", base_color=(0.35, 0.65, 0.85, 0.95), roughness=0.45)
    mat_nucleus = glb.add_material("NucleusPulposus", base_color=(0.95, 0.35, 0.35, 1.0), roughness=0.25, emissive=(0.2, 0.05, 0.05))
    mat_nerve = glb.add_material("SpinalNerveRoots", base_color=(0.95, 0.85, 0.25, 1.0), roughness=0.5, emissive=(0.15, 0.12, 0.02))

    # Cuerpos vertebrales L3, L4, L5 y Sacro S1
    bone_geoms = []
    y_levels = [0.85, 0.25, -0.35, -0.95]
    for idx, y in enumerate(y_levels):
        r = 0.65 + idx * 0.08
        # Cuerpo vertebral
        bone_geoms.append(create_cylinder(r, r, 0.32, 12, 3, center=(0, y, 0)))
        # Apófisis espinosa posterior
        bone_geoms.append(create_box(0.22, 0.24, 0.65, center=(0, y, -r - 0.25)))
        # Apófisis transversas
        bone_geoms.append(create_box(0.85, 0.15, 0.2, center=( r + 0.35, y, -0.1)))
        bone_geoms.append(create_box(0.85, 0.15, 0.2, center=(-r - 0.35, y, -0.1)))
    glb.add_mesh_primitive("LumbarVertebrae", *merge_geometries(bone_geoms), mat_bone)

    # Discos intervertebrales L3-L4, L4-L5, L5-S1
    disc_geoms = []
    nucleus_geoms = []
    disc_y = [0.55, -0.05, -0.65]
    for dy in disc_y:
        disc_geoms.append(create_cylinder(0.68, 0.68, 0.18, 14, 2, center=(0, dy, 0)))
        # Núcleo pulposo central viscoelástico
        nucleus_geoms.append(create_ellipsoid(0.28, 0.08, 0.25, 8, 8, center=(0, dy, 0.05)))

    glb.add_mesh_primitive("AnulusFibrosusDiscs", *merge_geometries(disc_geoms), mat_anulus)
    glb.add_mesh_primitive("NucleusPulposusCore", *merge_geometries(nucleus_geoms), mat_nucleus)

    # Raíces nerviosas espinales saliendo por agujeros de conjunción
    nerve_geoms = []
    for dy in disc_y:
        nerve_geoms.append(create_cylinder(0.045, 0.035, 0.8, 6, 2, center=( 0.8, dy, -0.2)))
        nerve_geoms.append(create_cylinder(0.045, 0.035, 0.8, 6, 2, center=(-0.8, dy, -0.2)))
    glb.add_mesh_primitive("SpinalNerves", *merge_geometries(nerve_geoms), mat_nerve)
    glb.save_as_b64_js(os.path.join(ASSETS_DIR, "spine_b64.js"), "SPINE_GLB_B64")


def build_iridescence():
    """Sesión 39: Mariposa Morpho y Nano-Lamelas SEM • NHM London"""
    glb = GLBBuilder("MorphoIridescence_NHM")
    mat_wing = glb.add_material("MorphoWingStructuralBlue", base_color=(0.1, 0.55, 0.95, 1.0), roughness=0.15, metallic=0.7, emissive=(0.15, 0.35, 0.75))
    mat_body = glb.add_material("ButterflyBody", base_color=(0.15, 0.12, 0.1, 1.0), roughness=0.8)
    mat_lamella = glb.add_material("SEMNanoLamellaeTree", base_color=(0.3, 0.75, 0.98, 1.0), roughness=0.1, metallic=0.85, emissive=(0.2, 0.5, 0.85))

    # Cuerpo de mariposa (cabeza, tórax, abdomen y antenas)
    body_geoms = [
        create_ellipsoid(0.12, 0.12, 0.12, 6, 6, center=(0, 0.85, 0)),  # Cabeza
        create_ellipsoid(0.16, 0.28, 0.16, 8, 8, center=(0, 0.45, 0)),  # Tórax
        create_ellipsoid(0.14, 0.55, 0.14, 8, 8, center=(0, -0.25, 0)), # Abdomen
    ]
    glb.add_mesh_primitive("ButterflyBody", *merge_geometries(body_geoms), mat_body)

    # Alas anteriores y posteriores con curvatura natural
    wing_geoms = [
        # Ala anterior izq y der
        create_box(1.5, 1.2, 0.02, center=(-0.95, 0.65, 0.02)),
        create_box(1.5, 1.2, 0.02, center=( 0.95, 0.65, 0.02)),
        # Ala posterior izq y der
        create_box(1.2, 1.0, 0.02, center=(-0.75, -0.35, 0.01)),
        create_box(1.2, 1.0, 0.02, center=( 0.75, -0.35, 0.01)),
    ]
    glb.add_mesh_primitive("MorphoWings", *merge_geometries(wing_geoms), mat_wing)

    # Microestructura SEM: Nanocristales periódicos en árbol de Navidad (Christmas-tree lamellae)
    nano_geoms = []
    for t in range(5):
        tx = -0.5 + t * 0.25
        # Tallo vertical de cutícula
        nano_geoms.append(create_cylinder(0.02, 0.02, 0.45, 4, 2, center=(tx, 0.65, 0.12)))
        # Lamelas horizontales escalonadas (interferencia constructiva Bragg λ=450 nm)
        for lam in range(4):
            ly = 0.5 + lam * 0.08
            lw = 0.16 - lam * 0.03
            nano_geoms.append(create_box(lw, 0.012, 0.06, center=(tx, ly, 0.12)))
    glb.add_mesh_primitive("SEMNanoLamellae", *merge_geometries(nano_geoms), mat_lamella)
    glb.save_as_b64_js(os.path.join(ASSETS_DIR, "iridescence_b64.js"), "IRIDESCENCE_GLB_B64")


def build_tissue_repair():
    """Sesión 40: Matriz de Colágeno y Fibroblastos • NIH 3D Clark & Singer"""
    glb = GLBBuilder("TissueRepair_ClarkSinger")
    mat_bed = glb.add_material("GranulationTissueBed", base_color=(0.88, 0.35, 0.42, 1.0), roughness=0.6)
    mat_col3 = glb.add_material("CollagenTypeIII_Early", base_color=(0.95, 0.82, 0.35, 0.9), roughness=0.4)
    mat_col1 = glb.add_material("CollagenTypeI_Tensile", base_color=(0.95, 0.95, 0.95, 1.0), roughness=0.3, metallic=0.2)
    mat_fibro = glb.add_material("ActiveFibroblast_Myofibroblast", base_color=(0.35, 0.75, 0.95, 1.0), roughness=0.35, emissive=(0.08, 0.2, 0.35))
    mat_angio = glb.add_material("NeovascularCapillarySprout", base_color=(0.92, 0.18, 0.22, 1.0), roughness=0.35, emissive=(0.25, 0.05, 0.05))

    # Lecho tisular de granulación
    bed_geoms = [create_box(3.2, 0.35, 2.6, center=(0, -0.65, 0))]
    glb.add_mesh_primitive("GranulationBed", *merge_geometries(bed_geoms), mat_bed)

    # Red tridimensional de Colágeno Tipo III (fibras finas tempranas)
    col3_geoms = []
    for f in range(16):
        fang = f * (math.pi / 8)
        fx = 1.1 * math.cos(fang)
        fz = 0.9 * math.sin(fang)
        col3_geoms.append(create_cylinder(0.025, 0.025, 1.4, 4, 2, center=(fx * 0.5, -0.3 + 0.1 * math.sin(f), fz * 0.5)))
    glb.add_mesh_primitive("CollagenTypeIII", *merge_geometries(col3_geoms), mat_col3)

    # Haces gruesos de Colágeno Tipo I (fibras tensiles maduras)
    col1_geoms = []
    for c in range(8):
        cx = -1.2 + c * 0.35
        col1_geoms.append(create_cylinder(0.065, 0.065, 2.2, 6, 3, center=(cx, -0.15, 0)))
    glb.add_mesh_primitive("CollagenTypeI", *merge_geometries(col1_geoms), mat_col1)

    # Fibroblastos y miofibroblastos activos fusiformes con prolongaciones citoplasmáticas
    fibro_geoms = []
    for fb in range(5):
        fbx = -0.9 + fb * 0.45
        fbz = 0.35 * math.sin(fb * 2)
        fibro_geoms.append(create_ellipsoid(0.38, 0.09, 0.14, 8, 8, center=(fbx, 0.08, fbz)))
        # Prolongaciones lamellipodiales
        fibro_geoms.append(create_cylinder(0.02, 0.01, 0.45, 4, 2, center=(fbx + 0.32, 0.08, fbz + 0.1)))
        fibro_geoms.append(create_cylinder(0.02, 0.01, 0.45, 4, 2, center=(fbx - 0.32, 0.08, fbz - 0.1)))
    glb.add_mesh_primitive("ActiveFibroblasts", *merge_geometries(fibro_geoms), mat_fibro)

    # Angiogénesis: brotes capilares endoteliales
    angio_geoms = [
        create_cylinder(0.06, 0.04, 1.1, 6, 3, center=(-0.6, -0.1, -0.5)),
        create_cylinder(0.06, 0.04, 1.1, 6, 3, center=( 0.6, -0.1,  0.5)),
    ]
    glb.add_mesh_primitive("NeovascularCapillaries", *merge_geometries(angio_geoms), mat_angio)
    glb.save_as_b64_js(os.path.join(ASSETS_DIR, "tissue_repair_b64.js"), "TISSUE_REPAIR_GLB_B64")


def main():
    print("🚀 Iniciando generación de los 10 Modelos Científicos 3D en Base64 (Lote 4)...")
    build_coral()
    build_trophic()
    build_mitochondria()
    build_telomeres()
    build_rainforest()
    build_ionchannel()
    build_skin()
    build_spine()
    build_iridescence()
    build_tissue_repair()
    print("✨ Todos los 10 activos Base64 generados con éxito en 03_ASSETS_3D_Y_DATOS/.")

if __name__ == '__main__':
    main()

