#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_visores_infografias.py
Genera visores interactivos HTML5 a pantalla completa para las infografías de NotebookLM:
- Sesión 04: VISOR_INFOGRAFIA_MAQUINA_HISTORIA_IA.html
- Sesión 06: VISOR_INFOGRAFIA_PLAN_MAESTRO_VERTICAL_IA.html

Características:
- Cero bordes muertos: la imagen se expande al 100% de la pantalla (100vw, 100vh, object-fit: contain).
- Zoom interactivo (+ / - / rueda del ratón / pellizco táctil en iPad).
- Arrastre libre (pan) para explorar cada detalle técnico.
- Botón de Pantalla Completa nativa (requestFullscreen).
- Acceso directo a la Ficha Didáctica PDF con los prompts de reflexión de Gemini.
- Triple Escudo Anti-Apagado (WakeLock) para iPad y tablets.
"""

import os

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>{title} • Visor Oficial HD</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-user-select: none;
            user-select: none;
        }}
        html, body {{
            width: 100%;
            height: 100%;
            overflow: hidden;
            background-color: #050811;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            color: #ffffff;
        }}
        
        /* BARRA SUPERIOR FLOTANTE */
        .hud-toolbar {{
            position: fixed;
            top: 14px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 100;
            display: flex;
            align-items: center;
            gap: 8px;
            background: rgba(15, 23, 42, 0.88);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 40px;
            padding: 6px 14px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            transition: opacity 0.3s ease, transform 0.3s ease;
        }}
        .hud-toolbar.dimmed {{
            opacity: 0.25;
        }}
        .hud-toolbar:hover {{
            opacity: 1;
        }}
        
        .hud-title {{
            font-size: 0.82rem;
            font-weight: 700;
            color: #38bdf8;
            padding-right: 10px;
            border-right: 1px solid rgba(255, 255, 255, 0.2);
            white-space: nowrap;
            letter-spacing: 0.3px;
        }}
        
        .hud-btn {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #f8fafc;
            font-size: 0.8rem;
            font-weight: 600;
            padding: 6px 12px;
            border-radius: 20px;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: all 0.15s ease;
            text-decoration: none;
            white-space: nowrap;
        }}
        .hud-btn:hover {{
            background: rgba(56, 189, 248, 0.25);
            border-color: #38bdf8;
            color: #38bdf8;
            transform: translateY(-1px);
        }}
        .hud-btn:active {{
            transform: scale(0.96);
        }}
        .hud-btn-primary {{
            background: linear-gradient(135deg, #0284c7, #2563eb);
            border-color: #60a5fa;
            color: #ffffff;
        }}
        .hud-btn-primary:hover {{
            background: linear-gradient(135deg, #0369a1, #1d4ed8);
            color: #ffffff;
        }}
        
        .zoom-display {{
            font-size: 0.78rem;
            font-weight: 700;
            color: #94a3b8;
            min-width: 44px;
            text-align: center;
        }}

        /* CONTENEDOR DE LA IMAGEN (CANVAS INTERACTIVO) */
        #viewport {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: grab;
            overflow: hidden;
            touch-action: none;
        }}
        #viewport.grabbing {{
            cursor: grabbing;
        }}
        
        #image-wrapper {{
            position: absolute;
            transform-origin: center center;
            will-change: transform;
            transition: transform 0.05s linear;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: 100%;
        }}
        
        #main-img {{
            max-width: 100vw;
            max-height: 100vh;
            width: 100%;
            height: 100%;
            object-fit: contain;
            pointer-events: none;
            filter: drop-shadow(0 15px 35px rgba(0, 0, 0, 0.8));
        }}
        
        /* HINT FLOTANTE INFERIOR */
        .bottom-hint {{
            position: fixed;
            bottom: 12px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 0.72rem;
            color: rgba(255, 255, 255, 0.45);
            background: rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(6px);
            padding: 4px 12px;
            border-radius: 12px;
            pointer-events: none;
            transition: opacity 0.4s ease;
        }}
    </style>
</head>
<body>

    <!-- BARRA HUD -->
    <div class="hud-toolbar" id="toolbar">
        <span class="hud-title">{badge}</span>
        <button class="hud-btn" id="btn-zoom-out" title="Alejar (Zoom -)">🔍 -</button>
        <span class="zoom-display" id="zoom-val">100%</span>
        <button class="hud-btn" id="btn-zoom-in" title="Acercar (Zoom +)">🔍 +</button>
        <button class="hud-btn" id="btn-reset" title="Ajustar a Pantalla">↺ Ajustar</button>
        <button class="hud-btn" id="btn-100" title="Ver al 100% Nativo">1:1</button>
        <button class="hud-btn" id="btn-fullscreen" title="Modo Pantalla Completa">⛶ Pantalla Completa</button>
        <a href="{pdf_href}" target="_blank" class="hud-btn hud-btn-primary" title="Abrir Ficha Didáctica y Preguntas (PDF)">📄 Ficha PDF ↗</a>
    </div>

    <!-- VIEWPORT CON IMAGEN -->
    <div id="viewport">
        <div id="image-wrapper">
            <img id="main-img" src="{img_src}" alt="{title}">
        </div>
    </div>

    <div class="bottom-hint" id="hint">💡 Usa la rueda del ratón o pellizca en la pantalla para hacer zoom • Arrastra para explorar</div>

    <script>
        // CONFIGURACIÓN Y ESTADO
        let scale = 1.0;
        let translateX = 0;
        let translateY = 0;
        const MIN_SCALE = 0.8;
        const MAX_SCALE = 5.0;
        
        const viewport = document.getElementById('viewport');
        const wrapper = document.getElementById('image-wrapper');
        const zoomVal = document.getElementById('zoom-val');
        const toolbar = document.getElementById('toolbar');
        const hint = document.getElementById('hint');
        
        function updateTransform() {{
            wrapper.style.transform = `translate(${{translateX}}px, ${{translateY}}px) scale(${{scale}})`;
            zoomVal.textContent = Math.round(scale * 100) + '%';
        }}

        function setZoom(newScale, centerX = window.innerWidth / 2, centerY = window.innerHeight / 2) {{
            newScale = Math.max(MIN_SCALE, Math.min(MAX_SCALE, newScale));
            const factor = newScale / scale;
            translateX = centerX - (centerX - translateX) * factor;
            translateY = centerY - (centerY - translateY) * factor;
            scale = newScale;
            updateTransform();
        }}

        function resetView() {{
            scale = 1.0;
            translateX = 0;
            translateY = 0;
            updateTransform();
        }}

        function fitToWidth() {{
            scale = 1.6;
            translateX = 0;
            translateY = 0;
            updateTransform();
        }}

        // BOTONES HUD
        document.getElementById('btn-zoom-in').addEventListener('click', (e) => {{
            e.stopPropagation();
            setZoom(scale * 1.25);
        }});
        document.getElementById('btn-zoom-out').addEventListener('click', (e) => {{
            e.stopPropagation();
            setZoom(scale / 1.25);
        }});
        document.getElementById('btn-reset').addEventListener('click', (e) => {{
            e.stopPropagation();
            resetView();
        }});
        document.getElementById('btn-100').addEventListener('click', (e) => {{
            e.stopPropagation();
            setZoom(1.5);
        }});
        
        // PANTALLA COMPLETA
        const btnFs = document.getElementById('btn-fullscreen');
        btnFs.addEventListener('click', (e) => {{
            e.stopPropagation();
            if (!document.fullscreenElement) {{
                document.documentElement.requestFullscreen().catch(() => {{}});
                btnFs.textContent = '✖ Salir';
            }} else {{
                document.exitFullscreen().catch(() => {{}});
                btnFs.textContent = '⛶ Pantalla Completa';
            }}
        }});
        document.addEventListener('fullscreenchange', () => {{
            if (!document.fullscreenElement) {{
                btnFs.textContent = '⛶ Pantalla Completa';
            }} else {{
                btnFs.textContent = '✖ Salir';
            }}
        }});

        // ARRASTRE CON RATÓN (PANNING)
        let isDragging = false;
        let startX = 0;
        let startY = 0;

        viewport.addEventListener('mousedown', (e) => {{
            if (e.button !== 0) return;
            isDragging = true;
            startX = e.clientX - translateX;
            startY = e.clientY - translateY;
            viewport.classList.add('grabbing');
        }});

        window.addEventListener('mousemove', (e) => {{
            if (!isDragging) return;
            translateX = e.clientX - startX;
            translateY = e.clientY - startY;
            updateTransform();
        }});

        window.addEventListener('mouseup', () => {{
            isDragging = false;
            viewport.classList.remove('grabbing');
        }});

        // ZOOM CON RUEDA DEL RATÓN
        viewport.addEventListener('wheel', (e) => {{
            e.preventDefault();
            const delta = e.deltaY < 0 ? 1.15 : 0.85;
            setZoom(scale * delta, e.clientX, e.clientY);
        }}, {{ passive: false }});

        // DOBLE CLIC PARA ZOOM RÁPIDO
        viewport.addEventListener('dblclick', (e) => {{
            if (scale > 1.2) {{
                resetView();
            }} else {{
                setZoom(2.2, e.clientX, e.clientY);
            }}
        }});

        // GESTIÓN TÁCTIL (IPAD / MÓVIL: PAN Y PINCH-TO-ZOOM)
        let touchStartDist = 0;
        let touchStartScale = 1;
        let touchStartMidX = 0;
        let touchStartMidY = 0;
        let touchStartX = 0;
        let touchStartY = 0;

        function getTouchDist(e) {{
            const dx = e.touches[0].clientX - e.touches[1].clientX;
            const dy = e.touches[0].clientY - e.touches[1].clientY;
            return Math.sqrt(dx * dx + dy * dy);
        }}

        viewport.addEventListener('touchstart', (e) => {{
            if (e.touches.length === 1) {{
                isDragging = true;
                touchStartX = e.touches[0].clientX - translateX;
                touchStartY = e.touches[0].clientY - translateY;
            }} else if (e.touches.length === 2) {{
                isDragging = false;
                touchStartDist = getTouchDist(e);
                touchStartScale = scale;
                touchStartMidX = (e.touches[0].clientX + e.touches[1].clientX) / 2;
                touchStartMidY = (e.touches[0].clientY + e.touches[1].clientY) / 2;
            }}
        }}, {{ passive: true }});

        viewport.addEventListener('touchmove', (e) => {{
            if (e.touches.length === 1 && isDragging) {{
                translateX = e.touches[0].clientX - touchStartX;
                translateY = e.touches[0].clientY - touchStartY;
                updateTransform();
            }} else if (e.touches.length === 2) {{
                const dist = getTouchDist(e);
                if (touchStartDist > 0) {{
                    const factor = dist / touchStartDist;
                    setZoom(touchStartScale * factor, touchStartMidX, touchStartMidY);
                }}
            }}
        }}, {{ passive: true }});

        viewport.addEventListener('touchend', () => {{
            isDragging = false;
        }});

        // AUTO-DIMMING DE LA BARRA AL ESTAR INACTIVO (ERGONOMÍA VISUAL)
        let dimTimeout;
        function resetDim() {{
            toolbar.classList.remove('dimmed');
            clearTimeout(dimTimeout);
            dimTimeout = setTimeout(() => {{
                toolbar.classList.add('dimmed');
            }}, 4000);
        }}
        window.addEventListener('mousemove', resetDim);
        window.addEventListener('touchstart', resetDim);
        resetDim();

        setTimeout(() => {{
            if (hint) hint.style.opacity = '0';
        }}, 5000);

        // ESCUDO ANTI-APAGADO PARA IPAD / TABLETS (WAKELOCK)
        async function activarWakeLock() {{
            try {{
                if ('wakeLock' in navigator) {{
                    await navigator.wakeLock.request('screen');
                }}
            }} catch (err) {{}}
        }}
        document.addEventListener('click', activarWakeLock, {{ once: true }});
        activarWakeLock();
    </script>
</body>
</html>
"""

