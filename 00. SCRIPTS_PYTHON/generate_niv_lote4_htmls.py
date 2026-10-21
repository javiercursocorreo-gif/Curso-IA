#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_niv_lote4_htmls.py
Genera de forma autónoma las 10 Micro-Aplicaciones Interactivas Senior (+65)
para las Sesiones 31 a 40 (Lote 4) bajo la Triple Salvaguarda Pedagógica.
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
        .step-card.completed {
            opacity: 0.88;
            border-color: rgba(16, 185, 129, 0.4);
        }
        .step-pill {
            width: 44px;
            height: 44px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: var(--font-mono);
            font-size: 1.15rem;
            font-weight: 900;
            background: rgba(255, 255, 255, 0.08);
            color: #ffffff;
            flex-shrink: 0;
        }
        .step-card.active .step-pill {
            background: var(--cyan);
            color: #04060b;
        }
        .step-card.completed .step-pill {
            background: rgba(16, 185, 129, 0.25);
            color: #34d399;
        }
        .step-details {
            flex: 1;
        }
        .step-name {
            font-size: 1.05rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .step-meta {
            font-size: 0.88rem;
            color: #94a3b8;
            line-height: 1.45;
        }
        .step-scale-badge {
            font-family: var(--font-mono);
            font-size: 0.78rem;
            color: var(--cyan);
            background: rgba(56, 189, 248, 0.1);
            padding: 2px 8px;
            border-radius: 6px;
            margin-left: auto;
        }

        .action-plan-box {
            background: rgba(16, 185, 129, 0.08);
            border: 1.5px solid rgba(16, 185, 129, 0.35);
            border-radius: 18px;
            padding: 22px;
            display: flex;
            align-items: flex-start;
            gap: 16px;
        }
        .action-icon {
            font-size: 2rem;
            line-height: 1;
            flex-shrink: 0;
        }
        .action-title {
            font-size: 1.1rem;
            font-weight: 800;
            color: #34d399;
            margin-bottom: 6px;
        }
        .action-text {
            font-size: 0.95rem;
            color: #e2e8f0;
            line-height: 1.6;
        }

        @media (max-width: 1024px) {
            .app-container { grid-template-columns: 1fr; }
            .status-hero { flex-direction: column; gap: 18px; text-align: center; }
            .status-hero-left { max-width: 100%; }
        }
"""

def generate_html_microapp(code, num, title, subtitle, icon, steps, kpis, initial_level, specific_aside_html, script_extra, prompt_seed, prompt_master):
    # Genera un archivo HTML completo y depurado
    steps_html = ""
    for s in steps:
        steps_html += f"""
                <div class="step-card" id="step-{s['num']}" onclick="selectStep({s['num']})">
                    <div class="step-pill">{s['num']}</div>
                    <div class="step-details">
                        <div class="step-name">
                            <span>{s['name']}</span>
                            <span class="step-scale-badge">{s['badge']}</span>
                        </div>
                        <div class="step-meta">{s['meta']}</div>
                    </div>
                </div>"""

    data_json = "{\n"
    for s in steps:
        data_json += f"""            {s['num']}: {{
                title: "{s['hero_title']}",
                badge: "{s['hero_badge']}",
                desc: "{s['hero_desc']}",
                action: "{s['action_text']}",
                kpi1: "{s['kpi1']}",
                kpi2: "{s['kpi2']}",
                kpi3: "{s['kpi3']}",
                kpi4: "{s['kpi4']}"
            }},\n"""
    data_json += "        }"

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesión {num:02d} • Micro-App [{code}]: {title} (+65)</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
{BASE_CSS}
    </style>
</head>
<body>

    <header>
        <div class="brand-box">
            <span class="brand-badge">[{code}]</span>
            <h1>{title} (+65)</h1>
        </div>
        <div class="header-actions">
            <button class="btn-pedagogic" onclick="openPromptModal()">🌱 Triple Salvaguarda (Prompts)</button>
        </div>
    </header>

    <div class="app-container">

        <!-- PANEL DE CONTROL INTERACTIVO -->
        <aside class="calculator-panel">
            <div class="panel-title">
                <span>{icon}</span>
                <span>{subtitle}</span>
            </div>

            <!-- Selector de Nivel -->
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">Nivel Seleccionado:</span>
                    <span class="control-badge" id="lblLevel">Nivel {initial_level}</span>
                </div>
                <input type="range" id="rngLevel" min="1" max="{len(steps)}" value="{initial_level}" step="1" oninput="updateSimulation()">
            </div>

            {specific_aside_html}

            <!-- KPIs -->
            <div class="kpi-grid">
                <div class="kpi-card">
                    <div class="kpi-val" id="valKpi1">{kpis[0]['val']}</div>
                    <div class="kpi-lbl">{kpis[0]['lbl']}</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-val" id="valKpi2" style="color:var(--cyan);">{kpis[1]['val']}</div>
                    <div class="kpi-lbl">{kpis[1]['lbl']}</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-val" id="valKpi3">{kpis[2]['val']}</div>
                    <div class="kpi-lbl">{kpis[2]['lbl']}</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-val" id="valKpi4" style="color:var(--primary);">{kpis[3]['val']}</div>
                    <div class="kpi-lbl">{kpis[3]['lbl']}</div>
                </div>
            </div>
        </aside>

        <!-- DASHBOARD DE LA ESCALA Y NIVELES -->
        <main class="dashboard-panel">

            <!-- HERO STATUS -->
            <div class="status-hero">
                <div class="status-hero-left">
                    <span class="status-badge" id="heroBadge">NIVEL {initial_level}</span>
                    <h2 class="status-title" id="heroTitle">{title}</h2>
                    <p class="status-desc" id="heroDesc">
                        Información y análisis en tiempo real adaptados a personas mayores.
                    </p>
                </div>
                <div class="status-circle-box">
                    <span class="status-circle-num" id="heroNum">{initial_level}</span>
                    <span class="status-circle-sub">Nivel</span>
                </div>
            </div>

            <!-- ESCALONES DE LA ESCALA -->
            <div class="steps-container">
{steps_html}
            </div>

            <!-- PLAN DE ACCIÓN Y RECOMENDACIÓN -->
            <div class="action-plan-box">
                <div class="action-icon">💡</div>
                <div>
                    <div class="action-title" id="actionTitle">Consejo Médico y Pedagógico Práctico</div>
                    <div class="action-text" id="actionDesc">
                        Cuidar estos hábitos en la vida diaria refuerza la autonomía, la paz interior y la salud de nuestros mayores.
                    </div>
                </div>
            </div>

        </main>
    </div>

    <!-- MODAL TRIPLE SALVAGUARDA -->
    <div id="promptModal" style="display:none; position:fixed; top:0; left:0; width:100vw; height:100vh; background:rgba(0,0,0,0.85); backdrop-filter:blur(10px); z-index:100; align-items:center; justify-content:center; padding:20px;" onclick="closePromptModal(event)">
        <div style="background:#0b1120; border:2px solid var(--cyan); border-radius:20px; max-width:850px; width:100%; max-height:90vh; overflow-y:auto; padding:28px; box-shadow:0 0 50px rgba(56,189,248,0.3); display:flex; flex-direction:column; gap:20px;" onclick="event.stopPropagation()">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:14px;">
                <div style="display:flex; align-items:center; gap:10px;">
                    <span style="font-size:1.6rem;">{icon}</span>
                    <strong style="font-size:1.2rem; color:#ffffff;">La Triple Salvaguarda Pedagógica (Sesión {num:02d} • [{code}])</strong>
                </div>
                <button onclick="closePromptModal()" style="background:transparent; border:none; color:#94a3b8; font-size:1.4rem; cursor:pointer;">✕</button>
            </div>

            <!-- PASO 1 -->
            <div style="background:rgba(56,189,248,0.08); border:1px solid rgba(56,189,248,0.3); border-radius:14px; padding:16px;">
                <div style="font-family:var(--font-mono); font-size:0.82rem; font-weight:800; color:var(--cyan); margin-bottom:8px;">PASO 1: EL PROMPT SEMILLA HUMANO</div>
                <p style="font-size:0.9rem; color:#cbd5e1; line-height:1.5; margin-bottom:10px;">En lenguaje natural, el alumno define el propósito pedagógico sin tecnicismos:</p>
                <div style="background:#030712; border:1px solid rgba(255,255,255,0.1); border-radius:10px; padding:14px; font-family:var(--font-mono); font-size:0.86rem; color:#38bdf8; line-height:1.6; user-select:all;">
{prompt_seed.replace(chr(10), '<br>')}
                </div>
            </div>

            <!-- PASO 2 -->
            <div style="background:rgba(16,185,129,0.08); border:1px solid rgba(16,185,129,0.3); border-radius:14px; padding:16px;">
                <div style="font-family:var(--font-mono); font-size:0.82rem; font-weight:800; color:#10b981; margin-bottom:8px;">PASO 2: EL PLANO MAESTRO TÉCNICO</div>
                <p style="font-size:0.9rem; color:#cbd5e1; line-height:1.5; margin-bottom:10px;">Plano de ingeniería de software para Gemini si se necesita máxima exhaustividad:</p>
                <div style="background:#030712; border:1px solid rgba(255,255,255,0.1); border-radius:10px; padding:14px; font-family:var(--font-mono); font-size:0.86rem; color:#34d399; line-height:1.6; user-select:all;">
{prompt_master.replace(chr(10), '<br>')}
                </div>
            </div>

            <!-- PASO 3 -->
            <div style="background:rgba(245,158,11,0.08); border:1px solid rgba(245,158,11,0.3); border-radius:14px; padding:16px;">
                <div style="font-family:var(--font-mono); font-size:0.82rem; font-weight:800; color:#f59e0b; margin-bottom:8px;">PASO 3: LA APP OFICIAL TERMINADA</div>
                <p style="font-size:0.9rem; color:#cbd5e1; line-height:1.5;">Garantía de aula: este archivo oficial terminado y desplegado en Classroom permite al alumno seguir la clase sin frustración ante cortes de red o IA.</p>
            </div>
        </div>
    </div>

    <script>
        function openPromptModal() {{ document.getElementById("promptModal").style.display = "flex"; }}
        function closePromptModal(e) {{ if (!e || e.target.id === "promptModal") document.getElementById("promptModal").style.display = "none"; }}

        function selectStep(lvl) {{
            document.getElementById("rngLevel").value = lvl;
            updateSimulation();
        }}

        const appData = {data_json};

        function updateSimulation() {{
            const lvl = parseInt(document.getElementById("rngLevel").value);
            const data = appData[lvl];

            document.getElementById("lblLevel").innerText = `Nivel ${{lvl}}`;
            document.getElementById("valKpi1").innerText = data.kpi1;
            document.getElementById("valKpi2").innerText = data.kpi2;
            document.getElementById("valKpi3").innerText = data.kpi3;
            document.getElementById("valKpi4").innerText = data.kpi4;

            document.getElementById("heroBadge").innerText = data.badge;
            document.getElementById("heroTitle").innerText = data.title;
            document.getElementById("heroDesc").innerText = data.desc;
            document.getElementById("heroNum").innerText = lvl;
            document.getElementById("actionDesc").innerText = data.action;

            for (let i = 1; i <= {len(steps)}; i++) {{
                const el = document.getElementById("step-" + i);
                if (el) {{
                    el.classList.remove("active", "completed");
                    if (i === lvl) el.classList.add("active");
                    else if (i < lvl) el.classList.add("completed");
                }}
            }}

            if (typeof customUpdateExtra === 'function') {{
                customUpdateExtra(lvl);
            }}
        }}

        {script_extra}

        // Inicializar al cargar
        updateSimulation();
    </script>
</body>
</html>"""
    return html


# ==============================================================================
# DEFINICIÓN DE LOS 10 MICRO-APPS DE LOTE 4
# ==============================================================================

APPS = [
    # --------------------------------------------------------------------------
    # SESIÓN 31: PROFUNDIDAD DEL OCÉANO & RESPIRACIÓN
    # --------------------------------------------------------------------------
    {
        "code": "NIV-031", "num": 31,
        "filename": "SIMULADOR_PROFUNDIDAD_OCEANO_RESPIRACION_SENIORS.html",
        "title": "Los 6 Estratos del Océano, Respiración Pulmonar y Calma Mental",
        "subtitle": "Batimetría Marina & Técnica 4-7-8",
        "icon": "🌊", "initial_level": 3,
        "kpis": [
            {"lbl": "Profundidad", "val": "1.000 m"},
            {"lbl": "Presión", "val": "100 Atm"},
            {"lbl": "Pulsaciones", "val": "68 ppm"},
            {"lbl": "Oxigenación", "val": "99%"}
        ],
        "aside": """
            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; text-align:center;">
                <div style="font-size:0.85rem; color:#94a3b8; font-weight:700; margin-bottom:8px;">GUÍA DE RESPIRACIÓN CONSCIENTE (4-7-8)</div>
                <div id="breathCircle" style="width:100px; height:100px; border-radius:50%; background:radial-gradient(circle, #38bdf8 0%, #0369a1 100%); margin:12px auto; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:1.1rem; color:#fff; box-shadow:0 0 25px rgba(56,189,248,0.5); transition:transform 4s ease-in-out;">Inhalar</div>
                <div id="breathTimerText" style="font-family:var(--font-mono); font-size:0.9rem; color:#38bdf8; font-weight:700;">Inhala en 4s</div>
                <button onclick="toggleBreathExercise()" id="btnBreath" style="margin-top:12px; background:rgba(56,189,248,0.2); border:1.5px solid #38bdf8; color:#fff; padding:8px 18px; border-radius:8px; font-weight:700; cursor:pointer;">▶ Iniciar Ciclo de Respiración</button>
            </div>
        """,
        "script": """
            let breathInterval = null;
            let breathState = 0; // 0: Inhala (4s), 1: Retén (7s), 2: Exhala (8s)
            function toggleBreathExercise() {
                const btn = document.getElementById('btnBreath');
                const circle = document.getElementById('breathCircle');
                const txt = document.getElementById('breathTimerText');
                if (breathInterval) {
                    clearInterval(breathInterval);
                    breathInterval = null;
                    btn.innerText = '▶ Reanudar Ciclo';
                    txt.innerText = 'Pausado';
                    circle.style.transform = 'scale(1)';
                } else {
                    btn.innerText = '⏸ Pausar Ciclo';
                    runBreathStep();
                }
            }
            function runBreathStep() {
                const circle = document.getElementById('breathCircle');
                const txt = document.getElementById('breathTimerText');
                if (breathState === 0) {
                    circle.innerText = 'Inhala';
                    circle.style.transition = 'transform 4s ease-in-out';
                    circle.style.transform = 'scale(1.35)';
                    txt.innerText = 'Inhala suavemente por la nariz (4s)';
                    breathInterval = setTimeout(() => { breathState = 1; runBreathStep(); }, 4000);
                } else if (breathState === 1) {
                    circle.innerText = 'Retén';
                    circle.style.transition = 'none';
                    txt.innerText = 'Mantén el aire con serenidad (7s)';
                    breathInterval = setTimeout(() => { breathState = 2; runBreathStep(); }, 7000);
                } else {
                    circle.innerText = 'Exhala';
                    circle.style.transition = 'transform 8s ease-in-out';
                    circle.style.transform = 'scale(0.85)';
                    txt.innerText = 'Exhala despacio por la boca (8s)';
                    breathInterval = setTimeout(() => { breathState = 0; runBreathStep(); }, 8000);
                }
            }
        """,
        "steps": [
            {
                "num": 1, "name": "Zona Epipelágica (0 a 200 m)", "badge": "Luz Solar • 1 a 20 Atm",
                "meta": "El mar soleado y cálido. Respiración superficial y actividad diurna. Oxigenación plena de la vida.",
                "hero_title": "Zona Epipelágica: El Sol Superficial y la Brisa Vital",
                "hero_badge": "NIVEL 1 DE 6 • SUPERFICIE MARINA FÓTICA",
                "hero_desc": "Bajo la luz del sol abunda el fitoplancton que genera más del 50% del oxígeno del planeta. Representa la actividad diaria alegre y los paseos matinales al aire libre.",
                "action_text": "Pasea junto al agua o en parques soleados: la luz natural de la mañana fija la vitamina D y sincroniza tu reloj biológico.",
                "kpi1": "0-200 m", "kpi2": "1-20 Atm", "kpi3": "76 ppm", "kpi4": "98%"
            },
            {
                "num": 2, "name": "Zona Mesopelágica (200 a 1.000 m)", "badge": "Penumbra • 20 a 100 Atm",
                "meta": "El atardecer perpetuo. Transición hacia la calma serena. Desaceleración consciente del ritmo.",
                "hero_title": "Zona Mesopelágica: El Reino de las Sombras y la Transición Serena",
                "hero_badge": "NIVEL 2 DE 6 • PENUMBRA MARINA",
                "hero_desc": "La luz solar se desvanece suavemente. Los animales marinos se mueven con cadencia pausada y ahorro energético.",
                "action_text": "Al caer la tarde, reduce las luces del salón y evita pantallas brillantes: prepara tu mente para el descanso nocturno.",
                "kpi1": "500 m", "kpi2": "50 Atm", "kpi3": "72 ppm", "kpi4": "98%"
            },
            {
                "num": 3, "name": "Zona Batipelágica (1.000 a 4.000 m)", "badge": "Oscuridad • 100 a 400 Atm",
                "meta": "Tiniebla total y silencio absoluto. Ritmo cardíaco estable y profundo. Respiración diafragmática.",
                "hero_title": "Zona Batipelágica: Silencio Profundo y Desconexión de las Prisas",
                "hero_badge": "NIVEL 3 DE 6 • OSCURIDAD Y SILENCIO",
                "hero_desc": "Sin ruidos de la superficie. En esta quietud los habitantes del abismo utilizan destellos bioluminiscentes para comunicarse en paz.",
                "action_text": "Practica la respiración 4-7-8 al acostarte: reduce las palpitaciones y te sumerge en un sueño reparador en minutos.",
                "kpi1": "1.000 m", "kpi2": "100 Atm", "kpi3": "68 ppm", "kpi4": "99%"
            },
            {
                "num": 4, "name": "Zona Abisopelágica (4.000 a 6.000 m)", "badge": "Abismo Helado • 400 a 600 Atm",
                "meta": "El gran lecho fangoso. Presión colosal y temperatura estable de 2 °C. Resiliencia biológica extrema.",
                "hero_title": "Zona Abisal: Calma Imperturbable ante la Presión Externa",
                "hero_badge": "NIVEL 4 DE 6 • FONDO ABISAL MARINO",
                "hero_desc": "A pesar de la enorme presión del agua, los organismos viven con total serenidad adaptando la fluidez de sus membranas celulares.",
                "action_text": "Cuando sientas presiones o preocupaciones familiares, recuerda que tu calma interior es más fuerte que cualquier problema externo.",
                "kpi1": "4.000 m", "kpi2": "400 Atm", "kpi3": "64 ppm", "kpi4": "99%"
            },
            {
                "num": 5, "name": "Zona Hadal - Fosas Marinas (6.000 a 11.000 m)", "badge": "Fosa de las Marianas • 1.100 Atm",
                "meta": "Las simas más hondas de la Tierra. Máxima profundidad conocida. Fortaleza celular microscópica.",
                "hero_title": "Zona Hadal: La Profundidad Máxima de la Paz Mental",
                "hero_badge": "NIVEL 5 DE 6 • FOSAS OCEÁNICAS HADALES",
                "hero_desc": "Bajo 11 kilómetros de agua, pequeños anfípodos y peces caracol nadan transparentes y flexibles. Su secreto es no oponer resistencia rígida a la presión.",
                "action_text": "La flexibilidad emocional en la madurez evita el sufrimiento: aceptar los cambios con suavidad protege el corazón y el ánimo.",
                "kpi1": "11.000 m", "kpi2": "1.100 Atm", "kpi3": "60 ppm", "kpi4": "100%"
            },
            {
                "num": 6, "name": "Chimeneas Hidrotermales", "badge": "Calor Vital • 350 °C Geoquímica",
                "meta": "Oasis volcánicos que nutren la vida sin luz solar. Fuente de energía pura y regeneración.",
                "hero_title": "Chimeneas Hidrotermales: El Fuego Vital que Nunca se Apaga",
                "hero_badge": "NIVEL 6 DE 6 • REGENERACIÓN GEOQUÍMICA",
                "hero_desc": "Gusanos tubo gigantes y microorganismos prosperan gracias al calor geotérmico interno de la Tierra, demostrando que la vida se reinventa siempre.",
                "action_text": "Mantén viva tu chispa de curiosidad: aprender cosas nuevas cada día renueva las sinapsis y llena de ilusión la jubilación.",
                "kpi1": "3.500 m", "kpi2": "350 Atm", "kpi3": "65 ppm", "kpi4": "99%"
            }
        ],
        "prompt_seed": """Actúa como un médico neumólogo y pedagogo de relajación para personas mayores (+65).
Explícame en 3 viñetas cómo diseñar una guía interactiva en HTML que use las profundidades del mar como metáfora para enseñar la respiración pausada (técnica 4-7-8) y oxigenar el cuerpo.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con selector de los 6 estratos marinos, guía animada de respiración (inhalar 4s, retener 7s, exhalar 8s), contador de ciclos y consejos para calmar palpitaciones y dormir mejor."""
    },

    # --------------------------------------------------------------------------
    # SESIÓN 32: PIRÁMIDE NUTRICIONAL & DIGESTIÓN SENIOR
    # --------------------------------------------------------------------------
    {
        "code": "NIV-032", "num": 32,
        "filename": "SIMULADOR_NUTRICION_DIGESTION_SALUDABLE_SENIORS.html",
        "title": "Los 5 Niveles de la Pirámide Nutricional y Digestión Saludable Senior",
        "subtitle": "Digestibilidad & Proteína Noble (+65)",
        "icon": "🥗", "initial_level": 3,
        "kpis": [
            {"lbl": "Peso Corporal", "val": "70 kg"},
            {"lbl": "Proteína Diaria", "val": "77 g/día"},
            {"lbl": "Fibra Suave", "val": "28 g/día"},
            {"lbl": "Digestibilidad", "val": "ÓPTIMA"}
        ],
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">Tu Peso Corporal:</span>
                    <span class="control-badge" id="lblWeight">70 kg</span>
                </div>
                <input type="range" id="rngWeight" min="50" max="100" value="70" step="1" oninput="calcProtein()">
            </div>
            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:16px;">
                <div style="font-size:0.85rem; color:#94a3b8; font-weight:700; margin-bottom:8px;">PLATO RECOMENDADO PARA HOY</div>
                <div id="recipeBox" style="font-size:0.95rem; color:#fff; line-height:1.5;">
                    🍲 <b>Merluza al vapor con puré de calabacín y AOVE crudo</b>: proteína limpia sin espinas, suave para el estómago y rica en minerales.
                </div>
            </div>
        """,
        "script": """
            function calcProtein() {
                const w = parseInt(document.getElementById('rngWeight').value);
                document.getElementById('lblWeight').innerText = w + ' kg';
                const prot = Math.round(w * 1.1);
                document.getElementById('valKpi1').innerText = w + ' kg';
                document.getElementById('valKpi2').innerText = prot + ' g/día';
            }
        """,
        "steps": [
            {
                "num": 1, "name": "1. Base Hidratante y Caldos Claros", "badge": "Agua, Infusiones y Caldos",
                "meta": "Hidratación constante para riñones y digestión. Caldos de verduras desgrasados que reconfortan el estómago.",
                "hero_title": "Escalón 1: El Agua y los Caldos Suaves como Cimiento Vital",
                "hero_badge": "ESCALÓN 1 DE 5 • BASE DE HIDRATACIÓN",
                "hero_desc": "La digestión en personas mayores requiere suficiente líquido para evitar digestiones pesadas y proteger la mucosa gástrica.",
                "action_text": "Toma un vaso de agua templada o caldo suave antes de comer: ayuda a preparar el estómago y activa el tránsito digestivo.",
                "kpi1": "70 kg", "kpi2": "77 g/día", "kpi3": "1.8 L agua", "kpi4": "FÁCIL"
            },
            {
                "num": 2, "name": "2. Verduras Cocidas y Fruta Madura", "badge": "Fibra Soluble Sin Gases",
                "meta": "Calabacín, zanahoria cocida, manzana asada y compotas. Fibra tierna que combate el estreñimiento sin inflamar.",
                "hero_title": "Escalón 2: Fibra Blanda y Vitaminas de Fácil Masticación",
                "hero_badge": "ESCALÓN 2 DE 5 • VERDURAS Y FRUTAS SUAVES",
                "hero_desc": "Cocer o asar las verduras rompe la celulosa dura y facilita la absorción de nutrientes sin provocar pesadez ni flatulencias.",
                "action_text": "Una manzana asada con canela al horno de postre es un bálsamo natural para el intestino y sacia las ganas de dulce.",
                "kpi1": "70 kg", "kpi2": "77 g/día", "kpi3": "30 g fibra", "kpi4": "MUY FÁCIL"
            },
            {
                "num": 3, "name": "3. Proteínas Nobles de Alta Asimilación", "badge": "Pescado, Huevos y Legumbres Trituradas",
                "meta": "El escudo contra la sarcopenia (pérdida de masa muscular). Pescado blanco, tortilla francesa y lentejas pasadas por pasapurés.",
                "hero_title": "Escalón 3: Proteína Noble para Conservar la Fuerza Muscular",
                "hero_badge": "ESCALÓN 3 DE 5 • PROTEÍNAS NOBLES",
                "hero_desc": "A partir de los 65 años se necesita un 20% más de proteína por kilo para no perder fuerza en brazos y piernas al caminar.",
                "action_text": "Asegura una ración de proteína en comida y cena (un huevo, pescado blanco, pechuga tierna o hummus suave).",
                "kpi1": "70 kg", "kpi2": "77 g/día", "kpi3": "28 g fibra", "kpi4": "EXCELENTE"
            },
            {
                "num": 4, "name": "4. Cereales Integrales y Aceite de Oliva", "badge": "Pan de Masa Madre y AOVE",
                "meta": "Energía limpia de liberación lenta. Arroz, copos de avena cocidos y el oro líquido del aceite de oliva virgen extra en crudo.",
                "hero_title": "Escalón 4: Energía Estable y Grasas Cardiosaludables",
                "hero_badge": "ESCALÓN 4 DE 5 • GRASAS SALUDABLES Y CEREALES",
                "hero_desc": "El aceite de oliva virgen extra protege las arterias y lubrica suavemente el intestino para un tránsito diario regular.",
                "action_text": "Aliña tus purés y ensaladas con un chorrito de aceite de oliva en crudo: aporta antioxidantes y multiplica el sabor.",
                "kpi1": "70 kg", "kpi2": "77 g/día", "kpi3": "25 g fibra", "kpi4": "NOTABLE"
            },
            {
                "num": 5, "name": "5. Moderación Absoluta y Ocasional", "badge": "Fritos, Embutidos y Azúcares",
                "meta": "Carnes muy grasas, embutidos duros y bollería industrial. Digerirlos exige un sobreesfuerzo innecesario al hígado y estómago.",
                "hero_title": "Escalón 5: La Cúspide de la Prudencia Digestiva",
                "hero_badge": "ESCALÓN 5 DE 5 • CONSUMO OCASIONAL",
                "hero_desc": "No se trata de prohibir, sino de disfrutar en celebraciones señaladas sin convertirlo en la costumbre diaria de la casa.",
                "action_text": "Sustituye los fritos pesados por cocciones al horno o al papillote: ganarás ligereza y dormirás de un tirón.",
                "kpi1": "70 kg", "kpi2": "77 g/día", "kpi3": "15 g fibra", "kpi4": "DIGESTIÓN PESADA"
            }
        ],
        "prompt_seed": """Actúa como un médico geriatra y nutricionista clínico para personas mayores (+65).
Explícame en 3 viñetas cómo diseñar un semáforo interactivo en HTML que clasifique los alimentos diarios según lo bien que sientan al estómago y el aporte proteico que necesitan los mayores.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con 5 escalones nutricionales, calculadora de raciones de proteína diaria (pescado, huevos, legumbres suaves), balance de hidratación y fibra, y platos tradicionales recomendados."""
    },

    # --------------------------------------------------------------------------
    # SESIÓN 33: VITALIDAD MUSCULAR & PREVENCIÓN DE SARCOPENIA
    # --------------------------------------------------------------------------
    {
        "code": "NIV-033", "num": 33,
        "filename": "SIMULADOR_VITALIDAD_MUSCULAR_SARCOPENIA_SENIORS.html",
        "title": "Los 6 Niveles de Vitalidad Celular, Mitocondrias y Masa Muscular",
        "subtitle": "Test de la Silla & Fuerza Funcional (+65)",
        "icon": "💪", "initial_level": 4,
        "kpis": [
            {"lbl": "Test de la Silla", "val": "11.2 seg"},
            {"lbl": "Estado Funcional", "val": "AUTÓNOMO"},
            {"lbl": "Fuerza Muscular", "val": "78 / 100"},
            {"lbl": "Mitocondrias", "val": "ACTIVAS"}
        ],
        "aside": """
            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px; text-align:center;">
                <div style="font-size:0.85rem; color:#94a3b8; font-weight:700; margin-bottom:8px;">EL TEST DE LA SILLA (5 REPETICIONES)</div>
                <div id="timerDisplay" style="font-family:var(--font-mono); font-size:2.4rem; font-weight:900; color:#38bdf8; margin:6px 0;">0.0 s</div>
                <p style="font-size:0.85rem; color:#cbd5e1; margin-bottom:12px;">Cruza los brazos sobre el pecho y levántate y siéntate 5 veces tan rápido como puedas con seguridad.</p>
                <div style="display:flex; justify-content:center; gap:8px;">
                    <button id="btnTimerStart" onclick="toggleTimer()" style="background:#10b981; color:#04120a; border:none; padding:8px 18px; border-radius:8px; font-weight:800; cursor:pointer;">▶ Empezar Test</button>
                    <button onclick="resetTimer()" style="background:rgba(255,255,255,0.1); color:#fff; border:none; padding:8px 14px; border-radius:8px; font-weight:700; cursor:pointer;">Reiniciar</button>
                </div>
            </div>
        """,
        "script": """
            let timerRunning = false;
            let timerSeconds = 0.0;
            let timerInterval = null;
            function toggleTimer() {
                const btn = document.getElementById('btnTimerStart');
                if (timerRunning) {
                    clearInterval(timerInterval);
                    timerRunning = false;
                    btn.innerText = '▶ Empezar Test';
                    btn.style.background = '#10b981';
                    evalChairTest(timerSeconds);
                } else {
                    timerSeconds = 0.0;
                    timerRunning = true;
                    btn.innerText = '⏹ Parar Test (5ª vez)';
                    btn.style.background = '#f43f5e';
                    timerInterval = setInterval(() => {
                        timerSeconds += 0.1;
                        document.getElementById('timerDisplay').innerText = timerSeconds.toFixed(1) + ' s';
                    }, 100);
                }
            }
            function resetTimer() {
                clearInterval(timerInterval);
                timerRunning = false;
                timerSeconds = 0.0;
                document.getElementById('timerDisplay').innerText = '0.0 s';
                document.getElementById('btnTimerStart').innerText = '▶ Empezar Test';
                document.getElementById('btnTimerStart').style.background = '#10b981';
            }
            function evalChairTest(t) {
                document.getElementById('valKpi1').innerText = t.toFixed(1) + ' seg';
                if (t < 11.0) {
                    document.getElementById('valKpi2').innerText = 'EXCELENTE';
                    selectStep(5);
                } else if (t <= 14.5) {
                    document.getElementById('valKpi2').innerText = 'NORMAL';
                    selectStep(4);
                } else {
                    document.getElementById('valKpi2').innerText = 'REFORZAR';
                    selectStep(3);
                }
            }
        """,
        "steps": [
            {
                "num": 1, "name": "1. Sedentarismo e Inmovilidad", "badge": "Peligro Fragilidad • > 18 seg",
                "meta": "Pasar horas sentado viendo la televisión debilita las fibras musculares rápidas y duplica el riesgo de tropiezos.",
                "hero_title": "Nivel 1: El Riesgo Silencioso de Pasar el Día Sentado",
                "hero_badge": "NIVEL 1 DE 6 • FRAGILIDAD POR SEDENTARISMO",
                "hero_desc": "El músculo es un órgano vivo: lo que no se usa, el cuerpo lo desmantela. Levantarse cada hora es la primera medicina.",
                "action_text": "Ponte una alarma en el reloj: cada 60 minutos levántate, da una vuelta por el pasillo y estira las piernas.",
                "kpi1": "> 18.0 s", "kpi2": "FRÁGIL", "kpi3": "30 / 100", "kpi4": "INACTIVAS"
            },
            {
                "num": 2, "name": "2. Movilidad Básica en el Hogar", "badge": "Tareas Cotidianas • 16 a 18 seg",
                "meta": "Caminar por la casa, cocinar y asearse sin ayuda. Mantiene la independencia básica sin reserva muscular de seguridad.",
                "hero_title": "Nivel 2: La Autonomía Doméstica Elemental",
                "hero_badge": "NIVEL 2 DE 6 • MOVILIDAD DOMÉSTICA",
                "hero_desc": "Cumple con las necesidades del día a día, pero ante una gripe o reposo prolongado la fuerza puede caer con rapidez.",
                "action_text": "Añade 5 repeticiones de levantarte de la silla antes de comer: tus cuádriceps ganarán fuerza sin esfuerzo.",
                "kpi1": "17.0 s", "kpi2": "BÁSICO", "kpi3": "48 / 100", "kpi4": "DÉBILES"
            },
            {
                "num": 3, "name": "3. Caminante Habitual Llano", "badge": "Paseo Diario • 14 a 16 seg",
                "meta": "Paseos diarios de 30-45 minutos por terreno llano. Buen fondo cardiovascular pero falta trabajo de fuerza pura.",
                "hero_title": "Nivel 3: El Caminante Diario de Terreno Llano",
                "hero_badge": "NIVEL 3 DE 6 • RESISTENCIA AERÓBICA",
                "hero_desc": "Caminar es maravilloso para el corazón y el ánimo, pero los cuádriceps y glúteos necesitan también vencer gravedad.",
                "action_text": "Aprovecha tramos con ligera cuesta o sube un piso por las escaleras en lugar de coger siempre el ascensor.",
                "kpi1": "14.8 s", "kpi2": "MODERADO", "kpi3": "62 / 100", "kpi4": "MODERADAS"
            },
            {
                "num": 4, "name": "4. Fuerza Funcional Activa", "badge": "Subir Escaleras • 11 a 14 seg",
                "meta": "Sube y baja escaleras con soltura. Levanta bolsas de compra medianas y mantiene el equilibrio sobre un pie.",
                "hero_title": "Nivel 4: Músculo Funcional y Blindaje Anticaídas",
                "hero_badge": "NIVEL 4 DE 6 • FUERZA FUNCIONAL",
                "hero_desc": "Las mitocondrias de tus células musculares queman glucosa con agilidad y sostienen la postura firme sin dolor de espalda.",
                "action_text": "Coge dos botellas de agua de 1 litro y haz 10 elevaciones de brazos sentado en el sofá mientras ves las noticias.",
                "kpi1": "12.1 s", "kpi2": "AUTÓNOMO", "kpi3": "78 / 100", "kpi4": "ACTIVAS"
            },
            {
                "num": 5, "name": "5. Autonomía Robusta y Vital", "badge": "Gran Reserva • 9 a 11 seg",
                "meta": "Carga la compra de la semana, cuida nietos o el huerto sin fatiga. Capacidad de reacción rápida ante un resbalón.",
                "hero_title": "Nivel 5: La Fortaleza Serena del Senior Activo",
                "hero_badge": "NIVEL 5 DE 6 • AUTONOMÍA ROBUSTA",
                "hero_desc": "Excelente reserva mitocondrial. En caso de una intervención médica o reposo, tu cuerpo recuperará la fuerza con rapidez.",
                "action_text": "Felicidades: mantener esta rutina de movimiento alegre te garantiza muchos años de independencia plena.",
                "kpi1": "10.2 s", "kpi2": "ROBUSTO", "kpi3": "90 / 100", "kpi4": "MUY ACTIVAS"
            },
            {
                "num": 6, "name": "6. Plenitud Funcional y Longevidad", "badge": "Cima Funcional • < 9 seg",
                "meta": "Agilidad y tono muscular envidiables. Exponente de los centenarios de las Zonas Azules con longevidad activa.",
                "hero_title": "Nivel 6: Plenitud Mitocondrial y Agilidad Serena",
                "hero_badge": "NIVEL 6 DE 6 • EXCELENCIA BIOLÓGICA",
                "hero_desc": "El ejercicio de fuerza suave realizado con constancia rejuvenece los marcadores celulares mitocondriales hasta 15 años.",
                "action_text": "Comparte tu ejemplo con amigos y vecinos: el entusiasmo por moverse en grupo es el mejor regalo familiar.",
                "kpi1": "8.4 s", "kpi2": "EXCELENCIA", "kpi3": "98 / 100", "kpi4": "REJUVENECIDAS"
            }
        ],
        "prompt_seed": """Actúa como un fisioterapeuta geriátrico y médico rehabilitador para personas mayores (+65).
Explícame en 3 viñetas cómo diseñar una herramienta interactiva en HTML que evalúe la fuerza muscular cotidiana y anime a hacer ejercicios suaves de fuerza en casa sin máquinas de gimnasio.""",
        "prompt_master": """Genera el archivo HTML interactivo con el test de levantarse de la silla (5 repeticiones), selector de 6 niveles de vitalidad mitocondrial, rutina guiada de ejercicios con botellas de agua y consejos de seguridad."""
    },

    # --------------------------------------------------------------------------
    # SESIÓN 34: EL SECRETO DE LAS ZONAS AZULES & LONGEVIDAD
    # --------------------------------------------------------------------------
    {
        "code": "NIV-034", "num": 34,
        "filename": "SIMULADOR_ZONAS_AZULES_LONGEVIDAD_SENIORS.html",
        "title": "Los 5 Pilares de la Longevidad Activa: El Secreto de las Zonas Azules",
        "subtitle": "Hábitos Centenarios Adaptados al Jubilado Español",
        "icon": "🌱", "initial_level": 3,
        "kpis": [
            {"lbl": "Índice Zona Azul", "val": "82 / 100"},
            {"lbl": "Región Afin", "val": "Cerdeña (Italia)"},
            {"lbl": "Ikigai / Ilusión", "val": "ALTO"},
            {"lbl": "Tribu y Amigos", "val": "ACTIVO"}
        ],
        "aside": """
            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px;">
                <div style="font-size:0.85rem; color:#94a3b8; font-weight:700; margin-bottom:10px;">LAS 5 ZONAS AZULES DEL MUNDO</div>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
                    <button onclick="setZone(1)" style="background:rgba(56,189,248,0.15); border:1px solid #38bdf8; color:#fff; padding:8px; border-radius:8px; font-weight:700; cursor:pointer;">🇮🇹 Cerdeña</button>
                    <button onclick="setZone(2)" style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); color:#cbd5e1; padding:8px; border-radius:8px; font-weight:700; cursor:pointer;">🇯🇵 Okinawa</button>
                    <button onclick="setZone(3)" style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); color:#cbd5e1; padding:8px; border-radius:8px; font-weight:700; cursor:pointer;">🇬🇷 Icaria</button>
                    <button onclick="setZone(4)" style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); color:#cbd5e1; padding:8px; border-radius:8px; font-weight:700; cursor:pointer;">🇨🇷 Nicoya</button>
                </div>
                <div id="zoneTip" style="font-size:0.88rem; color:#cbd5e1; line-height:1.5; margin-top:12px;">
                    En <b>Cerdeña</b> los ancianos caminan por colinas, toman una copa de vino tinto con amigos y la familia los venera en casa.
                </div>
            </div>
        """,
        "script": """
            function setZone(z) {
                if (z === 1) {
                    document.getElementById('zoneTip').innerHTML = 'En <b>Cerdeña</b> los pastores centenarios caminan a diario, toman aceite de oliva virgen extra y la familia los cuida con honor.';
                    document.getElementById('valKpi2').innerText = 'Cerdeña (Italia)';
                    selectStep(3);
                } else if (z === 2) {
                    document.getElementById('zoneTip').innerHTML = 'En <b>Okinawa</b> practican el <i>Moai</i> (grupo fiel de amigos de toda la vida) y comen con la regla del 80% (Hara Hachi Bu).';
                    document.getElementById('valKpi2').innerText = 'Okinawa (Japón)';
                    selectStep(4);
                } else if (z === 3) {
                    document.getElementById('zoneTip').innerHTML = 'En <b>Icaria</b> no usan reloj: duermen la siesta cada día, beben té de hierbas de montaña y el cáncer es casi inexistente.';
                    document.getElementById('valKpi2').innerText = 'Icaria (Grecia)';
                    selectStep(5);
                } else {
                    document.getElementById('zoneTip').innerHTML = 'En <b>Nicoya</b> tienen el <i>plan de vida</i>: levantarse con un propósito claro, tomar agua rica en calcio y reír a diario.';
                    document.getElementById('valKpi2').innerText = 'Nicoya (Costa Rica)';
                    selectStep(2);
                }
            }
        """,
        "steps": [
            {
                "num": 1, "name": "1. Moverse con Naturalidad Constante", "badge": "Caminar, Subir y Cuidar Plantas",
                "meta": "Los centenarios no van al gimnasio: viven en entornos que les obligan a levantarse, pasear y cuidar el jardín.",
                "hero_title": "Pilar 1: El Movimiento Orgánico sin Máquinas de Gimnasio",
                "hero_badge": "PILAR 1 DE 5 • MOVIMIENTO NATURAL",
                "hero_desc": "La clave no es correr maratones, sino evitar permanecer sentado durante horas seguidas.",
                "action_text": "Baja a comprar el pan a pie, cuida las macetas del balcón o haz los recados caminando con buen calzado.",
                "kpi1": "65 / 100", "kpi2": "Pilar 1", "kpi3": "BUENO", "kpi4": "ACTIVO"
            },
            {
                "num": 2, "name": "2. Tener un Propósito Matinal (Ikigai)", "badge": "Un Motivo para Levantarse",
                "meta": "Saber para qué te despiertas cada día: enseñar a los nietos, cuidar las flores, leer un libro o pintar.",
                "hero_title": "Pilar 2: La Fuerza Emocional del Ikigai",
                "hero_badge": "PILAR 2 DE 5 • PROPÓSITO DE VIDA",
                "hero_desc": "Las personas con un propósito vital ilusionante viven de media 7 años más con menor incidencia de deterioro cognitivo.",
                "action_text": "Planifica hoy algo ilusionante para mañana por la mañana: quedar con un amigo, regar el jardín o escribir tus memorias.",
                "kpi1": "75 / 100", "kpi2": "Nicoya", "kpi3": "MUY ALTO", "kpi4": "CON ILUSIÓN"
            },
            {
                "num": 3, "name": "3. Bajar el Ritmo y Saborear la Siesta", "badge": "Desterrar la Prisa • 20 min Siesta",
                "meta": "El estrés crónico produce inflamación. Una siesta breve de 20 minutos reduce el riesgo cardíaco un 37%.",
                "hero_title": "Pilar 3: La Desaceleración Serena y la Pausa Reparadora",
                "hero_badge": "PILAR 3 DE 5 • GESTIÓN DEL ESTRÉS",
                "hero_desc": "En las Zonas Azules se honra el descanso: rezar, recordar a los ancestros o charlar tranquilamente a la sombra de un árbol.",
                "action_text": "Tras la comida, descansa 20 minutos en el sillón sin televisor: relaja las arterias y renueva la claridad mental.",
                "kpi1": "82 / 100", "kpi2": "Cerdeña", "kpi3": "ALTO", "kpi4": "PAUSADO"
            },
            {
                "num": 4, "name": "4. La Regla del 80% (Hara Hachi Bu)", "badge": "Comer sin Llenarse a Reventar",
                "meta": "Dejar de comer cuando sientas un 80% de saciedad. Digestiones ligeras que alargan la juventud celular.",
                "hero_title": "Pilar 4: Alimentación Frugal y Moderación Sabia",
                "hero_badge": "PILAR 4 DE 5 • NUTRICIÓN FRUGAL",
                "hero_desc": "Cenar poco y temprano permite al cuerpo dedicar la noche a reparar tejidos celulares en vez de procesar digestiones pesadas.",
                "action_text": "Cena ligero al menos 2 horas antes de dormir: un tazón de puré de verduras con pescado blanco es ideal.",
                "kpi1": "90 / 100", "kpi2": "Okinawa", "kpi3": "EXCELENTE", "kpi4": "LIGERO"
            },
            {
                "num": 5, "name": "5. La Tribu y los Vínculos Familiares", "badge": "Amor, Apoyo Mutuo y Amistad",
                "meta": "Poner a la familia en primer lugar, cuidar a la pareja y mantener un grupo leal de amigos con los que reír.",
                "hero_title": "Pilar 5: La Red Humana como Escudo Protector",
                "hero_badge": "PILAR 5 DE 5 • CONEXIÓN SOCIAL",
                "hero_desc": "La soledad no deseada equivale a fumar 15 cigarrillos al día. Los abrazos y la charla diaria protegen las defensas inmunológicas.",
                "action_text": "Llama hoy a un amigo o familiar solo para decirle que te has acordado de él: cultivar la amistad alarga la vida.",
                "kpi1": "96 / 100", "kpi2": "Icaria", "kpi3": "MÁXIMO", "kpi4": "INSEPARABLES"
            }
        ],
        "prompt_seed": """Actúa como un epidemiólogo social y divulgador de las Zonas Azules para personas mayores (+65).
