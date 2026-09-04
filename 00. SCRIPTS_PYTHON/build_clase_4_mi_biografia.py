# -*- coding: utf-8 -*-
"""
Generador de la Clase Monográfica 4: "4. Mi_Biografia"
Crea la aplicación interactiva autónoma en HTML puro (Mi_Biografia.html)
y las fichas didácticas en PDF con formato idéntico a las ternas.
Incluye:
- Separación de acciones: Borrar grabación vs Quitar tema de la lista.
- Reordenación de temas (flechas ⬆️ / ⬇️).
- Regla de auto-corrección al hablar (si te equivocas, lo dices y la IA lo corrige).
- Regla de ordenación cronológica inteligente para anécdotas desordenadas.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(BASE_DIR, "CLASES", "4. Mi_Biografia")
os.makedirs(TARGET_DIR, exist_ok=True)

# ==============================================================================
# 1. GENERACIÓN DE LA APLICACIÓN HTML AUTÓNOMA (Mi_Biografia.html)
# ==============================================================================
HTML_CONTENT = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi Biografía - La Voz de Mi Vida</title>
  <style>
    :root {
      --primary: #1E3A8A;
      --primary-hover: #1E40AF;
      --accent: #D97706;
      --danger: #DC2626;
      --success: #16A34A;
      --bg: #F8FAFC;
      --card-bg: #FFFFFF;
      --text-main: #0F172A;
      --text-muted: #475569;
      --border: #CBD5E1;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; }
    body { background-color: var(--bg); color: var(--text-main); line-height: 1.6; padding: 24px 16px 80px; }
    .container { max-width: 960px; margin: 0 auto; }

    /* Cabecera */
    header { background: var(--card-bg); border: 2px solid var(--border); border-radius: 16px; padding: 28px; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }
    h1 { font-size: 2.2rem; color: var(--primary); margin-bottom: 8px; font-weight: 800; display: flex; align-items: center; gap: 12px; }
    p.subhead { font-size: 1.15rem; color: var(--text-muted); margin-bottom: 20px; }

    /* Barra de herramientas */
    .toolbar { display: flex; flex-wrap: wrap; gap: 12px; align-items: center; padding-top: 16px; border-top: 1px solid var(--border); }
    button { font-size: 1rem; font-weight: 700; padding: 12px 18px; border-radius: 10px; cursor: pointer; border: none; display: inline-flex; align-items: center; gap: 8px; transition: all 0.15s ease; }
    button:active { transform: scale(0.98); }
    .btn-danger { background-color: var(--danger); color: white; }
    .btn-danger:hover { background-color: #B91C1C; }
    .btn-success { background-color: var(--success); color: white; }
    .btn-success:hover { background-color: #15803D; }
    .btn-primary { background-color: var(--primary); color: white; }
    .btn-primary:hover { background-color: var(--primary-hover); }
    .btn-outline { background: transparent; border: 2px solid var(--border); color: var(--text-main); }
    .btn-outline:hover { background: #E2E8F0; }
    .btn-sm { padding: 6px 12px; font-size: 0.9rem; border-radius: 6px; }

    /* Banners informativos */
    .privacy-banner { background: #FEF3C7; border: 1px solid #F59E0B; border-radius: 10px; padding: 12px 16px; margin-bottom: 16px; font-size: 0.95rem; color: #92400E; }
    .tricks-banner { background: #EFF6FF; border: 1px solid #93C5FD; border-radius: 10px; padding: 14px 18px; margin-bottom: 24px; font-size: 0.95rem; color: #1E3A8A; line-height: 1.5; }

    /* Lista de Tarjetas */
    .chapters-list { display: flex; flex-direction: column; gap: 18px; }
    .chapter-card { background: var(--card-bg); border: 2px solid var(--border); border-radius: 14px; padding: 22px; transition: border-color 0.2s; position: relative; }
    .chapter-card.recorded { border-color: var(--success); background: #F0FDF4; }
    .card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; gap: 10px; }
    .card-title { font-size: 1.35rem; font-weight: 700; color: var(--primary); display: flex; align-items: center; gap: 10px; }
    .header-actions { display: flex; align-items: center; gap: 8px; }
    .status-badge { font-size: 0.85rem; font-weight: 700; padding: 4px 10px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.5px; }
    .badge-pending { background: #E2E8F0; color: #475569; }
    .badge-recorded { background: #DCFCE7; color: #166534; }
    .prompt-hint { font-size: 1.05rem; color: var(--text-muted); font-style: italic; margin-bottom: 14px; background: #F8FAFC; padding: 10px 14px; border-left: 4px solid var(--primary); border-radius: 0 8px 8px 0; }

    /* Notas de apoyo */
    .notes-input { width: 100%; min-height: 55px; font-size: 1rem; padding: 10px; border: 1px solid var(--border); border-radius: 8px; margin-bottom: 14px; resize: vertical; }

    /* Zona de Grabación */
    .record-actions { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
    .rec-btn { background: #DC2626; color: white; font-size: 1.05rem; }
    .rec-btn.recording { animation: pulse 1.2s infinite; background: #991B1B; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.6; } 100% { opacity: 1; } }
    .timer { font-size: 1.15rem; font-weight: 800; font-family: monospace; color: var(--danger); min-width: 60px; }
    audio { height: 42px; vertical-align: middle; }

    /* Pie de página y Botón Generar */
    .footer-actions { margin-top: 32px; text-align: center; }
    .btn-generate { font-size: 1.3rem; padding: 18px 36px; background: linear-gradient(135deg, #1E3A8A, #2563EB); color: white; border-radius: 14px; box-shadow: 0 10px 15px -3px rgba(37,99,235,0.3); }
    .btn-generate:hover { background: linear-gradient(135deg, #1E40AF, #1D4ED8); }

    /* Modales */
    .modal-overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 1000; align-items: center; justify-content: center; padding: 16px; }
    .modal-overlay.active { display: flex; }
    .modal-box { background: white; border-radius: 16px; max-width: 720px; width: 100%; max-height: 90vh; overflow-y: auto; padding: 28px; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.2); }
    .modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; border-bottom: 2px solid var(--border); padding-bottom: 12px; }
    .modal-title { font-size: 1.4rem; color: var(--primary); font-weight: 800; }
    .modal-content { font-size: 0.95rem; color: var(--text-main); margin-bottom: 20px; white-space: pre-wrap; background: #F1F5F9; padding: 16px; border-radius: 8px; border: 1px solid var(--border); max-height: 380px; overflow-y: auto; line-height: 1.5; }
    .modal-actions { display: flex; justify-content: flex-end; gap: 10px; }
  </style>
</head>
<body>

<div class="container">
  <header>
    <h1>📖 Mi Biografía: La Voz de Mi Vida</h1>
    <p class="subhead">Graba tus recuerdos paso a paso, a tu propio ritmo. Cada recuerdo queda a salvo en tu sesión y cuando quieras podrás <b>Generar tu Biografía</b> con Inteligencia Artificial.</p>
    
    <div class="toolbar">
      <button class="btn-success" onclick="exportToPendrive()">💾 Guardar copia en mi Pendrive</button>
      <button class="btn-primary" onclick="triggerImportPendrive()">📂 Abrir desde mi Pendrive</button>
      <button class="btn-outline" onclick="openAddTopicModal()">➕ Añadir nuevo tema / capítulo</button>
      <button class="btn-danger" style="margin-left: auto;" onclick="confirmClearClassroom()">🧹 Borrar todo al salir (Modo Aula)</button>
      <input type="file" id="pendriveInput" style="display:none;" accept=".json" onchange="importFromPendrive(event)">
    </div>
  </header>

  <div class="privacy-banner">
    🛡️ <b>Privacidad en Aula Compartida:</b> Si estás en el ordenador de clase, al terminar pulsa el botón rojo <b>«Borrar todo al salir»</b>. Así el siguiente alumno no podrá escuchar tus grabaciones. ¡Recuerda guardar antes una copia en tu pendrive!
  </div>

  <div class="tricks-banner">
    💡 <b>Dos trucos mágicos para hablar al micrófono con total tranquilidad:</b><br>
    • <b>1. Si te equivocas o dudas al hablar:</b> ¡No pares la grabación! Di con naturalidad <i>«Espera, me he equivocado: no fue en el 65 sino en el 68»</i> o <i>«Perdón, no era Juan sino Pedro»</i>. La Inteligencia Artificial está instruida para corregirlo sola y dejar el texto final limpio y perfecto.<br>
    • <b>2. Si te acuerdas de algo desordenado:</b> Cuéntalo cuando te venga a la mente, aunque haya ocurrido antes o después. La IA se encargará de ordenar cada recuerdo en su momento cronológico exacto de tu vida.
  </div>

  <div id="chaptersContainer" class="chapters-list"></div>

  <div class="footer-actions">
    <button class="btn-generate" onclick="generateBiographyModal()">✨ GENERAR MI BIOGRAFÍA</button>
  </div>
</div>

<!-- Modal para Añadir Tema -->
<div id="addTopicModal" class="modal-overlay">
  <div class="modal-box">
    <div class="modal-header">
      <h2 class="modal-title">➕ Añadir Nuevo Tema o Recuerdo</h2>
      <button class="btn-outline" onclick="closeModal('addTopicModal')">✕</button>
    </div>
    <p style="margin-bottom: 12px; color: var(--text-muted);">Puedes añadir cualquier aspecto de tu vida: tu trayectoria laboral, viajes especiales, anécdotas con amigos, aficiones, etc.</p>
    <label style="font-weight: 700; display: block; margin-bottom: 6px;">Título del tema:</label>
    <input type="text" id="newTopicTitle" placeholder="Ej: Mis 35 años de trabajo en la fábrica" style="width:100%; padding:10px; font-size:1.05rem; border:1px solid var(--border); border-radius:8px; margin-bottom:14px;">
    <label style="font-weight: 700; display: block; margin-bottom: 6px;">Pregunta o recuerdo que te inspire:</label>
    <input type="text" id="newTopicHint" placeholder="Ej: ¿Qué aprendí en mi empleo, qué compañeros recuerdo y cómo cambió el oficio?" style="width:100%; padding:10px; font-size:1.05rem; border:1px solid var(--border); border-radius:8px; margin-bottom:18px;">
    <div class="modal-actions">
      <button class="btn-outline" onclick="closeModal('addTopicModal')">Cancelar</button>
      <button class="btn-primary" onclick="addNewTopic()">Guardar Tema</button>
    </div>
  </div>
</div>

<!-- Modal de Generar Biografía -->
<div id="generateModal" class="modal-overlay">
  <div class="modal-box" style="max-width: 860px;">
    <div class="modal-header">
      <h2 class="modal-title">✨ Tu Biografía Lista para Gemini y NotebookLM</h2>
      <button class="btn-outline" onclick="closeModal('generateModal')">✕</button>
    </div>
    <p style="margin-bottom: 12px; color: var(--text-muted);">A continuación tienes el <b>Prompt Maestro</b> con todos tus temas y las instrucciones de auto-corrección y orden cronológico. Pulsa en <b>«Copiar todo»</b> y pégalo directamente en <b>Gemini</b>:</p>
    <div id="biographyOutputText" class="modal-content"></div>
    <div class="modal-actions">
      <button class="btn-outline" onclick="downloadTextFile()">⬇️ Descargar en archivo .txt</button>
      <button class="btn-primary" onclick="copyBiographyText()">📋 Copiar todo para Gemini</button>
    </div>
  </div>
</div>

<script>
// Temas base iniciales
const DEFAULT_TOPICS = [
  { id: 1, title: "1. Mis primeros años, mi casa y mi pueblo o barrio", hint: "¿Cómo era la casa de tu niñez, tu calle, a qué jugabas y qué olores o sonidos recuerdas?", notes: "", audioData: null },
  { id: 2, title: "2. La escuela, los maestros y los amigos de juventud", hint: "¿Cómo eran tus clases, qué maestros te marcaron y qué travesuras o juegos compartías con tus amigos?", notes: "", audioData: null },
  { id: 3, title: "3. Mi vida laboral y mis primeros pasos en el trabajo", hint: "¿A qué edad empezaste a trabajar, en qué oficio y qué sentiste al recibir tu primer sueldo?", notes: "", audioData: null },
  { id: 4, title: "4. Historias de juventud, amores y grandes amistades", hint: "¿Cómo eran los bailes o guateques de tu juventud, cómo conociste a personas clave y cómo formaste tu hogar?", notes: "", audioData: null },
  { id: 5, title: "5. Momentos históricos y cambios de época que viví", hint: "La llegada del hombre a la luna, el primer televisor en casa, el Seat 600... ¿Qué sentiste al vivirlo en persona?", notes: "", audioData: null },
  { id: 6, title: "6. Viajes memorables, tradiciones y anécdotas inolvidables", hint: "Aquel viaje especial, aquella receta familiar o aquella costumbre que no quieres que se pierda jamás.", notes: "", audioData: null },
  { id: 7, title: "7. Mis reflexiones de vida y consejos para el futuro", hint: "¿Qué es lo más valioso que te ha enseñado la vida y qué mensaje deseas transmitir a tus hijos y nietos?", notes: "", audioData: null }
];

let topics = [];
let mediaRecorder = null;
let audioChunks = [];
let recordingTopicId = null;
let timerInterval = null;
let recordingSeconds = 0;

// Cargar estado inicial
function init() {
  const saved = localStorage.getItem("mi_biografia_topics");
  if (saved) {
    try { topics = JSON.parse(saved); } catch(e) { topics = DEFAULT_TOPICS; }
  } else {
    topics = JSON.parse(JSON.stringify(DEFAULT_TOPICS));
  }
  renderTopics();
}

function saveState() {
  localStorage.setItem("mi_biografia_topics", JSON.stringify(topics));
}

function renderTopics() {
  const container = document.getElementById("chaptersContainer");
  container.innerHTML = "";
  
  topics.forEach((t, index) => {
    const card = document.createElement("div");
    card.className = "chapter-card" + (t.audioData ? " recorded" : "");
    card.id = `card-${t.id}`;
    
    const statusHtml = t.audioData 
      ? '<span class="status-badge badge-recorded">🟢 Grabado</span>' 
      : '<span class="status-badge badge-pending">⚪ Pendiente</span>';

    let audioPlayerHtml = "";
    if (t.audioData) {
      audioPlayerHtml = `
        <div style="display:flex; align-items:center; gap:10px; margin-top:12px; flex-wrap:wrap; padding:8px; background:#F8FAFC; border-radius:8px;">
          <audio controls src="${t.audioData}"></audio>
          <button class="btn-outline btn-sm" onclick="downloadSingleAudio(${t.id})">⬇️ Guardar este audio</button>
        </div>
      `;
    }

    card.innerHTML = `
      <div class="card-header">
        <div class="card-title">📖 ${t.title}</div>
        <div class="header-actions">
          ${statusHtml}
          <button class="btn-outline btn-sm" title="Subir orden" onclick="moveTopic(${index}, -1)">⬆️</button>
          <button class="btn-outline btn-sm" title="Bajar orden" onclick="moveTopic(${index}, 1)">⬇️</button>
          <button class="btn-outline btn-sm" style="color:var(--danger); border-color:#FECACA;" title="Quitar este tema de la lista" onclick="deleteTopicBlock(${t.id})">✖ Quitar tema</button>
        </div>
      </div>
      <div class="prompt-hint">${t.hint}</div>
      <textarea class="notes-input" placeholder="Apunta aquí nombres, fechas o recuerdos antes de hablar (opcional)..." onchange="updateNotes(${t.id}, this.value)">${t.notes || ""}</textarea>
      
      <div class="record-actions">
        <button id="rec-btn-${t.id}" class="rec-btn" onclick="toggleRecord(${t.id})">🎙️ GRABAR RECUERDO</button>
        <span id="timer-${t.id}" class="timer" style="display:none;">00:00</span>
        ${t.audioData ? `<button class="btn-outline" onclick="repeatRecord(${t.id})">🔄 Volver a grabar</button>` : ""}
        ${t.audioData || t.notes ? `<button class="btn-outline" style="color:#B91C1C; border-color:#FCA5A5;" onclick="clearTopicContentOnly(${t.id})">🗑️ Borrar grabación (dejar en blanco)</button>` : ""}
      </div>
      ${audioPlayerHtml}
    `;
    container.appendChild(card);
  });
}

function updateNotes(id, val) {
  const t = topics.find(x => x.id === id);
  if (t) { t.notes = val; saveState(); }
}

function moveTopic(index, direction) {
  const newIndex = index + direction;
  if (newIndex < 0 || newIndex >= topics.length) return;
  const temp = topics[index];
  topics[index] = topics[newIndex];
  topics[newIndex] = temp;
  saveState();
  renderTopics();
}

async function toggleRecord(id) {
  if (recordingTopicId === id) {
    stopRecording();
  } else {
    if (recordingTopicId !== null) stopRecording();
    startRecording(id);
  }
}

async function startRecording(id) {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    audioChunks = [];
    mediaRecorder = new MediaRecorder(stream);
    
    mediaRecorder.ondataavailable = e => { if (e.data.size > 0) audioChunks.push(e.data); };
    
    mediaRecorder.onstop = () => {
      const blob = new Blob(audioChunks, { type: 'audio/webm' });
      const reader = new FileReader();
      reader.onloadend = () => {
        const base64data = reader.result;
        const t = topics.find(x => x.id === id);
        if (t) {
          t.audioData = base64data;
          saveState();
          renderTopics();
        }
      };
      reader.readAsDataURL(blob);
      stream.getTracks().forEach(track => track.stop());
    };

    mediaRecorder.start();
    recordingTopicId = id;
    recordingSeconds = 0;

    const btn = document.getElementById(`rec-btn-${id}`);
    const timer = document.getElementById(`timer-${id}`);
    btn.classList.add("recording");
    btn.innerHTML = "⏹️ DETENER Y GUARDAR";
    timer.style.display = "inline";
    timer.innerText = "00:00";

    timerInterval = setInterval(() => {
      recordingSeconds++;
      const m = String(Math.floor(recordingSeconds / 60)).padStart(2, '0');
      const s = String(recordingSeconds % 60).padStart(2, '0');
      timer.innerText = `${m}:${s}`;
    }, 1000);

  } catch(err) {
    alert("No se pudo acceder al micrófono. Por favor, asegúrate de permitir el permiso de micrófono en tu navegador.");
  }
}

function stopRecording() {
  if (mediaRecorder && mediaRecorder.state !== "inactive") {
    mediaRecorder.stop();
  }
  clearInterval(timerInterval);
  recordingTopicId = null;
}

function repeatRecord(id) {
  if (confirm("¿Quieres volver a grabar este recuerdo? Se sustituirá la grabación anterior.")) {
    const t = topics.find(x => x.id === id);
    if (t) { t.audioData = null; saveState(); renderTopics(); }
  }
}

// 1. Borrar únicamente el contenido grabado, dejando el tema intacto
function clearTopicContentOnly(id) {
  if (confirm("¿Deseas BORRAR LA GRABACIÓN y notas de este tema?\\n\\nEl tema se mantendrá en tu lista (en estado Pendiente) para que puedas volver a grabarlo cuando quieras.")) {
    const t = topics.find(x => x.id === id);
    if (t) {
      t.audioData = null;
      t.notes = "";
      saveState();
      renderTopics();
    }
  }
}

// 2. Quitar el tema completo de la lista
function deleteTopicBlock(id) {
  if (confirm("¿Deseas QUITAR ESTE TEMA COMPLETO de tu lista de biografía?\\n\\nSe eliminará la tarjeta entera de la pantalla.")) {
    topics = topics.filter(x => x.id !== id);
    saveState();
    renderTopics();
  }
}

function openAddTopicModal() {
  document.getElementById("newTopicTitle").value = "";
  document.getElementById("newTopicHint").value = "";
  document.getElementById("addTopicModal").classList.add("active");
}

function closeModal(modalId) {
  document.getElementById(modalId).classList.remove("active");
}

function addNewTopic() {
  const title = document.getElementById("newTopicTitle").value.trim();
  const hint = document.getElementById("newTopicHint").value.trim();
  if (!title) { alert("Por favor, escribe un título para el nuevo tema."); return; }
  
  const newId = Date.now();
  topics.push({ id: newId, title: title, hint: hint || "Añade notas o graba tus vivencias sobre este tema.", notes: "", audioData: null });
  saveState();
  closeModal("addTopicModal");
  renderTopics();
}

// Privacidad en Aula
function confirmClearClassroom() {
  const ok = confirm("⚠️ ATENCIÓN MODO AULA:\\n\\n¿Deseas BORRAR todas tus grabaciones y textos de este ordenador?\\n\\nHaz esto SIEMPRE al terminar tu clase si el ordenador es compartido, para que nadie más escuche tu vida privada.\\n\\n¿Confirmas el borrado total?");
  if (ok) {
    localStorage.removeItem("mi_biografia_topics");
    topics = JSON.parse(JSON.stringify(DEFAULT_TOPICS));
    renderTopics();
    alert("✅ Todos tus recuerdos y audios han sido eliminados de este ordenador por seguridad.");
  }
}

// Pendrive: Guardar y Abrir
function exportToPendrive() {
  const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(topics));
  const a = document.createElement("a");
  a.setAttribute("href", dataStr);
  a.setAttribute("download", `Mi_Biografia_Sesion_${new Date().toISOString().slice(0,10)}.json`);
  document.body.appendChild(a);
  a.click();
  a.remove();
  alert("💾 Tu biografía se ha descargado. Guarda este archivo en tu Pendrive para llevarlo a casa o continuar en otra clase.");
}

function triggerImportPendrive() {
  document.getElementById("pendriveInput").click();
}

function importFromPendrive(event) {
  const file = event.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = e => {
    try {
      const imported = JSON.parse(e.target.result);
      if (Array.isArray(imported)) {
        topics = imported;
        saveState();
        renderTopics();
        alert("✅ Tu biografía se ha cargado correctamente desde el Pendrive.");
      } else {
        alert("El archivo no tiene el formato correcto.");
      }
    } catch(err) {
      alert("Error al leer el archivo de tu pendrive.");
    }
  };
  reader.readAsText(file);
}

function downloadSingleAudio(id) {
  const t = topics.find(x => x.id === id);
  if (!t || !t.audioData) return;
  const a = document.createElement("a");
  a.href = t.audioData;
  a.download = `Recuerdo_${t.title.replace(/[^a-zA-Z0-9]/g, '_')}.webm`;
  document.body.appendChild(a);
  a.click();
  a.remove();
}

// Generación de Biografía para Gemini y NLM con Auto-corrección y Cronología
function generateBiographyModal() {
  let fullPrompt = "Actúa como un biógrafo literario y escritor sensible profesional. A continuación te entrego las memorias y reflexiones recopiladas a lo largo de mi vida, organizadas por etapas y temas.\\n\\n";
  fullPrompt += "🧠 REGLAS CRÍTICAS DE REDACCIÓN Y EDICIÓN INTELIGENTE:\\n";
  fullPrompt += "1. AUTO-CORRECCIÓN INTELIGENTE: Si en mis relatos digo frases como 'espera, me he equivocado', 'perdón, no fue en ese año sino en...', o 'quería decir...', interpreta la rectificación automáticamente. Elimina el error y deja únicamente el dato corregido en el texto final.\\n";
  fullPrompt += "2. REORDENACIÓN CRONOLÓGICA: Si cuento anécdotas desordenadas (por ejemplo, menciono un recuerdo de mi infancia mientras hablaba de mi trabajo), ubica cada suceso en su momento vital correspondiente para que la historia fluya en un orden temporal perfecto y natural.\\n";
  fullPrompt += "3. TONO Y ESTILO: Redacta un libro biográfico cálido, elegante y emotivo, dividido en capítulos hermosos, manteniendo mi voz auténtica y destacando las lecciones de vida y valores.\\n";
  fullPrompt += "4. FORMATO: Deja el texto impecable para que sirva como fuente documental que después subiré a NotebookLM para generar mi libro de memorias en PDF y un podcast familiar.\\n\\n";
  fullPrompt += "ESTE ES EL MATERIAL Y LOS CAPÍTULOS DE MI VIDA:\\n";
  fullPrompt += "========================================================\\n\\n";

  topics.forEach((t, i) => {
    fullPrompt += `CAPÍTULO ${i+1}: ${t.title.toUpperCase()}\\n`;
    fullPrompt += `• Pregunta guía: ${t.hint}\\n`;
    if (t.notes) fullPrompt += `• Notas y recuerdos del autor: ${t.notes}\\n`;
    if (t.audioData) fullPrompt += `• [Recuerdo grabado por el autor con su voz - Incluir en este capítulo]\\n`;
    fullPrompt += "\\n";
  });

  fullPrompt += "========================================================\\n";
  fullPrompt += "Genera ahora la biografía completa estructurada por capítulos siguiendo las reglas anteriores.";

  document.getElementById("biographyOutputText").innerText = fullPrompt;
  document.getElementById("generateModal").classList.add("active");
}

function copyBiographyText() {
  const text = document.getElementById("biographyOutputText").innerText;
  navigator.clipboard.writeText(text).then(() => {
    alert("📋 ¡Copiado al portapapeles! Ahora abre Google Gemini y pulsa 'Pegar' (Ctrl + V).");
  });
}

function downloadTextFile() {
  const text = document.getElementById("biographyOutputText").innerText;
  const element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', `Mi_Biografia_para_Gemini_${new Date().toISOString().slice(0,10)}.txt`);
  document.body.appendChild(element);
  element.click();
  element.remove();
}

window.onload = init;
</script>
</body>
</html>
"""

