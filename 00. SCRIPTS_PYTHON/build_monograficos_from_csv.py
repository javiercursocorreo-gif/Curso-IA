#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_monograficos_from_csv.py
Genera:
1. El archivo CSV oficial 0.PANEL_MONOGRAFICOS.csv listo para importar directamente
   en Google Classroom (con todos los enlaces, títulos y descripciones ya creados).
2. El Mapa Maestro de Monográficos (MAPA_MONOGRAFICOS.html) con los 7 monográficos.
3. La Ficha Didáctica Oficial MONO-002 en PDF.
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DIR_104 = os.path.join(BASE_DIR, "104 ESTILO ANIMADOS SIN PROGRAMAR")
ROOT_MAP = os.path.join(BASE_DIR, "MAPA_MONOGRAFICOS.html")
MAP_IN_104 = os.path.join(DIR_104, "MAPA_MONOGRAFICOS.html")
OUTPUT_CSV = os.path.join(BASE_DIR, "0.PANEL_MONOGRAFICOS.csv")
OUTPUT_CSV_PANELES = os.path.join(BASE_DIR, "PANELES_CSV", "0.PANEL_MONOGRAFICOS.csv")

GITHUB_BASE = "https://javiercursocorreo-gif.github.io/Curso-IA/"

CSV_ROWS = [
    # MONOGRÁFICO 1
    {
        "tema": "Monográfico 1. Gemini en PC y Móvil (Instalación y Uso)",
        "titulo": "Material: Guia Visual de Gemini (PDF)",
        "desc": "Nuestra IA de cabecera: manejo en ordenador, instalación de la app oficial en el móvil, dictado por voz y fotos con la cámara.",
        "url": GITHUB_BASE + "CLASES/1.%20INTRODUCCION_GEMINI/%2A.Guia_Visual_de_Gemini.pdf",
        "type": "pdf"
    },
    # MONOGRÁFICO 2 (NUEVO)
    {
        "tema": "Monográfico 2. 104 Estilos Animados que puedes pedirle a la IA sin Programar",
        "titulo": "Taller Interactivo: 6 Ejercicios de Estilos Animados (HTML)",
        "desc": "Crea infografías y animaciones en movimiento con un solo prompt. Incluye 6 ejercicios de vida real para copiar y ejecutar.",
        "url": GITHUB_BASE + "104%20ESTILO%20ANIMADOS%20SIN%20PROGRAMAR/TALLER_MONOGRAFICO_02_ESTILOS_ANIMADOS.html",
        "type": "launch"
    },
    {
        "tema": "Monográfico 2. 104 Estilos Animados que puedes pedirle a la IA sin Programar",
        "titulo": "Material: Ficha Guia del Alumno MONO-002 (PDF)",
        "desc": "Metodología en 3 pasos para generar animaciones sin programar y guía completa de los 6 ejercicios prácticos de clase.",
        "url": GITHUB_BASE + "104%20ESTILO%20ANIMADOS%20SIN%20PROGRAMAR/MONO-002_104_Estilos_Animados_Sin_Programar.pdf",
        "type": "pdf"
    },
    {
        "tema": "Monográfico 2. 104 Estilos Animados que puedes pedirle a la IA sin Programar",
        "titulo": "Material: Catalogo Completo 104 Estilos con Dibujos (PDF)",
        "desc": "El catálogo de referencia de Paco Vida con los 104 estilos animados explicados con sus ilustraciones y enlaces a la galería.",
        "url": GITHUB_BASE + "104%20ESTILO%20ANIMADOS%20SIN%20PROGRAMAR/76_Estilos_Animados_Ia_Sin_Programar_DiarioVida.pdf",
        "type": "book"
    },
    # MONOGRÁFICO 3 (Antes 2)
    {
        "tema": "Monográfico 3. Gemini Notebook: Tu Cuaderno Inteligente",
        "titulo": "Ejemplo de Prueba: Guia de NotebookLM (PDF)",
        "desc": "Tu biblioteca personal inteligente: cómo subir documentos familiares o recuerdos para resumir, hacer preguntas y generar guiones.",
        "url": GITHUB_BASE + "CLASES/2.%20INTRODUCCION_NLM/1.%20PRESENTACI%C3%93N%20A%20LOS%20ALUMNOS/%2A.Guia_de_NotebookLM.pdf",
        "type": "pdf"
    },
    # MONOGRÁFICO 4 (Antes 3)
    {
        "tema": "Monográfico 4. Cómo Crear un Cuento Ilustrado con Gemini Notebook",
        "titulo": "Material: Paso 0 Introduccion Proyecto (PDF)",
        "desc": "Metodología en 3 pasos para crear historias inolvidables con Gemini Notebook y Gemini: el héroe, el guion por escenas y las ilustraciones para los nietos.",
        "url": GITHUB_BASE + "CLASES/3.%20COMO_HACER_UN_CUENTO_CON_NLM/%2A.%20Paso_0_Introduccion_Proyecto.pdf",
        "type": "pdf"
    },
    {
        "tema": "Monográfico 4. Cómo Crear un Cuento Ilustrado con Gemini Notebook",
        "titulo": "Material: Paso 1 Crear el Cuento (PDF)",
        "desc": "Metodología en 3 pasos para crear historias inolvidables con Gemini Notebook y Gemini: el héroe, el guion por escenas y las ilustraciones para los nietos.",
        "url": GITHUB_BASE + "CLASES/3.%20COMO_HACER_UN_CUENTO_CON_NLM/%2A.%20Paso_1_Crear_el_Cuento.pdf",
        "type": "pdf"
    },
    {
        "tema": "Monográfico 4. Cómo Crear un Cuento Ilustrado con Gemini Notebook",
        "titulo": "Material: Paso 2 Generador de Guion (PDF)",
        "desc": "Metodología en 3 pasos para crear historias inolvidables con Gemini Notebook y Gemini: el héroe, el guion por escenas y las ilustraciones para los nietos.",
        "url": GITHUB_BASE + "CLASES/3.%20COMO_HACER_UN_CUENTO_CON_NLM/%2A.%20Paso_2_Generador_de_Guion.pdf",
        "type": "pdf"
    },
    {
        "tema": "Monográfico 4. Cómo Crear un Cuento Ilustrado con Gemini Notebook",
        "titulo": "Material: Paso 3 Ilustrador Visual (PDF)",
        "desc": "Metodología en 3 pasos para crear historias inolvidables con Gemini Notebook y Gemini: el héroe, el guion por escenas y las ilustraciones para los nietos.",
        "url": GITHUB_BASE + "CLASES/3.%20COMO_HACER_UN_CUENTO_CON_NLM/%2A.%20Paso_3_Ilustrador_Visual.pdf",
        "type": "pdf"
    },
    # MONOGRÁFICO 5 (Antes 4)
    {
        "tema": "Monográfico 5. Mi Biografía (Escribe tus Memorias con IA)",
        "titulo": "Aplicación Web Interactiva: Mi Biografía (HTML)",
        "desc": "Escribe tus memorias familiares con ayuda de la IA: asistente interactivo para redactar vivencias, anécdotas y tu legado personal.",
        "url": GITHUB_BASE + "CLASES/4.%20Mi_Biografia/%2A.Mi_Biografia.html",
        "type": "launch"
    },
    {
        "tema": "Monográfico 5. Mi Biografía (Escribe tus Memorias con IA)",
        "titulo": "Material: Manual de Instrucciones (PDF)",
        "desc": "Escribe tus memorias familiares con ayuda de la IA: asistente interactivo para redactar vivencias, anécdotas y tu legado personal.",
        "url": GITHUB_BASE + "CLASES/4.%20Mi_Biografia/%2A.Manual_de_Instrucciones.pdf",
        "type": "pdf"
    },
    # MONOGRÁFICO 6 (Antes 5)
    {
        "tema": "Monográfico 6. Educanietos IA: Ayuda a tus Nietos con IA (Ciencias, Mates e Historia)",
        "titulo": "Aplicación Web Interactiva: Educanietos IA (HTML)",
        "desc": "Tu rol de mentor escolar: cómo explicar ciencias y matemáticas razonadas paso a paso y guiar las sesiones de estudio en pantalla con Gemini Notebook.",
        "url": GITHUB_BASE + "CLASES/5.%20EL_ABUELO_TUTOR_MATEMATICAS_HISTORIA/%2Aapp/index.html",
        "type": "launch"
    },
    {
        "tema": "Monográfico 6. Educanietos IA: Ayuda a tus Nietos con IA (Ciencias, Mates e Historia)",
        "titulo": "Material: FICHA MONOGRAFICO EDUCANIETOS IA (PDF)",
        "desc": "Tu rol de mentor escolar: cómo explicar ciencias y matemáticas razonadas paso a paso y guiar las sesiones de estudio en pantalla con Gemini Notebook.",
        "url": GITHUB_BASE + "CLASES/5.%20EL_ABUELO_TUTOR_MATEMATICAS_HISTORIA/%2A.pdf",
        "type": "pdf"
    },
    {
        "tema": "Monográfico 6. Educanietos IA: Ayuda a tus Nietos con IA (Ciencias, Mates e Historia)",
        "titulo": "Ejemplo de Prueba: APUNTES HISTORIA EJEMPLO REYES CATOLICOS (TXT)",
        "desc": "Tu rol de mentor escolar: cómo explicar ciencias y matemáticas razonadas paso a paso y guiar las sesiones de estudio en pantalla con Gemini Notebook.",
        "url": GITHUB_BASE + "CLASES/5.%20EL_ABUELO_TUTOR_MATEMATICAS_HISTORIA/EJEMPLOS_PRUEBA/%2A.APUNTES_HISTORIA_EJEMPLO_REYES_CATOLICOS.txt",
        "type": "book"
    },
    {
        "tema": "Monográfico 6. Educanietos IA: Ayuda a tus Nietos con IA (Ciencias, Mates e Historia)",
        "titulo": "Ejemplo de Prueba: PROBLEMAS MATES GUIA EJEMPLOS (TXT)",
        "desc": "Tu rol de mentor escolar: cómo explicar ciencias y matemáticas razonadas paso a paso y guiar las sesiones de estudio en pantalla con Gemini Notebook.",
        "url": GITHUB_BASE + "CLASES/5.%20EL_ABUELO_TUTOR_MATEMATICAS_HISTORIA/EJEMPLOS_PRUEBA/%2A.PROBLEMAS_MATES_GUIA_EJEMPLOS.txt",
        "type": "book"
    },
    # MONOGRÁFICO 7
    {
        "tema": "Monográfico 7. Mapa de Gestión del Proyecto con IA (Arquitectura y Flujo de Trabajo)",
        "titulo": "Infografía Interactiva: Mapa de Gestión del Proyecto con IA (HTML)",
        "desc": "Cómo creamos y publicamos este curso en equipo: el profesor, Antigravity en el PC, sincronización en GitHub y distribución automática en Google Classroom para los alumnos.",
        "url": GITHUB_BASE + "CLASES/7.%20MAPA_GESTION_PROYECTO_CON_IA/%2A.App_SIMULACION.html",
        "type": "launch"
    },
    {
        "tema": "Monográfico 7. Mapa de Gestión del Proyecto con IA (Arquitectura y Flujo de Trabajo)",
        "titulo": "Infografía: Creacion de materiales con IA (PNG)",
        "desc": "Cómo creamos y publicamos este curso en equipo: el profesor, Antigravity en el PC, sincronización en GitHub y distribución automática en Google Classroom para los alumnos.",
        "url": GITHUB_BASE + "CLASES/7.%20MAPA_GESTION_PROYECTO_CON_IA/%2A.INFOGRAFIA_Creacion_de_materiales_con_IA.png",
        "type": "pdf"
    }
]

