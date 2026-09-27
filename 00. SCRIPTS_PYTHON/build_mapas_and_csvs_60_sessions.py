#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_mapas_and_csvs_60_sessions.py
Genera:
1. MAPA_CLASE_SESION_XX.html para cada una de las 60 sesiones en formato de 2 o 3 COLUMNAS
   (siguiendo el diseño unificado de los Monográficos: Fases por columnas y tarjetas interactivas).
2. Los 4 archivos CSV de importación para Google Classroom:
   - 1.PANEL_SESIONES_01_AL_15.csv
   - 2.PANEL_SESIONES_16_AL_30.csv
   - 3.PANEL_SESIONES_31_AL_45.csv
   - 4.PANEL_SESIONES_46_AL_60.csv
   (1 sola fila por sesión apuntando al Mapa Interactivo de la sesión)
"""

import os
import re
import csv
import urllib.parse
import unicodedata

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
SESSIONS_DIR = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")
CSV_DIR = os.path.join(BASE_DIR, "PANELES_CSV")
GITHUB_BASE_URL = "https://javiercursocorreo-gif.github.io/Curso-IA/"

# Configuración de pasos, colores y columnas
STEP_CONFIG = {
    "TXT":   {"color": "#38bdf8", "cat": "Paso 1 • Prompts y Texto",        "icon": "✍️", "col": 1, "order": 1},
    "EST":   {"color": "#818cf8", "cat": "Paso 2 • Estilo de Imagen IA",    "icon": "🎨", "col": 1, "order": 2},
    "PRAC":  {"color": "#c084fc", "cat": "Paso 3 • Taller Práctico Gemini",  "icon": "⚡", "col": 1, "order": 3},
    "FRAC":  {"color": "#f472b6", "cat": "Paso 4 • Fractal & Vídeo HD",     "icon": "🌀", "col": 2, "order": 4},
    "FUNC":  {"color": "#f472b6", "cat": "Paso 4 • Función 3D & IA",        "icon": "📐", "col": 2, "order": 4},
    "INT":   {"color": "#fb7185", "cat": "Paso 5 • Mundo por Dentro",       "icon": "🏛️", "col": 2, "order": 5},
    "FUT":   {"color": "#fb923c", "cat": "Paso 6 • Sci-Fi & Futuro",        "icon": "🚀", "col": 2, "order": 6},
    "NAT":   {"color": "#facc15", "cat": "Paso 7 • Naturaleza Fascinante",  "icon": "🌿", "col": 2, "order": 7},
    "AVES":  {"color": "#facc15", "cat": "Paso 7 • Naturaleza Fascinante",  "icon": "🦅", "col": 2, "order": 7},
    "ARTE":  {"color": "#a3e635", "cat": "Paso 8 • Historia del Arte",      "icon": "🖼️", "col": 2, "order": 8},
    "NIV":   {"color": "#4ade80", "cat": "Paso 9 • Escalafones y Niveles",  "icon": "📊", "col": 3, "order": 9},
    "TRUC":  {"color": "#2dd4bf", "cat": "Paso 10 • Trucos Cotidianos",     "icon": "💡", "col": 3, "order": 10},
    "MOVIL": {"color": "#60a5fa", "cat": "Paso 11 • Salvavidas del Móvil",  "icon": "📱", "col": 3, "order": 11},
    "MEM":   {"color": "#a78bfa", "cat": "Paso 12 • Cápsula de Memoria",   "icon": "🕰️", "col": 3, "order": 12},
    "MEC":   {"color": "#f59e0b", "cat": "Paso 12 • Mecánica & Vídeo",     "icon": "⚙️", "col": 3, "order": 12},
    "CUENT": {"color": "#ec4899", "cat": "Paso 13 • Cuentos Ilustrados",    "icon": "📖", "col": 3, "order": 99}
}

COLUMNS_CONFIG = [
    {
        "col_id": 1,
        "badge": "FASE 1",
        "title": "Taller Creativo & Visual",
        "desc": "Prompts de texto, estilos de imagen y taller práctico directo con IA",
        "color": "#38bdf8",
        "icon": "🎨"
    },
    {
        "col_id": 2,
        "badge": "FASE 2",
        "title": "Ciencia, Arte & Futuro",
        "desc": "Fractales y biomimética, cortes transversales, sci-fi, naturaleza y pinacoteca",
        "color": "#fb7185",
        "icon": "🏛️"
    },
    {
        "col_id": 3,
        "badge": "FASE 3",
        "title": "Vida Práctica, Memoria & Cuentos",
        "desc": "Escalafones, trucos cotidianos, móvil, recuerdos y proyecto final de cómic con IA",
        "color": "#34d399",
        "icon": "💡"
    }
]

def clean_title_from_filename(filename):
    name, _ = os.path.splitext(filename)
    if 'CUENT' in filename:
        m_step = re.search(r'Paso_([0-3])(?:_|\s*)(.*)', name)
        if m_step:
            step_num = m_step.group(1)
            rest = m_step.group(2).replace('_', ' ').strip()
            rest = re.sub(r'\s+', ' ', rest)
            if step_num == '0':
                return 'Paso 0 • Proyecto Cómic Ilustrado (Introducción)'
            elif step_num == '1':
                return f'Paso 1 • Crear el Cuento: {rest}'
            elif step_num == '2':
                return f'Paso 2 • Guión del Cómic: {rest}'
            elif step_num == '3':
                return f'Paso 3 • Ilustrador Visual: {rest}'
    name = re.sub(r'^\d+\.\s*', '', name)
    name = re.sub(r'^[A-Z0-9\-_]+\s*-\s*\d+\s*', '', name)
    name = re.sub(r'^[A-Z0-9\-_]+_\d+\s*', '', name)
    name = name.replace('_', ' ').strip()
    name = re.sub(r'\s+', ' ', name)
    return name

def parse_step_code(filename):
    f_up = filename.upper()
    for code in STEP_CONFIG.keys():
        if f"{code}-" in f_up or f"_{code}_" in f_up or f" {code} " in f_up or f" {code}-" in f_up:
            return code
    for code in STEP_CONFIG.keys():
        if code in f_up:
            return code
    return "PRAC"

def file_sort_key(filename):
    code = parse_step_code(filename)
    if code == 'CUENT':
        if 'Paso_0' in filename:
            step_order = 0
        elif 'Paso_1' in filename:
            step_order = 1
        elif 'Paso_2' in filename:
            step_order = 2
        elif 'Paso_3' in filename:
            step_order = 3
        else:
            step_order = 4
        return (3, 99, step_order, filename.lower())
    cfg = STEP_CONFIG.get(code, {'col': 1, 'order': 99})
    col = cfg.get('col', 1)
    order = cfg.get('order', 99)
    m = re.match(r'^(\d+)\.', filename)
    num = int(m.group(1)) if m else 99
    return (col, order, num, filename.lower())

def generate_columns_html(session_num, session_folder, files):
    session_str = f"{session_num:02d}"
    
    # Filtrar archivos reales de contenido
    valid_files = [
        f for f in sorted(files, key=file_sort_key)
        if not f.startswith('.') and not f.startswith('MAPA_CLASE') and not f.endswith('.html') and not f.startswith('~$')
    ]
    
    # Clasificar archivos por columna (1, 2 o 3)
    parsed_items = []
    for f in valid_files:
        code = parse_step_code(f)
        cfg = STEP_CONFIG.get(code, {"color": "#38bdf8", "cat": "Práctica con IA", "icon": "📌", "col": 1})
        title = clean_title_from_filename(f)
        
        ext = os.path.splitext(f)[1].lower().replace('.', '')
        if ext == 'mp4':
            tag_class = 'tag-mp4'
            tag_text = 'MP4'
        elif ext == 'pdf':
            tag_class = 'tag-pdf'
            tag_text = 'PDF'
        elif ext in ('png', 'jpg', 'jpeg'):
            tag_class = 'tag-png'
            tag_text = 'IMG'
        else:
            tag_class = 'tag-txt'
            tag_text = ext.upper()
            
        parsed_items.append({
            "filename": f,
            "title": title,
            "code": code,
            "cat": cfg["cat"],
            "color": cfg["color"],
            "icon": cfg.get("icon", "📌"),
            "col": cfg.get("col", 1),
            "tag_class": tag_class,
            "tag_text": tag_text
        })
        
    total_recursos = len(parsed_items)
    
    # Asignar número correlativo general #01, #02...
    for i, it in enumerate(parsed_items, 1):
        it["step_num"] = f"#{i:02d}"

    # Agrupar en las 3 columnas
    columns_html = ""
    for col_info in COLUMNS_CONFIG:
        c_id = col_info["col_id"]
        col_items = [it for it in parsed_items if it["col"] == c_id]
        count_text = f"{len(col_items)} recursos" if len(col_items) != 1 else "1 recurso"
        
        cards_html = ""
        for it in col_items:
            rel_href = urllib.parse.quote(it["filename"])
            cards_html += f"""
                    <a href="{rel_href}" target="_blank" class="file-card">
                        <div class="file-left">
                            <span class="file-num">{it["step_num"]}</span>
                            <span class="file-tag {it["tag_class"]}">{it["tag_text"]}</span>
                            <div class="file-details">
                                <span class="file-title">{it["title"]}</span>
                                <span class="file-desc">{it["cat"]}</span>
                            </div>
                        </div>
                        <span class="file-arrow">↗</span>
                    </a>"""
                    
        columns_html += f"""
            <!-- COLUMNA {c_id} -->
            <div class="branch-column" style="--branch-color: {col_info['color']};">
                <div class="branch-header">
                    <span class="branch-badge">{col_info['badge']}</span>
                    <div>
                        <h2 class="branch-title">{col_info['icon']} {col_info['title']}</h2>
                        <p class="branch-desc">{col_info['desc']}</p>
                    </div>
                    <span class="branch-count">{count_text}</span>
                </div>
                <div class="file-stack">
                    {cards_html}
                </div>
            </div>"""

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesión {session_num} • Cuadro de Mando Didáctico — Curso de IA</title>
    <style>
        :root {{
            --bg-base: #070b14;
            --bg-card: rgba(15, 23, 42, 0.92);
            --border-glow: rgba(56, 189, 248, 0.45);
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
            --text-muted: #64748b;
            --primary: #38bdf8;
            --purple: #c084fc;
            --emerald: #34d399;
            --amber: #fbbf24;
            --rose: #fb7185;
            --cyan: #06b6d4;
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: radial-gradient(circle at 50% 20%, #151e3f 0%, #080c18 60%, #030509 100%);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
            user-select: none;
        }}

        header {{
            padding: 28px 20px 18px;
            text-align: center;
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.8) 0%, rgba(15, 23, 42, 0) 100%);
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }}
        .header-pill {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 5px 16px;
            border-radius: 9999px;
            background: rgba(56, 189, 248, 0.12);
            border: 1px solid rgba(56, 189, 248, 0.35);
            color: var(--primary);
            font-size: 0.82rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 10px;
        }}
        h1 {{
            font-size: 1.95rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            background: linear-gradient(135deg, #ffffff 40%, #94a3b8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 6px;
        }}
        p.subtitle {{
            color: var(--text-sub);
            font-size: 0.95rem;
            max-width: 720px;
            margin: 0 auto;
            line-height: 1.45;
        }}

        .mindmap-canvas {{
            flex: 1;
            padding: 28px 24px 44px;
            max-width: 1400px;
            margin: 0 auto;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        .core-node {{
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.95));
            border: 2px solid var(--border-glow);
            box-shadow: 0 0 35px rgba(56, 189, 248, 0.25), inset 0 0 15px rgba(56, 189, 248, 0.15);
            border-radius: 20px;
            padding: 16px 28px;
            text-align: center;
            margin-bottom: 28px;
            max-width: 820px;
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
        }}
        .core-badge {{
            font-family: ui-monospace, monospace;
            font-size: 1.15rem;
            font-weight: 900;
            color: #04060b;
            background: var(--primary);
            padding: 6px 14px;
            border-radius: 12px;
            letter-spacing: -0.5px;
            flex-shrink: 0;
        }}
        .core-text {{
            text-align: left;
        }}
        .core-title {{
            font-size: 1.18rem;
            font-weight: 800;
            color: #fff;
            letter-spacing: -0.01em;
        }}
        .core-desc {{
            font-size: 0.82rem;
            color: var(--text-sub);
            margin-top: 2px;
        }}

        /* DISPOSICIÓN EN 2 O 3 COLUMNAS */
        .branches-container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 24px;
            width: 100%;
        }}

        .branch-column {{
            background: var(--bg-card);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 18px;
            padding: 22px;
            display: flex;
            flex-direction: column;
            transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
        }}
        .branch-column:hover {{
            transform: translateY(-3px);
            border-color: rgba(255, 255, 255, 0.22);
            box-shadow: 0 14px 35px rgba(0, 0, 0, 0.55);
        }}

        .branch-header {{
            display: flex;
            align-items: flex-start;
            gap: 12px;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }}
        .branch-badge {{
            font-size: 0.75rem;
            font-weight: 900;
            padding: 4px 8px;
            border-radius: 6px;
            background: rgba(255, 255, 255, 0.08);
            color: var(--branch-color);
            font-family: ui-monospace, monospace;
            flex-shrink: 0;
            margin-top: 2px;
        }}
        .branch-title {{
            font-size: 1.05rem;
            font-weight: 700;
            color: #fff;
            line-height: 1.25;
        }}
        .branch-desc {{
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-top: 3px;
            line-height: 1.25;
        }}
        .branch-count {{
            margin-left: auto;
            font-size: 0.75rem;
            color: var(--text-sub);
            background: rgba(0, 0, 0, 0.4);
            padding: 3px 8px;
            border-radius: 10px;
            white-space: nowrap;
            flex-shrink: 0;
        }}

        .file-stack {{
            display: flex;
            flex-direction: column;
            gap: 11px;
            flex: 1;
        }}
        .file-card {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 12px;
            padding: 11px 14px;
            text-decoration: none;
            color: var(--text-main);
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .file-card:hover {{
            background: rgba(255, 255, 255, 0.08);
            border-color: var(--branch-color);
            transform: translateX(4px);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35);
        }}
        .file-left {{
            display: flex;
            align-items: center;
            gap: 11px;
            min-width: 0;
        }}
        .file-num {{
            font-family: ui-monospace, monospace;
            font-size: 0.8rem;
            font-weight: 800;
            color: var(--branch-color);
            background: rgba(255, 255, 255, 0.05);
            padding: 3px 6px;
            border-radius: 6px;
            flex-shrink: 0;
        }}
        .file-tag {{
            font-family: ui-monospace, monospace;
            font-weight: 800;
            font-size: 0.72rem;
            padding: 3px 6px;
            border-radius: 6px;
            flex-shrink: 0;
        }}
        .tag-pdf {{ background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); }}
        .tag-mp4 {{ background: rgba(168, 85, 247, 0.25); color: #e9d5ff; border: 1px solid rgba(168, 85, 247, 0.45); }}
        .tag-png {{ background: rgba(56, 189, 248, 0.2); color: #7dd3fc; border: 1px solid rgba(56, 189, 248, 0.4); }}
        .tag-txt {{ background: rgba(148, 163, 184, 0.2); color: #cbd5e1; border: 1px solid rgba(148, 163, 184, 0.4); }}

        .file-details {{
            display: flex;
            flex-direction: column;
            min-width: 0;
        }}
        .file-title {{
            font-size: 0.88rem;
            font-weight: 600;
            color: #f1f5f9;
            line-height: 1.3;
        }}
        .file-desc {{
            font-size: 0.74rem;
            color: var(--text-muted);
            margin-top: 2px;
            line-height: 1.2;
        }}
        .file-arrow {{
            font-size: 0.9rem;
            font-weight: 700;
            margin-left: 10px;
            color: var(--text-muted);
            flex-shrink: 0;
            transition: color 0.2s, transform 0.2s;
        }}
        .file-card:hover .file-arrow {{
            color: #fff;
            transform: translate(2px, -2px);
        }}

        .bottom-bar {{
            margin-top: 32px;
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 12px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            font-size: 0.85rem;
            color: var(--text-sub);
        }}
        .bottom-bar strong {{
            color: #fff;
        }}
    </style>
</head>
<body>

    <header>
        <div class="header-pill">🪐 Sesión {session_num} • Cuadro de Mando Didáctico</div>
        <h1>Sesión {session_num}: Prácticas y Retos con IA</h1>
        <p class="subtitle">Cuadro de mando interactivo organizado en 3 fases: Taller Creativo, Ciencia & Futuro, y Vida Práctica & Cuentos.</p>
    </header>

    <main class="mindmap-canvas">
        <div class="core-node">
            <span class="core-badge">SESIÓN {session_str}</span>
            <div class="core-text">
                <div class="core-title">Itinerario Formativo Completo • {total_recursos} Recursos Guiados</div>
                <div class="core-desc">Sigue la numeración correlativa del #01 al #{total_recursos:02d} o explora directamente la fase que prefieras.</div>
            </div>
        </div>

        <div class="branches-container">
            {columns_html}
        </div>

        <div class="bottom-bar">
            <span>🤖 <strong>Curso de Inteligencia Artificial</strong> • Sesión {session_num}</span>
            <span>Publicación unificada para Google Classroom</span>
        </div>
    </main>

</body>
</html>
"""
    return html

