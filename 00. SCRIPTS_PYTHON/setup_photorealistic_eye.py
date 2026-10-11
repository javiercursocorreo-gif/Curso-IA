#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
setup_photorealistic_eye.py
Descarga el modelo médico 3D oficial del Globo Ocular Humano (Visible Human Project / NIH 3D: 3DPX-020963)
en formato .GLB (eye.glb) y genera su paquete Base64 (eye_b64.js) para la Versión 2 (04_SIMULADOR_OJO_HUMANO_3D_V2.html),
sin tocar ni sobrescribir la V1 (04_SIMULADOR_OJO_HUMANO_3D.html).
"""

import os
import sys
import base64
import urllib.request
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS", "03_ASSETS_3D_Y_DATOS")
SIM_DIR = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS", "01_SIMULADORES")
S04_DIR = os.path.join(ROOT_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM", "04_Sesion")

GLB_DEST = os.path.join(ASSETS_DIR, "eye.glb")
B64_DEST = os.path.join(ASSETS_DIR, "eye_b64.js")
V2_HTML = os.path.join(SIM_DIR, "04_SIMULADOR_OJO_HUMANO_3D_V2.html")

CANDIDATE_URLS = [
    # URL Oficial 1: NIH / Human Reference Atlas CDN (Visible Human Right Eye v1.3 - 24 estructuras anatómicas)
    "https://cdn.humanatlas.io/digital-objects/ref-organ/eye-female-right/v1.3/assets/3d-vh-f-eye-r.glb",
    # URL Oficial 2: NIH / Human Reference Atlas CDN (v1.2)
    "https://cdn.humanatlas.io/digital-objects/ref-organ/eye-female-right/v1.2/assets/3d-vh-f-eye-r.glb",
    # URL Oficial 3: NIH 3D Direct API Output File (3DPX-020963)
    "https://3d.nih.gov/api/submissions/43473/runs/3ab39d8a-9bbf-44b8-ad20-23270a0e1a23/output-files/2443915"
]

def download_nih_eye_glb():
    os.makedirs(ASSETS_DIR, exist_ok=True)
    if os.path.exists(GLB_DEST) and os.path.getsize(GLB_DEST) > 50000:
        print(f"✅ Archivo eye.glb ya existente ({os.path.getsize(GLB_DEST) / 1024 / 1024:.2f} MB)")
        return True

    print("🌐 Descargando modelo médico 3D del Globo Ocular desde NIH / Human Reference Atlas...")
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}

    for url in CANDIDATE_URLS:
        try:
            print(f"   Intentando: {url} ...")
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=45) as response, open(GLB_DEST, "wb") as out_file:
                shutil.copyfileobj(response, out_file)
            size_mb = os.path.getsize(GLB_DEST) / 1024 / 1024
            if size_mb > 0.05:
                print(f"✅ Descarga médica completada con éxito: {GLB_DEST} ({size_mb:.2f} MB)")
                return True
        except Exception as e:
            print(f"   ⚠️ Error en URL ({e}), probando alternativa...")

    return False

def generate_base64_js():
    if not os.path.exists(GLB_DEST):
        print("❌ No se encontró eye.glb para empaquetar en Base64.")
        return False

    print("📦 Generando eye_b64.js para carga instantánea sin bloqueo CORS...")
    with open(GLB_DEST, "rb") as f:
        data = f.read()
    b64_str = base64.b64encode(data).decode("utf-8")
    with open(B64_DEST, "w", encoding="utf-8") as f:
        f.write(f'window.EYE_GLB_B64 = "data:model/gltf-binary;base64,{b64_str}";\n')
    print(f"✅ Creado eye_b64.js ({os.path.getsize(B64_DEST) / 1024 / 1024:.2f} MB)")

    # Copiar a 04_Sesion si existe
    if os.path.exists(S04_DIR):
        try:
            shutil.copy2(GLB_DEST, os.path.join(S04_DIR, "eye.glb"))
            shutil.copy2(B64_DEST, os.path.join(S04_DIR, "eye_b64.js"))
            shutil.copy2(V2_HTML, os.path.join(S04_DIR, "SIMULADOR_OJO_HUMANO_3D_V2.html"))
            print("✅ Copiado también a 04_Sesion.")
        except Exception:
            pass
    return True

if __name__ == "__main__":
    if download_nih_eye_glb():
        generate_base64_js()
        print("🚀 Todo listo. Abriendo 04_SIMULADOR_OJO_HUMANO_3D_V2.html...")
    else:
        print("⚠️ No se pudo descargar localmente, el visor V2 cargará directamente desde el CDN del NIH.")

