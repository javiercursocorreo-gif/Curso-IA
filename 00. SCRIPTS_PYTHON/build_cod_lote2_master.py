#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_cod_lote2_master.py
Compilador Maestro del LOTE 2 [COD] (Sesiones 11 a 20).
Ejecuta la generación de las 10 Fichas Didácticas Oficiales en PDF:
- COD-011: Violín Stradivarius 'The Gould 1693' (Met Museum)
- COD-012: Nebulosa Helix 'El Ojo de Dios' (NASA Hubble & Spitzer)
- COD-013: Doble Hélice de ADN (Protein Data Bank / Cristalografía)
- COD-014: Auroras Ultravioletas de Júpiter (NASA Cassini & Hubble)
- COD-015: El Partenón de Atenas & Proporción Áurea (Acrópolis)
- COD-016: Hígado Humano y Sistema Hepatobiliar (NIH 3D)
- COD-017: Faraón Tutankamón y Máscara de Oro (Tumba KV62)
- COD-018: Neurona Piramidal Cortical y Sinapsis (NeuroMorpho.Org / NIH)
- COD-019: Saturno, Anillos y División de Cassini (NASA Cassini)
- COD-020: Esqueleto de la Mano Humana y Biomecánica (NIH 3D)
"""

import sys
import os

from build_pdf_cod_011 import build_cod_011_taller_3d_pdf
from build_pdf_cod_012 import build_cod_012_taller_3d_pdf
from build_pdf_cod_013 import build_cod_013_taller_3d_pdf
from build_pdf_cod_014 import build_cod_014_taller_3d_pdf
from build_pdf_cod_015 import build_cod_015_taller_3d_pdf
from build_pdf_cod_016 import build_cod_016_taller_3d_pdf
from build_pdf_cod_017 import build_cod_017_taller_3d_pdf
from build_pdf_cod_018 import build_cod_018_taller_3d_pdf
from build_pdf_cod_019 import build_cod_019_taller_3d_pdf
from build_pdf_cod_020 import build_cod_020_taller_3d_pdf

TASKS = [
    ("COD-011 (Violín Stradivarius 3D)", build_cod_011_taller_3d_pdf),
    ("COD-012 (Nebulosa Helix 3D)", build_cod_012_taller_3d_pdf),
    ("COD-013 (Doble Hélice ADN 3D)", build_cod_013_taller_3d_pdf),
    ("COD-014 (Auroras de Júpiter 3D)", build_cod_014_taller_3d_pdf),
    ("COD-015 (Partenón de Atenas 3D)", build_cod_015_taller_3d_pdf),
    ("COD-016 (Hígado Humano 3D)", build_cod_016_taller_3d_pdf),
    ("COD-017 (Máscara Tutankamón 3D)", build_cod_017_taller_3d_pdf),
    ("COD-018 (Neurona Piramidal 3D)", build_cod_018_taller_3d_pdf),
    ("COD-019 (Saturno & Anillos 3D)", build_cod_019_taller_3d_pdf),
    ("COD-020 (Mano Humana 3D)", build_cod_020_taller_3d_pdf),
]

def main():
    print("=" * 80)
    print("🚀 INICIANDO COMPILACIÓN MAESTRA DE FICHAS DIDÁCTICAS LOTE 2 [COD] (SESIONES 11 A 20)")
    print("=" * 80)
    
    total = len(TASKS)
    success = 0
    errors = []

    for idx, (label, func) in enumerate(TASKS, 1):
        try:
            print(f"[{idx:02d}/{total:02d}] Generando {label}...")
            func()
            success += 1
        except Exception as e:
            print(f"❌ Error en {label}: {e}")
            errors.append((label, str(e)))

    print("\n" + "=" * 80)
    print(f"📊 RESUMEN: {success}/{total} FICHAS PDF GENERADAS CORRECTAMENTE.")
    if errors:
        print("⚠️ ERRORES DETECTADOS:")
        for label, err in errors:
            print(f"  - {label}: {err}")
        sys.exit(1)
    else:
        print("✅ 100% DE LAS FICHAS DEL LOTE 2 COMPILADAS Y SELLADAS.")
        print("=" * 80)

if __name__ == '__main__':
    main()

