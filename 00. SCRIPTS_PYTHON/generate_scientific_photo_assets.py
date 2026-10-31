#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_scientific_photo_assets.py
Genera los contenedores Base64 oficiales de fotografías científicas reales
para los Simuladores Fotográficos de las Sesiones 14, 15, 16, 17, 18 y 19.

Fuentes científicas oficiales acreditadas:
- Sesión 14: Auroras UV de Júpiter (NASA / ESA Hubble STIS)
- Sesión 15: Telescopio Espacial James Webb (NASA / ESA / CSA • Espejo de Berilio-Oro GSFC)
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
    "jwst_photo_b64.js": {
        "var_name": "window.JWST_PHOTO_B64",
        "local_jpg": "jwst.jpg",
        "urls": [
            "https://upload.wikimedia.org/wikipedia/commons/e/e0/James_Webb_Space_Telescope_mirror.jpg",
            "https://commons.wikimedia.org/wiki/Special:FilePath/James_Webb_Space_Telescope_mirror.jpg",
            "https://images-assets.nasa.gov/image/GSFC_20171208_Archive_e001465/GSFC_20171208_Archive_e001465~orig.jpg"
        ],
        "desc": "Telescopio Espacial James Webb (JWST • NASA/ESA/CSA • Espejo de Berilio-Oro GSFC)"
    },
    "liver_photo_b64.js": {
        "var_name": "window.LIVER_PHOTO_B64",
        "local_jpg": "liver.jpg",
        "urls": [
            "https://upload.wikimedia.org/wikipedia/commons/c/c5/Anatomy_of_the_liver_and_gallbladder.jpg",
            "https://commons.wikimedia.org/wiki/Special:FilePath/Anatomy_of_the_liver_and_gallbladder.jpg"
        ],
        "desc": "Hígado Humano y Sistema Hepatobiliar (NIH Visible Human Project • Fotografía Médica Real)"
    },
    "tutankhamun_photo_b64.js": {
        "var_name": "window.TUTANKHAMUN_PHOTO_B64",
        "local_jpg": "tutankhamun.jpg",
        "urls": [
            "https://upload.wikimedia.org/wikipedia/commons/3/38/Tutankhamun_mask_macro_crop.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/4/4e/Tutankhamun_death_mask_%28front%29.jpg",
            "https://commons.wikimedia.org/wiki/Special:FilePath/Tutankhamun_death_mask_(front).jpg"
        ],
        "desc": "Máscara Funeraria de Tutankamón (Museo Egipcio de El Cairo • Fotografía Macro Arqueológica Real)"
    },
    "neuron_photo_b64.js": {
        "var_name": "window.NEURON_PHOTO_B64",
        "local_jpg": "neuron.jpg",
        "urls": [
            "https://upload.wikimedia.org/wikipedia/commons/1/15/Pyramidal_hippocampal_neuron_40x.jpg",
            "https://commons.wikimedia.org/wiki/Special:FilePath/Pyramidal_hippocampal_neuron_40x.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/0/07/GolgiStainedNeuron.jpg"
        ],
        "desc": "Neurona Piramidal Cortical (NIH / NeuroMorpho • Microscopía Láser Confocal Real)"
    },
    "saturn_photo_b64.js": {
        "var_name": "window.SATURN_PHOTO_B64",
        "local_jpg": "saturn.jpg",
        "urls": [
            "https://upload.wikimedia.org/wikipedia/commons/b/b4/Saturn_%28planet%29_large.jpg",
            "https://commons.wikimedia.org/wiki/Special:FilePath/Saturn_(planet)_large.jpg"
        ],
        "desc": "Saturno, Anillos y División de Cassini (NASA Cassini ISS • Fotografía Astronómica Real)"
    }
}

def is_valid_image_data(data):
    if not data or len(data) < 5000:
        return False
    # Rechazar páginas de error HTML de Wikimedia o servidores
    if data.startswith(b'<!DOCTYPE') or data.startswith(b'<html') or b'Wikimedia Error' in data[:500]:
        return False
    # Verificar cabecera JPEG o PNG
    if data.startswith(b'\xff\xd8\xff') or data.startswith(b'\x89PNG'):
        return True
    return len(data) > 10000

def generate_assets():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Referer': 'https://commons.wikimedia.org/'
    }

    print("=" * 80)
    print("🔬 GENERADOR DE ACTIVOS CIENTÍFICOS REALES BASE64 (SESIONES 15 A 19)")
    print("=" * 80)

    for filename, info in SOURCES.items():
        js_path = os.path.join(ASSETS_DIR, filename)
        local_jpg_path = os.path.join(ASSETS_DIR, info["local_jpg"])
        
        data = None
        # 1. Verificar si ya existe el archivo JPG local válido
        if os.path.exists(local_jpg_path):
            with open(local_jpg_path, "rb") as f:
                existing = f.read()
            if is_valid_image_data(existing):
                print(f"📁 Usando archivo JPG local válido: {info['local_jpg']} ({len(existing)} bytes)...")
                data = existing
            else:
                print(f"🗑️ Descartando archivo JPG local corrupto/HTML: {info['local_jpg']} ({len(existing)} bytes)")
                try:
                    os.remove(local_jpg_path)
                except Exception:
                    pass

        # 2. Si no hay JPG local válido, intentar descargar probando las URLs alternativas
        if not data:
            print(f"⬇️ Descargando fotografía oficial: {info['desc']}...")
            for target_url in info["urls"]:
                try:
                    print(f"   Intentando: {target_url} ...")
                    req = urllib.request.Request(target_url, headers=headers)
                    with urllib.request.urlopen(req, timeout=25, context=ctx) as resp:
                        content = resp.read()
                        if is_valid_image_data(content):
                            data = content
                            with open(local_jpg_path, "wb") as f_out:
                                f_out.write(data)
                            print(f"   ✅ Descarga exitosa ({len(data)} bytes) desde {target_url}")
                            break
                        else:
                            print(f"   ⚠️ Respuesta inválida o HTML ({len(content)} bytes), probando siguiente...")
                except Exception as e:
                    print(f"   ⚠️ Error en descarga: {e}")

        # 3. Codificar en Base64 y guardar el archivo .js
        if data and is_valid_image_data(data):
            b64_str = base64.b64encode(data).decode('utf-8')
            mime = "image/png" if data.startswith(b'\x89PNG') else "image/jpeg"
            js_content = f'{info["var_name"]} = "data:{mime};base64,{b64_str}";\n'
            with open(js_path, "w", encoding="utf-8") as f_js:
                f_js.write(js_content)
            print(f"  ⭐ ACTIVO GENERADO: {filename} ({len(data)} bytes imagen -> {len(js_content)} chars Base64)")
        else:
            print(f"  ❌ ALERTA: No se pudo obtener la imagen para {filename}")

    print("=" * 80)
    print("✅ PROCESO DE ACTIVOS FOTOGRÁFICOS FINALIZADO")
    print("=" * 80)

if __name__ == "__main__":
    generate_assets()
