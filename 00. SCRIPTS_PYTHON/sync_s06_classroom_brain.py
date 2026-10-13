#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil
import html

ROOT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
S06_DIR = os.path.join(ROOT_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM", "06_Sesion")
ASSETS_DIR = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS", "03_ASSETS_3D_Y_DATOS")
MASTER_HTML_PATH = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS", "01_SIMULADORES", "06_SIMULADOR_CEREBRO_3D.html")

print("1. Copiando brain_b64.js y brain.glb a 06_Sesion (Classroom)...")
shutil.copy2(os.path.join(ASSETS_DIR, "brain_b64.js"), os.path.join(S06_DIR, "brain_b64.js"))
shutil.copy2(os.path.join(ASSETS_DIR, "brain.glb"), os.path.join(S06_DIR, "brain.glb"))

print("2. Leyendo HTML maestro de Babylon.js...")
with open(MASTER_HTML_PATH, "r", encoding="utf-8") as f:
    master_html = f.read()

# Crear versión para 06_Sesion con rutas relativas a la carpeta 06_Sesion
s06_html = master_html.replace(
    '<script src="../03_ASSETS_3D_Y_DATOS/brain_b64.js"></script>',
    '<script src="brain_b64.js"></script>\n    <script src="../../../../SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/brain_b64.js"></script>'
)

print("3. Actualizando SIMULADOR_CEREBRO_3D.html y 06_SIMULADOR_CEREBRO_3D.html en 06_Sesion...")
with open(os.path.join(S06_DIR, "SIMULADOR_CEREBRO_3D.html"), "w", encoding="utf-8") as f:
    f.write(s06_html)

with open(os.path.join(S06_DIR, "06_SIMULADOR_CEREBRO_3D.html"), "w", encoding="utf-8") as f:
    f.write(s06_html)

print("4. Actualizando PROBADOR_CODIGO_IA.html en 06_Sesion...")
probador_path = os.path.join(S06_DIR, "PROBADOR_CODIGO_IA.html")
with open(probador_path, "r", encoding="utf-8") as f:
    probador_content = f.read()

# Escapar el html para el textarea
escaped_code = html.escape(s06_html)

tag_start = '<textarea id="exampleBrainTemplate" style="display:none;">'
tag_end = '</textarea>'

start_pos = probador_content.find(tag_start)
if start_pos != -1:
    end_pos = probador_content.find(tag_end, start_pos)
    if end_pos != -1:
        probador_content = probador_content[:start_pos + len(tag_start)] + escaped_code + probador_content[end_pos:]
        with open(probador_path, "w", encoding="utf-8") as f:
            f.write(probador_content)
        print("   -> Template de Cerebro 3D actualizado con éxito en PROBADOR_CODIGO_IA.html.")
    else:
        print("   -> ADVERTENCIA: No se encontró etiqueta de cierre </textarea>.")
else:
    print("   -> ADVERTENCIA: No se encontró exampleBrainTemplate.")

print("✅ Sincronización completa con Classroom finalizada.")
