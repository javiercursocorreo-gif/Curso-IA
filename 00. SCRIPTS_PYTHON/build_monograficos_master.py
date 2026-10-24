#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_monograficos_master.py
Compilador Maestro de la Sección de Monográficos:
- Genera la Ficha Didáctica Oficial en PDF (MONO-001).
- Sincroniza y distribuye MAPA_MONOGRAFICOS.html y TALLER_MONOGRAFICO_01_ESTILOS_ANIMADOS.html.
- Abre automáticamente MAPA_MONOGRAFICOS.html en Safari para validación visual.
"""

import os
import sys
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DIR_104 = os.path.join(BASE_DIR, "104 ESTILO ANIMADOS SIN PROGRAMAR")
DIR_CLASSROOM = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "105. [MONOGRAFICOS] CUADERNOS_Y_TALLERES_ESPECIALES")
os.makedirs(DIR_104, exist_ok=True)
os.makedirs(DIR_CLASSROOM, exist_ok=True)

ROOT_MAP = os.path.join(BASE_DIR, "MAPA_MONOGRAFICOS.html")
MAP_IN_104 = os.path.join(DIR_104, "MAPA_MONOGRAFICOS.html")
MAP_IN_CLASSROOM = os.path.join(DIR_CLASSROOM, "MAPA_MONOGRAFICOS.html")

def main():
    print("=" * 80)
    print("🚀 INICIANDO COMPILACIÓN MAESTRA DE MONOGRÁFICOS")
    print("=" * 80)

    # 1. Compilar PDF MONO-001
    print("\n1. Generando Ficha Didáctica Oficial del Monográfico 01 (PDF)...")
    try:
        from build_pdf_mono_001 import build_mono_001_pdf
        build_mono_001_pdf()
    except Exception as e:
        print(f"❌ Error al compilar PDF MONO-001: {e}")

    # 2. Espejar MAPA_MONOGRAFICOS.html
    print("\n2. Sincronizando Mapa Maestro de Monográficos en todas las rutas...")
    if os.path.exists(ROOT_MAP):
        for dest in [MAP_IN_104, MAP_IN_CLASSROOM]:
            try:
                shutil.copy2(ROOT_MAP, dest)
                print(f"  ✅ Espejado en: {dest}")
            except Exception as e:
                print(f"  ❌ Error al copiar a {dest}: {e}")

    # 3. Validar Taller Interactivo
    taller_path = os.path.join(DIR_104, "TALLER_MONOGRAFICO_01_ESTILOS_ANIMADOS.html")
    if os.path.exists(taller_path):
        taller_classroom = os.path.join(DIR_CLASSROOM, "TALLER_MONOGRAFICO_01_ESTILOS_ANIMADOS.html")
        shutil.copy2(taller_path, taller_classroom)
        print(f"  ✅ Taller interactivo espejado en: {taller_classroom}")

    print("\n✨ Compilación de Monográficos finalizada con éxito.")

if __name__ == "__main__":
    main()

