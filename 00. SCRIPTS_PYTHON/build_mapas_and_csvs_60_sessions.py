#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_mapas_and_csvs_60_sessions.py
Genera:
1. MAPA_CLASE_SESION_XX.html para cada una de las 60 sesiones en su carpeta correspondiente.
2. Los 4 archivos CSV de importación para Google Classroom:
   - 1.PANEL_SESIONES_01_AL_15.csv
   - 2.PANEL_SESIONES_16_AL_30.csv
   - 3.PANEL_SESIONES_31_AL_45.csv
   - 4.PANEL_SESIONES_46_AL_60.csv
   (1 sola fila por sesión apuntando a su MAPA_CLASE_SESION_XX.html)
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

# Categorías y colores de pasos
STEP_CONFIG = {
    "TXT":   {"color": "#38bdf8", "cat": "Comunicación y Texto", "icon": "✍️"},
    "EST":   {"color": "#818cf8", "cat": "Estilo de Imagen IA", "icon": "🎨"},
    "PRAC":  {"color": "#c084fc", "cat": "Taller Práctico",     "icon": "⚡"},
    "FRAC":  {"color": "#f472b6", "cat": "Fractales & Vídeo",   "icon": "🌀"},
    "FUNC":  {"color": "#f472b6", "cat": "Funciones 3D & IA",   "icon": "📐"},
    "INT":   {"color": "#fb7185", "cat": "Mundo por Dentro",    "icon": "🏛️"},
    "FUT":   {"color": "#fb923c", "cat": "Sci-Fi & Futuro",     "icon": "🚀"},
    "NAT":   {"color": "#facc15", "cat": "Naturaleza en Acción", "icon": "🌿"},
    "ARTE":  {"color": "#a3e635", "cat": "Historia del Arte",   "icon": "🖼️"},
    "NIV":   {"color": "#4ade80", "cat": "Escalafones 101",     "icon": "📊"},
    "TRUC":  {"color": "#2dd4bf", "cat": "Trucos Cotidianos",   "icon": "💡"},
    "CUENT": {"color": "#38bdf8", "cat": "Cuentos para Nietos", "icon": "📖"},
    "MOVIL": {"color": "#60a5fa", "cat": "Salvavidas del Móvil","icon": "📱"},
    "MEM":   {"color": "#a78bfa", "cat": "Cápsula de Memoria",  "icon": "🕰️"},
    "MEC":   {"color": "#f59e0b", "cat": "Mecánica & Vídeo",    "icon": "⚙️"}
}

def clean_title_from_filename(filename):
    name, _ = os.path.splitext(filename)
    # Quitar prefijo de número y tag: ej "1. TXT-001_La IA como Consejera..."
    name = re.sub(r'^\d+\.\s*', '', name)
    name = re.sub(r'^[A-Z0-9\-_]+\s*-\s*\d+\s*', '', name)
    name = re.sub(r'^[A-Z0-9\-_]+_\d+\s*', '', name)
    name = name.replace('_', ' ').strip()
    return name

def parse_step_code(filename):
    for code in STEP_CONFIG.keys():
        if code in filename.upper():
            return code
    return "PRAC"

