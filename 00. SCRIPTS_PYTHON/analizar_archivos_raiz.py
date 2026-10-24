#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
analizar_archivos_raiz.py
Escanea todos los archivos y carpetas de CURSO-IA para clasificarlos en:
- VITAL (Imprescindible para GitHub Pages / Classroom)
- FÓSIL / PRUEBA (Maquetas antiguas, logs de pruebas de reposo de pantalla, etc.)
- RECURSO ACTIVO (Carpetas de sesiones, activos 3D, scripts)
"""

import os
import sys

IA_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_REPORT = os.path.join(IA_DIR, "00. SCRIPTS_PYTHON", "reporte_auditoria_archivos.txt")

def auditar():
    items = sorted(os.listdir(IA_DIR))
    lineas = []
    lineas.append(f"AUDITORÍA DE ARCHIVOS EN CURSO-IA: {IA_DIR}\n" + "="*80)

    for item in items:
        if item.startswith("."):
            continue # Ocultos
        item_path = os.path.join(IA_DIR, item)
        is_dir = os.path.isdir(item_path)
        tipo = "DIRECTORIO" if is_dir else "ARCHIVO"
        tam = os.path.getsize(item_path) if not is_dir else sum(os.path.getsize(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(item_path) if not filename.startswith("."))

        lineas.append(f"[{tipo}] {item} ({tam:,} bytes)")

    with open(OUTPUT_REPORT, "w", encoding="utf-8") as f:
        f.write("\n".join(lineas))
    print(f"Reporte generado en: {OUTPUT_REPORT}")

if __name__ == "__main__":
    auditar()

