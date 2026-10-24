#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
borrado_directo_absoluto.py
Escanea directamente la raíz de CURSO-IA con os.listdir(),
elimina con ruta absoluta cada archivo fósil/log/maqueta identificado,
y muestra en pantalla el antes y el después con confirmación visual.
"""

import os
import sys

IA_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"

# Elementos que NUNCA se tocan
VITALES = {
    "index.html",
    "MAPA_MONOGRAFICOS.html",
    "CURSO_IA_UNIFICADO.csv",
    "CLASES",
    "00. SCRIPTS_PYTHON",
    "03_ASSETS_3D_Y_DATOS",
    "104 ESTILO ANIMADOS SIN PROGRAMAR",
    "INDICE_DE_PRACTICAS_POR_ETIQUETA",
    "PANELES_CSV",
    "README.md",
    "AGENTS.md",
    "GEMINI.md",
    ".git",
    ".gitignore",
}

# Palabras clave de fósiles para borrar en la raíz
PALABRAS_FOSILES = [
    "maqueta", "radial", "columnas", "inactividad",
    "energia", "registro", "log", "indice", "panel", "guia"
]

def purgar_raiz():
    print(f"\n📂 Analizando carpeta raíz: {IA_DIR}\n" + "="*70, flush=True)
    
    if not os.path.exists(IA_DIR):
        print(f"❌ Error: La ruta no existe: {IA_DIR}", flush=True)
        return

    todos = os.listdir(IA_DIR)
    borrados = 0

    for item in todos:
        if item in VITALES or item.startswith("."):
            continue

        item_path = os.path.join(IA_DIR, item)
        item_lower = item.lower()

        # Si coincide con alguna palabra fósil o es un log/txt de prueba
        debe_borrar = any(p in item_lower for p in PALABRAS_FOSILES) or item_lower.endswith(".log")

        if debe_borrar:
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.remove(item_path)
                    print(f"  🗑️ BORRADO CON ÉXITO: {item}", flush=True)
                    borrados += 1
                elif os.path.isdir(item_path) and item not in VITALES:
                    import shutil
                    shutil.rmtree(item_path, ignore_errors=True)
                    print(f"  🗑️ CARPETA BORRADA: {item}/", flush=True)
                    borrados += 1
            except Exception as e:
                print(f"  ⚠️ Error al borrar {item}: {e}", flush=True)

    # También asegurar la limpieza en PANELES_CSV
    paneles_dir = os.path.join(IA_DIR, "PANELES_CSV")
    if os.path.exists(paneles_dir):
        for p_item in os.listdir(paneles_dir):
            if p_item != "CURSO_IA_UNIFICADO.csv":
                p_path = os.path.join(paneles_dir, p_item)
                try:
                    if os.path.isfile(p_path) or os.path.islink(p_path):
                        os.remove(p_path)
                        print(f"  🗑️ BORRADO EN PANELES_CSV: {p_item}", flush=True)
                        borrados += 1
                    elif os.path.isdir(p_path):
                        import shutil
                        shutil.rmtree(p_path, ignore_errors=True)
                        print(f"  🗑️ CARPETA BORRADA EN PANELES_CSV: {p_item}/", flush=True)
                        borrados += 1
                except Exception as e:
                    print(f"  ⚠️ Error borrando {p_item}: {e}", flush=True)

    print("="*70, flush=True)
    print(f"🎉 Resumen: Se han eliminado {borrados} elementos fósiles.\n", flush=True)

    print("📋 CONTENIDO FINAL QUE QUEDA EN LA RAÍZ DE CURSO-IA:")
    for final_item in sorted(os.listdir(IA_DIR)):
        if final_item.startswith("."):
            continue
        print(f"   👉 {final_item}", flush=True)

if __name__ == "__main__":
    purgar_raiz()

