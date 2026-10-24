#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
limpiar_paneles_fosiles.py
Purga radical: En PANELES_CSV deja ÚNICA Y EXCLUSIVAMENTE CURSO_IA_UNIFICADO.csv.
Borra cualquier otro archivo o subcarpeta (incluyendo índices, paneles viejos y carpetas archivadas).
"""

import os
import sys
import glob
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IA_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PARENT_DIR = os.path.abspath(os.path.join(IA_DIR, ".."))

def purga_total():
    print("=== PURGA RADICAL DE ARCHIVOS FÓSILES ===", flush=True)
    paneles_dir = os.path.join(IA_DIR, "PANELES_CSV")
    os.makedirs(paneles_dir, exist_ok=True)

    # 1. En PANELES_CSV: Borrar ABSOLUTAMENTE TODO excepto CURSO_IA_UNIFICADO.csv
    for item in os.listdir(paneles_dir):
        if item == "CURSO_IA_UNIFICADO.csv":
            continue
        item_path = os.path.join(paneles_dir, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
                print(f"  🗑️ Borrado en PANELES_CSV: {item}", flush=True)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path, ignore_errors=True)
                print(f"  🗑️ Carpeta borrada en PANELES_CSV: {item}/", flush=True)
        except Exception as e:
            print(f"  ⚠️ Error borrando {item}: {e}", flush=True)

    # 2. En la raíz de CURSO-IA: borrar cualquier CSV suelto excepto si se desea
    for csv_file in glob.glob(os.path.join(IA_DIR, "*.csv")):
        fname = os.path.basename(csv_file)
        if "UNIFICADO" not in fname:
            try:
                os.remove(csv_file)
                print(f"  🗑️ Borrado en raíz: {fname}", flush=True)
            except Exception as e:
                pass

    # 3. Eliminar cualquier archivo que contenga INDICE o FOSIL en IA y Robótica
    patrones_extra = [
        os.path.join(IA_DIR, "*INDICE*.csv"),
        os.path.join(IA_DIR, "*indice*.csv"),
        os.path.join(paneles_dir, "*INDICE*.csv"),
        os.path.join(paneles_dir, "*indice*.csv"),
    ]
    for p in patrones_extra:
        for f in glob.glob(p):
            try:
                os.remove(f)
                print(f"  🗑️ Borrado extra: {os.path.basename(f)}", flush=True)
            except Exception:
                pass

    print("\n✅ ESTADO FINAL DE LA CARPETA PANELES_CSV:")
    archivos_restantes = os.listdir(paneles_dir)
    for a in archivos_restantes:
        print(f"   👉 {a}", flush=True)

def main():
    purga_total()

if __name__ == "__main__":
    main()
