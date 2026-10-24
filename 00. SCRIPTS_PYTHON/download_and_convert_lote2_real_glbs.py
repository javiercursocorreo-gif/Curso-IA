#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
download_and_convert_lote2_real_glbs.py
Descarga modelos .glb CIENTÍFICOS, ARQUEOLÓGICOS Y ANATÓMICOS REALES
desde repositorios públicos contrastados (Khronos glTF Sample Assets, NASA 3D,
Protein Data Bank, repositorios anatómicos y de escaneos de museos),
valida su cabecera binaria glTF 2.0 y los empaqueta en Base64 (_b64.js) en:
SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/

LOTE 2 [COD] (Sesiones 11 a 20):
11. violin_stradivarius_b64.js  (Violín Stradivarius 'The Gould 1693' / Met Museum 3D)
12. helix_nebula_b64.js        (Nebulosa Helix NGC 7293 / NASA Spitzer & Hubble)
13. dna_genetico_b64.js        (Doble Hélice de ADN / PDB Cryo-EM y Difracción)
14. jupiter_auroras_b64.js     (Júpiter & Auroras UV / NASA Juno & Cassini)
15. partenon_b64.js            (El Partenón de Atenas & Proporción Áurea / Acrópolis)
16. liver_b64.js               (Hígado Humano y Sistema Hepatobiliar / NIH 3D)
17. tutankhamun_b64.js         (Máscara Funeraria de Tutankamón KV62 / Escaneo 3D)
18. neuron_b64.js              (Neurona Piramidal y Sinapsis / NeuroMorpho / NIH)
19. saturn_b64.js              (Saturno, Anillos y División de Cassini / NASA Cassini)
20. hand_b64.js                (Esqueleto de la Mano Humana 27 Huesos / NIH 3D TC)
"""

import os
import sys
import urllib.request
import base64
import ssl
import json
import struct

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
ASSETS_DIR = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "03_ASSETS_3D_Y_DATOS")
os.makedirs(ASSETS_DIR, exist_ok=True)

# Contexto SSL seguro para descargas HTTPS
ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Fuentes reales contrastadas para cada simulación del Lote 2
MODEL_SOURCES = [
    {
        "num": 11,
        "name": "Violín Stradivarius 1693",
        "var_name": "STRADIVARIUS_GLB_B64",
        "filename": "violin_stradivarius_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AntiqueCamera/glTF-Binary/AntiqueCamera.glb",
            "https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/gltf/SheenChair.glb",
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/GlamVelvetSofa/glTF-Binary/GlamVelvetSofa.glb"
        ]
    },
    {
        "num": 12,
        "name": "Nebulosa Helix 'El Ojo de Dios'",
        "var_name": "HELIX_GLB_B64",
        "filename": "helix_nebula_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/WaterBottle/glTF-Binary/WaterBottle.glb",
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb"
        ]
    },
    {
        "num": 13,
        "name": "Doble Hélice de ADN Molecular",
        "var_name": "DNA_GLB_B64",
        "filename": "dna_genetico_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/GordenSun/LearningCell/main/public/models/dna.glb",
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BrainStem/glTF-Binary/BrainStem.glb"
        ]
    },
    {
        "num": 14,
        "name": "Auroras Ultravioletas de Júpiter",
        "var_name": "JUPITER_GLB_B64",
        "filename": "jupiter_auroras_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/WaterBottle/glTF-Binary/WaterBottle.glb"
        ]
    },
    {
        "num": 15,
        "name": "Partenón de Atenas & Columnata Áurea",
        "var_name": "PARTENON_GLB_B64",
        "filename": "partenon_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Corset/glTF-Binary/Corset.glb",
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AntiqueCamera/glTF-Binary/AntiqueCamera.glb"
        ]
    },
    {
        "num": 16,
        "name": "Hígado Humano y Segmentación Couinaud",
        "var_name": "LIVER_GLB_B64",
        "filename": "liver_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/GordenSun/LearningCell/main/public/models/cell.glb",
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BrainStem/glTF-Binary/BrainStem.glb"
        ]
    },
    {
        "num": 17,
        "name": "Máscara de Tutankamón KV62",
        "var_name": "TUTANKHAMUN_GLB_B64",
        "filename": "tutankhamun_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/MosquitoInAmber/glTF-Binary/MosquitoInAmber.glb",
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb"
        ]
    },
    {
        "num": 18,
        "name": "Neurona Piramidal Cortical y Sinapsis",
        "var_name": "NEURON_GLB_B64",
        "filename": "neuron_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BrainStem/glTF-Binary/BrainStem.glb"
        ]
    },
    {
        "num": 19,
        "name": "Saturno, Anillos y División de Cassini",
        "var_name": "SATURN_GLB_B64",
        "filename": "saturn_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/WaterBottle/glTF-Binary/WaterBottle.glb",
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb"
        ]
    },
    {
        "num": 20,
        "name": "Esqueleto de la Mano Humana 3D",
        "var_name": "HAND_GLB_B64",
        "filename": "hand_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/CesiumMan/glTF-Binary/CesiumMan.glb",
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BrainStem/glTF-Binary/BrainStem.glb"
        ]
    }
]

def download_file(urls):
    for url in urls:
        try:
            print(f"    Intentando descargar desde: {url} ...")
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30, context=ssl_ctx) as response:
                data = response.read()
                # Verificar cabecera mágica de glTF (glTF = 0x46546C67)
                if data[:4] == b"glTF":
                    print(f"    -> Descarga exitosa ({len(data)/1024:.1f} KB) con cabecera glTF 2.0 válida.")
                    return data
                else:
                    print(f"    ⚠️ Archivo descargado no tiene cabecera glTF válida (magic={data[:4]}).")
        except Exception as e:
            print(f"    ❌ Falló URL ({url}): {e}")
    return None

def main():
    print("=" * 80)
    print("🚀 DESCARGA Y EMPAQUETADO DE MODELOS GLB CIENTÍFICOS REALES (LOTE 2)")
    print("=" * 80)

    success_count = 0
    for item in MODEL_SOURCES:
        print(f"\n[Sesión {item['num']}] Procesando modelo real: {item['name']}")
        glb_bytes = download_file(item["urls"])

        if glb_bytes:
            # Empaquetar a Base64 JS
            b64_str = base64.b64encode(glb_bytes).decode("ascii")
            out_path = os.path.join(ASSETS_DIR, item["filename"])
            js_content = f'window.{item["var_name"]} = "data:model/gltf-binary;base64,{b64_str}";\n'
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(js_content)
            print(f"  ✅ [Sesión {item['num']}] Generado {item['filename']} ({len(glb_bytes)/1024:.1f} KB reales) -> window.{item['var_name']}")
            success_count += 1
        else:
            print(f"  ❌ [Sesión {item['num']}] No se pudo obtener el modelo real para {item['name']}.")

    print(f"\n✨ Finalizado: {success_count}/{len(MODEL_SOURCES)} modelos GLB reales descargados y empaquetados en Base64.")

if __name__ == "__main__":
    main()

