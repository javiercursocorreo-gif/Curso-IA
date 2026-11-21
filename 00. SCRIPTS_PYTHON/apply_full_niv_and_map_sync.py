#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_full_niv_and_map_sync.py
Sincronización integral y definitiva de la Etiqueta [NIV] y mapas interactivos (S05 a S15).
"""

import os
import re
import shutil
import glob

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
SESSIONS_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
BLOQUE_9_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/09. [NIV] BLOQUE_9_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20")
BLOQUE_10_DIR = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/[NIV] BLOQUE_10_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20")

# 1. Actualizar build_all_niv_s05_to_s15.py
BUILD_SCRIPT = os.path.join(BASE_DIR, "00. SCRIPTS_PYTHON/build_all_niv_s05_to_s15.py")

with open(BUILD_SCRIPT, "r", encoding="utf-8") as f:
    content = f.read()

# Fix escape_pdf_text to strip emojis cleanly
clean_escape_code = '''def escape_pdf_text(text):
    text = str(text)
    for em in ['🛡️', '🛡', '🚀', '✨', '⭐', '💡', '📌', '🎉', '📄', '⚙️', '🔧', '🧭', '🌲', '⚡', '🎬', '🎥', '🍿', '🎵', '🎹', '🎼', '🏛️', '🏛', '«', '»']:
        text = text.replace(em, '')
    text = text.replace('\\\\', '\\\\\\\\').replace('(', '\\\\(').replace(')', '\\\\)')
    replacements = {
        'á': '\\xe1', 'é': '\\xe9', 'í': '\\xed', 'ó': '\\xf3', 'ú': '\\xfa',
        'Á': '\\xc1', 'É': '\\xc9', 'Í': '\\xcd', 'Ó': '\\xd3', 'Ú': '\\xda',
        'ñ': '\\xf1', 'Ñ': '\\xd1', 'ü': '\\xfc', 'Ü': '\\xdc',
        '•': '-', '—': '-', '–': '-', 'º': 'o', 'ª': 'a',
        '¿': '\\xbf', '¡': '\\xa1', '➔': '->', '→': '->',
        '’': "'", '‘': "'", '“': '"', '”': '"'
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text'''

content = re.sub(r'def escape_pdf_text\(text\):.*?(?=def wrap_text)', lambda m: clean_escape_code + '\n\n', content, flags=re.DOTALL)

# Fix banner text removing emoji
content = content.replace("<<🛡️ Abrir", "<<Abrir")
content = content.replace("«🛡️ Abrir", "<<Abrir")

# Fix sim_file names in NIV_DATA
content = content.replace("'sim_file': 'SIMULADOR_PODER_ADQUISITIVO_CESTA_SENIORS.html'", "'sim_file': 'SIMULADOR_PODER_ADQUISITIVO_COSTE_VIDA_SENIORS.html'")
content = content.replace("'sim_file': 'SIMULADOR_PERSUASION_INFLUENCIA_MASAS_SENIORS.html'", "'sim_file': 'SIMULADOR_RADAR_PERSUASION_PUBLICIDAD_SENIORS.html'")
content = content.replace("'sim_file': 'SIMULADOR_SEGURIDAD_CIUDADANA_PREVENCION_SENIORS.html'", "'sim_file': 'SIMULADOR_SEGURIDAD_PREVENCION_SENIORS.html'")
content = content.replace("'sim_file': 'SIMULADOR_ALFABETIZACION_FINANCIERA_SENIORS.html'", "'sim_file': 'SIMULADOR_SALUD_FINANCIERA_SENIORS.html'")
content = content.replace("'sim_file': 'SIMULADOR_INTELIGENCIA_CONCIENCIA_SENIORS.html'", "'sim_file': 'SIMULADOR_INTELIGENCIA_COGNITIVA_SENIORS.html'")

# Fix render_niv_worksheet to copy to ALL locations (spaced and underscore)
render_dest_code = '''    # Sincronización exhaustiva en Bloque 9, Bloque 10 y Carpeta de Sesión
    canonical_names = {
        5: ["NIV-005_Los 5 Niveles de la Evolución del Dinero.pdf", "NIV-005_Los_5_Niveles_de_la_Evolucin_del_Dinero.pdf"],
        6: ["NIV-006_Calculadora de Poder Adquisitivo y Cesta de la Compra.pdf", "NIV-006_Calculadora_de_Poder_Adquisitivo_y_Cesta.pdf", "NIV-006_Los 6 Niveles del Poder Adquisitivo y Coste de Vida Global.pdf"],
        7: ["NIV-007_Los 5 Niveles de Automatización del Trabajo Humano.pdf", "NIV-007_Los_5_Niveles_de_Automatizacion_e_IA_en_el_Hogar.pdf", "NIV-007_Los_5_Niveles_de_Automatizacin_e_IA_en_e.pdf"],
        8: ["NIV-008_Los 6 Niveles de Persuasión e Influencia de Masas.pdf", "NIV-008_Radar_Antimanipulacin_Los_6_Niveles_de_P.pdf"],
        9: ["NIV-009_Los 5 Niveles de Seguridad Ciudadana y Prevención Urbana.pdf", "NIV-009_Semforo_de_Seguridad_Ciudadana_y_Prevenc.pdf"],
        10: ["NIV-010_Los 6 Niveles de Alfabetización Financiera Personal.pdf", "NIV-010_Los_6_Niveles_de_Alfabetizacin_y_Blindaj.pdf"],
        11: ["NIV-011_Los 7 Niveles de Inteligencia Cognitiva y Conciencia.pdf", "NIV-011_Los_7_Niveles_de_Inteligencia_Cognitiva.pdf"],
        12: ["NIV-012_Los 6 Niveles de Conciencia y Alerta Neurológica.pdf", "NIV-012_Los_6_Niveles_de_Conciencia_Ritmos_Circa.pdf"],
        13: ["NIV-013_Los 5 Niveles de la Memoria y Retención Biológica.pdf", "NIV-013_Los_5_Niveles_de_Memoria_Prctica_y_Reten.pdf"],
        14: ["NIV-014_Los 6 Niveles de Toma de Decisiones y Sesgos Cognitivos.pdf", "NIV-014_Los_6_Niveles_de_Toma_de_Decisiones_y_Fi.pdf"],
        15: ["NIV-015_Los 5 Niveles de Resiliencia y Salud Mental.pdf", "NIV-015_Los_5_Niveles_de_Resiliencia_Emocional_y.pdf"]
    }

    # Copiar a Bloque 9 y Bloque 10
    b9_dir = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/09. [NIV] BLOQUE_9_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20")
    b10_dir = os.path.join(BASE_DIR, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/[NIV] BLOQUE_10_ESCALAFONES_Y_NIVELES_CULTURA101/Lote_01_al_20")
    sess_dir = os.path.join(SESSIONS_BASE, f"{session_num:02d}_Sesion")

    for cname in canonical_names.get(session_num, []):
        for target_dir in [b9_dir, b10_dir]:
            try:
                os.makedirs(target_dir, exist_ok=True)
                shutil.copy2(output_path, os.path.join(target_dir, cname))
            except Exception as e:
                print(f"Error copiando a {target_dir}: {e}")
        
        # También en la carpeta de sesión con prefijo 9. y sin prefijo
        try:
            shutil.copy2(output_path, os.path.join(sess_dir, cname))
            if not cname.startswith("9. "):
                shutil.copy2(output_path, os.path.join(sess_dir, f"9. {cname}"))
        except Exception as e:
            pass
'''

content = re.sub(r'# Sincronización en carpetas de bloque.*?(?=\n# ===)', lambda m: render_dest_code, content, flags=re.DOTALL)

with open(BUILD_SCRIPT, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Script build_all_niv_s05_to_s15.py actualizado exitosamente.")

# Ejecutar el script actualizado
import subprocess
res = subprocess.run(["/Library/Developer/CommandLineTools/usr/bin/python3", BUILD_SCRIPT], capture_output=True, text=True)
print(res.stdout[-600:])
if res.returncode != 0:
    print("ERROR:", res.stderr)

# 2. Actualizar mapas interactivos de sesiones 08 a 15
cod_sims = {
    8: ("SIMULADOR_MOTOR_4_TIEMPOS_3D.html", "Taller: Crea tu propio simulador del motor de 4 tiempos"),
    9: ("SIMULADOR_CRANEO_TREX_3D.html", "Taller: Crea tu propio simulador del cráneo de Tiranosaurio Rex"),
    10: ("SIMULADOR_MOLAR_HUMANO_3D.html", "Taller: Crea tu propio simulador del molar humano"),
    11: ("SIMULADOR_VIOLIN_STRADIVARIUS_3D.html", "Taller: Crea tu propio simulador del violín Stradivarius"),
    12: ("SIMULADOR_NEBULOSA_HELIX_3D.html", "Taller: Explora la Nebulosa Helix de la NASA (El Ojo de Dios)"),
    13: ("SIMULADOR_ADN_GENETICO_3D.html", "Taller: Crea el modelo molecular 3D del ADN"),
    14: ("SIMULADOR_AURORAS_JUPITER_3D.html", "Taller: Simula las auroras boreales de Júpiter (Hubble)"),
    15: ("SIMULADOR_PARTENON_3D.html", "Taller: Reconstruye el Partenón 3D y la Proporción Áurea"),
}

niv_sims = {
    8: "SIMULADOR_RADAR_PERSUASION_PUBLICIDAD_SENIORS.html",
    9: "SIMULADOR_SEGURIDAD_PREVENCION_SENIORS.html",
    10: "SIMULADOR_SALUD_FINANCIERA_SENIORS.html",
    11: "SIMULADOR_INTELIGENCIA_COGNITIVA_SENIORS.html",
    12: "SIMULADOR_CONCIENCIA_ALERTA_NEUROLOGICA_SENIORS.html",
    13: "SIMULADOR_MEMORIA_RETENCION_BIOLOGICA_SENIORS.html",
    14: "SIMULADOR_TOMA_DECISIONES_SESGOS_SENIORS.html",
    15: "SIMULADOR_RESILIENCIA_SALUD_MENTAL_SENIORS.html",
}

for s in range(8, 16):
    s_dir = os.path.join(SESSIONS_DIR, f"{s:02d}_Sesion")
    
    # Purgar PROBADOR_CODIGO_IA.html
    probador_path = os.path.join(s_dir, "PROBADOR_CODIGO_IA.html")
    if os.path.exists(probador_path):
        os.remove(probador_path)
        print(f"🗑️ [S{s:02d}] Purgado PROBADOR_CODIGO_IA.html")

    # Actualizar ambos mapas: MAPA_CLASE_SESION_XX.html y MAPA_SESION_XX.html
    for map_name in [f"MAPA_CLASE_SESION_{s:02d}.html", f"MAPA_SESION_{s:02d}.html"]:
        map_path = os.path.join(s_dir, map_name)
        if not os.path.exists(map_path):
            continue
        
        with open(map_path, "r", encoding="utf-8") as f:
            map_html = f.read()
        
        # 1. Reemplazar botón de PROBADOR en [COD] por botón de BKP Oficial 3D
        cod_sim_file, _ = cod_sims[s]
        # Regex para capturar el tag <a> de PROBADOR
        map_html = re.sub(
            r'<a\s+href="PROBADOR_CODIGO_IA\.html\?sesion=\d+"[^>]*>.*?</a>',
            f'<a href="{cod_sim_file}" target="_blank" class="btn-launch-interactive" style="margin-top:6px; background:linear-gradient(135deg, #0284c7, #0369a1); border-color:#38bdf8;" title="Ver Simulador 3D (BKP)">🚀 Ver Simulador 3D (BKP) ↗</a>',
            map_html,
            flags=re.DOTALL
        )
        
        # 2. Agregar botón 2 en [NIV] si falta
        niv_sim_file = niv_sims[s]
        niv_btn_html = f'<a href="{niv_sim_file}" target="_blank" class="btn-launch-interactive" style="margin-top:6px; background:linear-gradient(135deg, #059669, #047857); border-color:#10b981;" title="Abrir Micro-Aplicación Oficial (+65)">🛡️ Abrir Micro-Aplicación Oficial BKP (HTML) ↗</a>'
        
        # Localizar el bloque NIV
        idx_niv = map_html.find('[NIV]')
        if idx_niv != -1:
            end_card = map_html.find('</div>\n                    </div>', idx_niv)
            if end_card == -1:
                end_card = map_html.find('</div>', idx_niv + 300)
            
            # Verificar si ya tiene el botón del simulador
            if niv_sim_file not in map_html[idx_niv:idx_niv+1500]:
                # Buscar el botón del PDF dentro del bloque NIV
                pdf_btn_match = re.search(r'(<a\s+href="[^"]*NIV[^"]*\.pdf"[^>]*>.*?</a>)', map_html[idx_niv:end_card+200], flags=re.DOTALL)
                if pdf_btn_match:
                    full_match = pdf_btn_match.group(1)
                    replacement = full_match + '\n                        ' + niv_btn_html
                    # Reemplazar únicamente en este fragmento
                    first_half = map_html[:idx_niv]
                    rest = map_html[idx_niv:]
                    rest = rest.replace(full_match, replacement, 1)
                    map_html = first_half + rest
                    print(f"✅ [S{s:02d} {map_name}] Botón BKP NIV inyectado con éxito.")
        
        with open(map_path, "w", encoding="utf-8") as f:
            f.write(map_html)

print("\n🎉 Sincronización completa finalizada con éxito.")
