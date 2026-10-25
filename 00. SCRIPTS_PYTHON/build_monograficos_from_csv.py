#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_monograficos_from_csv.py
Genera:
1. Los archivos CSV oficiales separados por cada monográfico en PANELES_CSV/
   para poder publicarlos en Google Classroom UNO A UNO según el ritmo de la clase:
   - 1.PANEL_MONOGRAFICO_1_GEMINI_PC_Y_MOVIL.csv
   - 2.PANEL_MONOGRAFICO_2_GEMINI_NOTEBOOK.csv
   - 3.PANEL_MONOGRAFICO_3_CUENTO_ILUSTRADO.csv
   - 4.PANEL_MONOGRAFICO_4_MI_BIOGRAFIA.csv
   - 5.PANEL_MONOGRAFICO_5_EDUCANIETOS_IA.csv
   - 7.PANEL_MONOGRAFICO_7_MAPA_GESTION_PROYECTO.csv
   - 0.PANEL_MONOGRAFICOS.csv (completo en raíz y en PANELES_CSV/)
2. El Mapa Maestro de Monográficos (MAPA_MONOGRAFICOS.html) con los 6 monográficos oficiales vigentes.
"""

import os
import sys
import csv

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DIR_104 = os.path.join(BASE_DIR, "104 ESTILO ANIMADOS SIN PROGRAMAR")
DIR_PANELES = os.path.join(BASE_DIR, "PANELES_CSV")
ROOT_MAP = os.path.join(BASE_DIR, "MAPA_MONOGRAFICOS.html")
MAP_IN_104 = os.path.join(DIR_104, "MAPA_MONOGRAFICOS.html")
ROOT_CSV = os.path.join(BASE_DIR, "0.PANEL_MONOGRAFICOS.csv")
PANELES_CSV_TOTAL = os.path.join(DIR_PANELES, "0.PANEL_MONOGRAFICOS.csv")

os.makedirs(DIR_PANELES, exist_ok=True)

GITHUB_BASE = "https://javiercursocorreo-gif.github.io/Curso-IA/"

# CATÁLOGO OFICIAL ORIGINAL DE LOS 6 MONOGRÁFICOS
CSV_ROWS = [
    # MONOGRÁFICO 1
    {
        "num": 1,
        "file_suffix": "1_GEMINI_PC_Y_MOVIL",
        "tema": "Monográfico 1. Gemini en PC y Móvil (Instalación y Uso)",
        "titulo": "Material: Guia Visual de Gemini (PDF)",
        "desc": "Nuestra IA de cabecera: manejo en ordenador, instalación de la app oficial en el móvil, dictado por voz y fotos con la cámara.",
        "url": GITHUB_BASE + "CLASES/1.%20INTRODUCCION_GEMINI/%2A.Guia_Visual_de_Gemini.pdf",
        "type": "pdf"
    },
    # MONOGRÁFICO 2
    {
        "num": 2,
        "file_suffix": "2_GEMINI_NOTEBOOK",
        "tema": "Monográfico 2. Gemini Notebook: Tu Cuaderno Inteligente",
        "titulo": "Ejemplo de Prueba: Guia de NotebookLM (PDF)",
        "desc": "Tu biblioteca personal inteligente: cómo subir documentos familiares o recuerdos para resumir, hacer preguntas y generar guiones.",
        "url": GITHUB_BASE + "CLASES/2.%20INTRODUCCION_NLM/1.%20PRESENTACI%C3%93N%20A%20LOS%20ALUMNOS/%2A.Guia_de_NotebookLM.pdf",
        "type": "pdf"
    },
    # MONOGRÁFICO 3
    {
        "num": 3,
        "file_suffix": "3_CUENTO_ILUSTRADO",
        "tema": "Monográfico 3. Cómo Crear un Cuento Ilustrado con Gemini Notebook",
        "titulo": "Material: Paso 0 Introduccion Proyecto (PDF)",
        "desc": "Metodología en 3 pasos para crear historias inolvidables con Gemini Notebook y Gemini: el héroe, el guion por escenas y las ilustraciones para los nietos.",
        "url": GITHUB_BASE + "CLASES/3.%20COMO_HACER_UN_CUENTO_CON_NLM/%2A.%20Paso_0_Introduccion_Proyecto.pdf",
        "type": "pdf"
    },
    {
        "num": 3,
        "file_suffix": "3_CUENTO_ILUSTRADO",
        "tema": "Monográfico 3. Cómo Crear un Cuento Ilustrado con Gemini Notebook",
        "titulo": "Material: Paso 1 Crear el Cuento (PDF)",
        "desc": "Metodología en 3 pasos para crear historias inolvidables con Gemini Notebook y Gemini: el héroe, el guion por escenas y las ilustraciones para los nietos.",
        "url": GITHUB_BASE + "CLASES/3.%20COMO_HACER_UN_CUENTO_CON_NLM/%2A.%20Paso_1_Crear_el_Cuento.pdf",
        "type": "pdf"
    },
    {
        "num": 3,
        "file_suffix": "3_CUENTO_ILUSTRADO",
        "tema": "Monográfico 3. Cómo Crear un Cuento Ilustrado con Gemini Notebook",
        "titulo": "Material: Paso 2 Generador de Guion (PDF)",
        "desc": "Metodología en 3 pasos para crear historias inolvidables con Gemini Notebook y Gemini: el héroe, el guion por escenas y las ilustraciones para los nietos.",
        "url": GITHUB_BASE + "CLASES/3.%20COMO_HACER_UN_CUENTO_CON_NLM/%2A.%20Paso_2_Generador_de_Guion.pdf",
        "type": "pdf"
    },
    {
        "num": 3,
        "file_suffix": "3_CUENTO_ILUSTRADO",
        "tema": "Monográfico 3. Cómo Crear un Cuento Ilustrado con Gemini Notebook",
        "titulo": "Material: Paso 3 Ilustrador Visual (PDF)",
        "desc": "Metodología en 3 pasos para crear historias inolvidables con Gemini Notebook y Gemini: el héroe, el guion por escenas y las ilustraciones para los nietos.",
        "url": GITHUB_BASE + "CLASES/3.%20COMO_HACER_UN_CUENTO_CON_NLM/%2A.%20Paso_3_Ilustrador_Visual.pdf",
        "type": "pdf"
    },
    # MONOGRÁFICO 4
    {
        "num": 4,
        "file_suffix": "4_MI_BIOGRAFIA",
        "tema": "Monográfico 4. Mi Biografía (Escribe tus Memorias con IA)",
        "titulo": "Aplicación Web Interactiva: Mi Biografía (HTML)",
        "desc": "Escribe tus memorias familiares con ayuda de la IA: asistente interactivo para redactar vivencias, anécdotas y tu legado personal.",
        "url": GITHUB_BASE + "CLASES/4.%20Mi_Biografia/%2A.Mi_Biografia.html",
        "type": "launch"
    },
    {
        "num": 4,
        "file_suffix": "4_MI_BIOGRAFIA",
        "tema": "Monográfico 4. Mi Biografía (Escribe tus Memorias con IA)",
        "titulo": "Material: Manual de Instrucciones (PDF)",
        "desc": "Escribe tus memorias familiares con ayuda de la IA: asistente interactivo para redactar vivencias, anécdotas y tu legado personal.",
        "url": GITHUB_BASE + "CLASES/4.%20Mi_Biografia/%2A.Manual_de_Instrucciones.pdf",
        "type": "pdf"
    },
    # MONOGRÁFICO 5
    {
        "num": 5,
        "file_suffix": "5_EDUCANIETOS_IA",
        "tema": "Monográfico 5. Educanietos IA: Ayuda a tus Nietos con IA (Ciencias, Mates e Historia)",
        "titulo": "Aplicación Web Interactiva: Educanietos IA (HTML)",
        "desc": "Tu rol de mentor escolar: cómo explicar ciencias y matemáticas razonadas paso a paso y guiar las sesiones de estudio en pantalla con Gemini Notebook.",
        "url": GITHUB_BASE + "CLASES/5.%20EL_ABUELO_TUTOR_MATEMATICAS_HISTORIA/%2Aapp/index.html",
        "type": "launch"
    },
    {
        "num": 5,
        "file_suffix": "5_EDUCANIETOS_IA",
        "tema": "Monográfico 5. Educanietos IA: Ayuda a tus Nietos con IA (Ciencias, Mates e Historia)",
        "titulo": "Material: FICHA MONOGRAFICO EDUCANIETOS IA (PDF)",
        "desc": "Tu rol de mentor escolar: cómo explicar ciencias y matemáticas razonadas paso a paso y guiar las sesiones de estudio en pantalla con Gemini Notebook.",
        "url": GITHUB_BASE + "CLASES/5.%20EL_ABUELO_TUTOR_MATEMATICAS_HISTORIA/%2A.pdf",
        "type": "pdf"
    },
    {
        "num": 5,
        "file_suffix": "5_EDUCANIETOS_IA",
        "tema": "Monográfico 5. Educanietos IA: Ayuda a tus Nietos con IA (Ciencias, Mates e Historia)",
        "titulo": "Ejemplo de Prueba: APUNTES HISTORIA EJEMPLO REYES CATOLICOS (TXT)",
        "desc": "Tu rol de mentor escolar: cómo explicar ciencias y matemáticas razonadas paso a paso y guiar las sesiones de estudio en pantalla con Gemini Notebook.",
        "url": GITHUB_BASE + "CLASES/5.%20EL_ABUELO_TUTOR_MATEMATICAS_HISTORIA/EJEMPLOS_PRUEBA/%2A.APUNTES_HISTORIA_EJEMPLO_REYES_CATOLICOS.txt",
        "type": "book"
    },
    {
        "num": 5,
        "file_suffix": "5_EDUCANIETOS_IA",
        "tema": "Monográfico 5. Educanietos IA: Ayuda a tus Nietos con IA (Ciencias, Mates e Historia)",
        "titulo": "Ejemplo de Prueba: PROBLEMAS MATES GUIA EJEMPLOS (TXT)",
        "desc": "Tu rol de mentor escolar: cómo explicar ciencias y matemáticas razonadas paso a paso y guiar las sesiones de estudio en pantalla con Gemini Notebook.",
        "url": GITHUB_BASE + "CLASES/5.%20EL_ABUELO_TUTOR_MATEMATICAS_HISTORIA/EJEMPLOS_PRUEBA/%2A.PROBLEMAS_MATES_GUIA_EJEMPLOS.txt",
        "type": "book"
    },
    # MONOGRÁFICO 7
    {
        "num": 7,
        "file_suffix": "7_MAPA_GESTION_PROYECTO",
        "tema": "Monográfico 7. Mapa de Gestión del Proyecto con IA (Arquitectura y Flujo de Trabajo)",
        "titulo": "Infografía Interactiva: Mapa de Gestión del Proyecto con IA (HTML)",
        "desc": "Cómo creamos y publicamos este curso en equipo: el profesor, Antigravity en el PC, sincronización en GitHub y distribución automática en Google Classroom para los alumnos.",
        "url": GITHUB_BASE + "CLASES/7.%20MAPA_GESTION_PROYECTO_CON_IA/%2A.App_SIMULACION.html",
        "type": "launch"
    },
    {
        "num": 7,
        "file_suffix": "7_MAPA_GESTION_PROYECTO",
        "tema": "Monográfico 7. Mapa de Gestión del Proyecto con IA (Arquitectura y Flujo de Trabajo)",
        "titulo": "Infografía: Creacion de materiales con IA (PNG)",
        "desc": "Cómo creamos y publicamos este curso en equipo: el profesor, Antigravity en el PC, sincronización en GitHub y distribución automática en Google Classroom para los alumnos.",
        "url": GITHUB_BASE + "CLASES/7.%20MAPA_GESTION_PROYECTO_CON_IA/%2A.INFOGRAFIA_Creacion_de_materiales_con_IA.png",
        "type": "pdf"
    }
]

def generate_csv_files():
    """Genera exclusivamente el archivo CSV maestro único de Monográficos."""
    headers = ["ID_CURSO", "TEMA_CLASSROOM", "TITULO_MATERIAL", "DESCRIPCION_MATERIAL", "URL_GITHUB"]

    # CSV General Único (en raíz y en PANELES_CSV/)
    for path in [ROOT_CSV, PANELES_CSV_TOTAL]:
        with open(path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for r in CSV_ROWS:
                writer.writerow(["", r["tema"], r["titulo"], r["desc"], r["url"]])
    print(f"✅ CSV Maestro Único de Monográficos restaurado con éxito en:\n   - {ROOT_CSV}\n   - {PANELES_CSV_TOTAL}")

def generate_master_map():
    """Genera el Mapa Maestro MAPA_MONOGRAFICOS.html con los 6 monográficos oficiales vigentes."""
    cards_dict = {}
    for r in CSV_ROWS:
        tema = r["tema"]
        if tema not in cards_dict:
            cards_dict[tema] = {
                "num": r["num"],
                "tema": tema,
                "desc": r["desc"],
                "items": []
            }
        cards_dict[tema]["items"].append(r)

    cards_html = ""
    for tema, data in cards_dict.items():
        actions_html = ""
        for item in data["items"]:
            b_class = "btn-launch" if item["type"] == "launch" else "btn-pdf" if item["type"] == "pdf" else "btn-book"
            actions_html += f'<a href="{item["url"]}" target="_blank" class="btn-action {b_class}">{item["titulo"]} ↗</a>'

        cards_html += f"""
            <div class="mono-card">
                <div class="card-top">
                    <span class="mono-num">MONOGRÁFICO {data["num"]}</span>
                    <span class="tag-active">● DISPONIBLE EN CLASSROOM</span>
                </div>
                <h2 class="mono-title">{tema}</h2>
                <p class="mono-desc">{data["desc"]}</p>
                <div class="actions-stack">
                    {actions_html}
                </div>
            </div>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monográficos & Talleres Especiales de IA • Cuadro de Mando</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #070b14;
            --bg-card: rgba(15, 23, 42, 0.94);
            --primary: #38bdf8;
            --emerald: #34d399;
            --amber: #fbbf24;
            --purple: #8b5cf6;
            --text-main: #f8fafc;
            --text-sub: #cbd5e1;
            --text-muted: #94a3b8;
            --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; user-select: none; }}
        body {{
            font-family: var(--font-sans);
            background: radial-gradient(circle at 50% 15%, #151e3f 0%, #080c18 60%, #030509 100%);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
        }}

        header {{
            padding: 36px 24px 22px;
            text-align: center;
            background: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            position: sticky;
            top: 0;
            z-index: 50;
        }}

        .brand-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(56, 189, 248, 0.12);
            border: 1px solid rgba(56, 189, 248, 0.35);
            padding: 5px 14px;
            border-radius: 9999px;
            font-size: 0.78rem;
            font-weight: 700;
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 12px;
        }}

        h1 {{
            font-size: 2.1rem;
            font-weight: 900;
            letter-spacing: -0.03em;
            background: linear-gradient(to right, #ffffff, #93c5fd, #38bdf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 8px;
        }}

        .subtitle {{
            font-size: 0.95rem;
            color: var(--text-muted);
            max-width: 780px;
            margin: 0 auto 16px;
            line-height: 1.5;
        }}

        .controls-bar {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            margin-top: 14px;
        }}

        .search-box {{
            position: relative;
            width: 100%;
            max-width: 440px;
        }}

        .search-input {{
            width: 100%;
            background: rgba(2, 6, 23, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 10px 16px 10px 40px;
            color: #fff;
            font-size: 0.9rem;
            outline: none;
            transition: all 0.2s;
        }}

        .search-input:focus {{
            border-color: var(--primary);
            box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
        }}

        .search-icon {{
            position: absolute;
            left: 14px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 0.95rem;
            color: var(--text-muted);
            pointer-events: none;
        }}

        .canvas-container {{
            flex: 1;
            max-width: 1340px;
            width: 100%;
            margin: 0 auto;
            padding: 32px 24px 60px;
        }}

        .monos-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
            gap: 22px;
        }}

        .mono-card {{
            background: var(--bg-card);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 22px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}

        .mono-card:hover {{
            transform: translateY(-3px);
            border-color: rgba(56, 189, 248, 0.4);
            box-shadow: 0 14px 40px rgba(0, 0, 0, 0.55);
        }}

        .card-top {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
        }}

        .mono-num {{
            font-family: var(--font-mono);
            font-size: 0.72rem;
            font-weight: 800;
            color: var(--primary);
            background: rgba(56, 189, 248, 0.12);
            border: 1px solid rgba(56, 189, 248, 0.25);
            padding: 3px 8px;
            border-radius: 6px;
        }}

        .tag-active {{
            font-size: 0.7rem;
            font-weight: 700;
            color: var(--emerald);
        }}

        .mono-title {{
            font-size: 1.15rem;
            font-weight: 800;
            color: #fff;
            margin-bottom: 8px;
            line-height: 1.35;
        }}

        .mono-desc {{
            font-size: 0.86rem;
            color: var(--text-sub);
            line-height: 1.5;
            margin-bottom: 18px;
            flex-grow: 1;
        }}

        .actions-stack {{
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}

        .btn-action {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 9px 14px;
            border-radius: 10px;
            font-size: 0.82rem;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.15s;
        }}

        .btn-launch {{
            background: linear-gradient(135deg, rgba(56, 189, 248, 0.2), rgba(2, 132, 199, 0.3));
            border: 1px solid rgba(56, 189, 248, 0.4);
            color: #7dd3fc;
        }}
        .btn-launch:hover {{
            background: rgba(56, 189, 248, 0.35);
            color: #fff;
            transform: translateX(2px);
        }}

        .btn-pdf {{
            background: rgba(239, 68, 68, 0.12);
            border: 1px solid rgba(239, 68, 68, 0.3);
            color: #fca5a5;
        }}
        .btn-pdf:hover {{
            background: rgba(239, 68, 68, 0.25);
            color: #fff;
            transform: translateX(2px);
        }}

        .btn-book {{
            background: rgba(251, 191, 36, 0.12);
            border: 1px solid rgba(251, 191, 36, 0.3);
            color: #fde68a;
        }}
        .btn-book:hover {{
            background: rgba(251, 191, 36, 0.25);
            color: #fff;
            transform: translateX(2px);
        }}

        footer {{
            text-align: center;
            padding: 24px;
            font-size: 0.8rem;
            color: var(--text-muted);
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            background: rgba(2, 6, 23, 0.9);
        }}
    </style>