Explícame en 3 viñetas cómo diseñar una calculadora en HTML que mida los 5 hábitos de los pueblos más longevos del mundo y los traslade a la vida de un jubilado en España.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con selector de los 5 pilares de longevidad, puntuación de 0 a 100 de Índice Zona Azul, mapa interactivo de las 5 regiones y compromisos cotidianos alcanzables."""
    },

    # --------------------------------------------------------------------------
    # SESIÓN 35: BAÑOS DE BOSQUE (SHINRIN-YOKU) & NATURALEZA
    # --------------------------------------------------------------------------
    {
        "code": "NIV-035", "num": 35,
        "filename": "SIMULADOR_BANOS_BOSQUE_NATURALEZA_SENIORS.html",
        "title": "Los 6 Estratos del Bosque, Paseos Verdes y Baños de Bosque (Shinrin-Yoku)",
        "subtitle": "Fitoncidas, Cortisol & Salud en el Parque (+65)",
        "icon": "🌲", "initial_level": 3,
        "kpis": [
            {"lbl": "Tiempo en Parque", "val": "45 min"},
            {"lbl": "Cortisol (Estrés)", "val": "-16% bajada"},
            {"lbl": "Tensión Arterial", "val": "-5 mmHg"},
            {"lbl": "Defensas NK", "val": "+30% activas"}
        ],
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">Minutos Semanales en Parques:</span>
                    <span class="control-badge" id="lblForestTime">45 min</span>
                </div>
                <input type="range" id="rngForestTime" min="0" max="180" value="45" step="15" oninput="calcForestHealth()">
            </div>
            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:16px;">
                <div style="font-size:0.85rem; color:#94a3b8; font-weight:700; margin-bottom:8px;">EL PODER DE LOS FITONCIDAS</div>
                <div style="font-size:0.92rem; color:#fff; line-height:1.5;">
                    Los árboles liberan compuestos aromáticos protectores (fitoncidas) para defenderse de bacterias. Al respirarlos, nuestro sistema inmune fabrica más linfocitos naturales.
                </div>
            </div>
        """,
        "script": """
            function calcForestHealth() {
                const m = parseInt(document.getElementById('rngForestTime').value);
                document.getElementById('lblForestTime').innerText = m + ' min';
                document.getElementById('valKpi1').innerText = m + ' min';
                if (m < 20) {
                    document.getElementById('valKpi2').innerText = '-3% leve';
                    document.getElementById('valKpi3').innerText = '-1 mmHg';
                    document.getElementById('valKpi4').innerText = '+5%';
                } else if (m < 60) {
                    document.getElementById('valKpi2').innerText = '-16% óptimo';
                    document.getElementById('valKpi3').innerText = '-5 mmHg';
                    document.getElementById('valKpi4').innerText = '+30%';
                } else {
                    document.getElementById('valKpi2').innerText = '-25% profundo';
                    document.getElementById('valKpi3').innerText = '-8 mmHg';
                    document.getElementById('valKpi4').innerText = '+45%';
                }
            }
        """,
        "steps": [
            {
                "num": 1, "name": "1. El Asfalto Urbano sin Verde", "badge": "Estrés y Ruido • Cero Fitoncidas",
                "meta": "Tráfico, cláxones y superficies de hormigón. Mantienen el sistema nervioso simpático en alerta innecesaria.",
                "hero_title": "Nivel 1: El Hormigón Urbano y la Fatiga Sensorial",
                "hero_badge": "NIVEL 1 DE 6 • ENTORNO DE HORMIGÓN",
                "hero_desc": "Vivir rodeado exclusivamente de asfalto y ruido constante incrementa el cortisol en sangre y dificulta conciliar el sueño.",
                "action_text": "Busca escapar a diario al menos 30 minutos a una calle arbolada o parque cercano a tu domicilio.",
                "kpi1": "0 min", "kpi2": "0% cambio", "kpi3": "0 mmHg", "kpi4": "NORMAL"
            },
            {
                "num": 2, "name": "2. Plazas Arboladas y Jardines de Barrio", "badge": "Primer Oasis • Sombra y Bancos",
                "meta": "Cuatro árboles maduros y bancos para sentarse. Primer alivio para la vista cansada y la respiración.",
                "hero_title": "Nivel 2: El Primer Respiro Verde en la Plaza del Barrio",
                "hero_badge": "NIVEL 2 DE 6 • PLAZA DE BARRIO",
                "hero_desc": "La visión del color verde relaja los músculos ciliares del ojo y disminuye la tensión muscular de hombros y cuello.",
                "action_text": "Siéntate en un banco a la sombra de un árbol y observa el movimiento de las hojas con el viento: es meditación natural.",
                "kpi1": "20 min", "kpi2": "-8%", "kpi3": "-2 mmHg", "kpi4": "+12%"
            },
            {
                "num": 3, "name": "3. Parques Urbanos Frondosos", "badge": "El Pulmón de la Ciudad • Césped",
                "meta": "Caminos de tierra sin tráfico, estanques de agua y copas densas de plátanos de sombra, castaños y pinos.",
                "hero_title": "Nivel 3: El Gran Parque Urbano y la Descompresión",
                "hero_badge": "NIVEL 3 DE 6 • PARQUE URBANO",
                "hero_desc": "Caminar sobre tierra o albero es mucho más blando para las rodillas y caderas que el asfalto duro de la acera.",
                "action_text": "Camina despacio, sin mirar el reloj. Respira hondo por la nariz para llenar los pulmones de aire limpio.",
                "kpi1": "45 min", "kpi2": "-16%", "kpi3": "-5 mmHg", "kpi4": "+30%"
            },
            {
                "num": 4, "name": "4. Dehesas, Pinares y Senderos Llanos", "badge": "Inmersión Forestal Accesible",
                "meta": "Aire puro de pinos y encinas. Los fitoncidas alcanzan concentraciones clínicas demostradas que potencian las defensas.",
                "hero_title": "Nivel 4: El Pinar y el Baño de Fitoncidas",
                "hero_badge": "NIVEL 4 DE 6 • BOSQUE ACCESIBLE",
                "hero_desc": "El olor a resina de pino y jara estimula los receptores olfativos vinculados con la calma y reduce la frecuencia cardíaca.",
                "action_text": "Organiza una excursión tranquila de mañana con amigos o familia a un sendero llano de pinar acondicionado.",
                "kpi1": "75 min", "kpi2": "-22%", "kpi3": "-7 mmHg", "kpi4": "+40%"
            },
            {
                "num": 5, "name": "5. Bosques Maduros y Valles Húmedos", "badge": "Robledales y Hayedos",
                "meta": "Micorrizas subterráneas, musgo y rumor de arroyos. Máximo silencio terapéutico y oxigenación celular.",
                "hero_title": "Nivel 5: El Bosque Maduro y la Serenidad Profunda",
                "hero_badge": "NIVEL 5 DE 6 • BOSQUE MADURO",
                "hero_desc": "El sonido del agua corriendo y el crujir de la hojarasca producen ondas alfa cerebrales idénticas a las de la meditación profunda.",
                "action_text": "Toca la corteza rugosa de un árbol centenario: la conexión física con lo vivo aporta una inmensa paz espiritual.",
                "kpi1": "120 min", "kpi2": "-28%", "kpi3": "-9 mmHg", "kpi4": "+50%"
            },
            {
                "num": 6, "name": "6. Miradores de Cumbre y Perspectiva", "badge": "Horizonte Infinito • Aire Puro",
                "meta": "La vista panorámica del valle desde lo alto. Sensación de asombro y pequeñez que relativiza todas las preocupaciones.",
                "hero_title": "Nivel 6: La Gran Perspectiva y la Paz Interior",
                "hero_badge": "NIVEL 6 DE 6 • HORIZONTE PANORÁMICO",
                "hero_desc": "La ciencia psicológica llama a esto 'Efecto Perspectiva' (Awe): contemplar la inmensidad del paisaje elimina la rumiación mental.",
                "action_text": "Respira hondo en lo alto y siente gratitud por el camino recorrido: la vida en la madurez se saborea con serenidad.",
                "kpi1": "180 min", "kpi2": "-35%", "kpi3": "-10 mmHg", "kpi4": "+60%"
            }
        ],
        "prompt_seed": """Actúa como un médico naturista y pedagogo ambiental para personas mayores (+65).
Explícame en 3 viñetas cómo estructurar una guía interactiva en HTML que explique con base científica por qué pasear bajo los árboles mejora la salud y ayude a planificar paseos agradables.""",
        "prompt_master": """Genera el archivo HTML interactivo con los 6 niveles del ecosistema forestal, medidor de beneficios médicos (reducción de tensión y estrés), planificador de paseos semanales y pautas para caminar con calzado cómodo."""
    },

    # --------------------------------------------------------------------------
    # SESIÓN 36: RADAR DE TOXICIDAD EN EL HOGAR & PREVENCIÓN
    # --------------------------------------------------------------------------
    {
        "code": "NIV-036", "num": 36,
        "filename": "SIMULADOR_TOXICIDAD_HOGAR_PREVENCION_SENIORS.html",
        "title": "El Radar de Toxicidad en el Hogar: Químicos de Limpieza, Humos y Prevención",
        "subtitle": "Mezclas Prohibidas, Monóxido de Carbono & Salud (+65)",
        "icon": "⚠️", "initial_level": 1,
        "kpis": [
            {"lbl": "Nivel de Peligro", "val": "MORTAL"},
            {"lbl": "Gas Generado", "val": "Cloramina Tóxica"},
            {"lbl": "Efecto Pulmonar", "val": "Asfixia Inmediata"},
            {"lbl": "Alternativa Segura", "val": "Vinagre Blanco"}
        ],
        "aside": """
            <div style="background:rgba(239,68,68,0.15); border:1.5px solid #ef4444; border-radius:14px; padding:16px;">
                <div style="font-size:0.85rem; color:#fca5a5; font-weight:800; margin-bottom:8px;">🚨 NUNCA MEZCLES PRODUCTOS DE LIMPIEZA</div>
                <div style="font-size:0.92rem; color:#fff; line-height:1.5;">
                    Mezclar <b>Lejía con Amoníaco</b> crea gas cloramina que quema la garganta y los pulmones en segundos. Limpia con un solo producto cada vez.
                </div>
            </div>
            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:16px; margin-top:12px;">
                <div style="font-size:0.85rem; color:#94a3b8; font-weight:700; margin-bottom:6px;">TELÉFONOS OFICIALES DE URGENCIA</div>
                <div style="font-family:var(--font-mono); font-size:1.1rem; color:#38bdf8; font-weight:800;">☎️ 91 562 04 20</div>
                <div style="font-size:0.75rem; color:#cbd5e1;">Instituto Nacional de Toxicología (24h)</div>
                <div style="font-family:var(--font-mono); font-size:1.1rem; color:#ef4444; font-weight:800; margin-top:6px;">🚨 112 Emergencias</div>
            </div>
        """,
        "script": """
            // lógica adicional si se requiere
        """,
        "steps": [
            {
                "num": 1, "name": "1. Lejía + Amoníaco (Gas Cloramina)", "badge": "PELIGRO DE ASFIXIA • NUNCA MEZCLAR",
                "meta": "Produce vapores blanquecinos de cloramina que queman los ojos, garganta y provocan edema pulmonar agudo.",
                "hero_title": "Peligro Crítico: La Mezcla Mortal de Lejía y Amoníaco",
                "hero_badge": "MEZCLA PROHIBIDA 1 • CLORAMINA TÓXICA",
                "hero_desc": "Mucha gente cree que mezclando dos limpiadores desinfectará más. Es un error gravísimo que causa ingresos hospitalarios urgentes.",
                "action_text": "Si por error notas olor picante, sal inmediatamente de la habitación, abre ventanas y respira aire puro en el balcón o calle.",
                "kpi1": "MORTAL", "kpi2": "Cloramina", "kpi3": "Edema Pulmonar", "kpi4": "Jabón Neutro"
            },
            {
                "num": 2, "name": "2. Lejía + Salfumán / Vinagre (Cloro Gas)", "badge": "VAPOR VERDE CORROSIVO • PELIGRO EXTREMO",
                "meta": "El ácido clorhídrico (agua fuerte o salfumán) descompone la lejía liberando gas cloro puro, altamente corrosivo.",
                "hero_title": "Peligro Extremo: Lejía con Ácidos o Salfumán",
                "hero_badge": "MEZCLA PROHIBIDA 2 • GAS CLORO ASFIXIANTE",
                "hero_desc": "El gas cloro destruye las mucosas respiratorias. Nunca uses salfumán para el inodoro si antes echaste lejía.",
                "action_text": "Para quitar la cal del váter, usa solo vinagre de limpieza caliente. Es 100% inofensivo y disuelve la cal por completo.",
                "kpi1": "EXTREMO", "kpi2": "Cloro Gas", "kpi3": "Quemadura Vías", "kpi4": "Vinagre Limpieza"
            },
            {
                "num": 3, "name": "3. Monóxido de Carbono (Estufas y Braseros)", "badge": "El Asesino Silencioso • Gas Invisible",
                "meta": "Estufas de butano, calderas o braseros con mala combustión. No huele ni pica, da sueño y adormece.",
                "hero_title": "Alerta Silenciosa: Monóxido de Carbono (CO)",
                "hero_badge": "RIESGO EN EL HOGAR 3 • LA MUERTE DULCE",
                "hero_desc": "Una llama amarilla o naranja indica mala combustión peligrosa. La llama debe ser siempre limpia y azulada.",
                "action_text": "Nunca tapes las rejillas de ventilación de la cocina. Ventila 10 minutos cada mañana y revisa la caldera anualmente.",
                "kpi1": "INODORO", "kpi2": "Monóxido CO", "kpi3": "Adormecimiento", "kpi4": "Llama Azul 100%"
            },
            {
                "num": 4, "name": "4. Sprays e Insecticidas en Espacios Cerrados", "badge": "Aerosoles Químicos • Ventilación Obligatoria",
                "meta": "Vapores inflamables de ambientadores y matamoscas que saturan el aire del salón y provocan ataques de tos.",
                "hero_title": "Prevención: El Uso Prudente de Aerosoles Domésticos",
                "hero_badge": "RIESGO EN EL HOGAR 4 • AEROSOLES Y HUMOS",
                "hero_desc": "Los propelentes de los sprays son irritantes para los bronquios, especialmente en personas con asma o EPOC.",
                "action_text": "Para perfumar la casa, hierve agua con una rama de canela o cáscara de naranja: ambientador natural delicioso y sin químicos.",
                "kpi1": "IRRITANTE", "kpi2": "Propelentes", "kpi3": "Tos y Asma", "kpi4": "Canela / Naranja"
            },
            {
                "num": 5, "name": "5. El Hogar Seguro: Alternativas Ecológicas", "badge": "Bicarbonato, Vinagre y Jabón Tradicional",
                "meta": "Los trucos de toda la vida: limpian a fondo, no desprenden humos tóxicos y son baratísimos.",
                "hero_title": "La Solución Inteligente: Limpieza Tradicional Segura",
                "hero_badge": "HOGAR BLINDADO 5 • MÁXIMA SEGURIDAD",
                "hero_desc": "El bicarbonato sódico arrastra la grasa y desodoriza; el vinagre elimina la cal; y el jabón de lagarto lava sin alergias.",
                "action_text": "Adopta estos tres ingredientes en tu rutina: tu hogar olerá a limpio sin poner en riesgo tus pulmones ni tu pensión.",
                "kpi1": "INOFENSIVO", "kpi2": "Inerte", "kpi3": "Cero Riesgo", "kpi4": "Bicarbonato"
            }
        ],
        "prompt_seed": """Actúa como un jefe de bomberos y toxicólogo médico especializado en el hogar de personas mayores (+65).
Explícame en 3 viñetas cómo diseñar un detector interactivo en HTML que alerte de las mezclas peligrosas de limpieza y de los humos invisibles en casa.""",
        "prompt_master": """Genera la aplicación interactiva en HTML con matriz de mezclas prohibidas (lejía + amoníaco, etc.), semáforo de monóxido de carbono en calefacción, alternativas de limpieza natural segura y botón de urgencia toxicológica (91 562 04 20)."""
    },

    # --------------------------------------------------------------------------
    # SESIÓN 37: TERMORREGULACIÓN & CONFORT EN EL HOGAR
    # --------------------------------------------------------------------------
    {
        "code": "NIV-037", "num": 37,
        "filename": "SIMULADOR_TERMORREGULACION_CONFORT_SENIORS.html",
        "title": "Los 6 Niveles de Termorregulación Corporal, Abrigarse Bien y Evitar Caídas por Frío",
        "subtitle": "Termostato a 21 °C & Técnica de la Cebolla (+65)",
        "icon": "🧣", "initial_level": 3,
        "kpis": [
            {"lbl": "Termostato Salón", "val": "21 °C"},
            {"lbl": "Estado de Confort", "val": "ÓPTIMO SANIDAD"},
            {"lbl": "Ahorro Energético", "val": "14% anual"},
            {"lbl": "Riesgo Articular", "val": "MÍNIMO"}
        ],
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">Temperatura del Salón:</span>
                    <span class="control-badge" id="lblTemp">21 °C</span>
                </div>
                <input type="range" id="rngTemp" min="15" max="27" value="21" step="1" oninput="calcThermal()">
            </div>
            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:16px;">
                <div style="font-size:0.85rem; color:#94a3b8; font-weight:700; margin-bottom:8px;">LA REGLA DEL 7% DE AHORRO</div>
                <div style="font-size:0.92rem; color:#fff; line-height:1.5;">
                    Cada grado que subes la calefacción por encima de 21 °C encarece la factura un <b>7% mensual</b> y reseca la garganta.
                </div>
            </div>
        """,
        "script": """
            function calcThermal() {
                const t = parseInt(document.getElementById('rngTemp').value);
                document.getElementById('lblTemp').innerText = t + ' °C';
                document.getElementById('valKpi1').innerText = t + ' °C';
                if (t < 17) {
                    selectStep(1);
                    document.getElementById('valKpi2').innerText = 'FRÍO PELIGROSO';
                    document.getElementById('valKpi4').innerText = 'ALTO (Agarrotamiento)';
                } else if (t < 20) {
                    selectStep(2);
                    document.getElementById('valKpi2').innerText = 'FRESCO (Abrigo)';
                    document.getElementById('valKpi4').innerText = 'MODERADO';
                } else if (t <= 22) {
                    selectStep(3);
                    document.getElementById('valKpi2').innerText = 'ÓPTIMO SANIDAD';
                    document.getElementById('valKpi4').innerText = 'MÍNIMO';
                } else if (t <= 24) {
                    selectStep(4);
                    document.getElementById('valKpi2').innerText = 'AGRADABLE';
                    document.getElementById('valKpi4').innerText = 'BAJO';
                } else {
                    selectStep(5);
                    document.getElementById('valKpi2').innerText = 'EXCESIVO / SECO';
                    document.getElementById('valKpi4').innerText = 'DESHIDRATACIÓN';
                }
            }
        """,
        "steps": [
            {
                "num": 1, "name": "1. Hipotermia y Frío Doméstico (< 16 °C)", "badge": "Riesgo Cardiovascular y Agarrotamiento",
                "meta": "Tener la casa a menos de 16 °C estrecha las arterias, eleva la tensión arterial y entumece los dedos.",
                "hero_title": "Nivel 1: El Frío que Paraliza y Duplica los Tropiezos",
                "hero_badge": "NIVEL 1 DE 6 • FRÍO SEVERO EN EL HOGAR",
                "hero_desc": "Con la edad se pierde capa de grasa subcutánea. Pasar frío en casa agarrota las rodillas y es la causa oculta de muchas caídas matutinas.",
                "action_text": "Nunca dejes que la casa baje de 18 °C. Usa mantas polares ligeras y calcetines gruesos de lana natural sin costuras.",
                "kpi1": "< 16 °C", "kpi2": "HIPOTERMIA", "kpi3": "0% ahorro", "kpi4": "ALTO RIESGO"
            },
            {
                "num": 2, "name": "2. Ambiente Fresco (17 a 19 °C)", "badge": "Requiere Jersey y Calzado de Lana",
                "meta": "Aceptable para personas activas que se mueven, pero exige zapatillas abrigadas con suela de goma antideslizante.",
                "hero_title": "Nivel 2: La Franja Fresca que Exige Vestir por Capas",
                "hero_badge": "NIVEL 2 DE 6 • AMBIENTE FRESCO",
                "hero_desc": "Sentarse a leer o coser a 18 °C enfría rápidamente los pies. El cuerpo desvía sangre hacia el torso y deja los dedos helados.",
                "action_text": "Usa una chaqueta o forro polar suave y pon una alfombrilla con base de goma bajo tus pies en la mesa camilla.",
                "kpi1": "18 °C", "kpi2": "FRESCO", "kpi3": "21% ahorro", "kpi4": "MODERADO"
            },
            {
                "num": 3, "name": "3. Confort Óptimo de Salud (20 a 21 °C)", "badge": "Recomendación Oficial del Ministerio",
                "meta": "La temperatura ideal: mantiene las vías respiratorias húmedas, previene catarros y optimiza el consumo de gas o luz.",
                "hero_title": "Nivel 3: El Punto Dulce del Confort y la Salud",
                "hero_badge": "NIVEL 3 DE 6 • EQUILIBRIO PERFECTO",
                "hero_desc": "A 21 °C el corazón bombea relajado, las articulaciones se mantienen flexibles y se descansa plácidamente.",
                "action_text": "Fija tu termostato a 21 °C de día y bájalo a 18 °C para dormir con un buen nórdico: ahorrarás dinero y ganarás salud.",
                "kpi1": "21 °C", "kpi2": "ÓPTIMO", "kpi3": "14% ahorro", "kpi4": "MÍNIMO"
            },
            {
                "num": 4, "name": "4. Ambiente Muy Cálido (22 a 24 °C)", "badge": "Confort para Lectura Sedentaria",
                "meta": "Sensación de calidez agradable, pero encarece la factura eléctrica y exige ventilar para no viciar el aire.",
                "hero_title": "Nivel 4: Calidez Agradable pero de Mayor Gasto",
                "hero_badge": "NIVEL 4 DE 6 • CALIDEZ ELEVADA",
                "hero_desc": "Si tienes más de 80 años o pasas muchas horas en reposo absoluto puede apetecerte este calorcito, pero vigila la hidratación.",
                "action_text": "Coloca un cuenco con agua sobre los radiadores: añade humedad al ambiente para que no se te reseque la garganta.",
                "kpi1": "23 °C", "kpi2": "CÁLIDO", "kpi3": "-14% gasto", "kpi4": "BAJO"
            },
            {
                "num": 5, "name": "5. Calor Sofocante y Aire Seco (25 a 27 °C)", "badge": "Resequedad de Mucosas y Mareos",
                "meta": "Calefacción disparada. Reseca la saliva, congestiona la nariz y provoca mareos bruscos al ponerse de pie.",
                "hero_title": "Nivel 5: El Exceso de Calor que Agota el Cuerpo",
                "hero_badge": "NIVEL 5 DE 6 • CALOR EXCESIVO",
                "hero_desc": "Estar en mangas cortas en enero dentro de casa mientras fuera hiela es peligroso: el contraste térmico al salir provoca bronquitis.",
                "action_text": "Baja 3 grados el termostato y ponte un jersey suave: tu bolsillo lo agradecerá y respirarás aire mucho más limpio.",
                "kpi1": "26 °C", "kpi2": "SOFOCANTE", "kpi3": "-35% gasto", "kpi4": "MAREOS"
            },
            {
                "num": 6, "name": "6. Alerta de Golpe de Calor (> 28 °C en Verano)", "badge": "Riesgo de Deshidratación Aguda",
                "meta": "Olas de calor veraniegas. Los mayores no sienten sed a tiempo y el cuerpo no suda con la misma eficacia.",
                "hero_title": "Nivel 6: El Peligro del Calor Estival en Mayores",
                "hero_badge": "NIVEL 6 DE 6 • ALERTA DE CALOR ESTIVAL",
                "hero_desc": "En verano el calor es más peligroso que el frío. Requiere beber agua sin esperar a tener sed y bajar persianas en horas pico.",
                "action_text": "Baja persianas en las horas centrales de sol, usa ventiladores suaves y refréscate muñecas y nuca con agua fresca.",
                "kpi1": "> 28 °C", "kpi2": "GOLPE CALOR", "kpi3": "URGENCIA", "kpi4": "DESHIDRATACIÓN"
            }
        ],
        "prompt_seed": """Actúa como un médico geriatra y especialista en medicina del confort doméstico para personas mayores (+65).
Explícame en 3 viñetas cómo diseñar una herramienta interactiva en HTML que enseñe a regular la temperatura del hogar y protegerse del frío sin riesgos de caídas ni braseros peligrosos.""",
        "prompt_master": """Genera el archivo HTML interactivo con termómetro de confort (18 °C a 24 °C), selector de los 6 niveles de respuesta térmica corporal, recomendador de ropa por capas y protocolo para salir a la calle en días fríos."""
    },

    # --------------------------------------------------------------------------
    # SESIÓN 38: ERGONOMÍA, ESPALDA & ARTICULACIONES
    # --------------------------------------------------------------------------
    {
        "code": "NIV-038", "num": 38,
        "filename": "SIMULADOR_ERGONOMIA_COLUMNA_ARTICULACIONES_SENIORS.html",
        "title": "Calculadora de Ergonomía y Esfuerzo Doméstico: Cuidar Espalda y Articulaciones",
        "subtitle": "Presión Lumbar L5-S1 & Carro de 4 Ruedas (+65)",
        "icon": "🛒", "initial_level": 2,
        "kpis": [
            {"lbl": "Peso Levantado", "val": "5 kg"},
            {"lbl": "Presión en L5-S1", "val": "180 kg (Doblando espalda)"},
            {"lbl": "Si flexionas piernas", "val": "50 kg (¡-72% alivio!)"},
            {"lbl": "Riesgo de Lumbalgia", "val": "ALTO"}
        ],
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">Peso del Paquete / Compra:</span>
                    <span class="control-badge" id="lblLoadWeight">5 kg</span>
                </div>
                <input type="range" id="rngLoadWeight" min="2" max="15" value="5" step="1" oninput="calcErgo()">
            </div>
            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:16px;">
                <div style="font-size:0.85rem; color:#94a3b8; font-weight:700; margin-bottom:8px;">EL SECRETO DEL CARRO DE 4 RUEDAS</div>
                <div style="font-size:0.92rem; color:#fff; line-height:1.5;">
                    Arrastrar un carro de 2 ruedas tira de la espalda y hombro hacia atrás. Un carro de <b>4 ruedas que se empuja hacia adelante</b> reduce el esfuerzo un 60%.
                </div>
            </div>
        """,
        "script": """
            function calcErgo() {
                const kg = parseInt(document.getElementById('rngLoadWeight').value);
                document.getElementById('lblLoadWeight').innerText = kg + ' kg';
                document.getElementById('valKpi1').innerText = kg + ' kg';
                const badPress = Math.round(kg * 36);
                const goodPress = Math.round(kg * 10);
                document.getElementById('valKpi2').innerText = badPress + ' kg (Lomo curvo)';
                document.getElementById('valKpi3').innerText = goodPress + ' kg (Flexionando)';
                if (kg > 8) {
                    document.getElementById('valKpi4').innerText = 'CRÍTICO';
                    selectStep(1);
                } else if (kg > 4) {
                    document.getElementById('valKpi4').innerText = 'ALTO';
                    selectStep(2);
                } else {
                    document.getElementById('valKpi4').innerText = 'SEGURO';
                    selectStep(5);
                }
            }
        """,
        "steps": [
            {
                "num": 1, "name": "1. Levantar Peso Doblando la Cintura (A Plomo)", "badge": "SOBRECARGA SEVERA • RIESGO DE HERNIA",
                "meta": "Piernas rectas y espalda curvada: la columna actúa como una palanca desfavorable multiplicando la carga por 30.",
                "hero_title": "Peligro: Agacharse sin Doblar las Rodillas",
                "hero_badge": "POSTURA INCORRECTA 1 • PALANCA LUMBAR DESTRUCTIVA",
                "hero_desc": "Levantar un paquete de 5 kg con las piernas rígidas transmite casi 200 kg de presión directa a los discos intervertebrales L5-S1.",
                "action_text": "Dobla siempre las rodillas, mantén la espalda erguida y pega el paquete contra tu pecho antes de levantarte.",
                "kpi1": "5 kg", "kpi2": "180 kg", "kpi3": "50 kg", "kpi4": "ALTO RIESGO"
            },
            {
                "num": 2, "name": "2. Arrastrar el Carro de la Compra a Dos Ruedas", "badge": "Tirón Asimétrico en Hombro y Cadera",
                "meta": "Tirar de 12 kg con un solo brazo retuerce la pelvis y fuerza el hombro hacia atrás, sobrecargando el trapecio.",
                "hero_title": "Postura Inadecuada: El Carro de Dos Ruedas Arrastrado",
                "hero_badge": "POSTURA INCORRECTA 2 • ROTACIÓN ASIMÉTRICA",
                "hero_desc": "La fuerza asimétrica continua causa contracturas cervicales y lumbalgias que se confunden falsamente con artrosis.",
                "action_text": "Pasa a un carro de 4 ruedas y empújalo con ambas manos hacia adelante como si fuera un carrito de supermercado.",
                "kpi1": "10 kg", "kpi2": "Arrastre unilateral", "kpi3": "Empuje simétrico", "kpi4": "MODERADO"
            },
            {
                "num": 3, "name": "3. Barrer y Fregar con Mango Corto", "badge": "Espalda Encorvada Continuada",
                "meta": "Usar fregonas o escobas cortas obliga a estar inclinado hacia adelante durante 20 minutos seguidos.",
                "hero_title": "Ergonomía en la Limpieza: La Altura Correcta del Palo",
                "hero_badge": "POSTURA DOMÉSTICA 3 • HIGIENE DE COLUMNA",
                "hero_desc": "El palo de la escoba o fregona debe llegar al menos a la altura de tu barbilla para poder limpiar con la espalda 100% recta.",
                "action_text": "Compra mangos largos de 1.40 metros: limpiarás con la espalda apoyada y los brazos descansados.",
                "kpi1": "0 kg", "kpi2": "Cifosis postural", "kpi3": "Postura recta", "kpi4": "CONTRACTURA"
            },
            {
                "num": 4, "name": "4. Planchar y Estar de Pie sin Apoyo", "badge": "Sobrecarga en Zona Sacroilíaca",
                "meta": "Permanecer quieto de pie sobre suelo duro fatiga la zona baja de la espalda y sobrecarga las venas varicosas.",
                "hero_title": "El Truco del Taburete para Planchar o Cocinar",
                "hero_badge": "POSTURA DOMÉSTICA 4 • DESCANSO LUMBAR",
                "hero_desc": "Apoyar un pie en un pequeño peldaño o taco de madera de 15 cm bascula la pelvis y relaja la zona lumbar al instante.",
                "action_text": "Coloca una pequeña caja o taburete bajo tus pies al planchar y ve alternando el pie apoyado cada 10 minutos.",
                "kpi1": "0 kg", "kpi2": "Tensión estática", "kpi3": "Pelvis liberada", "kpi4": "ALIVIO RÁPIDO"
            },
            {
                "num": 5, "name": "5. Repartir las Bolsas de la Compra en 2 Manos", "badge": "Equilibrio Perfecto de Cargas",
                "meta": "Llevar 4 kg en la mano izquierda y 4 kg en la derecha equilibra la columna como una balanza perfecta.",
                "hero_title": "La Regla de Oro: Simetría en los Brazos",
                "hero_badge": "HÁBITO SEGURO 5 • EQUILIBRIO TOTAL",
                "hero_desc": "La columna vertebral agradece el peso equilibrado: los músculos erectores trabajan simétricamente sin dolor.",
                "action_text": "Pide en la tienda que te repartan los productos pesados en dos bolsas iguales para caminar recto y seguro a casa.",
                "kpi1": "4+4 kg", "kpi2": "Simétrico", "kpi3": "Balanceado", "kpi4": "100% SEGURO"
            }
        ],
        "prompt_seed": """Actúa como un traumatólogo y fisioterapeuta ergonómico para personas mayores (+65).
Explícame en 3 viñetas cómo crear una calculadora interactiva en HTML que muestre cuánto sufre la columna lumbar según la postura adoptada en tareas de la casa y enseñe a evitar lesiones.""",
        "prompt_master": """Genera el archivo HTML interactivo con calculadora de carga lumbar en kg (según postura recta vs doblada), comparador de 5 tareas cotidianas (carro de la compra, fregar el suelo, planchar, levantar peso), y decálogo visual de higiene postural."""
    },

    # --------------------------------------------------------------------------
    # SESIÓN 39: ILUMINACIÓN ACCESIBLE, CONTRASTE & SALUD OCULAR
    # --------------------------------------------------------------------------
    {
        "code": "NIV-039", "num": 39,
        "filename": "SIMULADOR_ILUMINACION_CUIDADO_OCULAR_SENIORS.html",
        "title": "Guía Interactiva de Iluminación Accesible, Contraste y Cuidado Ocular",
        "subtitle": "Lúmenes Reales, Contraste Anticaídas & Salud Visual (+65)",
        "icon": "💡", "initial_level": 3,
        "kpis": [
            {"lbl": "Edad del Ojo", "val": "70 años"},
            {"lbl": "Luz Necesaria", "val": "x3 veces más"},
            {"lbl": "Iluminación Lectura", "val": "600 Lux"},
            {"lbl": "Temperatura Color", "val": "3000K (Cálida)"}
        ],
        "aside": """
            <div class="control-group">
                <div class="control-label-row">
                    <span class="control-label">Edad del Usuario:</span>
                    <span class="control-badge" id="lblEyeAge">70 años</span>
                </div>
                <input type="range" id="rngEyeAge" min="50" max="90" value="70" step="5" oninput="calcEyeLight()">
            </div>
            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:16px;">
                <div style="font-size:0.85rem; color:#94a3b8; font-weight:700; margin-bottom:8px;">EL OJO MADURO NECESITA MÁS LUZ</div>
                <div style="font-size:0.92rem; color:#fff; line-height:1.5;">
                    Con los años el cristalino amarillea de forma natural y la pupila se abre menos: una persona de 70 años necesita <b>el triple de luz</b> que una de 20 para leer sin dolor de cabeza.
                </div>
            </div>
        """,
        "script": """
            function calcEyeLight() {
                const a = parseInt(document.getElementById('rngEyeAge').value);
                document.getElementById('lblEyeAge').innerText = a + ' años';
                document.getElementById('valKpi1').innerText = a + ' años';
                if (a < 60) {
                    document.getElementById('valKpi2').innerText = 'x1.8 normal';
                    document.getElementById('valKpi3').innerText = '400 Lux';
                    selectStep(1);
                } else if (a < 75) {
                    document.getElementById('valKpi2').innerText = 'x3.0 triple';
                    document.getElementById('valKpi3').innerText = '600 Lux';
                    selectStep(3);
                } else {
                    document.getElementById('valKpi2').innerText = 'x4.5 cuádruple';
                    document.getElementById('valKpi3').innerText = '800 Lux';
                    selectStep(4);
                }
            }
        """,
        "steps": [
            {
                "num": 1, "name": "1. Pasillos y Escaleras en Penumbra", "badge": "ZONA DE RIESGO DE TROPIEZO",
                "meta": "Bombillas tenues de 40W en pasillos largos: impiden ver pequeñas alfombras o zapatillas en el suelo.",
                "hero_title": "Peligro Doméstico: La Penumbra en Zonas de Paso",
                "hero_badge": "NIVEL 1 DE 5 • RIESGO EN PASILLOS",
                "hero_desc": "El 70% de las caídas nocturnas en casa ocurren al levantarse a oscuras para ir al baño.",
                "action_text": "Instala luces nocturnas piloto enchufables con sensor de movimiento: iluminan suavemente el suelo sin deslumbrar.",
                "kpi1": "70 años", "kpi2": "x3 luz", "kpi3": "100 Lux (Insuficiente)", "kpi4": "ALTO RIESGO"
            },
            {
                "num": 2, "name": "2. Salón y Sala de Estar con Luz Difusa", "badge": "250 a 350 Lux • Ambiente Acogedor",
                "meta": "Iluminación cálida que baña toda la estancia sin crear sombras duras ni reflejos molestos en el televisor.",
                "hero_title": "Nivel 2: La Luz General del Salón",
                "hero_badge": "NIVEL 2 DE 5 • LUZ AMBIENTAL",
                "hero_desc": "Utilizar pantallas de tela o lámparas con difusor reparte la luz uniformemente para no deslumbrar.",
                "action_text": "Usa bombillas LED de 3000K (luz cálida): reproduce los colores naturales sin fatigar los ojos.",
                "kpi1": "70 años", "kpi2": "x3 luz", "kpi3": "300 Lux", "kpi4": "3000K Cálida"
            },
            {
                "num": 3, "name": "3. Rincón de Lectura y Costura", "badge": "500 a 700 Lux • Foco Dirigido",
                "meta": "Lámpara orientable situada por detrás o al lado del hombro que enfoca directamente sobre la página o labor.",
                "hero_title": "Nivel 3: El Rincón de Lectura con Luz de Precisión",
                "hero_badge": "NIVEL 3 DE 5 • LECTURA Y COSTURA",
                "hero_desc": "La luz debe dar sobre el libro, nunca directamente a los ojos. Así se lee con nitidez sin forzar la vista.",
                "action_text": "Un flexo orientable con bombilla LED de 8W-10W te permitirá leer durante horas sin picor de ojos ni dolor de cabeza.",
                "kpi1": "70 años", "kpi2": "x3 luz", "kpi3": "600 Lux", "kpi4": "3000K Focal"
            },
            {
                "num": 4, "name": "4. Cocina y Encimera Segura", "badge": "500 Lux • Claridad para Cortar y Medicación",
                "meta": "Luces bajo los muebles altos que iluminan la encimera. Clave para cortar alimentos o leer prospectos sin error.",
                "hero_title": "Nivel 4: Claridad Absoluta en la Cocina",
                "hero_badge": "NIVEL 4 DE 5 • SEGURIDAD EN COCINA",
                "hero_desc": "Evita ponerte de espaldas a la luz del techo: tu propio cuerpo crearía una sombra sobre el cuchillo o las pastillas.",
                "action_text": "Coloca una tira LED adhesiva bajo los armarios de la cocina: cocinarás con total seguridad visual.",
                "kpi1": "70 años", "kpi2": "x3 luz", "kpi3": "500 Lux", "kpi4": "4000K Neutra"
            },
            {
                "num": 5, "name": "5. Contraste Visual Antideslizante", "badge": "Bordes de Escalones y Marcos Contrastados",
                "meta": "Pintar o poner cinta adhesiva contrastada en el borde del escalón y en los interruptores de la pared.",
                "hero_title": "Nivel 5: El Escudo de la Accesibilidad Visual",
                "hero_badge": "NIVEL 5 DE 5 • BLINDAJE POR CONTRASTE",
                "hero_desc": "El ojo maduro distingue peor los tonos parecidos. Un escalón del mismo color que el suelo es una trampa invisible.",
                "action_text": "Pon cinta de alto contraste en el borde del plato de ducha y en el último peldaño de la escalera: tropiezos cero.",
                "kpi1": "70 años", "kpi2": "x3 luz", "kpi3": "Contraste Alto", "kpi4": "MÁXIMA SEGURIDAD"
            }
        ],
        "prompt_seed": """Actúa como un médico oftalmólogo y diseñador de accesibilidad para personas mayores (+65).
Explícame en 3 viñetas cómo diseñar un simulador interactivo en HTML que muestre cuánta luz necesita un hogar senior para leer y caminar seguro sin tropezar por sombras o reflejos.""",
        "prompt_master": """Genera el archivo HTML interactivo con simulador de luminosidad por estancia (salón, cocina, pasillo, lectura), recomendador de bombillas LED cálidas (3000K, sin parpadeos), contraste visual antideslumbrante y consejos oftalmológicos preventivos."""
    },

    # --------------------------------------------------------------------------
    # SESIÓN 40: CUIDADO DE LA PIEL, CICATRIZACIÓN & DERMATOLOGÍA
    # --------------------------------------------------------------------------
    {
        "code": "NIV-040", "num": 40,
        "filename": "SIMULADOR_CUIDADO_PIEL_CICATRIZACION_SENIORS.html",
        "title": "Los 5 Niveles de Regeneración Cutánea, Cuidado de la Piel y Cicatrización",
        "subtitle": "Piel Madura, Crema de Urea & Regla ABCD (+65)",
        "icon": "🧴", "initial_level": 3,
        "kpis": [
            {"lbl": "Hidratación Dérmica", "val": "ÓPTIMA (Urea 10%)"},
            {"lbl": "Barrera Cutánea", "val": "PROTEGIDA"},
            {"lbl": "Regeneración", "val": "EFICAZ Y LIMPIA"},
            {"lbl": "Vigilancia Pecas", "val": "REGLA ABCD"}
        ],
        "aside": """
            <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:16px;">
                <div style="font-size:0.85rem; color:#94a3b8; font-weight:700; margin-bottom:8px;">LA REGLA ABCD DE LUNARES Y PECAS</div>
                <div style="font-size:0.85rem; color:#cbd5e1; line-height:1.5;">
                    • <b>A</b>simetría: la mitad no coincide con la otra.<br>
                    • <b>B</b>ordes: irregulares o festoneados.<br>
                    • <b>C</b>olor: tonos negros, marrones o rojizos mezclados.<br>
                    • <b>D</b>iámetro: mayor de 6 mm (goma de un lápiz).<br>
                    <span style="color:#10b981; font-weight:700;">Si cambia, consulta al médico de cabecera con total tranquilidad.</span>
                </div>
            </div>
            <div style="background:rgba(16,185,129,0.1); border:1px solid rgba(16,185,129,0.3); border-radius:14px; padding:14px; margin-top:12px;">
                <div style="font-size:0.82rem; color:#6ee7b7; font-weight:800; margin-bottom:4px;">CREMA CON UREA AL 10%</div>
                <div style="font-size:0.85rem; color:#fff;">
                    Aplícala en piernas y brazos tras la ducha: retiene el agua celular, calma el picor de la piel seca y evita que se agriete.
                </div>
            </div>
        """,
        "script": """
            // lógica adicional
        """,
        "steps": [
            {
                "num": 1, "name": "1. Piel Seca y Picor (Prurito Senil)", "badge": "Pérdida de Lípidos Naturales",
                "meta": "Piel tirante que pica en piernas y brazos al acostarse. Causada por jabones agresivos y duchas con agua ardiendo.",
                "hero_title": "Nivel 1: La Piel Seca y el Círculo del Rascado",
                "hero_badge": "NIVEL 1 DE 5 • SEQUEDAD CUTÁNEA",
                "hero_desc": "Con la edad las glándulas sebáceas producen menos grasa protectora. Rascarnos rompe la barrera y puede causar pequeñas infecciones.",
                "action_text": "Usa gel syndet (sin jabón alcalino), dúchate con agua templada y aplícate crema hidratante antes de secarte del todo.",
                "kpi1": "DESHIDRATADA", "kpi2": "AGRIETADA", "kpi3": "LENTA", "kpi4": "PICOR FRECUENTE"
            },
            {
                "num": 2, "name": "2. Fragilidad Capilar ('Piel de Cebolla')", "badge": "Moratones Fáciles ante Roces Leves",
                "meta": "Manchas moradas en antebrazos tras rozarse con una puerta o mesa. Capilares frágiles que sangran bajo la piel fina.",
                "hero_title": "Nivel 2: La Fragilidad Capilar o Púrpura Senil",
                "hero_badge": "NIVEL 2 DE 5 • FRAGILIDAD CAPILAR",
                "hero_desc": "Son totalmente benignos y desaparecen solos en 10-15 días. No indican ninguna enfermedad grave de la sangre.",
                "action_text": "Usa mangas largas finas de algodón en casa y evita tirones con esparadrapos agresivos: usa apósitos de silicona.",
                "kpi1": "FINA", "kpi2": "FRÁGIL", "kpi3": "MODERADA", "kpi4": "ROCES LEVES"
            },
            {
                "num": 3, "name": "3. Cura en 3 Pasos de Rozaduras y Cortes", "badge": "Agua, Clorhexidina y Apósito Suave",
                "meta": "Lavar con suero o agua y jabón, desinfectar con clorhexidina transparente y tapar con apósito transpirable sin pegar en la herida.",
                "hero_title": "Nivel 3: El Protocolo Limpio de Cura Doméstica",
                "hero_badge": "NIVEL 3 DE 5 • CICATRIZACIÓN EFICAZ",
                "hero_desc": "Evita el alcohol o agua oxigenada en heridas abiertas (queman las células vivas que intentan cerrar la herida).",
                "action_text": "Usa apósitos de silicona que no tiran de la piel al retirarlos: curan más rápido y no duelen nada.",
                "kpi1": "PROTEGIDA", "kpi2": "BARRERA ACTIVA", "kpi3": "EFICAZ", "kpi4": "CURA LIMPIA"
            },
            {
                "num": 4, "name": "4. Protección Solar y Queratosis Actínicas", "badge": "Protector Solar FPS 50 en la Cara",
                "meta": "El sol que tomamos a lo largo de toda la vida tiene memoria. Pequeñas costras rasposas en nariz, calva o mejillas.",
                "hero_title": "Nivel 4: La Memoria Solar y el Cuidado Dermatológico",
                "hero_badge": "NIVEL 4 DE 5 • ESCUDO SOLAR",
                "hero_desc": "Ponerse crema solar para pasear por la mañana previene lesiones y mantiene la piel tersa y sana.",
                "action_text": "Ponte una gorra con visera o sombrero al salir a pasear y crema solar en la cara incluso en días nublados.",
                "kpi1": "PROTEGIDA", "kpi2": "ESCUDO SOLAR", "kpi3": "REGENERADA", "kpi4": "REVISIÓN ANUAL"
            },
            {
                "num": 5, "name": "5. Piel Blindada, Elástica y en Paz", "badge": "Barrera Íntegra y Confort Diario",
                "meta": "Piel suave, sin picor, nutrida diariamente con crema emoliente y revisada periódicamente con total tranquilidad.",
                "hero_title": "Nivel 5: La Piel Madura Cuidada con Amor",
                "hero_badge": "NIVEL 5 DE 5 • PLENITUD Y CONFORT",
                "hero_desc": "Cuidar la piel cada día es un acto de cariño hacia uno mismo que regala bienestar, elimina molestias y previene complicaciones.",
                "action_text": "Convierte el momento de la crema tras el aseo en un masaje relajante para tus piernas y brazos: te sentirás como nuevo.",
                "kpi1": "HIDRATADA", "kpi2": "BLINDADA", "kpi3": "ÓPTIMA", "kpi4": "TRANQUILIDAD"
            }
        ],
        "prompt_seed": """Actúa como un médico dermatólogo y enfermero geriátrico para personas mayores (+65).
Explícame en 3 viñetas cómo diseñar una herramienta interactiva en HTML que enseñe a cuidar la piel frágil de las piernas y brazos, curar rozaduras sin dolor y vigilar manchas solares sin alarmismo.""",
        "prompt_master": """Genera el archivo HTML interactivo con los 5 niveles de salud de la piel madura, guía de hidratación diaria (urea), protocolo de cura en 3 pasos para heridas leves, y la regla ABCD de lunares explicada de forma sencilla."""
    }
]

def main():
    print("=== Generando las 10 Micro-Apps Interactivas Senior (+65) de LOTE 4 ===")
    
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

    print(f"\n¡Éxito! Las 10 Micro-Apps de Lote 4 han sido generadas y sincronizadas con éxito.")

if __name__ == "__main__":
    main()

