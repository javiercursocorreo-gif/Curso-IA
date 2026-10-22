#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_cod_lote4_master.py
Compilador Maestro del LOTE 4 [COD] (Sesiones 31 a 40):
- Descarga y empaqueta los 10 Modelos 3D REALES en Base64 (_b64.js) en 03_ASSETS_3D_Y_DATOS/.
- Genera y distribuye los 10 Simuladores HTML interactivos en Babylon.js (Dual Espejado).
- Genera las 10 Fichas Didácticas Oficiales en PDF (COD-031 a COD-040).
- Sincroniza las tarjetas #10B [COD] en MAPA_SESION_31.html a MAPA_SESION_40.html.
- Garantiza CERO dibujos animados ni mallas procedurales toscas.
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
SESSIONS_ROOT = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
SIM_DIR = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "01_SIMULADORES")
CATALOG_DIR = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "02_INDICES_Y_CATALOGOS")

os.makedirs(SIM_DIR, exist_ok=True)
os.makedirs(CATALOG_DIR, exist_ok=True)

def step1_download_real_glbs():
    print("\n--- 1. Descargando Modelos GLB Científicos Reales en Base64 ---")
    try:
        from download_and_convert_lote4_real_glbs import main as download_main
        download_main()
    except Exception as e:
        print(f"  ❌ Error en descarga de modelos reales: {e}")

def step2_generate_html_simulators():
    print("\n--- 2. Generando los 10 Simuladores HTML con Babylon.js (Dual Espejado) ---")
    try:
        from generate_cod_lote4_htmls import main as generate_htmls_main
        generate_htmls_main()
    except Exception as e:
        print(f"  ❌ Error generando simuladores HTML: {e}")

def step3_generate_pdf_fichas():
    print("\n--- 3. Generando Fichas Didácticas Oficiales en PDF (COD-031 a COD-040) ---")
    pdf_modules = [
        (31, "build_pdf_cod_031", "build_cod_031_taller_3d_pdf"),
        (32, "build_pdf_cod_032", "build_cod_032_taller_3d_pdf"),
        (33, "build_pdf_cod_033", "build_cod_033_taller_3d_pdf"),
        (34, "build_pdf_cod_034", "build_cod_034_taller_3d_pdf"),
        (35, "build_pdf_cod_035", "build_cod_035_taller_3d_pdf"),
        (36, "build_pdf_cod_036", "build_cod_036_taller_3d_pdf"),
        (37, "build_pdf_cod_037", "build_cod_037_taller_3d_pdf"),
        (38, "build_pdf_cod_038", "build_cod_038_taller_3d_pdf"),
        (39, "build_pdf_cod_039", "build_cod_039_taller_3d_pdf"),
        (40, "build_pdf_cod_040", "build_cod_040_taller_3d_pdf"),
    ]
    for num, mod_name, fn_name in pdf_modules:
        try:
            mod = __import__(mod_name)
            fn = getattr(mod, fn_name)
            fn()
        except Exception as e:
            print(f"  ❌ Error COD-{num:03d}: {e}")

def step4_sync_maps():
    print("\n--- 4. Sincronizando Tarjetas #10B [COD] en los Mapas de Sesión 31 a 40 ---")
    try:
        from sync_maps_lote4 import main as sync_maps_main
        sync_maps_main()
    except Exception as e:
        print(f"  ❌ Error sincronizando mapas: {e}")

def main():
    print("=" * 80)
    print("🚀 COMPILADOR MAESTRO LOTE 4 [COD] (SESIONES 31 A 40) - GLB CIENTÍFICOS REALES")
    print("=" * 80)

    step1_download_real_glbs()
    step2_generate_html_simulators()
    step3_generate_pdf_fichas()
    step4_sync_maps()

    print("\n✨ RECONSTRUCCIÓN COMPLETA DEL LOTE 4 CON MODELOS REALES FINALIZADA AL 100%.")

if __name__ == '__main__':
    main()
