#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_cod_lote4_htmls.py
Genera los 10 Simuladores 3D Oficiales del LOTE 4 [COD] (Sesiones 31 a 40)
con el estándar de oro de Babylon.js + Pipeline PBR + Datos Científicos Reales (Base64).
Guarda los archivos en:
  1. SIMULADORES_INTERACTIVOS/01_SIMULADORES/
  2. CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/XX_Sesion/
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
SIM_DIR = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "01_SIMULADORES")
SESSIONS_ROOT = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")

os.makedirs(SIM_DIR, exist_ok=True)

# Helper para plantilla común HTML5 + Babylon.js
def build_html_template(
    sesion_num,
    code_id,
    sim_title,
    sim_subtitle,
    source_badge,
    b64_filename,
    b64_varname,
    accent_color,
    accent_rgb,
    sliders_html,
    actions_html,
    kpis_html,
    chart_title,
    chart_unit,
    speech_intro,
    custom_babylon_setup_js,
    custom_render_loop_js,
    custom_chart_update_js
):
    sesion_str = f"{sesion_num:02d}"
    
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesión {sesion_str} • {sim_title} 3D [{code_id}]</title>
    <!-- Babylon.js CDN Oficial -->
    <script src="https://cdn.babylonjs.com/babylon.js"></script>
    <script src="https://cdn.babylonjs.com/loaders/babylonjs.loaders.min.js"></script>
    <!-- Modelo Científico en Base64 (Multi-Fallback) -->
    <script src="{b64_filename}"></script>
    <script src="../../../../SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/{b64_filename}"></script>
    <script src="../03_ASSETS_3D_Y_DATOS/{b64_filename}"></script>
    <script src="https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/{b64_filename}"></script>

    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #060913;
            --bg-panel: rgba(15, 23, 42, 0.92);
            --border: rgba(255, 255, 255, 0.12);
            --accent: {accent_color};
            --accent-glow: rgba({accent_rgb}, 0.35);
            --text-main: #f8fafc;
            --text-sub: #cbd5e1;
            --text-muted: #94a3b8;
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --font-mono: 'JetBrains Mono', ui-monospace, monospace;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            user-select: none;
        }}

        body {{
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-sans);
            width: 100vw;
            height: 100vh;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}

        /* 3D VIEWPORT */
        #renderCanvas {{
            width: 100%;
            height: 100%;
            touch-action: none;
            outline: none;
            display: block;
        }}

        /* HEADER HUD */
        header {{
            position: absolute;
            top: 18px;
            left: 20px;
            right: 20px;
            z-index: 20;
            display: flex;
            justify-content: space-between;
            align-items: center;
            pointer-events: none;
        }}

        .brand-card {{
            background: var(--bg-panel);
            backdrop-filter: blur(14px);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 12px 20px;
            display: flex;
            align-items: center;
            gap: 14px;
            box-shadow: 0 14px 35px rgba(0,0,0,0.6);
            pointer-events: auto;
        }}

        .brand-badge {{
            background: var(--accent-glow);
            border: 1px solid var(--accent);
            color: var(--accent);
            font-family: var(--font-mono);
            font-weight: 800;
            font-size: 0.85rem;
            padding: 5px 10px;
            border-radius: 8px;
            letter-spacing: 0.05em;
        }}

        .brand-title {{
            font-size: 1.15rem;
            font-weight: 800;
            letter-spacing: -0.01em;
            color: #ffffff;
        }}

        .brand-sub {{
            font-size: 0.76rem;
            color: var(--text-muted);
            margin-top: 2px;
        }}

        .header-actions {{
            display: flex;
            gap: 10px;
            pointer-events: auto;
        }}

        .btn-header {{
            background: var(--bg-panel);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            color: var(--text-sub);
            padding: 9px 14px;
            border-radius: 10px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.4);
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .btn-header:hover {{
            background: rgba(30, 41, 59, 0.95);
            border-color: var(--accent);
            color: #ffffff;
            transform: translateY(-1px);
        }}

        .btn-header.active {{
            background: var(--accent-glow);
            border-color: var(--accent);
            color: var(--accent);
        }}

        /* FLOATING SIDEBAR (CONTROLS) */
        .sidebar-left {{
            position: absolute;
            top: 86px;
            left: 20px;
            width: 320px;
            max-height: calc(100vh - 106px);
            background: var(--bg-panel);
            backdrop-filter: blur(16px);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            gap: 14px;
            z-index: 20;
            overflow-y: auto;
            box-shadow: 0 16px 40px rgba(0,0,0,0.6);
        }}

        .sidebar-left::-webkit-scrollbar {{
            width: 4px;
        }}
        .sidebar-left::-webkit-scrollbar-thumb {{
            background: rgba(255,255,255,0.2);
            border-radius: 4px;
        }}

        .panel-sec-title {{
            font-size: 0.78rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--accent);
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            padding-bottom: 6px;
            margin-top: 4px;
        }}

        .slider-wrap {{
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}

        .slider-head {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--text-sub);
        }}

        .slider-val {{
            font-family: var(--font-mono);
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--accent);
            background: rgba(255,255,255,0.06);
            padding: 2px 7px;
            border-radius: 6px;
        }}

        input[type="range"] {{
            width: 100%;
            height: 6px;
            border-radius: 4px;
            background: rgba(255, 255, 255, 0.15);
            outline: none;
            -webkit-appearance: none;
            accent-color: var(--accent);
            cursor: pointer;
        }}

        .btn-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
        }}

        .btn-action {{
            background: rgba(30, 41, 59, 0.8);
            border: 1px solid rgba(255,255,255,0.12);
            color: #e2e8f0;
            font-size: 0.78rem;
            font-weight: 700;
            padding: 8px 10px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.15s ease;
            text-align: center;
        }}

        .btn-action:hover {{
            background: rgba(51, 65, 85, 0.9);
            border-color: var(--accent);
            color: #ffffff;
        }}

        .btn-action.active {{
            background: var(--accent);
            border-color: var(--accent);
            color: #060913;
            box-shadow: 0 0 14px var(--accent-glow);
        }}

        /* BOTTOM TELEMETRY DOCK */
        .telemetry-dock {{
            position: absolute;
            bottom: 20px;
            left: 360px;
            right: 20px;
            height: 90px;
            background: var(--bg-panel);
            backdrop-filter: blur(14px);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 10px 22px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
            z-index: 20;
            box-shadow: 0 14px 35px rgba(0,0,0,0.6);
        }}

        .kpi-group {{
            display: flex;
            gap: 24px;
            align-items: center;
        }}

        .kpi-card {{
            display: flex;
            flex-direction: column;
            gap: 3px;
        }}

        .kpi-label {{
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-muted);
        }}

        .kpi-value {{
            font-family: var(--font-mono);
            font-size: 1.1rem;
            font-weight: 800;
            color: #ffffff;
        }}

        .kpi-pill {{
            display: inline-block;
            font-size: 0.7rem;
            font-weight: 800;
            padding: 2px 8px;
            border-radius: 9999px;
            margin-top: 2px;
        }}
        .pill-healthy {{ background: rgba(16, 185, 129, 0.2); color: #6ee7b7; border: 1px solid #10b981; }}
        .pill-warn {{ background: rgba(251, 191, 36, 0.2); color: #fde68a; border: 1px solid #fbbf24; }}
        .pill-danger {{ background: rgba(244, 63, 94, 0.2); color: #fda4af; border: 1px solid #f43f5e; }}

        .chart-box {{
            flex: 1;
            max-width: 320px;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}

        .chart-head {{
            display: flex;
            justify-content: space-between;
            font-size: 0.72rem;
            font-weight: 700;
            color: var(--accent);
            text-transform: uppercase;
        }}

        #dockCanvas {{
            width: 100%;
            height: 48px;
            background: rgba(0,0,0,0.3);
            border-radius: 6px;
            border: 1px solid rgba(255,255,255,0.08);
        }}

        /* LOADING SPINNER */
        #loadingOverlay {{
            position: absolute;
            inset: 0;
            background: var(--bg-base);
            z-index: 100;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 16px;
            transition: opacity 0.5s ease;
        }}

        .spinner {{
            width: 48px;
            height: 48px;
            border: 4px solid rgba(255,255,255,0.1);
            border-top-color: var(--accent);
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
        }}
        @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    </style>
</head>
<body>

    <div id="loadingOverlay">
        <div class="spinner"></div>
        <div style="font-weight:700; color:var(--text-sub); font-size:0.95rem;">Cargando Laboratorio 3D • {sim_title}...</div>
        <div style="font-size:0.75rem; color:var(--text-muted);">{source_badge}</div>
    </div>

    <header>
        <div class="brand-card">
            <span class="brand-badge">{code_id}</span>
            <div>
                <div class="brand-title">{sim_title} 3D</div>
                <div class="brand-sub">{sim_subtitle} • {source_badge}</div>
            </div>
        </div>
        <div class="header-actions">
            <button class="btn-header" id="btnAudio">🔊 Audio: ON</button>
            <button class="btn-header" id="btnVoice">🗣️ Guía por Voz</button>
            <button class="btn-header" id="btnRotate">🔄 Giro: ON</button>
            <button class="btn-header" id="btnReset">🎯 Centrar</button>
        </div>
    </header>

    <aside class="sidebar-left">
        {sliders_html}
        {actions_html}
    </aside>

    <div class="telemetry-dock">
        <div class="kpi-group">
            {kpis_html}
        </div>
        <div class="chart-box">
            <div class="chart-head">
                <span>{chart_title}</span>
                <span id="chartLiveVal">{chart_unit}</span>
            </div>
            <canvas id="dockCanvas" width="300" height="48"></canvas>
        </div>
    </div>

    <canvas id="renderCanvas"></canvas>

    <script>
        // WEB AUDIO PROCEDURAL SINTETIZADO (CERO DEPENDENCIAS EXTERNAS)
        let audioCtx = null;
        let isAudioPlaying = true;
        function initAudio() {{
            try {{
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
            }} catch(e) {{}}
        }}

        function playSciPing(freq = 440, duration = 0.25, type = 'sine') {{
            if (!isAudioPlaying) return;
            initAudio();
            if (!audioCtx) return;
            try {{
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.04, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + duration);
            }} catch(e) {{}}
        }}

        // SÍNTESIS DE VOZ PEDAGÓGICA EN ESPAÑOL
        function speakNarrative(text) {{
            if ('speechSynthesis' in window) {{
                window.speechSynthesis.cancel();
                const u = new SpeechSynthesisUtterance(text);
                u.lang = 'es-ES';
                u.rate = 1.02;
                window.speechSynthesis.speak(u);
            }}
        }}

        // BOTONES DE CABECERA
        document.getElementById('btnAudio').addEventListener('click', function() {{
            isAudioPlaying = !isAudioPlaying;
            this.innerText = isAudioPlaying ? '🔊 Audio: ON' : '🔇 Audio: OFF';
            this.classList.toggle('active', isAudioPlaying);
        }});

        document.getElementById('btnVoice').addEventListener('click', function() {{
            speakNarrative("{speech_intro}");
        }});

        // INICIALIZACIÓN DE BABYLON.JS
        const canvas = document.getElementById("renderCanvas");
        const engine = new BABYLON.Engine(canvas, true, {{ preserveDrawingBuffer: true, stencil: true }});
        let autoRotate = true;
        let modelMeshRoot = null;
        let isModelLoaded = false;
        let fixedBaseScale = 1.0;

        const createScene = function() {{
            const scene = new BABYLON.Scene(engine);
            scene.clearColor = new BABYLON.Color4(0.024, 0.035, 0.067, 1.0); // #060913

            // CÁMARA ORBITAL MÉDICO-CIENTÍFICA
            const camera = new BABYLON.ArcRotateCamera("Camera", -Math.PI / 2, Math.PI / 2.5, 6.0, new BABYLON.Vector3(0, 0, 0), scene);
            camera.attachControl(canvas, true);
            camera.wheelPrecision = 45;
            camera.lowerRadiusLimit = 2.2;
            camera.upperRadiusLimit = 16.0;

            // ILUMINACIÓN CLÍNICA PBR
            const hemiLight = new BABYLON.HemisphericLight("hemiLight", new BABYLON.Vector3(0, 1, 0), scene);
            hemiLight.intensity = 0.85;
            hemiLight.diffuse = new BABYLON.Color3(0.9, 0.95, 1.0);
            hemiLight.groundColor = new BABYLON.Color3(0.1, 0.15, 0.25);

            const keyLight = new BABYLON.DirectionalLight("keyLight", new BABYLON.Vector3(-1, -2, 1), scene);
            keyLight.position = new BABYLON.Vector3(5, 8, -5);
            keyLight.intensity = 1.2;

            const fillLight = new BABYLON.PointLight("fillLight", new BABYLON.Vector3(-5, -2, -4), scene);
            fillLight.diffuse = new BABYLON.Color3({accent_rgb});
            fillLight.intensity = 0.8;

            const glow = new BABYLON.GlowLayer("glow", scene);
            glow.intensity = 0.35;

            // CARGA ROBUSTA MULTI-RUTA (Base64 -> Local -> CDN)
            const candidateSources = [
                (window.{b64_varname} && window.{b64_varname}.length > 500) ? window.{b64_varname} : null,
                "{b64_filename}",
                "../../../../SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/{b64_filename}",
                "../03_ASSETS_3D_Y_DATOS/{b64_filename}",
                "https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/{b64_filename}"
            ].filter(Boolean);

            let currentSrcIdx = 0;
            function loadScientificMesh() {{
                if (currentSrcIdx >= candidateSources.length) {{
                    document.getElementById("loadingOverlay").innerHTML = '<div style="color:#ef4444;font-weight:700;">Simulación activa con modelo procedural</div>';
                    setTimeout(() => {{
                        document.getElementById("loadingOverlay").style.opacity = "0";
                        setTimeout(() => document.getElementById("loadingOverlay").style.display = "none", 400);
                    }}, 600);
                    return;
                }}
                const source = candidateSources[currentSrcIdx];
                BABYLON.SceneLoader.ImportMesh("", "", source, scene, function(meshes) {{
                    const overlay = document.getElementById("loadingOverlay");
                    overlay.style.opacity = "0";
                    setTimeout(() => overlay.style.display = "none", 400);

                    modelMeshRoot = new BABYLON.TransformNode("modelRoot", scene);
                    meshes.forEach(m => {{
                        if (m.parent === null) {{
                            m.parent = modelMeshRoot;
                        }}
                    }});

                    const hierarchy = modelMeshRoot.getHierarchyBoundingVectors();
                    const center = hierarchy.max.add(hierarchy.min).scale(0.5);
                    const size = hierarchy.max.subtract(hierarchy.min);
                    const maxDim = Math.max(size.x, size.y, size.z);

                    if (maxDim > 0) {{
                        fixedBaseScale = 2.8 / maxDim;
                        modelMeshRoot.scaling = new BABYLON.Vector3(fixedBaseScale, fixedBaseScale, fixedBaseScale);
                        modelMeshRoot.position = center.scale(-fixedBaseScale);
                    }}
                    camera.target = new BABYLON.Vector3(0, 0, 0);
                    isModelLoaded = true;
                }}, null, function(scene, msg) {{
                    console.warn("Fallo fuente:", source, msg);
                    currentSrcIdx++;
                    loadScientificMesh();
                }}, ".glb");
            }}
            loadScientificMesh();

            // SETUP ESPECÍFICO ADICIONAL
            {custom_babylon_setup_js}

            document.getElementById('btnReset').addEventListener('click', function() {{
                camera.radius = 6.0;
                camera.alpha = -Math.PI / 2;
                camera.beta = Math.PI / 2.5;
                camera.target = new BABYLON.Vector3(0, 0, 0);
                playSciPing(600, 0.15);
            }});

            document.getElementById('btnRotate').addEventListener('click', function() {{
                autoRotate = !autoRotate;
                this.innerText = autoRotate ? '🔄 Giro: ON' : '⏸️ Giro: OFF';
                this.classList.toggle('active', autoRotate);
            }});

            return scene;
        }};

        const scene = createScene();

        // RENDER LOOP
        let lastTime = performance.now();
        engine.runRenderLoop(function() {{
            const now = performance.now();
            const dt = (now - lastTime) / 1000;
            lastTime = now;

            if (autoRotate && modelMeshRoot) {{
                modelMeshRoot.rotation.y += 0.0035;
            }}

            {custom_render_loop_js}

            updateDockChart(dt);
            scene.render();
        }});

        window.addEventListener("resize", () => engine.resize());

        // TELEMETRÍA EN TIEMPO REAL (DOCK CANVAS)
        const dockCanvas = document.getElementById("dockCanvas");
        const dCtx = dockCanvas.getContext("2d");
        const chartHistory = [];
        let chartPhase = 0;

        function updateDockChart(dt) {{
            chartPhase += dt;
            {custom_chart_update_js}
        }}
    </script>
</body>
</html>
"""
    return html


# ==============================================================================
# DEFINICIONES DE LAS 10 SIMULACIONES (SESIONES 31 A 40)
# ==============================================================================

def generate_s31_coral():
    sliders = """
        <div class="panel-sec-title"><span>Variables Oceánicas</span><span>NOAA CRW</span></div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Temperatura Marina (SST)</span><span class="slider-val" id="valSST">27.0 °C</span></div>
            <input type="range" id="rngSST" min="24.0" max="33.0" step="0.1" value="27.0">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Acumulación DHW</span><span class="slider-val" id="valDHW">0.0 °C-sem</span></div>
            <input type="range" id="rngDHW" min="0" max="16" step="0.5" value="0">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Acidificación Oceánica (pH)</span><span class="slider-val" id="valPH">8.15 pH</span></div>
            <input type="range" id="rngPH" min="7.60" max="8.30" step="0.01" value="8.15">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Radiación UV</span><span class="slider-val" id="valUV">450 µmol</span></div>
            <input type="range" id="rngUV" min="100" max="1200" step="25" value="450">
        </div>
    """
    actions = """
        <div class="panel-sec-title"><span>Modos Biológicos</span><span>Simbiosis</span></div>
        <div class="btn-grid">
            <button class="btn-action active" id="btnDay">☀️ Modo Día</button>
            <button class="btn-action" id="btnNight">🌙 Noche / Captura</button>
        </div>
        <div class="btn-grid" style="margin-top:8px;">
            <button class="btn-action" id="btnHeatwave" style="border-color:#f43f5e; color:#fda4af;">🔥 Ola de Calor</button>
            <button class="btn-action" id="btnRecover">🌿 Recuperación</button>
        </div>
    """
    kpis = """
        <div class="kpi-card">
            <span class="kpi-label">Densidad Zooxantelas</span>
            <span class="kpi-value" id="kpiZoox">1.48×10⁶</span>
            <span class="kpi-pill pill-healthy" id="pillStatus">Normal / Saludable</span>
        </div>
        <div class="kpi-card">
            <span class="kpi-label">Tasa Calcificación</span>
            <span class="kpi-value" id="kpiCalc">14.2 g/m²</span>
        </div>
    """
    setup_js = """
        // Partículas bioluminiscentes de zooxantelas
        const particleSystem = new BABYLON.ParticleSystem("zooxParticles", 200, scene);
        particleSystem.emitter = new BABYLON.Vector3(0, 0, 0);
        particleSystem.minEmitBox = new BABYLON.Vector3(-1.2, -0.2, -1.2);
        particleSystem.maxEmitBox = new BABYLON.Vector3(1.2, 1.2, 1.2);
        particleSystem.color1 = new BABYLON.Color4(0.1, 0.8, 0.4, 0.8);
        particleSystem.color2 = new BABYLON.Color4(0.2, 0.9, 0.6, 0.2);
        particleSystem.minSize = 0.05;
        particleSystem.maxSize = 0.12;
        particleSystem.minLifeTime = 1.5;
        particleSystem.maxLifeTime = 3.0;
        particleSystem.emitRate = 40;
        particleSystem.start();

        // Sliders Listeners
        document.getElementById('rngSST').addEventListener('input', function(e) {
            document.getElementById('valSST').innerText = parseFloat(e.target.value).toFixed(1) + ' °C';
            playSciPing(320 + e.target.value * 15, 0.08);
        });
        document.getElementById('rngDHW').addEventListener('input', function(e) {
            document.getElementById('valDHW').innerText = parseFloat(e.target.value).toFixed(1) + ' °C-sem';
        });
        document.getElementById('rngPH').addEventListener('input', function(e) {
            document.getElementById('valPH').innerText = parseFloat(e.target.value).toFixed(2) + ' pH';
        });
        document.getElementById('btnHeatwave').addEventListener('click', function() {
            document.getElementById('rngSST').value = 31.8;
            document.getElementById('rngDHW').value = 9.5;
            document.getElementById('valSST').innerText = '31.8 °C';
            document.getElementById('valDHW').innerText = '9.5 °C-sem';
            playSciPing(220, 0.35, 'sawtooth');
        });
        document.getElementById('btnRecover').addEventListener('click', function() {
            document.getElementById('rngSST').value = 27.0;
            document.getElementById('rngDHW').value = 0.0;
            document.getElementById('valSST').innerText = '27.0 °C';
            document.getElementById('valDHW').innerText = '0.0 °C-sem';
            playSciPing(580, 0.2, 'sine');
        });
    """
    render_js = """
        const sst = parseFloat(document.getElementById('rngSST').value);
        const dhw = parseFloat(document.getElementById('rngDHW').value);
        const zoox = Math.max(0.05, 1.48 - (dhw * 0.14)).toFixed(2);
        document.getElementById('kpiZoox').innerText = zoox + '×10⁶';
        
        const pill = document.getElementById('pillStatus');
        if (dhw > 8 || sst > 31) {
            pill.className = 'kpi-pill pill-danger';
            pill.innerText = 'Blanqueamiento Crítico';
        } else if (dhw > 4 || sst > 29.5) {
            pill.className = 'kpi-pill pill-warn';
            pill.innerText = 'Alerta Térmica';
        } else {
            pill.className = 'kpi-pill pill-healthy';
            pill.innerText = 'Saludable / Simbiosis';
        }
    """
    chart_js = """
        const sst = parseFloat(document.getElementById('rngSST').value);
        const v = Math.sin(chartPhase * 4) * 8 + (sst - 24) * 4;
        chartHistory.push(v);
        if (chartHistory.length > 50) chartHistory.shift();

        dCtx.clearRect(0, 0, dockCanvas.width, dockCanvas.height);
        dCtx.strokeStyle = '#38bdf8';
        dCtx.lineWidth = 2;
        dCtx.beginPath();
        chartHistory.forEach((pt, idx) => {
            const x = (idx / 50) * dockCanvas.width;
            const y = dockCanvas.height - (pt / 40) * dockCanvas.height;
            if (idx === 0) dCtx.moveTo(x, y);
            else dCtx.lineTo(x, y);
        });
        dCtx.stroke();
        document.getElementById('chartLiveVal').innerText = sst.toFixed(1) + ' °C';
    """
    return build_html_template(
        31, "[COD-031]", "Arrecife de Coral, Pólipos y Simbiosis Marina",
        "Estructuras de CaCO3 y Dinámica de Zooxantelas", "NOAA Coral Reef Watch",
        "coral_b64.js", "CORAL_GLB_B64", "#38bdf8", "56, 189, 248",
        sliders, actions, kpis, "Curva Térmica NOAA", "27.0 °C",
        "Bienvenido al Laboratorio del Arrecife de Coral 3D. Observa cómo los pólipos cnidarios segregan carbonato de calcio y cómo la acumulación térmica causa la expulsión de las zooxantelas.",
        setup_js, render_js, chart_js
    )


def generate_s32_trophic():
    sliders = """
        <div class="panel-sec-title"><span>Dinámica de Biomasa</span><span>Lindeman 10%</span></div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Biomasa Productores (T1)</span><span class="slider-val" id="valT1">1000 g/m²</span></div>
            <input type="range" id="rngT1" min="200" max="2500" step="50" value="1000">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Eficiencia Ecológica</span><span class="slider-val" id="valEff">10.0 %</span></div>
            <input type="range" id="rngEff" min="5.0" max="20.0" step="0.5" value="10.0">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Caudal Fluvial</span><span class="slider-val" id="valFlow">14.5 m³/s</span></div>
            <input type="range" id="rngFlow" min="2.0" max="40.0" step="1.0" value="14.5">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Nutrientes N/P (Eutrofización)</span><span class="slider-val" id="valNP">0.8 ppm</span></div>
            <input type="range" id="rngNP" min="0.1" max="5.0" step="0.1" value="0.8">
        </div>
    """
    actions = """
        <div class="panel-sec-title"><span>Escenarios Fluviales</span><span>USGS</span></div>
        <div class="btn-grid">
            <button class="btn-action active" id="btnEquil">⚖️ Equilibrio</button>
            <button class="btn-action" id="btnEutro" style="border-color:#fbbf24; color:#fde68a;">🌿 Eutrofización</button>
        </div>
        <div class="btn-grid" style="margin-top:8px;">
            <button class="btn-action" id="btnSpill" style="border-color:#f43f5e; color:#fda4af;">⚠️ Vertido</button>
            <button class="btn-action" id="btnRest">🐟 Repoblación</button>
        </div>
    """
    kpis = """
        <div class="kpi-card">
            <span class="kpi-label">Biomasa Depredador (Trucha)</span>
            <span class="kpi-value" id="kpiApex">1.00 g/m²</span>
            <span class="kpi-pill pill-healthy" id="pillTrophic">Ecosistema Estable</span>
        </div>
        <div class="kpi-card">
            <span class="kpi-label">Disipación Metabólica</span>
            <span class="kpi-value" id="kpiHeat">90.0 %</span>
        </div>
    """
    setup_js = """
        document.getElementById('rngT1').addEventListener('input', (e) => {
            document.getElementById('valT1').innerText = e.target.value + ' g/m²';
            playSciPing(400, 0.05);
        });
        document.getElementById('rngEff').addEventListener('input', (e) => {
            document.getElementById('valEff').innerText = parseFloat(e.target.value).toFixed(1) + ' %';
        });
        document.getElementById('btnEutro').addEventListener('click', () => {
            document.getElementById('rngNP').value = 4.2;
            document.getElementById('valNP').innerText = '4.2 ppm';
            document.getElementById('rngT1').value = 2200;
            document.getElementById('valT1').innerText = '2200 g/m²';
            playSciPing(300, 0.2);
        });
    """
    render_js = """
        const t1 = parseFloat(document.getElementById('rngT1').value);
        const eff = parseFloat(document.getElementById('rngEff').value) / 100;
        const t2 = t1 * eff;
        const t3 = t2 * eff;
        const t4 = t3 * eff;
        document.getElementById('kpiApex').innerText = t4.toFixed(2) + ' g/m²';
        document.getElementById('kpiHeat').innerText = ((1 - eff) * 100).toFixed(1) + ' %';
    """
    chart_js = """
        const eff = parseFloat(document.getElementById('rngEff').value);
        const v = 15 + Math.sin(chartPhase * 3) * 5 + eff;
        chartHistory.push(v);
        if (chartHistory.length > 50) chartHistory.shift();

        dCtx.clearRect(0, 0, dockCanvas.width, dockCanvas.height);
        dCtx.strokeStyle = '#10b981';
        dCtx.lineWidth = 2;
        dCtx.beginPath();
        chartHistory.forEach((pt, idx) => {
            const x = (idx / 50) * dockCanvas.width;
            const y = dockCanvas.height - (pt / 40) * dockCanvas.height;
            if (idx === 0) dCtx.moveTo(x, y);
            else dCtx.lineTo(x, y);
        });
        dCtx.stroke();
        document.getElementById('chartLiveVal').innerText = eff.toFixed(1) + ' % Efic.';
    """
    return build_html_template(
        32, "[COD-032]", "Pirámide Trófica y Red Ecológica Fluvial",
        "Ley del 10% de Lindeman y Disipación Metabólica", "USGS River Ecology",
        "trophic_b64.js", "TROPHIC_GLB_B64", "#10b981", "16, 185, 129",
        sliders, actions, kpis, "Eficiencia Energética", "10.0 %",
        "Bienvenido al Simulador de la Red Trófica Fluvial. Analiza cómo la energía solar fijada por las algas se disipa en un noventa por ciento en cada escalón trófico.",
        setup_js, render_js, chart_js
    )


def generate_s33_mitochondria():
    sliders = """
        <div class="panel-sec-title"><span>Gradiente Quimiosmótico</span><span>Mitchell PMF</span></div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Potencial Membrana (ΔΨ)</span><span class="slider-val" id="valPsi">160 mV</span></div>
            <input type="range" id="rngPsi" min="40" max="220" step="5" value="160">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Gradiente pH (ΔpH)</span><span class="slider-val" id="valDpH">1.00 pH</span></div>
            <input type="range" id="rngDpH" min="0.2" max="1.5" step="0.05" value="1.00">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Concentración ADP + Pi</span><span class="slider-val" id="valADP">2.5 mM</span></div>
            <input type="range" id="rngADP" min="0.2" max="5.0" step="0.1" value="2.5">
        </div>
    """
    actions = """
        <div class="panel-sec-title"><span>Nanomotor ATP Sintasa</span><span>PDB 6J5I</span></div>
        <div class="btn-grid">
            <button class="btn-action active" id="btnBasal">⚡ Tasa Basal</button>
            <button class="btn-action" id="btnBurst">🚀 Demanda ATP</button>
        </div>
        <div class="btn-grid" style="margin-top:8px;">
            <button class="btn-action" id="btnUncouple" style="border-color:#fbbf24; color:#fde68a;">🔥 Desacoplante</button>
            <button class="btn-action" id="btnOligo" style="border-color:#f43f5e; color:#fda4af;">⛔ Oligomicina</button>
        </div>
    """
    kpis = """
        <div class="kpi-card">
            <span class="kpi-label">Rotor F₀ (RPM)</span>
            <span class="kpi-value" id="kpiRPM">9.000</span>
            <span class="kpi-pill pill-healthy" id="pillMito">Quimiosmosis Activa</span>
        </div>
        <div class="kpi-card">
            <span class="kpi-label">Síntesis ATP / seg</span>
            <span class="kpi-value" id="kpiATP">450 moléc/s</span>
        </div>
    """
    setup_js = """
        document.getElementById('rngPsi').addEventListener('input', (e) => {
            document.getElementById('valPsi').innerText = e.target.value + ' mV';
            playSciPing(500, 0.05);
        });
        document.getElementById('rngDpH').addEventListener('input', (e) => {
            document.getElementById('valDpH').innerText = parseFloat(e.target.value).toFixed(2) + ' pH';
        });
        document.getElementById('btnUncouple').addEventListener('click', () => {
            document.getElementById('rngPsi').value = 60;
            document.getElementById('valPsi').innerText = '60 mV';
            playSciPing(260, 0.25, 'triangle');
        });
    """
    render_js = """
        const psi = parseFloat(document.getElementById('rngPsi').value);
        const dpH = parseFloat(document.getElementById('rngDpH').value);
        const pmf = psi + 60 * dpH;
        const rpm = Math.round(pmf * 42);
        document.getElementById('kpiRPM').innerText = rpm.toLocaleString();
        document.getElementById('kpiATP').innerText = Math.round(rpm * 0.05) + ' moléc/s';
    """
    chart_js = """
        const psi = parseFloat(document.getElementById('rngPsi').value);
        const v = 20 + Math.sin(chartPhase * 8) * 8 + (psi - 100) * 0.15;
        chartHistory.push(v);
        if (chartHistory.length > 50) chartHistory.shift();

        dCtx.clearRect(0, 0, dockCanvas.width, dockCanvas.height);
        dCtx.strokeStyle = '#f59e0b';
        dCtx.lineWidth = 2;
        dCtx.beginPath();
        chartHistory.forEach((pt, idx) => {
            const x = (idx / 50) * dockCanvas.width;
            const y = dockCanvas.height - (pt / 40) * dockCanvas.height;
            if (idx === 0) dCtx.moveTo(x, y);
            else dCtx.lineTo(x, y);
        });
        dCtx.stroke();
        document.getElementById('chartLiveVal').innerText = psi + ' mV';
    """
    return build_html_template(
        33, "[COD-033]", "Mitocondria: Central Celular y Nanomotor ATP Sintasa",
        "Rotor F₀F₁ a 9.000 RPM y Fuerza Protón-Motriz", "PDB 6J5I Cryo-EM 2.9Å",
        "mitochondria_b64.js", "MITOCHONDRIA_GLB_B64", "#f59e0b", "245, 158, 11",
        sliders, actions, kpis, "Fuerza Protón-Motriz", "160 mV",
        "Bienvenido a la Mitocondria y su Nanomotor ATP Sintasa. La fuerza protón-motriz empuja protones por el rotor efe cero, haciéndolo girar a nueve mil revoluciones por minuto para fabricar ATP.",
        setup_js, render_js, chart_js
    )


def generate_s34_telomeres():
    sliders = """
        <div class="panel-sec-title"><span>Reloj Mitótico</span><span>Hayflick</span></div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Divisiones Mitóticas</span><span class="slider-val" id="valDiv">15</span></div>
            <input type="range" id="rngDiv" min="0" max="70" step="1" value="15">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Expresión Telomerasa (hTERT)</span><span class="slider-val" id="valTERT">0 %</span></div>
            <input type="range" id="rngTERT" min="0" max="100" step="5" value="0">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Estrés Oxidativo</span><span class="slider-val" id="valOx">Bajo</span></div>
            <input type="range" id="rngOx" min="1" max="5" step="1" value="1">
        </div>
    """
    actions = """
        <div class="panel-sec-title"><span>Fisiología Replicativa</span><span>Blackburn</span></div>
        <div class="btn-grid">
            <button class="btn-action" id="btnMitosis">🔬 +1 Mitosis</button>
            <button class="btn-action" id="btnTelomerase">🌟 Telomerasa ON</button>
        </div>
        <div class="btn-grid" style="margin-top:8px;">
            <button class="btn-action" id="btnHayflick" style="border-color:#fbbf24; color:#fde68a;">⏳ Límite Hayflick</button>
            <button class="btn-action" id="btnResetCell">🔄 Célula Inicial</button>
        </div>
    """
    kpis = """
        <div class="kpi-card">
            <span class="kpi-label">Longitud Telómeros</span>
            <span class="kpi-value" id="kpiKb">12.5 kb</span>
            <span class="kpi-pill pill-healthy" id="pillTelo">Proliferativa</span>
        </div>
        <div class="kpi-card">
            <span class="kpi-label">Capacidad Replicativa</span>
            <span class="kpi-value" id="kpiCap">35 ciclos</span>
        </div>
    """
    setup_js = """
        document.getElementById('btnMitosis').addEventListener('click', () => {
            const rng = document.getElementById('rngDiv');
            if (parseInt(rng.value) < 70) {
                rng.value = parseInt(rng.value) + 1;
                document.getElementById('valDiv').innerText = rng.value;
                playSciPing(650, 0.08);
            }
        });
        document.getElementById('btnTelomerase').addEventListener('click', () => {
            document.getElementById('rngTERT').value = 85;
            document.getElementById('valTERT').innerText = '85 %';
            playSciPing(880, 0.15);
        });
    """
    render_js = """
        const div = parseInt(document.getElementById('rngDiv').value);
        const tert = parseInt(document.getElementById('rngTERT').value);
        const kb = Math.max(1.8, 15.0 - (div * 0.18) + (tert * 0.04)).toFixed(1);
        document.getElementById('kpiKb').innerText = kb + ' kb';
        const rem = Math.max(0, 50 - div);
        document.getElementById('kpiCap').innerText = rem + ' ciclos';

        const pill = document.getElementById('pillTelo');
        if (div >= 50 && tert < 20) {
            pill.className = 'kpi-pill pill-danger';
            pill.innerText = 'Senescencia / Límite Hayflick';
        } else if (div > 35) {
            pill.className = 'kpi-pill pill-warn';
            pill.innerText = 'Acortamiento Crítico';
        } else {
            pill.className = 'kpi-pill pill-healthy';
            pill.innerText = 'Célula Proliferativa';
        }
    """
    chart_js = """
        const div = parseInt(document.getElementById('rngDiv').value);
        const v = Math.max(2, 38 - div * 0.5);
        chartHistory.push(v);
        if (chartHistory.length > 50) chartHistory.shift();

        dCtx.clearRect(0, 0, dockCanvas.width, dockCanvas.height);
        dCtx.strokeStyle = '#c084fc';
        dCtx.lineWidth = 2;
        dCtx.beginPath();
        chartHistory.forEach((pt, idx) => {
            const x = (idx / 50) * dockCanvas.width;
            const y = dockCanvas.height - (pt / 40) * dockCanvas.height;
            if (idx === 0) dCtx.moveTo(x, y);
            else dCtx.lineTo(x, y);
        });
        dCtx.stroke();
        document.getElementById('chartLiveVal').innerText = div + ' divisiones';
    """
    return build_html_template(
        34, "[COD-034]", "Telómeros Cromosómicos, Telomerasa y Límite de Hayflick",
        "Complejo Shelterin y Envejecimiento Replicativo", "PDB 6D6V Blackburn & Greider",
        "telomeres_b64.js", "TELOMERES_GLB_B64", "#c084fc", "192, 132, 252",
        sliders, actions, kpis, "Curva de Acortamiento", "15 div",
        "Bienvenido al Laboratorio Cromosómico de los Telómeros. En cada división celular, los extremos cromosómicos se acortan hasta topar con el límite de Hayflick.",
        setup_js, render_js, chart_js
    )


def generate_s35_rainforest():
    sliders = """
        <div class="panel-sec-title"><span>Perfil de Altura</span><span>50 Metros</span></div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Cota de Altura (Z)</span><span class="slider-val" id="valZ">25 m (Dosel)</span></div>
            <input type="range" id="rngZ" min="0" max="50" step="1" value="25">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Radiación Solar Incidente</span><span class="slider-val" id="valSun">1600 µmol</span></div>
            <input type="range" id="rngSun" min="200" max="2200" step="50" value="1600">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Humedad Relativa</span><span class="slider-val" id="valHum">88 %</span></div>
            <input type="range" id="rngHum" min="50" max="100" step="1" value="88">
        </div>
    """
    actions = """
        <div class="panel-sec-title"><span>Estratos Biológicos</span><span>STRI</span></div>
        <div class="btn-grid">
            <button class="btn-action" id="btnFloor">🍂 Suelo (1% Luz)</button>
            <button class="btn-action active" id="btnCanopy">🌿 Dosel (80% Bio)</button>
        </div>
        <div class="btn-grid" style="margin-top:8px;">
            <button class="btn-action" id="btnEmergent">🌲 Emergente (50m)</button>
            <button class="btn-action" id="btnRain">🌧️ Río Volador</button>
        </div>
    """
    kpis = """
        <div class="kpi-card">
            <span class="kpi-label">Luz PAR en Estrato</span>
            <span class="kpi-value" id="kpiPAR">65 %</span>
            <span class="kpi-pill pill-healthy" id="pillRain">Estrato Canopy</span>
        </div>
        <div class="kpi-card">
            <span class="kpi-label">Evapotranspiración</span>
            <span class="kpi-value" id="kpiTrans">1.200 L/árbol/día</span>
        </div>
    """
    setup_js = """
        document.getElementById('rngZ').addEventListener('input', (e) => {
            const z = parseInt(e.target.value);
            let name = 'Suelo';
            if (z > 40) name = 'Emergente';
            else if (z > 20) name = 'Dosel (Canopy)';
            else if (z > 5) name = 'Sotobosque';
            document.getElementById('valZ').innerText = z + ' m (' + name + ')';
            playSciPing(300 + z * 10, 0.05);
        });
        document.getElementById('btnFloor').addEventListener('click', () => {
            document.getElementById('rngZ').value = 1;
            document.getElementById('valZ').innerText = '1 m (Suelo)';
        });
        document.getElementById('btnEmergent').addEventListener('click', () => {
            document.getElementById('rngZ').value = 48;
            document.getElementById('valZ').innerText = '48 m (Emergente)';
        });
    """
    render_js = """
        const z = parseInt(document.getElementById('rngZ').value);
        const par = Math.min(100, Math.round(Math.pow(z / 50, 1.8) * 100));
        document.getElementById('kpiPAR').innerText = par + ' %';
    """
    chart_js = """
        const z = parseInt(document.getElementById('rngZ').value);
        const v = Math.pow(z / 50, 1.8) * 35;
        chartHistory.push(v);
        if (chartHistory.length > 50) chartHistory.shift();

        dCtx.clearRect(0, 0, dockCanvas.width, dockCanvas.height);
        dCtx.strokeStyle = '#22c55e';
        dCtx.lineWidth = 2;
        dCtx.beginPath();
        chartHistory.forEach((pt, idx) => {
            const x = (idx / 50) * dockCanvas.width;
            const y = dockCanvas.height - (pt / 40) * dockCanvas.height;
            if (idx === 0) dCtx.moveTo(x, y);
            else dCtx.lineTo(x, y);
        });
        dCtx.stroke();
        document.getElementById('chartLiveVal').innerText = z + ' m';
    """
    return build_html_template(
        35, "[COD-035]", "Bioma de Selva Tropical: Estratos y Microclimas",
        "Árbol Gigante Ceiba pentandra y Ríos Voladores", "Smithsonian Tropical Research Institute",
        "rainforest_b64.js", "RAINFOREST_GLB_B64", "#22c55e", "34, 197, 94",
        sliders, actions, kpis, "Perfil de Luz PAR", "25 m",
        "Bienvenido a los Estratos de la Selva Tropical. Descubre cómo la luz solar se extingue del cien por ciento en las copas emergentes a menos del uno por ciento en el suelo sombrío.",
        setup_js, render_js, chart_js
    )


def generate_s36_ionchannel():
    sliders = """
        <div class="panel-sec-title"><span>Potencial y Neurotoxina</span><span>Hodgkin-Huxley</span></div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Potencial de Membrana (Vm)</span><span class="slider-val" id="valVm">-70 mV</span></div>
            <input type="range" id="rngVm" min="-90" max="40" step="2" value="-70">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Concentración TTX</span><span class="slider-val" id="valTTX">0 nM</span></div>
            <input type="range" id="rngTTX" min="0" max="100" step="5" value="0">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Gradiente [Na⁺] Extracelular</span><span class="slider-val" id="valNa">145 mM</span></div>
            <input type="range" id="rngNa" min="50" max="160" step="5" value="145">
        </div>
    """
    actions = """
        <div class="panel-sec-title"><span>Canal Nav1.7</span><span>PDB 6A95</span></div>
        <div class="btn-grid">
            <button class="btn-action" id="btnSpike">⚡ Disparo Espiga</button>
            <button class="btn-action" id="btnBlockTTX" style="border-color:#f43f5e; color:#fda4af;">🐡 Inyectar TTX</button>
        </div>
        <div class="btn-grid" style="margin-top:8px;">
            <button class="btn-action" id="btnWashout">💧 Lavado TTX</button>
            <button class="btn-action active" id="btnRestVm">⏸️ Reposo -70mV</button>
        </div>
    """
    kpis = """
        <div class="kpi-card">
            <span class="kpi-label">Corriente de Sodio (I_Na)</span>
            <span class="kpi-value" id="kpiINa">0.0 pA</span>
            <span class="kpi-pill pill-healthy" id="pillNav">Canal en Reposo</span>
        </div>
        <div class="kpi-card">
            <span class="kpi-label">Apertura Poro DEKA</span>
            <span class="kpi-value" id="kpiPo">0.02 Po</span>
        </div>
    """
    setup_js = """
        document.getElementById('btnSpike').addEventListener('click', () => {
            document.getElementById('rngVm').value = 30;
            document.getElementById('valVm').innerText = '+30 mV';
            playSciPing(850, 0.06, 'sawtooth');
            setTimeout(() => {
                document.getElementById('rngVm').value = -70;
                document.getElementById('valVm').innerText = '-70 mV';
            }, 300);
        });
        document.getElementById('btnBlockTTX').addEventListener('click', () => {
            document.getElementById('rngTTX').value = 80;
            document.getElementById('valTTX').innerText = '80 nM';
            playSciPing(220, 0.3, 'square');
        });
        document.getElementById('btnWashout').addEventListener('click', () => {
            document.getElementById('rngTTX').value = 0;
            document.getElementById('valTTX').innerText = '0 nM';
            playSciPing(600, 0.15);
        });
    """
    render_js = """
        const vm = parseFloat(document.getElementById('rngVm').value);
        const ttx = parseFloat(document.getElementById('rngTTX').value);
        const openProb = vm > -40 ? Math.max(0, (1 - ttx / 100) * 0.95) : 0.02;
        const ina = (openProb * (vm - 55) * -1.2).toFixed(1);
        document.getElementById('kpiINa').innerText = (ttx > 60 ? '0.0' : ina) + ' pA';
        document.getElementById('kpiPo').innerText = openProb.toFixed(2) + ' Po';

        const pill = document.getElementById('pillNav');
        if (ttx > 50) {
            pill.className = 'kpi-pill pill-danger';
            pill.innerText = 'Poro Bloqueado por TTX';
        } else if (vm > -40) {
            pill.className = 'kpi-pill pill-warn';
            pill.innerText = 'Despolarización / Influx Na⁺';
        } else {
            pill.className = 'kpi-pill pill-healthy';
            pill.innerText = 'Reposo (-70 mV)';
        }
    """
    chart_js = """
        const vm = parseFloat(document.getElementById('rngVm').value);
        const ttx = parseFloat(document.getElementById('rngTTX').value);
        const v = ttx > 50 ? 5 : (vm > -40 ? 35 : 8);
        chartHistory.push(v);
        if (chartHistory.length > 50) chartHistory.shift();

        dCtx.clearRect(0, 0, dockCanvas.width, dockCanvas.height);
        dCtx.strokeStyle = '#38bdf8';
        dCtx.lineWidth = 2;
        dCtx.beginPath();
        chartHistory.forEach((pt, idx) => {
            const x = (idx / 50) * dockCanvas.width;
            const y = dockCanvas.height - (pt / 40) * dockCanvas.height;
            if (idx === 0) dCtx.moveTo(x, y);
            else dCtx.lineTo(x, y);
        });
        dCtx.stroke();
        document.getElementById('chartLiveVal').innerText = vm + ' mV';
    """
    return build_html_template(
        36, "[COD-036]", "Neurotoxina y Bloqueo de Canales Iónicos de Sodio",
        "Sensor S4, Filtro DEKA y Tetrodotoxina (TTX)", "PDB 6A95 Cryo-EM 3.2Å",
        "ionchannel_b64.js", "IONCHANNEL_GLB_B64", "#38bdf8", "56, 189, 248",
        sliders, actions, kpis, "Registro Patch-Clamp", "-70 mV",
        "Bienvenido al Canal de Sodio Nav1.7. Observa cómo el sensor de voltaje S4 activa la entrada de sodio y cómo la neurotoxina tetrodotoxina del pez globo tapona físicamente el filtro DEKA.",
        setup_js, render_js, chart_js
    )


def generate_s37_skin():
    sliders = """
        <div class="panel-sec-title"><span>Ambiente y Termorregulación</span><span>Cutánea</span></div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Temperatura Ambiental</span><span class="slider-val" id="valTemp">22.0 °C</span></div>
            <input type="range" id="rngTemp" min="-10" max="45" step="1" value="22">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Índice UV Solar</span><span class="slider-val" id="valUVI">3 UVI</span></div>
            <input type="range" id="rngUVI" min="0" max="12" step="1" value="3">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Actividad Física (W)</span><span class="slider-val" id="valMet">100 W</span></div>
            <input type="range" id="rngMet" min="70" max="800" step="10" value="100">
        </div>
    """
    actions = """
        <div class="panel-sec-title"><span>Respuestas Fisiológicas</span><span>Capas 3D</span></div>
        <div class="btn-grid">
            <button class="btn-action" id="btnVasodil">🔥 Vasodilatación</button>
            <button class="btn-action" id="btnVasocon">❄️ Vasoconstricción</button>
        </div>
        <div class="btn-grid" style="margin-top:8px;">
            <button class="btn-action" id="btnGoosebumps">🦔 Piel de Gallina</button>
            <button class="btn-action" id="btnSweat">💦 Sudoración Ecrina</button>
        </div>
    """
    kpis = """
        <div class="kpi-card">
            <span class="kpi-label">Temp Cutánea</span>
            <span class="kpi-value" id="kpiSkin">33.5 °C</span>
            <span class="kpi-pill pill-healthy" id="pillSkin">Homeostasia 37°C</span>
        </div>
        <div class="kpi-card">
            <span class="kpi-label">Tasa Sudor</span>
            <span class="kpi-value" id="kpiSweat">0.15 L/h</span>
        </div>
    """
    setup_js = """
        document.getElementById('btnVasodil').addEventListener('click', () => {
            document.getElementById('rngTemp').value = 38;
            document.getElementById('valTemp').innerText = '38.0 °C';
            playSciPing(440, 0.1);
        });
        document.getElementById('btnVasocon').addEventListener('click', () => {
            document.getElementById('rngTemp').value = 0;
            document.getElementById('valTemp').innerText = '0.0 °C';
            playSciPing(280, 0.1);
        });
    """
    render_js = """
        const t = parseFloat(document.getElementById('rngTemp').value);
        const skinT = (32.0 + (t - 20) * 0.18).toFixed(1);
        document.getElementById('kpiSkin').innerText = skinT + ' °C';
        const sweat = t > 28 ? ((t - 28) * 0.08).toFixed(2) : '0.05';
        document.getElementById('kpiSweat').innerText = sweat + ' L/h';
    """
    chart_js = """
        const t = parseFloat(document.getElementById('rngTemp').value);
        const v = 15 + (t / 45) * 20;
        chartHistory.push(v);
        if (chartHistory.length > 50) chartHistory.shift();

        dCtx.clearRect(0, 0, dockCanvas.width, dockCanvas.height);
        dCtx.strokeStyle = '#f43f5e';
        dCtx.lineWidth = 2;
        dCtx.beginPath();
        chartHistory.forEach((pt, idx) => {
            const x = (idx / 50) * dockCanvas.width;
            const y = dockCanvas.height - (pt / 40) * dockCanvas.height;
            if (idx === 0) dCtx.moveTo(x, y);
            else dCtx.lineTo(x, y);
        });
        dCtx.stroke();
        document.getElementById('chartLiveVal').innerText = t + ' °C Amb.';
    """
    return build_html_template(
        37, "[COD-037]", "Piel Humana, Capas Tisulares y Termorregulación",
        "Epidermis, Dermis, Vasomotilidad y Reflejo Pilomotor", "NIH Visible Human Project",
        "skin_b64.js", "SKIN_GLB_B64", "#f43f5e", "244, 63, 94",
        sliders, actions, kpis, "Termografía Cutánea", "22 °C",
        "Bienvenido a la Piel Humana 3D. Explora las tres capas histológicas, la irrigación capilar y cómo el músculo erector del pelo genera la piel de gallina ante el frío.",
        setup_js, render_js, chart_js
    )


def generate_s38_spine():
    sliders = """
        <div class="panel-sec-title"><span>Biomecánica Ergonómica</span><span>Chaffin L4-L5</span></div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Carga Levantada</span><span class="slider-val" id="valLoad">15 kg</span></div>
            <input type="range" id="rngLoad" min="0" max="50" step="5" value="15">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Flexión de Espalda</span><span class="slider-val" id="valFlex">30 °</span></div>
            <input type="range" id="rngFlex" min="0" max="90" step="5" value="30">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Distancia de Carga</span><span class="slider-val" id="valDist">25 cm</span></div>
            <input type="range" id="rngDist" min="15" max="65" step="5" value="25">
        </div>
    """
    actions = """
        <div class="panel-sec-title"><span>Técnica de Carga</span><span>NIOSH</span></div>
        <div class="btn-grid">
            <button class="btn-action active" id="btnSafe">🛡️ Espalda Recta</button>
            <button class="btn-action" id="btnDanger" style="border-color:#f43f5e; color:#fda4af;">⚠️ Flexión 90°</button>
        </div>
        <div class="btn-grid" style="margin-top:8px;">
            <button class="btn-action" id="btnHernia">💥 Simular Hernia</button>
            <button class="btn-action" id="btnDecompress">🧘 Descompresión</button>
        </div>
    """
    kpis = """
        <div class="kpi-card">
            <span class="kpi-label">Compresión L4-L5</span>
            <span class="kpi-value" id="kpiComp">2.450 N</span>
            <span class="kpi-pill pill-healthy" id="pillSpine">Bajo Límite NIOSH</span>
        </div>
        <div class="kpi-card">
            <span class="kpi-label">Presión Intradiscal</span>
            <span class="kpi-value" id="kpiMPa">1.25 MPa</span>
        </div>
    """
    setup_js = """
        document.getElementById('btnSafe').addEventListener('click', () => {
            document.getElementById('rngFlex').value = 10;
            document.getElementById('valFlex').innerText = '10 °';
            document.getElementById('rngDist').value = 20;
            playSciPing(520, 0.1);
        });
        document.getElementById('btnDanger').addEventListener('click', () => {
            document.getElementById('rngFlex').value = 90;
            document.getElementById('valFlex').innerText = '90 °';
            document.getElementById('rngDist').value = 55;
            playSciPing(180, 0.35, 'sawtooth');
        });
    """
    render_js = """
        const load = parseFloat(document.getElementById('rngLoad').value);
        const flex = parseFloat(document.getElementById('rngFlex').value);
        const dist = parseFloat(document.getElementById('rngDist').value);
        // Ecuación de momento lumbar Chaffin
        const compN = Math.round(750 + load * 9.8 * (dist / 10) + flex * 35);
        document.getElementById('kpiComp').innerText = compN.toLocaleString() + ' N';
        document.getElementById('kpiMPa').innerText = (compN / 1800).toFixed(2) + ' MPa';

        const pill = document.getElementById('pillSpine');
        if (compN > 3400) {
            pill.className = 'kpi-pill pill-danger';
            pill.innerText = 'Riesgo Crítico de Hernia (>3400 N)';
        } else if (compN > 2500) {
            pill.className = 'kpi-pill pill-warn';
            pill.innerText = 'Sobrecarga Lumbar';
        } else {
            pill.className = 'kpi-pill pill-healthy';
            pill.innerText = 'Zona Ergonómica Segura';
        }
    """
    chart_js = """
        const load = parseFloat(document.getElementById('rngLoad').value);
        const flex = parseFloat(document.getElementById('rngFlex').value);
        const compN = Math.round(750 + load * 9.8 * 2.5 + flex * 35);
        const v = Math.min(38, (compN / 5000) * 38);
        chartHistory.push(v);
        if (chartHistory.length > 50) chartHistory.shift();

        dCtx.clearRect(0, 0, dockCanvas.width, dockCanvas.height);
        dCtx.strokeStyle = compN > 3400 ? '#f43f5e' : '#eab308';
        dCtx.lineWidth = 2;
        dCtx.beginPath();
        chartHistory.forEach((pt, idx) => {
            const x = (idx / 50) * dockCanvas.width;
            const y = dockCanvas.height - (pt / 40) * dockCanvas.height;
            if (idx === 0) dCtx.moveTo(x, y);
            else dCtx.lineTo(x, y);
        });
        dCtx.stroke();
        document.getElementById('chartLiveVal').innerText = compN + ' N';
    """
    return build_html_template(
        38, "[COD-038]", "Columna Vertebral Humana, Discos y Biomecánica",
        "Segmento Lumbar L3-S1 y Presión Intradiscal de Nachemson", "NIH 3D Orthopedic Tomography",
        "spine_b64.js", "SPINE_GLB_B64", "#eab308", "234, 179, 8",
        sliders, actions, kpis, "Carga Lumbar NIOSH", "2450 N",
        "Bienvenido a la Columna Lumbar 3D. Compara la compresión sobre el disco L4-L5 al levantar peso flexionando las rodillas frente a doblar la espalda.",
        setup_js, render_js, chart_js
    )


def generate_s39_iridescence():
    sliders = """
        <div class="panel-sec-title"><span>Óptica Estructural</span><span>Ley de Bragg</span></div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Ángulo Incidencia (θ)</span><span class="slider-val" id="valTheta">30 °</span></div>
            <input type="range" id="rngTheta" min="0" max="80" step="2" value="30">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Índice Refracción Medio (n)</span><span class="slider-val" id="valN">1.00 (Aire)</span></div>
            <input type="range" id="rngN" min="1.00" max="1.40" step="0.02" value="1.00">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Espaciado Lamelas (d)</span><span class="slider-val" id="valD">205 nm</span></div>
            <input type="range" id="rngD" min="160" max="260" step="5" value="205">
        </div>
    """
    actions = """
        <div class="panel-sec-title"><span>Inmersión en Solventes</span><span>Morpho peleides</span></div>
        <div class="btn-grid">
            <button class="btn-action active" id="btnAir">💨 En Aire (Azul)</button>
            <button class="btn-action" id="btnWater">💧 En Agua (Verde)</button>
        </div>
        <div class="btn-grid" style="margin-top:8px;">
            <button class="btn-action" id="btnAcetone" style="border-color:#fbbf24; color:#fde68a;">🧪 Acetona (n=1.36)</button>
            <button class="btn-action" id="btnSEM">🔬 Zoom SEM 20.000x</button>
        </div>
    """
    kpis = """
        <div class="kpi-card">
            <span class="kpi-label">Longitud de Onda Pico (λ)</span>
            <span class="kpi-value" id="kpiLambda">450 nm (Azul)</span>
            <span class="kpi-pill pill-healthy" id="pillOptic">Interferencia Constructiva</span>
        </div>
        <div class="kpi-card">
            <span class="kpi-label">Reflectancia Pico</span>
            <span class="kpi-value" id="kpiReflect">78.5 %</span>
        </div>
    """
    setup_js = """
        document.getElementById('btnAir').addEventListener('click', () => {
            document.getElementById('rngN').value = 1.00;
            document.getElementById('valN').innerText = '1.00 (Aire)';
            playSciPing(700, 0.1);
        });
        document.getElementById('btnWater').addEventListener('click', () => {
            document.getElementById('rngN').value = 1.33;
            document.getElementById('valN').innerText = '1.33 (Agua)';
            playSciPing(550, 0.1);
        });
        document.getElementById('btnAcetone').addEventListener('click', () => {
            document.getElementById('rngN').value = 1.36;
            document.getElementById('valN').innerText = '1.36 (Acetona)';
            playSciPing(450, 0.1);
        });
    """
    render_js = """
        const theta = parseFloat(document.getElementById('rngTheta').value) * Math.PI / 180;
        const n = parseFloat(document.getElementById('rngN').value);
        const d = parseFloat(document.getElementById('rngD').value);
        // Ley de Bragg-Snell: lambda = 2 * d * sqrt(n^2 - sin^2(theta))
        const sinT = Math.sin(theta);
        const lambda = Math.round(2 * d * Math.sqrt(Math.max(0.1, n*n - sinT*sinT)) * 0.7);
        let colorName = 'Azul Cobalto';
        if (lambda > 550) colorName = 'Verde / Amarillo';
        else if (lambda > 500) colorName = 'Verde Esmeralda';
        document.getElementById('kpiLambda').innerText = lambda + ' nm (' + colorName + ')';
    """
    chart_js = """
        const theta = parseFloat(document.getElementById('rngTheta').value) * Math.PI / 180;
        const n = parseFloat(document.getElementById('rngN').value);
        const d = parseFloat(document.getElementById('rngD').value);
        const sinT = Math.sin(theta);
        const lambda = Math.round(2 * d * Math.sqrt(Math.max(0.1, n*n - sinT*sinT)) * 0.7);
        const v = Math.max(5, Math.min(38, (lambda - 380) * 0.1));
        chartHistory.push(v);
        if (chartHistory.length > 50) chartHistory.shift();

        dCtx.clearRect(0, 0, dockCanvas.width, dockCanvas.height);
        dCtx.strokeStyle = '#06b6d4';
        dCtx.lineWidth = 2;
        dCtx.beginPath();
        chartHistory.forEach((pt, idx) => {
            const x = (idx / 50) * dockCanvas.width;
            const y = dockCanvas.height - (pt / 40) * dockCanvas.height;
            if (idx === 0) dCtx.moveTo(x, y);
            else dCtx.lineTo(x, y);
        });
        dCtx.stroke();
        document.getElementById('chartLiveVal').innerText = lambda + ' nm';
    """
    return build_html_template(
        39, "[COD-039]", "Mimetismo Óptico: Nanocristales e Iridiscencia",
        "SEM a 20.000x de Morpho peleides y Ley de Bragg-Snell", "Natural History Museum London",
        "iridescence_b64.js", "IRIDESCENCE_GLB_B64", "#06b6d4", "6, 182, 212",
        sliders, actions, kpis, "Espectro Reflectancia", "450 nm",
        "Bienvenido a la Iridiscencia de la Mariposa Morpho. El azul brillante no es pigmento: son nanoestructuras en árbol de Navidad que interfieren la luz blanca.",
        setup_js, render_js, chart_js
    )


def generate_s40_tissue():
    sliders = """
        <div class="panel-sec-title"><span>Cronología Cicatrizal</span><span>28 Días</span></div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Día Post-Lesión</span><span class="slider-val" id="valDay">Día 7</span></div>
            <input type="range" id="rngDay" min="0" max="28" step="1" value="7">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Oxigenación Tisular (pO₂)</span><span class="slider-val" id="valO2">45 mmHg</span></div>
            <input type="range" id="rngO2" min="15" max="80" step="5" value="45">
        </div>
        <div class="slider-wrap">
            <div class="slider-head"><span>Tensión Mecánica</span><span class="slider-val" id="valTension">Moderada</span></div>
            <input type="range" id="rngTension" min="1" max="5" step="1" value="3">
        </div>
    """
    actions = """
        <div class="panel-sec-title"><span>Fases de Cicatrización</span><span>Clark & Singer</span></div>
        <div class="btn-grid">
            <button class="btn-action" id="btnHemostasis">🩸 Hemostasia (D0)</button>
            <button class="btn-action active" id="btnProlif">🌿 Proliferación (D7)</button>
        </div>
        <div class="btn-grid" style="margin-top:8px;">
            <button class="btn-action" id="btnRemodel">💪 Remodelación (D28)</button>
            <button class="btn-action" id="btnPlayTimeline">▶️ Cascada Completa</button>
        </div>
    """
    kpis = """
        <div class="kpi-card">
            <span class="kpi-label">Fuerza Tensil Tisular</span>
            <span class="kpi-value" id="kpiTensile">35 %</span>
            <span class="kpi-pill pill-warn" id="pillTissue">Colágeno III Predominante</span>
        </div>
        <div class="kpi-card">
            <span class="kpi-label">Densidad Fibroblastos</span>
            <span class="kpi-value" id="kpiFibro">1.850 cél/mm²</span>
        </div>
    """
    setup_js = """
        document.getElementById('btnHemostasis').addEventListener('click', () => {
            document.getElementById('rngDay').value = 0;
            document.getElementById('valDay').innerText = 'Día 0';
            playSciPing(350, 0.1);
        });
        document.getElementById('btnProlif').addEventListener('click', () => {
            document.getElementById('rngDay').value = 7;
            document.getElementById('valDay').innerText = 'Día 7';
            playSciPing(500, 0.1);
        });
        document.getElementById('btnRemodel').addEventListener('click', () => {
            document.getElementById('rngDay').value = 28;
            document.getElementById('valDay').innerText = 'Día 28';
            playSciPing(680, 0.1);
        });
    """
    render_js = """
        const day = parseInt(document.getElementById('rngDay').value);
        const tensile = Math.min(80, Math.round(Math.pow(day / 28, 1.2) * 80));
        document.getElementById('kpiTensile').innerText = tensile + ' %';
        const fibro = day < 3 ? 400 : (day < 14 ? 1850 : 600);
        document.getElementById('kpiFibro').innerText = fibro.toLocaleString() + ' cél/mm²';

        const pill = document.getElementById('pillTissue');
        if (day >= 21) {
            pill.className = 'kpi-pill pill-healthy';
            pill.innerText = 'Colágeno I / Maduración';
        } else if (day >= 4) {
            pill.className = 'kpi-pill pill-warn';
            pill.innerText = 'Fase Proliferativa (Colágeno III)';
        } else {
            pill.className = 'kpi-pill pill-danger';
            pill.innerText = 'Hemostasia / Coágulo de Fibrina';
        }
    """
    chart_js = """
        const day = parseInt(document.getElementById('rngDay').value);
        const v = Math.min(38, Math.pow(day / 28, 1.2) * 38);
        chartHistory.push(v);
        if (chartHistory.length > 50) chartHistory.shift();

        dCtx.clearRect(0, 0, dockCanvas.width, dockCanvas.height);
        dCtx.strokeStyle = '#ec4899';
        dCtx.lineWidth = 2;
        dCtx.beginPath();
        chartHistory.forEach((pt, idx) => {
            const x = (idx / 50) * dockCanvas.width;
            const y = dockCanvas.height - (pt / 40) * dockCanvas.height;
            if (idx === 0) dCtx.moveTo(x, y);
            else dCtx.lineTo(x, y);
        });
        dCtx.stroke();
        document.getElementById('chartLiveVal').innerText = 'Día ' + day;
    """
    return build_html_template(
        40, "[COD-040]", "Regeneración Tisular, Fibroblastos y Matriz Extracelular",
        "Cicatrización en 28 Días, Angiogénesis y Colágeno I/III", "NIH 3D Regenerative Medicine",
        "tissue_repair_b64.js", "TISSUE_REPAIR_GLB_B64", "#ec4899", "236, 72, 153",
        sliders, actions, kpis, "Fuerza Tensil Tisular", "Día 7",
        "Bienvenido al Laboratorio de Regeneración Tisular 3D. Observa cómo los fibroblastos migran hacia la herida, sintetizan colágeno tipo tres y lo reemplazan por colágeno tipo uno resistente.",
        setup_js, render_js, chart_js
    )


def save_dual(filename, content, sesion_num):
    # 1. En SIMULADORES_INTERACTIVOS/01_SIMULADORES/
    p1 = os.path.join(SIM_DIR, filename)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(content)

    # 2. En la carpeta de sesión correspondiente
    s_dir = os.path.join(SESSIONS_ROOT, f"{sesion_num:02d}_Sesion")
    os.makedirs(s_dir, exist_ok=True)
    p2 = os.path.join(s_dir, filename)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ [Sesión {sesion_num:02d}] Generado y espejado: {filename}")


def main():
    print("🚀 Iniciando reconstrucción oficial de los 10 Simuladores HTML del Lote 4 con Babylon.js...")
    
    save_dual("SIMULADOR_ARRECIFE_CORAL_3D.html", generate_s31_coral(), 31)
    save_dual("SIMULADOR_RED_TROFICA_3D.html", generate_s32_trophic(), 32)
    save_dual("SIMULADOR_MITOCONDRIA_3D.html", generate_s33_mitochondria(), 33)
    save_dual("SIMULADOR_TELOMEROS_3D.html", generate_s34_telomeres(), 34)
    save_dual("SIMULADOR_SELVA_TROPICAL_3D.html", generate_s35_rainforest(), 35)
    save_dual("SIMULADOR_CANAL_IONICO_3D.html", generate_s36_ionchannel(), 36)
    save_dual("SIMULADOR_PIEL_HUMANA_3D.html", generate_s37_skin(), 37)
    save_dual("SIMULADOR_COLUMNA_VERTEBRAL_3D.html", generate_s38_spine(), 38)
    save_dual("SIMULADOR_IRIDISCENCIA_3D.html", generate_s39_iridescence(), 39)
    save_dual("SIMULADOR_REGENERACION_TISULAR_3D.html", generate_s40_tissue(), 40)

    print("✨ Los 10 simuladores han sido reconstruidos y doble-espejados con éxito.")

if __name__ == '__main__':
    main()
