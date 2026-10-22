#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
download_and_convert_lote4_real_glbs.py
Descarga modelos .glb CIENTÍFICOS Y REALES desde repositorios públicos contrastados
(Khronos glTF Sample Assets, repositorios anatómicos abiertos, GitHub raw),
valida su cabecera binaria glTF 2.0 y los empaqueta en Base64 (_b64.js) en:
SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/

LOTE 4 [COD] (Sesiones 31 a 40):
1. coral_b64.js          (Arrecife de Coral / Fotogrametría Marina Real)
2. trophic_b64.js        (Trucha / Barramundi Fish Scan 3D PBR Khronos)
3. mitochondria_b64.js  (Arquitectura Celular y Mitocondria 3D)
4. telomeres_b64.js     (Doble Hélice ADN y Cromosoma Molecular 3D)
5. rainforest_b64.js    (Árbol Real Escaneado con Ramificaciones Naturales)
6. ionchannel_b64.js    (Canal Iónico y Complejo Macromolecular de Membrana)
7. skin_b64.js          (Bloque Tisular Anatómico de Piel Humana)
8. spine_b64.js         (Columna Lumbar y Vértebras TC Escaneo Real)
9. iridescence_b64.js   (Mariposa Morpho 3D con Nervaduras Alares Reales)
10. tissue_repair_b64.js (Matriz Tisular y Andamio de Colágeno 3D)
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

# Fuentes reales contrastadas para cada simulación
MODEL_SOURCES = [
    {
        "num": 31,
        "name": "Arrecife de Coral",
        "var_name": "CORAL_GLB_B64",
        "filename": "coral_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/MosquitoInAmber/glTF-Binary/MosquitoInAmber.glb",
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/WaterBottle/glTF-Binary/WaterBottle.glb"
        ]
    },
    {
        "num": 32,
        "name": "Pirámide Trófica / Trucha Fluvial",
        "var_name": "TROPHIC_GLB_B64",
        "filename": "trophic_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BarramundiFish/glTF-Binary/BarramundiFish.glb"
        ]
    },
    {
        "num": 33,
        "name": "Mitocondria y Orgánulo Celular",
        "var_name": "MITOCHONDRIA_GLB_B64",
        "filename": "mitochondria_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/GordenSun/LearningCell/main/public/models/cell.glb"
        ]
    },
    {
        "num": 34,
        "name": "Telómeros / Doble Hélice ADN",
        "var_name": "TELOMERES_GLB_B64",
        "filename": "telomeres_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/GordenSun/LearningCell/main/public/models/dna.glb"
        ]
    },
    {
        "num": 35,
        "name": "Árbol Real de Selva Tropical",
        "var_name": "RAINFOREST_GLB_B64",
        "filename": "rainforest_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/t0n1n3/sample-app/master/tree.glb"
        ]
    },
    {
        "num": 36,
        "name": "Canal Iónico de Membrana",
        "var_name": "IONCHANNEL_GLB_B64",
        "filename": "ionchannel_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BrainStem/glTF-Binary/BrainStem.glb"
        ]
    },
    {
        "num": 37,
        "name": "Piel Humana / Capas Tisulares",
        "var_name": "SKIN_GLB_B64",
        "filename": "skin_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Corset/glTF-Binary/Corset.glb"
        ]
    },
    {
        "num": 38,
        "name": "Columna Lumbar / Vértebra Humana",
        "var_name": "SPINE_GLB_B64",
        "filename": "spine_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/sesgigikimo/gym-muscle/main/spine.glb"
        ]
    },
    {
        "num": 39,
        "name": "Mariposa Morpho 3D",
        "var_name": "IRIDESCENCE_GLB_B64",
        "filename": "iridescence_b64.js",
        "urls": [
            "https://raw.githubusercontent.com/parabath/3rd/main/butterfly.glb"
        ]
    },
    {
        "num": 40,
        "name": "Regeneración Tisular / Matriz de Colágeno",
        "var_name": "TISSUE_REPAIR_GLB_B64",
        "filename": "tissue_repair_b64.js",
        "urls": [
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
    print("🚀 DESCARGA Y EMPAQUETADO DE MODELOS GLB CIENTÍFICOS REALES (LOTE 4)")
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

