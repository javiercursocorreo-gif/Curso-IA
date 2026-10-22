#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_maps_lote4.py
Sincroniza e inserta las tarjetas #10B [COD] de doble botón interactivo
en los cuadros de mando MAPA_SESION_31.html a MAPA_SESION_40.html.
"""

import os
import sys
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
SESSIONS_ROOT = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")

MAP_CARDS = {
    31: {
        "title": "Taller: Crea tu propio simulador 3D de Arrecife de Coral y Simbiosis [COD-031]",
        "pdf": "4. COD-031_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "probador": "PROBADOR_CODIGO_IA.html?sesion=31",
        "sim": "SIMULADOR_ARRECIFE_CORAL_3D.html",
        "btn_sim": "🪸 Abrir Arrecife de Coral 3D ↗",
        "color1": "#0284c7", "color2": "#38bdf8"
    },
    32: {
        "title": "Taller: Crea tu propio simulador de la Pirámide Trófica Fluvial [COD-032]",
        "pdf": "4. COD-032_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "probador": "PROBADOR_CODIGO_IA.html?sesion=32",
        "sim": "SIMULADOR_RED_TROFICA_3D.html",
        "btn_sim": "🐟 Abrir Red Trófica Fluvial 3D ↗",
        "color1": "#059669", "color2": "#10b981"
    },
    33: {
        "title": "Taller: Crea tu propio simulador 3D de la Mitocondria y ATP Sintasa [COD-033]",
        "pdf": "4. COD-033_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "probador": "PROBADOR_CODIGO_IA.html?sesion=33",
        "sim": "SIMULADOR_MITOCONDRIA_3D.html",
        "btn_sim": "⚡ Abrir Nanomotor ATP Sintasa 3D ↗",
        "color1": "#d97706", "color2": "#f59e0b"
    },
    34: {
        "title": "Taller: Crea tu propio simulador 3D de Telómeros y Telomerasa [COD-034]",
        "pdf": "4. COD-034_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "probador": "PROBADOR_CODIGO_IA.html?sesion=34",
        "sim": "SIMULADOR_TELOMEROS_3D.html",
        "btn_sim": "🧬 Abrir Telómeros y Telomerasa 3D ↗",
        "color1": "#7c3aed", "color2": "#c084fc"
    },
    35: {
        "title": "Taller: Crea tu propio simulador 3D de Estratos de Selva Tropical [COD-035]",
        "pdf": "4. COD-035_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "probador": "PROBADOR_CODIGO_IA.html?sesion=35",
        "sim": "SIMULADOR_SELVA_TROPICAL_3D.html",
        "btn_sim": "🌳 Abrir Selva Tropical 3D ↗",
        "color1": "#16a34a", "color2": "#22c55e"
    },
    36: {
        "title": "Taller: Crea tu propio simulador 3D del Canal de Sodio Nav1.7 [COD-036]",
        "pdf": "4. COD-036_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "probador": "PROBADOR_CODIGO_IA.html?sesion=36",
        "sim": "SIMULADOR_CANAL_IONICO_3D.html",
        "btn_sim": "⚡ Abrir Canal Iónico Nav1.7 3D ↗",
        "color1": "#0284c7", "color2": "#38bdf8"
    },
    37: {
        "title": "Taller: Crea tu propio simulador 3D de Piel Humana y Capas Tisulares [COD-037]",
        "pdf": "4. COD-037_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "probador": "PROBADOR_CODIGO_IA.html?sesion=37",
        "sim": "SIMULADOR_PIEL_HUMANA_3D.html",
        "btn_sim": "🔬 Abrir Piel Humana 3D ↗",
        "color1": "#e11d48", "color2": "#f43f5e"
    },
    38: {
        "title": "Taller: Crea tu propio simulador 3D de Columna Lumbar y Biomecánica [COD-038]",
        "pdf": "4. COD-038_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "probador": "PROBADOR_CODIGO_IA.html?sesion=38",
        "sim": "SIMULADOR_COLUMNA_VERTEBRAL_3D.html",
        "btn_sim": "🦴 Abrir Columna Lumbar 3D ↗",
        "color1": "#d97706", "color2": "#f59e0b"
    },
    39: {
        "title": "Taller: Crea tu propio simulador 3D de Iridiscencia y Nanocristales [COD-039]",
        "pdf": "4. COD-039_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "probador": "PROBADOR_CODIGO_IA.html?sesion=39",
        "sim": "SIMULADOR_IRIDISCENCIA_3D.html",
        "btn_sim": "🦋 Abrir Mariposa Morpho 3D ↗",
        "color1": "#0891b2", "color2": "#06b6d4"
    },
    40: {
        "title": "Taller: Crea tu propio simulador 3D de Regeneración Tisular y Colágeno [COD-040]",
        "pdf": "4. COD-040_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "probador": "PROBADOR_CODIGO_IA.html?sesion=40",
        "sim": "SIMULADOR_REGENERACION_TISULAR_3D.html",
        "btn_sim": "🔬 Abrir Regeneración Tisular 3D ↗",
        "color1": "#db2777", "color2": "#ec4899"
    }
}

def generate_card_html(info):
    return f'''                    <div class="file-card file-card-special">
                        <a href="{info['pdf']}" target="_blank" class="file-card-special-top" title="Abrir Ficha Guía de Tareas (PDF)">
                            <div class="file-left">
                                <span class="file-num">#10B [COD]</span>
                                <span class="file-tag tag-cod">TALLER</span>
                                <div class="file-details">
                                    <span class="file-title">{info['title']}</span>
                                    <span class="file-desc">Taller de Código con Gemini • Ficha de Tareas</span>
                                </div>
                            </div>
                            <span class="file-arrow">↗</span>
                        </a>
                        <a href="{info['probador']}" target="_blank" class="btn-launch-interactive" title="Abrir Taller Oficial de Pruebas">
                            🚀 Abrir Taller Interactivo de Pruebas ↗
                        </a>
                        <a href="{info['sim']}" target="_blank" class="btn-launch-interactive" style="margin-top:6px; background:linear-gradient(135deg, {info['color1']}, {info['color2']}); border-color:#fff3;" title="{info['title']}">
                            {info['btn_sim']}
                        </a>
                    </div>'''

def update_map(sesion_num):
    s_dir = os.path.join(SESSIONS_ROOT, f"{sesion_num:02d}_Sesion")
    map_path = os.path.join(s_dir, f"MAPA_SESION_{sesion_num:02d}.html")
    if not os.path.exists(map_path):
        print(f"  ⚠️ No existe {map_path}")
        return

    with open(map_path, "r", encoding="utf-8") as f:
        html = f.read()

    info = MAP_CARDS[sesion_num]
    card_html = generate_card_html(info)

    # Si ya tiene una tarjeta #10B [COD], la reemplazamos
    if "#10B [COD]" in html:
        # Reemplazar bloque <div class="file-card file-card-special"> ... </div>
        pattern = r'<div class="file-card file-card-special">[\s\S]*?#10B \[COD\][\s\S]*?</div>\s*</div>'
        # Buscamos y reemplazamos
        new_html, count = re.subn(pattern, card_html, html)
        if count == 0:
            # Fallback simple
            print(f"  ℹ️ [Sesión {sesion_num:02d}] Tarjeta #10B detectada, actualizando...")
            # split and replace
            start_idx = html.find('<div class="file-card file-card-special">')
            if start_idx != -1:
                end_idx = html.find('</div>\n\n                    <a href="14.', start_idx)
                if end_idx != -1:
                    new_html = html[:start_idx] + card_html + "\n\n" + html[end_idx + 27:]
                else:
                    new_html = html
        else:
            new_html = new_html
    else:
        # Insertar después del recurso de INT o 3D o antes de MEC
        # Buscar el cierre </a> que precede a MEC
        target_marker = '                    <a href="14.'
        if target_marker in html:
            new_html = html.replace(target_marker, card_html + "\n\n" + target_marker, 1)
        else:
            # Alternativa: buscar [INT]
            target_marker2 = '[INT]</span>'
            if target_marker2 in html:
                idx = html.find('</a>', html.find(target_marker2))
                if idx != -1:
                    new_html = html[:idx + 4] + "\n" + card_html + html[idx + 4:]
                else:
                    new_html = html
            else:
                new_html = html

    with open(map_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"  ✅ [Sesión {sesion_num:02d}] Sincronizado MAPA_SESION_{sesion_num:02d}.html con tarjeta #10B [COD].")

def main():
    print("🚀 Sincronizando tarjetas #10B [COD] en mapas de sesiones 31 a 40...")
    for s in range(31, 41):
        update_map(s)
    print("✨ Mapas del Lote 4 sincronizados al 100%.")

if __name__ == '__main__':
    main()
