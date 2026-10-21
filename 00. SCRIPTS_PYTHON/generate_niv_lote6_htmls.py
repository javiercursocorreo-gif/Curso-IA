#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_niv_lote6_htmls.py
Genera de forma autónoma las 10 Micro-Aplicaciones Interactivas Senior (+65)
para las Sesiones 51 a 60 (Lote 6 - Final del Proyecto) bajo la Triple Salvaguarda Pedagógica.
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

        select {
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 10px 14px;
            color: #f8fafc;
            font-size: 0.95rem;
            font-family: var(--font-sans);
            outline: none;
            cursor: pointer;
            width: 100%;
        }
        select:focus {
            border-color: var(--cyan);
            box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
        }

        .checkbox-row {
            display: flex;
            align-items: center;
            gap: 12px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 10px;
            padding: 10px 14px;
            cursor: pointer;
            transition: background 0.2s;
        }
        .checkbox-row:hover {
            background: rgba(255, 255, 255, 0.08);
        }
        .checkbox-row input[type="checkbox"] {
            width: 20px;
            height: 20px;
            cursor: pointer;
            accent-color: var(--primary);
        }
        .checkbox-label {
            font-size: 0.9rem;
            color: #cbd5e1;
            font-weight: 600;
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

# =============================================================================
# DEFINICIÓN DE LAS 10 MICRO-APPS INTERACTIVAS SENIOR (+65) — LOTE 6
# =============================================================================

APPS = [
    # -------------------------------------------------------------------------
    # SESIÓN 51: NIV-051
    # -------------------------------------------------------------------------
    {
        "code": "[NIV-051]",
        "num": 51,
        "filename": "SIMULADOR_ARQUITECTURA_HOGAR_ACCESIBLE_SENIORS.html",
        "title": "Los 6 Niveles de Altura, Escaleras y Accesibilidad: Diseñar un Hogar sin Barreras",
        "subtitle": "Eliminación de obstáculos, cotas seguras, rampas y adaptación del hogar para una autonomía vitalicia",
        "icon": "🏛️",
        "steps": [
            {
                "name": "Cota Cero Absoluta (Plato de Ducha Enrasado y Cero Resaltes)",
                "tag": "Suelo 100% Plano",
                "desc": "Eliminación total de resaltes en el pavimento, puertas sin bisel elevado y plato de ducha enrasado al nivel del suelo sin bordillo ni escalón alguno."
            },
            {
                "name": "Bordillo de Entrada con Rampa Suave (< 6% de Pendiente)",
                "tag": "Rampa Antideslizante",
                "desc": "Resolución de pequeños desniveles de entrada o terrazas mediante rampas suaves de pendiente inferior al 6% con superficie rugosa que no resbala al llover."
            },
            {
                "name": "Escalera con Doble Pasamanos y Peldaños Contrastados",
                "tag": "Tramo Seguro",
                "desc": "Pasamanos continuo y firme a ambos lados a 90 cm de altura, iluminación cenital sin sombras y aristas de cada peldaño señalizadas con cinta reflectante antideslizante."
            },
            {
                "name": "Silla Salvaescaleras o Plataforma Motorizada",
                "tag": "Elevación Mecánica",
                "desc": "Mecanismo electromecánico suave instalado en la barandilla para subir entre plantas en viviendas unifamiliares con total seguridad y cero sobreesfuerzo articular."
            },
            {
                "name": "Ascensor Comunitario Bajado a Cota Cero en Portal",
                "tag": "Portal sin Peldaños",
                "desc": "Reforma del portal comunitario bajando el ascensor a nivel de calle o instalando rampa reglamentaria para eliminar los 3-5 peldaños previos de entrada."
            },
            {
                "name": "Hábitat Universal y Accesibilidad Plena (+65)",
                "tag": "Autonomía Vitalicia",
                "desc": "Puertas de 82 cm de paso libre para andadores o sillas de ruedas, pasillos despejados de más de 1 metro y espacio de giro de 1,5 metros en baño y cocina."
            }
        ],
        "kpis": [
            {"val": "0 cm", "lbl": "Altura Resalte"},
            {"val": "4.2%", "lbl": "Pendiente Rampa"},
            {"val": "0%", "lbl": "Riesgo Caídas"},
            {"val": "100%", "lbl": "Autonomía Plena"}
        ],
        "initial_level": 1,
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🏢 Tipo de Vivienda y Acceso</span>
                </div>
                <select id="vivienda-select" onchange="updateAccesibilidadCalc()">
                    <option value="1">Piso moderno con ascensor a cota cero</option>
                    <option value="2">Portal antiguo con 4 peldaños previos</option>
                    <option value="3">Vivienda unifamiliar con escalera de piso</option>
                    <option value="4">Casa baja con resalte en la acera</option>
                </select>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">📐 Altura del Mayor Resalte</span>
                    <span class="control-badge" id="resalte-badge">0 cm</span>
                </div>
                <input type="range" id="resalte-range" min="0" max="25" value="0" step="1" oninput="updateAccesibilidadCalc()">
            </div>

            <div class="control-group">
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-ducha" checked onchange="updateAccesibilidadCalc()">
                    <span class="checkbox-label">🚿 Plato de ducha plano (sin escalón de bañera)</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-pasamanos" checked onchange="updateAccesibilidadCalc()">
                    <span class="checkbox-label">🦯 Doble pasamanos continuo a ambos lados</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-alfombras" checked onchange="updateAccesibilidadCalc()">
                    <span class="checkbox-label">🧹 Alfombras retiradas o fijadas con base de goma</span>
                </div>
            </div>

            <div style="background:rgba(16, 185, 129, 0.12); border:1px solid rgba(16, 185, 129, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#a7f3d0;">
                💡 <b>La regla de oro de la cota cero:</b> El 70% de las caídas domésticas ocurren por tropezar con bordillos de duchas o alfombrillas sueltas. Una reforma a cota cero regala 20 años de tranquilidad.
            </div>
        """,
        "script": """
        function updateAccesibilidadCalc() {
            const viv = parseInt(document.getElementById('vivienda-select').value);
            const resalte = parseInt(document.getElementById('resalte-range').value);
            const ducha = document.getElementById('chk-ducha').checked;
            const pasamanos = document.getElementById('chk-pasamanos').checked;
            const alfombras = document.getElementById('chk-alfombras').checked;

            document.getElementById('resalte-badge').innerText = resalte + " cm";

            let lvl = 1;
            if (resalte === 0 && ducha && alfombras) {
                lvl = viv === 1 ? 6 : 1;
            } else if (resalte > 0 && resalte <= 8) {
                lvl = 2;
            } else if (resalte > 8 && viv === 2) {
                lvl = 5;
            } else if (viv === 3 && !pasamanos) {
                lvl = 3;
            } else if (viv === 3 && pasamanos) {
                lvl = 4;
            } else {
                lvl = 2;
            }

            const pend = resalte === 0 ? "0%" : (resalte * 0.8).toFixed(1) + "%";
            document.getElementById('kpi1-val').innerText = resalte + " cm";
            document.getElementById('kpi2-val').innerText = pend;
            document.getElementById('kpi3-val').innerText = (ducha && alfombras && resalte < 3) ? "0% (Seguro)" : "35% (Alerta)";
            document.getElementById('kpi4-val').innerText = (lvl >= 5 || lvl === 1) ? "100% Plena" : "75% Buena";

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un arquitecto técnico y terapeuta ocupacional especializado en diseño accesible para personas mayores (+65).
Explícame en 3 viñetas cómo diseñar un simulador interactivo en HTML que enseñe a eliminar barreras arquitectónicas en el hogar, sustituyendo la bañera por ducha a cota cero y adaptando desniveles con rampas suaves.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con selector de vivienda (piso cota cero, portal con escalones, chalet), deslizador de altura de resaltes (0-25 cm), semáforo de riesgo de caídas domésticas y guía de ayudas públicas para reformas de accesibilidad."""
    },

    # -------------------------------------------------------------------------
    # SESIÓN 52: NIV-052
    # -------------------------------------------------------------------------
    {
        "code": "[NIV-052]",
        "num": 52,
        "filename": "SIMULADOR_CIUDAD_AMIGABLE_URBANISMO_SENIORS.html",
        "title": "Los 5 Niveles de la Ciudad Amigable con las Personas Mayores: Calles, Bancos y Vida de Barrio",
        "subtitle": "Urbanismo accesible según la OMS: aceras anchas, bancos con respaldo para descansar, semáforos con tiempo y comercio de cercanía",
        "icon": "🌳",
        "steps": [
            {
                "name": "Ciudad Barrera (Aceras Estrechas y Semáforos Cortos)",
                "tag": "Entorno Inseguro",
                "desc": "Aceras rotas con obstáculos, cruces semafóricos de menos de 12 segundos y ausencia de sombras que expulsan a los vecinos mayores de la calle."
            },
            {
                "name": "Urbanismo Básico sin Confort de Descanso",
                "tag": "Calle Transeúnte",
                "desc": "Pavimento regular pero sin asientos públicos ni fuentes de agua potable en los trayectos cotidianos, obligando a caminatas sin respiro."
            },
            {
                "name": "Ciudad de Proximidad o de los 15 Minutos",
                "tag": "Barrio Vital",
                "desc": "Farmacia, panadería, centro de salud, frutería y parque a menos de 400 metros llanos a pie desde el portal del domicilio."
            },
            {
                "name": "Entorno Verde con Bancos con Respaldo cada 150 m",
                "tag": "Descanso Digno",
                "desc": "Bancos ergonómicos con respaldo y apoyabrazos para levantarse fácilmente, instalados a la sombra de árboles frondosos y junto a fuentes limpias."
            },
            {
                "name": "Ciudad Amigable y Cuidadora Comunitaria (Estándar OMS)",
                "tag": "Comunidad Protegida",
                "desc": "Pasos peatonales sobreelevados, tiempos de semáforo generosos para paso tranquilo, baños públicos limpios y comerciantes con paciencia y trato humano."
            }
        ],
        "kpis": [
            {"val": "250 m", "lbl": "Distancia Servicios"},
            {"val": "150 m", "lbl": "Bancos en Ruta"},
            {"val": "28 seg", "lbl": "Tiempo Semáforo"},
            {"val": "98%", "lbl": "Índice Amabilidad"}
        ],
        "initial_level": 4,
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🏘️ Entorno de Barrio Habitual</span>
                </div>
                <select id="barrio-select" onchange="updateCiudadCalc()">
                    <option value="4">Barrio verde con paseos y plazas arboladas</option>
                    <option value="3">Ensanche urbano comercial con aceras anchas</option>
                    <option value="2">Casco histórico con calles empedradas y cuestas</option>
                    <option value="1">Polígono o periferia con grandes avenidas rápidas</option>
                </select>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🚶 Distancia al Comercio Más Cercano</span>
                    <span class="control-badge" id="dist-badge">250 m</span>
                </div>
                <input type="range" id="dist-range" min="50" max="1000" value="250" step="25" oninput="updateCiudadCalc()">
            </div>

            <div class="control-group">
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-bancos" checked onchange="updateCiudadCalc()">
                    <span class="checkbox-label">🪑 Bancos con respaldo cada 150-200 metros</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-semaforo" checked onchange="updateCiudadCalc()">
                    <span class="checkbox-label">🚦 Semáforos con tiempo tranquilo (> 25 segundos)</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-fuente" checked onchange="updateCiudadCalc()">
                    <span class="checkbox-label">🚰 Fuentes de agua potable en el paseo</span>
                </div>
            </div>

            <div style="background:rgba(56, 189, 248, 0.12); border:1px solid rgba(56, 189, 248, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#bae6fd;">
                🌳 <b>El valor del banco en la calle:</b> Poder sentarse 3 minutos a descansar los gemelos y charlar con un conocido es el mayor antidepresivo natural y la base de la longevidad activa.
            </div>
        """,
        "script": """
        function updateCiudadCalc() {
            const barrio = parseInt(document.getElementById('barrio-select').value);
            const dist = parseInt(document.getElementById('dist-range').value);
            const bancos = document.getElementById('chk-bancos').checked;
            const semaforo = document.getElementById('chk-semaforo').checked;
            const fuente = document.getElementById('chk-fuente').checked;

            document.getElementById('dist-badge').innerText = dist + " m";

            let lvl = 3;
            if (barrio === 1 || (!bancos && !semaforo)) {
                lvl = 1;
            } else if (!bancos && semaforo) {
                lvl = 2;
            } else if (dist <= 300 && bancos && semaforo && fuente) {
                lvl = 5;
            } else if (bancos && dist <= 400) {
                lvl = 4;
            } else {
                lvl = 3;
            }

            document.getElementById('kpi1-val').innerText = dist + " m";
            document.getElementById('kpi2-val').innerText = bancos ? "Cada 150 m" : "Escasos (>500m)";
            document.getElementById('kpi3-val').innerText = semaforo ? "28 seg (Calma)" : "14 seg (Rápido)";
            document.getElementById('kpi4-val').innerText = (lvl >= 4) ? "98% Excelente" : (lvl >= 3 ? "75% Aceptable" : "42% Deficiente");

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un sociólogo urbano y consultor de la Red Mundial de Ciudades Amigables con las Personas Mayores (OMS).
Explícame en 3 viñetas cómo crear una herramienta interactiva en HTML que evalúe si un vecindario es accesible y seguro para salir a pasear, valorando bancos, semáforos y tiendas cercanas.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con simulador de radio de paseo (15 minutos), comprobador de amabilidad del barrio (bancos con respaldo, pasos rebajados, fuentes potables) y decálogo OMS de convivencia comunitaria."""
    },

    # -------------------------------------------------------------------------
    # SESIÓN 53: NIV-053
    # -------------------------------------------------------------------------
    {
        "code": "[NIV-053]",
        "num": 53,
        "filename": "SIMULADOR_MOVILIDAD_TRANSPORTE_SEGURO_SENIORS.html",
        "title": "Los 6 Niveles de Movilidad, Transporte Público y Conducción Segura en la Madurez",
        "subtitle": "Elegir el mejor medio para cada trayecto: caminar con buen calzado, autobús de piso bajo, tren asistido y conducción autorregulada sin estrés",
        "icon": "🚌",
        "steps": [
            {
                "name": "Caminar con Seguridad y Firmeza Diaria",
                "tag": "Paseo Diario",
                "desc": "Calzado con suela de goma con relieve antideslizante, ropa luminosa y bastón de senderismo ergonómico si aporta firmeza y confianza en el paso."
            },
            {
                "name": "Autobús Urbano de Piso Bajo y Asientos Azules",
                "tag": "Transporte Accesible",
                "desc": "Subida mediante rampa arrodillada (kneeling), tarjeta de transporte bonificada y asientos reservados de cortesía cerca del conductor."
            },
            {
                "name": "Metro y Tranvía con Ascensores Operativos",
                "tag": "Red Urbana Rápida",
                "desc": "Desplazamientos rápidos verificando en la pantalla o app municipal que la estación de destino cuenta con ascensor en funcionamiento."
            },
            {
                "name": "Tren de Media/Larga Distancia con Servicio Atendo",
                "tag": "Asistencia Gratuita",
                "desc": "Uso del servicio oficial gratuito de acompañamiento de Renfe: ayuda con el equipaje y traslado en silla de ruedas hasta la butaca del tren."
            },
            {
                "name": "Conducción Autorregulada y Serena (Luz de Día)",
                "tag": "Sabiduría al Volante",
                "desc": "Evitar conducir de noche para no sufrir deslumbramientos de faros modernos, evitar lluvias torrenciales y preferir horas centrales soleadas."
            },
            {
                "name": "Copiloto Feliz y Alternativa Inteligente del Taxi/VTC",
                "tag": "Libertad sin Cargas",
                "desc": "Prescindir de coche propio ahorra entre 2.500 y 3.500 € al año en seguro, garaje, revisiones e ITV, presupuesto sobrado para viajar en taxi de puerta a puerta."
            }
        ],
        "kpis": [
            {"val": "Autobús", "lbl": "Medio Óptimo"},
            {"val": "10:30 h", "lbl": "Hora Ideal"},
            {"val": "2.850 €/año", "lbl": "Ahorro vs Coche"},
            {"val": "0% Tensión", "lbl": "Tranquilidad"}
        ],
        "initial_level": 2,
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🗺️ Tipo de Trayecto Habitual</span>
                </div>
                <select id="trayecto-select" onchange="updateMovilidadCalc()">
                    <option value="2">Desplazamiento urbano al centro o médico</option>
                    <option value="1">Compras en el barrio a menos de 500 m</option>
                    <option value="4">Viaje interurbano a otra ciudad a ver familiares</option>
                    <option value="5">Ruta por carretera secundaria comarcal</option>
                </select>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">☀️ Momento del Día y Clima</span>
                </div>
                <select id="clima-select" onchange="updateMovilidadCalc()">
                    <option value="1">Mañana soleada y despejada (10:00 - 13:00)</option>
                    <option value="2">Tarde con lluvia suave</option>
                    <option value="3">Noche oscura con tráfico denso y faros</option>
                </select>
            </div>

            <div class="control-group">
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-tarjeta" checked onchange="updateMovilidadCalc()">
                    <span class="checkbox-label">💳 Abono de transporte bonificado senior</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-atendo" checked onchange="updateMovilidadCalc()">
                    <span class="checkbox-label">🛎️ Servicio Atendo solicitado para tren</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-taxi" onchange="updateMovilidadCalc()">
                    <span class="checkbox-label">🚕 Uso de taxi/transporte para días de lluvia o salud</span>
                </div>
            </div>

            <div style="background:rgba(16, 185, 129, 0.12); border:1px solid rgba(16, 185, 129, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#a7f3d0;">
                🚗 <b>Dejar el coche no es perder libertad:</b> Cuando mantener el coche causa ansiedad por los aparcamientos o la ITV, dar el paso al autobús y taxi es ganar paz mental y ahorrar miles de euros.
            </div>
        """,
        "script": """
        function updateMovilidadCalc() {
            const tray = parseInt(document.getElementById('trayecto-select').value);
            const clima = parseInt(document.getElementById('clima-select').value);
            const taxi = document.getElementById('chk-taxi').checked;

            let lvl = 2;
            if (tray === 1) lvl = 1;
            else if (tray === 2 && !taxi) lvl = 2;
            else if (tray === 4) lvl = 4;
            else if (tray === 5 && clima === 1) lvl = 5;
            else if (taxi || clima === 3) lvl = 6;

            document.getElementById('kpi1-val').innerText = lvl === 1 ? "A pie" : (lvl === 2 ? "Autobús" : (lvl === 4 ? "Tren Atendo" : (lvl === 5 ? "Coche Día" : "Taxi / Puerta")));
            document.getElementById('kpi2-val').innerText = clima === 1 ? "10:30 h (Soleado)" : (clima === 2 ? "Tarde Templada" : "Evitar Noche");
            document.getElementById('kpi3-val').innerText = lvl === 6 ? "3.100 €/año" : "2.850 €/año";
            document.getElementById('kpi4-val').innerText = (clima === 3 && lvl === 5) ? "Alta Alerta" : "0% Tensión";

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un formador vial y especialista en movilidad sostenible para personas mayores (+65).
Explícame en 3 viñetas cómo crear una aplicación interactiva en HTML que ayude a elegir el medio de transporte más cómodo y seguro para cada situación, fomentando el transporte público y la conducción autorregulada de día.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con selector de trayecto y clima, comparativa económica de mantener coche propio vs usar transporte bonificado y taxis, y guía del Servicio Atendo de ayuda en estaciones de tren."""
    },

    # -------------------------------------------------------------------------
    # SESIÓN 54: NIV-054
    # -------------------------------------------------------------------------
    {
        "code": "[NIV-054]",
        "num": 54,
        "filename": "SIMULADOR_AGUA_POTABLE_HIDRATACION_SENIORS.html",
        "title": "Los 5 Niveles del Agua en el Hogar: Calidad del Grifo, Ahorro e Hidratación Saludable",
        "subtitle": "La ciencia del agua potable: estrictos controles sanitarios municipales, prevención de quemaduras y el hábito de los 6 a 8 vasos diarios",
        "icon": "💧",
        "steps": [
            {
                "name": "Alerta de Deshidratación Silenciosa (Pérdida del Reflejo de Sed)",
                "tag": "Riesgo Oculto",
                "desc": "Con los años el centro hipotalámico de la sed pierde sensibilidad; esperar a tener sed provoca mareos leves, confusión y sobrecarga en los riñones."
            },
            {
                "name": "Garantía Sanitaria del Agua del Grifo Municipal",
                "tag": "Seguridad Total",
                "desc": "El agua del grifo en España pasa más de 40 controles analíticos diarios; es 100% pura, ecológica y miles de veces más barata que el agua embotellada."
            },
            {
                "name": "Rutina Hidratante de los 6 a 8 Vasos Repartidos",
                "tag": "Hábito Vital",
                "desc": "Un vaso templado al despertar, infusiones suaves a media mañana, caldos caseros y una jarra de cristal visible en la mesa para beber sin esfuerzo."
            },
            {
                "name": "Grifería Termostática y Prevención de Quemaduras",
                "tag": "Confort Seguro",
                "desc": "Grifos con tope de seguridad a 38°C que impiden que el agua salga ardiendo por un tirón brusco, protegiendo la piel fina de quemaduras en ducha."
            },
            {
                "name": "Ahorro Inteligente con Aireadores Perlizadores en Grifos",
                "tag": "Hogar Sostenible",
                "desc": "Filtros atomizadores de 2 euros enroscados en la boca del grifo: mezclan aire con agua, dando sensación de chorro potente pero ahorrando el 50% de agua."
            }
        ],
        "kpis": [
            {"val": "7 vasos", "lbl": "Consumo Diario"},
            {"val": "100%", "lbl": "Control Sanitario"},
            {"val": "5 €/año", "lbl": "Coste Agua Grifo"},
            {"val": "38°C", "lbl": "Tope Térmico"}
        ],
        "initial_level": 3,
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🥤 Vasos de Líquidos al Día</span>
                    <span class="control-badge" id="vasos-badge">7 vasos</span>
                </div>
                <input type="range" id="vasos-range" min="2" max="10" value="7" step="1" oninput="updateAguaCalc()">
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🚰 Procedencia Habitual del Agua</span>
                </div>
                <select id="origen-select" onchange="updateAguaCalc()">
                    <option value="grifo">Agua del grifo de red municipal</option>
                    <option value="botella">Garrafas / botellas de agua mineral plástica</option>
                </select>
            </div>

            <div class="control-group">
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-termostato" checked onchange="updateAguaCalc()">
                    <span class="checkbox-label">🌡️ Grifo con tope de seguridad a 38°C</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-aireador" checked onchange="updateAguaCalc()">
                    <span class="checkbox-label">💨 Boquillas perlizadoras ahorradoras instaladas</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-jarra" checked onchange="updateAguaCalc()">
                    <span class="checkbox-label">🥛 Jarra de cristal siempre a la vista en la mesa</span>
                </div>
            </div>

            <div style="background:rgba(56, 189, 248, 0.12); border:1px solid rgba(56, 189, 248, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#bae6fd;">
                💧 <b>Desmitificación de las garrafas pesadas:</b> Cargar garrafas de 5 litros desde el súper lesiona la columna. El agua de red en España es excelente; si tiene sabor a cloro, basta dejarla reposar 20 minutos en jarra abierta.
            </div>
        """,
        "script": """
        function updateAguaCalc() {
            const vasos = parseInt(document.getElementById('vasos-range').value);
            const origen = document.getElementById('origen-select').value;
            const termo = document.getElementById('chk-termostato').checked;
            const aireador = document.getElementById('chk-aireador').checked;

            document.getElementById('vasos-badge').innerText = vasos + " vasos (" + (vasos * 0.25).toFixed(2) + " L)";

            let lvl = 3;
            if (vasos < 4) lvl = 1;
            else if (origen === 'grifo' && vasos >= 6 && !termo) lvl = 2;
            else if (termo && !aireador) lvl = 4;
            else if (termo && aireador && vasos >= 6) lvl = 5;
            else lvl = 3;

            document.getElementById('kpi1-val').innerText = vasos + " vasos (" + (vasos * 0.25).toFixed(1) + " L)";
            document.getElementById('kpi2-val').innerText = origen === 'grifo' ? "100% Control Red" : "Embotellada";
            document.getElementById('kpi3-val').innerText = origen === 'grifo' ? "5 €/año" : "320 €/año";
            document.getElementById('kpi4-val').innerText = termo ? "38°C Segura" : "Sin Tope (Alerta)";

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un médico geriatra e ingeniero sanitario para personas mayores (+65).
Explícame en 3 viñetas cómo crear una calculadora interactiva en HTML que promueva la hidratación regular sin esperar a tener sed, defienda la seguridad del agua del grifo y prevenga quemaduras con grifería termostática.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con planificador de ingesta de líquidos diaria (vasos e infusiones), calculadora de ahorro económico de agua de grifo vs garrafas plásticas y recomendaciones de seguridad antiquemaduras."""
    },

    # -------------------------------------------------------------------------
    # SESIÓN 55: NIV-055
    # -------------------------------------------------------------------------
    {
        "code": "[NIV-055]",
        "num": 55,
        "filename": "SIMULADOR_MEDICINA_PREVENTIVA_SALUD_SENIORS.html",
        "title": "Los 6 Niveles de la Medicina Preventiva: Revisiones, Vacunación y Relación con el Médico de Cabecera",
        "subtitle": "Anticiparse a la enfermedad: chequeos periódicos de tensión y vista, calendario vacunal del adulto mayor y cómo preparar la consulta médica",
        "icon": "🩺",
        "steps": [
            {
                "name": "Autocuidado Diario y Dieta Serena",
                "tag": "Estilo de Vida",
                "desc": "Caminata diaria de 30-40 minutos, alimentación mediterránea de puchero con verduras y legumbres, y descanso nocturno regular."
            },
            {
                "name": "Consulta con el Médico de Familia (Libreta de Dudas)",
                "tag": "Alianza Médica",
                "desc": "Llevar apuntadas en una libreta las 2 dudas principales para no olvidarlas con los nervios, y revisar la lista de medicación habitual."
            },
            {
                "name": "Calendario Vacunal Oficial del Adulto Mayor",
                "tag": "Inmunización Vital",
                "desc": "Vacuna anual contra la gripe, neumococo (pulmonía), recuerdo de herpes zóster y dosis estacionales recomendadas por la sanidad pública."
            },
            {
                "name": "Chequeos Periódicos Programados (Tensión y Vista)",
                "tag": "Revisión Rutinaria",
                "desc": "Control mensual de tensión arterial, analítica anual de sangre (glucosa y colesterol) y revisión periódica de la vista y oído cada 1-2 años."
            },
            {
                "name": "Detección Precoz y Programas de Cribado",
                "tag": "Cribado Preventivo",
                "desc": "Participación activa en el test de sangre oculta en heces para cáncer de colon a partir de los 50 años, mamografías y revisiones urológicas."
            },
            {
                "name": "Cirugías Menores y Avances Mínimamente Invasivos",
                "tag": "Medicina Moderna",
                "desc": "Pérdida del miedo al hospital: intervención de cataratas en 15 minutos con gotas sin ingreso o implantes articulares que devuelven el movimiento."
            }
        ],
        "kpis": [
            {"val": "100%", "lbl": "Chequeos al Día"},
            {"val": "Completa", "lbl": "Pauta Vacunal"},
            {"val": "120/75", "lbl": "Tensión Arterial"},
            {"val": "Máxima", "lbl": "Prevención Activa"}
        ],
        "initial_level": 4,
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🎂 Tramo de Edad Senior</span>
                </div>
                <select id="edad-select" onchange="updateMedicinaCalc()">
                    <option value="65">65 a 74 años (Jubilación activa)</option>
                    <option value="75">75 a 84 años (Madurez serena)</option>
                    <option value="85">85+ años (Longevidad avanzada)</option>
                </select>
            </div>

            <div class="control-group">
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-vacunas" checked onchange="updateMedicinaCalc()">
                    <span class="checkbox-label">💉 Vacunación de gripe y neumococo al día</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-tension" checked onchange="updateMedicinaCalc()">
                    <span class="checkbox-label">🩺 Tensión arterial medida en el último mes</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-cribado" checked onchange="updateMedicinaCalc()">
                    <span class="checkbox-label">🔬 Cribado de colon / analítica anual realizada</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-libreta" checked onchange="updateMedicinaCalc()">
                    <span class="checkbox-label">📝 Libreta con preguntas para la consulta médica</span>
                </div>
            </div>

            <div style="background:rgba(16, 185, 129, 0.12); border:1px solid rgba(16, 185, 129, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#a7f3d0;">
                📋 <b>El truco de la libreta en la consulta:</b> Las batas blancas a veces intimidan o aceleran el pulso. Llevar las 2 dudas escritas en un papelito en la mano garantiza que salgas con todas las respuestas claras.
            </div>
        """,
        "script": """
        function updateMedicinaCalc() {
            const vac = document.getElementById('chk-vacunas').checked;
            const tens = document.getElementById('chk-tension').checked;
            const crib = document.getElementById('chk-cribado').checked;
            const lib = document.getElementById('chk-libreta').checked;

            let lvl = 1;
            if (vac && tens && crib && lib) lvl = 5;
            else if (vac && tens && crib) lvl = 4;
            else if (vac && tens) lvl = 3;
            else if (lib) lvl = 2;
            else lvl = 1;

            document.getElementById('kpi1-val').innerText = crib ? "100% al Día" : "Pendiente";
            document.getElementById('kpi2-val').innerText = vac ? "Completa (Gripe+Neumo)" : "Incompleta";
            document.getElementById('kpi3-val').innerText = tens ? "120/75 Óptima" : "Por medir";
            document.getElementById('kpi4-val').innerText = (lvl >= 4) ? "Escudo Máximo" : "Básica";

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un especialista en medicina preventiva y médico de atención primaria para personas mayores (+65).
Explícame en 3 viñetas cómo crear una guía interactiva en HTML que recuerde las revisiones periódicas, el calendario vacunal del adulto mayor y pautas para aprovechar al máximo la consulta con el médico de cabecera.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con lista interactiva de chequeos médicos recomendados por edad, calendario vacunal del adulto mayor, bloc de notas para la consulta médica y desmitificación de cirugías ambulatorias modernas."""
    },

    # -------------------------------------------------------------------------
    # SESIÓN 56: NIV-056
    # -------------------------------------------------------------------------
    {
        "code": "[NIV-056]",
        "num": 56,
        "filename": "SIMULADOR_AGRICULTURA_HUERTA_ALIMENTACION_SENIORS.html",
        "title": "Los 5 Niveles de la Huerta Tradicional, Alimentos de Temporada y Consumo de Proximidad",
        "subtitle": "Comer bien, rico y barato: el calendario de frutas y verduras de temporada, mercados municipales y el placer de cultivar plantas aromáticas",
        "icon": "🍅",
        "steps": [
            {
                "name": "Ultraprocesados Industriales (Sal y Grasas Ocultas)",
                "tag": "Comida Inadecuada",
                "desc": "Alimentos envasados con conservantes artificiales y exceso de sodio que elevan la tensión arterial y dificultan las digestiones lentas."
            },
            {
                "name": "Alimentos Frescos de Cadena Larga e Invernadero Lejano",
                "tag": "Origen Distante",
                "desc": "Hortalizas recogidas verdes que maduran en cámaras frigoríficas tras miles de kilómetros: pierden sabor, textura y encarecen su coste."
            },
            {
                "name": "Alimentos de Temporada en España (Ricos y a Mitad de Precio)",
                "tag": "Temporada Óptima",
                "desc": "Comprar alcachofas y naranjas en invierno, espárragos y fresas en primavera, tomates y melón en verano: máximo sabor, más vitaminas y 40% más baratos."
            },
            {
                "name": "Mercado Municipal y Tienda de Barrio (Trato Humano)",
                "tag": "Comercio de Barrio",
                "desc": "El frutero de confianza te recomienda la pieza en su punto justo de maduración, te corta la porción deseada y mantiene vivo el tejido social del vecindario."
            },
            {
                "name": "Macetohuerto en Balcón y Hierbas Aromáticas",
                "tag": "Placer Saludable",
                "desc": "Cuidar macetas de romero, albahaca, perejil o pequeños tomates cherry: ejercicio físico suave al aire libre, aromas agradables y conexión con la naturaleza."
            }
        ],
        "kpis": [
            {"val": "Primavera", "lbl": "Estación Activa"},
            {"val": "-38%", "lbl": "Ahorro en Cesta"},
            {"val": "100%", "lbl": "Sabor y Nutrientes"},
            {"val": "Excelente", "lbl": "Salud Digestiva"}
        ],
        "initial_level": 3,
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🗓️ Estación del Año para Comprar</span>
                </div>
                <select id="estacion-select" onchange="updateHuertaCalc()">
                    <option value="primavera">Primavera (Fresas, espárragos, guisantes, alcachofas)</option>
                    <option value="verano">Verano (Tomates sabrosos, pimientos, melón, sandía)</option>
                    <option value="otono">Otoño (Uvas, calabaza, setas, granada, manzanas)</option>
                    <option value="invierno">Invierno (Naranjas, mandarinas, espinacas, acelgas)</option>
                </select>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🛒 Lugar de Compra Habitual</span>
                </div>
                <select id="lugar-select" onchange="updateHuertaCalc()">
                    <option value="mercado">Mercado tradicional de abastos / Frutería de barrio</option>
                    <option value="super">Supermercado empaquetado en plástico</option>
                </select>
            </div>

            <div class="control-group">
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-macetas" checked onchange="updateHuertaCalc()">
                    <span class="checkbox-label">🌱 Macetohuerto o hierbas aromáticas en terraza/balcón</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-legumbres" checked onchange="updateHuertaCalc()">
                    <span class="checkbox-label">🍲 Puchero de legumbres tradicional 2-3 veces/semana</span>
                </div>
            </div>

            <div style="background:rgba(16, 185, 129, 0.12); border:1px solid rgba(16, 185, 129, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#a7f3d0;">
                🍅 <b>El sabor de verdad de la huerta:</b> Un tomate de temporada en julio sabe a gloria y huele a huerto de pueblo. Comprarlo fuera de estación sale caro y solo sabe a agua. ¡Aprovecha la temporada!
            </div>
        """,
        "script": """
        function updateHuertaCalc() {
            const est = document.getElementById('estacion-select').value;
            const lug = document.getElementById('lugar-select').value;
            const mac = document.getElementById('chk-macetas').checked;

            let lvl = 3;
            if (lug === 'super' && !mac) lvl = 2;
            else if (lug === 'mercado' && !mac) lvl = 4;
            else if (lug === 'mercado' && mac) lvl = 5;
            else lvl = 3;

            const estN = est.charAt(0).toUpperCase() + est.slice(1);
            document.getElementById('kpi1-val').innerText = estN;
            document.getElementById('kpi2-val').innerText = lug === 'mercado' ? "-38% Ahorro" : "-10%";
            document.getElementById('kpi3-val').innerText = lug === 'mercado' ? "100% Natural" : "Estándar";
            document.getElementById('kpi4-val').innerText = mac ? "Óptima (+Huerto)" : "Buena";

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un agrónomo divulgador y experto en nutrición mediterránea para personas mayores (+65).
Explícame en 3 viñetas cómo diseñar una herramienta interactiva en HTML que muestre el calendario de frutas y verduras de temporada en España, defendiendo el mercado municipal y el cultivo en macetas de balcón.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con rueda estacional de alimentos de temporada (primavera a invierno), comparativa de sabor y ahorro en la cesta de la compra, y guía para iniciar un macetohuerto de hierbas aromáticas en el balcón."""
    },

    # -------------------------------------------------------------------------
    # SESIÓN 57: NIV-057
    # -------------------------------------------------------------------------
    {
        "code": "[NIV-057]",
        "num": 57,
        "filename": "SIMULADOR_MATERIALES_REFORMAS_HOGAR_SENIORS.html",
        "title": "Los 6 Niveles del Mantenimiento Seguro del Hogar: Materiales, Reformas y Confort Térmico",
        "subtitle": "Materiales duraderos y no resbaladizos, ventanas con aislamiento climalit, pintura ecológica sin humos y subvenciones de rehabilitación",
        "icon": "🔨",
        "steps": [
            {
                "name": "Pavimentos Deslizantes de Alto Riesgo",
                "tag": "Peligro en el Suelo",
                "desc": "Suelos pulidos de mármol o terrazo brillante que con una sola gota de agua se convierten en pista de patinaje; alfombrillas sueltas en pasillos."
            },
            {
                "name": "Suelos Antideslizantes Certificados Clase 2 o 3",
                "tag": "Agarre Firme",
                "desc": "Baldosas cerámicas mate con textura ligeramente rugosa en baño y cocina para pisar descalzo o con zapatillas húmedas con total adherencia."
            },
            {
                "name": "Ventanas con Doble Cristal Climalit y Rotura Térmica",
                "tag": "Aislamiento y Calma",
                "desc": "Carpintería estanca que elimina las corrientes de aire frío en invierno, aísla de los ruidos molestos de la calle y ahorra un 35% en calefacción."
            },
            {
                "name": "Pinturas Ecológicas al Agua sin Olores (Cero COVs)",
                "tag": "Aire Saludable",
                "desc": "Pinturas minerales sin disolventes químicos agresivos que permiten pintar la casa sin irritar los bronquios ni los ojos de los habitantes."
            },
            {
                "name": "Iluminación LED Cálida y Enchufes a Media Altura",
                "tag": "Ergonomía Diaria",
                "desc": "Enchufes e interruptores elevados a 70 cm del suelo para no agachar la espalda hasta el rodapié, y luces LED sin deslumbramientos."
            },
            {
                "name": "Rehabilitación Energética y Subvenciones Públicas",
                "tag": "Hogar Blindado",
                "desc": "Aprovechamiento de las subvenciones del Plan de Vivienda y Autonomía Personal para costear hasta el 80% del cambio de bañera y aislamiento."
            }
        ],
        "kpis": [
            {"val": "Clase 3", "lbl": "Antideslizante"},
            {"val": "Climalit", "lbl": "Ventanas"},
            {"val": "75 cm", "lbl": "Altura Enchufes"},
            {"val": "Hasta 80%", "lbl": "Ayuda Pública"}
        ],
        "initial_level": 3,
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🛠️ Reforma Prioritaria en Casa</span>
                </div>
                <select id="reforma-select" onchange="updateReformasCalc()">
                    <option value="3">Cambio de ventanas por doble cristal aislante</option>
                    <option value="2">Cambio de suelo de baño por antideslizante clase 3</option>
                    <option value="5">Subida de enchufes y mejora de iluminación LED</option>
                    <option value="6">Reforma integral accesible subvencionada</option>
                </select>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🪟 Estado Actual de las Ventanas</span>
                </div>
                <select id="ventanas-select" onchange="updateReformasCalc()">
                    <option value="climalit">Doble cristal moderno (Cierra hermético)</option>
                    <option value="antiguas">Aluminio fino o madera antigua con corrientes de aire</option>
                </select>
            </div>

            <div class="control-group">
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-suelobaño" checked onchange="updateReformasCalc()">
                    <span class="checkbox-label">🚿 Pavimento mate antideslizante en baño</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-enchufes" checked onchange="updateReformasCalc()">
                    <span class="checkbox-label">🔌 Enchufes a media altura (no en el rodapié)</span>
                </div>
            </div>

            <div style="background:rgba(56, 189, 248, 0.12); border:1px solid rgba(56, 189, 248, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#bae6fd;">
                🔨 <b>Las ayudas públicas para cambiar la bañera:</b> La mayoría de comunidades y ayuntamientos tienen subvenciones específicas para mayores de 65 años que cubren gran parte del coste de poner ducha plana. Pregunta en servicios sociales de tu barrio.
            </div>
        """,
        "script": """
        function updateReformasCalc() {
            const ref = parseInt(document.getElementById('reforma-select').value);
            const vent = document.getElementById('ventanas-select').value;
            const baño = document.getElementById('chk-suelobaño').checked;
            const ench = document.getElementById('chk-enchufes').checked;

            let lvl = ref;
            if (!baño) lvl = 1;
            else if (vent === 'antiguas' && ref === 3) lvl = 2;
            else if (ench && baño && vent === 'climalit') lvl = Math.max(ref, 5);

            document.getElementById('kpi1-val').innerText = baño ? "Clase 3 (Rugoso)" : "Clase 1 (Resbala)";
            document.getElementById('kpi2-val').innerText = vent === 'climalit' ? "Climalit 4-16-4" : "Vidrio Simple";
            document.getElementById('kpi3-val').innerText = ench ? "75 cm (Cómodo)" : "20 cm (Agacharse)";
            document.getElementById('kpi4-val').innerText = lvl >= 5 ? "Hasta 80% Ayuda" : "Subvencionable";

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un arquitecto de interiores y perito en reformas seguras para personas mayores (+65).
Explícame en 3 viñetas cómo crear una calculadora interactiva en HTML que oriente sobre materiales antideslizantes, aislamiento térmico con doble acristalamiento y colocación ergonómica de enchufes para el confort diario.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con simulador de reformas prioritarias en el hogar, test de aislamiento de ventanas y pavimento antideslizante, y guía de subvenciones públicas para accesibilidad y eficiencia."""
    },

    # -------------------------------------------------------------------------
    # SESIÓN 58: NIV-058
    # -------------------------------------------------------------------------
    {
        "code": "[NIV-058]",
        "num": 58,
        "filename": "SIMULADOR_ASTRONOMIA_EXPLORACION_COSMOS_SENIORS.html",
        "title": "Los 5 Niveles de Astronomía Cotidiana, Fases Lunares y Maravilla del Cosmos para Seniors",
        "subtitle": "La emoción de mirar el cielo nocturno: fases de la Luna, reconocer constelaciones a simple vista, prismáticos ligeros y serenidad cósmica",
        "icon": "🔭",
        "steps": [
            {
                "name": "Mirar al Cielo a Simple Vista desde el Balcón",
                "tag": "Asombro Inicial",
                "desc": "Reconocer la Estrella Polar para encontrar el Norte, el brillo inconfundible de Venus al atardecer y las tres estrellas del cinturón de Orión."
            },
            {
                "name": "El Baile de las Fases Lunares (Regla Mnemotécnica)",
                "tag": "Ciclo Lunar",
                "desc": "Comprender la regla de 'la luna es mentirosa': cuando tiene forma de C está Menguando (no Creciendo), y cuando tiene forma de D está Creciendo."
            },
            {
                "name": "Prismáticos Ligeros 7x50 o 10x50 con Apoyo Cómodo",
                "tag": "Visión Detallada",
                "desc": "Sin necesidad de telescopios pesados: con unos prismáticos sencillos apoyados en la barandilla se ven los mares lunares y los 4 satélites de Júpiter."
            },
            {
                "name": "Noches de Estrellas Fugaces en el Pueblo (Lágrimas de San Lorenzo)",
                "tag": "Vivencia Compartida",
                "desc": "Disfrutar en agosto de las Perseidas en una tumbona con manta y termo de té, compartiendo anécdotas de juventud bajo un cielo sin contaminación lumínica."
            },
            {
                "name": "Serenidad y Perspectiva Cósmica en la Madurez",
                "tag": "Sabiduría Vital",
                "desc": "Comprender la inmensidad del universo aporta paz mental, relativiza las pequeñas prisas cotidianas y demuestra que la curiosidad nunca envejece."
            }
        ],
        "kpis": [
            {"val": "Cuarto Creciente (D)", "lbl": "Fase Lunar"},
            {"val": "Prismáticos 7x50", "lbl": "Equipo Sugerido"},
            {"val": "Cielo Despejado", "lbl": "Visibilidad"},
            {"val": "100% Calma", "lbl": "Paz Mental"}
        ],
        "initial_level": 2,
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🌙 Fase Lunar a Observar</span>
                </div>
                <select id="fase-select" onchange="updateAstronomiaCalc()">
                    <option value="creciente">Cuarto Creciente (Forma de D - Maravillosa relieve)</option>
                    <option value="llena">Luna Llena (Círculo brillante deslumbrante)</option>
                    <option value="menguante">Cuarto Menguante (Forma de C - Madrugadas serenas)</option>
                    <option value="nueva">Luna Nueva (Cielo oscuro ideal para ver constelaciones)</option>
                </select>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🌌 Lugar de Observación</span>
                </div>
                <select id="lugar-astro" onchange="updateAstronomiaCalc()">
                    <option value="pueblo">Terraza o campo de pueblo (Cielo oscuro limpio)</option>
                    <option value="ciudad">Balcón de ciudad (Contaminación lumínica moderada)</option>
                </select>
            </div>

            <div class="control-group">
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-prismaticos" checked onchange="updateAstronomiaCalc()">
                    <span class="checkbox-label">🔭 Prismáticos ligeros de mano disponibles</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-tumbona" checked onchange="updateAstronomiaCalc()">
                    <span class="checkbox-label">🪑 Asiento o tumbona cómoda con respaldo</span>
                </div>
            </div>

            <div style="background:rgba(56, 189, 248, 0.12); border:1px solid rgba(56, 189, 248, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#bae6fd;">
                ✨ <b>El telescopio no es obligatorio:</b> Los telescopios grandes son pesados y difíciles de enfocar. Unos prismáticos clásicos apoyados en una almohada o barandilla son la forma más relajada y bonita de descubrir el relieve lunar.
            </div>
        """,
        "script": """
        function updateAstronomiaCalc() {
            const fase = document.getElementById('fase-select').value;
            const lugar = document.getElementById('lugar-astro').value;
            const prism = document.getElementById('chk-prismaticos').checked;

            let lvl = 2;
            if (!prism && lugar === 'ciudad') lvl = 1;
            else if (fase === 'creciente' || fase === 'menguante') lvl = 2;
            else if (prism && lugar === 'ciudad') lvl = 3;
            else if (prism && lugar === 'pueblo') lvl = 4;
            else if (lugar === 'pueblo') lvl = 5;

            const faseTxt = fase === 'creciente' ? "Cuarto Creciente (D)" : (fase === 'llena' ? "Luna Llena" : (fase === 'menguante' ? "Cuarto Menguante (C)" : "Luna Nueva"));
            document.getElementById('kpi1-val').innerText = faseTxt;
            document.getElementById('kpi2-val').innerText = prism ? "Prismáticos 7x50" : "A Simple Vista";
            document.getElementById('kpi3-val').innerText = lugar === 'pueblo' ? "Cielo de Pueblo 100%" : "Balcón Ciudad 65%";
            document.getElementById('kpi4-val').innerText = "100% Calma Cósmica";

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un astrónomo divulgador y docente para personas mayores (+65).
Explícame en 3 viñetas cómo crear una guía interactiva en HTML para observar la Luna y las estrellas a simple vista o con prismáticos ligeros, explicando las fases lunares con trucos mnemotécnicos sencillos.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con simulador de fases lunares (regla de la C y la D), guía de estrellas y planetas visibles a simple vista desde el balcón y pautas ergonómicas para disfrutar del cielo nocturno sin sobrecargar el cuello."""
    },

    # -------------------------------------------------------------------------
    # SESIÓN 59: NIV-059
    # -------------------------------------------------------------------------
    {
        "code": "[NIV-059]",
        "num": 59,
        "filename": "SIMULADOR_CONSERVACION_ALIMENTOS_DESPENSA_SENIORS.html",
        "title": "Los 6 Niveles de la Despensa Saludable: Conservación de Alimentos, Fechas de Caducidad y Congelación Segura",
        "subtitle": "Seguridad alimentaria en casa: distinguir 'caducidad' de 'consumo preferente', orden del frigorífico, descongelación correcta y cocina de aprovechamiento",
        "icon": "🥫",
        "steps": [
            {
                "name": "Fecha de Caducidad vs Consumo Preferente",
                "tag": "Regla de Oro",
                "desc": "'Caducidad' es por seguridad estricta en carnes, pescados y lácteos frescos; 'Consumo preferente' indica que legumbres o pastas pierden algo de aroma pero son 100% seguras."
            },
            {
                "name": "El Tesoro de las Conservas Tradicionales en Vidrio",
                "tag": "Fondo de Despensa",
                "desc": "Botes de garbanzos, lentejas, sardinillas y tomate frito casero: una reserva alimentaria saludable que dura años sin frío y resuelve comidas en 5 minutos."
            },
            {
                "name": "Organización Térmica del Frigorífico por Zonas",
                "tag": "Frío Correcto",
                "desc": "Carnes y pescados frescos abajo sobre la bandeja fría (2°C), guisos y lácteos al centro (4-5°C), verduras en el cajón (7°C) y mantequilla/huevos en la puerta."
            },
            {
                "name": "Congelación en Porciones y Descongelación en Nevera",
                "tag": "Congelación Sana",
                "desc": "Congelar en raciones individuales con fecha; descongelar siempre dentro de la nevera 24 horas antes: jamás sobre la encimera al aire para evitar bacterias."
            },
            {
                "name": "Fiambreras de Cristal Herméticas con Cinta y Fecha",
                "tag": "Orden y Claridad",
                "desc": "Guardar las sobras en recipientes de vidrio que no cogen olores; poner un trozo de cinta con el día que se cocinó para consumir en 48-72 horas."
            },
            {
                "name": "Cocina de Aprovechamiento y Desperdicio Cero (+65)",
                "tag": "Sabiduría Culinaria",
                "desc": "El caldo del cocido se convierte en sopa reconfortante, las sobras en croquetas caseras y las verduras maduras en puré: respeto por la comida y ahorro familiar."
            }
        ],
        "kpis": [
            {"val": "Bote Legumbres", "lbl": "Alimento Tipo"},
            {"val": "Consumo Pref.", "lbl": "Tipo de Fecha"},
            {"val": "Despensa Seca", "lbl": "Ubicación Ideal"},
            {"val": "0 € Pérdida", "lbl": "Desperdicio Evitado"}
        ],
        "initial_level": 3,
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">🥫 Alimento a Consultar</span>
                </div>
                <select id="alimento-select" onchange="updateDespensaCalc()">
                    <option value="conserva">Bote de garbanzos o lentejas cocidas en cristal</option>
                    <option value="pescado">Pescado blanco fresco de la pescadería</option>
                    <option value="yogur">Yogur natural envasado</option>
                    <option value="guiso">Guiso casero cocinado ayer</option>
                    <option value="arroz">Paquete de arroz o pasta seca</option>
                </select>
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">❄️ Método de Descongelación Habitual</span>
                </div>
                <select id="descong-select" onchange="updateDespensaCalc()">
                    <option value="nevera">Dentro de la nevera despacio (24 horas antes)</option>
                    <option value="encimera">En la encimera a temperatura ambiente (Riesgo)</option>
                </select>
            </div>

            <div class="control-group">
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-etiqueta" checked onchange="updateDespensaCalc()">
                    <span class="checkbox-label">🏷️ Etiqueto los tuppers de cristal con fecha</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-nevera4" checked onchange="updateDespensaCalc()">
                    <span class="checkbox-label">🌡️ Nevera ajustada a 4°C y congelador a -18°C</span>
                </div>
            </div>

            <div style="background:rgba(16, 185, 129, 0.12); border:1px solid rgba(16, 185, 129, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#a7f3d0;">
                🥫 <b>No tires comida en buen estado:</b> Los botes de legumbres o conservas con fecha de consumo preferente vencida de hace unos meses son totalmente comestibles si la tapa metálica no está abombada ni hace ruido al apretar.
            </div>
        """,
        "script": """
        function updateDespensaCalc() {
            const alim = document.getElementById('alimento-select').value;
            const descong = document.getElementById('descong-select').value;
            const etiq = document.getElementById('chk-etiqueta').checked;

            let lvl = 3;
            if (alim === 'conserva' || alim === 'arroz') lvl = 1;
            else if (alim === 'pescado') lvl = 3;
            else if (descong === 'nevera' && alim === 'guiso') lvl = 4;
            else if (etiq && alim === 'guiso') lvl = 5;
            else lvl = 2;

            if (descong === 'encimera') lvl = 1;

            const alimTxt = alim === 'conserva' ? "Bote Legumbres" : (alim === 'pescado' ? "Pescado Fresco" : (alim === 'yogur' ? "Yogur" : "Guiso Casero"));
            const fechaTxt = (alim === 'conserva' || alim === 'arroz') ? "Consumo Preferente" : "Caducidad Estricta";
            document.getElementById('kpi1-val').innerText = alimTxt;
            document.getElementById('kpi2-val').innerText = fechaTxt;
            document.getElementById('kpi3-val').innerText = alim === 'pescado' ? "Bandeja Inferior (2°C)" : (alim === 'conserva' ? "Despensa Seca" : "Balda Media (4°C)");
            document.getElementById('kpi4-val').innerText = descong === 'encimera' ? "Alerta Sanitaria" : "0 € Desperdicio";

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un especialista en seguridad alimentaria y divulgador culinario para personas mayores (+65).
Explícame en 3 viñetas cómo crear una guía interactiva en HTML que aclare la diferencia entre fecha de caducidad y consumo preferente, enseñe a colocar los alimentos en la nevera y descongelar con seguridad.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con clasificador interactivo de alimentos según su método de conservación (despensa, frío, congelador), semáforo de caducidad vs consumo preferente y protocolo higiénico de descongelación en nevera."""
    },

    # -------------------------------------------------------------------------
    # SESIÓN 60: NIV-060
    # -------------------------------------------------------------------------
    {
        "code": "[NIV-060]",
        "num": 60,
        "filename": "SIMULADOR_HISTORIA_LIBRO_LEGADO_SABIDURIA_SENIORS.html",
        "title": "Los 5 Niveles de la Lectura Activa, Memoria y el Legado Escrito de la Historia Personal",
        "subtitle": "El poder de las letras: libros de letra grande, bibliotecas de barrio, tinta electrónica sin cansancio y escribir las memorias familiares para los nietos",
        "icon": "📖",
        "steps": [
            {
                "name": "La Lectura Diaria como Gimnasio Cerebral Activo",
                "tag": "Neuroprotección",
                "desc": "Leer 25-30 minutos al día mantiene despierto el vocabulario, fortalece las conexiones neuronales y reduce el estrés cotidiano en un 68%."
            },
            {
                "name": "El Placer del Papel y la Biblioteca de Barrio (Club de Lectura)",
                "tag": "Vida Social",
                "desc": "Libros impresos en tipografía de letra grande (Large Print), el paseo saludable para devolver el ejemplar y la tertulia con vecinos en el club de lectura."
            },
            {
                "name": "El Libro Electrónico (E-reader con Letra Ajustable)",
                "tag": "Confort Ocular",
                "desc": "Pantalla de tinta electrónica mate que no cansa la vista, permite agrandar la letra al tamaño deseado y no pesa en las manos con artrosis (170 gramos)."
            },
            {
                "name": "Audiolibros y Relatos Narrados con Voz Cálida",
                "tag": "Escucha Placentera",
                "desc": "Disfrutar de novelas, poesía y biografías históricas narradas por actores de doblaje mientras se pasea por el parque o se descansa en el sillón favorito."
            },
            {
                "name": "Escribir el Legado de tu Propia Vida para los Nietos",
                "tag": "Sabiduría Imborrable",
                "desc": "Plasmar en un cuaderno las vivencias de la juventud en el pueblo, las recetas de cocina familiares y los valores aprendidos: el mayor tesoro para la familia."
            }
        ],
        "kpis": [
            {"val": "30 min/día", "lbl": "Tiempo Lectura"},
            {"val": "E-Reader / Papel", "lbl": "Formato Ideal"},
            {"val": "98% Alta", "lbl": "Reserva Cognitiva"},
            {"val": "Iniciado", "lbl": "Cuaderno Memorias"}
        ],
        "initial_level": 3,
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">⏳ Minutos de Lectura al Día</span>
                    <span class="control-badge" id="lectura-badge">30 min</span>
                </div>
                <input type="range" id="lectura-range" min="0" max="90" value="30" step="5" oninput="updateLibroCalc()">
            </div>

            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">📚 Formato de Lectura Favorito</span>
                </div>
                <select id="formato-select" onchange="updateLibroCalc()">
                    <option value="ereader">Lector de tinta electrónica (Letra grande ajustable)</option>
                    <option value="papel">Libro en papel tradicional de biblioteca</option>
                    <option value="audio">Audiolibro narrado para escuchar paseando</option>
                    <option value="prensa">Periódico o revistas de divulgación en papel</option>
                </select>
            </div>

            <div class="control-group">
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-biblioteca" checked onchange="updateLibroCalc()">
                    <span class="checkbox-label">🏛️ Carné de la biblioteca pública del barrio activo</span>
                </div>
                <div class="checkbox-row">
                    <input type="checkbox" id="chk-memorias" checked onchange="updateLibroCalc()">
                    <span class="checkbox-label">✍️ Anoto anécdotas y recuerdos para mis hijos y nietos</span>
                </div>
            </div>

            <div style="background:rgba(16, 185, 129, 0.12); border:1px solid rgba(16, 185, 129, 0.35); border-radius:12px; padding:12px; font-size:0.85rem; color:#a7f3d0;">
                📖 <b>Tu historia es el mayor regalo:</b> A veces pensamos que nuestra vida no tiene nada extraordinario, pero para tus nietos saber cómo era tu escuela, cómo se vivía sin móvil o las recetas de la abuela es una joya impagable.
            </div>
        """,
        "script": """
        function updateLibroCalc() {
            const min = parseInt(document.getElementById('lectura-range').value);
            const form = document.getElementById('formato-select').value;
            const bib = document.getElementById('chk-biblioteca').checked;
            const mem = document.getElementById('chk-memorias').checked;

            document.getElementById('lectura-badge').innerText = min + " min";

            let lvl = 3;
            if (min === 0) lvl = 1;
            else if (min > 0 && form === 'papel') lvl = 2;
            else if (form === 'ereader') lvl = 3;
            else if (form === 'audio') lvl = 4;
            else if (mem) lvl = 5;

            if (mem && min >= 20) lvl = 5;

            document.getElementById('kpi1-val').innerText = min + " min/día";
            document.getElementById('kpi2-val').innerText = form === 'ereader' ? "Tinta Electrónica" : (form === 'audio' ? "Audiolibro" : "Papel Grande");
            document.getElementById('kpi3-val').innerText = min >= 25 ? "98% Muy Alta" : "70% Media";
            document.getElementById('kpi4-val').innerText = mem ? "Tesoro Familiar" : "Por Empezar";

            setLevel(lvl);
        }

        function onLevelChanged(lvl) {}
        """,
        "prompt_seed": """Actúa como un pedagogo humanista y bibliotecario divulgador para personas mayores (+65).
Explícame en 3 viñetas cómo crear una herramienta interactiva en HTML que motive la lectura diaria, recomiende libros de letra grande o e-readers que no pesan y anime a escribir un cuaderno de memorias familiares.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con planificador de lectura diaria y estimulación de memoria, comparativa ergonómica de formatos (papel, tinta electrónica, audiolibro) y plantilla guiada para escribir los recuerdos familiares."""
    }
]

def main():
    print("=== Generando las 10 Micro-Apps Interactivas Senior (+65) de LOTE 6 (Sesiones 51 a 60) ===")
    
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

    print(f"\n¡Éxito! Las 10 Micro-Apps de Lote 6 han sido generadas y sincronizadas con éxito.")

if __name__ == "__main__":
    main()