# ==============================================================================
# 2. GENERADOR DE FICHAS PDF IDÉNTICAS A LAS TERNAS
# ==============================================================================
def create_pdf_ficha(filename, title, content):
    file_path = os.path.join(TARGET_DIR, filename)
    doc = SimpleDocTemplate(file_path, pagesize=letter, rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45)
    styles = getSampleStyleSheet()
    
    style_title = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=15, textColor=colors.HexColor('#1E3A8A'), spaceAfter=14)
    style_body = ParagraphStyle('BodyStyle', parent=styles['BodyText'], fontName='Helvetica', fontSize=11, leading=16, textColor=colors.HexColor('#2C3E50'), spaceAfter=8)
    style_prompt = ParagraphStyle('PromptStyle', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=10, leading=15, textColor=colors.HexColor('#0F172A'))
    
    story = []
    story.append(Paragraph(title, style_title))
    
    if "PASO 0" in title:
        intro_p = (
            "En esta clase monográfica aprenderás a utilizar la aplicación interactiva <b>Mi_Biografia.html</b> para grabar tus vivencias paso a paso a lo largo de los días, sin prisas y a tu propio ritmo.<br/><br/>"
            "El proyecto une la tecnología más humana para que dejes tu legado personal, laboral o viajero:<br/>"
            "- <b>GRABACIÓN EN EL PC (Mi_Biografia.html):</b> Abres la app en el navegador haciendo doble clic, eliges el tema que quieras contar hoy y hablas tranquilamente al micrófono.<br/>"
            "- <b>HABLA CON TRANQUILIDAD (AUTO-CORRECCIÓN):</b> Si te equivocas, no pares la grabación: di <i>«Espera, me he equivocado...»</i> y la IA lo rectificará sola. Y si recuerdas algo desordenado, la IA lo ordenará cronológicamente.<br/>"
            "- <b>PRIVACIDAD EN EL AULA:</b> Si usas un ordenador compartido en clase, la app tiene un botón rojo de <i>Borrar todo al salir</i> para que nadie escuche tus recuerdos privados. Y puedes llevarte todo en tu pendrive.<br/>"
            "- <b>GENERAR CON GEMINI:</b> Cuando tengas varios temas grabados, un solo botón une tus vivencias y le pide a Gemini que redacte tu biografía literaria en capítulos.<br/>"
            "- <b>PODCAST Y LIBRO EN NOTEBOOKLM:</b> Pasas el texto a NotebookLM para generar tu libro de memorias en PDF y un podcast de audio."
        )
        story.append(Paragraph(intro_p, style_body))
    elif "PASO 1" in title:
        story.append(Paragraph("📝 INSTRUCCIONES GUÍA (1/3): Haz doble clic sobre <b>Mi_Biografia.html</b>. Elige una etapa de tu vida y pulsa <b>GRABAR RECUERDO</b>. Puedes añadir nuevos temas libres como tu vida laboral o tus viajes.", style_body))
    elif "PASO 2" in title:
        story.append(Paragraph("📝 INSTRUCCIONES GUÍA (2/3): Cuando tengas tus recuerdos listos, pulsa en la aplicación el botón <b>GENERAR MI BIOGRAFÍA</b>. Copia el texto y pégalo en Gemini con este prompt maestro:", style_body))
    elif "PASO 3" in title:
        story.append(Paragraph("📝 INSTRUCCIONES GUÍA (3/3): Abre NotebookLM, añade el texto de tu biografía como fuente y genera la presentación visual y el podcast de audio para tu familia.", style_body))
        
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=14))
    
    for blk in content.split("\n"):
        if blk.strip():
            story.append(Paragraph(blk.strip(), style_prompt))
        else:
            story.append(Spacer(1, 4))
            
    doc.build(story)
    return file_path

