#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
setup_photorealistic_lungs.py - V2
Integra:
1. Árbol bronquial y tráquea fotogramétrico real de NIH 3D en GLB.
2. Lóbulos pulmonares anatómicos (izquierdo y derecho) con sombreado PBR orgánico y control de opacidad (Completo / Translúcido / Rayos X / Solo Bronquios).
3. Biomecánica respiratoria amplificada: descenso y elevación diafragmática de la tráquea (arriba/abajo) y expansión volumétrica tridimensional elástica de alvéolos.
4. Presets fisiológicos de RPM, audio aéreo procedimental Web Audio API y perspectiva 360°.
"""

import os
import sys
import base64
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIM_DIR = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS")
S01_DIR = os.path.join(ROOT_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM", "01_Sesion")

GLB_DEST = os.path.join(SIM_DIR, "lungs.glb")
B64_DEST = os.path.join(SIM_DIR, "lungs_b64.js")
V1_PATH = os.path.join(SIM_DIR, "SIMULADOR_PULMONES_3D_V1.html")
V2_PATH = os.path.join(SIM_DIR, "SIMULADOR_PULMONES_3D.html")

def check_realistic_lungs():
    os.makedirs(SIM_DIR, exist_ok=True)
    if os.path.exists(GLB_DEST) and os.path.getsize(GLB_DEST) > 50000:
        print(f"✅ Archivo lungs.glb verificado ({os.path.getsize(GLB_DEST) / 1024 / 1024:.2f} MB)")
        return True

    import glob
    candidates = (
        glob.glob(os.path.expanduser("~/Downloads/*lung*.glb")) +
        glob.glob(os.path.expanduser("~/Downloads/*pulmon*.glb")) +
        glob.glob(os.path.expanduser("~/Downloads/*3DPX*.glb")) +
        glob.glob(os.path.expanduser("~/Downloads/*.glb"))
    )
    valid = [f for f in candidates if os.path.isfile(f) and os.path.getsize(f) > 50000 and "heart" not in os.path.basename(f).lower()]
    if valid:
        latest = max(valid, key=os.path.getctime)
        shutil.copy2(latest, GLB_DEST)
        print(f"✅ Copiado desde Descargas: {latest}")
        return True
    return False

def generate_base64_js():
    if not os.path.exists(GLB_DEST):
        return False
    if os.path.exists(B64_DEST) and os.path.getsize(B64_DEST) > 1000000:
        print(f"✅ Archivo lungs_b64.js ya listo ({os.path.getsize(B64_DEST) / 1024 / 1024:.2f} MB)")
        return True
    print("📦 Generando lungs_b64.js...")
    with open(GLB_DEST, "rb") as f:
        data = f.read()
    b64_str = base64.b64encode(data).decode("utf-8")
    with open(B64_DEST, "w", encoding="utf-8") as f:
        f.write(f'window.LUNGS_GLB_B64 = "data:model/gltf-binary;base64,{b64_str}";\n')
    print("✅ Creado lungs_b64.js")
    return True

def build_v2_html():
    print("🎨 Construyendo SIMULADOR_PULMONES_3D.html (Edición V2: Pulmones + Bronquios + Dinámica Vertical)...")
    
    # Preservar V1 si aún no está guardado
    if os.path.exists(V2_PATH) and not os.path.exists(V1_PATH):
        shutil.copy2(V2_PATH, V1_PATH)
        print(f"💾 Guardada copia histórica V1 en: {V1_PATH}")

    html_code = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laboratorio Anatómico 3D V2 • Pulmones y Árbol Bronquial Hiperrealistas (GLB + Babylon.js)</title>
    <!-- Babylon.js Motor 3D Oficial CDN -->
    <script src="https://cdn.babylonjs.com/babylon.js"></script>
    <script src="https://cdn.babylonjs.com/loaders/babylonjs.loaders.min.js"></script>
    <!-- Respaldo Base64 para entornos locales / offline -->
    <script src="lungs_b64.js"></script>
    <script src="https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/lungs_b64.js"></script>
    <style>
        :root {
            --bg-base: #060913;
            --bg-card: rgba(15, 23, 42, 0.92);
            --border: rgba(56, 189, 248, 0.35);
            --primary: #38bdf8;
            --emerald: #34d399;
            --rose: #fb7185;
            --lung-pink: #f472b6;
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
            border-radius: 14px;
            padding: 12px 20px;
            display: flex; align-items: center; gap: 14px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            pointer-events: auto;
        }
        .brand-icon { font-size: 2.2rem; }
        .brand-title { font-size: 1.15rem; font-weight: 800; color: #fff; letter-spacing: -0.01em; }
        .brand-sub { font-size: 0.78rem; color: var(--text-sub); margin-top: 2px; }

        .live-tag {
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid rgba(56, 189, 248, 0.4);
            color: var(--primary);
            padding: 8px 16px; border-radius: 9999px;
            font-size: 0.8rem; font-weight: 800;
            display: flex; align-items: center; gap: 8px;
            pointer-events: auto;
            box-shadow: 0 4px 15px rgba(56, 189, 248, 0.2);
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
            width: 310px; display: flex; flex-direction: column; gap: 12px;
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
            display: flex; justify-content: space-between; align-items: center;
        }

        /* CONTROL VISUAL DE PULMONES (OPACIDAD) */
        .vis-modes-grid {
            display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-bottom: 8px;
        }
        .btn-vis {
            padding: 7px 8px; border-radius: 8px; font-size: 0.73rem; font-weight: 700;
            border: 1px solid rgba(255, 255, 255, 0.12);
            background: rgba(255, 255, 255, 0.05); color: #cbd5e1;
            cursor: pointer; transition: all 0.2s ease; text-align: center;
        }
        .btn-vis:hover { background: rgba(56, 189, 248, 0.2); border-color: var(--primary); color: #fff; }
        .btn-vis.active { background: rgba(244, 114, 182, 0.25); border-color: var(--lung-pink); color: #fbcfe8; }

        .opacity-slider-wrap {
            margin-top: 8px; padding-top: 8px; border-top: 1px solid rgba(255, 255, 255, 0.08);
        }
        .opacity-label {
            display: flex; justify-content: space-between; font-size: 0.74rem; color: var(--text-sub); margin-bottom: 4px;
        }

        /* FRECUENCIA RESPIRATORIA */
        .rpm-display {
            display: flex; align-items: baseline; justify-content: space-between;
            margin-bottom: 8px;
        }
        .rpm-num { font-size: 2.2rem; font-weight: 900; color: #fff; line-height: 1; }
        .rpm-unit { font-size: 0.76rem; color: var(--text-sub); }
        input[type="range"] {
            width: 100%; accent-color: var(--primary); cursor: pointer;
        }

        /* PRESETS RÁPIDOS */
        .preset-grid {
            display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-top: 10px;
        }
        .btn-preset {
            padding: 7px 10px; border-radius: 8px; font-size: 0.75rem; font-weight: 700;
            border: 1px solid rgba(255, 255, 255, 0.12);
            background: rgba(255, 255, 255, 0.05); color: #cbd5e1;
            cursor: pointer; transition: all 0.2s ease; text-align: center;
        }
        .btn-preset:hover { background: rgba(56, 189, 248, 0.2); border-color: var(--primary); color: #fff; }
        .btn-preset.active { background: rgba(56, 189, 248, 0.3); border-color: var(--primary); color: #fff; }

        /* BOTONES DE ACCIÓN */
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

        .btn-views-grid {
            display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-top: 6px;
        }

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
        <div style="font-weight: 600; color: #94a3b8; font-size: 0.9rem;" id="loadingStatusText">Cargando modelo anatómico 3D de pulmones y bronquios (V2)...</div>
    </div>

    <header>
        <div class="brand-card">
            <span class="brand-icon">🫁</span>
            <div>
                <div class="brand-title">Aparato Respiratorio Humano 3D • Edición V2</div>
                <div class="brand-sub">Tráquea Dinámica, Árbol Bronquial Fractal y Lóbulos Pulmonares Translúcidos</div>
            </div>
        </div>
        <div class="live-tag">
            <span class="pulse-dot"></span>
            <span id="cycleStatus">INHALACIÓN ACTIVA</span>
        </div>
    </header>

    <canvas id="renderCanvas"></canvas>

    <aside class="hud-sidebar">
        <!-- CAPA VISUAL PULMONES (V2) -->
        <div class="panel-box">
            <div class="box-title">
                <span>🫁 Capa de Pulmones</span>
                <span style="font-size:0.7rem; color:var(--lung-pink); font-weight:700;">V2 DUAL</span>
            </div>
            <div class="vis-modes-grid">
                <button class="btn-vis active" data-opacity="0.45" id="btnModeRayosX">🔬 Rayos X (45%)</button>
                <button class="btn-vis" data-opacity="0.85" id="btnModeCompleto">🫁 Tejido (85%)</button>
                <button class="btn-vis" data-opacity="0.0" id="btnModeBronquios">⚡ Solo Bronquios</button>
                <button class="btn-vis" data-opacity="1.0" id="btnModeOpaco">🛡️ 100% Sólido</button>
            </div>
            <div class="opacity-slider-wrap">
                <div class="opacity-label">
                    <span>Opacidad del Tejido Pulmonar</span>
                    <span id="opacityVal">45%</span>
                </div>
                <input type="range" id="opacitySlider" min="0" max="100" value="45">
            </div>
        </div>

        <!-- FRECUENCIA RESPIRATORIA -->
        <div class="panel-box">
            <div class="box-title">
                <span>🌬️ Ventilación Biológica</span>
            </div>
            <div class="rpm-display">
                <div class="rpm-num" id="rpmVal">14</div>
                <div class="rpm-unit">Respiraciones / min (RPM)</div>
            </div>
            <input type="range" id="rpmSlider" min="6" max="36" value="14">
            
            <div class="preset-grid">
                <button class="btn-preset active" data-rpm="14">🛋️ Reposo (14)</button>
                <button class="btn-preset" data-rpm="22">🚶 Paseo (22)</button>
                <button class="btn-preset" data-rpm="32">🏃 Carrera (32)</button>
                <button class="btn-preset" data-rpm="8">🧘 Zen (8)</button>
            </div>
        </div>

        <!-- SONIDO -->
        <div class="panel-box">
            <div class="box-title">🔊 Sonido Acústico Biológico</div>
            <button class="btn-action active" id="btnAudio">
                <span>🌬️ Flujo de Aire (In/Ex)</span>
                <span id="audioState">ON</span>
            </button>
        </div>

        <!-- CÁMARA Y PERSPECTIVA -->
        <div class="panel-box">
            <div class="box-title">🎥 Perspectiva Anatómica 360°</div>
            <div class="btn-views-grid">
                <button class="btn-action" id="btnFront" style="margin-top:0;">👁️ Anterior</button>
                <button class="btn-action" id="btnBack" style="margin-top:0;">🔙 Posterior</button>
            </div>
            <button class="btn-action active" id="btnAutoRotate" style="margin-top:8px;">
                <span>🔄 Auto-Rotación Suave</span>
                <span id="rotState">ON</span>
            </button>
        </div>
    </aside>

    <div class="hint-bar">
        <span>🖱️ <strong>Arrastra</strong> para rotar 360° • <strong>Rueda</strong> para zoom • <strong>Clic derecho</strong> para desplazar</span>
    </div>

    <script>
        const canvas = document.getElementById("renderCanvas");
        const engine = new BABYLON.Engine(canvas, true, { preserveDrawingBuffer: true, stencil: true });
        const loadingOverlay = document.getElementById("loadingOverlay");

        let lungsRoot = null;
        let leftLungLobe = null;
        let rightLungLobe = null;
        let lungMaterial = null;
        let lungAnimGroup = null;

        let fixedBaseScale = 1.0;
        let baseCenter = new BABYLON.Vector3(0, 0, 0);
        let isModelLoaded = false;
        let currentRpm = 14;
        let autoRotate = true;
        let currentOpacity = 0.45;

        // GENERADOR ANATÓMICO DE LÓBULOS PULMONARES PBR (V2)
        function createAnatomicalLungLobes(scene, rootNode) {
            lungMaterial = new BABYLON.PBRMaterial("lungPBRMaterial", scene);
            lungMaterial.albedoColor = new BABYLON.Color3(0.92, 0.44, 0.48); // Tono rosado orgánico alveolar
            lungMaterial.emissiveColor = new BABYLON.Color3(0.12, 0.04, 0.05);
            lungMaterial.roughness = 0.28; // Brillo húmedo de pleura
            lungMaterial.metallic = 0.04;
            lungMaterial.alpha = currentOpacity;
            lungMaterial.backFaceCulling = false;
            lungMaterial.transparencyMode = BABYLON.PBRMaterial.PBRMATERIAL_ALPHABLEND;
            lungMaterial.subSurface.isTranslucencyEnabled = true;
            lungMaterial.subSurface.translucencyIntensity = 0.7;

            // Función para deformar geométricamente una esfera en un lóbulo pulmonar anatómico
            function buildLobeMesh(name, isLeft) {
                const sphere = BABYLON.MeshBuilder.CreateSphere(name, {
                    segments: 36,
                    diameterX: 7.6,
                    diameterY: 14.8,
                    diameterZ: 7.2
                }, scene);

                const positions = sphere.getVerticesData(BABYLON.VertexBuffer.PositionKind);
                const numberOfVertices = positions.length / 3;

                for (let i = 0; i < numberOfVertices; i++) {
                    let x = positions[i * 3];
                    let y = positions[i * 3 + 1];
                    let z = positions[i * 3 + 2];

                    const normY = y / 7.4; // -1 (base) a +1 (ápice)

                    // 1. Ápice superior afilado y estrecho
                    if (normY > 0) {
                        const taper = 1.0 - (normY * 0.48);
                        x *= taper;
                        z *= taper;
                    } 
                    // 2. Base diafragmática ensanchada y cóncava
                    else {
                        const expandBase = 1.0 + Math.abs(normY) * 0.32;
                        x *= expandBase;
                        z *= expandBase;
                        // Concavidad de la cúpula diafragmática en el fondo
                        if (normY < -0.65) {
                            y += Math.sin((x*x + z*z) * 0.08) * 0.9;
                        }
                    }

                    // 3. Aplanamiento medial (donde entran los bronquios)
                    if (isLeft && x > 0) {
                        x *= 0.72;
                        // Escotadura cardíaca en el pulmón izquierdo
                        if (normY > -0.4 && normY < 0.3 && z > -1.0) {
                            x *= 0.65;
                            z *= 0.85;
                        }
                    } else if (!isLeft && x < 0) {
                        x *= 0.76;
                    }

                    positions[i * 3] = x;
                    positions[i * 3 + 1] = y;
                    positions[i * 3 + 2] = z;
                }

                sphere.updateVerticesData(BABYLON.VertexBuffer.PositionKind, positions);
                const indices = sphere.getIndices();
                const normals = [];
                BABYLON.VertexData.ComputeNormals(positions, indices, normals);
                sphere.updateVerticesData(BABYLON.VertexBuffer.NormalKind, normals);

                sphere.material = lungMaterial;
                sphere.parent = rootNode;
                return sphere;
            }

            // Crear y posicionar lóbulo derecho e izquierdo envolviendo el árbol bronquial
            rightLungLobe = buildLobeMesh("rightLungLobe", false);
            rightLungLobe.position = new BABYLON.Vector3(4.8, -1.2, -0.2);
            rightLungLobe.rotation = new BABYLON.Vector3(0.04, 0.08, -0.05);

            leftLungLobe = buildLobeMesh("leftLungLobe", true);
            leftLungLobe.position = new BABYLON.Vector3(-4.8, -1.2, -0.2);
            leftLungLobe.rotation = new BABYLON.Vector3(0.04, -0.08, 0.05);

            console.log("✅ Lóbulos pulmonares V2 generados y acoplados con éxito.");
        }

        const createScene = function () {
            const scene = new BABYLON.Scene(engine);
            scene.clearColor = new BABYLON.Color4(0.024, 0.035, 0.075, 1.0);

            // Cámara orbital cinemática
            const camera = new BABYLON.ArcRotateCamera("Camera", -Math.PI / 2, Math.PI / 2.3, 5.2, BABYLON.Vector3.Zero(), scene);
            camera.attachControl(canvas, true);
            camera.wheelPrecision = 40;
            camera.lowerRadiusLimit = 2.0;
            camera.upperRadiusLimit = 15.0;

            // Iluminación quirúrgica/médica PBR
            const hemiLight = new BABYLON.HemisphericLight("hemiLight", new BABYLON.Vector3(0, 1, 0), scene);
            hemiLight.intensity = 1.15;
            hemiLight.diffuse = new BABYLON.Color3(1.0, 0.96, 0.94);
            hemiLight.groundColor = new BABYLON.Color3(0.12, 0.16, 0.28);

            const keyLight = new BABYLON.DirectionalLight("keyLight", new BABYLON.Vector3(-1, -2, -1), scene);
            keyLight.position = new BABYLON.Vector3(5, 8, 5);
            keyLight.intensity = 1.9;
            keyLight.diffuse = new BABYLON.Color3(1.0, 0.98, 0.95);

            const fillLight = new BABYLON.PointLight("fillLight", new BABYLON.Vector3(-6, -2, -4), scene);
            fillLight.diffuse = new BABYLON.Color3(0.3, 0.6, 0.95);
            fillLight.intensity = 1.4;

            const rimLight = new BABYLON.PointLight("rimLight", new BABYLON.Vector3(4, 4, 6), scene);
            rimLight.diffuse = new BABYLON.Color3(1.0, 0.45, 0.55);
            rimLight.intensity = 1.6;

            const gl = new BABYLON.GlowLayer("glow", scene);
            gl.intensity = 0.25;

            // CASCADE ROBUSTO DE FUENTES (GLB LOCAL -> BASE64 OFFLINE -> CDN GITHUB)
            const candidateSources = [
                "lungs.glb",
                (window.LUNGS_GLB_B64 && window.LUNGS_GLB_B64.length > 1000) ? window.LUNGS_GLB_B64 : null,
                "https://javiercursocorreo-gif.github.io/Curso-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100.%20[SESSIONS]%20TERNAS_LISTAS_PARA_CLASSROOM/01_Sesion/lungs.glb",
                "https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/lungs.glb"
            ].filter(Boolean);

            let currentSourceIdx = 0;

            function tryLoadNextSource() {
                if (currentSourceIdx >= candidateSources.length) {
                    loadingOverlay.innerHTML = '<div style="color:#ef4444;font-weight:700;padding:24px;text-align:center;max-width:420px;line-height:1.5;">⚠️ Error al cargar el modelo 3D de pulmones.<br><small style="color:#94a3b8;font-weight:400;display:block;margin-top:8px;">Verifica la conexión a Internet o el archivo lungs.glb.<br>El simulador funciona de forma óptima desde Classroom o mediante servidor web.</small></div>';
                    return;
                }

                const src = candidateSources[currentSourceIdx];
                const isB64 = (typeof src === "string" && src.startsWith("data:"));
                console.log("[Simulador Pulmones 3D V2] Intentando cargar fuente " + (currentSourceIdx + 1) + "/" + candidateSources.length + ":", isB64 ? "Data URI Base64 (" + (src.length / 1024 / 1024).toFixed(1) + " MB)" : src);

                BABYLON.SceneLoader.ImportMesh(
                    "",
                    "",
                    src,
                    scene,
                    function (meshes, particleSystems, skeletons, animationGroups) {
                        try {
                            loadingOverlay.style.opacity = "0";
                            setTimeout(() => loadingOverlay.style.display = "none", 500);

                            lungsRoot = new BABYLON.TransformNode("lungsRoot", scene);

                            meshes.forEach(m => {
                                if (m.parent === null) {
                                    m.parent = lungsRoot;
                                }
                            });

                            // Construir lóbulos anatómicos envolventes V2 acoplados al mismo TransformNode
                            createAnatomicalLungLobes(scene, lungsRoot);

                            // Si el modelo incluye la animación médica de respiración (Blender morph targets)
                            if (animationGroups && animationGroups.length > 0) {
                                lungAnimGroup = animationGroups[0];
                                lungAnimGroup.play(true);
                                lungAnimGroup.speedRatio = currentRpm / 14.0;
                                console.log("[Simulador Pulmones 3D V2] Animación médica nativa activada:", lungAnimGroup.name);
                            }

                            // Normalización de escala y centrado volumétrico exacto
                            const hierarchy = lungsRoot.getHierarchyBoundingVectors();
                            const center = hierarchy.max.add(hierarchy.min).scale(0.5);
                            const size = hierarchy.max.subtract(hierarchy.min);
                            const maxDim = Math.max(size.x, size.y, size.z);

                            if (maxDim > 0 && isFinite(maxDim)) {
                                fixedBaseScale = 2.8 / maxDim;
                                lungsRoot.scaling = new BABYLON.Vector3(fixedBaseScale, fixedBaseScale, fixedBaseScale);
                                baseCenter = center.scale(-fixedBaseScale);
                                lungsRoot.position = baseCenter.clone();
                            } else {
                                fixedBaseScale = 0.25;
                                lungsRoot.scaling = new BABYLON.Vector3(fixedBaseScale, fixedBaseScale, fixedBaseScale);
                                baseCenter = new BABYLON.Vector3(0, 0, 0);
                            }

                            camera.radius = 5.2;
                            camera.target = new BABYLON.Vector3(0, 0, 0);
                            isModelLoaded = true;
                            console.log("✅ [Simulador Pulmones 3D V2] Cargado exitosamente desde:", isB64 ? "Base64 Embebido" : src);
                        } catch (initErr) {
                            console.error("Error inicializando modelo en escena:", initErr);
                            currentSourceIdx++;
                            tryLoadNextSource();
                        }
                    },
                    null,
                    function (scene, message, exception) {
                        console.warn("⚠️ Falló fuente:", src, message, exception);
                        currentSourceIdx++;
                        tryLoadNextSource();
                    },
                    ".glb" // <-- PARÁMETRO VITAL: pluginExtension forzado
                );
            }

            tryLoadNextSource();

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

        // BUCLE DE RENDER: BIOMECÁNICA RESPIRATORIA DINÁMICA VERTICAL Y EXPANSIVA (V2)
        let breathTime = 0;
        engine.runRenderLoop(function () {
            const dt = engine.getDeltaTime() / 1000.0;
            const cycleDuration = 60.0 / currentRpm;
            breathTime = (breathTime + dt) % cycleDuration;
            const cyclePhase = breathTime / cycleDuration; // 0.0 a 1.0

            // Inhalación activa 45% (diafragma desciende y expande), exhalación elástica pasiva 55% (asciende)
            let expansion = 0;
            let isInhaling = true;
            if (cyclePhase < 0.45) {
                const p = cyclePhase / 0.45;
                expansion = 0.5 - 0.5 * Math.cos(p * Math.PI); // 0.0 a 1.0 suave
                isInhaling = true;
            } else {
                const p = (cyclePhase - 0.45) / 0.55;
                expansion = 0.5 + 0.5 * Math.cos(p * Math.PI); // 1.0 a 0.0 suave
                isInhaling = false;
            }

            const statusEl = document.getElementById("cycleStatus");
            if (statusEl) {
                statusEl.textContent = isInhaling ? "INHALACIÓN (DIAFRAGMA BAJA)" : "EXHALACIÓN (RETRACCIÓN ELÁSTICA)";
                statusEl.style.color = isInhaling ? "#38bdf8" : "#34d399";
            }

            // APLICACIÓN DINÁMICA DE LA RESPIRACIÓN EN LA TRÁQUEA Y LÓBULOS (V2)
            if (lungsRoot && isModelLoaded) {
                // 1. Desplazamiento vertical diafragmático pronunciado (Arriba / Abajo)
                // Durante la inhalación el árbol traqueobronquial desciende; al exhalar asciende
                const verticalShift = -expansion * 0.28; 
                lungsRoot.position.y = baseCenter.y + verticalShift;

                // 2. Expansión elástica tridimensional (alvéolos y lóbulos se ensanchan)
                const scaleX = fixedBaseScale * (1.0 + expansion * 0.16); // 16% apertura lateral
                const scaleY = fixedBaseScale * (1.0 + expansion * 0.10); // 10% elongación vertical
                const scaleZ = fixedBaseScale * (1.0 + expansion * 0.16); // 16% expansión anteroposterior

                lungsRoot.scaling.x = scaleX;
                lungsRoot.scaling.y = scaleY;
                lungsRoot.scaling.z = scaleZ;

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

        // CONTROLES DE LA INTERFAZ (V2)
        // 1. Selector de Opacidad de Pulmones
        const opacitySlider = document.getElementById("opacitySlider");
        const opacityVal = document.getElementById("opacityVal");
        const visBtns = document.querySelectorAll(".btn-vis");

        function setLungOpacity(alphaVal) {
            currentOpacity = Math.max(0, Math.min(1, alphaVal));
            if (lungMaterial) {
                lungMaterial.alpha = currentOpacity;
            }
            if (leftLungLobe && rightLungLobe) {
                const isVisible = currentOpacity > 0.02;
                leftLungLobe.setEnabled(isVisible);
                rightLungLobe.setEnabled(isVisible);
            }
            opacitySlider.value = Math.round(currentOpacity * 100);
            opacityVal.textContent = Math.round(currentOpacity * 100) + "%";

            visBtns.forEach(btn => {
                const bAlpha = parseFloat(btn.getAttribute("data-opacity"));
                btn.classList.toggle("active", Math.abs(bAlpha - currentOpacity) < 0.08);
            });
        }

        opacitySlider.addEventListener("input", (e) => {
            setLungOpacity(parseInt(e.target.value) / 100.0);
        });

        visBtns.forEach(btn => {
            btn.addEventListener("click", () => {
                const a = parseFloat(btn.getAttribute("data-opacity"));
                setLungOpacity(a);
            });
        });

        // 2. Frecuencia Respiratoria
        const rpmSlider = document.getElementById("rpmSlider");
        const rpmVal = document.getElementById("rpmVal");
        const presetBtns = document.querySelectorAll(".btn-preset");

        function updateRpm(val) {
            currentRpm = val;
            rpmSlider.value = val;
            rpmVal.textContent = val;
            if (lungAnimGroup) {
                lungAnimGroup.speedRatio = currentRpm / 14.0;
            }
            presetBtns.forEach(b => {
                b.classList.toggle("active", parseInt(b.getAttribute("data-rpm")) === val);
            });
        }

        rpmSlider.addEventListener("input", (e) => {
            updateRpm(parseInt(e.target.value));
        });

        presetBtns.forEach(btn => {
            btn.addEventListener("click", () => {
                const r = parseInt(btn.getAttribute("data-rpm"));
                updateRpm(r);
            });
        });

        // 3. Audio
        const btnAudio = document.getElementById("btnAudio");
        btnAudio.addEventListener("click", () => {
            if (!audioCtx) initAudio();
            audioEnabled = !audioEnabled;
            btnAudio.classList.toggle("active", audioEnabled);
            document.getElementById("audioState").textContent = audioEnabled ? "ON" : "OFF";
            if (!audioEnabled && gainNode) gainNode.gain.value = 0;
        });

        // 4. Vistas y Rotación
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

    with open(V2_PATH, "w", encoding="utf-8") as f:
        f.write(html_code)
    print(f"✅ Guardado V2 en: {V2_PATH}")

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
            print("✅ PROBADOR_CODIGO_IA.html actualizado con plantilla V2")
        except Exception as e:
            print(f"⚠️ Error actualizando probador: {e}")

    # Copiar a 01_Sesion
    if os.path.exists(S01_DIR):
        try:
            shutil.copy2(V2_PATH, os.path.join(S01_DIR, "SIMULADOR_PULMONES_3D.html"))
            if os.path.exists(V1_PATH):
                shutil.copy2(V1_PATH, os.path.join(S01_DIR, "SIMULADOR_PULMONES_3D_V1.html"))
            if os.path.exists(B64_DEST):
                shutil.copy2(B64_DEST, os.path.join(S01_DIR, "lungs_b64.js"))
            if os.path.exists(GLB_DEST):
                shutil.copy2(GLB_DEST, os.path.join(S01_DIR, "lungs.glb"))
            if os.path.exists(p_path):
                shutil.copy2(p_path, os.path.join(S01_DIR, "PROBADOR_CODIGO_IA.html"))
            print(f"✅ Sincronizado V1 y V2 en {S01_DIR}")
        except Exception as e:
            print(f"⚠️ Nota al copiar a 01_Sesion: {e}")

def main():
    print("🚀 === GENERANDO PULMONES 3D V2 (LÓBULOS + DINÁMICA TRÁQUEA/ALVÉOLOS) ===")
    ok = check_realistic_lungs()
    if ok:
        generate_base64_js()
    build_v2_html()
    print("🎉 === V2 COMPLETADA EXITOSAMENTE ===")

if __name__ == "__main__":
    main()
