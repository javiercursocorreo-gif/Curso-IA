#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_cod_lote4_htmls.py
Generador Maestro y Espejador Dual de los 10 Simuladores Científicos Hiperrealistas 3D
para el LOTE 4 [COD] (Sesiones 31 a 40):
- Sesión 31: Arrecife de Coral, Pólipos y Simbiosis Marina 3D (SIMULADOR_ARRECIFE_CORAL_3D.html)
- Sesión 32: Pirámide Trófica y Red Ecológica Fluvial 3D (SIMULADOR_RED_TROFICA_3D.html)
- Sesión 33: Mitocondria: Central Celular y ATP Sintasa 3D (SIMULADOR_MITOCONDRIA_3D.html)
- Sesión 34: Telómeros Cromosómicos, Telomerasa y Hayflick 3D (SIMULADOR_TELOMEROS_3D.html)
- Sesión 35: Bioma de Selva Tropical: Estratos de Altura 3D (SIMULADOR_SELVA_TROPICAL_3D.html)
- Sesión 36: Neurotoxina y Bloqueo de Canales Iónicos 3D (SIMULADOR_CANAL_IONICO_3D.html)
- Sesión 37: Piel Humana, Capas Tisulares y Termorregulación 3D (SIMULADOR_PIEL_HUMANA_3D.html)
- Sesión 38: Columna Vertebral Humana, Discos y Biomecánica Lumbar 3D (SIMULADOR_COLUMNA_VERTEBRAL_3D.html)
- Sesión 39: Mimetismo Óptico: Nanocristales e Iridiscencia 3D (SIMULADOR_IRIDISCENCIA_3D.html)
- Sesión 40: Regeneración Tisular, Fibroblastos y Matriz Extracelular 3D (SIMULADOR_REGENERACION_TISULAR_3D.html)

