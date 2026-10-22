#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_mapas_cod_lote4.py
Inserta la tarjeta #10B [COD] de doble botón en los mapas de sesión:
MAPA_SESION_31.html a MAPA_SESION_40.html
en CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/XX_Sesion/
"""

import os
import re

SESSIONS_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM"

MAP_CARDS = [
    {
        "num": 31,
        "title": "Taller: Crea tu propio simulador 3D de Arrecife de Coral y Simbiosis [COD-031]",
        "sim_file": "SIMULADOR_ARRECIFE_CORAL_3D.html",
        "btn_text": "🪸 Abrir Arrecife de Coral 3D ↗",
        "btn_gradient": "linear-gradient(135deg, #0284c7, #38bdf8)",
        "btn_border": "#7dd3fc"
    },
    {
        "num": 32,
        "title": "Taller: Crea tu propio simulador 3D de la Pirámide Trófica Fluvial [COD-032]",
        "sim_file": "SIMULADOR_RED_TROFICA_3D.html",
        "btn_text": "🏞️ Abrir Pirámide Trófica 3D ↗",
        "btn_gradient": "linear-gradient(135deg, #059669, #10b981)",
        "btn_border": "#34d399"
    },
    {
        "num": 33,
        "title": "Taller: Crea tu propio simulador 3D de la Mitocondria y ATP Sintasa [COD-033]",
        "sim_file": "SIMULADOR_MITOCONDRIA_3D.html",
        "btn_text": "⚡ Abrir Nanomotor ATP Sintasa 3D ↗",
        "btn_gradient": "linear-gradient(135deg, #7c3aed, #c084fc)",
        "btn_border": "#d8b4fe"
    },
    {
        "num": 34,
        "title": "Taller: Crea tu propio simulador 3D de Telómeros y Límite de Hayflick [COD-034]",
        "sim_file": "SIMULADOR_TELOMEROS_3D.html",
        "btn_text": "🧬 Abrir Telómeros y Hayflick 3D ↗",
        "btn_gradient": "linear-gradient(135deg, #0284c7, #38bdf8)",
        "btn_border": "#7dd3fc"
    },
    {
        "num": 35,
        "title": "Taller: Crea tu propio simulador 3D de Selva Tropical y Estratos [COD-035]",
        "sim_file": "SIMULADOR_SELVA_TROPICAL_3D.html",
        "btn_text": "🌴 Abrir Bioma de Selva Tropical 3D ↗",
        "btn_gradient": "linear-gradient(135deg, #059669, #34d399)",
        "btn_border": "#6ee7b7"
    },
    {
        "num": 36,
        "title": "Taller: Crea tu propio simulador 3D de Canales Iónicos y Neurotoxina [COD-036]",
        "sim_file": "SIMULADOR_CANAL_IONICO_3D.html",
        "btn_text": "⚡ Abrir Canal de Sodio y TTX 3D ↗",
        "btn_gradient": "linear-gradient(135deg, #7c3aed, #a855f7)",
        "btn_border": "#c084fc"
    },
    {
        "num": 37,
        "title": "Taller: Crea tu propio simulador 3D de Piel Humana y Termorregulación [COD-037]",
        "sim_file": "SIMULADOR_PIEL_HUMANA_3D.html",
        "btn_text": "🩺 Abrir Piel y Termorregulación 3D ↗",
        "btn_gradient": "linear-gradient(135deg, #e11d48, #f43f5e)",
        "btn_border": "#fda4af"
    },
    {
        "num": 38,
        "title": "Taller: Crea tu propio simulador 3D de Columna y Biomecánica Lumbar [COD-038]",
        "sim_file": "SIMULADOR_COLUMNA_VERTEBRAL_3D.html",
        "btn_text": "🦴 Abrir Columna y Biomecánica 3D ↗",
        "btn_gradient": "linear-gradient(135deg, #0284c7, #38bdf8)",
        "btn_border": "#7dd3fc"
    },
    {
        "num": 39,
        "title": "Taller: Crea tu propio simulador 3D de Iridiscencia de Mariposa [COD-039]",
        "sim_file": "SIMULADOR_IRIDISCENCIA_3D.html",
        "btn_text": "🦋 Abrir Iridiscencia de Mariposa 3D ↗",
        "btn_gradient": "linear-gradient(135deg, #0284c7, #38bdf8)",
        "btn_border": "#7dd3fc"
    },
    {
        "num": 40,
        "title": "Taller: Crea tu propio simulador 3D de Regeneración Tisular [COD-040]",
        "sim_file": "SIMULADOR_REGENERACION_TISULAR_3D.html",
        "btn_text": "🔬 Abrir Regeneración Tisular 3D ↗",
        "btn_gradient": "linear-gradient(135deg, #0284c7, #38bdf8)",
        "btn_border": "#7dd3fc"
    }
]

def make_card_html(item):
    num_str = f"{item['num']:03d}"
    return f'''                    <div class="file-card file-card-special">
                        <a href="4. COD-{num_str}_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf" target="_blank" class="file-card-special-top" title="Abrir Ficha Guía de Tareas (PDF)">
                            <div class="file-left">
                                <span class="file-num">#10B [COD]</span>
                                <span class="file-tag tag-cod">TALLER</span>
                                <div class="file-details">
                                    <span class="file-title">{item['title']}</span>
                                    <span class="file-desc">Taller de Código con Gemini • Ficha de Tareas</span>
                                </div>
                            </div>
                            <span class="file-arrow">↗</span>
                        </a>
                        <a href="PROBADOR_CODIGO_IA.html?sesion={item['num']}" target="_blank" class="btn-launch-interactive" title="Abrir Taller Oficial de Pruebas">
                            🚀 Abrir Taller Interactivo de Pruebas ↗
                        </a>
                        <a href="{item['sim_file']}" target="_blank" class="btn-launch-interactive" style="margin-top:6px; background:{item['btn_gradient']}; border-color:{item['btn_border']};" title="Abrir {item['title']}">
                            {item['btn_text']}
                        </a>
                    </div>
'''

def update_map(item):
    folder = os.path.join(SESSIONS_DIR, f"{item['num']:02d}_Sesion")
    map_file = os.path.join(folder, f"MAPA_SESION_{item['num']}.html")
    if not os.path.exists(map_file):
        print(f"⚠️ No encontrado: {map_file}")
        return

    with open(map_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Si ya contiene #10B [COD], omitir o actualizar
    if "#10B [COD]" in content:
        print(f"ℹ️ Sesión {item['num']}: Tarjeta #10B [COD] ya existe.")
        return

    card_html = make_card_html(item)

    # Buscar el final de la tarjeta #10 [INT]
    # Buscar patrón: #10 [INT] ... </a>
    pattern = re.compile(r'(<span class="file-num">#10 \[INT\]</span>.*?</a>)', re.DOTALL)
    match = pattern.search(content)

    if match:
        end_idx = match.end()
        new_content = content[:end_idx] + "\n" + card_html + content[end_idx:]
        with open(map_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ Sesión {item['num']}: Tarjeta #10B [COD] insertada con éxito.")
    else:
        print(f"❌ Sesión {item['num']}: No se encontró la etiqueta #10 [INT] en {map_file}")

def main():
    print("=" * 80)
    print("🗺️ INSERTANDO TARJETA #10B [COD] EN MAPAS DE SESIÓN 31 A 40")
    print("=" * 80)
    for item in MAP_CARDS:
        update_map(item)
    print("=" * 80)

if __name__ == '__main__':
    main()

