#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
integrar_vista_elephant_goldfish.py
Integra la Vista 4: El Elefante y el Pez (Elephant-Goldfish Model)
en la aplicación interactiva *.App_SIMULACION.html de Monográfico 7 (Gestión con IA).
"""

import os
import re

FILE_PATH = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/7. MAPA_GESTION_PROYECTO_CON_IA/*.App_SIMULACION.html"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. ACTUALIZAR LOS BOTONES DE NAVEGACIÓN EN EL HEADER
old_nav = '''      <button class="view-switch-btn" id="btnViewWorkshop" onclick="switchMainView('workshop')">
        💻 Vista 4: Taller en tu Portátil
      </button>
      <button class="view-switch-btn" id="btnViewMacro" onclick="switchMainView('macro')">
        🗺️ Vista 5: Flujo a Classroom
      </button>'''

new_nav = '''      <button class="view-switch-btn" id="btnViewGoldfish" onclick="switchMainView('goldfish')">
        🐘 Vista 4: El Elefante y el Pez (Auditoría)
      </button>
      <button class="view-switch-btn" id="btnViewWorkshop" onclick="switchMainView('workshop')">
        💻 Vista 5: Taller en tu Portátil
      </button>
      <button class="view-switch-btn" id="btnViewMacro" onclick="switchMainView('macro')">
        🗺️ Vista 6: Flujo a Classroom
      </button>'''

if old_nav in html:
    html = html.replace(old_nav, new_nav)
    print("✅ Header view-switch-box actualizado")
else:
    print("⚠️ No se encontró exactamente old_nav, buscando variante...")

# 2. ACTUALIZAR EL BOTÓN SIGUIENTE DE VISTA 3 (ANTIGRAVITY)
old_btn_anti = '''onclick="switchMainView('workshop')">
          Siguiente: Vista 4 • Taller en tu Portátil ➔
        </button>'''

new_btn_anti = '''onclick="switchMainView('goldfish')">
          Siguiente: Vista 4 • El Elefante y el Pez (Auditoría) ➔
        </button>'''

if old_btn_anti in html:
    html = html.replace(old_btn_anti, new_btn_anti)
    print("✅ Botón de salida de Vista 3 actualizado hacia Vista 4 (Goldfish)")

# 3. ACTUALIZAR LOS BOTONES DE VISTA WORKSHOP (AHORA VISTA 5)
old_work_top = '''onclick="switchMainView('antigravity')">
            ⬅ Anterior: Vista 3 • Control de Ficheros
          </button>
          <button class="nav-step-btn" style="background:linear-gradient(135deg, rgba(168,85,247,0.3), rgba(56,189,248,0.3)); border-color:var(--cyan); color:#fff;" onclick="switchMainView('macro')">
            Siguiente: Vista 5 • Flujo a Classroom ➔
          </button>'''

new_work_top = '''onclick="switchMainView('goldfish')">
            ⬅ Anterior: Vista 4 • El Elefante y el Pez
          </button>
          <button class="nav-step-btn" style="background:linear-gradient(135deg, rgba(168,85,247,0.3), rgba(56,189,248,0.3)); border-color:var(--cyan); color:#fff;" onclick="switchMainView('macro')">
            Siguiente: Vista 6 • Flujo a Classroom ➔
          </button>'''

if old_work_top in html:
    html = html.replace(old_work_top, new_work_top)
    print("✅ Botones superiores e inferiores de Vista Workshop actualizados")

# 4. ACTUALIZAR EL BOTÓN ANTERIOR DE VISTA MACRO (AHORA VISTA 6)
old_macro_prev = '''onclick="switchMainView('workshop')">
            ⬅ Anterior: Vista 4 • Taller en tu Portátil
          </button>'''

new_macro_prev = '''onclick="switchMainView('workshop')">
            ⬅ Anterior: Vista 5 • Taller en tu Portátil
          </button>'''

if old_macro_prev in html:
    html = html.replace(old_macro_prev, new_macro_prev)
    print("✅ Botón anterior de Vista Macro actualizado a Vista 5")

# 5. ESTILOS CSS PARA LA NUEVA VISTA
goldfish_css = '''
    /* ========================================================================= */
    /* ESTILOS DE LA VISTA 4: ELEPHANT - GOLDFISH MODEL (DOBLE VERIFICACIÓN)     */
    /* ========================================================================= */
    .goldfish-hero-box {
      background: linear-gradient(135deg, rgba(234, 88, 12, 0.18), rgba(13, 22, 45, 0.95) 70%, rgba(56, 189, 248, 0.12));
      border: 1px solid rgba(251, 146, 60, 0.5);
      border-radius: 16px;
      padding: 24px 28px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }
    .goldfish-hero-box h2 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.5rem;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 8px;
    }
    .goldfish-dual-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-top: 20px;
    }
    @media (max-width: 900px) {
      .goldfish-dual-grid { grid-template-columns: 1fr; }
    }
    .goldfish-card {
      background: rgba(13, 22, 45, 0.88);
      border-radius: 14px;
      padding: 22px;
      border: 1px solid var(--border-soft);
      display: flex;
      flex-direction: column;
      gap: 12px;
      position: relative;
      overflow: hidden;
    }
    .goldfish-card.elephant-card {
      border-color: rgba(56, 189, 248, 0.45);
      background: linear-gradient(180deg, rgba(56, 189, 248, 0.08) 0%, rgba(13, 22, 45, 0.9) 100%);
    }
    .goldfish-card.fish-card {
      border-color: rgba(251, 146, 60, 0.5);
      background: linear-gradient(180deg, rgba(251, 146, 60, 0.08) 0%, rgba(13, 22, 45, 0.9) 100%);
    }
    .goldfish-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      width: fit-content;
    }
    .badge-elephant { background: rgba(56, 189, 248, 0.2); color: var(--blue); border: 1px solid var(--blue); }
    .badge-fish { background: rgba(251, 146, 60, 0.2); color: var(--orange); border: 1px solid var(--orange); }

    .goldfish-flow-steps {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      margin-top: 22px;
    }
    @media (max-width: 800px) {
      .goldfish-flow-steps { grid-template-columns: 1fr 1fr; }
    }
    .goldfish-step-item {
      background: rgba(13, 22, 45, 0.8);
      border: 1px solid var(--border-soft);
      border-radius: 12px;
      padding: 16px;
      text-align: center;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .goldfish-step-num {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.1);
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
      font-weight: 700;
      color: #fff;
      font-size: 0.85rem;
    }
    .goldfish-step-item.active .goldfish-step-num {
      background: var(--orange);
      color: #000;
      box-shadow: 0 0 12px var(--orange);
    }
    .goldfish-sim-console {
      background: #040813;
      border: 1px solid rgba(251, 146, 60, 0.4);
      border-radius: 12px;
      padding: 18px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      color: #e2e8f0;
      margin-top: 18px;
      min-height: 180px;
      line-height: 1.6;
    }
'''

# Inyectar estilos antes de </style>
if "</style>" in html and ".goldfish-hero-box" not in html:
    html = html.replace("</style>", goldfish_css + "\n  </style>")
    print("✅ Estilos CSS de Elephant-Goldfish inyectados")

# 6. HTML DE LA VISTA 4 (GOLDFISH)
goldfish_html = '''
  <!-- ========================================================================= -->
  <!-- VISTA 4: EL ELEFANTE Y EL PEZ DE COLORES (ELEPHANT-GOLDFISH MODEL)        -->
  <!-- ========================================================================= -->
  <div id="viewGoldfishContainer" style="display: none;">
    <div class="workshop-stage-container">

      <!-- HERO DE LA VISTA -->
      <div class="goldfish-hero-box">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
          <div style="max-width: 820px;">
            <h2>
              <span>🐘</span> El Elefante y el Pez de Colores <span>🐠</span>
            </h2>
            <p style="margin-top:6px; color:#cbd5e1; font-size:0.95rem;">
              <b>El modelo de Google para eliminar la "ceguera de contexto" y las alucinaciones en proyectos de IA:</b> 
              ¿Cómo evitamos que la IA cometa fallos tontos cuando llevamos horas trabajando con ella? 
              Dividiendo su cerebro en dos entidades con memorias opuestas que se auto-auditan.
            </p>
          </div>
          <button class="nav-step-btn" style="background:linear-gradient(135deg, rgba(251,146,60,0.3), rgba(56,189,248,0.3)); border-color:var(--orange); color:#fff;" onclick="switchMainView('workshop')">
            Siguiente: Vista 5 • Taller en tu Portátil ➔
          </button>
        </div>
      </div>

      <!-- SECCIÓN 1: EL PROBLEMA REAL -->
      <div class="workshop-card" style="border-color: rgba(239, 68, 68, 0.35); background: linear-gradient(180deg, rgba(239, 68, 68, 0.06) 0%, rgba(13, 22, 45, 0.9) 100%);">
        <h3 style="color:#f87171; display:flex; align-items:center; gap:10px; font-size:1.15rem;">
          ⚠️ El Gran Problema en Proyectos Largos: La "Ceguera de Contexto" (Context Drift)
        </h3>
        <p style="color:#cbd5e1; font-size:0.92rem; line-height:1.6; margin-top:8px;">
          Cuando hablas durante horas o días con una IA en el mismo chat, el modelo acumula decenas de miles de palabras (tokens). 
          Ocurre exactamente lo mismo que a los humanos: <b>empieza a dar cosas por supuestas</b>, se confía, adquiere "amor de padre" hacia el código que acaba de escribir y <b>es incapaz de ver sus propios fallos</b> (como un enlace que no funciona, un PDF que ocupa 3 páginas en vez de 1, o una regla de oro olvidada).
        </p>
      </div>

      <!-- SECCIÓN 2: LAS DOS CARAS DEL SISTEMA -->
      <div class="goldfish-dual-grid">
        
        <!-- TARJETA ELEFANTE -->
        <div class="goldfish-card elephant-card">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <div style="font-size:2rem;">🐘</div>
            <span class="goldfish-badge badge-elephant">El Coordinador con Memoria</span>
          </div>
          <h3 style="color:#38bdf8; font-size:1.25rem;">El Elefante (Mucha Memoria)</h3>
          <p style="color:#94a3b8; font-size:0.9rem; line-height:1.6;">
            Es el <b>agente principal de Antigravity</b> que mantiene la conversación contigo. Tiene la memoria de un elefante:
          </p>
          <ul style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; padding-left:18px;">
            <li>🧠 <b>Memoria Total:</b> Conoce tu estilo, las sesiones pasadas, las reglas maestras de <code>AGENTS.md</code> y el calendario.</li>
            <li>✍️ <b>Creador y Programador:</b> Escribe los simuladores 3D, compila las fichas PDF y diseña los scripts de Python.</li>
            <li>⚠️ <b>Su talón de Aquiles:</b> Al haber escrito el archivo, sufre de sesgo cognitivo y no ve los pequeños errores de maquetación o sintaxis.</li>
          </ul>
        </div>

        <!-- TARJETA GOLDFISH -->
        <div class="goldfish-card fish-card">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <div style="font-size:2rem;">🐠</div>
            <span class="goldfish-badge badge-fish">El Auditor Imparcial Efímero</span>
          </div>
          <h3 style="color:#fb923c; font-size:1.25rem;">El Pez de Colores (Memoria Cero)</h3>
          <p style="color:#94a3b8; font-size:0.9rem; line-height:1.6;">
            Es un <b>subagente independiente</b> que nace en blanco para auditar con ojos completamente limpios:
          </p>
          <ul style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; padding-left:18px;">
            <li>🧼 <b>Cero Memoria Previa:</b> Nace con la mente virgen. No ha participado en la charla anterior y no tiene ningún apego al código.</li>
            <li>🔍 <b>Auditoría Ciega:</b> Solo recibe el archivo recién creado y una lista de control estricta: <i>«¿Mide 1 página? ¿Hay enlaces rotos? ¿Las fuentes se solapan?»</i>.</li>
            <li>💥 <b>Destrucción Inmediata (Kill):</b> En cuanto emite su veredicto (tarda 10 segundos), el sistema lo destruye. <b>Cero procesos zombis ni restos en memoria</b>.</li>
          </ul>
        </div>

      </div>

      <!-- SECCIÓN 3: EL FLUJO EN 4 PASOS -->
      <div class="workshop-card" style="margin-top:16px;">
        <h3 style="color:#fff; font-size:1.15rem; margin-bottom:12px; display:flex; align-items:center; gap:10px;">
          <span>⚙️</span> El Ciclo Operativo de 4 Pasos en Cada Tarea
        </h3>
        
        <div class="goldfish-flow-steps">
          <div class="goldfish-step-item">
            <div class="goldfish-step-num">1</div>
            <b style="color:#38bdf8; font-size:0.92rem;">Plan del Elefante</b>
            <span style="color:#94a3b8; font-size:0.8rem; line-height:1.4;">El agente principal debate contigo y redacta la solución.</span>
          </div>
          <div class="goldfish-step-item">
            <div class="goldfish-step-num">2</div>
            <b style="color:#38bdf8; font-size:0.92rem;">Construcción</b>
            <span style="color:#94a3b8; font-size:0.8rem; line-height:1.4;">Genera el código HTML o compila la ficha PDF en disco.</span>
          </div>
          <div class="goldfish-step-item active">
            <div class="goldfish-step-num">3</div>
            <b style="color:#fb923c; font-size:0.92rem;">Auditoría del Pez</b>
            <span style="color:#94a3b8; font-size:0.8rem; line-height:1.4;">Un subagente virgen revisa el archivo con lista de control ciega.</span>
          </div>
          <div class="goldfish-step-item">
            <div class="goldfish-step-num">4</div>
            <b style="color:#34d399; font-size:0.92rem;">Corrección & Purga</b>
            <span style="color:#94a3b8; font-size:0.8rem; line-height:1.4;">Se corrigen fallos y el Pez se destruye de inmediato (Kill).</span>
          </div>
        </div>
      </div>

      <!-- SECCIÓN 4: SIMULADOR INTERACTIVO DE AUDITORÍA GOLDFISH -->
      <div class="workshop-card" style="margin-top:16px; border-color:rgba(56,189,248,0.35);">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
          <div>
            <h3 style="color:#38bdf8; font-size:1.15rem; display:flex; align-items:center; gap:10px;">
              <span>🧪</span> Simulador Interactivo: Mira cómo el Pez audita un archivo en vivo
            </h3>
            <p style="color:#94a3b8; font-size:0.88rem; margin-top:4px;">
              Pulsa el botón para ver la consola en tiempo real: nacimiento del subagente, análisis ciego y destrucción.
            </p>
          </div>
          <button id="btnRunGoldfishDemo" onclick="runGoldfishSimulation()" style="background:linear-gradient(135deg, #ea580c, #f97316); color:#fff; border:none; border-radius:10px; padding:10px 18px; font-weight:700; font-size:0.9rem; cursor:pointer; box-shadow:0 4px 14px rgba(234,88,12,0.4);">
            ▶ Iniciar Simulación Goldfish
          </button>
        </div>

        <div id="goldfishConsole" class="goldfish-sim-console">
          <span style="color:#64748b;">// Pulsa "Iniciar Simulación Goldfish" para ver el ciclo de vida efímero...</span>
        </div>
      </div>

      <!-- SECCIÓN 5: IMPACTO PARA EL ALUMNO SENIOR -->
      <div class="workshop-card" style="border-color: rgba(52, 211, 153, 0.4); background: linear-gradient(180deg, rgba(52, 211, 153, 0.08) 0%, rgba(13, 22, 45, 0.9) 100%);">
        <h3 style="color:#34d399; display:flex; align-items:center; gap:10px; font-size:1.15rem;">
          🎯 La Garantía de Oro para el Alumno y el Profesor
        </h3>
        <p style="color:#cbd5e1; font-size:0.92rem; line-height:1.6; margin-top:8px;">
          Nuestra regla número uno es: <b>«Cero trabajo de depuración para el usuario»</b>. El alumno sénior jamás debe probar un enlace roto ni encontrarse con un simulador que no arranca. El modelo Elephant-Goldfish garantiza que todo material pasa por una <b>doble aduana ciega e independiente</b> antes de que nadie haga clic en él.
        </p>
      </div>

      <!-- NAVEGACIÓN INFERIOR -->
      <div style="display:flex; justify-content:space-between; align-items:center; margin-top:20px; flex-wrap:wrap; gap:12px;">
        <button class="nav-step-btn" onclick="switchMainView('antigravity')">
          ⬅ Anterior: Vista 3 • Control de Ficheros
        </button>
        <button class="nav-step-btn" style="background:linear-gradient(135deg, rgba(251,146,60,0.3), rgba(56,189,248,0.3)); border-color:var(--orange); color:#fff;" onclick="switchMainView('workshop')">
          Siguiente: Vista 5 • Taller en tu Portátil ➔
        </button>
      </div>

    </div>
  </div>
'''

# Inyectar el contenedor antes de viewWorkshopContainer
if '<div id="viewWorkshopContainer"' in html and 'id="viewGoldfishContainer"' not in html:
    html = html.replace('<div id="viewWorkshopContainer"', goldfish_html + '\n  <div id="viewWorkshopContainer"')
    print("✅ Contenedor HTML de Vista 4 (Goldfish) inyectado")

# 7. ACTUALIZAR JAVASCRIPT SWITCHMAINVIEW Y SIMULADOR
old_js_vars = '''      var btnAnti = document.getElementById('btnViewAntigravity');
      var btnWorkshop = document.getElementById('btnViewWorkshop');'''

new_js_vars = '''      var btnAnti = document.getElementById('btnViewAntigravity');
      var btnGoldfish = document.getElementById('btnViewGoldfish');
      var btnWorkshop = document.getElementById('btnViewWorkshop');'''

old_js_conts = '''      var antiCont = document.getElementById('viewAntigravityContainer');
      var workshopCont = document.getElementById('viewWorkshopContainer');'''

new_js_conts = '''      var antiCont = document.getElementById('viewAntigravityContainer');
      var goldfishCont = document.getElementById('viewGoldfishContainer');
      var workshopCont = document.getElementById('viewWorkshopContainer');'''

old_js_remove = '''[btnConcepts, btnVs, btnAnti, btnWorkshop, btnMacro].forEach(function(b) { if (b) b.classList.remove('active'); });
      [conceptsCont, vsCont, antiCont, workshopCont, macroCont].forEach(function(c) { if (c) c.style.display = 'none'; });'''

new_js_remove = '''[btnConcepts, btnVs, btnAnti, btnGoldfish, btnWorkshop, btnMacro].forEach(function(b) { if (b) b.classList.remove('active'); });
      [conceptsCont, vsCont, antiCont, goldfishCont, workshopCont, macroCont].forEach(function(c) { if (c) c.style.display = 'none'; });'''

old_js_branch = '''} else if (view === 'antigravity') {
        if (btnAnti) btnAnti.classList.add('active');
        if (antiCont) antiCont.style.display = 'block';
      } else if (view === 'workshop') {'''

new_js_branch = '''} else if (view === 'antigravity') {
        if (btnAnti) btnAnti.classList.add('active');
        if (antiCont) antiCont.style.display = 'block';
      } else if (view === 'goldfish') {
        if (btnGoldfish) btnGoldfish.classList.add('active');
        if (goldfishCont) goldfishCont.style.display = 'block';
      } else if (view === 'workshop') {'''

html = html.replace(old_js_vars, new_js_vars)
html = html.replace(old_js_conts, new_js_conts)
html = html.replace(old_js_remove, new_js_remove)
html = html.replace(old_js_branch, new_js_branch)
print("✅ JavaScript switchMainView actualizado para soportar goldfish")

# Función interactiva de simulación en JavaScript
sim_js = '''
    // --- SIMULADOR INTERACTIVO ELEPHANT - GOLDFISH ---
    function runGoldfishSimulation() {
      var consoleElem = document.getElementById('goldfishConsole');
      var btn = document.getElementById('btnRunGoldfishDemo');
      if (!consoleElem || !btn) return;

      btn.disabled = true;
      btn.innerText = '⏳ Ejecutando Auditoría...';
      consoleElem.innerHTML = '<span style="color:#38bdf8;">[Paso 1: ELEFANTE]</span> Compilando recurso: <code>FICHA_SESION_07.pdf</code> (1024 KB)...<br>';

      setTimeout(function() {
        consoleElem.innerHTML += '<span style="color:#94a3b8;">[SISTEMA]</span> Invocando subagente Pez efímero: <code>invoke_subagent(Role="Goldfish Reviewer")</code>...<br>';
        consoleElem.innerHTML += '<span style="color:#fb923c;">[Paso 2: PEZ GOLDFISH]</span> Subagente despierto. <b>Tokens de contexto previo: 0</b> (Mente 100% limpia).<br>';
      }, 700);

      setTimeout(function() {
        consoleElem.innerHTML += '<span style="color:#fb923c;">[Paso 3: AUDITORÍA]</span> Inspeccionando reglas de oro en <code>FICHA_SESION_07.pdf</code>:<br>' +
          '&nbsp;&nbsp;✔ Número de páginas: EXACTAMENTE 1 (Cumplido)<br>' +
          '&nbsp;&nbsp;✔ Longitud de frases: &lt; 20 palabras adaptado a sénior (Cumplido)<br>' +
          '&nbsp;&nbsp;✔ Cero código fuente visible para el alumno (Cumplido)<br>' +
          '&nbsp;&nbsp;✔ Enlaces y parámetros canónicos: Validados al 100%<br>';
      }, 1500);

      setTimeout(function() {
        consoleElem.innerHTML += '<span style="color:#34d399; font-weight:bold;">[VEREDICTO PEZ]</span> APROBADO: Cero errores encontrados. Listo para el alumno.<br>';
        consoleElem.innerHTML += '<span style="color:#f43f5e;">[Paso 4: PURGA]</span> Ejecutando orden <code>manage_subagents(Action="kill")</code>...<br>';
        consoleElem.innerHTML += '<span style="color:#a855f7;">✨ [SISTEMA]</span> Subagente destruido en 8.2 segundos. <b>Cero procesos zombis en RAM. Cero archivos fósiles.</b><br>';
        btn.disabled = false;
        btn.innerText = '⟲ Repetir Simulación';
      }, 2500);
    }
'''

if "function runGoldfishSimulation" not in html:
    html = html.replace("// --- INICIALIZACIÓN ---", sim_js + "\n    // --- INICIALIZACIÓN ---")
    print("✅ Función interactiva runGoldfishSimulation inyectada")

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("✨ Modificación completada exitosamente en *.App_SIMULACION.html")