def generate_radial_html(session_num, session_folder, files):
    session_str = f"{session_num:02d}"
    
    # Clasificar archivos por paso
    items = []
    for f in sorted(files):
        if f.startswith('.') or f.startswith('MAPA_CLASE') or f.endswith('.html'):
            continue
        
        code = parse_step_code(f)
        cfg = STEP_CONFIG.get(code, {"color": "#38bdf8", "cat": "Práctica IA", "icon": "📌"})
        title = clean_title_from_filename(f)
        
        # Tipo de tag
        ext = os.path.splitext(f)[1].lower().replace('.', '')
        if ext == 'mp4':
            tag_class = 'tag-mp4'
            tag_text = 'MP4'
        elif ext == 'pdf':
            tag_class = 'tag-pdf'
            tag_text = 'PDF'
        elif ext in ('png', 'jpg'):
            tag_class = 'tag-png'
            tag_text = 'IMG'
        else:
            tag_class = 'tag-txt'
            tag_text = ext.upper()

        items.append({
            "filename": f,
            "title": title,
            "code": code,
            "cat": cfg["cat"],
            "color": cfg["color"],
            "tag_class": tag_class,
            "tag_text": tag_text
        })
    
    # Calcular posiciones radiales orbitales
    total = len(items)
    nodes_html = ""
    
    import math
    for i, item in enumerate(items):
        step_num = f"#{i+1:02d}"
        angle = (2 * math.pi * i) / max(total, 1) - (math.pi / 2) # Empezar en el norte (arriba)
        # Radio elíptico
        rx = 42
        ry = 38
        cx = 50
        cy = 50
        left_pct = cx + rx * math.cos(angle)
        top_pct = cy + ry * math.sin(angle)
        
        rel_href = urllib.parse.quote(item["filename"])
        
        nodes_html += f"""
            <a href="{rel_href}" target="_blank" class="planet-node" style="top: {top_pct:.1f}%; left: {left_pct:.1f}%; --p-color: {item['color']};">
                <span class="step-number">{step_num}</span>
                <div class="planet-info">
                    <span class="planet-title">{item['title']}</span>
                    <span class="planet-cat">{item['code']} • {item['cat']}</span>
                </div>
                <span class="file-tag {item['tag_class']}">{item['tag_text']}</span>
                <span class="planet-arrow">↗</span>
            </a>"""

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesión {session_num} • Cuadro de Mando Radial — Curso de IA</title>
    <style>
        :root {{
            --bg-base: #060913;
            --bg-card: rgba(15, 23, 42, 0.92);
            --border-glow: rgba(56, 189, 248, 0.4);
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
            --text-muted: #64748b;
            --primary: #38bdf8;
            --purple: #a855f7;
            --emerald: #10b981;
            --amber: #f59e0b;
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: radial-gradient(circle at 50% 40%, #0f172a 0%, #070b14 60%, #030509 100%);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
            user-select: none;
        }}

        header {{
            padding: 20px 20px 14px;
            text-align: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(12px);
            z-index: 20;
        }}
        .header-pill {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(56, 189, 248, 0.12);
            color: #7dd3fc;
            border: 1px solid rgba(56, 189, 248, 0.4);
            border-radius: 9999px;
            padding: 4px 16px;
            font-size: 0.8rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }}
        h1 {{
            font-size: 2rem;
            font-weight: 800;
            letter-spacing: -0.5px;
            background: linear-gradient(135deg, #ffffff 30%, #38bdf8 70%, #c084fc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 6px;
        }}
        .subtitle {{
            font-size: 0.9rem;
            color: var(--text-sub);
            max-width: 720px;
            margin: 0 auto;
        }}

        .radial-canvas {{
            flex: 1;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 30px 20px 70px;
            min-height: 740px;
            overflow: visible;
        }}

        .orbit-ring {{
            position: absolute;
            border-radius: 50%;
            border: 1px dashed rgba(56, 189, 248, 0.14);
            pointer-events: none;
            z-index: 1;
        }}
        .ring-1 {{ width: 440px; height: 440px; }}
        .ring-2 {{ width: 780px; height: 780px; border-color: rgba(168, 85, 247, 0.14); }}

        .sun-node {{
            width: 220px;
            height: 220px;
            border-radius: 50%;
            background: radial-gradient(circle at 35% 30%, #1e293b 0%, #090d16 85%);
            border: 3px solid var(--primary);
            box-shadow: 0 0 50px rgba(56, 189, 248, 0.4), inset 0 0 25px rgba(255, 255, 255, 0.08);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 20px;
            z-index: 10;
            position: relative;
            cursor: pointer;
            transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .sun-node:hover {{
            transform: scale(1.06);
            box-shadow: 0 0 70px rgba(56, 189, 248, 0.65);
            border-color: #7dd3fc;
        }}
        .sun-tag {{
            font-size: 0.75rem;
            font-weight: 800;
            color: var(--primary);
            letter-spacing: 1px;
            text-transform: uppercase;
        }}
        .sun-title {{
            font-size: 1.25rem;
            font-weight: 800;
            color: #fff;
            margin: 6px 0 4px;
            line-height: 1.2;
        }}
        .sun-desc {{
            font-size: 0.75rem;
            color: var(--text-sub);
        }}

        .planets-orbit {{
            position: absolute;
            width: 100%;
            height: 100%;
            max-width: 1160px;
            max-height: 820px;
            z-index: 8;
            pointer-events: none;
        }}

        .planet-node {{
            position: absolute;
            pointer-events: auto;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 10px;
            background: var(--bg-card);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 14px;
            padding: 8px 14px;
            color: var(--text-main);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(12px);
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
            max-width: 270px;
            transform: translate(-50%, -50%);
        }}
        .planet-node:hover {{
            transform: translate(-50%, -50%) scale(1.08);
            border-color: var(--p-color, var(--primary));
            box-shadow: 0 0 25px var(--p-color, var(--primary));
            z-index: 15;
            background: rgba(30, 41, 59, 0.95);
        }}

        .step-number {{
            font-family: ui-monospace, monospace;
            font-size: 0.85rem;
            font-weight: 900;
            background: var(--p-color, var(--primary));
            color: #04060b;
            padding: 3px 8px;
            border-radius: 8px;
            flex-shrink: 0;
            letter-spacing: -0.5px;
        }}

        .planet-info {{
            display: flex;
            flex-direction: column;
            min-width: 0;
        }}
        .planet-title {{
            font-size: 0.82rem;
            font-weight: 700;
            color: #f1f5f9;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            line-height: 1.25;
        }}
        .planet-cat {{
            font-size: 0.7rem;
            color: var(--text-sub);
            font-weight: 500;
        }}

        .file-tag {{
            font-family: ui-monospace, monospace;
            font-weight: 800;
            font-size: 0.7rem;
            padding: 2px 6px;
            border-radius: 4px;
            flex-shrink: 0;
        }}
        .tag-pdf {{ background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); }}
        .tag-mp4 {{ background: rgba(168, 85, 247, 0.2); color: #e9d5ff; border: 1px solid rgba(168, 85, 247, 0.4); }}
        .tag-png {{ background: rgba(56, 189, 248, 0.2); color: #7dd3fc; border: 1px solid rgba(56, 189, 248, 0.4); }}
        .tag-txt {{ background: rgba(148, 163, 184, 0.2); color: #cbd5e1; border: 1px solid rgba(148, 163, 184, 0.4); }}

        .planet-arrow {{
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-left: auto;
            flex-shrink: 0;
        }}
        .planet-node:hover .planet-arrow {{
            color: #fff;
        }}

        .bottom-guide {{
            position: fixed;
            bottom: 16px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 30px;
            padding: 8px 24px;
            display: flex;
            align-items: center;
            gap: 16px;
            backdrop-filter: blur(16px);
            z-index: 25;
            font-size: 0.82rem;
            color: var(--text-sub);
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        }}
        .guide-badge {{
            background: rgba(56, 189, 248, 0.15);
            color: var(--primary);
            padding: 3px 10px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 0.75rem;
        }}
    </style>
</head>
<body>

    <header>
        <div class="header-pill">🪐 Sesión {session_num} • Cuadro de Mando</div>
        <h1>Sesión {session_num}: Prácticas y Retos con IA</h1>
        <p class="subtitle">Pulsa en cada satélite numerado (#01 al #{total:02d}) para abrir la ficha o recurso correspondiente.</p>
    </header>

    <main class="radial-canvas">
        <div class="orbit-ring ring-1"></div>
        <div class="orbit-ring ring-2"></div>

        <div class="sun-node">
            <span class="sun-tag">Clase Individual</span>
            <h2 class="sun-title">SESIÓN {session_str}</h2>
            <p class="sun-desc">{total} Recursos Guiados</p>
        </div>

        <div class="planets-orbit">
            {nodes_html}
        </div>
    </main>

    <div class="bottom-guide">
        <span class="guide-badge">Ruta Guiada</span>
        <span>Sigue la numeración correlativa del <strong>#01 al #{total:02d}</strong></span>
        <span style="opacity: 0.4">•</span>
        <span>Publicación independiente para Google Classroom</span>
    </div>

</body>
</html>
"""
    return html

def process_all_sessions():
    sessions_data = [] # List of tuples: (session_num, tema, title, desc, url)
    
    # Listar carpetas reales en SESSIONS_DIR
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
        html_content = generate_radial_html(session_num, session_path, files)
        
        html_filename = f"MAPA_CLASE_SESION_{session_num:02d}.html"
        html_path = os.path.join(session_path, html_filename)
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Calcular URL de GitHub Pages
        rel_path = os.path.relpath(html_path, BASE_DIR)
        rel_path_nfc = unicodedata.normalize('NFC', rel_path)
        url_github = GITHUB_BASE_URL + urllib.parse.quote(rel_path_nfc)
        
        tema = f"Sesión {session_num:02d}"
        titulo = f"Mapa Interactivo: Sesión {session_num:02d} (HTML)"
        desc = f"Cuadro de mando interactivo radial de la Sesión {session_num:02d} con todos los recursos y retos guiados paso a paso."
        
        sessions_data.append((session_num, tema, titulo, desc, url_github))
        
    print(f"✅ Generados {len(sessions_data)} mapas radiales MAPA_CLASE_SESION_XX.html")

    
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
