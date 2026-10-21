#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_niv_lote5_htmls.py
Genera de forma autónoma las 10 Micro-Aplicaciones Interactivas Senior (+65)
para las Sesiones 41 a 50 (Lote 5) bajo la Triple Salvaguarda Pedagógica.
Las guarda tanto en SIMULADORES_INTERACTIVOS/01_SIMULADORES/ como en
CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/XX_Sesion/
"""

import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
SIM_DIR = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "01_SIMULADORES")
SESSIONS_DIR = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")

os.makedirs(SIM_DIR, exist_ok=True)

# Plantilla base CSS común de alto contraste, accesible y adaptable (+65)
BASE_CSS = """
        :root {
            --bg-base: #060913;
            --bg-card: rgba(15, 23, 42, 0.92);
            --border: rgba(255, 255, 255, 0.12);
            --primary: #10b981;
            --primary-glow: rgba(16, 185, 129, 0.35);
            --cyan: #38bdf8;
            --gold: #f59e0b;
            --purple: #a855f7;
            --rose: #f43f5e;
            --text-main: #f8fafc;
            --text-sub: #cbd5e1;
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-sans);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
            background-image: radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.12) 0%, transparent 65%);
            font-size: 17px;
        }

        header {
            background: rgba(15, 23, 42, 0.98);
            border-bottom: 1px solid var(--border);
            padding: 16px 32px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            backdrop-filter: blur(14px);
            position: sticky;
            top: 0;
            z-index: 50;
        }
        .brand-box {
            display: flex;
            align-items: center;
            gap: 14px;
        }
        .brand-badge {
            background: rgba(56, 189, 248, 0.18);
            color: var(--cyan);
            border: 1px solid rgba(56, 189, 248, 0.45);
            font-family: var(--font-mono);
            font-size: 0.88rem;
            font-weight: 800;
            padding: 5px 12px;
            border-radius: 8px;
        }
        h1 {
            font-size: 1.35rem;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: -0.01em;
        }

        .header-actions {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .btn-pedagogic {
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid var(--primary);
            color: #6ee7b7;
            padding: 8px 16px;
            border-radius: 10px;
            font-weight: 700;
            font-size: 0.88rem;
            cursor: pointer;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        .btn-pedagogic:hover {
            background: var(--primary);
            color: #04120a;
            box-shadow: 0 0 16px var(--primary-glow);
        }

        .app-container {
            flex: 1;
            display: grid;
            grid-template-columns: 480px 1fr;
            gap: 28px;
            max-width: 1540px;
            width: 100%;
            margin: 0 auto;
            padding: 28px;
        }

        .calculator-panel {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 26px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            backdrop-filter: blur(14px);
            box-shadow: 0 12px 35px rgba(0,0,0,0.5);
            height: fit-content;
        }
        .panel-title {
            font-size: 1.15rem;
            font-weight: 800;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 10px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 14px;
        }

        .control-group {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .control-label-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .control-label {
            font-size: 0.95rem;
            font-weight: 700;
            color: #e2e8f0;
        }
        .control-badge {
            font-family: var(--font-mono);
            font-size: 0.85rem;
            font-weight: 800;
            padding: 3px 10px;
            border-radius: 6px;
            background: rgba(56, 189, 248, 0.15);
            color: var(--cyan);
            border: 1px solid rgba(56, 189, 248, 0.3);
        }

        input[type="range"] {
            -webkit-appearance: none;
            width: 100%;
            height: 10px;
            border-radius: 5px;
            background: rgba(255, 255, 255, 0.12);
            outline: none;
            cursor: pointer;
            transition: background 0.2s;
        }
        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 26px;
            height: 26px;
            border-radius: 50%;
            background: var(--cyan);
            border: 3px solid #ffffff;
            cursor: pointer;
            box-shadow: 0 0 12px rgba(56, 189, 248, 0.6);
            transition: transform 0.15s ease;
        }
        input[type="range"]::-webkit-slider-thumb:hover {
            transform: scale(1.15);
        }

        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            margin-top: 6px;
        }
        .kpi-card {
            background: rgba(0, 0, 0, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 14px;
            text-align: center;
        }
        .kpi-val {
            font-family: var(--font-mono);
            font-size: 1.15rem;
            font-weight: 800;
            color: #ffffff;
        }
        .kpi-lbl {
            font-size: 0.76rem;
            color: #94a3b8;
            font-weight: 600;
            text-transform: uppercase;
            margin-top: 4px;
        }

        .dashboard-panel {
            display: flex;
            flex-direction: column;
            gap: 22px;
        }

        .status-hero {
            background: linear-gradient(135deg, rgba(56, 189, 248, 0.18) 0%, rgba(15, 23, 42, 0.95) 100%);
            border: 2px solid var(--cyan);
            border-radius: 22px;
            padding: 26px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 0 35px rgba(56, 189, 248, 0.3);
            position: relative;
        }
        .status-hero-left {
            max-width: 74%;
        }
        .status-badge {
            font-family: var(--font-mono);
            font-size: 0.8rem;
            font-weight: 800;
            color: var(--cyan);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 6px;
            display: inline-block;
        }
        .status-title {
            font-size: 1.55rem;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: -0.02em;
            line-height: 1.25;
            margin-bottom: 10px;
        }
        .status-desc {
            font-size: 0.98rem;
            color: #cbd5e1;
            line-height: 1.6;
        }
        .status-circle-box {
            width: 105px;
            height: 105px;
            border-radius: 50%;
            border: 4px solid var(--cyan);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: rgba(0, 0, 0, 0.6);
            box-shadow: 0 0 25px rgba(56, 189, 248, 0.4);
            flex-shrink: 0;
        }
        .status-circle-num {
            font-family: var(--font-mono);
            font-size: 2.1rem;
            font-weight: 900;
            color: var(--cyan);
            line-height: 1;
        }
        .status-circle-sub {
            font-size: 0.7rem;
            color: #94a3b8;
            font-weight: 800;
            text-transform: uppercase;
        }

        .steps-container {
            display: flex;
            flex-direction: column-reverse;
            gap: 12px;
        }
        .step-card {
            background: var(--bg-card);
            border: 1.5px solid var(--border);
            border-radius: 16px;
            padding: 16px 20px;
            display: flex;
            align-items: center;
            gap: 18px;
            transition: all 0.25s ease;
            opacity: 0.65;
            cursor: pointer;
        }
        .step-card:hover {
            opacity: 0.95;
            transform: translateX(4px);
        }
        .step-card.active {
            opacity: 1;
            border-color: var(--cyan);
            background: rgba(56, 189, 248, 0.12);
            box-shadow: 0 0 20px rgba(56, 189, 248, 0.25);
            transform: scale(1.01);
        }
        .step-num-pill {
            width: 44px;
            height: 44px;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.08);
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: var(--font-mono);
            font-size: 1.15rem;
            font-weight: 800;
            color: #ffffff;
            flex-shrink: 0;
            border: 1px solid rgba(255, 255, 255, 0.15);
        }
        .step-card.active .step-num-pill {
            background: var(--cyan);
            color: #060913;
            border-color: #ffffff;
        }
        .step-body {
            flex: 1;
        }
        .step-title-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 4px;
        }
        .step-name {
            font-size: 1.05rem;
            font-weight: 800;
            color: #ffffff;
        }
        .step-tag {
            font-size: 0.8rem;
            font-family: var(--font-mono);
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 6px;
            background: rgba(255, 255, 255, 0.08);
            color: #94a3b8;
        }
        .step-card.active .step-tag {
            background: rgba(56, 189, 248, 0.25);
            color: var(--cyan);
        }
        .step-detail {
            font-size: 0.88rem;
            color: #94a3b8;
            line-height: 1.45;
        }
        .step-card.active .step-detail {
            color: #e2e8f0;
        }

        .pedagogic-modal {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(10px);
            z-index: 100;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .pedagogic-modal.active {
            display: flex;
        }
        .modal-box {
            background: #0b1329;
            border: 2px solid var(--primary);
            border-radius: 24px;
            max-width: 900px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            padding: 32px;
            box-shadow: 0 0 50px rgba(16, 185, 129, 0.4);
            display: flex;
            flex-direction: column;
            gap: 22px;
        }
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.12);
            padding-bottom: 16px;
        }
        .modal-title {
            font-size: 1.3rem;
            font-weight: 800;
            color: #6ee7b7;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .btn-close {
            background: transparent;
            border: none;
            color: #94a3b8;
            font-size: 1.5rem;
            cursor: pointer;
            transition: color 0.2s;
        }
        .btn-close:hover { color: #ffffff; }

        .safeguard-card {
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .safeguard-card.green {
            border-color: rgba(16, 185, 129, 0.4);
            background: rgba(6, 95, 70, 0.15);
        }
        .safeguard-card.cyan {
            border-color: rgba(56, 189, 248, 0.4);
            background: rgba(14, 116, 144, 0.15);
        }
        .safeguard-card.amber {
            border-color: rgba(245, 158, 11, 0.4);
            background: rgba(180, 83, 9, 0.15);
        }
        .safeguard-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .safeguard-badge {
            font-family: var(--font-mono);
            font-size: 0.8rem;
            font-weight: 800;
            padding: 4px 10px;
            border-radius: 6px;
        }
        .btn-copy {
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #ffffff;
            padding: 4px 12px;
            border-radius: 6px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
        }
        .btn-copy:hover {
            background: var(--primary);
            color: #04120a;
        }
        .code-box {
            background: rgba(0, 0, 0, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 10px;
            padding: 14px;
            font-family: var(--font-mono);
            font-size: 0.88rem;
            color: #e2e8f0;
            white-space: pre-wrap;
            line-height: 1.5;
        }

        @media (max-width: 1100px) {
            .app-container {
                grid-template-columns: 1fr;
            }
        }
"""

def generate_html_microapp(code, num, title, subtitle, icon, steps, kpis, initial_level, aside_html, script_js, seed_prompt, master_prompt):
    """
    Genera el archivo HTML autocontenido para una Micro-App Senior.
    """
    steps_html = ""
    for idx, s in enumerate(steps, 1):
        active_cls = " active" if idx == initial_level else ""
        steps_html += f"""
                <div class="step-card{active_cls}" onclick="setLevel({idx})">
                    <div class="step-num-pill">{idx}</div>
                    <div class="step-body">
                        <div class="step-title-row">
                            <span class="step-name">{s['name']}</span>
                            <span class="step-tag">{s['tag']}</span>
                        </div>
                        <div class="step-detail">{s['desc']}</div>
                    </div>
                </div>"""

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{code} — {title}</title>
    <style>
{BASE_CSS}
    </style>
</head>
<body>

    <header>
        <div class="brand-box">
            <span class="brand-badge">{code}</span>
            <div>
                <h1>{icon} {title}</h1>
                <div style="font-size: 0.82rem; color: #94a3b8;">{subtitle}</div>
            </div>
        </div>
        <div class="header-actions">
            <button class="btn-pedagogic" onclick="openModal()">
                🛡️ La Triple Salvaguarda Pedagógica
            </button>
        </div>
    </header>

    <div class="app-container">
        <!-- Panel de control interactivo -->
        <aside class="calculator-panel">
            <div class="panel-title">
                <span>⚙️ Controles y Diagnóstico</span>
            </div>
            
{aside_html}

            <div class="kpi-grid">
                <div class="kpi-card">
                    <div class="kpi-val" id="kpi1-val">{kpis[0]['val']}</div>
                    <div class="kpi-lbl">{kpis[0]['lbl']}</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-val" id="kpi2-val">{kpis[1]['val']}</div>
                    <div class="kpi-lbl">{kpis[1]['lbl']}</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-val" id="kpi3-val">{kpis[2]['val']}</div>
                    <div class="kpi-lbl">{kpis[2]['lbl']}</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-val" id="kpi4-val">{kpis[3]['val']}</div>
                    <div class="kpi-lbl">{kpis[3]['lbl']}</div>
                </div>
            </div>
        </aside>

        <!-- Tablero de niveles y estado activo -->
        <main class="dashboard-panel">
            <div class="status-hero" id="status-hero">
                <div class="status-hero-left">
                    <span class="status-badge" id="status-badge">Nivel {initial_level}</span>
                    <h2 class="status-title" id="status-title">{steps[initial_level-1]['name']}</h2>
                    <p class="status-desc" id="status-desc">{steps[initial_level-1]['desc']}</p>
                </div>
                <div class="status-circle-box" id="status-circle">
                    <span class="status-circle-num" id="status-circle-num">{initial_level}</span>
                    <span class="status-circle-sub">NIVEL</span>
                </div>
            </div>

            <div class="steps-container" id="steps-container">
{steps_html}
            </div>
        </main>
    </div>

    <!-- Modal Pedagógico Triple Salvaguarda -->
    <div class="pedagogic-modal" id="pedagogic-modal">
        <div class="modal-box">
            <div class="modal-header">
                <div class="modal-title">
                    <span>🛡️ La Triple Salvaguarda Pedagógica (CURSO-IA)</span>
                </div>
                <button class="btn-close" onclick="closeModal()">&times;</button>
            </div>

            <div class="safeguard-card green">
                <div class="safeguard-header">
                    <span class="safeguard-badge" style="background: rgba(16, 185, 129, 0.3); color: #6ee7b7;">NIVEL 1: PROMPT SEMILLA HUMANO</span>
                    <button class="btn-copy" onclick="copyText('prompt-seed')">📋 Copiar Prompt</button>
                </div>
                <p style="font-size: 0.88rem; color: #cbd5e1;">Pega esta orden en Gemini en lenguaje natural para que entienda el objetivo pedagógico:</p>
                <div class="code-box" id="prompt-seed">{seed_prompt}</div>
            </div>

            <div class="safeguard-card cyan">
                <div class="safeguard-header">
                    <span class="safeguard-badge" style="background: rgba(56, 189, 248, 0.3); color: #7dd3fc;">NIVEL 2: PLANO MAESTRO TÉCNICO</span>
                    <button class="btn-copy" onclick="copyText('prompt-master')">📋 Copiar Plano</button>
                </div>
                <p style="font-size: 0.88rem; color: #cbd5e1;">Si Gemini duda o necesitas forzar la generación exacta del archivo HTML:</p>
                <div class="code-box" id="prompt-master">{master_prompt}</div>
            </div>

            <div class="safeguard-card amber">
                <div class="safeguard-header">
                    <span class="safeguard-badge" style="background: rgba(245, 158, 11, 0.3); color: #fcd34d;">NIVEL 3: GARANTÍA OFICIAL EN EL AULA</span>
                </div>
                <p style="font-size: 0.88rem; color: #cbd5e1;">
                    Si la conexión o la IA se saturan en el aula, abre directamente esta Micro-App oficial 100% probada y desplegada en Classroom. ¡Cero frustración para el alumno!
                </p>
            </div>
        </div>
    </div>

    <script>
        const STEPS_DATA = {steps};

        function setLevel(lvl) {{
            const cards = document.querySelectorAll('.step-card');
            cards.forEach((c, idx) => {{
                if (idx === (lvl - 1)) {{
                    c.classList.add('active');
                }} else {{
                    c.classList.remove('active');
                }}
            }});

            const data = STEPS_DATA[lvl - 1];
            document.getElementById('status-badge').innerText = 'NIVEL ' + lvl + ' • ' + (data.tag || '');
            document.getElementById('status-title').innerText = data.name;
            document.getElementById('status-desc').innerText = data.desc;
            document.getElementById('status-circle-num').innerText = lvl;

            if (typeof onLevelChanged === 'function') {{
                onLevelChanged(lvl);
            }}
        }}

        function openModal() {{
            document.getElementById('pedagogic-modal').classList.add('active');
        }}

        function closeModal() {{
            document.getElementById('pedagogic-modal').classList.remove('active');
        }}

        function copyText(id) {{
            const text = document.getElementById(id).innerText;
            navigator.clipboard.writeText(text).then(() => {{
                alert('¡Copiado al portapapeles con éxito!');
            }});
        }}

{script_js}
    </script>
</body>
</html>"""


APPS = [
    # =========================================================================
    # SESIÓN 41: NIV-041
    # =========================================================================
    {
        "code": "[NIV-041]",
        "num": 41,
        "filename": "SIMULADOR_CONECTIVIDAD_WIFI_HOGAR_SENIORS.html",
        "title": "Los 6 Niveles de Conectividad Digital, Wi-Fi del Hogar y Videollamadas Familiares",
        "subtitle": "De la red de cobre antigua a la fibra óptica y Wi-Fi de alta cobertura para ver a los nietos sin cortes",
        "icon": "📶",
        "initial_level": 4,
        "steps": [
            {"name": "Zona Ciega / Sin Señal", "tag": "0 BARRAS", "desc": "Router oculto dentro de un mueble de madera o detrás de paredes gruesas de carga. La videollamada se corta continuamente o no conecta."},
            {"name": "Señal Débil / Inestable", "tag": "1 BARRA", "desc": "Llegan menos de 10 Mbps. La voz de los nietos llega con retraso ('efecto robot') y la imagen se congela al mínimo movimiento."},
            {"name": "Conectividad Básica de Lectura", "tag": "2 BARRAS", "desc": "Velocidad entre 20 y 50 Mbps. Permite leer la prensa digital del día y enviar mensajes o fotos por WhatsApp sin esperas."},
            {"name": "Conexión Óptima de Fibra en Salón", "tag": "3 BARRAS", "desc": "Velocidad de 100 a 300 Mbps con router en alto y despejado. Videollamadas familiares en alta definición nítidas y sin saltos."},
            {"name": "Cobertura Total con Repetidor de Pasillo", "tag": "COBERTURA 100%", "desc": "Toda la casa cubierta (terraza, cocina, dormitorios) mediante un pequeño enchufe repetidor Wi-Fi colocado en el pasillo intermedio."},
            {"name": "Red de Fibra Simétrica de Última Generación", "tag": "ALTA VELOCIDAD", "desc": "Fibra pura de 600 Mbps a 1 Gbps. Varios familiares conectados a la vez (televisión por internet, móvil, tablet) sin perder fluidez."}
        ],
        "kpis": [
            {"val": "85%", "lbl": "Cobertura en Estancia"},
            {"val": "300 Mbps", "lbl": "Velocidad Fibra"},
            {"val": "Excelente", "lbl": "Calidad Videollamada"},
            {"val": "30 seg", "lbl": "Regla Reinicio Router"}
        ],
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">📍 Ubicación del Router en Casa</span>
                    <span class="control-badge" id="loc-badge">Salón Despejado</span>
                </div>
                <select id="loc-select" style="width:100%; padding:10px; border-radius:10px; background:rgba(0,0,0,0.5); color:#fff; border:1px solid rgba(255,255,255,0.2);" onchange="updateWifiCalc()">
                    <option value="1">Escondido en un mueble / suelo (Pérdida -60%)</option>
                    <option value="2">Dormitorio al fondo de la casa (Descentrado)</option>
                    <option value="3" selected>Salón céntrico sobre mesita alta (Óptimo)</option>
                    <option value="4">Con Repetidor Wi-Fi en el pasillo (Cobertura Total)</option>
                </select>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🧱 Grosor de Paredes y Puertas</span>
                    <span class="control-badge" id="wall-badge">Tabique Estándar</span>
                </div>
                <input type="range" id="wall-slider" min="1" max="3" value="2" oninput="updateWifiCalc()">
                <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#94a3b8;">
                    <span>Pladur ligero</span>
                    <span>Ladrillo estándar</span>
                    <span>Muro de piedra/carga</span>
                </div>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">📱 Actividad Deseada</span>
                    <span class="control-badge" id="act-badge">Videollamada HD</span>
                </div>
                <select id="act-select" style="width:100%; padding:10px; border-radius:10px; background:rgba(0,0,0,0.5); color:#fff; border:1px solid rgba(255,255,255,0.2);" onchange="updateWifiCalc()">
                    <option value="text">Enviar mensajes WhatsApp (Requiere 2 Mbps)</option>
                    <option value="news">Leer prensa digital y recetas (Requiere 15 Mbps)</option>
                    <option value="video" selected>Videollamada familiar con nietos (Requiere 50 Mbps)</option>
                    <option value="tv">Ver película en la tele por internet (Requiere 100 Mbps)</option>
                </select>
            </div>
            
            <div style="background:rgba(56, 189, 248, 0.1); border:1px solid rgba(56, 189, 248, 0.3); border-radius:12px; padding:12px; font-size:0.85rem; color:#cbd5e1;">
                💡 <b>Regla de Oro de los 30 segundos:</b> Si la conexión se congela, desenchufa el router de la pared, cuenta despacio hasta 30 para vaciar la memoria y vuelve a enchufarlo. Se arregla el 90% de las incidencias sin llamar al técnico.
            </div>
        """,
        "script": """
        function updateWifiCalc() {
            const loc = parseInt(document.getElementById('loc-select').value);
            const wall = parseInt(document.getElementById('wall-slider').value);
            const act = document.getElementById('act-select').value;
            
            let lvl = 1;
            let cobertura = 30;
            let mbps = 15;
            let calidad = "Baja";

            if (loc === 1) {
                lvl = wall === 3 ? 1 : 2;
                cobertura = 35;
                mbps = 20;
                calidad = "Entrecortada";
            } else if (loc === 2) {
                lvl = wall === 3 ? 2 : 3;
                cobertura = 55;
                mbps = 60;
                calidad = "Aceptable";
            } else if (loc === 3) {
                lvl = wall === 3 ? 3 : 4;
                cobertura = 85;
                mbps = 300;
                calidad = "Excelente";
            } else {
                lvl = wall === 3 ? 5 : 6;
                cobertura = 98;
                mbps = 600;
                calidad = "Impecable";
            }

            document.getElementById('kpi1-val').innerText = cobertura + "%";
            document.getElementById('kpi2-val').innerText = mbps + " Mbps";
            document.getElementById('kpi3-val').innerText = calidad;
            
            setLevel(lvl);
        }

        function onLevelChanged(lvl) {
            // sincronizar selector si es necesario
        }
        """,
        "prompt_seed": """Actúa como un técnico de telecomunicaciones y pedagogo digital para personas mayores (+65).
Explícame en 3 viñetas cómo diseñar un simulador interactivo en HTML que muestre por qué la Wi-Fi no llega bien a todas las habitaciones y enseñe a colocar el router en alto para hablar con los nietos por videollamada sin cortes.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con selector de estancia del router (salón, pasillo, escondido), grosor de tabiques, medidor de cobertura Wi-Fi y velocidad de fibra, y el protocolo paso a paso de los 30 segundos para reiniciar el router con tranquilidad."""
    },

    # =========================================================================
    # SESIÓN 42: NIV-042
    # =========================================================================
    {
        "code": "[NIV-042]",
        "num": 42,
        "filename": "SIMULADOR_CIBERSEGURIDAD_CONTRASENAS_2FA_SENIORS.html",
        "title": "Los 5 Niveles de Blindaje Digital: Contraseñas Fuertes, Verificación en Dos Pasos y Privacidad",
        "subtitle": "Sustituye claves imposibles de recordar por frases llave memorables y protege tus cuentas bancarias",
        "icon": "🔐",
        "initial_level": 4,
        "steps": [
            {"name": "Peligro Crítico: Clave Simple", "tag": "DESCIFRADO EN 1 SEG", "desc": "Contraseñas como '123456', 'maria' o la fecha de cumpleaños. Un programa automático de hackers la descifra al instante."},
            {"name": "Seguridad Básica Vulnerable", "tag": "ROBO EN 2 HORAS", "desc": "Una sola palabra común con un número detrás (ej. 'Madrid2020'). Aunque parece segura, los diccionarios de estafadores la averiguan rápido."},
            {"name": "Frase Llave Memorable en Español", "tag": "400 AÑOS", "desc": "Método de oro senior: juntar 4 palabras fáciles de recordar para ti (ej. 'MiNietoLucasNacioEn2021!'). Es facilísima de escribir y casi imposible de hackear."},
            {"name": "Doble Factor y Huella Dactilar (2FA)", "tag": "DOBLE CANDADO", "desc": "Frase llave + confirmación con la huella dactilar o rostro en el móvil. Aunque un ladrón supiera tu clave, no puede entrar sin tu teléfono físico."},
            {"name": "Blindaje Absoluto y Paz Mental", "tag": "INFRANQUEABLE", "desc": "Cuentas bancarias blindadas, copia de contraseñas guardada en una libreta física en el cajón de casa (lejos de internet) y regla de nunca dictar códigos SMS a nadie."}
        ],
        "kpis": [
            {"val": "400 Años", "lbl": "Resistencia a Hackers"},
            {"val": "95%", "lbl": "Índice de Blindaje"},
            {"val": "Activo", "lbl": "Doble Factor (2FA)"},
            {"val": "0%", "lbl": "Riesgo Bancario"}
        ],
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">✍️ Prueba una Contraseña o Frase</span>
                    <span class="control-badge" id="pwd-badge">Muy Robusta</span>
                </div>
                <input type="text" id="pwd-input" value="MiNietoLucasNacioEn2021!" style="width:100%; padding:10px; border-radius:10px; background:rgba(0,0,0,0.5); color:#fff; border:1px solid rgba(255,255,255,0.2); font-family:var(--font-mono);" oninput="checkPasswordHealth()">
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">💡 Generador de Frases Llave Seguras</span>
                </div>
                <button class="btn-pedagogic" style="width:100%; justify-content:center;" onclick="generateMemorablePhrase()">
                    🎲 Generar Nueva Frase Llave Fácil
                </button>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">👆 Huella Dactilar / Reconocimiento</span>
                    <span class="control-badge" id="bio-badge">Activada</span>
                </div>
                <label style="display:flex; align-items:center; gap:10px; color:#cbd5e1; cursor:pointer;">
                    <input type="checkbox" id="bio-check" checked onchange="checkPasswordHealth()" style="width:20px; height:20px;">
                    Usar huella en el móvil para entrar al banco
                </label>
            </div>

            <div style="background:rgba(245, 158, 11, 0.12); border:1px solid rgba(245, 158, 11, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#fde68a;">
                ⚠️ <b>Regla Sagrada del Código SMS:</b> Si recibes un código en el móvil y te llama alguien diciendo ser de tu banco para pedírtelo... <b>¡JAMÁS SE LO DES!</b> Tu banco de verdad nunca te pedirá códigos por teléfono. Cuelga inmediatamente.
            </div>
        """,
        "script": """
        const PHRASES = [
            "MiNietoLucasNacioEn2021!",
            "ElCafeConMisAmigosLosJueves#",
            "PaseoPorElParqueA LasDiez*",
            "MiPuebloTieneLasMejoresFiestas24!",
            "TortillaDePatatasConCebolla2025?"
        ];

        function generateMemorablePhrase() {
            const randomP = PHRASES[Math.floor(Math.random() * PHRASES.length)];
            document.getElementById('pwd-input').value = randomP;
            checkPasswordHealth();
        }

        function checkPasswordHealth() {
            const pwd = document.getElementById('pwd-input').value;
            const bio = document.getElementById('bio-check').checked;
            
            let lvl = 1;
            let timeStr = "1 segundo";
            let blindaje = "20%";

            if (pwd.length < 6) {
                lvl = 1;
                timeStr = "Instantáneo";
                blindaje = "15%";
            } else if (pwd.length < 10) {
                lvl = 2;
                timeStr = "3 horas";
                blindaje = "40%";
            } else if (pwd.length < 16) {
                lvl = 3;
                timeStr = "50 años";
                blindaje = "75%";
            } else {
                lvl = bio ? 5 : 4;
                timeStr = "400 años";
                blindaje = bio ? "98%" : "88%";
            }

            document.getElementById('kpi1-val').innerText = timeStr;
            document.getElementById('kpi2-val').innerText = blindaje;
            document.getElementById('kpi3-val').innerText = bio ? "Activo" : "Inactivo";
            document.getElementById('kpi4-val').innerText = (lvl >= 4 && bio) ? "0%" : (lvl >= 3 ? "5%" : "85%");

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un experto en ciberseguridad bancaria y docente para personas mayores (+65).
Explícame en 3 viñetas cómo diseñar una herramienta interactiva en HTML que enseñe a crear contraseñas memorables mediante frases en español sin agobios y alerte de no compartir jamás el código SMS del banco.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con comprobador de frases llave en tiempo real, generador de contraseñas memorables en español, interruptor de biometría (huella dactilar), medidor de tiempo de descifrado y advertencia antifraude telefónico."""
    },

    # =========================================================================
    # SESIÓN 43: NIV-043
    # =========================================================================
    {
        "code": "[NIV-043]",
        "num": 43,
        "filename": "SIMULADOR_ACCESIBILIDAD_PANTALLAS_TEXTO_SENIORS.html",
        "title": "Los 6 Niveles de Resolución, Tamaño de Letra y Accesibilidad en Pantallas",
        "subtitle": "Configura tu móvil, tablet y televisión para leer con comodidad sin cansar la vista ni forzar el cuello",
        "icon": "🔍",
        "initial_level": 4,
        "steps": [
            {"name": "Texto Diminuto de Fábrica (14px)", "tag": "FATIGA VISUAL", "desc": "Letra pequeña que viene por defecto en los teléfonos. Obliga a forzar el cristalino y provoca picor de ojos y dolor de cabeza al poco rato."},
            {"name": "Tamaño Básico Ajustado (16px)", "tag": "ESFUERZO MEDIO", "desc": "Mejora leve, pero todavía requiere entrecerrar los ojos para leer prospectos de medicamentos o mensajes largos de WhatsApp."},
            {"name": "Tamaño Cómodo de Lectura (18px-20px)", "tag": "CONFORT GENERAL", "desc": "El tamaño estándar recomendado para personas con presbicia (vista cansada). Las noticias y recados se leen con naturalidad a 40 cm de distancia."},
            {"name": "Accesibilidad Óptima Senior (22px)", "tag": "LECTURA RELAJADA", "desc": "Texto amplio, botones grandes y espacio generoso entre líneas. Permite utilizar el teléfono sin necesidad de buscar corriendo las gafas de cerca."},
            {"name": "Modo Contraste Alto + Filtro Cálido Nocturno", "tag": "DESCANSO TOTAL", "desc": "Letra nítida sobre fondo oscuro y activación de la luz nocturna ámbar a partir de las 20:00 para no desvelar la melatonina ni alterar el sueño."},
            {"name": "Accesibilidad Integral con Lupa y Dictado", "tag": "AUTONOMÍA PLENA", "desc": "Lupa digital activada con tres toques para ampliar la carta de un restaurante o las instrucciones de una receta, y dictado por voz para responder mensajes sin teclear."}
        ],
        "kpis": [
            {"val": "22 px", "lbl": "Tamaño de Letra"},
            {"val": "95%", "lbl": "Legibilidad"},
            {"val": "Mínimo", "lbl": "Esfuerzo Visual"},
            {"val": "Protegido", "lbl": "Descanso Ocular"}
        ],
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🔤 Tamaño del Texto en Pantalla</span>
                    <span class="control-badge" id="size-badge">22 px (Grande)</span>
                </div>
                <input type="range" id="size-slider" min="14" max="26" value="22" oninput="updateVisualCalc()">
                <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#94a3b8;">
                    <span>14px (Pequeño)</span>
                    <span>18px (Normal)</span>
                    <span>26px (Muy Grande)</span>
                </div>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🎨 Modo Visual y Contraste</span>
                </div>
                <select id="theme-select" style="width:100%; padding:10px; border-radius:10px; background:rgba(0,0,0,0.5); color:#fff; border:1px solid rgba(255,255,255,0.2);" onchange="updateVisualCalc()">
                    <option value="1">Modo Estándar (Fondo Blanco / Letra Gris)</option>
                    <option value="2" selected>Modo Alto Contraste (Fondo Oscuro / Letra Blanca)</option>
                    <option value="3">Modo Lectura Ámbar (Filtro Cálido Antifatiga)</option>
                </select>
            </div>

            <!-- Previsualización de texto en vivo -->
            <div class="control-group">
                <div class="control-label">📖 Muestra de Lectura en Pantalla:</div>
                <div id="preview-box" style="background:#0f172a; border:2px solid #38bdf8; border-radius:12px; padding:16px; font-size:22px; line-height:1.5; color:#f8fafc; min-height:110px;">
                    "Hola abuelo, te hemos enviado las fotos del cumpleaños de los niños. ¡Están preciosos!"
                </div>
            </div>
            
            <div style="background:rgba(56, 189, 248, 0.1); border:1px solid rgba(56, 189, 248, 0.3); border-radius:12px; padding:12px; font-size:0.85rem; color:#cbd5e1;">
                💡 <b>El truco de la Lupa en el móvil:</b> En los ajustes de 'Accesibilidad', puedes activar la 'Lupa' con un atajo. Podrás usar la cámara del teléfono como una potente lupa con luz para leer prospectos de medicamentos o cartas en restaurantes oscuros.
            </div>
        """,
        "script": """
        function updateVisualCalc() {
            const size = parseInt(document.getElementById('size-slider').value);
            const theme = parseInt(document.getElementById('theme-select').value);
            const preview = document.getElementById('preview-box');

            document.getElementById('size-badge').innerText = size + " px";
            preview.style.fontSize = size + "px";

            if (theme === 1) {
                preview.style.background = "#e2e8f0";
                preview.style.color = "#0f172a";
            } else if (theme === 2) {
                preview.style.background = "#060913";
                preview.style.color = "#f8fafc";
            } else {
                preview.style.background = "#2d2013";
                preview.style.color = "#fed7aa";
            }

            let lvl = 1;
            let esfuerzo = "Alto";
            if (size <= 14) { lvl = 1; esfuerzo = "Muy Alto"; }
            else if (size <= 16) { lvl = 2; esfuerzo = "Notable"; }
            else if (size <= 19) { lvl = 3; esfuerzo = "Moderado"; }
            else if (size <= 22) { lvl = theme === 2 ? 4 : 4; esfuerzo = "Mínimo"; }
            else if (size <= 24) { lvl = theme === 3 ? 5 : 4; esfuerzo = "Cero"; }
            else { lvl = 6; esfuerzo = "Cero"; }

            document.getElementById('kpi1-val').innerText = size + " px";
            document.getElementById('kpi2-val').innerText = Math.min(100, (size - 10) * 7) + "%";
            document.getElementById('kpi3-val').innerText = esfuerzo;
            document.getElementById('kpi4-val').innerText = theme === 3 ? "Óptimo (Ámbar)" : "Adecuado";

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un oftalmólogo geriátrico y diseñador de accesibilidad digital para personas mayores (+65).
Explícame en 3 viñetas cómo crear una guía interactiva en HTML que demuestre la importancia de agrandar la letra en el móvil (a 20-22px) y activar el modo cálido nocturno para no cansar la vista.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con deslizador de tamaño de letra en tiempo real (14px a 26px), caja de previsualización de mensajes, selector de contraste alto y filtro ámbar, y medidor de fatiga visual geriátrica."""
    },

    # =========================================================================
    # SESIÓN 44: NIV-044
    # =========================================================================
    {
        "code": "[NIV-044]",
        "num": 44,
        "filename": "SIMULADOR_COPIAS_SEGURIDAD_FOTOS_NUBE_SENIORS.html",
        "title": "Los 5 Niveles del Archivo Digital: Copias de Seguridad, Fotos Familiares y la Nube",
        "subtitle": "Protege los recuerdos familiares de toda una vida para que nunca se pierdan si se rompe o extravía el móvil",
        "icon": "☁️",
        "initial_level": 4,
        "steps": [
            {"name": "Peligro Crítico: Solo en el Teléfono", "tag": "RIESGO MÁXIMO", "desc": "Todas las fotos familiares guardadas únicamente en la memoria interna del teléfono. Si el móvil se cae al agua, se estropea o se pierde, se pierden las fotos de los nietos para siempre."},
            {"name": "Copia Manual en Tarjeta de Memoria o Pendrive", "tag": "RESPALDO OCASIONAL", "desc": "Copiar fotos una vez al año al ordenador o a un pendrive con ayuda de un familiar. Mejor que nada, pero si pasan meses sin hacerlo se pierden los últimos recuerdos."},
            {"name": "Copia Automática en la Nube con Wi-Fi", "tag": "TRANQUILIDAD DIARIA", "desc": "Google Fotos o iCloud activados para sincronizar solo cuando el móvil se conecta a la Wi-Fi de casa por la noche. No gasta datos móviles y sube cada foto automáticamente."},
            {"name": "Doble Bóveda Digital + Álbum en Papel", "tag": "RECUERDOS BLINDADOS", "desc": "Copia en la nube más la maravillosa costumbre de imprimir una vez al año las 50 fotos más bonitas en un álbum físico en papel para hojearlo en el salón."},
            {"name": "Legado Familiar Compartido y Perpetuo", "tag": "MEMORIA INMORTAL", "desc": "Álbumes familiares organizados por años y eventos (Navidades, viajes, bautizos) compartidos con hijos y nietos. Los recuerdos permanecen vivos y protegidos para las próximas generaciones."}
        ],
        "kpis": [
            {"val": "100%", "lbl": "Fotos Protegidas"},
            {"val": "Nulo", "lbl": "Riesgo de Pérdida"},
            {"val": "Automática", "lbl": "Copia Nocturna Wi-Fi"},
            {"val": "Perpetua", "lbl": "Tranquilidad Familiar"}
        ],
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">📸 Cantidad de Fotos Familiares</span>
                    <span class="control-badge" id="photos-badge">2.500 Fotos</span>
                </div>
                <input type="range" id="photos-slider" min="500" max="10000" step="500" value="2500" oninput="updateBackupCalc()">
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🛡️ Sistema de Copia de Seguridad</span>
                </div>
                <select id="backup-select" style="width:100%; padding:10px; border-radius:10px; background:rgba(0,0,0,0.5); color:#fff; border:1px solid rgba(255,255,255,0.2);" onchange="updateBackupCalc()">
                    <option value="1">Solo en la memoria del teléfono (Sin copia)</option>
                    <option value="2">Copia manual en un pendrive o PC (Una vez al año)</option>
                    <option value="3" selected>Copia automática en la Nube (Google Fotos / iCloud)</option>
                    <option value="4">Copia en la Nube + Álbum físico impreso anual</option>
                </select>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🌙 Copia Silenciosa Nocturna</span>
                    <span class="control-badge">Recomendado</span>
                </div>
                <label style="display:flex; align-items:center; gap:10px; color:#cbd5e1; cursor:pointer;">
                    <input type="checkbox" id="wifi-check" checked onchange="updateBackupCalc()" style="width:20px; height:20px;">
                    Subir solo con Wi-Fi mientras el móvil se carga de noche
                </label>
            </div>

            <div style="background:rgba(56, 189, 248, 0.1); border:1px solid rgba(56, 189, 248, 0.3); border-radius:12px; padding:12px; font-size:0.85rem; color:#cbd5e1;">
                ☁️ <b>¿Qué es 'la Nube' explicada sin palabras raras?</b> Es como tener una caja fuerte privada en un desván gigante que no se quema, no se moja y no se desgasta. Si cambias de teléfono o se te rompe, metes tu correo y contraseña ¡y todas tus fotos vuelven a aparecer al instante!
            </div>
        """,
        "script": """
        function updateBackupCalc() {
            const photos = parseInt(document.getElementById('photos-slider').value);
            const sys = parseInt(document.getElementById('backup-select').value);
            const wifi = document.getElementById('wifi-check').checked;

            document.getElementById('photos-badge').innerText = photos.toLocaleString('es-ES') + " Fotos";

            let lvl = sys;
            let blindadas = "0%";
            let riesgo = "Crítico";

            if (sys === 1) {
                lvl = 1;
                blindadas = "0%";
                riesgo = "Crítico (100%)";
            } else if (sys === 2) {
                lvl = 2;
                blindadas = "50%";
                riesgo = "Moderado";
            } else if (sys === 3) {
                lvl = wifi ? 4 : 3;
                blindadas = "100%";
                riesgo = "Nulo";
            } else {
                lvl = 5;
                blindadas = "100% + Físico";
                riesgo = "Cero Absoluto";
            }

            document.getElementById('kpi1-val').innerText = blindadas;
            document.getElementById('kpi2-val').innerText = riesgo;
            document.getElementById('kpi3-val').innerText = wifi ? "Activada" : "Manual";
            document.getElementById('kpi4-val').innerText = lvl >= 4 ? "Total" : "Vulnerable";

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un archivero digital y pedagogo familiar para personas mayores (+65).
Explícame en 3 viñetas cómo crear una herramienta interactiva en HTML que explique qué es la nube con metáforas sencillas y enseñe a activar la copia automática de fotos familiares para no perder los recuerdos.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con calculadora de fotos protegidas, selector de sistemas de respaldo (móvil, pendrive, nube, álbum impreso), explicación tranquilizadora de la nube y medidor de riesgo de pérdida por extravío del teléfono."""
    },

    # =========================================================================
    # SESIÓN 45: NIV-045
    # =========================================================================
    {
        "code": "[NIV-045]",
        "num": 45,
        "filename": "SIMULADOR_BATERIA_CONSUMO_DISPOSITIVOS_SENIORS.html",
        "title": "Los 6 Niveles de Energía en Dispositivos: Cuidado de Baterías, Cargadores y Autonomía",
        "subtitle": "Mantén tu teléfono con batería todo el día para salir a pasear o al médico con total tranquilidad",
        "icon": "🔋",
        "initial_level": 4,
        "steps": [
            {"name": "Alerta Crítica: Menos del 15%", "tag": "APAGADO INMINENTE", "desc": "Peligro de apagado durante la calle. Activar de inmediato el 'Ahorro de batería', bajar el brillo y apagar la linterna o aplicaciones abiertas."},
            {"name": "Reserva de Emergencia (15% - 25%)", "tag": "SOLO LLAMADAS", "desc": "Suficiente para llamar a un familiar en caso de necesidad o pedir un taxi, pero no para ver vídeos ni navegar."},
            {"name": "Autonomía Media de Recados (25% - 50%)", "tag": "SALIDA CORTA", "desc": "Permite salir a hacer recados o al centro de salud durante 3 o 4 horas sin angustia."},
            {"name": "Rango Óptimo de Salud de Batería (50% - 80%)", "tag": "ZONA DE ORO", "desc": "Las baterías de litio modernas sufren menos cuando están entre el 20% y el 80%. Mantenerla en este rango alarga la vida del teléfono muchos años."},
            {"name": "Carga Completa para Días Fuera (80% - 100%)", "tag": "LISTO PARA VIAJAR", "desc": "Carga ideal antes de salir de excursión, viajar en tren o pasar todo el día fuera con los nietos."},
            {"name": "Cuidado Inteligente y Cargador Homologado", "tag": "SEGURIDAD MÁXIMA", "desc": "Cargador oficial con sello CE (sin calentamiento excesivo), cable intacto y carga sobre mesita despejada (nunca debajo de la almohada ni al sol directo)."}
        ],
        "kpis": [
            {"val": "75%", "lbl": "Nivel de Batería"},
            {"val": "14 horas", "lbl": "Autonomía Restante"},
            {"val": "Segura", "lbl": "Temperatura Batería"},
            {"val": "CE Oficial", "lbl": "Estado Cargador"}
        ],
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">⚡ Nivel Actual de Batería</span>
                    <span class="control-badge" id="bat-badge">75%</span>
                </div>
                <input type="range" id="bat-slider" min="5" max="100" value="75" oninput="updateBatteryCalc()">
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🔌 Tipo de Cargador y Cable</span>
                </div>
                <select id="charger-select" style="width:100%; padding:10px; border-radius:10px; background:rgba(0,0,0,0.5); color:#fff; border:1px solid rgba(255,255,255,0.2);" onchange="updateBatteryCalc()">
                    <option value="1">Cable deshilachado o cargador muy caliente (¡Peligro!)</option>
                    <option value="2">Cargador genérico de tienda sin marca clara</option>
                    <option value="3" selected>Cargador oficial homologado con marca CE</option>
                </select>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🔦 Consumidores Invisibles</span>
                </div>
                <label style="display:flex; align-items:center; gap:10px; color:#cbd5e1; cursor:pointer; margin-bottom:6px;">
                    <input type="checkbox" id="torch-check" onchange="updateBatteryCalc()" style="width:18px; height:18px;">
                    Linterna encendida sin querer en el bolsillo
                </label>
                <label style="display:flex; align-items:center; gap:10px; color:#cbd5e1; cursor:pointer;">
                    <input type="checkbox" id="gps-check" onchange="updateBatteryCalc()" style="width:18px; height:18px;">
                    Brillo de pantalla al 100% continuo
                </label>
            </div>

            <div style="background:rgba(245, 158, 11, 0.12); border:1px solid rgba(245, 158, 11, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#fde68a;">
                ⚠️ <b>Bulo desmentido:</b> Ya NO hace falta dejar que el teléfono se descargue al 0% para cargarlo. Eso era en los móviles viejos de hace 25 años. Las baterías actuales de litio prefieren cargas suaves en cualquier momento.
            </div>
        """,
        "script": """
        function updateBatteryCalc() {
            const bat = parseInt(document.getElementById('bat-slider').value);
            const charger = parseInt(document.getElementById('charger-select').value);
            const torch = document.getElementById('torch-check').checked;
            const bright = document.getElementById('gps-check').checked;

            document.getElementById('bat-badge').innerText = bat + "%";

            let drainFactor = 1.0;
            if (torch) drainFactor += 1.5;
            if (bright) drainFactor += 0.8;

            let hours = Math.round((bat / 5) / drainFactor);
            if (hours < 1) hours = 0.5;

            let lvl = 1;
            if (bat <= 15) lvl = 1;
            else if (bat <= 25) lvl = 2;
            else if (bat <= 50) lvl = 3;
            else if (bat <= 80) lvl = 4;
            else if (bat <= 95) lvl = 5;
            else lvl = (charger === 3) ? 6 : 5;

            document.getElementById('kpi1-val').innerText = bat + "%";
            document.getElementById('kpi2-val').innerText = hours + " horas";
            document.getElementById('kpi3-val').innerText = (torch || charger === 1) ? "Templada/Caliente" : "Fresca (Normal)";
            document.getElementById('kpi4-val').innerText = charger === 1 ? "¡Cambiar Cable!" : (charger === 2 ? "Aceptable" : "Seguro (CE)");

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un ingeniero de hardware y especialista en seguridad doméstica para personas mayores (+65).
Explícame en 3 viñetas cómo crear una herramienta interactiva en HTML que enseñe a cuidar la batería del móvil, desmitifique viejos bulos y advierta de los riesgos de cables pelados o dejar el móvil cargando bajo la almohada.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con simulador de porcentaje de batería, estimador de horas de autonomía según pantalla y linterna, comprobador de seguridad de cargadores homologados CE y desmentido de bulos de baterías de litio."""
    },

    # =========================================================================
    # SESIÓN 46: NIV-046
    # =========================================================================
    {
        "code": "[NIV-046]",
        "num": 46,
        "filename": "SIMULADOR_ROBOTICA_ASISTENTES_HOGAR_SENIORS.html",
        "title": "Los 5 Niveles de la Robótica Doméstica: Robots Aspiradores, Sensores y Asistencia Vital",
        "subtitle": "Ayudas técnicas que limpian sin agachar la espalda y protegen la independencia en casa",
        "icon": "🤖",
        "initial_level": 4,
        "steps": [
            {"name": "Esfuerzo Físico Manual Completo", "tag": "SOBRECARGA LUMBAR", "desc": "Barrer, pasar la mopa y agacharse debajo de camas y sofás. Riesgo de lumbagos, mareos por agacharse y tropiezos en la oscuridad."},
            {"name": "Sensores de Paso y Luces Nocturnas Automáticas", "tag": "PREVENCIÓN CAÍDAS", "desc": "Pequeños pilotos enchufados en el pasillo y el baño que se iluminan suavemente en cuanto detectan los pies al levantarse de noche, evitando tropezar con alfombras o puertas."},
            {"name": "Limpieza Automatizada con Robot Aspirador", "tag": "ESPALDA DESCANSADA", "desc": "Un robot redondo que barre y friega el suelo todos los días mientras sales a pasear. Limpia debajo de la cama sin que tengas que doblar la espalda ni una sola vez."},
            {"name": "Asistente de Voz y Recordatorios de Salud", "tag": "COMPAÑÍA Y MEMORIA", "desc": "Un altavoz inteligente en el salón que avisa con cariño: 'Son las 14:00, hora de la pastilla de la tensión', pone música de tu época o llama a tu hijo con solo pedírselo por voz."},
            {"name": "Escudo de Autonomía Plena y Teleasistencia SOS", "tag": "INDEPENDENCIA TOTAL", "desc": "Reloj de muñeca discreto con detección automática de caídas y botón de socorro conectado 24 horas. Tranquilidad absoluta para ti y tus familiares sabiendo que nunca estás desamparado."}
        ],
        "kpis": [
            {"val": "18 horas", "lbl": "Esfuerzo Ahorrado/Mes"},
            {"val": "98%", "lbl": "Seguridad Nocturna"},
            {"val": "Activa 24h", "lbl": "Teleasistencia SOS"},
            {"val": "Máxima", "lbl": "Autonomía en Casa"}
        ],
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🏠 Ayudas Instaladas en Casa</span>
                </div>
                <label style="display:flex; align-items:center; gap:10px; color:#cbd5e1; cursor:pointer; margin-bottom:6px;">
                    <input type="checkbox" id="light-check" checked onchange="updateRoboticsCalc()" style="width:18px; height:18px;">
                    Luces automáticas con sensor en el pasillo
                </label>
                <label style="display:flex; align-items:center; gap:10px; color:#cbd5e1; cursor:pointer; margin-bottom:6px;">
                    <input type="checkbox" id="vacuum-check" checked onchange="updateRoboticsCalc()" style="width:18px; height:18px;">
                    Robot aspirador para barrer debajo de camas
                </label>
                <label style="display:flex; align-items:center; gap:10px; color:#cbd5e1; cursor:pointer; margin-bottom:6px;">
                    <input type="checkbox" id="voice-check" checked onchange="updateRoboticsCalc()" style="width:18px; height:18px;">
                    Asistente de voz para recordatorios de pastillas
                </label>
                <label style="display:flex; align-items:center; gap:10px; color:#cbd5e1; cursor:pointer;">
                    <input type="checkbox" id="sos-check" onchange="updateRoboticsCalc()" style="width:18px; height:18px;">
                    Reloj con detección de caídas y botón SOS
                </label>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🧹 Superficie de la Casa</span>
                    <span class="control-badge" id="area-badge">90 m²</span>
                </div>
                <input type="range" id="area-slider" min="50" max="150" step="10" value="90" oninput="updateRoboticsCalc()">
            </div>

            <div style="background:rgba(16, 185, 129, 0.12); border:1px solid rgba(16, 185, 129, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#a7f3d0;">
                🌱 <b>La tecnología que regala libertad:</b> Los robots domésticos no están para sustituir a las personas, sino para quitarte las tareas pesadas y peligrosas de agacharte, permitiéndote vivir en tu propia casa con independencia, comodidad y seguridad por muchos más años.
            </div>
        """,
        "script": """
        function updateRoboticsCalc() {
            const light = document.getElementById('light-check').checked;
            const vacuum = document.getElementById('vacuum-check').checked;
            const voice = document.getElementById('voice-check').checked;
            const sos = document.getElementById('sos-check').checked;
            const area = parseInt(document.getElementById('area-slider').value);

            document.getElementById('area-badge').innerText = area + " m²";

            let savedHours = 0;
            if (vacuum) savedHours += Math.round(area * 0.2); // ~18h al mes

            let lvl = 1;
            if (!light && !vacuum && !voice && !sos) lvl = 1;
            else if (light && !vacuum && !voice && !sos) lvl = 2;
            else if (vacuum && !sos) lvl = voice ? 4 : 3;
            else if (sos) lvl = 5;
            else lvl = 3;

            document.getElementById('kpi1-val').innerText = savedHours + " h/mes";
            document.getElementById('kpi2-val').innerText = light ? "98% (Protegido)" : "35% (Riesgo Tropiezo)";
            document.getElementById('kpi3-val').innerText = sos ? "Activa 24h" : "No equipada";
            document.getElementById('kpi4-val').innerText = lvl >= 4 ? "Excelente" : "Básica";

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un terapeuta ocupacional y pedagogo en gerontotecnología para personas mayores (+65).
Explícame en 3 viñetas cómo diseñar un simulador interactivo en HTML que muestre cómo los robots aspiradores y sensores de luz nocturna evitan dolores de espalda y tropiezos en casa.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con checklist de equipamiento doméstico (sensores nocturnos, robot aspirador, avisos por voz, reloj SOS), calculadora de horas de esfuerzo físico ahorradas y medidor de autonomía e independencia en el hogar."""
    },

    # =========================================================================
    # SESIÓN 47: NIV-047
    # =========================================================================
    {
        "code": "[NIV-047]",
        "num": 47,
        "filename": "SIMULADOR_VIAJES_VIRTUALES_ESTIMULACION_SENIORS.html",
        "title": "Los 6 Niveles de Exploración Virtual, Viajes sin Salir de Casa y Estimulación Sensorial",
        "subtitle": "Pasea por el pueblo donde creciste, visita museos mundiales y estimula la memoria desde tu sillón",
        "icon": "🌍",
        "initial_level": 4,
        "steps": [
            {"name": "Fotografía Tradicional de Archivo", "tag": "ÁLBUM EN PAPEL", "desc": "Mirar fotos fijas en un álbum de papel. Despierta recuerdos queridos, pero sin la sensación inmersiva de pasear por el lugar."},
            {"name": "Búsqueda Guiada en Pantalla", "tag": "IMÁGENES EN RED", "desc": "Ver fotos actuales del pueblo o de ciudades históricas en internet para comprobar cómo han cambiado las plazas y las calles."},
            {"name": "Paseo Callejero en 360° (Street View)", "tag": "INMERSIÓN EN EL PUEBLO", "desc": "Caminar virtualmente por la calle donde naciste, acercarte a la puerta de la iglesia o a la casa familiar moviendo el dedo en la tablet como si estuvieras allí."},
            {"name": "Visitas Virtuales a Museos en Alta Resolución", "tag": "CULTURA AL DETALLE", "desc": "Recorrer las salas del Museo del Prado o la Alhambra de Granada pudiendo acercar el zoom para ver cada pincelada de Velázquez mejor que en persona."},
            {"name": "Sonidos de la Naturaleza y Calma Inmersiva", "tag": "RELAJACIÓN SENSORIAL", "desc": "Vídeos en pantalla completa con el sonido relajante de olas de mar, arroyos o cantos de pájaros que bajan el pulso y alivian la tensión o el insomnio."},
            {"name": "Viaje Compartido Intergeneracional", "tag": "CONEXIÓN CON NIETOS", "desc": "Pasear virtualmente por la pantalla de la televisión con los nietos, enseñándoles dónde jugabas de pequeño mientras narras historias familiares con total viveza."}
        ],
        "kpis": [
            {"val": "92%", "lbl": "Estimulación Cognitiva"},
            {"val": "Alta", "lbl": "Evocación Afectiva"},
            {"val": "Óptima", "lbl": "Calma y Relajación"},
            {"val": "Muy Fuerte", "lbl": "Vínculo Familiar"}
        ],
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🏛️ Destino Virtual Seleccionado</span>
                </div>
                <select id="dest-select" style="width:100%; padding:10px; border-radius:10px; background:rgba(0,0,0,0.5); color:#fff; border:1px solid rgba(255,255,255,0.2);" onchange="updateTravelCalc()">
                    <option value="1">El pueblo natal / Calles de la infancia (Memoria autobiográfica)</option>
                    <option value="2" selected>Museo del Prado: Las Meninas en ultra-alta resolución</option>
                    <option value="3">La Alhambra de Granada y sus jardines con sonido de agua</option>
                    <option value="4">Paseo por la orilla del mar en calma al atardecer</option>
                </select>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">📺 Dispositivo de Visualización</span>
                </div>
                <select id="device-select" style="width:100%; padding:10px; border-radius:10px; background:rgba(0,0,0,0.5); color:#fff; border:1px solid rgba(255,255,255,0.2);" onchange="updateTravelCalc()">
                    <option value="1">Pantalla del teléfono móvil (Pequeña)</option>
                    <option value="2">Tablet en las manos (Cómoda e interactiva)</option>
                    <option value="3" selected>Televisión del salón conectada en grande</option>
                </select>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">👨‍👩‍👧 Compañía del Viaje</span>
                </div>
                <label style="display:flex; align-items:center; gap:10px; color:#cbd5e1; cursor:pointer;">
                    <input type="checkbox" id="grandkids-check" checked onchange="updateTravelCalc()" style="width:18px; height:18px;">
                    Compartido con hijos o nietos contando anécdotas
                </label>
            </div>

            <div style="background:rgba(56, 189, 248, 0.1); border:1px solid rgba(56, 189, 248, 0.3); border-radius:12px; padding:12px; font-size:0.85rem; color:#cbd5e1;">
                🧠 <b>Terapia de Reminiscencia Cognitiva:</b> Pasear por las calles de la infancia mediante herramientas gratuitas en pantalla activa los circuitos de la memoria a largo plazo y genera emociones de alegría y arraigo muy beneficiosas para el cerebro maduro.
            </div>
        """,
        "script": """
        function updateTravelCalc() {
            const dest = parseInt(document.getElementById('dest-select').value);
            const dev = parseInt(document.getElementById('device-select').value);
            const withKids = document.getElementById('grandkids-check').checked;

            let lvl = 3;
            if (dest === 1) lvl = withKids ? 6 : 3;
            else if (dest === 2) lvl = 4;
            else if (dest === 3) lvl = 5;
            else lvl = 5;

            if (dev === 3 && withKids) lvl = 6;

            let cog = dest === 1 ? "95%" : (dest === 2 ? "90%" : "85%");
            let calma = dest === 4 ? "Máxima (Plena)" : "Alta";

            document.getElementById('kpi1-val').innerText = cog;
            document.getElementById('kpi2-val').innerText = withKids ? "Muy Emocionante" : "Serena";
            document.getElementById('kpi3-val').innerText = calma;
            document.getElementById('kpi4-val').innerText = withKids ? "Fortalecido" : "Individual";

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un neuropsicólogo y divulgador cultural para personas mayores (+65).
Explícame en 3 viñetas cómo crear una herramienta interactiva en HTML que anime a los mayores a pasear por su pueblo natal y visitar museos desde la pantalla del salón, explicando los beneficios de la reminiscencia para la memoria.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con selector de destinos virtuales (calles del pueblo, museos, naturaleza), selección de pantalla (tablet, televisor), medidor de estimulación cognitiva y guía para compartir recuerdos con los nietos."""
    },

    # =========================================================================
    # SESIÓN 48: NIV-048
    # =========================================================================
    {
        "code": "[NIV-048]",
        "num": 48,
        "filename": "SIMULADOR_EFICIENCIA_ELECTRODOMESTICOS_FACTURA_SENIORS.html",
        "title": "Los 5 Niveles de Eficiencia en Electrodomésticos: Ahorro de Luz y Manejo Sencillo",
        "subtitle": "Aprende a usar los programas 'Eco', desmitifica la etiqueta energética y recorta la factura eléctrica",
        "icon": "⚡",
        "initial_level": 4,
        "steps": [
            {"name": "Despilfarro Involuntario y Consumo Fantasma", "tag": "FACTURA ELEVADA", "desc": "Lavados siempre con agua muy caliente (60°C), aparatos en 'standby' con la lucecita roja encendida todo el año y frigorífico con hielo en las paredes."},
            {"name": "Hábitos Básicos de Apagado", "tag": "PRIMER ALIVIO", "desc": "Apagar luces de habitaciones vacías, descongelar el congelador una vez al año para que no fuerce el motor y tapar las cacerolas al cocinar para calentar antes."},
            {"name": "Uso Inteligente del Programa 'Eco'", "tag": "50% MENOS LUZ", "desc": "Poner la lavadora y el lavavajillas en programa 'Eco'. Aunque tarda un poco más, no calienta el agua a temperaturas exageradas y gasta la mitad de electricidad dejando la ropa impecable."},
            {"name": "Regletas con Interruptor y Termostato a 21°C", "tag": "BLINDAJE DE CONSUMO", "desc": "Apagar la regleta de la televisión por la noche (ahorro de 45 € al año) y mantener la calefacción a 21°C estables sin picos de calor que disparan el recibo."},
            {"name": "Eficiencia Máxima con Tecnología Inverter", "tag": "HOGAR ACCESIBLE Y EFICIENTE", "desc": "Electrodomésticos modernos clase A o B con motores inverter silenciosos que consumen un tercio que los antiguos, con iluminación LED cálida en toda la casa."}
        ],
        "kpis": [
            {"val": "165 €/año", "lbl": "Ahorro Estimado"},
            {"val": "Clase A/B", "lbl": "Etiqueta Eficiente"},
            {"val": "Eco 30°C", "lbl": "Lavado Inteligente"},
            {"val": "45 €/año", "lbl": "Ahorro Regletas Standby"}
        ],
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🧺 Modo de Lavado Habitual</span>
                </div>
                <select id="wash-select" style="width:100%; padding:10px; border-radius:10px; background:rgba(0,0,0,0.5); color:#fff; border:1px solid rgba(255,255,255,0.2);" onchange="updateEnergyCalc()">
                    <option value="1">Programa Rápido / Caliente a 60°C (Gasto Alto)</option>
                    <option value="2" selected>Programa 'Eco' a 30°C / Frío (Ahorro del 60% en luz)</option>
                </select>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🔴 Lucecita Roja de Televisión (Standby)</span>
                </div>
                <label style="display:flex; align-items:center; gap:10px; color:#cbd5e1; cursor:pointer;">
                    <input type="checkbox" id="strip-check" checked onchange="updateEnergyCalc()" style="width:18px; height:18px;">
                    Uso regleta con botón para apagar tele y equipos de noche
                </label>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">❄️ Ajuste del Frigorífico</span>
                </div>
                <select id="fridge-select" style="width:100%; padding:10px; border-radius:10px; background:rgba(0,0,0,0.5); color:#fff; border:1px solid rgba(255,255,255,0.2);" onchange="updateEnergyCalc()">
                    <option value="cold">Puesto a 2°C (Demasiado frío, escarcha innecesaria)</option>
                    <option value="opt" selected>Puesto a 4°C o 5°C (Perfecto según Sanidad)</option>
                </select>
            </div>

            <div style="background:rgba(245, 158, 11, 0.12); border:1px solid rgba(245, 158, 11, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#fde68a;">
                💡 <b>¿Por qué el programa 'Eco' tarda más pero gasta menos?</b> Porque el 85% de la luz de la lavadora se gasta en calentar el agua de golpe con una resistencia. El programa Eco usa agua templada y lava con más calma: gasta poquísima luz y cuida mejor los tejidos de la ropa.
            </div>
        """,
        "script": """
        function updateEnergyCalc() {
            const wash = parseInt(document.getElementById('wash-select').value);
            const strip = document.getElementById('strip-check').checked;
            const fridge = document.getElementById('fridge-select').value;

            let ahorroTotal = 0;
            if (wash === 2) ahorroTotal += 75; // 75€/año por lavar en eco
            if (strip) ahorroTotal += 45;       // 45€ por regletas
            if (fridge === 'opt') ahorroTotal += 45; // 45€ por no sobreenfriar

            let lvl = 1;
            if (wash === 1 && !strip && fridge === 'cold') lvl = 1;
            else if (wash === 1 && strip) lvl = 2;
            else if (wash === 2 && !strip) lvl = 3;
            else if (wash === 2 && strip && fridge === 'opt') lvl = 4;
            else lvl = 5;

            document.getElementById('kpi1-val').innerText = ahorroTotal + " €/año";
            document.getElementById('kpi2-val').innerText = lvl >= 4 ? "Clase A/B" : (lvl >= 3 ? "Clase C/D" : "Clase F");
            document.getElementById('kpi3-val').innerText = wash === 2 ? "Eco 30°C" : "Intensivo 60°C";
            document.getElementById('kpi4-val').innerText = strip ? "45 € Ahorrados" : "Consumo Fantasma";

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un asesor energético y divulgador de economía doméstica para personas mayores (+65).
Explícame en 3 viñetas cómo crear una calculadora interactiva en HTML que explique cómo usar el programa Eco de la lavadora y apagar las regletas para recortar la factura de la luz sin pasar frío ni complicaciones.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con calculadora de ahorro eléctrico anual en euros, selector de programas de lavado (eco vs caliente), ajuste óptimo del frigorífico a 4°C, semáforo de etiquetas energéticas y explicación del consumo fantasma (standby)."""
    },

    # =========================================================================
    # SESIÓN 49: NIV-049
    # =========================================================================
    {
        "code": "[NIV-049]",
        "num": 49,
        "filename": "SIMULADOR_TRAMITES_DIGITALES_CERTIFICADO_SENIORS.html",
        "title": "Los 6 Niveles de Trámites Digitales: Certificado Digital, Cl@ve y Citas Médicas sin Colas",
        "subtitle": "Realiza gestiones oficiales desde casa sin madrugar, pasar frío en colas ni pedir favores",
        "icon": "🏛️",
        "initial_level": 4,
        "steps": [
            {"name": "Dependencia Presencial Total y Madrugones", "tag": "COLAS Y FRÍO", "desc": "Tener que levantarse a las 7:30 de la mañana para hacer cola en la puerta del centro de salud o en la Seguridad Social bajo el frío para pedir una cita o un papel."},
            {"name": "Cita Telefónica Automatizada", "tag": "ESPERAS EN LÍNEA", "desc": "Llamar por teléfono al contestador de citas. A menudo comunica o cuesta entender a la locución automática si hay prisa."},
            {"name": "Cita Médica en 30 Segundos por App del Móvil", "tag": "GESTIÓN FÁCIL", "desc": "Tener la aplicación oficial de salud de tu comunidad autónoma en el móvil con tu número de tarjeta sanitaria guardado: eliges médico, día y hora sentado en el sofá."},
            {"name": "Acceso Sencillo con Cl@ve Pin por SMS", "tag": "SIN INSTALACIONES", "desc": "Sistema oficial del Estado que te manda un código de 3 letras al móvil por SMS. Te permite entrar a consultar tu pensión o la renta sin tener que instalar nada complicado."},
            {"name": "Certificado Digital Instalado en el Navegador", "tag": "DNI EN CASA", "desc": "Tu firma electrónica oficial en el ordenador. Permite descargar volantes de empadronamiento, informes de vida laboral o certificados de pensión con un solo clic."},
            {"name": "Soberanía Digital Plena y Serenidad Ciudadana", "tag": "AUTONOMÍA TOTAL", "desc": "Realizas cualquier gestión de tus derechos ciudadanos desde casa a tu ritmo, con la seguridad de saber identificar siempre las páginas oficiales legítimas que terminan en '.gob.es'."}
        ],
        "kpis": [
            {"val": "14 horas", "lbl": "Tiempo Ahorrado/Año"},
            {"val": "100%", "lbl": "Webs Seguras (.gob.es)"},
            {"val": "Cl@ve SMS", "lbl": "Acceso Rápido"},
            {"val": "Máxima", "lbl": "Autonomía Personal"}
        ],
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">📋 Trámite que Deseas Realizar</span>
                </div>
                <select id="proc-select" style="width:100%; padding:10px; border-radius:10px; background:rgba(0,0,0,0.5); color:#fff; border:1px solid rgba(255,255,255,0.2);" onchange="updateDigitalProcCalc()">
                    <option value="1">Pedir o cambiar cita con el médico de cabecera</option>
                    <option value="2" selected>Descargar el justificante de la pensión revalorizada</option>
                    <option value="3">Consultar la tarjeta sanitaria europea para viajar</option>
                    <option value="4">Obtener el volante de empadronamiento municipal</option>
                </select>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🔑 Método de Acceso Elegido</span>
                </div>
                <select id="auth-select" style="width:100%; padding:10px; border-radius:10px; background:rgba(0,0,0,0.5); color:#fff; border:1px solid rgba(255,255,255,0.2);" onchange="updateDigitalProcCalc()">
                    <option value="1">Presencial en ventanilla (Cola física)</option>
                    <option value="2">Por teléfono de atención al ciudadano</option>
                    <option value="3">Por App de salud con número de tarjeta</option>
                    <option value="4" selected>Sistema Cl@ve Pin con código al móvil por SMS</option>
                    <option value="5">Certificado Digital instalado en el ordenador</option>
                </select>
            </div>

            <div style="background:rgba(16, 185, 129, 0.12); border:1px solid rgba(16, 185, 129, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#a7f3d0;">
                🛡️ <b>La Regla de Oro de las Webs Oficiales:</b> Fíjate siempre en la dirección de arriba del navegador. Todas las páginas legítimas de la Seguridad Social, Hacienda o Ministerios de España terminan en <b>.gob.es</b> (con 'b' de gobierno). Si termina en .com o .org y te pide dinero por un trámite, ¡salte!
            </div>
        """,
        "script": """
        function updateDigitalProcCalc() {
            const auth = parseInt(document.getElementById('auth-select').value);

            let lvl = auth;
            let timeSaved = "0 horas";
            let autonomy = "Baja";

            if (auth === 1) {
                lvl = 1;
                timeSaved = "0 horas (Colas)";
                autonomy = "Dependiente";
            } else if (auth === 2) {
                lvl = 2;
                timeSaved = "2 h/año";
                autonomy = "Básica";
            } else if (auth === 3) {
                lvl = 3;
                timeSaved = "8 h/año";
                autonomy = "Buena";
            } else if (auth === 4) {
                lvl = 4;
                timeSaved = "14 h/año";
                autonomy = "Muy Alta";
            } else {
                lvl = 6;
                timeSaved = "20 h/año";
                autonomy = "Soberanía Plena";
            }

            document.getElementById('kpi1-val').innerText = timeSaved;
            document.getElementById('kpi2-val').innerText = "100% (.gob.es)";
            document.getElementById('kpi3-val').innerText = auth >= 4 ? "Digital Seguro" : "Tradicional";
            document.getElementById('kpi4-val').innerText = autonomy;

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un mediador administrativo y pedagogo de alfabetización digital para personas mayores (+65).
Explícame en 3 viñetas cómo diseñar un simulador interactivo en HTML que enseñe a pedir cita médica y descargar certificados de pensión mediante Cl@ve Pin sin necesidad de hacer colas en ventanilla.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con simulador de trámites frecuentes (cita médica, justificante de pensión, empadronamiento), comparador de métodos de acceso (presencial vs Cl@ve SMS vs Certificado Digital), calculadora de horas ahorradas en colas y filtro de webs oficiales seguras (.gob.es)."""
    },

    # =========================================================================
    # SESIÓN 50: NIV-050
    # =========================================================================
    {
        "code": "[NIV-050]",
        "num": 50,
        "filename": "SIMULADOR_COMUNICACION_WHATSAPP_CONVIVENCIA_SENIORS.html",
        "title": "Los 5 Niveles de Comunicación Digital: WhatsApp Familiar, Grupos y Convivencia Serena",
        "subtitle": "Disfruta de la comunicación con hijos y amigos sin agobios, cadenas molestas ni noticias falsas",
        "icon": "💬",
        "initial_level": 4,
        "steps": [
            {"name": "Saturación y Angustia por Avisos Continuos", "tag": "AGOBIO SONORO", "desc": "Grupos de vecinos o conocidos sonando a todas horas. Sensación de obligación de contestar al momento y confusión con botones pequeños."},
            {"name": "Escritura Tecla a Tecla con Dificultad", "tag": "CANSANCIO EN DEDOS", "desc": "Intentar escribir mensajes largos letra por letra en la pantalla pequeña. Borrar varias veces por equivocación y tardar 10 minutos en una frase sencilla."},
            {"name": "Comunicación Fluida mediante Dictado por Voz", "tag": "EL TRUCO DEL MICRÓFONO", "desc": "Pulsar el icono del micrófono del teclado y hablar con naturalidad: el teléfono escribe solo todo lo que dices con perfecta ortografía sin tocar letras."},
            {"name": "Grupos Silenciados y Paz Mental Garantizada", "tag": "SILENCIAR PARA SIEMPRE", "desc": "Aprender a 'Silenciar grupo para siempre'. Los mensajes siguen ahí para cuando te apetezca leerlos, pero el teléfono no pita ni vibra jamás. ¡Nadie se entera de que lo has silenciado!"},
            {"name": "Filtro Natural de Bulos y Conexión Afectuosa", "tag": "SABIDURÍA DIGITAL", "desc": "No reenviar cadenas alarmistas ('Reenvía a 10 contactos o cobrarán'). Compartir fotos de momentos bonitos con los nietos y llamadas familiares con alegría y serenidad."}
        ],
        "kpis": [
            {"val": "100%", "lbl": "Paz Mental"},
            {"val": "Por Voz", "lbl": "Dictado Rápido"},
            {"val": "Silenciados", "lbl": "Grupos Ruidosos"},
            {"val": "0 Bulos", "lbl": "Filtro de Cadenas"}
        ],
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🎙️ Cómo Enviar Mensajes</span>
                </div>
                <select id="input-select" style="width:100%; padding:10px; border-radius:10px; background:rgba(0,0,0,0.5); color:#fff; border:1px solid rgba(255,255,255,0.2);" onchange="updateWhatsappCalc()">
                    <option value="1">Escribiendo letra por letra despacio en el teclado</option>
                    <option value="2" selected>Dictando con la voz al micrófono del teclado</option>
                    <option value="3">Grabando un mensaje de audio breve (Nota de voz)</option>
                </select>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🔕 Estado de Grupos Numerosos</span>
                </div>
                <label style="display:flex; align-items:center; gap:10px; color:#cbd5e1; cursor:pointer;">
                    <input type="checkbox" id="mute-check" checked onchange="updateWhatsappCalc()" style="width:18px; height:18px;">
                    Silenciar grupos ruidosos 'Para Siempre'
                </label>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🛑 Detector de Cadenas y Bulos</span>
                </div>
                <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.1); border-radius:10px; padding:10px; font-size:0.85rem; color:#cbd5e1;">
                    Regla de oro: Si un mensaje dice <i>"Reenvía esto a todos tus contactos o te cerrarán la cuenta"</i> o promete regalos milagro, <b>es 100% mentira</b>. Bórralo sin reenviar y mantendrás limpio tu chat.
                </div>
            </div>

            <div style="background:rgba(16, 185, 129, 0.12); border:1px solid rgba(16, 185, 129, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#a7f3d0;">
                ❤️ <b>WhatsApp a tu servicio, no tú al servicio del móvil:</b> El teléfono es una herramienta para acercarte a quienes quieres, no para agobiarte. No hay ninguna prisa por contestar de inmediato; las cosas importantes se avisan por llamada.
            </div>
        """,
        "script": """
        function updateWhatsappCalc() {
            const inp = parseInt(document.getElementById('input-select').value);
            const mute = document.getElementById('mute-check').checked;

            let lvl = 2;
            if (!mute && inp === 1) lvl = 1;
            else if (mute && inp === 1) lvl = 2;
            else if (!mute && inp === 2) lvl = 3;
            else if (mute && inp === 2) lvl = 4;
            else if (mute && inp === 3) lvl = 5;

            document.getElementById('kpi1-val').innerText = mute ? "100% (Paz Mental)" : "30% (Pitidos Continuos)";
            document.getElementById('kpi2-val').innerText = inp === 1 ? "Lento (Teclado)" : (inp === 2 ? "Rápido (Dictado)" : "Audio Directo");
            document.getElementById('kpi3-val').innerText = mute ? "Silenciados" : "Sonando";
            document.getElementById('kpi4-val').innerText = "0 Bulos";

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un pedagogo de convivencia digital y relaciones familiares para personas mayores (+65).
Explícame en 3 viñetas cómo crear una guía interactiva en HTML que enseñe a silenciar grupos ruidosos de WhatsApp sin salirse, dictar mensajes por voz y no reenviar cadenas o noticias falsas.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con simulador de dictado por voz frente al teclado tradicional, botón interactivo para 'Silenciar grupo para siempre', detector de cadenas de mensajes falsos y decálogo de convivencia serena en WhatsApp."""
    }
]

def main():
    print("=== Generando las 10 Micro-Apps Interactivas Senior (+65) de LOTE 5 ===")
    
    for app in APPS:
        code = app["code"]
        num = app["num"]
        fn = app["filename"]
        title = app["title"]
        subtitle = app["subtitle"]
        icon = app["icon"]
        steps = app["steps"]
        kpis = app["kpis"]
        initial_lvl = app["initial_level"]
        aside = app["aside"]
        script = app["script"]
        seed = app["prompt_seed"]
        master = app["prompt_master"]

        html_content = generate_html_microapp(
            code, num, title, subtitle, icon, steps, kpis, initial_lvl, aside, script, seed, master
        )

        # 1. Guardar en SIMULADORES_INTERACTIVOS/01_SIMULADORES/ con ambos nombres (con prefijo y sin él)
        sim_path_prefix = os.path.join(SIM_DIR, f"{num:02d}_{fn}")
        sim_path_clean = os.path.join(SIM_DIR, fn)
        with open(sim_path_prefix, "w", encoding="utf-8") as f:
            f.write(html_content)
        with open(sim_path_clean, "w", encoding="utf-8") as f:
            f.write(html_content)

        # 2. Guardar en la carpeta de sesión de Classroom correspondiente
        sess_folder = os.path.join(SESSIONS_DIR, f"{num:02d}_Sesion")
        os.makedirs(sess_folder, exist_ok=True)
        sess_path = os.path.join(sess_folder, fn)
        with open(sess_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        # Copia de compatibilidad con prefijo de sesión
        sess_path_prefix = os.path.join(sess_folder, f"{num:02d}_{fn}")
        with open(sess_path_prefix, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"  ✓ [{code}] Sesión {num:02d}: {fn} generada y distribuida.")

    print(f"\n¡Éxito! Las 10 Micro-Apps de Lote 5 han sido generadas y sincronizadas con éxito.")

if __name__ == "__main__":
    main()