Guarda automáticamente en:
1. SIMULADORES_INTERACTIVOS/01_SIMULADORES/
2. CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/XX_Sesion/
"""

import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
SIM_DIR = os.path.join(BASE_DIR, "SIMULADORES_INTERACTIVOS", "01_SIMULADORES")
SESSIONS_DIR = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM")

os.makedirs(SIM_DIR, exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SESIÓN 31: ARRECIFE DE CORAL, PÓLIPOS Y SIMBIOSIS MARINA 3D
# -----------------------------------------------------------------------------
def get_html_s31():
    return """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesión 31 • Arrecife de Coral, Pólipos y Simbiosis Marina 3D [COD-031]</title>
    <!-- NOAA Coral Reef Watch • Cryo-EM Cnidarios • Grados Días de Calentamiento (DHW) -->
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #010712;
            --bg-panel: rgba(4, 15, 30, 0.94);
            --border: rgba(56, 189, 248, 0.35);
            --primary: #38bdf8;
            --primary-glow: rgba(56, 189, 248, 0.4);
            --coral-live: #f43f5e;
            --coral-bleached: #f8fafc;
            --zoox: #10b981;
            --amber: #fbbf24;
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
            --font-title: 'Cinzel', serif;
            --font-sans: 'Inter', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
        body {
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-sans);
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            font-size: 14px;
        }

        header {
            background: linear-gradient(180deg, rgba(2, 10, 24, 0.98) 0%, rgba(2, 10, 24, 0.88) 100%);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border);
            padding: 10px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-shrink: 0;
            z-index: 40;
        }
        .brand-box { display: flex; align-items: center; gap: 14px; }
        .badge-pill {
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid var(--primary);
            color: var(--primary);
            font-family: var(--font-mono);
            font-weight: 800;
            font-size: 0.82rem;
            padding: 4px 10px;
            border-radius: 6px;
        }
        .title-text h1 {
            font-family: var(--font-title);
            font-size: 1.15rem;
            font-weight: 800;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .title-text p { font-size: 0.78rem; color: var(--text-sub); margin-top: 1px; }

        .header-actions { display: flex; align-items: center; gap: 10px; }
        .btn-header {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: var(--text-main);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .btn-header:hover { background: rgba(56, 189, 248, 0.2); border-color: var(--primary); color: #fff; }

        .workspace { flex: 1; position: relative; overflow: hidden; display: flex; }

        .viewer-container {
            flex: 1;
            position: relative;
            background: radial-gradient(circle at center, #03182e 0%, #010712 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        #coralCanvas {
            max-width: 96%;
            max-height: 92%;
            border-radius: 14px;
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.9);
            border: 1px solid rgba(56, 189, 248, 0.25);
            background: #020b17;
            cursor: grab;
        }
        #coralCanvas:active { cursor: grabbing; }

        .controls-panel {
            position: absolute;
            top: 18px;
            left: 20px;
            width: 350px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 18px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 14px;
            max-height: calc(100vh - 120px);
            overflow-y: auto;
        }

        .panel-sec-title {
            font-size: 0.78rem;
            font-family: var(--font-mono);
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 5px;
        }

        .slider-group { display: flex; flex-direction: column; gap: 6px; }
        .slider-label {
            display: flex;
            justify-content: space-between;
            font-size: 0.82rem;
            color: var(--text-sub);
        }
        .slider-val { font-family: var(--font-mono); color: #fff; font-weight: 700; }
        input[type="range"] {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: #1e293b;
            outline: none;
            cursor: pointer;
            accent-color: var(--primary);
        }

        .btn-group { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
        .btn-action {
            background: rgba(56, 189, 248, 0.12);
            border: 1px solid rgba(56, 189, 248, 0.35);
            color: #fff;
            padding: 9px 10px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }
        .btn-action:hover { background: rgba(56, 189, 248, 0.28); border-color: var(--primary); }
        .btn-action.active { background: var(--primary); color: #020712; font-weight: 800; }
        .btn-action.danger { background: rgba(244, 63, 94, 0.15); border-color: #f43f5e; color: #fca5a5; }
        .btn-action.danger:hover { background: #f43f5e; color: #fff; }

        .telemetry-card {
            position: absolute;
            bottom: 20px;
            right: 20px;
            width: 320px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 16px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .kpi-row { display: flex; justify-content: space-between; align-items: center; }
        .kpi-name { font-size: 0.78rem; color: var(--text-sub); }
        .kpi-val { font-family: var(--font-mono); font-size: 0.88rem; font-weight: 700; color: #fff; }
        .status-badge {
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.74rem;
            font-weight: 800;
            text-align: center;
        }
        .status-healthy { background: rgba(16, 185, 129, 0.2); color: #6ee7b7; border: 1px solid #10b981; }
        .status-warning { background: rgba(251, 191, 36, 0.2); color: #fde68a; border: 1px solid #fbbf24; }
        .status-bleached { background: rgba(244, 63, 94, 0.2); color: #fda4af; border: 1px solid #f43f5e; }
    </style>
</head>
<body>
    <header>
        <div class="brand-box">
            <span class="badge-pill">[COD-031]</span>
            <div class="title-text">
                <h1>🪸 Laboratorio Marino: Arrecife de Coral & Simbiosis 3D</h1>
                <p>NOAA Coral Reef Watch • Pólipos Cnidarios • Dinámica de Zooxantelas (Symbiodiniaceae) • Grados Días de Calentamiento (DHW)</p>
            </div>
        </div>
        <div class="header-actions">
            <button class="btn-header" id="btnAudioToggle">🔊 Audio Ecosistema: ON</button>
            <button class="btn-header" id="btnVoiceGuide">🗣️ Guía por Voz</button>
            <button class="btn-header" id="btnResetView">🎯 Centrar Vista</button>
        </div>
    </header>

    <div class="workspace">
        <div class="viewer-container">
            <canvas id="coralCanvas" width="900" height="650"></canvas>
        </div>

        <div class="controls-panel">
            <div class="panel-sec-title">
                <span>Variables Oceánicas (NOAA CRW)</span>
                <span>🌊 IN-SITU</span>
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Temperatura del Agua (SST)</span>
                    <span class="slider-val" id="valTemp">27.0 °C</span>
                </div>
                <input type="range" id="rngTemp" min="24.0" max="33.0" step="0.1" value="27.0">
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Acumulación Térmica (DHW)</span>
                    <span class="slider-val" id="valDHW">0.0 °C-sem</span>
                </div>
                <input type="range" id="rngDHW" min="0" max="16" step="0.5" value="0">
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Acidificación Oceánica (pH)</span>
                    <span class="slider-val" id="valPH">8.15 pH</span>
                </div>
                <input type="range" id="rngPH" min="7.60" max="8.30" step="0.01" value="8.15">
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Radiación Solar / UV</span>
                    <span class="slider-val" id="valUV">450 µmol/m²s</span>
                </div>
                <input type="range" id="rngUV" min="100" max="1200" step="25" value="450">
            </div>

            <div class="panel-sec-title">
                <span>Modos y Procesos Biológicos</span>
                <span>🔬 CNIDARIOS</span>
            </div>

            <div class="btn-group">
                <button class="btn-action active" id="btnCycle">☀️ Modo Día</button>
                <button class="btn-action" id="btnFeeding">🦐 Zooplancton</button>
            </div>

            <div class="btn-group">
                <button class="btn-action danger" id="btnHeatwave">🔥 Ola de Calor</button>
                <button class="btn-action" id="btnRecovery">🌿 Recuperación</button>
            </div>
        </div>

        <div class="telemetry-card">
            <div class="panel-sec-title">
                <span>Telemetría Arrecifal</span>
                <span>NOAA / Cryo-EM</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Densidad Zooxantelas:</span>
                <span class="kpi-val" id="kpiZoox">1.48 × 10⁶ cél/cm²</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Tasa Calcificación CaCO₃:</span>
                <span class="kpi-val" id="kpiCalc">14.2 g/m²/día</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Extensión de Tentáculos:</span>
                <span class="kpi-val" id="kpiTent">Reposo Diurno</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Estado de Blanqueamiento:</span>
                <span class="status-badge status-healthy" id="kpiStatus">Normal / Saludable</span>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('coralCanvas');
        const ctx = canvas.getContext('2d');

        // Estado científico del arrecife
        let state = {
            temp: 27.0,
            dhw: 0.0,
            ph: 8.15,
            uv: 450,
            isNight: false,
            feeding: false,
            zooxHealth: 1.0, // 1.0 = normal, 0.0 = blanqueado total
            rotX: -0.2,
            rotY: 0.3,
            zoom: 1.0,
            audioEnabled: true
        };

        // Generar estructura de coral (esqueleto aragonito + pólipos radiales)
        const polyps = [];
        const numPolyps = 24;
        for (let i = 0; i < numPolyps; i++) {
            const phi = Math.acos(-1 + (2 * i) / numPolyps);
            const theta = Math.sqrt(numPolyps * Math.PI) * phi;
            const r = 140 + Math.sin(i * 3.5) * 20;
            polyps.push({
                x: r * Math.sin(phi) * Math.cos(theta),
                y: r * Math.sin(phi) * Math.sin(theta) * 0.7 - 20,
                z: r * Math.cos(phi),
                tentacles: 8,
                phase: Math.random() * Math.PI * 2,
                size: 14 + Math.random() * 6
            });
        }

        // Web Audio Submarino
        let audioCtx = null;
        function playSubAudio() {
            if (!state.audioEnabled) return;
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(80 + Math.random() * 40, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.02, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 1.2);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + 1.2);
            } catch(e) {}
        }
        setInterval(playSubAudio, 2400);

        // Síntesis de voz
        function speak(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const u = new SpeechSynthesisUtterance(text);
                u.lang = 'es-ES';
                u.rate = 1.05;
                window.speechSynthesis.speak(u);
            }
        }

        // Interacción orbital con ratón
        let isDragging = false;
        let lastMouse = { x: 0, y: 0 };
        canvas.addEventListener('mousedown', (e) => {
            isDragging = true;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        window.addEventListener('mouseup', () => isDragging = false);
        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            const dx = e.clientX - lastMouse.x;
            const dy = e.clientY - lastMouse.y;
            state.rotY += dx * 0.008;
            state.rotX += dy * 0.008;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        canvas.addEventListener('wheel', (e) => {
            e.preventDefault();
            state.zoom *= e.deltaY > 0 ? 0.95 : 1.05;
            state.zoom = Math.max(0.6, Math.min(2.2, state.zoom));
        });

        // Loop de renderizado 3D fotorrealista
        let t = 0;
        function render() {
            t += 0.025;
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            const cx = canvas.width / 2;
            const cy = canvas.height / 2 + 30;

            // Iluminación cáustica marina submarina
            const causticAlpha = state.isNight ? 0.04 : 0.15;
            ctx.save();
            ctx.fillStyle = `rgba(56, 189, 248, ${causticAlpha})`;
            for (let i = 0; i < 5; i++) {
                ctx.beginPath();
                ctx.arc(cx + Math.sin(t * 0.8 + i) * 260, cy - 120 + Math.cos(t * 0.6 + i) * 100, 80 + i * 20, 0, Math.PI * 2);
                ctx.fill();
            }
            ctx.restore();

            // Transformación 3D
            const cosY = Math.cos(state.rotY);
            const sinY = Math.sin(state.rotY);
            const cosX = Math.cos(state.rotX);
            const sinX = Math.sin(state.rotX);

            function project(p) {
                // Rot Y
                let x1 = p.x * cosY + p.z * sinY;
                let z1 = -p.x * sinY + p.z * cosY;
                // Rot X
                let y2 = p.y * cosX - z1 * sinX;
                let z2 = p.y * sinX + z1 * cosX;
                const fov = 480;
                const scale = (fov / (fov + z2 + 300)) * state.zoom;
                return {
                    x: cx + x1 * scale,
                    y: cy + y2 * scale,
                    z: z2,
                    scale: scale
                };
            }

            // Ordenar pólipos por profundidad Z (Painter's algorithm)
            const projectedPolyps = polyps.map((p, idx) => ({ ...p, proj: project(p), idx }));
            projectedPolyps.sort((a, b) => b.proj.z - a.proj.z);

            // Base de esqueleto pétreo CaCO3
            ctx.save();
            const gradBase = ctx.createRadialGradient(cx, cy + 60, 20, cx, cy + 60, 220 * state.zoom);
            const rBase = Math.floor(220 * (1 - state.zooxHealth) + 120 * state.zooxHealth);
            const gBase = Math.floor(220 * (1 - state.zooxHealth) + 60 * state.zooxHealth);
            const bBase = Math.floor(220 * (1 - state.zooxHealth) + 80 * state.zooxHealth);
            gradBase.addColorStop(0, `rgb(${rBase}, ${gBase}, ${bBase})`);
            gradBase.addColorStop(1, '#051329');
            ctx.fillStyle = gradBase;
            ctx.beginPath();
            ctx.ellipse(cx, cy + 50, 180 * state.zoom, 110 * state.zoom, 0, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();

            // Dibujar cada pólipo cnidario
            projectedPolyps.forEach(p => {
                const pr = p.proj;
                if (pr.scale <= 0) return;

                // Color dinámico según salud de zooxantelas y blanqueamiento
                // Zooxantelas saludables = coral marrón-rosado brillante (#e11d48 a #059669)
                // Blanqueado = blanco lechoso de aragonito (#f1f5f9)
                const hR = Math.floor(240 * (1 - state.zooxHealth) + 225 * state.zooxHealth);
                const hG = Math.floor(245 * (1 - state.zooxHealth) + 40 * state.zooxHealth);
                const hB = Math.floor(250 * (1 - state.zooxHealth) + 90 * state.zooxHealth);

                // Columna del pólipo
                ctx.beginPath();
                ctx.arc(pr.x, pr.y, p.size * pr.scale, 0, Math.PI * 2);
                ctx.fillStyle = `rgb(${hR}, ${hG}, ${hB})`;
                ctx.fill();
                ctx.strokeStyle = `rgba(255, 255, 255, 0.35)`;
                ctx.lineWidth = 1.5;
                ctx.stroke();

                // Tentáculos móviles (se extienden de noche o al alimentar)
                const tentReach = (state.isNight || state.feeding ? 1.6 : 0.6) * pr.scale;
                const tentCount = p.tentacles;
                for (let k = 0; k < tentCount; k++) {
                    const ang = (Math.PI * 2 / tentCount) * k + t * 0.5 + p.phase;
                    const sway = Math.sin(t * 2 + k + p.phase) * (6 * pr.scale);
                    const tx = pr.x + Math.cos(ang) * (p.size * pr.scale + 16 * tentReach) + sway;
                    const ty = pr.y + Math.sin(ang) * (p.size * pr.scale + 16 * tentReach) + sway;

                    ctx.beginPath();
                    ctx.moveTo(pr.x + Math.cos(ang) * (p.size * pr.scale * 0.8), pr.y + Math.sin(ang) * (p.size * pr.scale * 0.8));
                    ctx.quadraticCurveTo(pr.x + Math.cos(ang) * 12 * pr.scale + sway, pr.y + Math.sin(ang) * 12 * pr.scale + sway, tx, ty);
                    ctx.strokeStyle = state.zooxHealth > 0.4 ? `rgba(251, 113, 133, 0.8)` : `rgba(241, 245, 249, 0.7)`;
                    ctx.lineWidth = 2.2 * pr.scale;
                    ctx.stroke();

                    // Zooxantelas visibles como puntos verdes fotosintéticos si está sano
                    if (state.zooxHealth > 0.25 && !state.isNight) {
                        ctx.beginPath();
                        ctx.arc(tx, ty, 1.8 * pr.scale, 0, Math.PI * 2);
                        ctx.fillStyle = `rgba(16, 185, 129, ${state.zooxHealth * 0.9})`;
                        ctx.fill();
                    }
                }

                // Boca / cavidad gastrovascular central
                ctx.beginPath();
                ctx.arc(pr.x, pr.y, 3 * pr.scale, 0, Math.PI * 2);
                ctx.fillStyle = '#1e1b4b';
                ctx.fill();
            });

            // Partículas de zooplancton suspendidas
            if (state.feeding || state.isNight) {
                ctx.fillStyle = 'rgba(251, 191, 36, 0.75)';
                for (let j = 0; j < 18; j++) {
                    const px = cx + Math.sin(t * 0.5 + j * 1.3) * 280;
                    const py = cy - 80 + Math.cos(t * 0.7 + j * 0.9) * 180;
                    ctx.beginPath();
                    ctx.arc(px, py, 2.2, 0, Math.PI * 2);
                    ctx.fill();
                }
            }

            requestAnimationFrame(render);
        }
        render();

        // Lógica de telemetría y actualización
        function updateTelemetry() {
            // Umbral biológico: > 30.5 °C o DHW > 4 causa expulsión de zooxantelas
            if (state.temp > 30.5 || state.dhw >= 4.0) {
                const stress = Math.max((state.temp - 30.5) * 0.2, (state.dhw - 3.5) * 0.08);
                state.zooxHealth = Math.max(0.05, state.zooxHealth - stress * 0.02);
            } else if (state.temp <= 28.5 && state.dhw < 2.0) {
                state.zooxHealth = Math.min(1.0, state.zooxHealth + 0.008);
            }

            const dens = (state.zooxHealth * 1.5).toFixed(2);
            document.getElementById('kpiZoox').innerText = `${dens} × 10⁶ cél/cm²`;

            // Tasa de calcificación afectada por pH y zooxantelas
            const phFactor = Math.max(0.2, (state.ph - 7.6) / (8.2 - 7.6));
            const calc = (14.5 * state.zooxHealth * phFactor).toFixed(1);
            document.getElementById('kpiCalc').innerText = `${calc} g/m²/día`;

            // Estado NOAA
            const statusEl = document.getElementById('kpiStatus');
            if (state.dhw >= 8 || state.zooxHealth < 0.2) {
                statusEl.className = 'status-badge status-bleached';
                statusEl.innerText = '🚨 Alerta Nivel 2: Blanqueamiento Masivo';
            } else if (state.dhw >= 4 || state.zooxHealth < 0.6) {
                statusEl.className = 'status-badge status-warning';
                statusEl.innerText = '⚠️ Alerta Nivel 1: Riesgo Térmico';
            } else {
                statusEl.className = 'status-badge status-healthy';
                statusEl.innerText = 'Normal / Simbiosis Estable';
            }

            document.getElementById('kpiTent').innerText = state.isNight ? 'Expandidos (Captura Activa)' : (state.feeding ? 'Capturando Zooplancton' : 'Reposo Diurno');
        }
        setInterval(updateTelemetry, 300);

        // Controladores UI
        document.getElementById('rngTemp').addEventListener('input', (e) => {
            state.temp = parseFloat(e.target.value);
            document.getElementById('valTemp').innerText = state.temp.toFixed(1) + ' °C';
            if (state.temp > 30.5) state.dhw = Math.min(16, state.dhw + 0.2);
            document.getElementById('rngDHW').value = state.dhw;
            document.getElementById('valDHW').innerText = state.dhw.toFixed(1) + ' °C-sem';
        });

        document.getElementById('rngDHW').addEventListener('input', (e) => {
            state.dhw = parseFloat(e.target.value);
            document.getElementById('valDHW').innerText = state.dhw.toFixed(1) + ' °C-sem';
        });

        document.getElementById('rngPH').addEventListener('input', (e) => {
            state.ph = parseFloat(e.target.value);
            document.getElementById('valPH').innerText = state.ph.toFixed(2) + ' pH';
        });

        document.getElementById('rngUV').addEventListener('input', (e) => {
            state.uv = parseInt(e.target.value);
            document.getElementById('valUV').innerText = state.uv + ' µmol/m²s';
        });

        document.getElementById('btnCycle').addEventListener('click', (e) => {
            state.isNight = !state.isNight;
            e.target.innerText = state.isNight ? '🌙 Modo Noche' : '☀️ Modo Día';
            e.target.classList.toggle('active', !state.isNight);
        });

        document.getElementById('btnFeeding').addEventListener('click', () => {
            state.feeding = !state.feeding;
            document.getElementById('btnFeeding').classList.toggle('active', state.feeding);
            if (state.feeding) speak("Alimentación cnidaria activada. Los pólipos despliegan sus tentáculos radiales para capturar zooplancton mediante nematocistos.");
        });

        document.getElementById('btnHeatwave').addEventListener('click', () => {
            state.temp = 32.2;
            state.dhw = 9.5;
            document.getElementById('rngTemp').value = 32.2;
            document.getElementById('valTemp').innerText = '32.2 °C';
            document.getElementById('rngDHW').value = 9.5;
            document.getElementById('valDHW').innerText = '9.5 °C-sem';
            speak("Alerta NOAA Nivel 2. Ola marina calórica extrema. La fotosíntesis de las zooxantelas colapsa y el pólipo expulsa las algas simbiontes, blanqueando el arrecife.");
        });

        document.getElementById('btnRecovery').addEventListener('click', () => {
            state.temp = 26.5;
            state.dhw = 0.5;
            state.zooxHealth = 0.95;
            document.getElementById('rngTemp').value = 26.5;
            document.getElementById('valTemp').innerText = '26.5 °C';
            document.getElementById('rngDHW').value = 0.5;
            document.getElementById('valDHW').innerText = '0.5 °C-sem';
            speak("Temperatura oceánica restablecida a niveles óptimos. Las microalgas zooxantelas repueblan el tejido de los pólipos restableciendo la simbiosis.");
        });

        document.getElementById('btnAudioToggle').addEventListener('click', (e) => {
            state.audioEnabled = !state.audioEnabled;
            e.target.innerText = state.audioEnabled ? '🔊 Audio Ecosistema: ON' : '🔈 Audio: OFF';
        });

        document.getElementById('btnVoiceGuide').addEventListener('click', () => {
            speak("Bienvenido al simulador tridimensional del Arrecife de Coral. Observa la colonia de pólipos y el esqueleto de aragonito. Aumenta la temperatura para presenciar el fenómeno de blanqueamiento.");
        });

        document.getElementById('btnResetView').addEventListener('click', () => {
            state.rotX = -0.2;
            state.rotY = 0.3;
            state.zoom = 1.0;
        });
    </script>
</body>
</html>
"""

# -----------------------------------------------------------------------------
# 2. SESIÓN 32: PIRÁMIDE TRÓFICA Y RED ECOLÓGICA FLUVIAL 3D
# -----------------------------------------------------------------------------
def get_html_s32():
    return """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesión 32 • Pirámide Trófica y Red Ecológica Fluvial 3D [COD-032]</title>
    <!-- Dinámica de Biomasa Lindeman (Ley del 10%) • USGS River Ecology • Eutrofización -->
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #020914;
            --bg-panel: rgba(6, 18, 36, 0.94);
            --border: rgba(16, 185, 129, 0.35);
            --primary: #10b981;
            --primary-glow: rgba(16, 185, 129, 0.4);
            --cyan: #38bdf8;
            --amber: #fbbf24;
            --rose: #f43f5e;
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
            --font-title: 'Cinzel', serif;
            --font-sans: 'Inter', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
        body {
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-sans);
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            font-size: 14px;
        }

        header {
            background: linear-gradient(180deg, rgba(4, 15, 30, 0.98) 0%, rgba(4, 15, 30, 0.88) 100%);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border);
            padding: 10px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-shrink: 0;
            z-index: 40;
        }
        .brand-box { display: flex; align-items: center; gap: 14px; }
        .badge-pill {
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid var(--primary);
            color: var(--primary);
            font-family: var(--font-mono);
            font-weight: 800;
            font-size: 0.82rem;
            padding: 4px 10px;
            border-radius: 6px;
        }
        .title-text h1 {
            font-family: var(--font-title);
            font-size: 1.15rem;
            font-weight: 800;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .title-text p { font-size: 0.78rem; color: var(--text-sub); margin-top: 1px; }

        .header-actions { display: flex; align-items: center; gap: 10px; }
        .btn-header {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: var(--text-main);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .btn-header:hover { background: rgba(16, 185, 129, 0.2); border-color: var(--primary); color: #fff; }

        .workspace { flex: 1; position: relative; overflow: hidden; display: flex; }

        .viewer-container {
            flex: 1;
            position: relative;
            background: radial-gradient(circle at center, #062238 0%, #020914 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        #riverCanvas {
            max-width: 96%;
            max-height: 92%;
            border-radius: 14px;
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.9);
            border: 1px solid rgba(16, 185, 129, 0.25);
            background: #031021;
            cursor: grab;
        }
        #riverCanvas:active { cursor: grabbing; }

        .controls-panel {
            position: absolute;
            top: 18px;
            left: 20px;
            width: 350px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 18px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 14px;
            max-height: calc(100vh - 120px);
            overflow-y: auto;
        }

        .panel-sec-title {
            font-size: 0.78rem;
            font-family: var(--font-mono);
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 5px;
        }

        .slider-group { display: flex; flex-direction: column; gap: 6px; }
        .slider-label {
            display: flex;
            justify-content: space-between;
            font-size: 0.82rem;
            color: var(--text-sub);
        }
        .slider-val { font-family: var(--font-mono); color: #fff; font-weight: 700; }
        input[type="range"] {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: #1e293b;
            outline: none;
            cursor: pointer;
            accent-color: var(--primary);
        }

        .btn-group { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
        .btn-action {
            background: rgba(16, 185, 129, 0.12);
            border: 1px solid rgba(16, 185, 129, 0.35);
            color: #fff;
            padding: 9px 10px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }
        .btn-action:hover { background: rgba(16, 185, 129, 0.28); border-color: var(--primary); }
        .btn-action.active { background: var(--primary); color: #020914; font-weight: 800; }
        .btn-action.danger { background: rgba(244, 63, 94, 0.15); border-color: #f43f5e; color: #fca5a5; }
        .btn-action.danger:hover { background: #f43f5e; color: #fff; }

        .telemetry-card {
            position: absolute;
            bottom: 20px;
            right: 20px;
            width: 320px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 16px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .kpi-row { display: flex; justify-content: space-between; align-items: center; }
        .kpi-name { font-size: 0.78rem; color: var(--text-sub); }
        .kpi-val { font-family: var(--font-mono); font-size: 0.88rem; font-weight: 700; color: #fff; }
        .status-badge {
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.74rem;
            font-weight: 800;
            text-align: center;
        }
        .status-healthy { background: rgba(16, 185, 129, 0.2); color: #6ee7b7; border: 1px solid #10b981; }
        .status-warning { background: rgba(251, 191, 36, 0.2); color: #fde68a; border: 1px solid #fbbf24; }
        .status-danger { background: rgba(244, 63, 94, 0.2); color: #fda4af; border: 1px solid #f43f5e; }
    </style>
</head>
<body>
    <header>
        <div class="brand-box">
            <span class="badge-pill">[COD-032]</span>
            <div class="title-text">
                <h1>🏞️ Pirámide Trófica y Red Ecológica Fluvial 3D</h1>
                <p>Dinámica de Lindeman (Ley del 10%) • USGS River Ecology • Flujo de Energía (kcal/m²/año) • Bioacumulación</p>
            </div>
        </div>
        <div class="header-actions">
            <button class="btn-header" id="btnAudioToggle">🔊 Sonido Río: ON</button>
            <button class="btn-header" id="btnVoiceGuide">🗣️ Guía por Voz</button>
            <button class="btn-header" id="btnResetView">🎯 Centrar Vista</button>
        </div>
    </header>

    <div class="workspace">
        <div class="viewer-container">
            <canvas id="riverCanvas" width="900" height="650"></canvas>
        </div>

        <div class="controls-panel">
            <div class="panel-sec-title">
                <span>Parámetros de Entrada Ecológica</span>
                <span>⚡ ENERGÍA</span>
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Radiación Solar Fotosintética</span>
                    <span class="slider-val" id="valSolar">20.000 kcal/m²</span>
                </div>
                <input type="range" id="rngSolar" min="5000" max="40000" step="1000" value="20000">
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Eficiencia de Lindeman (%)</span>
                    <span class="slider-val" id="valEff">10.0 %</span>
                </div>
                <input type="range" id="rngEff" min="5.0" max="20.0" step="0.5" value="10.0">
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Concentración Nitratos/Fósforo</span>
                    <span class="slider-val" id="valNutr">2.4 mg/L</span>
                </div>
                <input type="range" id="rngNutr" min="0.5" max="15.0" step="0.5" value="2.4">
            </div>

            <div class="panel-sec-title">
                <span>Impactos Antrópicos y Modos</span>
                <span>🧪 PERTURBACIÓN</span>
            </div>

            <div class="btn-group">
                <button class="btn-action danger" id="btnEutro">⚠️ Eutrofización</button>
                <button class="btn-action danger" id="btnOverfish">🎣 Sobrepesca</button>
            </div>

            <div class="btn-group">
                <button class="btn-action" id="btnBiomagn">☢️ Bioacumulación</button>
                <button class="btn-action active" id="btnResetEco">🌿 Restaurar</button>
            </div>
        </div>

        <div class="telemetry-card">
            <div class="panel-sec-title">
                <span>Telemetría de la Red Trófica</span>
                <span>USGS / Lindeman</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Productores (Diatomeas):</span>
                <span class="kpi-val" id="kpiL1">20.000 kcal</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Consumidores 1° (Efímeras):</span>
                <span class="kpi-val" id="kpiL2">2.000 kcal</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Consumidores 2° (Truchas):</span>
                <span class="kpi-val" id="kpiL3">200 kcal</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Ápice (Nutria Fluvial):</span>
                <span class="kpi-val" id="kpiL4">20 kcal</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Oxígeno Disuelto (DO):</span>
                <span class="kpi-val" id="kpiDO">8.8 mg/L</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Estado del Ecosistema:</span>
                <span class="status-badge status-healthy" id="kpiStatus">Equilibrio Trófico</span>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('riverCanvas');
        const ctx = canvas.getContext('2d');

        let state = {
            solar: 20000,
            eff: 0.10,
            nutr: 2.4,
            eutro: false,
            overfish: false,
            biomag: false,
            rotX: -0.25,
            rotY: 0.4,
            zoom: 1.0,
            audioEnabled: true
        };

        // Web Audio - Flujo de corriente fluvial
        let audioCtx = null;
        function playRiverFlow() {
            if (!state.audioEnabled) return;
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                const bufferSize = audioCtx.sampleRate * 1.5;
                const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
                const data = buffer.getChannelData(0);
                for (let i = 0; i < bufferSize; i++) {
                    data[i] = (Math.random() * 2 - 1) * 0.015;
                }
                const noise = audioCtx.createBufferSource();
                noise.buffer = buffer;
                const filter = audioCtx.createBiquadFilter();
                filter.type = 'lowpass';
                filter.frequency.setValueAtTime(450, audioCtx.currentTime);
                noise.connect(filter);
                filter.connect(audioCtx.destination);
                noise.start();
            } catch(e) {}
        }
        setInterval(playRiverFlow, 2000);

        function speak(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const u = new SpeechSynthesisUtterance(text);
                u.lang = 'es-ES';
                u.rate = 1.05;
                window.speechSynthesis.speak(u);
            }
        }

        // Interacción orbital
        let isDragging = false;
        let lastMouse = { x: 0, y: 0 };
        canvas.addEventListener('mousedown', (e) => {
            isDragging = true;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        window.addEventListener('mouseup', () => isDragging = false);
        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            const dx = e.clientX - lastMouse.x;
            const dy = e.clientY - lastMouse.y;
            state.rotY += dx * 0.008;
            state.rotX += dy * 0.008;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        canvas.addEventListener('wheel', (e) => {
            e.preventDefault();
            state.zoom *= e.deltaY > 0 ? 0.95 : 1.05;
            state.zoom = Math.max(0.6, Math.min(2.0, state.zoom));
        });

        // 4 Niveles Tróficos tridimensionales en pirámide
        let t = 0;
        function render() {
            t += 0.02;
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            const cx = canvas.width / 2;
            const cy = canvas.height / 2 + 50;

            const cosY = Math.cos(state.rotY);
            const sinY = Math.sin(state.rotY);
            const cosX = Math.cos(state.rotX);
            const sinX = Math.sin(state.rotX);

            function project(x, y, z) {
                let x1 = x * cosY + z * sinY;
                let z1 = -x * sinY + z * cosY;
                let y2 = y * cosX - z1 * sinX;
                let z2 = y * sinX + z1 * cosX;
                const fov = 450;
                const scale = (fov / (fov + z2 + 300)) * state.zoom;
                return { x: cx + x1 * scale, y: cy + y2 * scale, z: z2, scale: scale };
            }

            // Datos de la pirámide elométrica trófica (Lindeman)
            const levels = [
                { name: "Productores (Diatomeas)", w: 320, h: 45, y: 80, color: '#10b981', energy: state.solar },
                { name: "Consumidores 1° (Invertebrados)", w: 220, h: 45, y: 25, color: '#38bdf8', energy: state.solar * state.eff },
                { name: "Consumidores 2° (Truchas)", w: 140, h: 45, y: -30, color: '#fbbf24', energy: state.solar * Math.pow(state.eff, 2) },
                { name: "Ápice (Nutria Fluvial)", w: 60, h: 45, y: -85, color: '#f43f5e', energy: state.solar * Math.pow(state.eff, 3) }
            ];

            // Dibujar cada bloque tridimensional de la pirámide
            levels.forEach((lvl, idx) => {
                const hw = lvl.w / 2;
                const hh = lvl.h / 2;
                const hd = (lvl.w * 0.7) / 2;

                // 8 vértices del paralelepípedo
                const v = [
                    project(-hw, lvl.y - hh, -hd),
                    project(hw, lvl.y - hh, -hd),
                    project(hw, lvl.y - hh, hd),
                    project(-hw, lvl.y - hh, hd),
                    project(-hw, lvl.y + hh, -hd),
                    project(hw, lvl.y + hh, -hd),
                    project(hw, lvl.y + hh, hd),
                    project(-hw, lvl.y + hh, hd)
                ];

                // Cara frontal
                ctx.beginPath();
                ctx.moveTo(v[3].x, v[3].y);
                ctx.lineTo(v[2].x, v[2].y);
                ctx.lineTo(v[6].x, v[6].y);
                ctx.lineTo(v[7].x, v[7].y);
                ctx.closePath();
                ctx.fillStyle = lvl.color;
                ctx.globalAlpha = 0.85;
                ctx.fill();
                ctx.strokeStyle = '#fff';
                ctx.lineWidth = 1.2;
                ctx.stroke();

                // Cara superior
                ctx.beginPath();
                ctx.moveTo(v[0].x, v[0].y);
                ctx.lineTo(v[1].x, v[1].y);
                ctx.lineTo(v[2].x, v[2].y);
                ctx.lineTo(v[3].x, v[3].y);
                ctx.closePath();
                ctx.fillStyle = 'rgba(255, 255, 255, 0.25)';
                ctx.fill();
                ctx.stroke();

                // Cara lateral derecha
                ctx.beginPath();
                ctx.moveTo(v[2].x, v[2].y);
                ctx.lineTo(v[1].x, v[1].y);
                ctx.lineTo(v[5].x, v[5].y);
                ctx.lineTo(v[6].x, v[6].y);
                ctx.closePath();
                ctx.fillStyle = 'rgba(0, 0, 0, 0.35)';
                ctx.fill();
                ctx.stroke();

                // Texto etiqueta
                ctx.globalAlpha = 1.0;
                ctx.font = 'bold 11px JetBrains Mono';
                ctx.fillStyle = '#fff';
                const centerPr = project(0, lvl.y, hd + 5);
                ctx.fillText(`N${4 - idx}: ${Math.round(lvl.energy)} kcal`, centerPr.x - 45, centerPr.y + 4);
            });

            // Flujo energético ascendente (flechas de partículas que se reducen 90% en cada paso)
            ctx.fillStyle = '#f8fafc';
            for (let i = 0; i < 16; i++) {
                const py = 90 - ((t * 80 + i * 25) % 180);
                const progress = (90 - py) / 180;
                const flowWidth = 140 * (1 - progress * 0.7);
                const px = cx + Math.sin(t * 3 + i) * flowWidth * 0.3;
                ctx.beginPath();
                ctx.arc(px, cy + py * state.zoom, 2.5 * (1 - progress * 0.5), 0, Math.PI * 2);
                ctx.fill();
            }

            requestAnimationFrame(render);
        }
        render();

        function updateTelemetry() {
            const l1 = Math.round(state.solar);
            const l2 = Math.round(l1 * state.eff);
            const l3 = Math.round(l2 * state.eff);
            const l4 = Math.round(l3 * state.eff);

            document.getElementById('kpiL1').innerText = `${l1.toLocaleString()} kcal`;
            document.getElementById('kpiL2').innerText = `${l2.toLocaleString()} kcal`;
            document.getElementById('kpiL3').innerText = `${l3.toLocaleString()} kcal`;
            document.getElementById('kpiL4').innerText = `${l4.toLocaleString()} kcal`;

            let doVal = 9.2 - (state.nutr * 0.45);
            if (state.eutro) doVal = 2.1;
            document.getElementById('kpiDO').innerText = `${Math.max(1.0, doVal).toFixed(1)} mg/L`;

            const statusEl = document.getElementById('kpiStatus');
            if (doVal < 3.0) {
                statusEl.className = 'status-badge status-danger';
                statusEl.innerText = '🚨 Anoxia / Colapso Fluvial';
            } else if (state.overfish || state.nutr > 6.0) {
                statusEl.className = 'status-badge status-warning';
                statusEl.innerText = '⚠️ Desequilibrio Ecológico';
            } else {
                statusEl.className = 'status-badge status-healthy';
                statusEl.innerText = 'Equilibrio Trófico Estable';
            }
        }
        setInterval(updateTelemetry, 300);

        document.getElementById('rngSolar').addEventListener('input', (e) => {
            state.solar = parseInt(e.target.value);
            document.getElementById('valSolar').innerText = state.solar.toLocaleString() + ' kcal/m²';
        });

        document.getElementById('rngEff').addEventListener('input', (e) => {
            state.eff = parseFloat(e.target.value) / 100.0;
            document.getElementById('valEff').innerText = (state.eff * 100).toFixed(1) + ' %';
        });

        document.getElementById('rngNutr').addEventListener('input', (e) => {
            state.nutr = parseFloat(e.target.value);
            document.getElementById('valNutr').innerText = state.nutr.toFixed(1) + ' mg/L';
        });

        document.getElementById('btnEutro').addEventListener('click', () => {
            state.eutro = !state.eutro;
            state.nutr = state.eutro ? 12.0 : 2.4;
            document.getElementById('rngNutr').value = state.nutr;
            document.getElementById('valNutr').innerText = state.nutr.toFixed(1) + ' mg/L';
            if (state.eutro) speak("Alerta de eutrofización fluvial. El exceso de nitrógeno y fósforo causa una proliferación masiva de algas superficiales, bloqueando la luz y agotando el oxígeno disuelto en el lecho fluvial.");
        });

        document.getElementById('btnOverfish').addEventListener('click', () => {
            state.overfish = !state.overfish;
            if (state.overfish) speak("Sobreexplotación de carnívoros secundarios. La reducción drástica de truchas desencadena una explosión descontrolada de macroinvertebrados herbívoros.");
        });

        document.getElementById('btnBiomagn').addEventListener('click', () => {
            state.biomag = !state.biomag;
            speak("Principio de biomagnificación. Las toxinas no biodegradables como el mercurio se concentran diez veces en cada escalón trófico, alcanzando concentraciones letales en la nutria fluvial.");
        });

        document.getElementById('btnResetEco').addEventListener('click', () => {
            state.solar = 20000;
            state.eff = 0.10;
            state.nutr = 2.4;
            state.eutro = false;
            state.overfish = false;
            state.biomag = false;
            document.getElementById('rngSolar').value = 20000;
            document.getElementById('valSolar').innerText = '20.000 kcal/m²';
            document.getElementById('rngEff').value = 10.0;
            document.getElementById('valEff').innerText = '10.0 %';
            document.getElementById('rngNutr').value = 2.4;
            document.getElementById('valNutr').innerText = '2.4 mg/L';
            speak("Ecosistema fluvial restaurado a parámetros basales de equilibrio de Lindeman.");
        });

        document.getElementById('btnAudioToggle').addEventListener('click', (e) => {
            state.audioEnabled = !state.audioEnabled;
            e.target.innerText = state.audioEnabled ? '🔊 Sonido Río: ON' : '🔈 Sonido: OFF';
        });

        document.getElementById('btnVoiceGuide').addEventListener('click', () => {
            speak("Bienvenido al simulador de la Pirámide Trófica. Explora cómo el noventa por ciento de la energía química se disipa como calor metabólico entre cada nivel trófico.");
        });

        document.getElementById('btnResetView').addEventListener('click', () => {
            state.rotX = -0.25;
            state.rotY = 0.4;
            state.zoom = 1.0;
        });
    </script>
</body>
</html>
"""

# -----------------------------------------------------------------------------
# 3. SESIÓN 33: MITOCONDRIA: CENTRAL CELULAR Y ATP SINTASA 3D
# -----------------------------------------------------------------------------
def get_html_s33():
    return """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesión 33 • Mitocondria: Central Celular y Nanomotor ATP Sintasa 3D [COD-033]</title>
    <!-- NIH 3D • PDB 6J5I • Teoría Quimiosmótica de Peter Mitchell • Rotor F0 / Cabeza F1 -->
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #0a0414;
            --bg-panel: rgba(18, 8, 36, 0.94);
            --border: rgba(168, 85, 247, 0.35);
            --primary: #c084fc;
            --primary-glow: rgba(192, 132, 252, 0.4);
            --cyan: #38bdf8;
            --emerald: #34d399;
            --amber: #fbbf24;
            --rose: #f43f5e;
            --text-main: #f8fafc;
            --text-sub: #cbd5e1;
            --font-title: 'Cinzel', serif;
            --font-sans: 'Inter', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
        body {
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-sans);
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            font-size: 14px;
        }

        header {
            background: linear-gradient(180deg, rgba(14, 6, 28, 0.98) 0%, rgba(14, 6, 28, 0.88) 100%);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border);
            padding: 10px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-shrink: 0;
            z-index: 40;
        }
        .brand-box { display: flex; align-items: center; gap: 14px; }
        .badge-pill {
            background: rgba(192, 132, 252, 0.15);
            border: 1px solid var(--primary);
            color: var(--primary);
            font-family: var(--font-mono);
            font-weight: 800;
            font-size: 0.82rem;
            padding: 4px 10px;
            border-radius: 6px;
        }
        .title-text h1 {
            font-family: var(--font-title);
            font-size: 1.15rem;
            font-weight: 800;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .title-text p { font-size: 0.78rem; color: var(--text-sub); margin-top: 1px; }

        .header-actions { display: flex; align-items: center; gap: 10px; }
        .btn-header {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: var(--text-main);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .btn-header:hover { background: rgba(192, 132, 252, 0.2); border-color: var(--primary); color: #fff; }

        .workspace { flex: 1; position: relative; overflow: hidden; display: flex; }

        .viewer-container {
            flex: 1;
            position: relative;
            background: radial-gradient(circle at center, #1b0a33 0%, #06020c 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        #mitoCanvas {
            max-width: 96%;
            max-height: 92%;
            border-radius: 14px;
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.9);
            border: 1px solid rgba(192, 132, 252, 0.25);
            background: #080312;
            cursor: grab;
        }
        #mitoCanvas:active { cursor: grabbing; }

        .controls-panel {
            position: absolute;
            top: 18px;
            left: 20px;
            width: 350px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 18px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 14px;
            max-height: calc(100vh - 120px);
            overflow-y: auto;
        }

        .panel-sec-title {
            font-size: 0.78rem;
            font-family: var(--font-mono);
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 5px;
        }

        .slider-group { display: flex; flex-direction: column; gap: 6px; }
        .slider-label {
            display: flex;
            justify-content: space-between;
            font-size: 0.82rem;
            color: var(--text-sub);
        }
        .slider-val { font-family: var(--font-mono); color: #fff; font-weight: 700; }
        input[type="range"] {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: #1e293b;
            outline: none;
            cursor: pointer;
            accent-color: var(--primary);
        }

        .btn-group { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
        .btn-action {
            background: rgba(192, 132, 252, 0.12);
            border: 1px solid rgba(192, 132, 252, 0.35);
            color: #fff;
            padding: 9px 10px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }
        .btn-action:hover { background: rgba(192, 132, 252, 0.28); border-color: var(--primary); }
        .btn-action.active { background: var(--primary); color: #080312; font-weight: 800; }
        .btn-action.danger { background: rgba(244, 63, 94, 0.15); border-color: #f43f5e; color: #fca5a5; }
        .btn-action.danger:hover { background: #f43f5e; color: #fff; }

        .telemetry-card {
            position: absolute;
            bottom: 20px;
            right: 20px;
            width: 320px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 16px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .kpi-row { display: flex; justify-content: space-between; align-items: center; }
        .kpi-name { font-size: 0.78rem; color: var(--text-sub); }
        .kpi-val { font-family: var(--font-mono); font-size: 0.88rem; font-weight: 700; color: #fff; }
        .status-badge {
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.74rem;
            font-weight: 800;
            text-align: center;
        }
        .status-healthy { background: rgba(52, 211, 153, 0.2); color: #6ee7b7; border: 1px solid #34d399; }
        .status-warning { background: rgba(251, 191, 36, 0.2); color: #fde68a; border: 1px solid #fbbf24; }
        .status-danger { background: rgba(244, 63, 94, 0.2); color: #fda4af; border: 1px solid #f43f5e; }
    </style>
</head>
<body>
    <header>
        <div class="brand-box">
            <span class="badge-pill">[COD-033]</span>
            <div class="title-text">
                <h1>⚡ Mitocondria: Nanomotor ATP Sintasa 3D</h1>
                <p>NIH 3D • PDB 6J5I • Quimiosmosis de Peter Mitchell • Rotor F₀ (9.000 RPM) • Cabeza Catalítica F₁ α₃β₃</p>
            </div>
        </div>
        <div class="header-actions">
            <button class="btn-header" id="btnAudioToggle">🔊 Audio Motor: ON</button>
            <button class="btn-header" id="btnVoiceGuide">🗣️ Guía por Voz</button>
            <button class="btn-header" id="btnResetView">🎯 Centrar Vista</button>
        </div>
    </header>

    <div class="workspace">
        <div class="viewer-container">
            <canvas id="mitoCanvas" width="900" height="650"></canvas>
        </div>

        <div class="controls-panel">
            <div class="panel-sec-title">
                <span>Gradiente Electroquímico (Δp)</span>
                <span>🔋 QUIMIOSMOSIS</span>
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Potencial de Membrana (ΔΨm)</span>
                    <span class="slider-val" id="valVolt">-180 mV</span>
                </div>
                <input type="range" id="rngVolt" min="-220" max="-60" step="5" value="-180">
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Disponibilidad ADP + Pi</span>
                    <span class="slider-val" id="valADP">85 %</span>
                </div>
                <input type="range" id="rngADP" min="10" max="100" step="5" value="85">
            </div>

            <div class="panel-sec-title">
                <span>Inhibidores y Desacopladores</span>
                <span>🛑 FARMACOLOGÍA</span>
            </div>

            <div class="btn-group">
                <button class="btn-action danger" id="btnOligo">🧪 Oligomicina</button>
                <button class="btn-action danger" id="btnDNP">🔥 Desacoplador DNP</button>
            </div>

            <div class="btn-group">
                <button class="btn-action" id="btnBurstADP">⚡ Disparo de ATP</button>
                <button class="btn-action active" id="btnResetMito">🔄 Reset Óptimo</button>
            </div>
        </div>

        <div class="telemetry-card">
            <div class="panel-sec-title">
                <span>Cinética Molecular (PDB 6J5I)</span>
                <span>Peter Mitchell</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Velocidad del Rotor F₀:</span>
                <span class="kpi-val" id="kpiRPM">8.400 RPM</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Tasa Síntesis de ATP:</span>
                <span class="kpi-val" id="kpiATP">420 moléculas/s</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Flujo de Protones H⁺:</span>
                <span class="kpi-val" id="kpiProtons">1.260 H⁺/s</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Estado Quimiosmótico:</span>
                <span class="status-badge status-healthy" id="kpiStatus">Fosforilación Activa</span>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('mitoCanvas');
        const ctx = canvas.getContext('2d');

        let state = {
            volt: -180,
            adp: 85,
            inhibitor: 'none',
            rotorAngle: 0,
            rotX: -0.2,
            rotY: 0.35,
            zoom: 1.0,
            audioEnabled: true
        };

        // Web Audio - Zumbido rotacional del nanomotor a altas RPM
        let audioCtx = null;
        let motorOsc = null;
        let motorGain = null;

        function initMotorAudio() {
            if (!state.audioEnabled || motorOsc) return;
            try {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                motorOsc = audioCtx.createOscillator();
                motorGain = audioCtx.createGain();
                motorOsc.type = 'sawtooth';
                motorOsc.frequency.setValueAtTime(140, audioCtx.currentTime);
                motorGain.gain.setValueAtTime(0.015, audioCtx.currentTime);
                motorOsc.connect(motorGain);
                motorGain.connect(audioCtx.destination);
                motorOsc.start();
            } catch(e) {}
        }

        function updateMotorAudio(rpm) {
            if (!motorOsc || !audioCtx) return;
            const freq = Math.max(30, (rpm / 60) * 1.5);
            motorOsc.frequency.setTargetAtTime(freq, audioCtx.currentTime, 0.05);
            motorGain.gain.setTargetAtTime(state.audioEnabled ? 0.015 : 0.0, audioCtx.currentTime, 0.05);
        }

        function speak(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const u = new SpeechSynthesisUtterance(text);
                u.lang = 'es-ES';
                u.rate = 1.05;
                window.speechSynthesis.speak(u);
            }
        }

        // Interacción orbital con ratón
        let isDragging = false;
        let lastMouse = { x: 0, y: 0 };
        canvas.addEventListener('mousedown', (e) => {
            initMotorAudio();
            isDragging = true;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        window.addEventListener('mouseup', () => isDragging = false);
        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            const dx = e.clientX - lastMouse.x;
            const dy = e.clientY - lastMouse.y;
            state.rotY += dx * 0.008;
            state.rotX += dy * 0.008;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        canvas.addEventListener('wheel', (e) => {
            e.preventDefault();
            state.zoom *= e.deltaY > 0 ? 0.95 : 1.05;
            state.zoom = Math.max(0.6, Math.min(2.2, state.zoom));
        });

        // Loop de renderizado 3D de la ATP Sintasa
        let t = 0;
        function render() {
            t += 0.02;

            // Calcular velocidad rotacional en función de ΔΨm e inhibidores
            let targetRPM = 0;
            if (state.inhibitor === 'oligo') targetRPM = 0;
            else if (state.inhibitor === 'dnp') targetRPM = 600;
            else {
                const drivingForce = Math.abs(state.volt) / 180.0;
                targetRPM = 9000 * drivingForce * (state.adp / 100.0);
            }

            const rotSpeed = (targetRPM / 60) * 0.005;
            state.rotorAngle += rotSpeed;
            updateMotorAudio(targetRPM);

            ctx.clearRect(0, 0, canvas.width, canvas.height);

            const cx = canvas.width / 2;
            const cy = canvas.height / 2;

            const cosY = Math.cos(state.rotY);
            const sinY = Math.sin(state.rotY);
            const cosX = Math.cos(state.rotX);
            const sinX = Math.sin(state.rotX);

            function project(x, y, z) {
                let x1 = x * cosY + z * sinY;
                let z1 = -x * sinY + z * cosY;
                let y2 = y * cosX - z1 * sinX;
                let z2 = y * sinX + z1 * cosX;
                const fov = 450;
                const scale = (fov / (fov + z2 + 300)) * state.zoom;
                return { x: cx + x1 * scale, y: cy + y2 * scale, z: z2, scale: scale };
            }

            // Bicapa lipídica de la cresta mitocondrial (plano transversal)
            ctx.save();
            const pMemL = project(-240, -40, 0);
            const pMemR = project(240, -40, 0);
            ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
            ctx.lineWidth = 14 * state.zoom;
            ctx.beginPath();
            ctx.moveTo(pMemL.x, pMemL.y);
            ctx.lineTo(pMemR.x, pMemR.y);
            ctx.stroke();

            // Etiquetas de compartimentos
            ctx.font = 'bold 11px JetBrains Mono';
            ctx.fillStyle = '#38bdf8';
            ctx.fillText("ESPACIO INTERMEMBRANA [H⁺ ALTO]", cx - 180, cy - 140 * state.zoom);
            ctx.fillStyle = '#c084fc';
            ctx.fillText("MATRIZ MITOCONDRIAL [ATP SÍNTESIS]", cx - 180, cy + 180 * state.zoom);
            ctx.restore();

            // 1. Rotor F₀ (incrustado en membrana lipídica, gira con state.rotorAngle)
            const numSubunitsC = 10;
            const radiusF0 = 36;
            for (let i = 0; i < numSubunitsC; i++) {
                const ang = state.rotorAngle + (Math.PI * 2 / numSubunitsC) * i;
                const rx = Math.cos(ang) * radiusF0;
                const rz = Math.sin(ang) * radiusF0;
                const pr = project(rx, -40, rz);
                ctx.beginPath();
                ctx.arc(pr.x, pr.y, 8 * pr.scale, 0, Math.PI * 2);
                ctx.fillStyle = (i % 2 === 0) ? '#38bdf8' : '#0284c7';
                ctx.fill();
                ctx.strokeStyle = '#fff';
                ctx.lineWidth = 1;
                ctx.stroke();
            }

            // 2. Tallo central asimétrico γ-ε que conecta F₀ con F₁
            const pStemTop = project(0, -30, 0);
            const pStemBot = project(Math.sin(state.rotorAngle) * 8, 45, Math.cos(state.rotorAngle) * 8);
            ctx.beginPath();
            ctx.moveTo(pStemTop.x, pStemTop.y);
            ctx.lineTo(pStemBot.x, pStemBot.y);
            ctx.strokeStyle = '#fbbf24';
            ctx.lineWidth = 9 * state.zoom;
            ctx.stroke();

            // 3. Cabeza catalítica F₁ α₃β₃ (hexámero fijo en matriz)
            const numF1 = 6;
            const radiusF1 = 58;
            for (let j = 0; j < numF1; j++) {
                const f1Ang = (Math.PI * 2 / numF1) * j;
                const fx = Math.cos(f1Ang) * radiusF1;
                const fz = Math.sin(f1Ang) * radiusF1;
                const prF1 = project(fx, 65, fz);
                ctx.beginPath();
                ctx.arc(prF1.x, prF1.y, 16 * prF1.scale, 0, Math.PI * 2);
                ctx.fillStyle = (j % 2 === 0) ? '#c084fc' : '#a855f7';
                ctx.fill();
                ctx.strokeStyle = '#f8fafc';
                ctx.lineWidth = 1.5;
                ctx.stroke();

                // Letras α y β
                ctx.fillStyle = '#fff';
                ctx.font = 'bold 9px JetBrains Mono';
                ctx.fillText((j % 2 === 0) ? 'α' : 'β', prF1.x - 3, prF1.y + 3);
            }

            // 4. Estator periférico estático (brazo b₂ / OSCP exterior que evita la rotación de F₁)
            const pStatorTop = project(-radiusF0 - 18, -40, 0);
            const pStatorMid = project(-radiusF1 - 12, 20, 0);
            const pStatorBot = project(-radiusF1 - 4, 75, 0);
            ctx.beginPath();
            ctx.moveTo(pStatorTop.x, pStatorTop.y);
            ctx.lineTo(pStatorMid.x, pStatorMid.y);
            ctx.lineTo(pStatorBot.x, pStatorBot.y);
            ctx.strokeStyle = '#ef4444';
            ctx.lineWidth = 5 * state.zoom;
            ctx.stroke();

            // 5. Flujo de protones H⁺ atravesando el semicanal F₀ hacia la matriz
            if (targetRPM > 100) {
                ctx.fillStyle = '#34d399';
                for (let h = 0; h < 12; h++) {
                    const py = -100 + ((t * 120 + h * 22) % 180);
                    const prH = project(15 + Math.sin(h) * 12, py, Math.cos(h) * 12);
                    ctx.beginPath();
                    ctx.arc(prH.x, prH.y, 3 * prH.scale, 0, Math.PI * 2);
                    ctx.fill();
                }
            }

            // 6. Moléculas de ATP liberadas desde F₁ (estallido fosfórico)
            if (targetRPM > 1000) {
                ctx.fillStyle = '#fbbf24';
                for (let a = 0; a < 6; a++) {
                    const atpY = 85 + ((t * 80 + a * 30) % 120);
                    const prATP = project(Math.cos(a * 1.5) * 80, atpY, Math.sin(a * 1.5) * 80);
                    ctx.beginPath();
                    ctx.arc(prATP.x, prATP.y, 4 * prATP.scale, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.font = 'bold 8px JetBrains Mono';
                    ctx.fillText("ATP", prATP.x + 6, prATP.y + 3);
                }
            }

            requestAnimationFrame(render);
        }
        render();

        function updateTelemetry() {
            let rpm = 0;
            if (state.inhibitor === 'oligo') rpm = 0;
            else if (state.inhibitor === 'dnp') rpm = 450;
            else {
                const drivingForce = Math.abs(state.volt) / 180.0;
                rpm = Math.round(9000 * drivingForce * (state.adp / 100.0));
            }

            document.getElementById('kpiRPM').innerText = `${rpm.toLocaleString()} RPM`;
            const atpRate = Math.round((rpm / 60) * 3);
            document.getElementById('kpiATP').innerText = `${atpRate} moléc/s`;
            document.getElementById('kpiProtons').innerText = `${atpRate * 3} H⁺/s`;

            const statusEl = document.getElementById('kpiStatus');
            if (state.inhibitor === 'oligo') {
                statusEl.className = 'status-badge status-danger';
                statusEl.innerText = '🛑 Bloqueo F₀ (Oligomicina)';
            } else if (state.inhibitor === 'dnp') {
                statusEl.className = 'status-badge status-warning';
                statusEl.innerText = '🔥 Desacoplado DNP (Calor)';
            } else if (rpm > 7000) {
                statusEl.className = 'status-badge status-healthy';
                statusEl.innerText = 'Fosforilación Óptima (9 krpm)';
            } else {
                statusEl.className = 'status-badge status-warning';
                statusEl.innerText = 'Baja Tasa Respiratoria';
            }
        }
        setInterval(updateTelemetry, 250);

        document.getElementById('rngVolt').addEventListener('input', (e) => {
            state.volt = parseInt(e.target.value);
            document.getElementById('valVolt').innerText = state.volt + ' mV';
        });

        document.getElementById('rngADP').addEventListener('input', (e) => {
            state.adp = parseInt(e.target.value);
            document.getElementById('valADP').innerText = state.adp + ' %';
        });

        document.getElementById('btnOligo').addEventListener('click', () => {
            state.inhibitor = (state.inhibitor === 'oligo') ? 'none' : 'oligo';
            if (state.inhibitor === 'oligo') speak("Inhibición por oligomicina. La toxina ocluye físicamente el canal F cero transmembrana, deteniendo la rotación mecánica del motor mitocondrial.");
        });

        document.getElementById('btnDNP').addEventListener('click', () => {
            state.inhibitor = (state.inhibitor === 'dnp') ? 'none' : 'dnp';
            if (state.inhibitor === 'dnp') speak("Desacoplamiento quimiosmótico con DNP. Los protones cruzan libremente la membrana interna sin pasar por la ATP sintasa, disipando la energía como calor sin sintetizar ATP.");
        });

        document.getElementById('btnBurstADP').addEventListener('click', () => {
            state.adp = 100;
            state.volt = -210;
            state.inhibitor = 'none';
            document.getElementById('rngVolt').value = -210;
            document.getElementById('valVolt').innerText = '-210 mV';
            document.getElementById('rngADP').value = 100;
            document.getElementById('valADP').innerText = '100 %';
            speak("Disparo masivo de ADP y sustrato fosfórico. Rotación catalítica acelerada al máximo fisiológico.");
        });

        document.getElementById('btnResetMito').addEventListener('click', () => {
            state.volt = -180;
            state.adp = 85;
            state.inhibitor = 'none';
            document.getElementById('rngVolt').value = -180;
            document.getElementById('valVolt').innerText = '-180 mV';
            document.getElementById('rngADP').value = 85;
            document.getElementById('valADP').innerText = '85 %';
            speak("Mitocondria restablecida a parámetros fisiológicos normales.");
        });

        document.getElementById('btnAudioToggle').addEventListener('click', (e) => {
            state.audioEnabled = !state.audioEnabled;
            e.target.innerText = state.audioEnabled ? '🔊 Audio Motor: ON' : '🔈 Audio: OFF';
        });

        document.getElementById('btnVoiceGuide').addEventListener('click', () => {
            speak("Bienvenido al simulador tridimensional del nanomotor molecular ATP Sintasa. Observa el anillo de protones F cero en la membrana y la cabeza catalítica F uno en la matriz mitocondrial.");
        });

        document.getElementById('btnResetView').addEventListener('click', () => {
            state.rotX = -0.2;
            state.rotY = 0.35;
            state.zoom = 1.0;
        });
    </script>
</body>
</html>
"""

print("Módulos S31, S32 y S33 preparados.")

# -----------------------------------------------------------------------------
# 4. SESIÓN 34: TELÓMEROS CROMOSÓMICOS, TELOMERASA Y LÍMITE DE HAYFLICK 3D
# -----------------------------------------------------------------------------
def get_html_s34():
    return """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesión 34 • Telómeros Cromosómicos, Telomerasa y Límite de Hayflick 3D [COD-034]</title>
    <!-- Nobel Blackburn & Greider • PDB 6D6V • Repeticiones TTAGGG • Complejo Shelterin -->
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #030a14;
            --bg-panel: rgba(8, 20, 38, 0.94);
            --border: rgba(56, 189, 248, 0.35);
            --primary: #38bdf8;
            --primary-glow: rgba(56, 189, 248, 0.4);
            --telomere: #f43f5e;
            --t-active: #34d399;
            --amber: #fbbf24;
            --text-main: #f8fafc;
            --text-sub: #cbd5e1;
            --font-title: 'Cinzel', serif;
            --font-sans: 'Inter', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
        body {
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-sans);
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            font-size: 14px;
        }

        header {
            background: linear-gradient(180deg, rgba(6, 16, 32, 0.98) 0%, rgba(6, 16, 32, 0.88) 100%);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border);
            padding: 10px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-shrink: 0;
            z-index: 40;
        }
        .brand-box { display: flex; align-items: center; gap: 14px; }
        .badge-pill {
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid var(--primary);
            color: var(--primary);
            font-family: var(--font-mono);
            font-weight: 800;
            font-size: 0.82rem;
            padding: 4px 10px;
            border-radius: 6px;
        }
        .title-text h1 {
            font-family: var(--font-title);
            font-size: 1.15rem;
            font-weight: 800;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .title-text p { font-size: 0.78rem; color: var(--text-sub); margin-top: 1px; }

        .header-actions { display: flex; align-items: center; gap: 10px; }
        .btn-header {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: var(--text-main);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .btn-header:hover { background: rgba(56, 189, 248, 0.2); border-color: var(--primary); color: #fff; }

        .workspace { flex: 1; position: relative; overflow: hidden; display: flex; }

        .viewer-container {
            flex: 1;
            position: relative;
            background: radial-gradient(circle at center, #0a2540 0%, #030a14 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        #teloCanvas {
            max-width: 96%;
            max-height: 92%;
            border-radius: 14px;
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.9);
            border: 1px solid rgba(56, 189, 248, 0.25);
            background: #04101e;
            cursor: grab;
        }
        #teloCanvas:active { cursor: grabbing; }

        .controls-panel {
            position: absolute;
            top: 18px;
            left: 20px;
            width: 350px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 18px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 14px;
            max-height: calc(100vh - 120px);
            overflow-y: auto;
        }

        .panel-sec-title {
            font-size: 0.78rem;
            font-family: var(--font-mono);
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 5px;
        }

        .slider-group { display: flex; flex-direction: column; gap: 6px; }
        .slider-label {
            display: flex;
            justify-content: space-between;
            font-size: 0.82rem;
            color: var(--text-sub);
        }
        .slider-val { font-family: var(--font-mono); color: #fff; font-weight: 700; }
        input[type="range"] {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: #1e293b;
            outline: none;
            cursor: pointer;
            accent-color: var(--primary);
        }

        .btn-group { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
        .btn-action {
            background: rgba(56, 189, 248, 0.12);
            border: 1px solid rgba(56, 189, 248, 0.35);
            color: #fff;
            padding: 9px 10px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }
        .btn-action:hover { background: rgba(56, 189, 248, 0.28); border-color: var(--primary); }
        .btn-action.active { background: var(--primary); color: #04101e; font-weight: 800; }
        .btn-action.danger { background: rgba(244, 63, 94, 0.15); border-color: #f43f5e; color: #fca5a5; }
        .btn-action.danger:hover { background: #f43f5e; color: #fff; }

        .telemetry-card {
            position: absolute;
            bottom: 20px;
            right: 20px;
            width: 320px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 16px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .kpi-row { display: flex; justify-content: space-between; align-items: center; }
        .kpi-name { font-size: 0.78rem; color: var(--text-sub); }
        .kpi-val { font-family: var(--font-mono); font-size: 0.88rem; font-weight: 700; color: #fff; }
        .status-badge {
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.74rem;
            font-weight: 800;
            text-align: center;
        }
        .status-healthy { background: rgba(52, 211, 153, 0.2); color: #6ee7b7; border: 1px solid #34d399; }
        .status-warning { background: rgba(251, 191, 36, 0.2); color: #fde68a; border: 1px solid #fbbf24; }
        .status-danger { background: rgba(244, 63, 94, 0.2); color: #fda4af; border: 1px solid #f43f5e; }
    </style>
</head>
<body>
    <header>
        <div class="brand-box">
            <span class="badge-pill">[COD-034]</span>
            <div class="title-text">
                <h1>🧬 Telómeros Cromosómicos & Límite de Hayflick 3D</h1>
                <p>Blackburn & Greider (Premio Nobel) • PDB 6D6V • Casquetes TTAGGG • Ribonucleoproteína Telomerasa • Senescencia</p>
            </div>
        </div>
        <div class="header-actions">
            <button class="btn-header" id="btnAudioToggle">🔊 Audio Pulso: ON</button>
            <button class="btn-header" id="btnVoiceGuide">🗣️ Guía por Voz</button>
            <button class="btn-header" id="btnResetView">🎯 Centrar Vista</button>
        </div>
    </header>

    <div class="workspace">
        <div class="viewer-container">
            <canvas id="teloCanvas" width="900" height="650"></canvas>
        </div>

        <div class="controls-panel">
            <div class="panel-sec-title">
                <span>Reloj Biológico Replicativo</span>
                <span>⏱️ HAYFLICK</span>
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Divisiones Celulares Acumuladas</span>
                    <span class="slider-val" id="valDivs">15 / 60</span>
                </div>
                <input type="range" id="rngDivs" min="0" max="65" step="1" value="15">
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Estrés Oxidativo (ROS)</span>
                    <span class="slider-val" id="valOx">Bajo (1.0x)</span>
                </div>
                <input type="range" id="rngOx" min="1.0" max="3.0" step="0.2" value="1.0">
            </div>

            <div class="panel-sec-title">
                <span>Enzima Telomerasa (hTERT + hTR)</span>
                <span>🔬 INMORTALIDAD</span>
            </div>

            <div class="btn-group">
                <button class="btn-action" id="btnTelomerase">⚡ Activar Telomerasa</button>
                <button class="btn-action danger" id="btnHayflick">🛑 Forzar Senescencia</button>
            </div>

            <div class="btn-group">
                <button class="btn-action" id="btnDivide">+1 División Celular</button>
                <button class="btn-action active" id="btnResetTelo">🔄 Célula Embrionaria</button>
            </div>
        </div>

        <div class="telemetry-card">
            <div class="panel-sec-title">
                <span>Telemetría Genómica</span>
                <span>PDB 6D6V</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Longitud Telomérica:</span>
                <span class="kpi-val" id="kpiKb">11.8 kilobases (kb)</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Repeticiones TTAGGG:</span>
                <span class="kpi-val" id="kpiReps">~1.960 hexámeros</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Integridad del Bucle T-loop:</span>
                <span class="kpi-val" id="kpiShelterin">Shelterin Estable</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Estado Proliferativo:</span>
                <span class="status-badge status-healthy" id="kpiStatus">Célula Competente</span>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('teloCanvas');
        const ctx = canvas.getContext('2d');

        let state = {
            divs: 15,
            maxDivs: 55,
            ox: 1.0,
            telomeraseActive: false,
            rotX: -0.2,
            rotY: 0.35,
            zoom: 1.0,
            audioEnabled: true
        };

        let audioCtx = null;
        function playBeep(freq, dur) {
            if (!state.audioEnabled) return;
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.03, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + dur);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + dur);
            } catch(e) {}
        }

        function speak(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const u = new SpeechSynthesisUtterance(text);
                u.lang = 'es-ES';
                u.rate = 1.05;
                window.speechSynthesis.speak(u);
            }
        }

        let isDragging = false;
        let lastMouse = { x: 0, y: 0 };
        canvas.addEventListener('mousedown', (e) => {
            isDragging = true;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        window.addEventListener('mouseup', () => isDragging = false);
        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            const dx = e.clientX - lastMouse.x;
            const dy = e.clientY - lastMouse.y;
            state.rotY += dx * 0.008;
            state.rotX += dy * 0.008;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        canvas.addEventListener('wheel', (e) => {
            e.preventDefault();
            state.zoom *= e.deltaY > 0 ? 0.95 : 1.05;
            state.zoom = Math.max(0.6, Math.min(2.2, state.zoom));
        });

        // Loop de renderizado 3D de Cromosoma Metafásico y Telómeros
        let t = 0;
        function render() {
            t += 0.02;
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            const cx = canvas.width / 2;
            const cy = canvas.height / 2;

            const cosY = Math.cos(state.rotY);
            const sinY = Math.sin(state.rotY);
            const cosX = Math.cos(state.rotX);
            const sinX = Math.sin(state.rotX);

            function project(x, y, z) {
                let x1 = x * cosY + z * sinY;
                let z1 = -x * sinY + z * cosY;
                let y2 = y * cosX - z1 * sinX;
                let z2 = y * sinX + z1 * cosX;
                const fov = 450;
                const scale = (fov / (fov + z2 + 300)) * state.zoom;
                return { x: cx + x1 * scale, y: cy + y2 * scale, z: z2, scale: scale };
            }

            // Calcular longitud telomérica en función de divisiones y telomerasa
            let kbRemain = 15.0 - (state.divs * 0.22 * state.ox);
            if (state.telomeraseActive) kbRemain = 14.5;
            kbRemain = Math.max(1.8, kbRemain);

            const telomereFrac = Math.max(0.08, (kbRemain - 1.8) / (15.0 - 1.8));

            // 4 Brazos cromosómicos (brazos p superiores y q inferiores con cromátidas hermanas)
            const arms = [
                { start: [0, 0, -10], end: [-90, -170, -25], isP: true },
                { start: [0, 0, 10], end: [90, -170, 25], isP: true },
                { start: [0, 0, -10], end: [-110, 180, -30], isP: false },
                { start: [0, 0, 10], end: [110, 180, 30], isP: false }
            ];

            // Dibujar brazos cromosómicos de cromatina condensada
            arms.forEach(a => {
                const p0 = project(a.start[0], a.start[1], a.start[2]);
                const p1 = project(a.end[0], a.end[1], a.end[2]);

                // Cuerpo de cromátida
                ctx.beginPath();
                ctx.moveTo(p0.x, p0.y);
                ctx.lineTo(p1.x, p1.y);
                ctx.strokeStyle = '#38bdf8';
                ctx.lineWidth = 26 * state.zoom;
                ctx.lineCap = 'round';
                ctx.stroke();

                // Detalle trabecular / bandas G de Giemsa
                ctx.beginPath();
                ctx.moveTo(p0.x, p0.y);
                ctx.lineTo(p1.x, p1.y);
                ctx.strokeStyle = 'rgba(14, 116, 144, 0.4)';
                ctx.lineWidth = 14 * state.zoom;
                ctx.stroke();

                // Telómeros en los extremos terminales (Casquetes TTAGGG)
                const teloLen = 32 * telomereFrac * state.zoom;
                const dirX = (a.end[0] - a.start[0]);
                const dirY = (a.end[1] - a.start[1]);
                const dirZ = (a.end[2] - a.start[2]);
                const len = Math.hypot(dirX, dirY, dirZ);

                const tStart = project(a.end[0] - (dirX / len) * teloLen, a.end[1] - (dirY / len) * teloLen, a.end[2] - (dirZ / len) * teloLen);
                const tEnd = p1;

                ctx.beginPath();
                ctx.moveTo(tStart.x, tStart.y);
                ctx.lineTo(tEnd.x, tEnd.y);
                ctx.strokeStyle = state.telomeraseActive ? '#34d399' : (telomereFrac < 0.25 ? '#f43f5e' : '#fb7185');
                ctx.lineWidth = 28 * state.zoom;
                ctx.stroke();

                // Resplandor fluorescente del telómero
                ctx.beginPath();
                ctx.arc(tEnd.x, tEnd.y, (8 + Math.sin(t * 3) * 2) * state.zoom, 0, Math.PI * 2);
                ctx.fillStyle = state.telomeraseActive ? 'rgba(52, 211, 153, 0.8)' : (telomereFrac < 0.25 ? 'rgba(244, 63, 94, 0.9)' : 'rgba(251, 113, 133, 0.8)');
                ctx.fill();
            });

            // Centrómero central condensado (constricción primaria con cinetocoro)
            const pCen = project(0, 0, 0);
            ctx.beginPath();
            ctx.arc(pCen.x, pCen.y, 16 * state.zoom, 0, Math.PI * 2);
            ctx.fillStyle = '#0284c7';
            ctx.fill();
            ctx.strokeStyle = '#fff';
            ctx.lineWidth = 1.5;
            ctx.stroke();

            // Telomerasa si está activa: complejo enzimático acoplado a un extremo
            if (state.telomeraseActive) {
                const pEnzyme = project(-95 + Math.sin(t * 4) * 5, -175 + Math.cos(t * 4) * 5, -25);
                ctx.beginPath();
                ctx.arc(pEnzyme.x, pEnzyme.y, 18 * state.zoom, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(52, 211, 153, 0.85)';
                ctx.fill();
                ctx.strokeStyle = '#fff';
                ctx.lineWidth = 2;
                ctx.stroke();

                ctx.font = 'bold 9px JetBrains Mono';
                ctx.fillStyle = '#04101e';
                ctx.fillText("hTERT", pEnzyme.x - 14, pEnzyme.y + 3);
            }

            requestAnimationFrame(render);
        }
        render();

        function updateTelemetry() {
            let kb = 15.0 - (state.divs * 0.22 * state.ox);
            if (state.telomeraseActive) kb = 14.5;
            kb = Math.max(1.8, kb);

            document.getElementById('kpiKb').innerText = `${kb.toFixed(1)} kb`;
            const reps = Math.round((kb * 1000) / 6);
            document.getElementById('kpiReps').innerText = `~${reps.toLocaleString()} hexámeros`;

            const statusEl = document.getElementById('kpiStatus');
            const shelterinEl = document.getElementById('kpiShelterin');

            if (state.telomeraseActive) {
                statusEl.className = 'status-badge status-healthy';
                statusEl.innerText = 'Inmortalizada / Célula Madre';
                shelterinEl.innerText = 'Elongación de ADN Activa';
            } else if (kb <= 3.5) {
                statusEl.className = 'status-badge status-danger';
                statusEl.innerText = '🛑 Senescencia Replicativa (Hayflick)';
                shelterinEl.innerText = 'Colapso Shelterin / Daño ADN';
            } else if (kb <= 6.0) {
                statusEl.className = 'status-badge status-warning';
                statusEl.innerText = '⚠️ Envejecimiento Celular Avanzado';
                shelterinEl.innerText = 'T-loop Inestable';
            } else {
                statusEl.className = 'status-badge status-healthy';
                statusEl.innerText = 'Célula Mitótica Competente';
                shelterinEl.innerText = 'Shelterin Estable';
            }
        }
        setInterval(updateTelemetry, 250);

        document.getElementById('rngDivs').addEventListener('input', (e) => {
            state.divs = parseInt(e.target.value);
            document.getElementById('valDivs').innerText = `${state.divs} / 60`;
            playBeep(440 - state.divs * 4, 0.08);
        });

        document.getElementById('rngOx').addEventListener('input', (e) => {
            state.ox = parseFloat(e.target.value);
            document.getElementById('valOx').innerText = `${state.ox.toFixed(1)}x`;
        });

        document.getElementById('btnDivide').addEventListener('click', () => {
            if (state.divs < 65) {
                state.divs++;
                document.getElementById('rngDivs').value = state.divs;
                document.getElementById('valDivs').innerText = `${state.divs} / 60`;
                playBeep(520, 0.12);
            }
        });

        document.getElementById('btnTelomerase').addEventListener('click', () => {
            state.telomeraseActive = !state.telomeraseActive;
            const btn = document.getElementById('btnTelomerase');
            btn.classList.toggle('active', state.telomeraseActive);
            btn.innerText = state.telomeraseActive ? '🟢 Telomerasa Activada' : '⚡ Activar Telomerasa';
            if (state.telomeraseActive) speak("Ribonucleoproteína telomerasa activada. La enzima añade repeticiones hexaméricas TTAGGG en los extremos tres prima, superando el límite replicativo de Hayflick.");
        });

        document.getElementById('btnHayflick').addEventListener('click', () => {
            state.divs = 55;
            state.telomeraseActive = false;
            document.getElementById('rngDivs').value = 55;
            document.getElementById('valDivs').innerText = '55 / 60';
            document.getElementById('btnTelomerase').classList.remove('active');
            document.getElementById('btnTelomerase').innerText = '⚡ Activar Telomerasa';
            speak("Límite de Leonard Hayflick alcanzado. Los telómeros se han acortado por debajo de cuatro kilobases, desencadenando la respuesta de daño al ADN mediada por la proteína p53 y provocando la senescencia celular irreversible.");
        });

        document.getElementById('btnResetTelo').addEventListener('click', () => {
            state.divs = 0;
            state.ox = 1.0;
            state.telomeraseActive = false;
            document.getElementById('rngDivs').value = 0;
            document.getElementById('valDivs').innerText = '0 / 60';
            document.getElementById('rngOx').value = 1.0;
            document.getElementById('valOx').innerText = 'Bajo (1.0x)';
            document.getElementById('btnTelomerase').classList.remove('active');
            document.getElementById('btnTelomerase').innerText = '⚡ Activar Telomerasa';
            speak("Célula restablecida a estadio cigoto embrionario con quince kilobases completas de telómeros.");
        });

        document.getElementById('btnAudioToggle').addEventListener('click', (e) => {
            state.audioEnabled = !state.audioEnabled;
            e.target.innerText = state.audioEnabled ? '🔊 Audio Pulso: ON' : '🔈 Audio: OFF';
        });

        document.getElementById('btnVoiceGuide').addEventListener('click', () => {
            speak("Bienvenido al simulador tridimensional de Telómeros Cromosómicos. Observa los casquetes terminales fluorescentes que protegen el ADN de la degradación durante la división celular.");
        });

        document.getElementById('btnResetView').addEventListener('click', () => {
            state.rotX = -0.2;
            state.rotY = 0.35;
            state.zoom = 1.0;
        });
    </script>
</body>
</html>
"""

# -----------------------------------------------------------------------------
# 5. SESIÓN 35: BIOMA DE SELVA TROPICAL: ESTRATOS DE ALTURA 3D
# -----------------------------------------------------------------------------
def get_html_s35():
    return """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesión 35 • Bioma de Selva Tropical: Estratos de Altura 3D [COD-035]</title>
    <!-- Smithsonian Tropical Research Institute (STRI) • Perfil de 50m • Dosel (Canopy) • Ríos Voladores -->
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #010d06;
            --bg-panel: rgba(4, 24, 14, 0.94);
            --border: rgba(52, 211, 153, 0.35);
            --primary: #34d399;
            --primary-glow: rgba(52, 211, 153, 0.4);
            --amber: #fbbf24;
            --cyan: #38bdf8;
            --text-main: #f8fafc;
            --text-sub: #cbd5e1;
            --font-title: 'Cinzel', serif;
            --font-sans: 'Inter', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
        body {
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-sans);
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            font-size: 14px;
        }

        header {
            background: linear-gradient(180deg, rgba(2, 20, 10, 0.98) 0%, rgba(2, 20, 10, 0.88) 100%);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border);
            padding: 10px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-shrink: 0;
            z-index: 40;
        }
        .brand-box { display: flex; align-items: center; gap: 14px; }
        .badge-pill {
            background: rgba(52, 211, 153, 0.15);
            border: 1px solid var(--primary);
            color: var(--primary);
            font-family: var(--font-mono);
            font-weight: 800;
            font-size: 0.82rem;
            padding: 4px 10px;
            border-radius: 6px;
        }
        .title-text h1 {
            font-family: var(--font-title);
            font-size: 1.15rem;
            font-weight: 800;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .title-text p { font-size: 0.78rem; color: var(--text-sub); margin-top: 1px; }

        .header-actions { display: flex; align-items: center; gap: 10px; }
        .btn-header {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: var(--text-main);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .btn-header:hover { background: rgba(52, 211, 153, 0.2); border-color: var(--primary); color: #fff; }

        .workspace { flex: 1; position: relative; overflow: hidden; display: flex; }

        .viewer-container {
            flex: 1;
            position: relative;
            background: radial-gradient(circle at center, #072a15 0%, #010d06 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        #jungleCanvas {
            max-width: 96%;
            max-height: 92%;
            border-radius: 14px;
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.9);
            border: 1px solid rgba(52, 211, 153, 0.25);
            background: #021208;
            cursor: grab;
        }
        #jungleCanvas:active { cursor: grabbing; }

        .controls-panel {
            position: absolute;
            top: 18px;
            left: 20px;
            width: 350px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 18px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 14px;
            max-height: calc(100vh - 120px);
            overflow-y: auto;
        }

        .panel-sec-title {
            font-size: 0.78rem;
            font-family: var(--font-mono);
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 5px;
        }

        .slider-group { display: flex; flex-direction: column; gap: 6px; }
        .slider-label {
            display: flex;
            justify-content: space-between;
            font-size: 0.82rem;
            color: var(--text-sub);
        }
        .slider-val { font-family: var(--font-mono); color: #fff; font-weight: 700; }
        input[type="range"] {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: #1e293b;
            outline: none;
            cursor: pointer;
            accent-color: var(--primary);
        }

        .btn-group { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
        .btn-action {
            background: rgba(52, 211, 153, 0.12);
            border: 1px solid rgba(52, 211, 153, 0.35);
            color: #fff;
            padding: 9px 10px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }
        .btn-action:hover { background: rgba(52, 211, 153, 0.28); border-color: var(--primary); }
        .btn-action.active { background: var(--primary); color: #010d06; font-weight: 800; }

        .telemetry-card {
            position: absolute;
            bottom: 20px;
            right: 20px;
            width: 320px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 16px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .kpi-row { display: flex; justify-content: space-between; align-items: center; }
        .kpi-name { font-size: 0.78rem; color: var(--text-sub); }
        .kpi-val { font-family: var(--font-mono); font-size: 0.88rem; font-weight: 700; color: #fff; }
        .status-badge {
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.74rem;
            font-weight: 800;
            text-align: center;
        }
        .status-healthy { background: rgba(52, 211, 153, 0.2); color: #6ee7b7; border: 1px solid #34d399; }
        .status-canopy { background: rgba(56, 189, 248, 0.2); color: #7dd3fc; border: 1px solid #38bdf8; }
        .status-floor { background: rgba(251, 191, 36, 0.2); color: #fde68a; border: 1px solid #fbbf24; }
    </style>
</head>
<body>
    <header>
        <div class="brand-box">
            <span class="badge-pill">[COD-035]</span>
            <div class="title-text">
                <h1>🌴 Bioma de Selva Tropical: Estratos de Altura 3D</h1>
                <p>Smithsonian Tropical Research Institute (STRI) • Perfil Vertical de 50 Metros • Dosel Arbóreo (Canopy) • Ríos Voladores</p>
            </div>
        </div>
        <div class="header-actions">
            <button class="btn-header" id="btnAudioToggle">🔊 Sonidos Selva: ON</button>
            <button class="btn-header" id="btnVoiceGuide">🗣️ Guía por Voz</button>
            <button class="btn-header" id="btnResetView">🎯 Centrar Vista</button>
        </div>
    </header>

    <div class="workspace">
        <div class="viewer-container">
            <canvas id="jungleCanvas" width="900" height="650"></canvas>
        </div>

        <div class="controls-panel">
            <div class="panel-sec-title">
                <span>Elevador Bioclimático</span>
                <span>📶 ALTÍMETRO</span>
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Cota de Altura (Z)</span>
                    <span class="slider-val" id="valAlt">32 m (Dosel / Canopy)</span>
                </div>
                <input type="range" id="rngAlt" min="0" max="50" step="1" value="32">
            </div>

            <div class="panel-sec-title">
                <span>Fenómenos Atmosféricos</span>
                <span>🌧️ METEOROLOGÍA</span>
            </div>

            <div class="btn-group">
                <button class="btn-action" id="btnRain">🌧️ Lluvia Monzónica</button>
                <button class="btn-action active" id="btnRivers">☁️ Ríos Voladores</button>
            </div>

            <div class="btn-group">
                <button class="btn-action" id="btnCanopyJump">🐒 Salto al Dosel</button>
                <button class="btn-action" id="btnFloorJump">🐜 Suelo Húmedo</button>
            </div>
        </div>

        <div class="telemetry-card">
            <div class="panel-sec-title">
                <span>Microclima In-Situ (STRI)</span>
                <span>Torre de Grúa Biológica</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Estrato Actual:</span>
                <span class="status-badge status-canopy" id="kpiStratum">Dosel Continuo (Canopy)</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Radiación Solar (PAR):</span>
                <span class="kpi-val" id="kpiPAR">68 % (1.350 µmol)</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Humedad Relativa:</span>
                <span class="kpi-val" id="kpiHum">78 %</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Temperatura:</span>
                <span class="kpi-val" id="kpiTemp">28.4 °C</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Viento:</span>
                <span class="kpi-val" id="kpiWind">6.2 km/h</span>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('jungleCanvas');
        const ctx = canvas.getContext('2d');

        let state = {
            alt: 32,
            rain: false,
            rivers: true,
            rotX: -0.15,
            rotY: 0.3,
            zoom: 1.0,
            audioEnabled: true
        };

        let audioCtx = null;
        function playJungleSounds() {
            if (!state.audioEnabled) return;
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(1200 + Math.random() * 800, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.015, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.3);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.3);
            } catch(e) {}
        }
        setInterval(playJungleSounds, 1800);

        function speak(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const u = new SpeechSynthesisUtterance(text);
                u.lang = 'es-ES';
                u.rate = 1.05;
                window.speechSynthesis.speak(u);
            }
        }

        let isDragging = false;
        let lastMouse = { x: 0, y: 0 };
        canvas.addEventListener('mousedown', (e) => {
            isDragging = true;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        window.addEventListener('mouseup', () => isDragging = false);
        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            const dx = e.clientX - lastMouse.x;
            const dy = e.clientY - lastMouse.y;
            state.rotY += dx * 0.008;
            state.rotX += dy * 0.008;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        canvas.addEventListener('wheel', (e) => {
            e.preventDefault();
            state.zoom *= e.deltaY > 0 ? 0.95 : 1.05;
            state.zoom = Math.max(0.6, Math.min(2.0, state.zoom));
        });

        // Loop de renderizado 3D de la Torre de Selva Tropical
        let t = 0;
        function render() {
            t += 0.02;
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            const cx = canvas.width / 2;
            const cy = canvas.height / 2;

            const cosY = Math.cos(state.rotY);
            const sinY = Math.sin(state.rotY);
            const cosX = Math.cos(state.rotX);
            const sinX = Math.sin(state.rotX);

            function project(x, y, z) {
                let x1 = x * cosY + z * sinY;
                let z1 = -x * sinY + z * cosY;
                let y2 = y * cosX - z1 * sinX;
                let z2 = y * sinX + z1 * cosX;
                const fov = 450;
                const scale = (fov / (fov + z2 + 300)) * state.zoom;
                return { x: cx + x1 * scale, y: cy + y2 * scale, z: z2, scale: scale };
            }

            // Los 4 Estratos ecológicos verticales (0 a 50m)
            // Y: 0 m = 190 px (Suelo) -> 50 m = -190 px (Emergente)
            const hScale = (m) => 190 - (m / 50.0) * 380;

            // 1. Suelo del bosque (0 a 5m)
            const pFloorL = project(-180, hScale(0), 0);
            const pFloorR = project(180, hScale(0), 0);
            ctx.strokeStyle = '#3f2e18';
            ctx.lineWidth = 18 * state.zoom;
            ctx.beginPath();
            ctx.moveTo(pFloorL.x, pFloorL.y);
            ctx.lineTo(pFloorR.x, pFloorR.y);
            ctx.stroke();

            // 2. Tronco central majestuoso (Ceiba pentandra con raíces tabulares)
            const pTrunkBot = project(0, hScale(0), 0);
            const pTrunkTop = project(0, hScale(48), 0);
            ctx.beginPath();
            ctx.moveTo(pTrunkBot.x, pTrunkBot.y);
            ctx.lineTo(pTrunkTop.x, pTrunkTop.y);
            ctx.strokeStyle = '#523a22';
            ctx.lineWidth = 22 * state.zoom;
            ctx.stroke();

            // Raíces tabulares (buttress roots) en el suelo
            const pRoot1 = project(-50, hScale(0), 20);
            const pRoot2 = project(50, hScale(0), -20);
            ctx.beginPath();
            ctx.moveTo(pTrunkBot.x, pTrunkBot.y);
            ctx.lineTo(pRoot1.x, pRoot1.y);
            ctx.moveTo(pTrunkBot.x, pTrunkBot.y);
            ctx.lineTo(pRoot2.x, pRoot2.y);
            ctx.strokeStyle = '#3f2e18';
            ctx.lineWidth = 10 * state.zoom;
            ctx.stroke();

            // 3. Estrato del Sotobosque / Understory (5 - 20 m)
            for (let u = 0; u < 5; u++) {
                const uy = hScale(8 + u * 2.5);
                const ux = (u % 2 === 0 ? -60 : 60);
                const pLeaf = project(ux, uy, Math.sin(u) * 30);
                ctx.beginPath();
                ctx.arc(pLeaf.x, pLeaf.y, (14 + u * 2) * state.zoom, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(16, 185, 129, 0.7)';
                ctx.fill();
            }

            // 4. Dosel Continuo / Canopy (20 - 40 m) - Techo denso con 80% biodiversidad
            for (let c = 0; c < 8; c++) {
                const cyNode = hScale(25 + Math.sin(c) * 8);
                const cxNode = Math.cos(c * 0.8) * 110;
                const czNode = Math.sin(c * 0.8) * 60;
                const pCanopy = project(cxNode, cyNode, czNode);
                ctx.beginPath();
                ctx.arc(pCanopy.x, pCanopy.y, 34 * state.zoom, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(5, 150, 105, 0.85)';
                ctx.fill();
                ctx.strokeStyle = 'rgba(52, 211, 153, 0.6)';
                ctx.lineWidth = 1.5;
                ctx.stroke();
            }

            // 5. Estrato Emergente (40 - 50 m) - Cúpula de Ceiba al viento
            const pEmergent = project(0, hScale(48), 0);
            ctx.beginPath();
            ctx.arc(pEmergent.x, pEmergent.y, 45 * state.zoom, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(52, 211, 153, 0.9)';
            ctx.fill();
            ctx.strokeStyle = '#fff';
            ctx.lineWidth = 2;
            ctx.stroke();

            // Marcador visual de altura del elevador del usuario
            const curY = hScale(state.alt);
            const pElev = project(0, curY, 0);
            ctx.beginPath();
            ctx.arc(pElev.x, pElev.y, 8 * state.zoom, 0, Math.PI * 2);
            ctx.fillStyle = '#fbbf24';
            ctx.fill();
            ctx.strokeStyle = '#fff';
            ctx.lineWidth = 2;
            ctx.stroke();

            // Línea de referencia del elevador
            ctx.setLineDash([4, 4]);
            ctx.strokeStyle = '#fbbf24';
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(pElev.x - 70, pElev.y);
            ctx.lineTo(pElev.x + 70, pElev.y);
            ctx.stroke();
            ctx.setLineDash([]);

            // Ríos voladores: vapor de agua y nubes orográficas flotando
            if (state.rivers) {
                ctx.fillStyle = 'rgba(255, 255, 255, 0.12)';
                for (let r = 0; r < 6; r++) {
                    const ry = hScale(35 + Math.sin(t + r) * 6);
                    const rx = -120 + ((t * 40 + r * 60) % 240);
                    ctx.beginPath();
                    ctx.arc(cx + rx, cy + ry * 0.4, 28 + r * 5, 0, Math.PI * 2);
                    ctx.fill();
                }
            }

            // Lluvia monzónica
            if (state.rain) {
                ctx.strokeStyle = 'rgba(56, 189, 248, 0.6)';
                ctx.lineWidth = 1.2;
                for (let k = 0; k < 25; k++) {
                    const rx = cx - 180 + ((t * 200 + k * 35) % 360);
                    const ry = (t * 400 + k * 45) % canvas.height;
                    ctx.beginPath();
                    ctx.moveTo(rx, ry);
                    ctx.lineTo(rx - 4, ry + 16);
                    ctx.stroke();
                }
            }

            requestAnimationFrame(render);
        }
        render();

        function updateTelemetry() {
            const alt = state.alt;
            let stratum = "";
            let par = 0;
            let hum = 0;
            let temp = 0;
            let wind = 0;

            const stratEl = document.getElementById('kpiStratum');

            if (alt >= 40) {
                stratum = "Estrato Emergente (40-50m)";
                stratEl.className = 'status-badge status-healthy';
                par = 100;
                hum = 62;
                temp = 32.5;
                wind = 14.5;
            } else if (alt >= 20) {
                stratum = "Dosel Continuo / Canopy (20-40m)";
                stratEl.className = 'status-badge status-canopy';
                par = 68;
                hum = 78;
                temp = 28.4;
                wind = 6.2;
            } else if (alt >= 5) {
                stratum = "Sotobosque / Understory (5-20m)";
                stratEl.className = 'status-badge status-floor';
                par = 15;
                hum = 88;
                temp = 25.8;
                wind = 1.8;
            } else {
                stratum = "Suelo Forestal (0-5m)";
                stratEl.className = 'status-badge status-floor';
                par = 1.5;
                hum = 98;
                temp = 24.1;
                wind = 0.3;
            }

            stratEl.innerText = stratum;
            document.getElementById('kpiPAR').innerText = `${par.toFixed(1)} % (${Math.round(par * 20)} µmol)`;
            document.getElementById('kpiHum').innerText = `${hum} %`;
            document.getElementById('kpiTemp').innerText = `${temp.toFixed(1)} °C`;
            document.getElementById('kpiWind').innerText = `${wind.toFixed(1)} km/h`;
        }
        setInterval(updateTelemetry, 250);

        document.getElementById('rngAlt').addEventListener('input', (e) => {
            state.alt = parseInt(e.target.value);
            document.getElementById('valAlt').innerText = `${state.alt} m`;
        });

        document.getElementById('btnCanopyJump').addEventListener('click', () => {
            state.alt = 32;
            document.getElementById('rngAlt').value = 32;
            document.getElementById('valAlt').innerText = '32 m (Dosel / Canopy)';
            speak("Ascendiendo al dosel continuo a treinta y dos metros. Aquí habita más del ochenta por ciento de la biodiversidad animal y vegetal de la selva tropical.");
        });

        document.getElementById('btnFloorJump').addEventListener('click', () => {
            state.alt = 2;
            document.getElementById('rngAlt').value = 2;
            document.getElementById('valAlt').innerText = '2 m (Suelo Forestal)';
            speak("Descendiendo al suelo forestal en penumbra. Apenas el uno punto cinco por ciento de la luz solar logra penetrar, con una humedad relativa cercana a la saturación.");
        });

        document.getElementById('btnRain').addEventListener('click', () => {
            state.rain = !state.rain;
            document.getElementById('btnRain').classList.toggle('active', state.rain);
            if (state.rain) speak("Lluvia monzónica tropical activada. Las hojas con goteros apicales canalizan el agua hacia el suelo.");
        });

        document.getElementById('btnRivers').addEventListener('click', () => {
            state.rivers = !state.rivers;
            document.getElementById('btnRivers').classList.toggle('active', state.rivers);
            if (state.rivers) speak("Ríos voladores de la cuenca amazónica. Un árbol adulto evapotranspira hasta mil litros diarios de agua hacia la atmósfera.");
        });

        document.getElementById('btnAudioToggle').addEventListener('click', (e) => {
            state.audioEnabled = !state.audioEnabled;
            e.target.innerText = state.audioEnabled ? '🔊 Sonidos Selva: ON' : '🔈 Sonidos: OFF';
        });

        document.getElementById('btnVoiceGuide').addEventListener('click', () => {
            speak("Bienvenido al simulador tridimensional del Bioma de Selva Tropical. Recorre los cincuenta metros de estratificación vertical para comprobar cómo cambian la luz, la humedad y las especies.");
        });

        document.getElementById('btnResetView').addEventListener('click', () => {
            state.rotX = -0.15;
            state.rotY = 0.3;
            state.zoom = 1.0;
        });
    </script>
</body>
</html>
"""

print("Módulos S34 y S35 preparados.")

# -----------------------------------------------------------------------------
# 6. SESIÓN 36: NEUROTOXINA Y BLOQUEO DE CANALES IÓNICOS DE SODIO 3D
# -----------------------------------------------------------------------------
def get_html_s36():
    return """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesión 36 • Neurotoxina y Bloqueo de Canales Iónicos de Sodio 3D [COD-036]</title>
    <!-- Protein Data Bank (PDB 6A95) • Canal Nav1.7 • Tetrodotoxina (TTX) • Hodgkin-Huxley -->
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #06020e;
            --bg-panel: rgba(16, 6, 32, 0.94);
            --border: rgba(168, 85, 247, 0.35);
            --primary: #c084fc;
            --primary-glow: rgba(192, 132, 252, 0.4);
            --cyan: #38bdf8;
            --amber: #fbbf24;
            --rose: #f43f5e;
            --text-main: #f8fafc;
            --text-sub: #cbd5e1;
            --font-title: 'Cinzel', serif;
            --font-sans: 'Inter', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
        body {
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-sans);
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            font-size: 14px;
        }

        header {
            background: linear-gradient(180deg, rgba(14, 4, 28, 0.98) 0%, rgba(14, 4, 28, 0.88) 100%);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border);
            padding: 10px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-shrink: 0;
            z-index: 40;
        }
        .brand-box { display: flex; align-items: center; gap: 14px; }
        .badge-pill {
            background: rgba(192, 132, 252, 0.15);
            border: 1px solid var(--primary);
            color: var(--primary);
            font-family: var(--font-mono);
            font-weight: 800;
            font-size: 0.82rem;
            padding: 4px 10px;
            border-radius: 6px;
        }
        .title-text h1 {
            font-family: var(--font-title);
            font-size: 1.15rem;
            font-weight: 800;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .title-text p { font-size: 0.78rem; color: var(--text-sub); margin-top: 1px; }

        .header-actions { display: flex; align-items: center; gap: 10px; }
        .btn-header {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: var(--text-main);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .btn-header:hover { background: rgba(192, 132, 252, 0.2); border-color: var(--primary); color: #fff; }

        .workspace { flex: 1; position: relative; overflow: hidden; display: flex; }

        .viewer-container {
            flex: 1;
            position: relative;
            background: radial-gradient(circle at center, #1b0a36 0%, #06020e 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        #channelCanvas {
            max-width: 96%;
            max-height: 92%;
            border-radius: 14px;
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.9);
            border: 1px solid rgba(192, 132, 252, 0.25);
            background: #080314;
            cursor: grab;
        }
        #channelCanvas:active { cursor: grabbing; }

        .controls-panel {
            position: absolute;
            top: 18px;
            left: 20px;
            width: 350px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 18px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 14px;
            max-height: calc(100vh - 120px);
            overflow-y: auto;
        }

        .panel-sec-title {
            font-size: 0.78rem;
            font-family: var(--font-mono);
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 5px;
        }

        .slider-group { display: flex; flex-direction: column; gap: 6px; }
        .slider-label {
            display: flex;
            justify-content: space-between;
            font-size: 0.82rem;
            color: var(--text-sub);
        }
        .slider-val { font-family: var(--font-mono); color: #fff; font-weight: 700; }
        input[type="range"] {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: #1e293b;
            outline: none;
            cursor: pointer;
            accent-color: var(--primary);
        }

        .btn-group { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
        .btn-action {
            background: rgba(192, 132, 252, 0.12);
            border: 1px solid rgba(192, 132, 252, 0.35);
            color: #fff;
            padding: 9px 10px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }
        .btn-action:hover { background: rgba(192, 132, 252, 0.28); border-color: var(--primary); }
        .btn-action.active { background: var(--primary); color: #080314; font-weight: 800; }
        .btn-action.danger { background: rgba(244, 63, 94, 0.15); border-color: #f43f5e; color: #fca5a5; }
        .btn-action.danger:hover { background: #f43f5e; color: #fff; }

        .telemetry-card {
            position: absolute;
            bottom: 20px;
            right: 20px;
            width: 320px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 16px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .kpi-row { display: flex; justify-content: space-between; align-items: center; }
        .kpi-name { font-size: 0.78rem; color: var(--text-sub); }
        .kpi-val { font-family: var(--font-mono); font-size: 0.88rem; font-weight: 700; color: #fff; }
        .status-badge {
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.74rem;
            font-weight: 800;
            text-align: center;
        }
        .status-healthy { background: rgba(52, 211, 153, 0.2); color: #6ee7b7; border: 1px solid #34d399; }
        .status-warning { background: rgba(251, 191, 36, 0.2); color: #fde68a; border: 1px solid #fbbf24; }
        .status-danger { background: rgba(244, 63, 94, 0.2); color: #fda4af; border: 1px solid #f43f5e; }
    </style>
</head>
<body>
    <header>
        <div class="brand-box">
            <span class="badge-pill">[COD-036]</span>
            <div class="title-text">
                <h1>⚡ Bloqueo de Canales Iónicos de Sodio 3D</h1>
                <p>Protein Data Bank (PDB 6A95) • Canal Nav1.7 • Tetrodotoxina (TTX Pez Globo) • Hodgkin-Huxley</p>
            </div>
        </div>
        <div class="header-actions">
            <button class="btn-header" id="btnAudioToggle">🔊 Audio Sináptico: ON</button>
            <button class="btn-header" id="btnVoiceGuide">🗣️ Guía por Voz</button>
            <button class="btn-header" id="btnResetView">🎯 Centrar Vista</button>
        </div>
    </header>

    <div class="workspace">
        <div class="viewer-container">
            <canvas id="channelCanvas" width="900" height="650"></canvas>
        </div>

        <div class="controls-panel">
            <div class="panel-sec-title">
                <span>Electroestimulación Neuronal</span>
                <span>⚡ VOLTAJE</span>
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Voltaje de Membrana (Vm)</span>
                    <span class="slider-val" id="valVm">-70 mV (Reposo)</span>
                </div>
                <input type="range" id="rngVm" min="-90" max="40" step="1" value="-70">
            </div>

            <div class="panel-sec-title">
                <span>Neurotoxinas y Fármacos</span>
                <span>🧪 TOXICOLOGÍA</span>
            </div>

            <div class="btn-group">
                <button class="btn-action danger" id="btnTTX">🐡 Tetrodotoxina (TTX)</button>
                <button class="btn-action" id="btnLido">💉 Lidocaína</button>
            </div>

            <div class="btn-group">
                <button class="btn-action active" id="btnActionPulse">⚡ Disparo Acción</button>
                <button class="btn-action" id="btnWashout">🚿 Lavado Fisiológico</button>
            </div>
        </div>

        <div class="telemetry-card">
            <div class="panel-sec-title">
                <span>Osciloscopio Celular</span>
                <span>Hodgkin-Huxley</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Conductancia de Sodio:</span>
                <span class="kpi-val" id="kpiGNa">0.05 mS/cm²</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Corriente Iónica (INa):</span>
                <span class="kpi-val" id="kpiINa">0.0 µA</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Conformación del Canal:</span>
                <span class="kpi-val" id="kpiConf">Cerrado en Reposo</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Estado de Conducción:</span>
                <span class="status-badge status-healthy" id="kpiStatus">Neurona Funcional</span>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('channelCanvas');
        const ctx = canvas.getContext('2d');

        let state = {
            vm: -70,
            toxin: 'none',
            isOpen: false,
            rotX: -0.2,
            rotY: 0.35,
            zoom: 1.0,
            audioEnabled: true
        };

        let audioCtx = null;
        function playSpikeAudio() {
            if (!state.audioEnabled) return;
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(880, audioCtx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(220, audioCtx.currentTime + 0.12);
                gain.gain.setValueAtTime(0.04, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.12);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.12);
            } catch(e) {}
        }

        function speak(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const u = new SpeechSynthesisUtterance(text);
                u.lang = 'es-ES';
                u.rate = 1.05;
                window.speechSynthesis.speak(u);
            }
        }

        let isDragging = false;
        let lastMouse = { x: 0, y: 0 };
        canvas.addEventListener('mousedown', (e) => {
            isDragging = true;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        window.addEventListener('mouseup', () => isDragging = false);
        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            const dx = e.clientX - lastMouse.x;
            const dy = e.clientY - lastMouse.y;
            state.rotY += dx * 0.008;
            state.rotX += dy * 0.008;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        canvas.addEventListener('wheel', (e) => {
            e.preventDefault();
            state.zoom *= e.deltaY > 0 ? 0.95 : 1.05;
            state.zoom = Math.max(0.6, Math.min(2.2, state.zoom));
        });

        // Loop de renderizado 3D de Canal Nav y Poro DEKA
        let t = 0;
        function render() {
            t += 0.02;
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            const cx = canvas.width / 2;
            const cy = canvas.height / 2;

            const cosY = Math.cos(state.rotY);
            const sinY = Math.sin(state.rotY);
            const cosX = Math.cos(state.rotX);
            const sinX = Math.sin(state.rotX);

            function project(x, y, z) {
                let x1 = x * cosY + z * sinY;
                let z1 = -x * sinY + z * cosY;
                let y2 = y * cosX - z1 * sinX;
                let z2 = y * sinX + z1 * cosX;
                const fov = 450;
                const scale = (fov / (fov + z2 + 300)) * state.zoom;
                return { x: cx + x1 * scale, y: cy + y2 * scale, z: z2, scale: scale };
            }

            // Bicapa lipídica neuronal (plano transversal)
            ctx.save();
            const pMemL = project(-220, 0, 0);
            const pMemR = project(220, 0, 0);
            ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
            ctx.lineWidth = 16 * state.zoom;
            ctx.beginPath();
            ctx.moveTo(pMemL.x, pMemL.y);
            ctx.lineTo(pMemR.x, pMemR.y);
            ctx.stroke();

            ctx.font = 'bold 11px JetBrains Mono';
            ctx.fillStyle = '#38bdf8';
            ctx.fillText("MEDIO EXTRACELULAR [Na⁺ = 145 mM]", cx - 160, cy - 140 * state.zoom);
            ctx.fillStyle = '#c084fc';
            ctx.fillText("CITOSOL AXONAL [Na⁺ = 12 mM]", cx - 140, cy + 180 * state.zoom);
            ctx.restore();

            // Canal de Sodio Nav (4 dominios pseudotetraméricos I, II, III, IV alrededor del poro central)
            const numDomains = 4;
            const poreRadius = (state.isOpen && state.toxin === 'none') ? 38 : 16;
            for (let d = 0; d < numDomains; d++) {
                const ang = (Math.PI * 2 / numDomains) * d + 0.4;
                const dx = Math.cos(ang) * poreRadius * 2.2;
                const dz = Math.sin(ang) * poreRadius * 2.2;

                const pTop = project(dx, -70, dz);
                const pMid = project(dx * 0.8, 0, dz * 0.8);
                const pBot = project(dx, 70, dz);

                // Hélice de proteína transmembrana
                ctx.beginPath();
                ctx.moveTo(pTop.x, pTop.y);
                ctx.lineTo(pMid.x, pMid.y);
                ctx.lineTo(pBot.x, pBot.y);
                ctx.strokeStyle = '#c084fc';
                ctx.lineWidth = 20 * state.zoom;
                ctx.lineCap = 'round';
                ctx.stroke();

                // Sensor de voltaje S4 (cargas positivas arginina)
                const pS4 = project(dx * 1.3, -20, dz * 1.3);
                ctx.beginPath();
                ctx.arc(pS4.x, pS4.y, 6 * state.zoom, 0, Math.PI * 2);
                ctx.fillStyle = '#38bdf8';
                ctx.fill();
            }

            // Neurotoxina Tetrodotoxina (TTX) encajada en el filtro DEKA exterior
            if (state.toxin === 'ttx') {
                const pTTX = project(0, -68, 0);
                ctx.beginPath();
                ctx.arc(pTTX.x, pTTX.y, 22 * state.zoom, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(244, 63, 94, 0.95)';
                ctx.fill();
                ctx.strokeStyle = '#fff';
                ctx.lineWidth = 2;
                ctx.stroke();

                ctx.font = 'bold 10px JetBrains Mono';
                ctx.fillStyle = '#fff';
                ctx.fillText("TTX (Oclusión Poro)", pTTX.x - 55, pTTX.y - 18);
            } else if (state.toxin === 'lido') {
                const pLido = project(0, 35, 0);
                ctx.beginPath();
                ctx.arc(pLido.x, pLido.y, 16 * state.zoom, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(251, 191, 36, 0.95)';
                ctx.fill();
                ctx.font = 'bold 9px JetBrains Mono';
                ctx.fillStyle = '#080314';
                ctx.fillText("Lidocaína", pLido.x - 24, pLido.y + 3);
            }

            // Iones de Sodio Na⁺ fluyendo a través del canal si está abierto y sin toxina
            if (state.isOpen && state.toxin === 'none') {
                ctx.fillStyle = '#38bdf8';
                for (let i = 0; i < 15; i++) {
                    const py = -110 + ((t * 180 + i * 22) % 220);
                    const prIon = project(Math.sin(i) * 6, py, Math.cos(i) * 6);
                    ctx.beginPath();
                    ctx.arc(prIon.x, prIon.y, 3.5 * state.zoom, 0, Math.PI * 2);
                    ctx.fill();
                }
            }

            requestAnimationFrame(render);
        }
        render();

        function updateTelemetry() {
            state.isOpen = state.vm > -50;
            const gNaEl = document.getElementById('kpiGNa');
            const iNaEl = document.getElementById('kpiINa');
            const confEl = document.getElementById('kpiConf');
            const statusEl = document.getElementById('kpiStatus');

            if (state.toxin === 'ttx') {
                gNaEl.innerText = '0.00 mS/cm² (Bloqueado)';
                iNaEl.innerText = '0.0 µA';
                confEl.innerText = 'Poro Ocluido por TTX';
                statusEl.className = 'status-badge status-danger';
                statusEl.innerText = '🚨 Parálisis Respiratoria Flácida';
            } else if (state.toxin === 'lido') {
                gNaEl.innerText = '0.02 mS/cm²';
                iNaEl.innerText = '0.1 µA';
                confEl.innerText = 'Inactivación por Anestésico';
                statusEl.className = 'status-badge status-warning';
                statusEl.innerText = '💉 Bloqueo Anestésico Reversible';
            } else if (state.isOpen) {
                gNaEl.innerText = '32.4 mS/cm²';
                iNaEl.innerText = '-4.2 µA (Influjo Masivo)';
                confEl.innerText = 'Abierto Conductor (DEKA)';
                statusEl.className = 'status-badge status-healthy';
                statusEl.innerText = '⚡ Despolarización Neuronal';
            } else {
                gNaEl.innerText = '0.05 mS/cm²';
                iNaEl.innerText = '0.0 µA';
                confEl.innerText = 'Cerrado en Reposo (-70 mV)';
                statusEl.className = 'status-badge status-healthy';
                statusEl.innerText = 'Potencial de Reposo Normal';
            }
        }
        setInterval(updateTelemetry, 250);

        document.getElementById('rngVm').addEventListener('input', (e) => {
            state.vm = parseInt(e.target.value);
            document.getElementById('valVm').innerText = `${state.vm} mV`;
            if (state.vm > -50 && state.toxin === 'none') playSpikeAudio();
        });

        document.getElementById('btnTTX').addEventListener('click', () => {
            state.toxin = 'ttx';
            speak("Tetrodotoxina aplicada. La molécula de TTX actúa como un tapón estéreo-específico rígido con carga positiva que bloquea el filtro exterior DEKA de los canales Nav, aboliendo los potenciales de acción y causando asfixia por parálisis diafragmática.");
        });

        document.getElementById('btnLido').addEventListener('click', () => {
            state.toxin = 'lido';
            speak("Anestésico local lidocaína aplicado. Bloquea el canal dependiente de voltaje desde el lado intracelular, bloqueando la conducción de las fibras del dolor.");
        });

        document.getElementById('btnActionPulse').addEventListener('click', () => {
            state.vm = 30;
            document.getElementById('rngVm').value = 30;
            document.getElementById('valVm').innerText = '+30 mV (Pico Despolarización)';
            if (state.toxin === 'none') playSpikeAudio();
            setTimeout(() => {
                state.vm = -70;
                document.getElementById('rngVm').value = -70;
                document.getElementById('valVm').innerText = '-70 mV (Reposo)';
            }, 600);
        });

        document.getElementById('btnWashout').addEventListener('click', () => {
            state.toxin = 'none';
            state.vm = -70;
            document.getElementById('rngVm').value = -70;
            document.getElementById('valVm').innerText = '-70 mV (Reposo)';
            speak("Lavado tisular completado. Neurotoxinas eliminadas, restableciendo la conductancia normal del canal Nav.");
        });

        document.getElementById('btnAudioToggle').addEventListener('click', (e) => {
            state.audioEnabled = !state.audioEnabled;
            e.target.innerText = state.audioEnabled ? '🔊 Audio Sináptico: ON' : '🔈 Audio: OFF';
        });

        document.getElementById('btnVoiceGuide').addEventListener('click', () => {
            speak("Bienvenido al simulador tridimensional del Canal de Sodio Dependiente de Voltaje Nav1.7. Observa cómo la tetrodotoxina bloquea el flujo iónico e interrumpe el impulso nervioso.");
        });

        document.getElementById('btnResetView').addEventListener('click', () => {
            state.rotX = -0.2;
            state.rotY = 0.35;
            state.zoom = 1.0;
        });
    </script>
</body>
</html>
"""

# -----------------------------------------------------------------------------
# 7. SESIÓN 37: PIEL HUMANA, CAPAS TISULARES Y TERMORREGULACIÓN 3D
# -----------------------------------------------------------------------------
def get_html_s37():
    return """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesión 37 • Piel Humana, Capas Tisulares y Termorregulación 3D [COD-037]</title>
    <!-- NIH Visible Human • Epidermis, Dermis, Hipodermis • Vasoconstricción • Sudoración Ecrina -->
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #100604;
            --bg-panel: rgba(30, 10, 8, 0.94);
            --border: rgba(244, 63, 94, 0.35);
            --primary: #f43f5e;
            --primary-glow: rgba(244, 63, 94, 0.4);
            --amber: #fbbf24;
            --cyan: #38bdf8;
            --text-main: #f8fafc;
            --text-sub: #cbd5e1;
            --font-title: 'Cinzel', serif;
            --font-sans: 'Inter', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
        body {
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-sans);
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            font-size: 14px;
        }

        header {
            background: linear-gradient(180deg, rgba(24, 8, 6, 0.98) 0%, rgba(24, 8, 6, 0.88) 100%);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border);
            padding: 10px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-shrink: 0;
            z-index: 40;
        }
        .brand-box { display: flex; align-items: center; gap: 14px; }
        .badge-pill {
            background: rgba(244, 63, 94, 0.15);
            border: 1px solid var(--primary);
            color: var(--primary);
            font-family: var(--font-mono);
            font-weight: 800;
            font-size: 0.82rem;
            padding: 4px 10px;
            border-radius: 6px;
        }
        .title-text h1 {
            font-family: var(--font-title);
            font-size: 1.15rem;
            font-weight: 800;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .title-text p { font-size: 0.78rem; color: var(--text-sub); margin-top: 1px; }

        .header-actions { display: flex; align-items: center; gap: 10px; }
        .btn-header {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: var(--text-main);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .btn-header:hover { background: rgba(244, 63, 94, 0.2); border-color: var(--primary); color: #fff; }

        .workspace { flex: 1; position: relative; overflow: hidden; display: flex; }

        .viewer-container {
            flex: 1;
            position: relative;
            background: radial-gradient(circle at center, #2b0d08 0%, #100604 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        #skinCanvas {
            max-width: 96%;
            max-height: 92%;
            border-radius: 14px;
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.9);
            border: 1px solid rgba(244, 63, 94, 0.25);
            background: #140705;
            cursor: grab;
        }
        #skinCanvas:active { cursor: grabbing; }

        .controls-panel {
            position: absolute;
            top: 18px;
            left: 20px;
            width: 350px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 18px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 14px;
            max-height: calc(100vh - 120px);
            overflow-y: auto;
        }

        .panel-sec-title {
            font-size: 0.78rem;
            font-family: var(--font-mono);
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 5px;
        }

        .slider-group { display: flex; flex-direction: column; gap: 6px; }
        .slider-label {
            display: flex;
            justify-content: space-between;
            font-size: 0.82rem;
            color: var(--text-sub);
        }
        .slider-val { font-family: var(--font-mono); color: #fff; font-weight: 700; }
        input[type="range"] {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: #1e293b;
            outline: none;
            cursor: pointer;
            accent-color: var(--primary);
        }

        .btn-group { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
        .btn-action {
            background: rgba(244, 63, 94, 0.12);
            border: 1px solid rgba(244, 63, 94, 0.35);
            color: #fff;
            padding: 9px 10px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }
        .btn-action:hover { background: rgba(244, 63, 94, 0.28); border-color: var(--primary); }
        .btn-action.active { background: var(--primary); color: #fff; font-weight: 800; }

        .telemetry-card {
            position: absolute;
            bottom: 20px;
            right: 20px;
            width: 320px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 16px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .kpi-row { display: flex; justify-content: space-between; align-items: center; }
        .kpi-name { font-size: 0.78rem; color: var(--text-sub); }
        .kpi-val { font-family: var(--font-mono); font-size: 0.88rem; font-weight: 700; color: #fff; }
        .status-badge {
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.74rem;
            font-weight: 800;
            text-align: center;
        }
        .status-healthy { background: rgba(52, 211, 153, 0.2); color: #6ee7b7; border: 1px solid #34d399; }
        .status-hot { background: rgba(244, 63, 94, 0.2); color: #fda4af; border: 1px solid #f43f5e; }
        .status-cold { background: rgba(56, 189, 248, 0.2); color: #7dd3fc; border: 1px solid #38bdf8; }
    </style>
</head>
<body>
    <header>
        <div class="brand-box">
            <span class="badge-pill">[COD-037]</span>
            <div class="title-text">
                <h1>🩺 Piel Humana, Capas Tisulares y Termorregulación 3D</h1>
                <p>NIH Visible Human Project • Epidermis, Dermis & Hipodermis • Vasomotilidad Capilar • Sudoración Ecrina</p>
            </div>
        </div>
        <div class="header-actions">
            <button class="btn-header" id="btnAudioToggle">🔊 Audio Pulso: ON</button>
            <button class="btn-header" id="btnVoiceGuide">🗣️ Guía por Voz</button>
            <button class="btn-header" id="btnResetView">🎯 Centrar Vista</button>
        </div>
    </header>

    <div class="workspace">
        <div class="viewer-container">
            <canvas id="skinCanvas" width="900" height="650"></canvas>
        </div>

        <div class="controls-panel">
            <div class="panel-sec-title">
                <span>Variables Termodinámicas</span>
                <span>🌡️ HOMEOSTASIS</span>
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Temperatura Ambiental</span>
                    <span class="slider-val" id="valTemp">22.0 °C (Confort)</span>
                </div>
                <input type="range" id="rngTemp" min="0" max="45" step="1" value="22">
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Índice Ultravioleta (UVI)</span>
                    <span class="slider-val" id="valUV">UVI 3 (Moderado)</span>
                </div>
                <input type="range" id="rngUV" min="0" max="11" step="1" value="3">
            </div>

            <div class="panel-sec-title">
                <span>Mecanismos Fisiológicos</span>
                <span>🔬 RESPUESTA</span>
            </div>

            <div class="btn-group">
                <button class="btn-action" id="btnHeat">🔥 Golpe de Calor (40°C)</button>
                <button class="btn-action" id="btnCold">❄️ Frío Polar (2°C)</button>
            </div>

            <div class="btn-group">
                <button class="btn-action" id="btnGoose">🦔 Piel de Gallina</button>
                <button class="btn-action active" id="btnResetSkin">🔄 Normal (22°C)</button>
            </div>
        </div>

        <div class="telemetry-card">
            <div class="panel-sec-title">
                <span>Histología y Termorregulación</span>
                <span>NIH Medical Data</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Flujo Sanguíneo Dérmico:</span>
                <span class="kpi-val" id="kpiFlow">12 mL/100g/min</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Tasa de Sudoración:</span>
                <span class="kpi-val" id="kpiSweat">0.05 L/hora</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Músculo Erector del Pelo:</span>
                <span class="kpi-val" id="kpiPilo">Relajado</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Estado Homeostático:</span>
                <span class="status-badge status-healthy" id="kpiStatus">Normotermia (36.8°C)</span>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('skinCanvas');
        const ctx = canvas.getContext('2d');

        let state = {
            temp: 22,
            uv: 3,
            piloerection: false,
            rotX: -0.22,
            rotY: 0.35,
            zoom: 1.0,
            audioEnabled: true
        };

        function speak(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const u = new SpeechSynthesisUtterance(text);
                u.lang = 'es-ES';
                u.rate = 1.05;
                window.speechSynthesis.speak(u);
            }
        }

        let isDragging = false;
        let lastMouse = { x: 0, y: 0 };
        canvas.addEventListener('mousedown', (e) => {
            isDragging = true;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        window.addEventListener('mouseup', () => isDragging = false);
        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            const dx = e.clientX - lastMouse.x;
            const dy = e.clientY - lastMouse.y;
            state.rotY += dx * 0.008;
            state.rotX += dy * 0.008;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        canvas.addEventListener('wheel', (e) => {
            e.preventDefault();
            state.zoom *= e.deltaY > 0 ? 0.95 : 1.05;
            state.zoom = Math.max(0.6, Math.min(2.0, state.zoom));
        });

        // Loop de renderizado 3D del Bloque Tisular Cutáneo
        let t = 0;
        function render() {
            t += 0.02;
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            const cx = canvas.width / 2;
            const cy = canvas.height / 2;

            const cosY = Math.cos(state.rotY);
            const sinY = Math.sin(state.rotY);
            const cosX = Math.cos(state.rotX);
            const sinX = Math.sin(state.rotX);

            function project(x, y, z) {
                let x1 = x * cosY + z * sinY;
                let z1 = -x * sinY + z * cosY;
                let y2 = y * cosX - z1 * sinX;
                let z2 = y * sinX + z1 * cosX;
                const fov = 450;
                const scale = (fov / (fov + z2 + 300)) * state.zoom;
                return { x: cx + x1 * scale, y: cy + y2 * scale, z: z2, scale: scale };
            }

            // Dimensiones del bloque tisular
            const bw = 240, bh = 220, bd = 160;

            // 1. Capa Epidermis (Superior: -110 a -85 px)
            // Color influenciado por melanina UV
            const melR = Math.max(160, 220 - state.uv * 6);
            const melG = Math.max(110, 175 - state.uv * 6);
            const melB = Math.max(90, 145 - state.uv * 6);

            // 2. Capa Dermis (Media: -85 a 45 px) - Fibras de colágeno, capilares
            // 3. Capa Hipodermis (Inferior: 45 a 110 px) - Adipocitos amarillos

            const layers = [
                { name: "Epidermis", y0: -110, y1: -85, color: `rgb(${melR}, ${melG}, ${melB})` },
                { name: "Dermis", y0: -85, y1: 45, color: '#e17055' },
                { name: "Hipodermis", y0: 45, y1: 110, color: '#ffeaa7' }
            ];

            layers.forEach(layer => {
                const hw = bw / 2, hd = bd / 2;
                const v = [
                    project(-hw, layer.y0, -hd), project(hw, layer.y0, -hd),
                    project(hw, layer.y0, hd), project(-hw, layer.y0, hd),
                    project(-hw, layer.y1, -hd), project(hw, layer.y1, -hd),
                    project(hw, layer.y1, hd), project(-hw, layer.y1, hd)
                ];

                // Cara frontal
                ctx.beginPath();
                ctx.moveTo(v[3].x, v[3].y);
                ctx.lineTo(v[2].x, v[2].y);
                ctx.lineTo(v[6].x, v[6].y);
                ctx.lineTo(v[7].x, v[7].y);
                ctx.closePath();
                ctx.fillStyle = layer.color;
                ctx.fill();
                ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
                ctx.stroke();

                // Cara superior si es epidermis
                if (layer.name === "Epidermis") {
                    ctx.beginPath();
                    ctx.moveTo(v[0].x, v[0].y);
                    ctx.lineTo(v[1].x, v[1].y);
                    ctx.lineTo(v[2].x, v[2].y);
                    ctx.lineTo(v[3].x, v[3].y);
                    ctx.closePath();
                    ctx.fillStyle = `rgb(${melR + 15}, ${melG + 15}, ${melB + 15})`;
                    ctx.fill();
                    ctx.stroke();
                }

                // Cara lateral
                ctx.beginPath();
                ctx.moveTo(v[2].x, v[2].y);
                ctx.lineTo(v[1].x, v[1].y);
                ctx.lineTo(v[5].x, v[5].y);
                ctx.lineTo(v[6].x, v[6].y);
                ctx.closePath();
                ctx.fillStyle = 'rgba(0, 0, 0, 0.25)';
                ctx.fill();
                ctx.stroke();

                // Etiqueta
                ctx.fillStyle = '#fff';
                ctx.font = 'bold 10px JetBrains Mono';
                const pTag = project(-hw + 15, (layer.y0 + layer.y1) / 2, hd);
                ctx.fillText(layer.name, pTag.x, pTag.y);
            });

            // Folículo piloso con tallo del pelo y músculo erector
            const pHairRoot = project(15, 30, 20);
            const hairAngle = (state.piloerection || state.temp < 10) ? -0.1 : 0.45;
            const pHairTip = project(15 + Math.sin(hairAngle) * 90, -110 - Math.cos(hairAngle) * 70, 20);

            ctx.beginPath();
            ctx.moveTo(pHairRoot.x, pHairRoot.y);
            ctx.lineTo(pHairTip.x, pHairTip.y);
            ctx.strokeStyle = '#2d3436';
            ctx.lineWidth = 4 * state.zoom;
            ctx.lineCap = 'round';
            ctx.stroke();

            // Capilares dérmicos: Vasodilatación (rojo intenso grueso) vs Vasoconstricción (azul fino)
            const isHot = state.temp > 30;
            const isCold = state.temp < 15;
            ctx.strokeStyle = isHot ? '#f43f5e' : (isCold ? '#38bdf8' : '#e67e22');
            ctx.lineWidth = (isHot ? 6 : (isCold ? 2 : 3.5)) * state.zoom;
            ctx.beginPath();
            const pCap1 = project(-60, -30, 10);
            const pCap2 = project(60, -30, 10);
            ctx.moveTo(pCap1.x, pCap1.y);
            ctx.bezierCurveTo(pCap1.x + 30, pCap1.y - 15, pCap2.x - 30, pCap2.y + 15, pCap2.x, pCap2.y);
            ctx.stroke();

            // Gotas de sudor ecrino emergiendo si hace calor
            if (isHot) {
                ctx.fillStyle = 'rgba(56, 189, 248, 0.85)';
                for (let s = 0; s < 5; s++) {
                    const pSweat = project(-50 + s * 25, -114 - Math.sin(t * 3 + s) * 4, 15);
                    ctx.beginPath();
                    ctx.arc(pSweat.x, pSweat.y, 4 * state.zoom, 0, Math.PI * 2);
                    ctx.fill();
                }
            }

            requestAnimationFrame(render);
        }
        render();

        function updateTelemetry() {
            const temp = state.temp;
            let flow = 0;
            let sweat = 0;
            const flowEl = document.getElementById('kpiFlow');
            const sweatEl = document.getElementById('kpiSweat');
            const piloEl = document.getElementById('kpiPilo');
            const statusEl = document.getElementById('kpiStatus');

            if (temp >= 35) {
                flow = 75;
                sweat = 1.4;
                flowEl.innerText = `${flow} mL/100g/min (Vasodilatación)`;
                sweatEl.innerText = `${sweat.toFixed(1)} L/hora (Evaporación)`;
                piloEl.innerText = 'Relajado';
                statusEl.className = 'status-badge status-hot';
                statusEl.innerText = '🔥 Estrés Térmico / Disipación';
            } else if (temp <= 12) {
                flow = 2.5;
                sweat = 0.0;
                flowEl.innerText = `${flow} mL/100g/min (Vasoconstricción)`;
                sweatEl.innerText = '0.0 L/hora';
                piloEl.innerText = 'Erección Activa (Piel de Gallina)';
                statusEl.className = 'status-badge status-cold';
                statusEl.innerText = '❄️ Conservación de Calor';
            } else {
                flow = 12;
                sweat = 0.05;
                flowEl.innerText = `${flow} mL/100g/min (Basal)`;
                sweatEl.innerText = `${sweat.toFixed(2)} L/hora (Insensible)`;
                piloEl.innerText = state.piloerection ? 'Erección Forzada' : 'Relajado';
                statusEl.className = 'status-badge status-healthy';
                statusEl.innerText = 'Normotermia Estable (36.8°C)';
            }
        }
        setInterval(updateTelemetry, 250);

        document.getElementById('rngTemp').addEventListener('input', (e) => {
            state.temp = parseInt(e.target.value);
            document.getElementById('valTemp').innerText = `${state.temp} °C`;
        });

        document.getElementById('rngUV').addEventListener('input', (e) => {
            state.uv = parseInt(e.target.value);
            document.getElementById('valUV').innerText = `UVI ${state.uv}`;
        });

        document.getElementById('btnHeat').addEventListener('click', () => {
            state.temp = 40;
            document.getElementById('rngTemp').value = 40;
            document.getElementById('valTemp').innerText = '40 °C (Calor Extremo)';
            speak("Respuesta a golpe de calor. Vasodilatación arteriolar masiva para aumentar el flujo sanguíneo cutáneo y secreción de sudor ecrino para disipación térmica por evaporación latente.");
        });

        document.getElementById('btnCold').addEventListener('click', () => {
            state.temp = 2;
            state.piloerection = true;
            document.getElementById('rngTemp').value = 2;
            document.getElementById('valTemp').innerText = '2 °C (Frío Polar)';
            speak("Respuesta al frío extremo. Vasoconstricción refleja para retener el calor en los órganos vitales y activación de los músculos erectores del pelo para atrapar una capa de aire aislante.");
        });

        document.getElementById('btnGoose').addEventListener('click', () => {
            state.piloerection = !state.piloerection;
            document.getElementById('btnGoose').classList.toggle('active', state.piloerection);
            speak("Reflejo pilomotor activado. El músculo erector tracciona el folículo piloso generando la protuberancia conocida como piel de gallina.");
        });

        document.getElementById('btnResetSkin').addEventListener('click', () => {
            state.temp = 22;
            state.uv = 3;
            state.piloerection = false;
            document.getElementById('rngTemp').value = 22;
            document.getElementById('valTemp').innerText = '22 °C (Confort)';
            document.getElementById('rngUV').value = 3;
            document.getElementById('valUV').innerText = 'UVI 3 (Moderado)';
            document.getElementById('btnGoose').classList.remove('active');
            speak("Homeostasis cutánea restablecida a temperatura ambiente de confort.");
        });

        document.getElementById('btnAudioToggle').addEventListener('click', (e) => {
            state.audioEnabled = !state.audioEnabled;
            e.target.innerText = state.audioEnabled ? '🔊 Audio Pulso: ON' : '🔈 Audio: OFF';
        });

        document.getElementById('btnVoiceGuide').addEventListener('click', () => {
            speak("Bienvenido al simulador tridimensional de Piel Humana y Termorregulación. Ajusta la temperatura para observar en tiempo real la vasodilatación y el reflejo pilomotor.");
        });

        document.getElementById('btnResetView').addEventListener('click', () => {
            state.rotX = -0.22;
            state.rotY = 0.35;
            state.zoom = 1.0;
        });
    </script>
</body>
</html>
"""

# -----------------------------------------------------------------------------
# 8. SESIÓN 38: COLUMNA VERTEBRAL HUMANA, DISCOS Y BIOMECÁNICA LUMBAR 3D
# -----------------------------------------------------------------------------
def get_html_s38():
    return """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesión 38 • Columna Vertebral, Discos y Biomecánica Lumbar 3D [COD-038]</title>
    <!-- NIH 3D TC Lumbar • Biomecánica Chaffin & Nachemson • Disco L5-S1 • Umbral NIOSH -->
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #060812;
            --bg-panel: rgba(10, 16, 32, 0.94);
            --border: rgba(56, 189, 248, 0.35);
            --primary: #38bdf8;
            --primary-glow: rgba(56, 189, 248, 0.4);
            --bone: #f8fafc;
            --disc: #38bdf8;
            --nerve: #fbbf24;
            --danger: #f43f5e;
            --text-main: #f8fafc;
            --text-sub: #cbd5e1;
            --font-title: 'Cinzel', serif;
            --font-sans: 'Inter', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
        body {
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-sans);
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            font-size: 14px;
        }

        header {
            background: linear-gradient(180deg, rgba(8, 14, 28, 0.98) 0%, rgba(8, 14, 28, 0.88) 100%);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border);
            padding: 10px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-shrink: 0;
            z-index: 40;
        }
        .brand-box { display: flex; align-items: center; gap: 14px; }
        .badge-pill {
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid var(--primary);
            color: var(--primary);
            font-family: var(--font-mono);
            font-weight: 800;
            font-size: 0.82rem;
            padding: 4px 10px;
            border-radius: 6px;
        }
        .title-text h1 {
            font-family: var(--font-title);
            font-size: 1.15rem;
            font-weight: 800;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .title-text p { font-size: 0.78rem; color: var(--text-sub); margin-top: 1px; }

        .header-actions { display: flex; align-items: center; gap: 10px; }
        .btn-header {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: var(--text-main);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .btn-header:hover { background: rgba(56, 189, 248, 0.2); border-color: var(--primary); color: #fff; }

        .workspace { flex: 1; position: relative; overflow: hidden; display: flex; }

        .viewer-container {
            flex: 1;
            position: relative;
            background: radial-gradient(circle at center, #0f1d38 0%, #060812 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        #spineCanvas {
            max-width: 96%;
            max-height: 92%;
            border-radius: 14px;
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.9);
            border: 1px solid rgba(56, 189, 248, 0.25);
            background: #080d1e;
            cursor: grab;
        }
        #spineCanvas:active { cursor: grabbing; }

        .controls-panel {
            position: absolute;
            top: 18px;
            left: 20px;
            width: 350px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 18px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 14px;
            max-height: calc(100vh - 120px);
            overflow-y: auto;
        }

        .panel-sec-title {
            font-size: 0.78rem;
            font-family: var(--font-mono);
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 5px;
        }

        .slider-group { display: flex; flex-direction: column; gap: 6px; }
        .slider-label {
            display: flex;
            justify-content: space-between;
            font-size: 0.82rem;
            color: var(--text-sub);
        }
        .slider-val { font-family: var(--font-mono); color: #fff; font-weight: 700; }
        input[type="range"] {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: #1e293b;
            outline: none;
            cursor: pointer;
            accent-color: var(--primary);
        }

        .btn-group { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
        .btn-action {
            background: rgba(56, 189, 248, 0.12);
            border: 1px solid rgba(56, 189, 248, 0.35);
            color: #fff;
            padding: 9px 10px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }
        .btn-action:hover { background: rgba(56, 189, 248, 0.28); border-color: var(--primary); }
        .btn-action.active { background: var(--primary); color: #060812; font-weight: 800; }
        .btn-action.danger { background: rgba(244, 63, 94, 0.15); border-color: #f43f5e; color: #fca5a5; }
        .btn-action.danger:hover { background: #f43f5e; color: #fff; }

        .telemetry-card {
            position: absolute;
            bottom: 20px;
            right: 20px;
            width: 320px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 16px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .kpi-row { display: flex; justify-content: space-between; align-items: center; }
        .kpi-name { font-size: 0.78rem; color: var(--text-sub); }
        .kpi-val { font-family: var(--font-mono); font-size: 0.88rem; font-weight: 700; color: #fff; }
        .status-badge {
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.74rem;
            font-weight: 800;
            text-align: center;
        }
        .status-healthy { background: rgba(52, 211, 153, 0.2); color: #6ee7b7; border: 1px solid #34d399; }
        .status-warning { background: rgba(251, 191, 36, 0.2); color: #fde68a; border: 1px solid #fbbf24; }
        .status-danger { background: rgba(244, 63, 94, 0.2); color: #fda4af; border: 1px solid #f43f5e; }
    </style>
</head>
<body>
    <header>
        <div class="brand-box">
            <span class="badge-pill">[COD-038]</span>
            <div class="title-text">
                <h1>🦴 Columna Vertebral y Biomecánica Lumbar 3D</h1>
                <p>NIH 3D Tomografía Ortopédica • Biomecánica de Chaffin & Nachemson • Segmento L3-S1 • Compresión vs Rodillas</p>
            </div>
        </div>
        <div class="header-actions">
            <button class="btn-header" id="btnAudioToggle">🔊 Audio Alerta: ON</button>
            <button class="btn-header" id="btnVoiceGuide">🗣️ Guía por Voz</button>
            <button class="btn-header" id="btnResetView">🎯 Centrar Vista</button>
        </div>
    </header>

    <div class="workspace">
        <div class="viewer-container">
            <canvas id="spineCanvas" width="900" height="650"></canvas>
        </div>

        <div class="controls-panel">
            <div class="panel-sec-title">
                <span>Carga y Postura de Levantamiento</span>
                <span>🏋️ BIOMECÁNICA</span>
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Peso Levantado (kg)</span>
                    <span class="slider-val" id="valWeight">15 kg</span>
                </div>
                <input type="range" id="rngWeight" min="0" max="35" step="1" value="15">
            </div>

            <div class="panel-sec-title">
                <span>Técnica de Levantamiento</span>
                <span>📐 ERGONOMÍA</span>
            </div>

            <div class="btn-group">
                <button class="btn-action active" id="btnPostureKnees">🦵 Flexionando Rodillas</button>
                <button class="btn-action danger" id="btnPostureBack">⚠️ Doblando Espalda</button>
            </div>

            <div class="btn-group">
                <button class="btn-action danger" id="btnHernia">💥 Hernia Discal L5-S1</button>
                <button class="btn-action" id="btnDecompress">🧘 Descompresión</button>
            </div>
        </div>

        <div class="telemetry-card">
            <div class="panel-sec-title">
                <span>Telemetría Ortopédica (L5-S1)</span>
                <span>NIOSH Limit (3.400 N)</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Fuerza Compresiva L5-S1:</span>
                <span class="kpi-val" id="kpiForce">1.180 N (120 kgf)</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Presión Intradiscal:</span>
                <span class="kpi-val" id="kpiPressure">0.85 MPa</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Raíz Nerviosa Ciática:</span>
                <span class="kpi-val" id="kpiSciatic">Canal Libre</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Evaluación de Riesgo:</span>
                <span class="status-badge status-healthy" id="kpiStatus">Zona Segura Ergonómica</span>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('spineCanvas');
        const ctx = canvas.getContext('2d');

        let state = {
            weight: 15,
            posture: 'knees', // 'knees' o 'back'
            hernia: false,
            rotX: -0.15,
            rotY: 0.35,
            zoom: 1.0,
            audioEnabled: true
        };

        function speak(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const u = new SpeechSynthesisUtterance(text);
                u.lang = 'es-ES';
                u.rate = 1.05;
                window.speechSynthesis.speak(u);
            }
        }

        let isDragging = false;
        let lastMouse = { x: 0, y: 0 };
        canvas.addEventListener('mousedown', (e) => {
            isDragging = true;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        window.addEventListener('mouseup', () => isDragging = false);
        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            const dx = e.clientX - lastMouse.x;
            const dy = e.clientY - lastMouse.y;
            state.rotY += dx * 0.008;
            state.rotX += dy * 0.008;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        canvas.addEventListener('wheel', (e) => {
            e.preventDefault();
            state.zoom *= e.deltaY > 0 ? 0.95 : 1.05;
            state.zoom = Math.max(0.6, Math.min(2.0, state.zoom));
        });

        // Loop de renderizado 3D de Vértebras L3, L4, L5 y Sacro S1
        let t = 0;
        function render() {
            t += 0.02;
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            const cx = canvas.width / 2;
            const cy = canvas.height / 2;

            const cosY = Math.cos(state.rotY);
            const sinY = Math.sin(state.rotY);
            const cosX = Math.cos(state.rotX);
            const sinX = Math.sin(state.rotX);

            function project(x, y, z) {
                let x1 = x * cosY + z * sinY;
                let z1 = -x * sinY + z * cosY;
                let y2 = y * cosX - z1 * sinX;
                let z2 = y * sinX + z1 * cosX;
                const fov = 450;
                const scale = (fov / (fov + z2 + 300)) * state.zoom;
                return { x: cx + x1 * scale, y: cy + y2 * scale, z: z2, scale: scale };
            }

            // Vértebras lumbares (L3, L4, L5 y Sacro S1)
            const vertebrae = [
                { name: "L3", y: -130, w: 95, h: 42 },
                { name: "L4", y: -60, w: 105, h: 44 },
                { name: "L5", y: 15, w: 115, h: 46 },
                { name: "Sacro S1", y: 95, w: 140, h: 55 }
            ];

            // Dibujar cada vértebra ósea
            vertebrae.forEach(v => {
                const hw = v.w / 2;
                const hh = v.h / 2;
                const hd = 50;

                const pts = [
                    project(-hw, v.y - hh, -hd), project(hw, v.y - hh, -hd),
                    project(hw, v.y - hh, hd), project(-hw, v.y - hh, hd),
                    project(-hw, v.y + hh, -hd), project(hw, v.y + hh, -hd),
                    project(hw, v.y + hh, hd), project(-hw, v.y + hh, hd)
                ];

                // Cuerpo vertebral anterior
                ctx.beginPath();
                ctx.moveTo(pts[3].x, pts[3].y);
                ctx.lineTo(pts[2].x, pts[2].y);
                ctx.lineTo(pts[6].x, pts[6].y);
                ctx.lineTo(pts[7].x, pts[7].y);
                ctx.closePath();
                ctx.fillStyle = '#e2e8f0';
                ctx.fill();
                ctx.strokeStyle = '#94a3b8';
                ctx.lineWidth = 1.2;
                ctx.stroke();

                // Cara superior trabecular
                ctx.beginPath();
                ctx.moveTo(pts[0].x, pts[0].y);
                ctx.lineTo(pts[1].x, pts[1].y);
                ctx.lineTo(pts[2].x, pts[2].y);
                ctx.lineTo(pts[3].x, pts[3].y);
                ctx.closePath();
                ctx.fillStyle = '#f8fafc';
                ctx.fill();
                ctx.stroke();

                // Apófisis espinosa posterior (sobresale hacia atrás)
                const pSpine = project(0, v.y, -hd - 45);
                const pSpineBase = project(0, v.y, -hd);
                ctx.beginPath();
                ctx.moveTo(pSpineBase.x, pSpineBase.y);
                ctx.lineTo(pSpine.x, pSpine.y);
                ctx.strokeStyle = '#cbd5e1';
                ctx.lineWidth = 14 * state.zoom;
                ctx.stroke();

                ctx.font = 'bold 10px JetBrains Mono';
                ctx.fillStyle = '#0f172a';
                ctx.fillText(v.name, pts[3].x + 10, v.y * state.zoom + cy + 4);
            });

            // Discos intervertebrales (L3-L4, L4-L5, L5-S1)
            const discs = [
                { y: -95, w: 90, name: "L3-L4" },
                { y: -22, w: 100, name: "L4-L5" },
                { y: 55, w: 110, name: "L5-S1" }
            ];

            discs.forEach(d => {
                const isL5S1 = d.name === "L5-S1";
                const isSeverelyLoaded = isL5S1 && (state.posture === 'back' || state.hernia);

                ctx.beginPath();
                const pL = project(-d.w / 2, d.y, 25);
                const pR = project(d.w / 2, d.y, 25);
                ctx.moveTo(pL.x, pL.y);
                ctx.lineTo(pR.x, pR.y);
                ctx.strokeStyle = isSeverelyLoaded ? '#f43f5e' : '#38bdf8';
                ctx.lineWidth = (isSeverelyLoaded ? 18 : 12) * state.zoom;
                ctx.lineCap = 'round';
                ctx.stroke();

                // Protrusión herniaria en L5-S1
                if (isSeverelyLoaded && (state.hernia || state.weight > 20)) {
                    const pHernia = project(d.w / 2 + 18, d.y, -15);
                    ctx.beginPath();
                    ctx.arc(pHernia.x, pHernia.y, (8 + Math.sin(t * 4) * 2) * state.zoom, 0, Math.PI * 2);
                    ctx.fillStyle = 'rgba(244, 63, 94, 0.95)';
                    ctx.fill();

                    // Compresión del nervio ciático amarillo
                    ctx.beginPath();
                    ctx.arc(pHernia.x + 8, pHernia.y, 4 * state.zoom, 0, Math.PI * 2);
                    ctx.fillStyle = '#fbbf24';
                    ctx.fill();
                }
            });

            requestAnimationFrame(render);
        }
        render();

        function updateTelemetry() {
            const w = state.weight;
            let force = 0;
            let press = 0;
            const forceEl = document.getElementById('kpiForce');
            const pressEl = document.getElementById('kpiPressure');
            const sciaticEl = document.getElementById('kpiSciatic');
            const statusEl = document.getElementById('kpiStatus');

            if (state.posture === 'back') {
                // Brazo de palanca desfavorable de 40 cm -> Momento flexor masivo
                force = Math.round(1800 + w * 115);
                press = (0.9 + w * 0.07).toFixed(2);
            } else {
                // Rodillas flexionadas, columna recta neutra -> Momento mínimo
                force = Math.round(750 + w * 28);
                press = (0.5 + w * 0.025).toFixed(2);
            }

            if (state.hernia) force += 900;

            forceEl.innerText = `${force.toLocaleString()} N (${Math.round(force / 9.81)} kgf)`;
            pressEl.innerText = `${press} MPa`;

            if (force > 3400 || state.hernia) {
                statusEl.className = 'status-badge status-danger';
                statusEl.innerText = '🚨 Supera Límite NIOSH (>3.400 N)';
                sciaticEl.innerText = 'Pinzamiento Nervioso Agudo';
            } else if (force > 2200) {
                statusEl.className = 'status-badge status-warning';
                statusEl.innerText = '⚠️ Fatiga Discal Acumulada';
                sciaticEl.innerText = 'Canal Estrecho';
            } else {
                statusEl.className = 'status-badge status-healthy';
                statusEl.innerText = 'Zona Ergonómica Segura';
                sciaticEl.innerText = 'Canal Libre Sin Presión';
            }
        }
        setInterval(updateTelemetry, 250);

        document.getElementById('rngWeight').addEventListener('input', (e) => {
            state.weight = parseInt(e.target.value);
            document.getElementById('valWeight').innerText = `${state.weight} kg`;
        });

        document.getElementById('btnPostureKnees').addEventListener('click', () => {
            state.posture = 'knees';
            state.hernia = false;
            document.getElementById('btnPostureKnees').classList.add('active');
            document.getElementById('btnPostureBack').classList.remove('active');
            speak("Técnica ergonómica correcta adoptada. Doblar las rodillas a noventa grados y mantener la carga cerca del centro de gravedad reduce la compresión en L5-S1 en más de un setenta por ciento.");
        });

        document.getElementById('btnPostureBack').addEventListener('click', () => {
            state.posture = 'back';
            document.getElementById('btnPostureBack').classList.add('active');
            document.getElementById('btnPostureKnees').classList.remove('active');
            speak("Peligro ergonómico. Levantar la carga doblando la espalda multiplica el brazo de palanca dorsal, disparando la fuerza compresiva en el disco L5-S1 por encima del umbral de lesión de tres mil cuatrocientos Newtons.");
        });

        document.getElementById('btnHernia').addEventListener('click', () => {
            state.hernia = true;
            state.posture = 'back';
            document.getElementById('btnPostureBack').classList.add('active');
            document.getElementById('btnPostureKnees').classList.remove('active');
            speak("Ruptura del anillo fibroso y hernia del núcleo pulposo en L5-S1. El material gelatinoso protruye hacia el canal posterior comprimiendo la raíz del nervio ciático con dolor irradiado.");
        });

        document.getElementById('btnDecompress').addEventListener('click', () => {
            state.weight = 0;
            state.posture = 'knees';
            state.hernia = false;
            document.getElementById('rngWeight').value = 0;
            document.getElementById('valWeight').innerText = '0 kg';
            document.getElementById('btnPostureKnees').classList.add('active');
            document.getElementById('btnPostureBack').classList.remove('active');
            speak("Columna en descompresión axial neutra. El disco intervertebral se rehidrata por imbibición de proteoglicanos.");
        });

        document.getElementById('btnAudioToggle').addEventListener('click', (e) => {
            state.audioEnabled = !state.audioEnabled;
            e.target.innerText = state.audioEnabled ? '🔊 Audio Alerta: ON' : '🔈 Audio: OFF';
        });

        document.getElementById('btnVoiceGuide').addEventListener('click', () => {
            speak("Bienvenido al simulador tridimensional de Columna Vertebral y Biomecánica Lumbar. Comprueba cómo levantar peso flexionando la cintura daña el disco L5-S1.");
        });

        document.getElementById('btnResetView').addEventListener('click', () => {
            state.rotX = -0.15;
            state.rotY = 0.35;
            state.zoom = 1.0;
        });
    </script>
</body>
</html>
"""

print("Módulos S36, S37 y S38 preparados.")

# -----------------------------------------------------------------------------
# 9. SESIÓN 39: MIMETISMO ÓPTICO: NANOCRISTALES E IRIDISCENCIA DE MARIPOSA 3D
# -----------------------------------------------------------------------------
def get_html_s39():
    return """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesión 39 • Mimetismo Óptico: Nanocristales e Iridiscencia de Mariposa 3D [COD-039]</title>
    <!-- Natural History Museum London • Morpho peleides • Ley de Bragg-Snell • Inmersión Líquida -->
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #010814;
            --bg-panel: rgba(4, 16, 36, 0.94);
            --border: rgba(56, 189, 248, 0.35);
            --primary: #38bdf8;
            --primary-glow: rgba(56, 189, 248, 0.4);
            --morpho-blue: #0284c7;
            --amber: #fbbf24;
            --text-main: #f8fafc;
            --text-sub: #cbd5e1;
            --font-title: 'Cinzel', serif;
            --font-sans: 'Inter', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
        body {
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-sans);
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            font-size: 14px;
        }

        header {
            background: linear-gradient(180deg, rgba(2, 12, 28, 0.98) 0%, rgba(2, 12, 28, 0.88) 100%);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border);
            padding: 10px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-shrink: 0;
            z-index: 40;
        }
        .brand-box { display: flex; align-items: center; gap: 14px; }
        .badge-pill {
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid var(--primary);
            color: var(--primary);
            font-family: var(--font-mono);
            font-weight: 800;
            font-size: 0.82rem;
            padding: 4px 10px;
            border-radius: 6px;
        }
        .title-text h1 {
            font-family: var(--font-title);
            font-size: 1.15rem;
            font-weight: 800;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .title-text p { font-size: 0.78rem; color: var(--text-sub); margin-top: 1px; }

        .header-actions { display: flex; align-items: center; gap: 10px; }
        .btn-header {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: var(--text-main);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .btn-header:hover { background: rgba(56, 189, 248, 0.2); border-color: var(--primary); color: #fff; }

        .workspace { flex: 1; position: relative; overflow: hidden; display: flex; }

        .viewer-container {
            flex: 1;
            position: relative;
            background: radial-gradient(circle at center, #062244 0%, #010814 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        #morphoCanvas {
            max-width: 96%;
            max-height: 92%;
            border-radius: 14px;
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.9);
            border: 1px solid rgba(56, 189, 248, 0.25);
            background: #020c1a;
            cursor: grab;
        }
        #morphoCanvas:active { cursor: grabbing; }

        .controls-panel {
            position: absolute;
            top: 18px;
            left: 20px;
            width: 350px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 18px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 14px;
            max-height: calc(100vh - 120px);
            overflow-y: auto;
        }

        .panel-sec-title {
            font-size: 0.78rem;
            font-family: var(--font-mono);
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 5px;
        }

        .slider-group { display: flex; flex-direction: column; gap: 6px; }
        .slider-label {
            display: flex;
            justify-content: space-between;
            font-size: 0.82rem;
            color: var(--text-sub);
        }
        .slider-val { font-family: var(--font-mono); color: #fff; font-weight: 700; }
        input[type="range"] {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: #1e293b;
            outline: none;
            cursor: pointer;
            accent-color: var(--primary);
        }

        .btn-group { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
        .btn-action {
            background: rgba(56, 189, 248, 0.12);
            border: 1px solid rgba(56, 189, 248, 0.35);
            color: #fff;
            padding: 9px 10px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }
        .btn-action:hover { background: rgba(56, 189, 248, 0.28); border-color: var(--primary); }
        .btn-action.active { background: var(--primary); color: #010814; font-weight: 800; }

        .telemetry-card {
            position: absolute;
            bottom: 20px;
            right: 20px;
            width: 320px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 16px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .kpi-row { display: flex; justify-content: space-between; align-items: center; }
        .kpi-name { font-size: 0.78rem; color: var(--text-sub); }
        .kpi-val { font-family: var(--font-mono); font-size: 0.88rem; font-weight: 700; color: #fff; }
        .status-badge {
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.74rem;
            font-weight: 800;
            text-align: center;
        }
        .status-healthy { background: rgba(56, 189, 248, 0.2); color: #7dd3fc; border: 1px solid #38bdf8; }
        .status-warning { background: rgba(251, 191, 36, 0.2); color: #fde68a; border: 1px solid #fbbf24; }
        .status-brown { background: rgba(180, 83, 9, 0.2); color: #fcd34d; border: 1px solid #b45309; }
    </style>
</head>
<body>
    <header>
        <div class="brand-box">
            <span class="badge-pill">[COD-039]</span>
            <div class="title-text">
                <h1>🦋 Mimetismo Óptico e Iridiscencia de Mariposa 3D</h1>
                <p>Natural History Museum London • Morpho peleides • Nanocristales en Árbol de Navidad • Color Estructural Puro</p>
            </div>
        </div>
        <div class="header-actions">
            <button class="btn-header" id="btnAudioToggle">🔊 Audio Óptico: ON</button>
            <button class="btn-header" id="btnVoiceGuide">🗣️ Guía por Voz</button>
            <button class="btn-header" id="btnResetView">🎯 Centrar Vista</button>
        </div>
    </header>

    <div class="workspace">
        <div class="viewer-container">
            <canvas id="morphoCanvas" width="900" height="650"></canvas>
        </div>

        <div class="controls-panel">
            <div class="panel-sec-title">
                <span>Óptica Física y Ley de Bragg</span>
                <span>🌈 INTERFERENCIA</span>
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Ángulo de Incidencia de la Luz</span>
                    <span class="slider-val" id="valAngle">15° (Normal)</span>
                </div>
                <input type="range" id="rngAngle" min="0" max="75" step="1" value="15">
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Escala de Visualización (Zoom)</span>
                    <span class="slider-val" id="valScale">Nanoestructura (SEM)</span>
                </div>
                <input type="range" id="rngScale" min="1" max="4" step="1" value="4">
            </div>

            <div class="panel-sec-title">
                <span>Prueba de Refracción en Medios</span>
                <span>🧪 EXPERIMENTO</span>
            </div>

            <div class="btn-group">
                <button class="btn-action active" id="btnAir">💨 Aire (n=1.00)</button>
                <button class="btn-action" id="btnWater">💧 Agua (n=1.33)</button>
            </div>

            <div class="btn-group">
                <button class="btn-action" id="btnEthanol">🧪 Etanol (n=1.36)</button>
                <button class="btn-action" id="btnFlap">🦋 Batir Alas</button>
            </div>
        </div>

        <div class="telemetry-card">
            <div class="panel-sec-title">
                <span>Espectrofotometría Multicapa</span>
                <span>Bragg-Snell</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Longitud de Onda Dominante:</span>
                <span class="kpi-val" id="kpiLambda">465 nm (Azul Metálico)</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Reflectancia Especular:</span>
                <span class="kpi-val" id="kpiReflect">84.2 %</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Medio Circundante:</span>
                <span class="kpi-val" id="kpiMedium">Aire (n = 1.00)</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Origen del Color:</span>
                <span class="status-badge status-healthy" id="kpiStatus">Color Físico Estructural</span>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('morphoCanvas');
        const ctx = canvas.getContext('2d');

        let state = {
            angle: 15,
            scaleView: 4, // 1: macro, 2: micro, 3: submicro, 4: nano
            medium: 'air', // 'air', 'water', 'ethanol'
            isFlapping: false,
            rotX: -0.2,
            rotY: 0.35,
            zoom: 1.0,
            audioEnabled: true
        };

        function speak(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const u = new SpeechSynthesisUtterance(text);
                u.lang = 'es-ES';
                u.rate = 1.05;
                window.speechSynthesis.speak(u);
            }
        }

        let isDragging = false;
        let lastMouse = { x: 0, y: 0 };
        canvas.addEventListener('mousedown', (e) => {
            isDragging = true;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        window.addEventListener('mouseup', () => isDragging = false);
        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            const dx = e.clientX - lastMouse.x;
            const dy = e.clientY - lastMouse.y;
            state.rotY += dx * 0.008;
            state.rotX += dy * 0.008;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        canvas.addEventListener('wheel', (e) => {
            e.preventDefault();
            state.zoom *= e.deltaY > 0 ? 0.95 : 1.05;
            state.zoom = Math.max(0.6, Math.min(2.0, state.zoom));
        });

        // Loop de renderizado 3D de la nanoestructura en Árbol de Navidad
        let t = 0;
        function render() {
            t += 0.02;
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            const cx = canvas.width / 2;
            const cy = canvas.height / 2;

            const cosY = Math.cos(state.rotY);
            const sinY = Math.sin(state.rotY);
            const cosX = Math.cos(state.rotX);
            const sinX = Math.sin(state.rotX);

            function project(x, y, z) {
                let x1 = x * cosY + z * sinY;
                let z1 = -x * sinY + z * cosY;
                let y2 = y * cosX - z1 * sinX;
                let z2 = y * sinX + z1 * cosX;
                const fov = 450;
                const scale = (fov / (fov + z2 + 300)) * state.zoom;
                return { x: cx + x1 * scale, y: cy + y2 * scale, z: z2, scale: scale };
            }

            // Cálculo del color según Bragg-Snell y medio líquido
            // Aire: Azul brillante #0284c7 (465 nm) -> vira a violeta #8b5cf6 con ángulo
            // Agua: Vira a verde esmeralda apagado #059669
            // Etanol: Desaparece la interferencia -> Marrón melanina #78350f
            let rCol = 2, gCol = 132, bCol = 199;
            if (state.medium === 'ethanol') {
                rCol = 120; gCol = 65; bCol = 25; // Marrón melanina químico basal
            } else if (state.medium === 'water') {
                rCol = 5; gCol = 150; bCol = 105; // Verde esmeralda
            } else {
                // Aire: desplazamiento angular hacia el violeta
                const shift = state.angle * 1.2;
                rCol = Math.floor(2 + shift * 1.5);
                gCol = Math.floor(132 - shift * 1.1);
                bCol = 220;
            }

            // Vista 4: Nanoestructura de Árbol de Navidad (Lamelas de cutícula separadas 140 nm)
            if (state.scaleView >= 3) {
                const numTrees = 5;
                for (let tr = 0; tr < numTrees; tr++) {
                    const tx = -140 + tr * 70;
                    const pTrunkBot = project(tx, 140, 0);
                    const pTrunkTop = project(tx, -140, 0);

                    // Tallo central de la cresta
                    ctx.beginPath();
                    ctx.moveTo(pTrunkBot.x, pTrunkBot.y);
                    ctx.lineTo(pTrunkTop.x, pTrunkTop.y);
                    ctx.strokeStyle = '#64748b';
                    ctx.lineWidth = 8 * state.zoom;
                    ctx.stroke();

                    // Lamelas laterales escalonadas (cutícula n=1.56)
                    const numBranches = 10;
                    for (let b = 0; b < numBranches; b++) {
                        const by = 120 - b * 26;
                        const bwBranch = (10 - b * 0.7) * 4.5 * state.zoom;

                        const pLeft = project(tx - bwBranch, by, 0);
                        const pRight = project(tx + bwBranch, by, 0);

                        ctx.beginPath();
                        ctx.moveTo(pLeft.x, pLeft.y);
                        ctx.lineTo(pRight.x, pRight.y);
                        ctx.strokeStyle = `rgb(${rCol}, ${gCol}, ${bCol})`;
                        ctx.lineWidth = 5 * state.zoom;
                        ctx.stroke();
                    }
                }

                // Rayos de luz incidente y reflejada por interferencia constructiva
                const pRayTarget = project(0, -20, 0);
                const rayAngRad = (state.angle * Math.PI) / 180;
                const pRaySource = project(-Math.sin(rayAngRad) * 220, -20 - Math.cos(rayAngRad) * 200, 0);
                const pRayReflect = project(Math.sin(rayAngRad) * 220, -20 - Math.cos(rayAngRad) * 200, 0);

                // Rayo incidente blanco
                ctx.setLineDash([6, 6]);
                ctx.strokeStyle = 'rgba(255, 255, 255, 0.7)';
                ctx.lineWidth = 2.5;
                ctx.beginPath();
                ctx.moveTo(pRaySource.x, pRaySource.y);
                ctx.lineTo(pRayTarget.x, pRayTarget.y);
                ctx.stroke();

                // Rayo reflejado con color iridiscente puro
                ctx.strokeStyle = `rgb(${rCol}, ${gCol}, ${bCol})`;
                ctx.lineWidth = 4;
                ctx.beginPath();
                ctx.moveTo(pRayTarget.x, pRayTarget.y);
                ctx.lineTo(pRayReflect.x, pRayReflect.y);
                ctx.stroke();
                ctx.setLineDash([]);
            } else {
                // Vista Macro / Micro: Ala de Morpho peleides con batido alar
                const flapAngle = state.isFlapping ? Math.sin(t * 8) * 0.4 : 0.0;
                const pWingL = project(-180 * Math.cos(flapAngle), -80 * Math.sin(flapAngle), 0);
                const pWingR = project(180 * Math.cos(flapAngle), -80 * Math.sin(flapAngle), 0);
                const pBody = project(0, 40, 0);

                ctx.beginPath();
                ctx.moveTo(pBody.x, pBody.y);
                ctx.lineTo(pWingL.x, pWingL.y);
                ctx.lineTo(cx - 80, cy - 120);
                ctx.closePath();
                ctx.fillStyle = `rgb(${rCol}, ${gCol}, ${bCol})`;
                ctx.fill();

                ctx.beginPath();
                ctx.moveTo(pBody.x, pBody.y);
                ctx.lineTo(pWingR.x, pWingR.y);
                ctx.lineTo(cx + 80, cy - 120);
                ctx.closePath();
                ctx.fillStyle = `rgb(${rCol}, ${gCol}, ${bCol})`;
                ctx.fill();
            }

            requestAnimationFrame(render);
        }
        render();

        function updateTelemetry() {
            const lambdaEl = document.getElementById('kpiLambda');
            const reflectEl = document.getElementById('kpiReflect');
            const medEl = document.getElementById('kpiMedium');
            const statEl = document.getElementById('kpiStatus');

            if (state.medium === 'ethanol') {
                lambdaEl.innerText = 'Color Perdido (580 nm melanina)';
                reflectEl.innerText = '8.5 % (Absorbente)';
                medEl.innerText = 'Etanol (n = 1.36)';
                statEl.className = 'status-badge status-brown';
                statEl.innerText = '⚠️ Prueba Positiva: Cero Pigmento Azul';
            } else if (state.medium === 'water') {
                lambdaEl.innerText = '515 nm (Verde Esmeralda)';
                reflectEl.innerText = '42.0 %';
                medEl.innerText = 'Agua (n = 1.33)';
                statEl.className = 'status-badge status-warning';
                statEl.innerText = 'Desplazamiento Óptico por Agua';
            } else {
                const wl = Math.round(465 - state.angle * 0.9);
                lambdaEl.innerText = `${wl} nm (${wl < 420 ? 'Violeta / UV' : 'Azul Morpho'})`;
                reflectEl.innerText = '84.2 % (Interferencia Constructiva)';
                medEl.innerText = 'Aire (n = 1.00)';
                statEl.className = 'status-badge status-healthy';
                statEl.innerText = 'Color Físico Estructural Puro';
            }
        }
        setInterval(updateTelemetry, 250);

        document.getElementById('rngAngle').addEventListener('input', (e) => {
            state.angle = parseInt(e.target.value);
            document.getElementById('valAngle').innerText = `${state.angle}°`;
        });

        document.getElementById('rngScale').addEventListener('input', (e) => {
            state.scaleView = parseInt(e.target.value);
            const labels = ["", "Mariposa Completa", "Tejas de Escamas", "Crestas Microscópicas", "Nanoestructura (SEM)"];
            document.getElementById('valScale').innerText = labels[state.scaleView];
        });

        document.getElementById('btnAir').addEventListener('click', () => {
            state.medium = 'air';
            document.getElementById('btnAir').classList.add('active');
            document.getElementById('btnWater').classList.remove('active');
            document.getElementById('btnEthanol').classList.remove('active');
            speak("Aire ambiental con índice de refracción uno punto cero cero. Interferencia constructiva máxima en cuatrocientos sesenta y cinco nanómetros generando el azul metálico característico.");
        });

        document.getElementById('btnWater').addEventListener('click', () => {
            state.medium = 'water';
            document.getElementById('btnWater').classList.add('active');
            document.getElementById('btnAir').classList.remove('active');
            document.getElementById('btnEthanol').classList.remove('active');
            speak("Inmersión en agua. El índice de refracción asciende a uno punto treinta y tres, desplazando el pico de reflexión hacia el verde.");
        });

        document.getElementById('btnEthanol').addEventListener('click', () => {
            state.medium = 'ethanol';
            document.getElementById('btnEthanol').classList.add('active');
            document.getElementById('btnAir').classList.remove('active');
            document.getElementById('btnWater').classList.remove('active');
            speak("Experimento de inmersión en etanol. Al coincidir el índice de refracción del solvente con el de la cutícula, la reflexión por interferencia se anula por completo, revelando el color marrón oscuro de la melanina química y demostrando que no existe pigmento azul en el ala.");
        });

        document.getElementById('btnFlap').addEventListener('click', () => {
            state.isFlapping = !state.isFlapping;
            document.getElementById('btnFlap').classList.toggle('active', state.isFlapping);
        });

        document.getElementById('btnAudioToggle').addEventListener('click', (e) => {
            state.audioEnabled = !state.audioEnabled;
            e.target.innerText = state.audioEnabled ? '🔊 Audio Óptico: ON' : '🔈 Audio: OFF';
        });

        document.getElementById('btnVoiceGuide').addEventListener('click', () => {
            speak("Bienvenido al simulador de Mimetismo Óptico e Iridiscencia. Comprueba cómo las lamelas nanoscópicas en forma de árbol de Navidad crean color mediante física de ondas sin usar pigmentos químicos.");
        });

        document.getElementById('btnResetView').addEventListener('click', () => {
            state.rotX = -0.2;
            state.rotY = 0.35;
            state.zoom = 1.0;
        });
    </script>
</body>
</html>
"""

# -----------------------------------------------------------------------------
# 10. SESIÓN 40: REGENERACIÓN TISULAR, FIBROBLASTOS Y MATRIZ EXTRACELULAR 3D
# -----------------------------------------------------------------------------
def get_html_s40():
    return """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesión 40 • Regeneración Tisular, Fibroblastos y Matriz Extracelular 3D [COD-040]</title>
    <!-- NIH 3D • Medicina Regenerativa • Cascada de Cicatrización • Colágeno I/III • Fibroblastos -->
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #060a14;
            --bg-panel: rgba(8, 18, 36, 0.94);
            --border: rgba(56, 189, 248, 0.35);
            --primary: #38bdf8;
            --primary-glow: rgba(56, 189, 248, 0.4);
            --fibro: #34d399;
            --collagen: #fbbf24;
            --wound: #f43f5e;
            --text-main: #f8fafc;
            --text-sub: #cbd5e1;
            --font-title: 'Cinzel', serif;
            --font-sans: 'Inter', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
        body {
            background-color: var(--bg-base);
            color: var(--text-main);
            font-family: var(--font-sans);
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            font-size: 14px;
        }

        header {
            background: linear-gradient(180deg, rgba(6, 14, 28, 0.98) 0%, rgba(6, 14, 28, 0.88) 100%);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border);
            padding: 10px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-shrink: 0;
            z-index: 40;
        }
        .brand-box { display: flex; align-items: center; gap: 14px; }
        .badge-pill {
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid var(--primary);
            color: var(--primary);
            font-family: var(--font-mono);
            font-weight: 800;
            font-size: 0.82rem;
            padding: 4px 10px;
            border-radius: 6px;
        }
        .title-text h1 {
            font-family: var(--font-title);
            font-size: 1.15rem;
            font-weight: 800;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .title-text p { font-size: 0.78rem; color: var(--text-sub); margin-top: 1px; }

        .header-actions { display: flex; align-items: center; gap: 10px; }
        .btn-header {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: var(--text-main);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .btn-header:hover { background: rgba(56, 189, 248, 0.2); border-color: var(--primary); color: #fff; }

        .workspace { flex: 1; position: relative; overflow: hidden; display: flex; }

        .viewer-container {
            flex: 1;
            position: relative;
            background: radial-gradient(circle at center, #0b2242 0%, #060a14 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        #woundCanvas {
            max-width: 96%;
            max-height: 92%;
            border-radius: 14px;
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.9);
            border: 1px solid rgba(56, 189, 248, 0.25);
            background: #040e20;
            cursor: grab;
        }
        #woundCanvas:active { cursor: grabbing; }

        .controls-panel {
            position: absolute;
            top: 18px;
            left: 20px;
            width: 350px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 18px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 14px;
            max-height: calc(100vh - 120px);
            overflow-y: auto;
        }

        .panel-sec-title {
            font-size: 0.78rem;
            font-family: var(--font-mono);
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 5px;
        }

        .slider-group { display: flex; flex-direction: column; gap: 6px; }
        .slider-label {
            display: flex;
            justify-content: space-between;
            font-size: 0.82rem;
            color: var(--text-sub);
        }
        .slider-val { font-family: var(--font-mono); color: #fff; font-weight: 700; }
        input[type="range"] {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: #1e293b;
            outline: none;
            cursor: pointer;
            accent-color: var(--primary);
        }

        .btn-group { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
        .btn-action {
            background: rgba(56, 189, 248, 0.12);
            border: 1px solid rgba(56, 189, 248, 0.35);
            color: #fff;
            padding: 9px 10px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }
        .btn-action:hover { background: rgba(56, 189, 248, 0.28); border-color: var(--primary); }
        .btn-action.active { background: var(--primary); color: #040e20; font-weight: 800; }
        .btn-action.danger { background: rgba(244, 63, 94, 0.15); border-color: #f43f5e; color: #fca5a5; }
        .btn-action.danger:hover { background: #f43f5e; color: #fff; }

        .telemetry-card {
            position: absolute;
            bottom: 20px;
            right: 20px;
            width: 320px;
            background: var(--bg-panel);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 16px;
            backdrop-filter: blur(14px);
            z-index: 20;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .kpi-row { display: flex; justify-content: space-between; align-items: center; }
        .kpi-name { font-size: 0.78rem; color: var(--text-sub); }
        .kpi-val { font-family: var(--font-mono); font-size: 0.88rem; font-weight: 700; color: #fff; }
        .status-badge {
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.74rem;
            font-weight: 800;
            text-align: center;
        }
        .status-healthy { background: rgba(52, 211, 153, 0.2); color: #6ee7b7; border: 1px solid #34d399; }
        .status-warning { background: rgba(251, 191, 36, 0.2); color: #fde68a; border: 1px solid #fbbf24; }
        .status-wound { background: rgba(244, 63, 94, 0.2); color: #fda4af; border: 1px solid #f43f5e; }
    </style>
</head>
<body>
    <header>
        <div class="brand-box">
            <span class="badge-pill">[COD-040]</span>
            <div class="title-text">
                <h1>🔬 Regeneración Tisular y Matriz Extracelular 3D</h1>
                <p>NIH 3D • Medicina Regenerativa • Cascada de Cicatrización • Migración de Fibroblastos • Colágeno Tipo I/III</p>
            </div>
        </div>
        <div class="header-actions">
            <button class="btn-header" id="btnAudioToggle">🔊 Audio Pulso: ON</button>
            <button class="btn-header" id="btnVoiceGuide">🗣️ Guía por Voz</button>
            <button class="btn-header" id="btnResetView">🎯 Centrar Vista</button>
        </div>
    </header>

    <div class="workspace">
        <div class="viewer-container">
            <canvas id="woundCanvas" width="900" height="650"></canvas>
        </div>

        <div class="controls-panel">
            <div class="panel-sec-title">
                <span>Cronología de Cicatrización</span>
                <span>⏱️ CASCADA</span>
            </div>

            <div class="slider-group">
                <div class="slider-label">
                    <span>Línea de Tiempo (Días)</span>
                    <span class="slider-val" id="valDays">Día 5 (Proliferación)</span>
                </div>
                <input type="range" id="rngDays" min="0" max="28" step="1" value="5">
            </div>

            <div class="panel-sec-title">
                <span>Comorbilidades y Factores</span>
                <span>🩺 FISIOPATOLOGÍA</span>
            </div>

            <div class="btn-group">
                <button class="btn-action danger" id="btnDiabetes">🍬 Hiperglucemia</button>
                <button class="btn-action" id="btnOxygen">🫧 Oxigenoterapia</button>
            </div>

            <div class="btn-group">
                <button class="btn-action active" id="btnPlayAuto">▶️ Auto-Evolución</button>
                <button class="btn-action" id="btnFreshWound">🩸 Nueva Herida</button>
            </div>
        </div>

        <div class="telemetry-card">
            <div class="panel-sec-title">
                <span>Cinética de Reparación Tisular</span>
                <span>Clark & Singer</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Fase Activa:</span>
                <span class="status-badge status-warning" id="kpiPhase">Fase 3: Proliferativa</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Cierre de la Brecha:</span>
                <span class="kpi-val" id="kpiClosure">58 %</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Resistencia Mecánica:</span>
                <span class="kpi-val" id="kpiTensile">32 % del tejido sano</span>
            </div>
            <div class="kpi-row">
                <span class="kpi-name">Ratio Colágeno (I / III):</span>
                <span class="kpi-val" id="kpiCollagen">Ratio 1.4 (Granulación)</span>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('woundCanvas');
        const ctx = canvas.getContext('2d');

        let state = {
            day: 5,
            diabetes: false,
            oxygen: false,
            isAuto: false,
            rotX: -0.2,
            rotY: 0.35,
            zoom: 1.0,
            audioEnabled: true
        };

        function speak(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const u = new SpeechSynthesisUtterance(text);
                u.lang = 'es-ES';
                u.rate = 1.05;
                window.speechSynthesis.speak(u);
            }
        }

        let isDragging = false;
        let lastMouse = { x: 0, y: 0 };
        canvas.addEventListener('mousedown', (e) => {
            isDragging = true;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        window.addEventListener('mouseup', () => isDragging = false);
        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            const dx = e.clientX - lastMouse.x;
            const dy = e.clientY - lastMouse.y;
            state.rotY += dx * 0.008;
            state.rotX += dy * 0.008;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        canvas.addEventListener('wheel', (e) => {
            e.preventDefault();
            state.zoom *= e.deltaY > 0 ? 0.95 : 1.05;
            state.zoom = Math.max(0.6, Math.min(2.0, state.zoom));
        });

        // Loop de renderizado 3D de la Brecha de la Herida y Migración Fibroblástica
        let t = 0;
        function render() {
            t += 0.02;

            if (state.isAuto && Math.floor(t * 30) % 25 === 0) {
                state.day = (state.day + 1) % 29;
                document.getElementById('rngDays').value = state.day;
            }

            ctx.clearRect(0, 0, canvas.width, canvas.height);

            const cx = canvas.width / 2;
            const cy = canvas.height / 2;

            const cosY = Math.cos(state.rotY);
            const sinY = Math.sin(state.rotY);
            const cosX = Math.cos(state.rotX);
            const sinX = Math.sin(state.rotX);

            function project(x, y, z) {
                let x1 = x * cosY + z * sinY;
                let z1 = -x * sinY + z * cosY;
                let y2 = y * cosX - z1 * sinX;
                let z2 = y * sinX + z1 * cosX;
                const fov = 450;
                const scale = (fov / (fov + z2 + 300)) * state.zoom;
                return { x: cx + x1 * scale, y: cy + y2 * scale, z: z2, scale: scale };
            }

            // Ancho de la brecha de la herida disminuye con el día
            let closureFrac = Math.min(1.0, state.day / 24.0);
            if (state.diabetes) closureFrac *= 0.45;
            if (state.oxygen) closureFrac = Math.min(1.0, closureFrac * 1.35);

            const gapWidth = 140 * (1 - closureFrac * 0.85);

            // Tejido dérmico periférico sano
            const pLeftTissue = project(-180, 0, 0);
            const pLeftEdge = project(-gapWidth / 2, 0, 0);
            const pRightEdge = project(gapWidth / 2, 0, 0);
            const pRightTissue = project(180, 0, 0);

            // Bloque tisular izquierdo
            ctx.beginPath();
            ctx.moveTo(pLeftTissue.x, pLeftTissue.y - 70 * state.zoom);
            ctx.lineTo(pLeftEdge.x, pLeftEdge.y - 70 * state.zoom);
            ctx.lineTo(pLeftEdge.x, pLeftEdge.y + 70 * state.zoom);
            ctx.lineTo(pLeftTissue.x, pLeftTissue.y + 70 * state.zoom);
            ctx.closePath();
            ctx.fillStyle = '#f87171';
            ctx.fill();

            // Bloque tisular derecho
            ctx.beginPath();
            ctx.moveTo(pRightEdge.x, pRightEdge.y - 70 * state.zoom);
            ctx.lineTo(pRightTissue.x, pRightTissue.y - 70 * state.zoom);
            ctx.lineTo(pRightTissue.x, pRightTissue.y + 70 * state.zoom);
            ctx.lineTo(pRightEdge.x, pRightEdge.y + 70 * state.zoom);
            ctx.closePath();
            ctx.fillStyle = '#f87171';
            ctx.fill();

            // Lecho central de la herida
            ctx.beginPath();
            ctx.moveTo(pLeftEdge.x, pLeftEdge.y - 70 * state.zoom);
            ctx.lineTo(pRightEdge.x, pRightEdge.y - 70 * state.zoom);
            ctx.lineTo(pRightEdge.x, pRightEdge.y + 70 * state.zoom);
            ctx.lineTo(pLeftEdge.x, pLeftEdge.y + 70 * state.zoom);
            ctx.closePath();
            // Si día 0-2 = coágulo de fibrina rojo oscuro #881337
            // Si día 3-10 = tejido de granulación rosado vascular #fb7185
            // Si día > 14 = cicatriz de colágeno maduro organizada #fbcfe8
            let bedColor = '#881337';
            if (state.day >= 14) bedColor = '#fbcfe8';
            else if (state.day >= 3) bedColor = '#fb7185';
            ctx.fillStyle = bedColor;
            ctx.fill();

            // Red de colágeno sintetizada por fibroblastos (hilos en 3D)
            const numFibers = Math.floor(state.day * 2.2);
            ctx.strokeStyle = state.day >= 14 ? '#fbbf24' : 'rgba(255, 255, 255, 0.45)';
            ctx.lineWidth = 1.5;
            for (let f = 0; f < numFibers; f++) {
                const fx1 = -gapWidth / 2 + Math.sin(f * 1.5) * 15;
                const fx2 = gapWidth / 2 - Math.cos(f * 1.5) * 15;
                const fy = -55 + (f * 9) % 110;
                const pf1 = project(fx1, fy, Math.sin(f) * 20);
                const pf2 = project(fx2, fy, Math.cos(f) * 20);
                ctx.beginPath();
                ctx.moveTo(pf1.x, pf1.y);
                ctx.lineTo(pf2.x, pf2.y);
                ctx.stroke();
            }

            // Fibroblastos fusiformes migrando hacia el centro
            const numFibro = Math.min(18, state.day * 2);
            ctx.fillStyle = '#34d399';
            for (let b = 0; b < numFibro; b++) {
                const side = (b % 2 === 0 ? -1 : 1);
                const bx = side * (gapWidth / 2 - (state.day * 1.8) + (b * 3));
                const by = -50 + (b * 12) % 100;
                const prFibro = project(bx, by, 10);
                ctx.beginPath();
                ctx.ellipse(prFibro.x, prFibro.y, 8 * state.zoom, 3 * state.zoom, 0.3 * side, 0, Math.PI * 2);
                ctx.fill();
            }

            requestAnimationFrame(render);
        }
        render();

        function updateTelemetry() {
            const day = state.day;
            const phaseEl = document.getElementById('kpiPhase');
            const closureEl = document.getElementById('kpiClosure');
            const tensileEl = document.getElementById('kpiTensile');
            const colEl = document.getElementById('kpiCollagen');

            let closure = Math.min(100, Math.round((day / 24.0) * 100));
            if (state.diabetes) closure = Math.round(closure * 0.45);
            if (state.oxygen) closure = Math.min(100, Math.round(closure * 1.35));

            let tensile = Math.min(80, Math.round((day / 28.0) * 75));

            closureEl.innerText = `${closure} %`;
            tensileEl.innerText = `${tensile} % del tejido original`;

            if (day <= 1) {
                phaseEl.className = 'status-badge status-wound';
                phaseEl.innerText = 'Fase 1: Hemostasia (Coágulo)';
                colEl.innerText = 'Fibrina / Plaquetas Activas';
            } else if (day <= 4) {
                phaseEl.className = 'status-badge status-wound';
                phaseEl.innerText = 'Fase 2: Inflamación (Macrófagos)';
                colEl.innerText = 'Desbridamiento Tisular M1';
            } else if (day <= 14) {
                phaseEl.className = 'status-badge status-warning';
                phaseEl.innerText = 'Fase 3: Proliferativa (Granulación)';
                colEl.innerText = 'Colágeno Tipo III (Abundante)';
            } else {
                phaseEl.className = 'status-badge status-healthy';
                phaseEl.innerText = 'Fase 4: Remodelación / Matriz';
                colEl.innerText = 'Colágeno Tipo I (Resistencia Tensil)';
            }

            document.getElementById('valDays').innerText = `Día ${day} (${phaseEl.innerText})`;
        }
        setInterval(updateTelemetry, 250);

        document.getElementById('rngDays').addEventListener('input', (e) => {
            state.day = parseInt(e.target.value);
            state.isAuto = false;
            document.getElementById('btnPlayAuto').classList.remove('active');
        });

        document.getElementById('btnDiabetes').addEventListener('click', () => {
            state.diabetes = !state.diabetes;
            document.getElementById('btnDiabetes').classList.toggle('active', state.diabetes);
            if (state.diabetes) speak("Comorbilidad por hiperglucemia y diabetes mellitus activada. Retrasa la transición de macrófagos a fenotipo reparador M2 y bloquea la angiogénesis.");
        });

        document.getElementById('btnOxygen').addEventListener('click', () => {
            state.oxygen = !state.oxygen;
            document.getElementById('btnOxygen').classList.toggle('active', state.oxygen);
            if (state.oxygen) speak("Terapia de oxigenación hiperbárica. Aumenta la síntesis de colágeno por los fibroblastos acelerando la proliferación.");
        });

        document.getElementById('btnPlayAuto').addEventListener('click', () => {
            state.isAuto = !state.isAuto;
            document.getElementById('btnPlayAuto').classList.toggle('active', state.isAuto);
        });

        document.getElementById('btnFreshWound').addEventListener('click', () => {
            state.day = 0;
            state.isAuto = false;
            document.getElementById('rngDays').value = 0;
            document.getElementById('btnPlayAuto').classList.remove('active');
            speak("Nueva lesión tisular aguda. Coagulación inmediata con polimerización de fibrina y agregación plaquetaria.");
        });

        document.getElementById('btnAudioToggle').addEventListener('click', (e) => {
            state.audioEnabled = !state.audioEnabled;
            e.target.innerText = state.audioEnabled ? '🔊 Audio Pulso: ON' : '🔈 Audio: OFF';
        });

        document.getElementById('btnVoiceGuide').addEventListener('click', () => {
            speak("Bienvenido al simulador tridimensional de Regeneración Tisular y Matriz Extracelular. Sigue la cronología de veintiocho días para presenciar la migración de fibroblastos y la síntesis de colágeno.");
        });

        document.getElementById('btnResetView').addEventListener('click', () => {
            state.rotX = -0.2;
            state.rotY = 0.35;
            state.zoom = 1.0;
        });
    </script>
</body>
</html>
"""

# -----------------------------------------------------------------------------
# EJECUTOR MAESTRO DE GENERACIÓN Y ESPEJADO DUAL
# -----------------------------------------------------------------------------
SIMULATORS = [
    (31, "SIMULADOR_ARRECIFE_CORAL_3D.html", get_html_s31),
    (32, "SIMULADOR_RED_TROFICA_3D.html", get_html_s32),
    (33, "SIMULADOR_MITOCONDRIA_3D.html", get_html_s33),
    (34, "SIMULADOR_TELOMEROS_3D.html", get_html_s34),
    (35, "SIMULADOR_SELVA_TROPICAL_3D.html", get_html_s35),
    (36, "SIMULADOR_CANAL_IONICO_3D.html", get_html_s36),
    (37, "SIMULADOR_PIEL_HUMANA_3D.html", get_html_s37),
    (38, "SIMULADOR_COLUMNA_VERTEBRAL_3D.html", get_html_s38),
    (39, "SIMULADOR_IRIDISCENCIA_3D.html", get_html_s39),
    (40, "SIMULADOR_REGENERACION_TISULAR_3D.html", get_html_s40),
]

def main():
    print("=" * 80)
    print("🚀 GENERANDO Y ESPEJANDO 10 SIMULADORES CIENTÍFICOS 3D DEL LOTE 4 [COD]")
    print("=" * 80)

    for sesion_num, filename, get_html_func in SIMULATORS:
        html_content = get_html_func()

        # 1. Guardar en SIMULADORES_INTERACTIVOS/01_SIMULADORES/
        path_sim = os.path.join(SIM_DIR, filename)
        with open(path_sim, "w", encoding="utf-8") as f:
            f.write(html_content)

        # 2. Espejar en CLASES/.../XX_Sesion/
        session_folder = os.path.join(SESSIONS_DIR, f"{sesion_num:02d}_Sesion")
        os.makedirs(session_folder, exist_ok=True)
        path_session = os.path.join(session_folder, filename)
        with open(path_session, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"✅ Sesión {sesion_num:02d}: {filename} -> 2 copias sincronizadas.")

    print("=" * 80)
    print("🎉 10 SIMULADORES 3D GENERADOS Y ESPEJADOS EXITOSAMENTE.")
    print("=" * 80)

if __name__ == '__main__':
    main()

