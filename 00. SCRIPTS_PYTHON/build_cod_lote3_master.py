#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_cod_lote3_master.py
Compilador Maestro del LOTE 3 [COD] (Sesiones 21 a 30).
Ejecuta la generación de las 10 Fichas Didácticas Oficiales en PDF:
- COD-021: Escala Cósmica 3D (CERN / Planck a Universo Observable)
- COD-022: Esfera de Dyson y Megaestructuras Kardashev 3D (Freeman Dyson)
- COD-023: Termodinámica Molecular: Cero Absoluto a Fusión 3D (NIST Boltzmann)
- COD-024: Las 11 Dimensiones, Espacios Calabi-Yau y Teoría M 3D (CERN / Witten)
- COD-025: Relatividad Especial, Cono de Luz y Dilatación Lorentz 3D (Einstein)
- COD-026: Agujero Negro Supermasivo y Lente Gravitatoria 3D (EHT / Schwarzschild)
- COD-027: Estructura del Átomo y Orbitales Cuánticos 3D (Schrödinger / NIST)
- COD-028: Tabla Periódica Interactiva y Enlaces Químicos 3D (IUPAC / VSEPR)
- COD-029: Experimento de la Doble Rendija y Dualidad Onda-Partícula 3D (Young / Davisson)
- COD-030: Computación Cuántica, Qubits y Esfera de Bloch 3D (Félix Bloch / IBM Quantum)
"""

import sys
import os

from build_pdf_cod_021 import build_cod_021_taller_3d_pdf
from build_pdf_cod_022 import build_cod_022_taller_3d_pdf
from build_pdf_cod_023 import build_cod_023_taller_3d_pdf
from build_pdf_cod_024 import build_cod_024_taller_3d_pdf
from build_pdf_cod_025 import build_cod_025_taller_3d_pdf
from build_pdf_cod_026 import build_cod_026_taller_3d_pdf
from build_pdf_cod_027 import build_cod_027_taller_3d_pdf
from build_pdf_cod_028 import build_cod_028_taller_3d_pdf
from build_pdf_cod_029 import build_cod_029_taller_3d_pdf
from build_pdf_cod_030 import build_cod_030_taller_3d_pdf

TASKS = [
    ("COD-021 (Escala Cósmica 3D)", build_cod_021_taller_3d_pdf),
    ("COD-022 (Esfera de Dyson 3D)", build_cod_022_taller_3d_pdf),
    ("COD-023 (Termodinámica Molecular 3D)", build_cod_023_taller_3d_pdf),
    ("COD-024 (11 Dimensiones & Calabi-Yau 3D)", build_cod_024_taller_3d_pdf),
    ("COD-025 (Relatividad Especial 3D)", build_cod_025_taller_3d_pdf),
    ("COD-026 (Agujero Negro Supermasivo 3D)", build_cod_026_taller_3d_pdf),
    ("COD-027 (Átomo y Orbitales Cuánticos 3D)", build_cod_027_taller_3d_pdf),
    ("COD-028 (Tabla Periódica & Enlaces 3D)", build_cod_028_taller_3d_pdf),
    ("COD-029 (Doble Rendija Cuántica 3D)", build_cod_029_taller_3d_pdf),
    ("COD-030 (Computación Cuántica & Bloch 3D)", build_cod_030_taller_3d_pdf),
]

def main():
    print("=" * 80)
    print("🚀 INICIANDO COMPILACIÓN MAESTRA DE FICHAS DIDÁCTICAS LOTE 3 [COD] (SESIONES 21 A 30)")
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
        print("✅ 100% DE LAS FICHAS DEL LOTE 3 COMPILADAS Y SELLADAS.")
        print("=" * 80)

if __name__ == '__main__':
    main()

