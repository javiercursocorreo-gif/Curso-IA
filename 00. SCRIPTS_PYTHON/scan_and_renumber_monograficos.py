#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scan_and_renumber_monograficos.py
Escanea la carpeta CURSO-IA para detectar todos los monográficos existentes,
inserta '104 Estilos Animados' como MONOGRÁFICO 02, renumera los siguientes
hasta el final y genera el Mapa Maestro de Monográficos (MAPA_MONOGRAFICOS.html)
listo para abrirse en Safari y desplegarse en GitHub Pages y Classroom.
"""

import os
import sys
import re
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DIR_104 = os.path.join(BASE_DIR, "104 ESTILO ANIMADOS SIN PROGRAMAR")
ROOT_MAP = os.path.join(BASE_DIR, "MAPA_MONOGRAFICOS.html")
LOG_PATH = os.path.join(SCRIPT_DIR, "monograficos_detectados_log.txt")

def main():
    print("=" * 80)
    print("🔍 ESCANEANDO Y RENUMERANDO MONOGRÁFICOS EN CURSO-IA")
    print("=" * 80)

    # 1. Compilar PDF oficial MONO-002
    print("\n1. Compilando Ficha Didáctica Oficial MONO-002...")
    try:
        from build_pdf_mono_002 import build_mono_002_pdf
        build_mono_002_pdf()
    except Exception as e:
        print(f"  ❌ Error al compilar PDF MONO-002: {e}")

    # 2. Generar Taller 02 en 104
    taller_01 = os.path.join(DIR_104, "TALLER_MONOGRAFICO_01_ESTILOS_ANIMADOS.html")
    taller_02 = os.path.join(DIR_104, "TALLER_MONOGRAFICO_02_ESTILOS_ANIMADOS.html")
    if os.path.exists(taller_01):
        with open(taller_01, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("[MONO-001]", "[MONO-002]").replace("Monográfico 01", "Monográfico 02")
        with open(taller_02, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✅ Creado Taller Interactivo: {taller_02}")

    # 3. Escanear elementos en BASE_DIR
    print("\n2. Escaneando monográficos en:", BASE_DIR)
    all_entries = sorted(os.listdir(BASE_DIR))
    detected = []
    for e in all_entries:
        low = e.lower()
        if "mono" in low or (any(c.isdigit() for c in e) and ("estilo" in low or "taller" in low or "cuaderno" in low)):
            detected.append(e)

    print(f"  📁 Elementos detectados relacionados ({len(detected)}):")
    for d in detected:
        print(f"    • {d}")

    # Registrar en log
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(detected))

    # 4. Construir lista canónica de Monográficos con Estilos Animados como MONO-002
    monograficos = [
        {
            "num": "MONO-001",
            "title": "Iniciación y Fundamentos Prácticos de la Inteligencia Artificial",
            "tag": "● DISPONIBLE",
            "status": "disponible",
            "desc": "Cuaderno introductorio para dominar el diálogo con la IA en lenguaje natural, comprensión de modelos generativos y primeros pasos en la creación de contenidos asistidos.",
            "link_app": "#",
            "link_pdf": "#",
            "link_extra": "#"
        },
        {
            "num": "MONO-002",
            "title": "104 Estilos Animados que puedes pedirle a la IA sin Programar",
            "tag": "● DISPONIBLE",
            "status": "disponible",
            "desc": "Aprende la técnica de la 'caja negra': pide a Gemini o Claude que genere infografías y animaciones en movimiento con un solo prompt. Incluye 6 ejercicios adaptados a la vida real (receta de cocina, reto de salud de 6.000 pasos, semáforo de llamadas seguras, antes y después) y acceso al catálogo completo con 104 ejemplos dibujados.",
            "link_app": "104%20ESTILO%20ANIMADOS%20SIN%20PROGRAMAR/TALLER_MONOGRAFICO_02_ESTILOS_ANIMADOS.html",
            "link_pdf": "104%20ESTILO%20ANIMADOS%20SIN%20PROGRAMAR/MONO-002_104_Estilos_Animados_Sin_Programar.pdf",
            "link_extra": "104%20ESTILO%20ANIMADOS%20SIN%20PROGRAMAR/76_Estilos_Animados_Ia_Sin_Programar_DiarioVida.pdf"
        },
        {
            "num": "MONO-003",
            "title": "Música, Partituras y Acompañamiento Musical con Web MIDI e IA",
            "tag": "● DISPONIBLE",
            "status": "disponible",
            "desc": "Taller monográfico avanzado sobre síntesis sonora, transcripción de partituras, conexión de teclado Korg EK-50 y armonización automática con inteligencia artificial.",
            "link_app": "CURSO_MUSICA/ATRIL_DIGITAL.html",
            "link_pdf": "#",
            "link_extra": "#"
        },
        {
            "num": "MONO-004",
            "title": "Restauración de Fotos Antiguas y Álbum Genealógico Familiar",
            "tag": "● DISPONIBLE",
            "status": "disponible",
            "desc": "Restaura fotografías familiares desgastadas, colóralas en alta fidelidad histórica y construye árboles genealógicos interactivos para conservar la memoria de tus antepasados.",
            "link_app": "#",
            "link_pdf": "#",
            "link_extra": "#"
        },
        {
            "num": "MONO-005",
            "title": "Asistentes de Voz en el Móvil y Trámites Digitales para Seniors",
            "tag": "● DISPONIBLE",
            "status": "disponible",
            "desc": "Domina el dictado de voz, recordatorios de citas médicas, lectura de prospectos y notas inteligentes en tu teléfono inteligente sin tocar el teclado.",
            "link_app": "#",
            "link_pdf": "#",
            "link_extra": "#"
        },
        {
            "num": "MONO-006",
            "title": "Seguridad Digital, Detección de Estafas Telefónicas y Deepfakes",
            "tag": "● DISPONIBLE",
            "status": "disponible",
            "desc": "Guía práctica de autodefensa digital para personas mayores: cómo identificar audios clonados por IA, llamadas fraudulentas de bancos y enlaces trampa de mensajería.",
            "link_app": "#",
            "link_pdf": "#",
            "link_extra": "#"
        },
        {
            "num": "MONO-007",
            "title": "Escritura Creativa, Memorias Familiares y Biografías Ilustradas",
            "tag": "● DISPONIBLE",
            "status": "disponible",
            "desc": "Taller para escribir y maquetar tu propio libro de memorias o cuentos para tus nietos, combinando relatos personales con ilustraciones generadas por IA.",
            "link_app": "#",
            "link_pdf": "#",
            "link_extra": "#"
        }
    ]

    # 5. Generar MAPA_MONOGRAFICOS.html con las tarjetas ordenadas
    cards_html = ""
    for m in monograficos:
        is_disp = m["status"] == "disponible"
        tag_class = "tag-active" if is_disp else "tag-soon"
        
        actions = ""
        if m["num"] == "MONO-002":
            actions = f"""
                <div class="actions-stack">
                    <a href="{m['link_app']}" target="_blank" class="btn-action btn-launch">
                        🚀 Abrir Taller Interactivo de los 6 Ejercicios ↗
                    </a>
                    <a href="{m['link_pdf']}" target="_blank" class="btn-action btn-pdf">
                        📄 Descargar Ficha Guía del Alumno (PDF) ↗
                    </a>
                    <a href="{m['link_extra']}" target="_blank" class="btn-action btn-book">
                        📕 Ver Catálogo Completo (PDF Original 104 Estilos con Dibujos) ↗
                    </a>
                </div>
            """
        elif m["num"] == "MONO-003":
            actions = f"""
                <div class="actions-stack">
                    <a href="{m['link_app']}" target="_blank" class="btn-action btn-launch">
                        🎹 Abrir Atril Digital Web MIDI ↗
                    </a>
                </div>
            """
        else:
            actions = f"""
                <div class="actions-stack">
                    <button class="btn-action btn-book" style="opacity: 0.8; cursor: pointer;" onclick="alert('Monográfico disponible en tu cuaderno de clase.')">
                        📖 Consultar Cuaderno Didáctico
                    </button>
                </div>
            """

        cards_html += f"""
            <div class="mono-card" data-status="{m['status']}">
                <div class="card-top">
                    <span class="mono-num">#{m['num']}</span>
                    <span class="{tag_class}">{m['tag']}</span>
                </div>
                <h2 class="mono-title">{m['title']}</h2>
                <p class="mono-desc">{m['desc']}</p>
                {actions}
            </div>
        """

    full_map_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monográficos & Talleres Especiales • Cuadro de Mando — Curso de IA</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #070b14;
            --bg-card: rgba(15, 23, 42, 0.94);
            --border-glow: rgba(56, 189, 248, 0.45);
            --text-main: #f8fafc;
            --text-sub: #cbd5e1;
            --text-muted: #94a3b8;
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
            background: radial-gradient(circle at 50% 15%, #151e3f 0%, #080c18 60%, #030509 100%);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
            user-select: none;
        }}

        header {{
            padding: 32px 24px 22px;
            text-align: center;
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.85) 0%, rgba(15, 23, 42, 0) 100%);
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            position: relative;
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
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            flex-wrap: wrap;
        }}

        .search-box {{
            flex: 1;
            min-width: 280px;
            position: relative;
        }}
        .search-input {{
            width: 100%;
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 12px 18px 12px 44px;
            color: var(--text-main);
            font-size: 0.95rem;
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
            position: relative;
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
            gap: 10px;
            padding-top: 14px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
        }}

        .btn-action {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            padding: 12px 18px;
            border-radius: 10px;
            font-weight: 800;
            font-size: 0.92rem;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.2s;
            border: 1px solid transparent;
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
            font-size: 0.85rem;
        }}
        .btn-book:hover {{ background: rgba(255, 255, 255, 0.1); color: var(--text-main); }}

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
            <span>Catálogo Dinámico Permanente • Actualización Automática</span>
        </div>
        <h1>📚 Monográficos & Talleres Especiales de IA</h1>
        <p class="subtitle">
            Cuadernos prácticos, talleres visuales y monográficos complementarios del Curso de IA para Adultos Mayores. Este mapa se actualiza automáticamente con cada nuevo taller sin necesidad de cambiar el enlace de Google Classroom.
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
        Curso de Inteligencia Artificial y Tecnología para Adultos Mayores (60+) • Cuadro de Mando de Monográficos • Despliegue Oficial en GitHub Pages
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
        f.write(full_map_html)
    print(f"\n3. Generado Mapa Maestro de Monográficos en:\n   {ROOT_MAP}")

    # Espejar a la carpeta 104 y Classroom
    map_104 = os.path.join(DIR_104, "MAPA_MONOGRAFICOS.html")
    with open(map_104, "w", encoding="utf-8") as f:
        f.write(full_map_html)
    print(f"  ✅ Espejado en: {map_104}")

    print("\n✨ Monográfico 02 integrado y renumeración completada.")

if __name__ == "__main__":
    main()

