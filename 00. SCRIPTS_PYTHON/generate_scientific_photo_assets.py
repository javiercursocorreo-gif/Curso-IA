#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_scientific_photo_assets.py
Genera los contenedores Base64 oficiales de fotografías científicas reales
para los Simuladores Fotográficos de las Sesiones 15, 16, 17, 18 y 19.

Fuentes oficiales acreditadas:
- Sesión 15: El Partenón de Atenas (Fotografía Arqueológica Real de la Acrópolis / Steve Swayne)
- Sesión 16: Hígado Humano y Vía Biliar (NIH Visible Human Project / Gray Anatomy Real Photo)
- Sesión 17: Máscara Funeraria de Tutankamón (Museo Egipcio de El Cairo / Met KV62 Macro Photo)
- Sesión 18: Neurona Piramidal Fluorescente (NIH Confocal Laser / NeuroMorpho.Org 40x)
- Sesión 19: Saturno y Anillos en Alta Resolución (NASA Cassini ISS Natural Color Mosaic)
"""

import os
import sys
import ssl
import urllib.request
import base64

ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "SIMULADORES_INTERACTIVOS", "03_ASSETS_3D_Y_DATOS"))
os.makedirs(ASSETS_DIR, exist_ok=True)

SOURCES = {
    "parthenon_photo_b64.js": {
        "var_name": "window.PARTHENON_PHOTO_B64",
        "local_jpg": "parthenon.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/The_Parthenon_in_Athens.jpg/1280px-The_Parthenon_in_Athens.jpg",
        "desc": "El Partenón de Atenas (Fotografía Arqueológica Real • Acrópolis)"
    },
    "liver_photo_b64.js": {
        "var_name": "window.LIVER_PHOTO_B64",
        "local_jpg": "liver.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Anatomy_of_the_liver_and_gallbladder.jpg/1280px-Anatomy_of_the_liver_and_gallbladder.jpg",
        "desc": "Hígado Humano y Sistema Hepatobiliar (NIH Visible Human Project • Fotografía Médica Real)"
    },
    "tutankhamun_photo_b64.js": {
        "var_name": "window.TUTANKHAMUN_PHOTO_B64",
        "local_jpg": "tutankhamun.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Tutankhamun_mask_macro_crop.jpg/1024px-Tutankhamun_mask_macro_crop.jpg",
        "desc": "Máscara Funeraria de Tutankamón (Museo de El Cairo • Fotografía Macro Arqueológica Real)"
    },
    "neuron_photo_b64.js": {
        "var_name": "window.NEURON_PHOTO_B64",
        "local_jpg": "neuron.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Pyramidal_hippocampal_neuron_40x.jpg/1024px-Pyramidal_hippocampal_neuron_40x.jpg",
        "desc": "Neurona Piramidal Cortical (NIH / NeuroMorpho • Microscopía Láser Confocal Real)"
    },
    "saturn_photo_b64.js": {
        "var_name": "window.SATURN_PHOTO_B64",
        "local_jpg": "saturn.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Saturn_%28planet%29_large.jpg/1280px-Saturn_%28planet%29_large.jpg",
        "desc": "Saturno, Anillos y División de Cassini (NASA Cassini ISS • Fotografía Astronómica Real)"
    }
}

def generate_assets():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
    }

    for filename, info in SOURCES.items():
        js_path = os.path.join(ASSETS_DIR, filename)
        local_jpg_path = os.path.join(ASSETS_DIR, info["local_jpg"])
        
        data = None
        # 1. Verificar si ya existe el JPG descargado localmente
        if os.path.exists(local_jpg_path) and os.path.getsize(local_jpg_path) > 5000:
            print(f"📁 Usando archivo JPG local: {info['local_jpg']} ({os.path.getsize(local_jpg_path)} bytes)...")
            with open(local_jpg_path, "rb") as f:
                data = f.read()
        
        # 2. Si no hay JPG local, intentar descargar por Python
        if not data:
            print(f"⬇️ Descargando por Python: {info['desc']}...")
            try:
                req = urllib.request.Request(info["url"], headers=headers)
                with urllib.request.urlopen(req, timeout=20, context=ctx) as resp:
                    data = resp.read()
                    if len(data) > 5000:
                        with open(local_jpg_path, "wb") as f_out:
                            f_out.write(data)
            except Exception as e:
                print(f"  ⚠️ Error de descarga Python para {info['desc']}: {e}")

        # 3. Codificar en Base64 y guardar el archivo .js
        if data and len(data) > 5000:
            b64_str = base64.b64encode(data).decode('utf-8')
            js_content = f'{info["var_name"]} = "data:image/jpeg;base64,{b64_str}";\n'
            with open(js_path, "w", encoding="utf-8") as f_js:
                f_js.write(js_content)
            print(f"  ✅ Generado {filename} ({len(data)} bytes imagen -> {len(js_content)} chars Base64)")
        else:
            print(f"  ❌ ALERTA: No se pudo obtener la imagen para {filename}")

if __name__ == "__main__":
    generate_assets()
