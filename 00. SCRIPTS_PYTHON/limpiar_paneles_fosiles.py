#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
limpiar_paneles_fosiles.py
Limpia y archiva los paneles CSV fósiles (antiguas clases trimestrales y monográficos sueltos)
tanto en CURSO-IA como en las carpetas de Robótica.
Conserva únicamente los archivos maestros unificados vigentes:
- CURSO_IA_UNIFICADO.csv
- CURSO_ROBOTICA_UNIFICADO.csv (si existe)
"""

import os
import sys
import glob
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IA_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PARENT_DIR = os.path.abspath(os.path.join(IA_DIR, ".."))

def limpiar_curso_ia():
    print("=== LIMPIEZA DE PANELES FÓSILES EN CURSO-IA ===", flush=True)
    paneles_dir = os.path.join(IA_DIR, "PANELES_CSV")
    archive_dir = os.path.join(paneles_dir, "ARCHIVADOS_FOSILES")
    os.makedirs(archive_dir, exist_ok=True)

    # 1. En PANELES_CSV: mover los paneles por lotes y monográficos antiguos
    fosiles = [
        "0.PANEL_MONOGRAFICOS.csv",
        "1.PANEL_SESIONES_01_AL_15.csv",
        "2.PANEL_SESIONES_16_AL_30.csv",
        "3.PANEL_SESIONES_31_AL_45.csv",
        "4.PANEL_SESIONES_46_AL_60.csv",
    ]
    for f in fosiles:
        src = os.path.join(paneles_dir, f)
        if os.path.exists(src):
            dst = os.path.join(archive_dir, f)
            shutil.move(src, dst)
            print(f"  📦 Archivado fósil: PANELES_CSV/{f} -> ARCHIVADOS_FOSILES/{f}", flush=True)

    # 2. En la raíz de CURSO-IA: limpiar duplicados sueltos dejando la raíz limpia
    raiz_fosiles = ["0.PANEL_MONOGRAFICOS.csv"]
    for f in raiz_fosiles:
        src = os.path.join(IA_DIR, f)
        if os.path.exists(src):
            os.remove(src)
            print(f"  🗑️ Eliminado de la raíz: {f}", flush=True)

    # Asegurar que CURSO_IA_UNIFICADO.csv es el único en PANELES_CSV
    unificado = os.path.join(paneles_dir, "CURSO_IA_UNIFICADO.csv")
    if os.path.exists(unificado):
        print(f"  ✅ Archivo Maestro Vigente Preservado: PANELES_CSV/CURSO_IA_UNIFICADO.csv", flush=True)

def limpiar_robotica():
    print("\n=== BÚSQUEDA Y LIMPIEZA EN CARPETAS DE ROBÓTICA ===", flush=True)
    # Buscar carpetas de robótica en el directorio de clases
    carpetas_rob = glob.glob(os.path.join(PARENT_DIR, "*ROBOTICA*")) + glob.glob(os.path.join(PARENT_DIR, "*Robótica*")) + glob.glob(os.path.join(PARENT_DIR, "*ROBOT*"))
    carpetas_rob = list(set([os.path.abspath(c) for c in carpetas_rob]))

    encontrado = False
    for c_dir in carpetas_rob:
        # No tocar CURSO-ROBOTICA-IA-COMUN
        if "COMUN" in os.path.basename(c_dir).upper():
            continue

        print(f"Inspeccionando carpeta: {os.path.basename(c_dir)}", flush=True)
        # Buscar carpetas de paneles o CSVs sueltos
        posibles_dirs_csv = [
            c_dir,
            os.path.join(c_dir, "PANELES_CSV"),
            os.path.join(c_dir, "CSV"),
            os.path.join(c_dir, "PANELES")
        ]
        
        for d in posibles_dirs_csv:
            if not os.path.exists(d):
                continue
            arch_dir = os.path.join(d, "ARCHIVADOS_FOSILES")
            
            csv_files = glob.glob(os.path.join(d, "*.csv"))
            for csv_path in csv_files:
                fname = os.path.basename(csv_path)
                # Si es el unificado vigente, conservarlo
                if "UNIFICADO" in fname.upper():
                    print(f"  ✅ Archivo Maestro Vigente Preservado: {fname}", flush=True)
                    continue
                # Si es un panel de bloques antiguos o sesiones antiguas
                os.makedirs(arch_dir, exist_ok=True)
                dst = os.path.join(arch_dir, fname)
                shutil.move(csv_path, dst)
                print(f"  📦 Archivado fósil: {fname} -> ARCHIVADOS_FOSILES/{fname}", flush=True)
                encontrado = True

    if not encontrado:
        print("  ℹ️ No se detectaron paneles CSV fósiles pendientes en carpetas de robótica.", flush=True)

def main():
    limpiar_curso_ia()
    limpiar_robotica()
    print("\n🎉 ¡Limpieza de paneles fósiles completada con éxito!", flush=True)

if __name__ == "__main__":
    main()

