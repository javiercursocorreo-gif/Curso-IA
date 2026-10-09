#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
setup_photorealistic_lungs.py
Descarga e integra el modelo 3D anatómico real de Pulmones (formato GLB fotogramétrico / médico)
del NIH 3D Medical Repository / Visible Human Project para lograr calidad fotográfica idéntica a heart.glb.
"""

import os
import sys
import base64
import urllib.request
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIM_DIR = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS")
S01_DIR = os.path.join(ROOT_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM", "01_Sesion")

GLB_DEST = os.path.join(SIM_DIR, "lungs.glb")
B64_DEST = os.path.join(SIM_DIR, "lungs_b64.js")

# URLs oficiales de modelos médicos abiertos en GLB (NIH 3D Print Exchange / Visible Human)
CANDIDATE_URLS = [
    # Modelo 1: 3DPX-021148 - Lungs & Bronchi (while breathing)
    "https://nih3d-v2-data-cln-media-prod.s3.amazonaws.com/2119467/lungs_bronchi-nih3d.glb",
    # Modelo 2: 3DPX-013408 - Visible Human Male Respiratory System (NLM)
    "https://nih3d-v2-data-cln-media-prod.s3.amazonaws.com/1040029/vhm_respiratory_viewer_0_0-nih3d.glb",
    # Modelo 3: 3DPX-021008 - HRA Male Lung Reference Organ
    "https://nih3d-v2-data-cln-media-prod.s3.amazonaws.com/2111105/3d-vh-f-lung-nih3d.glb"
]

def download_realistic_lungs():
    os.makedirs(SIM_DIR, exist_ok=True)
    if os.path.exists(GLB_DEST) and os.path.getsize(GLB_DEST) > 500000:
        print(f"✅ Archivo lungs.glb ya existente ({os.path.getsize(GLB_DEST) / 1024 / 1024:.2f} MB)")
        return True

    print("🌐 Descargando modelo 3D hiperrealista de pulmones desde NIH 3D Medical...")
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}

    for url in CANDIDATE_URLS:
        try:
            print(f"   Intentando: {url} ...")
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as response, open(GLB_DEST, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
            size_mb = os.path.getsize(GLB_DEST) / 1024 / 1024
            if size_mb > 0.2:
                print(f"✅ Descarga completada con éxito: {size_mb:.2f} MB")
                return True
        except Exception as e:
            print(f"   ⚠️ Error en URL ({e}), probando alternativa...")

    return False

def generate_base64_js():
    if not os.path.exists(GLB_DEST):
        print("❌ No se encontró lungs.glb para generar base64")
        return False
    
    print("📦 Empaquetando lungs.glb en base64 para carga instantánea offline...")
    with open(GLB_DEST, "rb") as f:
        data = f.read()
    b64_str = base64.b64encode(data).decode('utf-8')
    js_content = f'window.LUNGS_GLB_B64 = "data:model/gltf-binary;base64,{b64_str}";\n'
    with open(B64_DEST, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"✅ Creado lungs_b64.js ({os.path.getsize(B64_DEST) / 1024 / 1024:.2f} MB)")
    return True

def build_photorealistic_lungs_html():
    print("🎨 Construyendo SIMULADOR_PULMONES_3D.html fotorealista con Babylon.js...")
    html_code = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laboratorio Anatómico 3D • Árbol Bronquial y Pulmones Hiperrealistas (GLB + Babylon.js)</title>
    <!-- Babylon.js Motor 3D Oficial CDN -->
    <script src="https://cdn.babylonjs.com/babylon.js"></script>
    <script src="https://cdn.babylonjs.com/loaders/babylonjs.loaders.min.js"></script>
    <!-- Base64 y fallback CDN -->
    <script src="lungs_b64.js"></script>
    <script src="https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/lungs_b64.js"></script>
    <style>
        :root {
            --bg-base: #060913;
            --bg-card: rgba(15, 23, 42, 0.90);
            --border: rgba(56, 189, 248, 0.35);
            --primary: #38bdf8;
            --emerald: #34d399;
            --rose: #fb7185;
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
            --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }

        body {
            font-family: var(--font-sans);
            background: radial-gradient(circle at 50% 30%, #0d1a30 0%, #060913 85%, #020408 100%);
            color: var(--text-main);
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        /* OVERLAY DE CARGA */
        #loadingOverlay {
            position: absolute; inset: 0; z-index: 100;
            background: #060913;
            display: flex; flex-direction: column;
            align-items: center; justify-content: center; gap: 16px;
            transition: opacity 0.5s ease;
        }
        .spinner {
            width: 50px; height: 50px;
            border: 4px solid rgba(56, 189, 248, 0.2);
            border-top: 4px solid var(--primary);
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        @keyframes spin { 100% { transform: rotate(360deg); } }

        /* HEADER */
        header {
            position: absolute; top: 16px; left: 20px; right: 20px; z-index: 10;
            display: flex; justify-content: space-between; align-items: center;
            pointer-events: none;
        }
        .brand-card {
            background: var(--bg-card);
            backdrop-filter: blur(14px);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 12px 20px;
            display: flex; align-items: center; gap: 14px;
            pointer-events: auto;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        }
        .brand-icon {
            font-size: 1.8rem;
            background: rgba(56, 189, 248, 0.15);
            padding: 4px 10px; border-radius: 12px;
        }
        .brand-title { font-size: 1.05rem; font-weight: 800; color: #fff; }
        .brand-sub { font-size: 0.74rem; color: var(--text-sub); }

        .live-tag {
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.4);
            color: #34d399;
            padding: 6px 14px; border-radius: 9999px;
            font-size: 0.75rem; font-weight: 700;
            display: flex; align-items: center; gap: 8px;
            pointer-events: auto;
        }
        .pulse-dot {
            width: 8px; height: 8px; border-radius: 50%;
            background: #10b981;
            box-shadow: 0 0 10px #10b981;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse { 0%,100% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.3); opacity: 0.5; } }

        /* CANVAS 3D */
        #renderCanvas {
            width: 100vw; height: 100vh;
            display: block; outline: none;
        }

        /* HUD CONTROLES DERECHA */
        .hud-sidebar {
            position: absolute; right: 20px; top: 85px; z-index: 10;
            width: 280px; display: flex; flex-direction: column; gap: 12px;
        }
        .panel-box {
            background: var(--bg-card);
            backdrop-filter: blur(14px);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 14px 18px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        }
        .box-title {
            font-size: 0.78rem; text-transform: uppercase; font-weight: 800;
            color: var(--primary); letter-spacing: 0.05em; margin-bottom: 10px;
        }
        .rpm-display {
            display: flex; align-items: baseline; justify-content: space-between;
            margin-bottom: 8px;
        }
        .rpm-num { font-size: 1.8rem; font-weight: 900; color: #fff; }
        .rpm-unit { font-size: 0.78rem; color: var(--text-sub); }
        input[type="range"] {
            width: 100%; accent-color: var(--primary); cursor: pointer;
        }

        /* BOTONES DE AUDIO Y VISTA */
        .btn-action {
            width: 100%; padding: 8px 12px; border-radius: 8px;
            font-size: 0.8rem; font-weight: 700; cursor: pointer;
            border: 1px solid rgba(255, 255, 255, 0.15);
            background: rgba(255, 255, 255, 0.08); color: #fff;
            display: flex; align-items: center; justify-content: space-between;
            margin-top: 6px; transition: all 0.2s ease;
        }
        .btn-action:hover { background: rgba(56, 189, 248, 0.2); border-color: var(--primary); }
        .btn-action.active { background: rgba(16, 185, 129, 0.25); border-color: #10b981; color: #34d399; }

        /* HINT INFERIOR */
        .hint-bar {
            position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%);
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 8px 20px; border-radius: 9999px;
            font-size: 0.78rem; color: var(--text-sub);
            display: flex; align-items: center; gap: 8px;
            pointer-events: none;
        }
        .hint-bar strong { color: #fff; }
    </style>
</head>
<body>

    <div id="loadingOverlay">
        <div class="spinner"></div>
        <div style="font-weight: 600; color: #94a3b8; font-size: 0.9rem;">Cargando modelo fotogramétrico 3D de pulmones...</div>
    </div>

    <header>
        <div class="brand-card">
            <span class="brand-icon">🫁</span>
            <div>
                <div class="brand-title">Aparato Respiratorio Humano • Fotogrametría 3D</div>
                <div class="brand-sub">Escaneo Anatómico Médico Real • Tráquea, Árbol Bronquial y Lóbulos</div>
            </div>
        </div>
        <div class="live-tag">
            <span class="pulse-dot"></span>
            <span id="cycleStatus">INHALACIÓN ACTIVA</span>
        </div>
    </header>

    <canvas id="renderCanvas"></canvas>

    <aside class="hud-sidebar">
        <div class="panel-box">
            <div class="box-title">🫁 Frecuencia Respiratoria</div>
            <div class="rpm-display">
                <div class="rpm-num" id="rpmVal">14</div>
                <div class="rpm-unit">Respiraciones / min (RPM)</div>
            </div>
            <input type="range" id="rpmSlider" min="8" max="28" value="14">
        </div>

        <div class="panel-box">
            <div class="box-title">🔊 Sonido Acústico Biológico</div>
            <button class="btn-action active" id="btnAudio">
                <span>Flujo de Ventilación</span>
                <span id="audioState">ON</span>
            </button>
        </div>

        <div class="panel-box">
            <div class="box-title">🎥 Perspectiva Orbital</div>
            <button class="btn-action" id="btnFront"><span>Vista Frontal (Tráquea)</span> <span>↺</span></button>
            <button class="btn-action" id="btnBack"><span>Vista Posterior (Bronquios)</span> <span>↻</span></button>
            <button class="btn-action" id="btnAutoRotate"><span>Giro Automático 360°</span> <span id="rotState">ON</span></button>
        </div>
    </aside>

    <div class="hint-bar">
        <span>🖱️ <strong>Control 360°:</strong> Arrastra con el ratón para rotar el modelo en cualquier ángulo • Rueda para zoom macro</span>
    </div>

    <script>
        const canvas = document.getElementById("renderCanvas");
        const loadingOverlay = document.getElementById("loadingOverlay");
        const engine = new BABYLON.Engine(canvas, true, { preserveDrawingBuffer: true, stencil: true });

        let currentRpm = 14;
        let lungsRoot = null;
        let autoRotate = true;
        let fixedBaseScale = 1.0;
        let isModelLoaded = false;

        const createScene = function () {
            const scene = new BABYLON.Scene(engine);
            scene.clearColor = new BABYLON.Color4(0.024, 0.035, 0.075, 1.0);

            const camera = new BABYLON.ArcRotateCamera("camera", -Math.PI / 2, Math.PI / 2.2, 5.0, new BABYLON.Vector3(0, 0, 0), scene);
            camera.attachControl(canvas, true);
            camera.wheelPrecision = 45;
            camera.lowerRadiusLimit = 1.8;
            camera.upperRadiusLimit = 15;

            // ILUMINACIÓN CLÍNICA PROFESIONAL PBR
            const hemiLight = new BABYLON.HemisphericLight("hemiLight", new BABYLON.Vector3(0, 1, 0), scene);
            hemiLight.intensity = 0.95;
            hemiLight.groundColor = new BABYLON.Color3(0.1, 0.12, 0.18);

            const keyLight = new BABYLON.DirectionalLight("keyLight", new BABYLON.Vector3(-1, -2, -1), scene);
            keyLight.position = new BABYLON.Vector3(5, 8, 5);
            keyLight.intensity = 1.8;
            keyLight.diffuse = new BABYLON.Color3(1.0, 0.98, 0.95);

            const fillLight = new BABYLON.PointLight("fillLight", new BABYLON.Vector3(-6, -2, -4), scene);
            fillLight.diffuse = new BABYLON.Color3(0.3, 0.6, 0.95);
            fillLight.intensity = 1.3;

            const rimLight = new BABYLON.PointLight("rimLight", new BABYLON.Vector3(4, 4, 6), scene);
            rimLight.diffuse = new BABYLON.Color3(1.0, 0.4, 0.5);
            rimLight.intensity = 1.5;

            const gl = new BABYLON.GlowLayer("glow", scene);
            gl.intensity = 0.25;

            // CARGA DEL MODELO FOTOGRAMÉTRICO REAL .GLB (Data URI embebido o local/nube)
            const modelSource = (window.LUNGS_GLB_B64) 
                ? window.LUNGS_GLB_B64 
                : "https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/lungs.glb";

            BABYLON.SceneLoader.ImportMesh("", "", modelSource, scene, function (meshes) {
                loadingOverlay.style.opacity = "0";
                setTimeout(() => loadingOverlay.style.display = "none", 500);

                lungsRoot = new BABYLON.TransformNode("lungsRoot", scene);
                meshes.forEach(m => {
                    if (m.parent === null) {
                        m.parent = lungsRoot;
                    }
                    if (m.material) {
                        // Mejorar brillo orgánico de tejido húmedo
                        m.material.roughness = 0.35;
                    }
                });

                // Normalización de escala y centrado volumétrico exacto
                const hierarchy = lungsRoot.getHierarchyBoundingVectors();
                const center = hierarchy.max.add(hierarchy.min).scale(0.5);
                const size = hierarchy.max.subtract(hierarchy.min);
                const maxDim = Math.max(size.x, size.y, size.z);

                if (maxDim > 0) {
                    fixedBaseScale = 2.8 / maxDim;
                    lungsRoot.scaling = new BABYLON.Vector3(fixedBaseScale, fixedBaseScale, fixedBaseScale);
                    lungsRoot.position = center.scale(-fixedBaseScale);
                }

                camera.radius = 5.2;
                camera.target = new BABYLON.Vector3(0, 0, 0);
                isModelLoaded = true;
            }, null, function (scene, message) {
                console.error("Error al cargar lungs.glb:", message);
                loadingOverlay.innerHTML = '<div style="color:#ef4444;font-weight:700;">Error al cargar modelo 3D. Verifica la conexión o el archivo lungs.glb</div>';
            });

            return { scene, camera };
        };

        const { scene, camera } = createScene();

        // MOTOR DE AUDIO BIOLÓGICO PROCEDIMENTAL (Flujo de aire nasal/traqueal)
        let audioCtx = null;
        let noiseNode = null;
        let filterNode = null;
        let gainNode = null;
        let audioEnabled = true;

        function initAudio() {
            if (audioCtx) return;
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            audioCtx = new AudioContext();

            // Generador de ruido rosa/blanco para aire
            const bufferSize = audioCtx.sampleRate * 2;
            const noiseBuffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
            const output = noiseBuffer.getChannelData(0);
            let b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0, b6 = 0;
            for (let i = 0; i < bufferSize; i++) {
                const white = Math.random() * 2 - 1;
                b0 = 0.99886 * b0 + white * 0.0555179;
                b1 = 0.99332 * b1 + white * 0.0750759;
                b2 = 0.96900 * b2 + white * 0.1538520;
                b3 = 0.86650 * b3 + white * 0.3104856;
                b4 = 0.55000 * b4 + white * 0.5329522;
                b5 = -0.7616 * b5 - white * 0.0168980;
                output[i] = (b0 + b1 + b2 + b3 + b4 + b5 + b6 + white * 0.5362) * 0.04;
                b6 = white * 0.115926;
            }

            noiseNode = audioCtx.createBufferSource();
            noiseNode.buffer = noiseBuffer;
            noiseNode.loop = true;

            filterNode = audioCtx.createBiquadFilter();
            filterNode.type = "bandpass";
            filterNode.frequency.value = 450;
            filterNode.Q.value = 1.2;

            gainNode = audioCtx.createGain();
            gainNode.gain.value = 0.0;

            noiseNode.connect(filterNode);
            filterNode.connect(gainNode);
            gainNode.connect(audioCtx.destination);
            noiseNode.start(0);
        }

        window.addEventListener("pointerdown", () => {
            if (!audioCtx) initAudio();
            else if (audioCtx.state === 'suspended') audioCtx.resume();
        }, { once: true });

        // BUCLE DE RENDER: VENTILACIÓN BIOLÓGICA ASIMÉTRICA REAL
        let breathTime = 0;
        engine.runRenderLoop(function () {
            const dt = engine.getDeltaTime() / 1000.0;
            const cycleDuration = 60.0 / currentRpm;
            breathTime = (breathTime + dt) % cycleDuration;
            const cyclePhase = breathTime / cycleDuration; // 0.0 a 1.0

            // Inhalación activa 45%, exhalación elástica pasiva 55%
            let expansion = 0;
            let isInhaling = true;
            if (cyclePhase < 0.45) {
                const p = cyclePhase / 0.45;
                expansion = 0.5 - 0.5 * Math.cos(p * Math.PI); // 0 a 1
                isInhaling = true;
            } else {
                const p = (cyclePhase - 0.45) / 0.55;
                expansion = 0.5 + 0.5 * Math.cos(p * Math.PI); // 1 a 0
                isInhaling = false;
            }

            const statusEl = document.getElementById("cycleStatus");
            if (statusEl) {
                statusEl.textContent = isInhaling ? "INHALACIÓN ACTIVA" : "EXHALACIÓN ELÁSTICA";
                statusEl.style.color = isInhaling ? "#38bdf8" : "#34d399";
            }

            // Aplicar expansión volumétrica suave a la masa pulmonar
            if (lungsRoot && isModelLoaded) {
                const scaleFactor = 1.0 + (expansion * 0.09); // 9% expansión volumétrica natural
                lungsRoot.scaling.x = fixedBaseScale * scaleFactor;
                lungsRoot.scaling.y = fixedBaseScale * (1.0 + expansion * 0.07);
                lungsRoot.scaling.z = fixedBaseScale * scaleFactor;

                if (autoRotate) {
                    lungsRoot.rotation.y += 0.003;
                }
            }

            // Modular sonido de respiración
            if (gainNode && audioCtx && audioEnabled) {
                const flowVelocity = Math.sin(cyclePhase * Math.PI * 2);
                const airVol = Math.abs(flowVelocity) * 0.35;
                gainNode.gain.setTargetAtTime(airVol, audioCtx.currentTime, 0.05);
                filterNode.frequency.setTargetAtTime(isInhaling ? 520 : 380, audioCtx.currentTime, 0.05);
            }

            scene.render();
        });

        window.addEventListener("resize", () => engine.resize());

        // CONTROLES DE LA INTERFAZ
        const rpmSlider = document.getElementById("rpmSlider");
        const rpmVal = document.getElementById("rpmVal");
        rpmSlider.addEventListener("input", (e) => {
            currentRpm = parseInt(e.target.value);
            rpmVal.textContent = currentRpm;
        });

        const btnAudio = document.getElementById("btnAudio");
        btnAudio.addEventListener("click", () => {
            if (!audioCtx) initAudio();
            audioEnabled = !audioEnabled;
            btnAudio.classList.toggle("active", audioEnabled);
            document.getElementById("audioState").textContent = audioEnabled ? "ON" : "OFF";
            if (!audioEnabled && gainNode) gainNode.gain.value = 0;
        });

        document.getElementById("btnFront").addEventListener("click", () => {
            camera.alpha = -Math.PI / 2;
            camera.beta = Math.PI / 2.2;
            if (lungsRoot) lungsRoot.rotation.y = 0;
        });

        document.getElementById("btnBack").addEventListener("click", () => {
            camera.alpha = Math.PI / 2;
            camera.beta = Math.PI / 2.2;
            if (lungsRoot) lungsRoot.rotation.y = Math.PI;
        });

        const btnAutoRotate = document.getElementById("btnAutoRotate");
        btnAutoRotate.addEventListener("click", () => {
            autoRotate = !autoRotate;
            btnAutoRotate.classList.toggle("active", autoRotate);
            document.getElementById("rotState").textContent = autoRotate ? "ON" : "OFF";
        });
    </script>
</body>
</html>
"""
    dest_path = os.path.join(SIM_DIR, "SIMULADOR_PULMONES_3D.html")
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html_code)
    print(f"✅ Guardado {dest_path}")

    # Actualizar PROBADOR_CODIGO_IA.html
    p_path = os.path.join(ROOT_DIR, "PROBADOR_CODIGO_IA.html")
    if os.path.exists(p_path):
        try:
            with open(p_path, "r", encoding="utf-8") as pf:
                p_code = pf.read()
            import html, re
            escaped = html.escape(html_code)
            p_code = re.sub(
                r'<textarea id="examplePulmonesTemplate"[^>]*>[\s\S]*?</textarea>',
                f'<textarea id="examplePulmonesTemplate" style="display:none;">{escaped}</textarea>',
                p_code
            )
            if "lungs_b64.js" not in p_code:
                p_code = p_code.replace("</head>", '    <script src="SIMULADORES_INTERACTIVOS/lungs_b64.js"></script>\n    <script src="https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/lungs_b64.js"></script>\n</head>')
            with open(p_path, "w", encoding="utf-8") as pf:
                pf.write(p_code)
            print("✅ PROBADOR_CODIGO_IA.html actualizado con plantilla GLB")
        except Exception as e:
            print(f"⚠️ Error actualizando probador: {e}")

    # Copiar a 01_Sesion
    if os.path.exists(S01_DIR):
        shutil.copy2(dest_path, os.path.join(S01_DIR, "SIMULADOR_PULMONES_3D.html"))
        if os.path.exists(B64_DEST):
            shutil.copy2(B64_DEST, os.path.join(S01_DIR, "lungs_b64.js"))
        if os.path.exists(GLB_DEST):
            shutil.copy2(GLB_DEST, os.path.join(S01_DIR, "lungs.glb"))
        if os.path.exists(p_path):
            shutil.copy2(p_path, os.path.join(S01_DIR, "PROBADOR_CODIGO_IA.html"))
        print(f"✅ Sincronizado en {S01_DIR}")

def main():
    print("🚀 === INICIANDO INTEGRACIÓN DE PULMONES 3D FOTOREALISTAS ===")
    ok = download_realistic_lungs()
    if ok:
        generate_base64_js()
    build_photorealistic_lungs_html()
    print("🎉 === PROCESO COMPLETADO ===")

if __name__ == "__main__":
    main()