</head>
<body>
    <header>
        <div class="brand-badge">CATÁLOGO OFICIAL • GOOGLE CLASSROOM & GITHUB PAGES</div>
        <h1>Monográficos & Talleres Especiales de IA</h1>
        <p class="subtitle">
            Cuadernos prácticos, talleres visuales y monográficos complementarios del Curso de IA para Adultos Mayores.
            Disponibles en Google Classroom mediante ficheros CSV independientes para publicar sesión a sesión.
        </p>

        <div class="controls-bar">
            <div class="search-box">
                <span class="search-icon">🔍</span>
                <input type="text" class="search-input" id="searchInput" placeholder="Buscar monográfico por tema o palabra clave..." oninput="filterMonos()">
            </div>
        </div>
    </header>

    <div class="canvas-container">
        <div class="monos-grid" id="monosGrid">
            {cards_html}
        </div>
    </div>

    <footer>
        Curso de Inteligencia Artificial y Tecnología para Adultos Mayores (60+) • Despliegue Oficial en GitHub Pages
    </footer>

    <script>
        function filterMonos() {{
            const query = document.getElementById('searchInput').value.toLowerCase().trim();
            const cards = document.querySelectorAll('.mono-card');
            cards.forEach(card => {{
                const title = card.querySelector('.mono-title').textContent.toLowerCase();
                const desc = card.querySelector('.mono-desc').textContent.toLowerCase();
                if (!query || title.includes(query) || desc.includes(query)) {{
                    card.style.display = 'flex';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}
    </script>
</body>
</html>
"""
    with open(ROOT_MAP, "w", encoding="utf-8") as f:
        f.write(full_html)
    if os.path.exists(DIR_104):
        with open(MAP_IN_104, "w", encoding="utf-8") as f:
            f.write(full_html)
    print(f"✅ Mapa Maestro HTML generado en:\n   - {ROOT_MAP}\n   - {MAP_IN_104}")

def main():
    print("=" * 80)
    print("🚀 GENERACIÓN DE MONOGRÁFICOS OFICIALES Y CSVs PARA GOOGLE CLASSROOM")
    print("=" * 80)

    # 1. Generar los archivos CSV separados por cada monográfico + el CSV general
    generate_csv_files()

    # 2. Generar el Mapa Maestro MAPA_MONOGRAFICOS.html (6 monográficos oficiales vigentes)
    generate_master_map()

    print("\n✨ Proceso completado con éxito. CSVs listos para importar uno a uno en Classroom.")

if __name__ == "__main__":
    main()
