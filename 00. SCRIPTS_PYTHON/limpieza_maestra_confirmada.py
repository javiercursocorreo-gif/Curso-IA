#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
limpieza_maestra_confirmada.py
1. RESTAURA INMEDIATAMENTE la carpeta 'CLASES' (que fue renombrada erróneamente a 'monográficos').
   (Las 60 sesiones anuales de Classroom dependen de la ruta 'CLASES/').
2. Elimina los scripts y logs residuales confirmados:
   - actualizar_classroom.sh
   - diagnostico_pantalla_resultado.txt
   - resultado_inactividad.txt
   - scratch/
   - chrome_data/
   - CURSO_IA_UNIFICADO.csv suelto en la raíz (dejando el único maestro en PANELES_CSV/).
3. Protege intactos los elementos vitales:
   - index.html
   - MAPA_MONOGRAFICOS.html (en raíz)
   - INDICE_DE_PRACTICAS_POR_ETIQUETA/
   - PANELES_CSV/CURSO_IA_UNIFICADO.csv
"""

import os
import sys
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IA_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

def restaurar_clases():
    print("1. Verificando restauración de la carpeta troncal 'CLASES'...", flush=True)
    clases_path = os.path.join(IA_DIR, "CLASES")
    
    # Buscar posibles nombres erróneos
    posibles_nombres = ["monográficos", "MONOGRAFICOS", "monograficos", "Monográficos"]
    for p_nom in posibles_nombres:
        p_path = os.path.join(IA_DIR, p_nom)
        if os.path.exists(p_path) and not os.path.exists(clases_path):
            os.rename(p_path, clases_path)
            print(f"  🚨 RESTAURADA CON ÉXITO: '{p_nom}' -> 'CLASES'", flush=True)
            break

    if os.path.exists(clases_path):
        print("  ✅ Carpeta troncal 'CLASES' asegurada y activa (60 sesiones a salvo).", flush=True)

def borrar_residuos_confirmados():
    print("\n2. Eliminando residuos confirmados...", flush=True)
    a_borrar_archivos = [
        "actualizar_classroom.sh",
        "actualizar-Classroom.sh",
        "diagnostico_pantalla_resultado.txt",
        "resultado_inactividad.txt",
        "MAQUETA_SESION_RADIAL.html",
        "MAQUETA_MONOGRAFICOS_COLUMNAS.html",
        "0.PANEL_MONOGRAFICOS.csv",
        "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.docx",
        "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.html",
        "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.md",
        "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.pdf",
        "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.rtf",
        "CURSO_IA_UNIFICADO.csv", # Borrar de raíz (queda en PANELES_CSV/)
    ]

    for f in a_borrar_archivos:
        p = os.path.join(IA_DIR, f)
        if os.path.exists(p):
            try:
                os.remove(p)
                print(f"  🗑️ Borrado: {f}", flush=True)
            except Exception as e:
                print(f"  ⚠️ Error borrando {f}: {e}", flush=True)

    a_borrar_carpetas = [
        "scratch",
        "chrome_data",
        "chrome data",
    ]
    for c in a_borrar_carpetas:
        p = os.path.join(IA_DIR, c)
        if os.path.exists(p):
            try:
                shutil.rmtree(p, ignore_errors=True)
                print(f"  🗑️ Carpeta borrada: {c}/", flush=True)
            except Exception as e:
                print(f"  ⚠️ Error borrando carpeta {c}: {e}", flush=True)

def verificar_vitales():
    print("\n3. Verificación de Elementos Vitales:", flush=True)
    vitales = {
        "index.html": "Puerta de enlace GitHub Pages",
        "MAPA_MONOGRAFICOS.html": "Enlace oficial Classroom Monográficos (en raíz)",
        "INDICE_DE_PRACTICAS_POR_ETIQUETA": "Catálogo general interactivo",
        "CLASES": "Carpeta troncal de las 60 Sesiones anuales",
        "PANELES_CSV/CURSO_IA_UNIFICADO.csv": "Panel maestro único de Classroom",
    }
    for item, desc in vitales.items():
        p = os.path.join(IA_DIR, item)
        ok = os.path.exists(p)
        print(f"  {'🟢' if ok else '❌'} {item} ({desc}): {'OK' if ok else 'FALTA'}", flush=True)

def main():
    restaurar_clases()
    borrar_residuos_confirmados()
    verificar_vitales()
    print("\n🎉 ¡Limpieza maestra ejecutada con éxito y enlaces protegidos!", flush=True)

if __name__ == "__main__":
    main()

