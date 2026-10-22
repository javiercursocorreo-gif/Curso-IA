#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_mapas_lote3_cod.py
Sincroniza los mapas interactivos de las sesiones 21 a 30 (LOTE 3)
insertando la tarjeta unificada #10B [COD] de doble acción
(Ficha de Tareas PDF + Probador de Código + Simulador 3D Oficial).
"""

import os
import re

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM"

SESSIONS_CONFIG = {
    21: {
        "title": "Taller: Crea tu propio simulador 3D de la Escala Cósmica [COD-021]",
        "pdf": "4. COD-021_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "sim_file": "SIMULADOR_ESCALA_UNIVERSO_3D.html",
        "btn_text": "🌌 Abrir Escala Cósmica 3D ↗",
        "title_attr": "Abrir Simulador 3D Escala Cósmica"
    },
    22: {
        "title": "Taller: Crea tu propio simulador 3D de la Esfera de Dyson [COD-022]",
        "pdf": "4. COD-022_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "sim_file": "SIMULADOR_ESFERA_DYSON_3D.html",
        "btn_text": "☀️ Abrir Esfera Dyson 3D ↗",
        "title_attr": "Abrir Simulador 3D Esfera Dyson"
    },
    23: {
        "title": "Taller: Crea tu propio simulador 3D de Termodinámica Molecular [COD-023]",
        "pdf": "4. COD-023_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "sim_file": "SIMULADOR_TERMODINAMICA_3D.html",
        "btn_text": "🔥 Abrir Termodinámica 3D ↗",
        "title_attr": "Abrir Simulador 3D Termodinámica Molecular"
    },
    24: {
        "title": "Taller: Crea tu propio simulador 3D de las 11 Dimensiones [COD-024]",
        "pdf": "4. COD-024_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "sim_file": "SIMULADOR_11_DIMENSIONES_3D.html",
        "btn_text": "🌀 Abrir 11 Dimensiones 3D ↗",
        "title_attr": "Abrir Simulador 3D 11 Dimensiones"
    },
    25: {
        "title": "Taller: Crea tu propio simulador 3D de la Relatividad Especial [COD-025]",
        "pdf": "4. COD-025_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "sim_file": "SIMULADOR_RELATIVIDAD_3D.html",
        "btn_text": "⚡ Abrir Relatividad 3D ↗",
        "title_attr": "Abrir Simulador 3D Relatividad Especial"
    },
    26: {
        "title": "Taller: Crea tu propio simulador 3D de un Agujero Negro [COD-026]",
        "pdf": "4. COD-026_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "sim_file": "SIMULADOR_AGUJERO_NEGRO_3D.html",
        "btn_text": "🕳️ Abrir Agujero Negro 3D ↗",
        "title_attr": "Abrir Simulador 3D Agujero Negro"
    },
    27: {
        "title": "Taller: Crea tu propio simulador 3D del Átomo y Orbitales [COD-027]",
        "pdf": "4. COD-027_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "sim_file": "SIMULADOR_ATOMO_CUANTICO_3D.html",
        "btn_text": "⚛️ Abrir Átomo Cuántico 3D ↗",
        "title_attr": "Abrir Simulador 3D Átomo Cuántico"
    },
    28: {
        "title": "Taller: Crea tu propio simulador 3D de la Tabla Periódica & Enlaces [COD-028]",
        "pdf": "4. COD-028_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "sim_file": "SIMULADOR_TABLA_PERIODICA_3D.html",
        "btn_text": "🧪 Abrir Tabla Periódica 3D ↗",
        "title_attr": "Abrir Simulador 3D Tabla Periódica"
    },
    29: {
        "title": "Taller: Crea tu propio simulador 3D de la Doble Rendija Cuántica [COD-029]",
        "pdf": "4. COD-029_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "sim_file": "SIMULADOR_DOBLE_RENDIJA_3D.html",
        "btn_text": "🔬 Abrir Doble Rendija 3D ↗",
        "title_attr": "Abrir Simulador 3D Doble Rendija"
    },
    30: {
        "title": "Taller: Crea tu propio simulador 3D de Computación Cuántica y Qubits [COD-030]",
        "pdf": "4. COD-030_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf",
        "sim_file": "SIMULADOR_COMPUTACION_CUANTICA_3D.html",
        "btn_text": "💻 Abrir Computador Cuántico 3D ↗",
        "title_attr": "Abrir Simulador 3D Computador Cuántico"
    }
}

def update_map(session_num, cfg):
    map_path = os.path.join(BASE_DIR, f"{session_num:02d}_Sesion", f"MAPA_SESION_{session_num:02d}.html")
    if not os.path.exists(map_path):
        print(f"⚠️ Mapa no encontrado: {map_path}")
        return False

    with open(map_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Si ya contiene #10B [COD], omitir
    if "#10B [COD]" in content:
        print(f"ℹ️ Sesión {session_num:02d}: Tarjeta #10B [COD] ya presente.")
        return True

    # Card template
    card_html = f'''                    <div class="file-card file-card-special">
                        <a href="{cfg['pdf']}" target="_blank" class="file-card-special-top" title="Abrir Ficha Guía de Tareas (PDF)">
                            <div class="file-left">
                                <span class="file-num">#10B [COD]</span>
                                <span class="file-tag tag-cod">TALLER</span>
                                <div class="file-details">
                                    <span class="file-title">{cfg['title']}</span>
                                    <span class="file-desc">Taller de Código con Gemini • Ficha de Tareas</span>
                                </div>
                            </div>
                            <span class="file-arrow">↗</span>
                        </a>
                        <a href="PROBADOR_CODIGO_IA.html?sesion={session_num:02d}" target="_blank" class="btn-launch-interactive" title="Abrir Taller Oficial de Pruebas">
                            🚀 Abrir Taller Interactivo de Pruebas ↗
                        </a>
                        <a href="{cfg['sim_file']}" target="_blank" class="btn-launch-interactive" style="margin-top:6px; background:linear-gradient(135deg, #0284c7, #38bdf8); border-color:#7dd3fc;" title="{cfg['title_attr']}">
                            {cfg['btn_text']}
                        </a>
                    </div>
'''

    # Localizar el final de la tarjeta #10 [INT]
    # Busca la tarjeta con #10 [INT] y su cierre </a>
    pattern_int = re.compile(r'(<span class="file-num">#10 \[INT\]</span>.*?</a>)', re.DOTALL)
    match = pattern_int.search(content)

    if not match:
        print(f"❌ No se pudo localizar la tarjeta #10 [INT] en Sesión {session_num:02d}")
        return False

    end_pos = match.end()
    # Insertar justo después
    new_content = content[:end_pos] + "\n" + card_html + content[end_pos:]

    # Actualizar contador de recursos en la columna 2 si dice 6 recursos -> 7 recursos
    new_content = re.sub(
        r'(<h2 class="branch-title">🔬 Ciencia, Naturaleza, Ingeniería & Futuro</h2>.*?<span class="branch-count">)6 recursos(</span>)',
        r'\g<1>7 recursos\g<2>',
        new_content,
        flags=re.DOTALL
    )

    with open(map_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ Sesión {session_num:02d}: Tarjeta #10B [COD] insertada con éxito.")
    return True

def main():
    print("=" * 80)
    print("🧭 ACTUALIZANDO MAPAS DIDÁCTICOS LOTE 3 [COD] (SESIONES 21 A 30)")
    print("=" * 80)
    success = 0
    for s_num in range(21, 31):
        if update_map(s_num, SESSIONS_CONFIG[s_num]):
            success += 1
    print("=" * 80)
    print(f"📊 {success}/10 mapas didácticos actualizados y sincronizados con #10B [COD].")
    print("=" * 80)

if __name__ == '__main__':
    main()