# ==============================================================================
# EJEMPLO REAL DE BIOGRAFÍA YA GENERADA EN PDF
# ==============================================================================
EJEMPLO_BIOGRAFIA_TEXTO = """MEMORIAS DE UNA VIDA: EL CAMINO RECORRIDO

CAPÍTULO 1: LA CALLE EMPEDRADA Y EL OLOR A PAN CALIENTE
Nací en un pueblo donde el tiempo no corría por relojes digitales sino por las campanadas de la iglesia y la luz del sol sobre los campos. Mi casa tenía muros anchos de piedra que guardaban el frescor en verano y el calor del brasero en las largas noches de invierno. Jugábamos a las chapas, a la peonza de madera y a escondernos entre las eras de trillar. No teníamos pantallas, pero teníamos una imaginación infinita que convertía un trozo de madera en una espada y un viejo neumático en una nave espacial.

CAPÍTULO 2: EL MAESTRO DON ANTONIO Y LA PIZARRA DE TIZA
La escuela era un aula única donde convivíamos niños de todas las edades. Don Antonio nos enseñaba matemáticas con granos de trigo y geografía señalando mapas gastados que colgaban de la pared. De él aprendí que la curiosidad es el motor del mundo y que saber leer y escribir con soltura abre puertas que nadie puede cerrar. Aún recuerdo el olor a tinta china y el tacto áspero del papel secante.

CAPÍTULO 3: CUARENTA AÑOS EN EL FERROCARRIL: EL VALOR DEL TRABAJO
A los diecisiete años entré como aprendiz en los talleres de la estación. Vi cómo las locomotoras de vapor daban paso a las diésel y más tarde a la electrificación. En aquel taller aprendí lo que significa la solidaridad entre compañeros: cuando el trabajo era duro o una pieza se atascaba, siempre había dos manos amigas dispuestas a empujar a tu lado. Mi primer sueldo se lo entregué íntegro a mi madre en la cocina; aquel orgullo me acompañará hasta el último día.

CAPÍTULO 4: EL VIAJE QUE ME CAMBIÓ LA MIRADA
A los cincuenta años pude hacer mi primer gran viaje fuera de España. Tomar aquel tren nocturno y despertar frente a las costas del norte me demostró que el mundo es un libro inmenso y que quien no viaja solo lee la primera página. Aquellos paisajes me enseñaron que todos los seres humanos, vivamos donde vivamos, buscamos exactamente lo mismo: paz, respeto y ver felices a los que queremos.

CAPÍTULO 5: LO QUE HE APRENDIDO Y QUIERO DEJAROS
Si algo me ha enseñado este largo camino es que las posesiones materiales se gastan y se olvidan, pero las horas compartidas con la gente a la que amas son eternas. A vosotros, mis nietos, os pido que nunca tengáis prisa por crecer, que escuchéis a los mayores no porque seamos más listos, sino porque ya nos hemos equivocado muchas veces antes, y que tratéis siempre a los demás con la misma bondad con la que os gustaría ser recordados."""