def generate_csv_file():
    # En el modelo unificado vigente no se utilizan paneles sueltos como 0.PANEL_MONOGRAFICOS.csv.
    # El archivo maestro único es PANELES_CSV/CURSO_IA_UNIFICADO.csv.
    pass

def generate_master_map():
    # Agrupar por temas para las tarjetas
    cards_dict = {}
    for r in CSV_ROWS:
        tema = r["tema"]
        if tema not in cards_dict:
            cards_dict[tema] = {
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
                    <span class="mono-num">MONOGRÁFICO</span>
                    <span class="tag-active">● DISPONIBLE</span>
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
            padding: 32px 24px 22px;
            text-align: center;
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.85) 0%, rgba(15, 23, 42, 0) 100%);
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }}

        .header-pill {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 18px;
            border-radius: 9999px;
            background: rgba(56, 189, 248, 0.12);
            border: 1px solid rgba(56, 189, 248, 0.4);
            color: var(--primary);
            font-size: 0.82rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 12px;
        }}
        .pulse-dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--primary);
            box-shadow: 0 0 10px var(--primary);
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{ 0%, 100% {{ opacity: 1; transform: scale(1); }} 50% {{ opacity: 0.4; transform: scale(0.85); }} }}

        h1 {{
            font-size: 2.2rem;
            font-weight: 900;
            letter-spacing: -0.02em;
            background: linear-gradient(135deg, #ffffff 40%, #94a3b8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 8px;
        }}

        p.subtitle {{
            color: var(--text-sub);
            font-size: 1.05rem;
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.5;
        }}

        .controls-bar {{
            max-width: 1300px;
            margin: 24px auto 0;
            padding: 0 24px;
            width: 100%;
        }}
        .search-box {{ width: 100%; position: relative; }}
        .search-input {{
            width: 100%;
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 14px 18px 14px 46px;
            color: var(--text-main);
            font-size: 1rem;
            outline: none;
            transition: all 0.2s;
        }}
        .search-input:focus {{
            border-color: var(--primary);
            box-shadow: 0 0 16px rgba(56, 189, 248, 0.3);
        }}
        .search-icon {{
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
            font-size: 1.1rem;
        }}

        .canvas-container {{
            flex: 1;
            padding: 32px 24px 60px;
            max-width: 1300px;
            margin: 0 auto;
            width: 100%;
        }}

        .monos-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
            gap: 24px;
        }}

        .mono-card {{
            background: var(--bg-card);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 18px;
            padding: 26px;
            display: flex;
            flex-direction: column;
            gap: 16px;
            box-shadow: 0 14px 34px rgba(0, 0, 0, 0.4);
            transition: all 0.25s ease;
        }}
        .mono-card:hover {{
            transform: translateY(-4px);
            border-color: var(--primary);
            box-shadow: 0 20px 44px rgba(0, 0, 0, 0.6), 0 0 20px rgba(56, 189, 248, 0.2);
        }}

        .card-top {{
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .mono-num {{
            font-family: var(--font-mono);
            font-size: 0.85rem;
            font-weight: 800;
            padding: 4px 12px;
            border-radius: 8px;
            background: rgba(56, 189, 248, 0.15);
            color: var(--primary);
            border: 1px solid rgba(56, 189, 248, 0.35);
        }}

        .tag-active {{
            font-size: 0.75rem;
            font-weight: 800;
            padding: 4px 10px;
            border-radius: 6px;
            background: rgba(52, 211, 153, 0.15);
            color: var(--emerald);
            border: 1px solid var(--emerald);
            text-transform: uppercase;
        }}

        .mono-title {{
            font-size: 1.25rem;
            font-weight: 800;
            line-height: 1.35;
            color: var(--text-main);
        }}

        .mono-desc {{
            font-size: 0.92rem;
            color: var(--text-sub);
            line-height: 1.55;
            flex: 1;
        }}

        .actions-stack {{
            display: flex;
            flex-direction: column;
            gap: 8px;
            padding-top: 14px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
        }}

        .btn-action {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 10px 14px;
            border-radius: 10px;
            font-weight: 700;
            font-size: 0.88rem;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.2s;
            border: 1px solid transparent;
            text-align: center;
        }}
        .btn-launch {{
            background: linear-gradient(135deg, #0284c7, #0ea5e9);
            color: #ffffff;
            box-shadow: 0 4px 14px rgba(2, 132, 199, 0.4);
        }}
        .btn-launch:hover {{
            background: linear-gradient(135deg, #0369a1, #0284c7);
            box-shadow: 0 6px 20px rgba(2, 132, 199, 0.6);
            transform: translateY(-1px);
        }}

        .btn-pdf {{
            background: rgba(56, 189, 248, 0.1);
            color: var(--primary);
            border-color: rgba(56, 189, 248, 0.3);
        }}
        .btn-pdf:hover {{ background: rgba(56, 189, 248, 0.2); }}

        .btn-book {{
            background: rgba(255, 255, 255, 0.05);
            color: var(--text-sub);
            border-color: rgba(255, 255, 255, 0.1);
            font-size: 0.82rem;
        }}
        .btn-book:hover {{ background: rgba(255, 255, 255, 0.12); color: var(--text-main); }}

        footer {{
            padding: 24px;
            text-align: center;
            color: var(--text-muted);
            font-size: 0.85rem;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            background: rgba(15, 23, 42, 0.6);
        }}
    </style>
</head>
<body>

    <header>
        <div class="header-pill">
            <div class="pulse-dot"></div>
            <span>Catálogo Dinámico Permanente • 7 Monográficos Oficiales</span>
        </div>
        <h1>📚 Monográficos & Talleres Especiales de IA</h1>
        <p class="subtitle">
            Cuadernos prácticos, talleres visuales y monográficos complementarios del Curso de IA para Adultos Mayores.
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
    with open(MAP_IN_104, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"✅ Mapa Maestro HTML generado en:\n   {ROOT_MAP}\n   {MAP_IN_104}")

def main():
    print("=" * 80)
    print("🚀 GENERACIÓN DEL CSV Y MAPA OFICIAL DE MONOGRÁFICOS")
    print("=" * 80)

    # 1. Compilar PDF oficial MONO-002
    try:
        from build_pdf_mono_002 import build_mono_002_pdf
        build_mono_002_pdf()
    except Exception as e:
        print(f"  ❌ Error PDF MONO-002: {e}")

    # 2. Generar Taller 02 en 104
    taller_01 = os.path.join(DIR_104, "TALLER_MONOGRAFICO_01_ESTILOS_ANIMADOS.html")
    taller_02 = os.path.join(DIR_104, "TALLER_MONOGRAFICO_02_ESTILOS_ANIMADOS.html")
    if os.path.exists(taller_01):
        with open(taller_01, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("[MONO-001]", "[MONO-002]").replace("Monográfico 01", "Monográfico 02").replace("MONO-001_", "MONO-002_")
        with open(taller_02, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Taller 02 generado en:\n   {taller_02}")

    # 3. Generar CSV 0.PANEL_MONOGRAFICOS.csv
    generate_csv_file()

    # 4. Generar MAPA_MONOGRAFICOS.html
    generate_master_map()

    print("\n✨ CSV y Mapa Maestro listos para subir a Classroom y GitHub.")

if __name__ == "__main__":
    main()
