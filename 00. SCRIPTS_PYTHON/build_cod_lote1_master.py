#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_cod_lote1_master.py
Compilador Maestro del LOTE 1 [COD] (Sesiones 01 a 10):
- Genera las 10 Fichas Didácticas Oficiales en PDF (COD-001 a COD-010).
- Sincroniza y distribuye los Simuladores HTML interactivos hacia
  SIMULADORES_INTERACTIVOS/01_SIMULADORES/ y las carpetas de sesión.
- Sesiones 03 a 07: Simuladores Científicos Oficiales NASA Eyes 3D.
"""

import os
import sys
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
SESSIONS_ROOT = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
SIM_DIR = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "01_SIMULADORES")
CATALOG_DIR = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "02_INDICES_Y_CATALOGOS")

os.makedirs(SIM_DIR, exist_ok=True)
os.makedirs(CATALOG_DIR, exist_ok=True)

# Mapeo de archivos de simuladores por sesión
LOTE_1_SIMS = [
    {
        "num": 1,
        "src_name": "SIMULADOR_PULMONES_3D.html",
        "aliases": ["SIMULADOR_PULMONES_3D.html"]
    },
    {
        "num": 2,
        "src_name": "SIMULADOR_CORAZON_3D.html",
        "aliases": ["SIMULADOR_CORAZON_3D.html"]
    },
    {
        "num": 3,
        "src_name": "SIMULADOR_SISTEMA_SOLAR_3D.html",
        "aliases": ["SIMULADOR_SISTEMA_SOLAR_3D.html", "3. COD-003_Simulador_Sistema_Solar_3D.html", "COD_003_SIMULADOR.html"]
    },
    {
        "num": 4,
        "src_name": "SIMULADOR_TIERRA_CLIMA_3D.html",
        "aliases": ["SIMULADOR_TIERRA_CLIMA_3D.html", "3. COD-004_Simulador_Tierra_Clima_3D.html", "COD_004_SIMULADOR.html"]
    },
    {
        "num": 5,
        "src_name": "SIMULADOR_ESTACION_ESPACIAL_ISS_3D.html",
        "aliases": ["SIMULADOR_ESTACION_ESPACIAL_ISS_3D.html", "SIMULADOR_ISS_3D.html", "3. COD-005_Simulador_ISS_3D.html", "COD_005_SIMULADOR.html"]
    },
    {
        "num": 6,
        "src_name": "SIMULADOR_LUNA_ARTEMISA_3D.html",
        "aliases": ["SIMULADOR_LUNA_ARTEMISA_3D.html", "SIMULADOR_LUNA_3D.html", "3. COD-006_Simulador_Luna_Artemisa_3D.html", "COD_006_SIMULADOR.html"]
    },
    {
        "num": 7,
        "src_name": "SIMULADOR_SOL_SONDA_PARKER_3D.html",
        "aliases": ["SIMULADOR_SOL_SONDA_PARKER_3D.html", "SIMULADOR_SOL_3D.html", "3. COD-007_Simulador_Sol_Parker_3D.html", "COD_007_SIMULADOR.html"]
    },
    {
        "num": 8,
        "src_name": "SIMULADOR_MOTOR_TURBOFAN_3D.html",
        "aliases": ["SIMULADOR_MOTOR_TURBOFAN_3D.html", "SIMULADOR_MOTOR_3D.html"]
    },
    {
        "num": 9,
        "src_name": "SIMULADOR_CRANEO_TREX_3D.html",
        "aliases": ["SIMULADOR_CRANEO_TREX_3D.html", "SIMULADOR_TREX_3D.html"]
    },
    {
        "num": 10,
        "src_name": "SIMULADOR_MOLAR_HUMANO_3D.html",
        "aliases": ["SIMULADOR_MOLAR_HUMANO_3D.html", "SIMULADOR_MOLAR_3D.html"]
    }
]

def generate_all_pdfs():
    print("\n--- Generando Fichas Didácticas Oficiales en PDF (COD-001 a COD-010) ---")
    
    # 001
    try:
        from build_pdf_cod_001 import build_cod_001_taller_3d_pdf
        build_cod_001_taller_3d_pdf()
    except Exception as e:
        print(f"  ❌ Error COD-001: {e}")

    # 002
    try:
        from build_pdf_cod_002 import build_cod_002_taller_3d_pdf
        build_cod_002_taller_3d_pdf()
    except Exception as e:
        print(f"  ❌ Error COD-002: {e}")

    # 003
    try:
        from build_pdf_cod_003 import build_cod_003_taller_3d_pdf
        build_cod_003_taller_3d_pdf()
    except Exception as e:
        print(f"  ❌ Error COD-003: {e}")

    # 004
    try:
        from build_pdf_cod_004 import build_cod_004_taller_3d_pdf
        build_cod_004_taller_3d_pdf()
    except Exception as e:
        print(f"  ❌ Error COD-004: {e}")

    # 005
    try:
        from build_pdf_cod_005 import build_cod_005_taller_3d_pdf
        build_cod_005_taller_3d_pdf()
    except Exception as e:
        print(f"  ❌ Error COD-005: {e}")

    # 006
    try:
        from build_pdf_cod_006 import build_cod_006_taller_3d_pdf
        build_cod_006_taller_3d_pdf()
    except Exception as e:
        print(f"  ❌ Error COD-006: {e}")

    # 007
    try:
        from build_pdf_cod_007 import build_cod_007_taller_3d_pdf
        build_cod_007_taller_3d_pdf()
    except Exception as e:
        print(f"  ❌ Error COD-007: {e}")

    # 008
    try:
        from build_pdf_cod_008 import build_cod_008_taller_3d_pdf
        build_cod_008_taller_3d_pdf()
    except Exception as e:
        print(f"  ❌ Error COD-008: {e}")

    # 009
    try:
        from build_pdf_cod_009 import build_cod_009_taller_3d_pdf
        build_cod_009_taller_3d_pdf()
    except Exception as e:
        print(f"  ❌ Error COD-009: {e}")

    # 010
    try:
        from build_pdf_cod_010 import build_cod_010_taller_3d_pdf
        build_cod_010_taller_3d_pdf()
    except Exception as e:
        print(f"  ❌ Error COD-010: {e}")

def sync_simulators():
    print("\n--- Sincronizando y Desplegando Simuladores HTML del Lote 1 ---")
    for item in LOTE_1_SIMS:
        n = item["num"]
        src_name = item["src_name"]
        sess_folder = os.path.join(SESSIONS_ROOT, f"{n:02d}_Sesion")
        src_path = os.path.join(sess_folder, src_name)
        
        if not os.path.exists(src_path):
            print(f"  ⚠️ Advertencia: No se encontró {src_path}")
            continue

        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Asegurar alias en la propia carpeta de sesión
        for alias in item["aliases"]:
            alias_path = os.path.join(sess_folder, alias)
            if alias_path != src_path:
                with open(alias_path, "w", encoding="utf-8") as f:
                    f.write(content)

        # Copiar a SIMULADORES_INTERACTIVOS/01_SIMULADORES/ con todos los alias
        for alias in item["aliases"]:
            dest_sim_path = os.path.join(SIM_DIR, alias)
            with open(dest_sim_path, "w", encoding="utf-8") as f:
                f.write(content)

        print(f"  ✓ Sesión {n:02d} ({src_name}) sincronizada con éxito en SIMULADORES_INTERACTIVOS/01_SIMULADORES/.")

def main():
    print("==============================================================================")
    print("🚀 COMPILADOR MAESTRO LOTE 1 [COD] • SESIONES 01 A 10 (TRIPLE SALVAGUARDA)")
    print("==============================================================================")
    generate_all_pdfs()
    sync_simulators()
    print("\n🎉 ¡LOTE 1 [COD] (Sesiones 01 a 10) 100% Compilado, Desplegado y Sincronizado!")

if __name__ == '__main__':
    main()