def process_all_sessions():
    sessions_data = [] # List of tuples: (session_num, tema, title, desc, url)
    
    all_folders = os.listdir(SESSIONS_DIR)
    
    for session_num in range(1, 61):
        prefix = f"{session_num:02d}_"
        matching = [f for f in all_folders if f.startswith(prefix)]
        if not matching:
            print(f"⚠️ Carpeta de sesión no encontrada para prefijo: {prefix}")
            continue
            
        session_folder_name = matching[0]
        session_path = os.path.join(SESSIONS_DIR, session_folder_name)
            
        files = os.listdir(session_path)
        html_content = generate_columns_html(session_num, session_path, files)
        
        html_filename = f"MAPA_SESION_{session_num:02d}.html"
        html_path = os.path.join(session_path, html_filename)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # También guardar copia como MAPA_CLASE_SESION_XX.html para enlaces previos
        legacy_path = os.path.join(session_path, f"MAPA_CLASE_SESION_{session_num:02d}.html")
        with open(legacy_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Calcular URL de GitHub Pages con el nuevo archivo para refrescar miniaturas en Classroom
        rel_path = os.path.relpath(html_path, BASE_DIR)
        url_github = GITHUB_BASE_URL + urllib.parse.quote(rel_path)
        
        tema = f"Sesión {session_num:02d}"
        titulo = f"Mapa Interactivo: Sesión {session_num:02d} (HTML)"
        desc = f"Cuadro de mando interactivo en 3 columnas de la Sesión {session_num:02d} con todos los recursos y retos guiados paso a paso."
        
        sessions_data.append((session_num, tema, titulo, desc, url_github))
        
    print(f"✅ Generados {len(sessions_data)} mapas en 3 columnas (MAPA_SESION_XX.html)")

    # Exportar los 4 CSVs por lotes
    lotes = [
        ("1.PANEL_SESIONES_01_AL_15.csv", 1, 15),
        ("2.PANEL_SESIONES_16_AL_30.csv", 16, 30),
        ("3.PANEL_SESIONES_31_AL_45.csv", 31, 45),
        ("4.PANEL_SESIONES_46_AL_60.csv", 46, 60),
    ]
    
    header = ['ID_CURSO', 'TEMA_CLASSROOM', 'TITULO_MATERIAL', 'DESCRIPCION_MATERIAL', 'URL_GITHUB']
    
    for filename, start_s, end_s in lotes:
        csv_path = os.path.join(CSV_DIR, filename)
        rows = []
        for s_num, tema, titulo, desc, url in sessions_data:
            if start_s <= s_num <= end_s:
                rows.append(['', tema, titulo, desc, url])
                
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)
            
        print(f"✅ CSV generado ({len(rows)} filas): {csv_path}")

if __name__ == "__main__":
    process_all_sessions()
