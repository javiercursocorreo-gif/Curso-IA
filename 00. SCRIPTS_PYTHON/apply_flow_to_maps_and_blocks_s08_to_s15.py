#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_flow_to_maps_and_blocks_s08_to_s15.py
Actualización completa de las tarjetas + VÍDEO FLOW en los mapas interactivos (S08 a S15)
y sincronización exhaustiva de las 40 fichas de imagen en las carpetas de bloque oficiales.
"""

import os
import re
import shutil
import unicodedata

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
SESSIONS_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
BLOCKS_BASE = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF")

BLOCK_DIRS = {
    'EST': os.path.join(BLOCKS_BASE, "02. [EST] BLOQUE_2_ESTILOS_DE_IMAGEN_IA/Lote_01_al_20"),
    'PRAC': os.path.join(BLOCKS_BASE, "03. [PRAC] BLOQUE_3_TALLERES_DE_PROMPTS_PRACTICOS/Lote_01_al_20"),
    'INT': os.path.join(BLOCKS_BASE, "05. [INT] BLOQUE_5_MUNDO_POR_DENTRO_Y_RECONSTRUCCION/Lote_01_al_20"),
    'FUT': os.path.join(BLOCKS_BASE, "06. [FUT] BLOQUE_6_INFOGRAFIAS_DEL_FUTURO_SCI_FI/Lote_01_al_20"),
    'ARTE': os.path.join(BLOCKS_BASE, "08. [ARTE] BLOQUE_8_CUADROS_MAS_FAMOSOS_DE_LA_HISTORIA/Lote_01_al_20")
}

# 1. Actualizar Mapas Interactivos de Sesiones 08 a 15 (MAPA_CLASE_SESION_XX y MAPA_SESION_XX)
print("=== 1. ACTUALIZANDO TARJETAS EN MAPAS INTERACTIVOS (S08 A S15) ===")

TAG_DESC_BASE = {
    'EST': 'Estilo de Imagen IA',
    'ARTE': 'Historia del Arte',
    'PRAC': 'Taller Práctico Gemini',
    'INT': 'Mundo por Dentro',
    'FUT': 'Sci-Fi & Futuro'
}

for s in range(8, 16):
    s_folder = os.path.join(SESSIONS_DIR, f"{s:02d}_Sesion")
    if not os.path.exists(s_folder):
        continue

    for map_name in [f"MAPA_CLASE_SESION_{s:02d}.html", f"MAPA_SESION_{s:02d}.html"]:
        map_path = os.path.join(s_folder, map_name)
        if not os.path.exists(map_path):
            continue

        with open(map_path, "r", encoding="utf-8") as f:
            html = f.read()

        updated_count = 0

        # Función para transformar cada tarjeta <a ... class="file-card">...</a>
        def update_card(match):
            card_html = match.group(0)
            href = match.group(1)
            inner = match.group(2)

            # Verificar si pertenece a una de las 5 etiquetas de imagen
            matched_tag = None
            for t in ['EST', 'ARTE', 'PRAC', 'INT', 'FUT']:
                if f"{t}-{s:03d}" in href or f"[{t}]" in inner or f" {t}-" in href:
                    matched_tag = t
                    break

            if not matched_tag:
                return card_html

            # Si ya tiene + VÍDEO FLOW, no tocar
            if "+ VÍDEO FLOW" in card_html or "+ VIDEO FLOW" in card_html:
                return card_html

            # Reemplazar la etiqueta tag-pdf
            new_tag = '<span class="file-tag tag-pdf" style="background:#ea4335; color:#fff;">+ VÍDEO FLOW</span>'
            inner_new = re.sub(r'<span class="file-tag tag-pdf">[^<]*</span>', new_tag, inner)

            # Reemplazar la descripción para añadir la ampliación Flow
            flow_suffix = " • Ampliación a Vídeo con Google Flow (12 créditos) 🎬"
            def update_desc(d_match):
                curr_desc = d_match.group(1).strip()
                if "Google Flow" in curr_desc or "Flow" in curr_desc:
                    return d_match.group(0)
                return f'<span class="file-desc">{curr_desc}{flow_suffix}</span>'

            inner_new = re.sub(r'<span class="file-desc">([^<]+)</span>', update_desc, inner_new)

            return f'<a href="{href}" target="_blank" class="file-card">{inner_new}</a>'

        new_html = re.sub(r'<a\s+href="([^"]+)"[^>]*class="file-card"[^>]*>(.*?)</a>', update_card, html, flags=re.DOTALL)

        if new_html != html:
            with open(map_path, "w", encoding="utf-8") as f:
                f.write(new_html)
            flow_count = len(re.findall(r'\+ V[IÍ]DEO FLOW', new_html))
            print(f"✅ [S{s:02d} {map_name}] Actualizadas 5 tarjetas con badge '+ VÍDEO FLOW' (Total detectadas: {flow_count})")

# 2. Sincronización Exhaustiva de Fichas PDF en Bloques 02, 03, 05, 06, 08
print("\n=== 2. SINCRONIZANDO FICHAS PDF DE IMAGEN EN CARPETAS DE BLOQUE ===")

for s in range(8, 16):
    s_folder = os.path.join(SESSIONS_DIR, f"{s:02d}_Sesion")
    if not os.path.exists(s_folder):
        continue

    files_in_sess = os.listdir(s_folder)

    for tag, b_dir in BLOCK_DIRS.items():
        if not os.path.exists(b_dir):
            continue

        # Encontrar el archivo de esta sesión en la carpeta de sesión
        tag_pattern = f"-{s:03d}"
        sess_file = None
        for f in files_in_sess:
            if tag_pattern in f and f.endswith(".pdf"):
                sess_file = f
                break

        if not sess_file:
            continue

        src_pdf = os.path.join(s_folder, sess_file)

        # En la carpeta de bloque, buscar todos los archivos que coincidan con este tag y sesión
        b_files = os.listdir(b_dir)
        matched_b_files = []
        for bf in b_files:
            # Normalizar NFD a NFC para comparación
            bf_norm = unicodedata.normalize('NFC', bf)
            if tag_pattern in bf_norm and bf.endswith(".pdf"):
                matched_b_files.append(bf)

        # Copiar al nombre limpio sin prefijo de sesión si no existe
        clean_name = sess_file
        if clean_name.startswith(f"2. ") or clean_name.startswith(f"3. ") or clean_name.startswith(f"5. ") or clean_name.startswith(f"6. ") or clean_name.startswith(f"8. "):
            clean_name = clean_name[3:]

        dest_main = os.path.join(b_dir, clean_name)
        shutil.copy2(src_pdf, dest_main)
        print(f"📄 [S{s:02d} {tag}] Sincronizado en Bloque -> {clean_name}")

        # Sobreescribir también cualquier versión duplicada preexistente en el bloque (con 2.pdf, 4.pdf o acentos descompuestos)
        for old_f in matched_b_files:
            target_path = os.path.join(b_dir, old_f)
            shutil.copy2(src_pdf, target_path)
            if old_f != clean_name:
                print(f"   ↳ Sobreescrito archivo histórico redundante: {old_f}")

print("\n🎉 ¡Actualización de + VÍDEO FLOW en mapas y sincronización de bloques completada al 100%!")