def generate_visores():
    base_dir = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
    s04_dir = os.path.join(base_dir, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/04_Sesion")
    s06_dir = os.path.join(base_dir, "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/06_Sesion")

    # 1. Sesión 04
    html_04 = HTML_TEMPLATE.format(
        title="La IA es la Máquina Más Grande de la Historia",
        badge="SESIÓN 04 • INFOGRAFÍA DE ALTA DEFINICIÓN",
        img_src="1.%20INFO-004_La_IA_es_la_Maquina_Mas_Grande_de_la_Historia.jpg",
        pdf_href="1.%20INFO-004_La_IA_es_la_Maquina_Mas_Grande_de_la_Historia.pdf"
    )
    dest_04 = os.path.join(s04_dir, "VISOR_INFOGRAFIA_MAQUINA_HISTORIA_IA.html")
    with open(dest_04, "w", encoding="utf-8") as f:
        f.write(html_04)
    print(f"✅ Visor generado: {dest_04}")

    # 2. Sesión 06
    html_06 = HTML_TEMPLATE.format(
        title="El Plan Maestro de Integración Vertical en IA",
        badge="SESIÓN 06 • INFOGRAFÍA DE ALTA DEFINICIÓN",
        img_src="1.%20INFO-006_El_Plan_Maestro_de_Integracion_Vertical_de_IA.jpg",
        pdf_href="1.%20INFO-006_El_Plan_Maestro_de_Integracion_Vertical_de_IA.pdf"
    )
    dest_06 = os.path.join(s06_dir, "VISOR_INFOGRAFIA_PLAN_MAESTRO_VERTICAL_IA.html")
    with open(dest_06, "w", encoding="utf-8") as f:
        f.write(html_06)
    print(f"✅ Visor generado: {dest_06}")

if __name__ == "__main__":
    generate_visores()