def build_all():
    print("🚀 Generando materiales para '4. Mi_Biografia'...")
    
    # 1. Guardar la App HTML interactiva
    html_path = os.path.join(TARGET_DIR, "Mi_Biografia.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print("  ✅ Creada la aplicación interactiva Mi_Biografia.html")
    
    # 2. Paso 0: Introducción del Proyecto
    create_pdf_ficha(
        "0. Paso_0_Introduccion_Proyecto.pdf",
        "PASO 0: PROYECTO MI BIOGRAFÍA INTERACTIVA",
        ""
    )
    
    # 3. Paso 1: Guía de Grabación
    p1_text = (
        "CÓMO USAR LA APLICACIÓN 'Mi_Biografia.html':\n\n"
        "1. Haz doble clic sobre el archivo 'Mi_Biografia.html' desde tu ordenador.\n"
        "2. Se abrirá automáticamente en tu navegador (Edge o Chrome). No necesitas instalar nada.\n"
        "3. Elige la etapa que quieras contar hoy y pulsa el botón '🎙️ GRABAR RECUERDO'.\n"
        "4. Habla con calma y tranquilidad al micrófono del ordenador. Cuando termines, pulsa '⏹️ DETENER Y GUARDAR'.\n"
        "5. Si quieres contar algo diferente (tu trabajo, tus viajes, tus aficiones), pulsa el botón '➕ Añadir nuevo tema / capítulo'.\n\n"
        "💡 DOS TRUCOS MÁGICOS PARA HABLAR CON TOTAL TRANQUILIDAD:\n"
        "• Si te equivocas o dudas: ¡No pares la grabación! Di con naturalidad 'Espera, me he equivocado, fue en...' y la IA lo corregirá sola al generar el texto limpio.\n"
        "• Si te acuerdas de algo desordenado: Cuéntalo cuando te venga a la mente, la IA ordenará cada recuerdo cronológicamente.\n\n"
        "🛡️ REGLA DE PRIVACIDAD EN EL AULA:\n"
        "Si estás en un ordenador compartido de clase, antes de marcharte pulsa '💾 Guardar en mi Pendrive' para llevarte tu trabajo a casa y luego pulsa '🧹 Borrar todo al salir (Modo Aula)'. Así nadie podrá escuchar tu vida."
    )
    create_pdf_ficha(
        "1. Paso_1_Grabar_Recuerdos_y_Temas.pdf",
        "PASO 1: GRABAR TUS RECUERDOS POR ETAPAS",
        p1_text
    )
    
    # 4. Paso 2: Generar Biografía con Gemini
    p2_text = (
        "PROMPT MAESTRO PARA GEMINI:\n\n"
        "Actúa como un biógrafo literario y escritor sensible profesional. A continuación te entrego las memorias y reflexiones recopiladas a lo largo de mi vida, organizadas por etapas y temas.\n\n"
        "🧠 REGLAS CRÍTICAS DE REDACCIÓN Y EDICIÓN INTELIGENTE:\n"
        "1. AUTO-CORRECCIÓN INTELIGENTE: Si en mis relatos digo frases como 'espera, me he equivocado', 'perdón, no fue en ese año sino en...', o 'quería decir...', interpreta la rectificación automáticamente. Elimina el error y deja únicamente el dato corregido en el texto final.\n"
        "2. REORDENACIÓN CRONOLÓGICA: Si cuento anécdotas desordenadas (por ejemplo, menciono un recuerdo de mi infancia mientras hablaba de mi trabajo), ubica cada suceso en su momento vital correspondiente para que la historia fluya en un orden temporal perfecto y natural.\n"
        "3. TONO Y ESTILO: Redacta un libro biográfico cálido, elegante y emotivo, dividido en capítulos hermosos, manteniendo mi voz auténtica y destacando las lecciones de vida y valores.\n"
        "4. FORMATO: Deja el texto impecable para que sirva como fuente documental que después subiré a NotebookLM para generar mi libro de memorias en PDF y un podcast familiar.\n\n"
        "ESTE ES EL MATERIAL DE MI VIDA:\n"
        "[Pega aquí el contenido generado desde el botón 'GENERAR MI BIOGRAFÍA' de la aplicación]\n\n"
        "Genera ahora la biografía completa estructurada por capítulos siguiendo las reglas anteriores."
    )
    create_pdf_ficha(
        "2. Paso_2_Generar_Biografia_con_Gemini.pdf",
        "PASO 2: GENERAR TU BIOGRAFÍA CON GEMINI",
        p2_text
    )
    
    # 5. Paso 3: Crear Podcast y Libro en NotebookLM
    p3_text = (
        "CÓMO GENERAR TU PODCAST Y LIBRO EN NOTEBOOKLM:\n\n"
        "1. Entra en notebooklm.google.com e inicia sesión con tu cuenta de Google.\n"
        "2. Crea un 'Cuaderno Nuevo' y ponle de título: 'Mi Biografía'.\n"
        "3. En Fuentes, selecciona 'Texto Copiado' y pega el texto de tu biografía que acaba de redactar Gemini.\n"
        "4. En la barra derecha de Guía del Cuaderno:\n"
        "   • Pulsa en 'Conversación de Audio' (Audio Overview) para generar el podcast donde dos presentadores conversan y analizan con emoción la historia de tu vida.\n"
        "   • Pulsa en 'Presentación' para generar el resumen visual con diapositivas maquetadas de tus memorias.\n"
        "5. Descarga el audio MP3 y la presentación para guardarlos en tu pendrive o compartirlos con quien tú quieras."
    )
    create_pdf_ficha(
        "3. Paso_3_Crear_Podcast_y_Libro_en_NLM.pdf",
        "PASO 3: CREAR PODCAST Y LIBRO EN NOTEBOOKLM",
        p3_text
    )
    
    # 6. Ejemplo real en PDF listo para NotebookLM
    ejemplo_pdf = os.path.join(TARGET_DIR, "EJEMPLO_A_FUENTE_BIOGRAFIA_PARA_NOTEBOOKLM.pdf")
    doc_e = SimpleDocTemplate(ejemplo_pdf, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
    styles = getSampleStyleSheet()
    st_t = ParagraphStyle('ETitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=14, textColor=colors.HexColor('#1E3A8A'), spaceAfter=12)
    st_b = ParagraphStyle('EBody', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=15, textColor=colors.HexColor('#1E293B'))
    
    st_story = [Paragraph("MEMORIAS DE UNA VIDA: EL CAMINO RECORRIDO", st_t), HRFlowable(width="100%", thickness=1, color=colors.HexColor('#1E3A8A'), spaceAfter=12)]
    for line in EJEMPLO_BIOGRAFIA_TEXTO.split("\n"):
        if line.startswith("CAPÍTULO"):
            st_story.append(Spacer(1, 8))
            st_story.append(Paragraph(f"<b>{line}</b>", ParagraphStyle('Sub', parent=st_b, fontSize=11, textColor=colors.HexColor('#B45309'))))
        elif line.strip():
            st_story.append(Paragraph(line, st_b))
        else:
            st_story.append(Spacer(1, 4))
    doc_e.build(st_story)
    print("  ✅ Creado el ejemplo de biografía en PDF")
    
    print("🎉 ¡Clase Monográfica 4. Mi_Biografia completada y actualizada con éxito!")

if __name__ == "__main__":
    build_all()
