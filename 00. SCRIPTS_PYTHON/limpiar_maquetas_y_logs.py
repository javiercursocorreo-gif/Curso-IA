#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
limpiar_maquetas_y_logs.py
Elimina de la raíz de CURSO-IA:
- Maquetas visuales obsoletas (MAQUETA_SESION_RADIAL.html, etc.)
- Archivos de telemetría y pruebas de reposo (resultado_inactividad.txt, logs de energía)
- Archivos residuales de guías o CSVs viejos en la raíz

Preserva intactos:
- index.html (Entrada web a GitHub Pages)
- MAPA_MONOGRAFICOS.html (Mapa Oficial de Monográficos en Classroom)
- INDICE_DE_PRACTICAS_POR_ETIQUETA/ (Catálogo general)
- PANELES_CSV/CURSO_IA_UNIFICADO.csv (Maestro de Classroom)
"""

import os
import sys
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IA_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

PATRONES_BORRADO = [
    # Maquetas obsoletas
    os.path.join(IA_DIR, "*MAQUETA*.*"),
    os.path.join(IA_DIR, "*maqueta*.*"),
    # Logs y pruebas de reposo / energía
    os.path.join(IA_DIR, "*inactividad*.*"),
    os.path.join(IA_DIR, "*energia*.*"),
    os.path.join(IA_DIR, "*registro*.*"),
    os.path.join(IA_DIR, "*.log"),
    # Guías sueltas en raíz (la única oficial vive en CURSO-ROBOTICA-IA-COMUN)
    os.path.join(IA_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.*"),
    # CSVs residuales en raíz (la única oficial vive en PANELES_CSV/)
    os.path.join(IA_DIR, "0.PANEL_MONOGRAFICOS.csv"),
    os.path.join(IA_DIR, "*INDICE*.csv"),
    os.path.join(IA_DIR, "*indice*.csv"),
]

def main():
    print("=== LIMPIEZA DE MAQUETAS Y LOGS RESIDUALES EN CURSO-IA ===", flush=True)
    borrados = 0
    for patron in PATRONES_BORRADO:
        for fpath in glob.glob(patron):
            fname = os.path.basename(fpath)
            # Salvaguardas estrictas: NUNCA borrar los vitales
            if fname in ["index.html", "MAPA_MONOGRAFICOS.html", "CURSO_IA_UNIFICADO.csv"]:
                continue
            if "INDICE_DE_PRACTICAS_POR_ETIQUETA" in fname:
                continue

            try:
                if os.path.isfile(fpath) or os.path.islink(fpath):
                    os.remove(fpath)
                    print(f"  🗑️ Eliminado: {fname}", flush=True)
                    borrados += 1
            except Exception as e:
                print(f"  ⚠️ Error eliminando {fname}: {e}", flush=True)

    print(f"\n✨ Total de archivos fósiles/logs eliminados: {borrados}")
    print("\n✅ Elementos vitales confirmados en raíz:")
    vitales = ["index.html", "MAPA_MONOGRAFICOS.html", "INDICE_DE_PRACTICAS_POR_ETIQUETA"]
    for v in vitales:
        existe = os.path.exists(os.path.join(IA_DIR, v))
        print(f"   {'🟢' if existe else '❌'} {v}: {'PRESENTE Y ACTIVO' if existe else 'NO ENCONTRADO'}")

if __name__ == "__main__":
    main()

