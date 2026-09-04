# -*- coding: utf-8 -*-
"""
Clase Monográfica 4: "4. Mi_Biografia"
Genera:
1. Mi_Biografia.html -> Aplicación web interactiva autónoma (sin errores de sintaxis JS).
2. Manual_de_Instrucciones.pdf -> ÚNICO DOCUMENTO para el alumno.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(BASE_DIR, "CLASES", "4. Mi_Biografia")
os.makedirs(TARGET_DIR, exist_ok=True)

# ==============================================================================
# 1. GENERACIÓN DE LA APLICACIÓN HTML AUTÓNOMA (Mi_Biografia.html)
# ==============================================================================
HTML_CONTENT = r"""<!DOCTYPE html>
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
    .btn-secondary { background-color: #475569; color: white; }
    .btn-secondary:hover { background-color: #334155; }
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
    .card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; gap: 10px; flex-wrap: wrap; }
    .card-title { font-size: 1.35rem; font-weight: 700; color: var(--primary); display: flex; align-items: center; gap: 10px; }
    .header-actions { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
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
    .modal-box { background: white; border-radius: 16px; max-width: 860px; width: 100%; max-height: 90vh; overflow-y: auto; padding: 28px; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.2); }
    .modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; border-bottom: 2px solid var(--border); padding-bottom: 12px; }
    .modal-title { font-size: 1.4rem; color: var(--primary); font-weight: 800; }
    .modal-content { font-size: 1rem; color: var(--text-main); margin-bottom: 20px; white-space: pre-wrap; background: #F1F5F9; padding: 16px; border-radius: 8px; border: 1px solid var(--border); max-height: 380px; overflow-y: auto; }
    .modal-actions { display: flex; justify-content: flex-end; gap: 10px; flex-wrap: wrap; }
  </style>
</head>
<body>

<div class="container">
  <header>
    <h1>📖 Mi Biografía: La Voz de Mi Vida</h1>
    <p class="subhead">Graba tus recuerdos paso a paso en tu ordenador, a tu propio ritmo. Cada recuerdo queda a salvo en tu sesión y cuando quieras podrás <b>Generar tu Biografía</b> con Inteligencia Artificial.</p>
    
    <div class="toolbar">
      <button class="btn-success" onclick="exportToPendrive()">💾 Guardar copia en mi Pendrive / PC</button>
      <button class="btn-primary" onclick="triggerImportPendrive()">📂 Abrir copia de seguridad</button>
      <button class="btn-outline" onclick="openAddTopicModal()">➕ Añadir nuevo tema / capítulo</button>
      <button class="btn-danger" style="margin-left: auto;" onclick="confirmClearClassroom()">🧹 Borrar todo al salir (Modo Aula)</button>
      <input type="file" id="pendriveInput" style="display:none;" accept=".json" onchange="importFromPendrive(event)">
    </div>
  </header>

  <div class="privacy-banner">
    🛡️ <b>Privacidad en Aula Compartida:</b> Si estás en el ordenador de clase, al terminar pulsa el botón rojo <b>«Borrar todo al salir»</b>. Así el siguiente alumno no podrá escuchar tus grabaciones. En el ordenador de tu casa <b>NO</b> hace falta pulsarlo; Chrome guardará tus recuerdos de un día para otro.
  </div>

  <div class="tricks-banner">
    💡 <b>Dos trucos mágicos para hablar al micrófono con total tranquilidad:</b><br>
    • <b>1. Si te equivocas o dudas al hablar:</b> ¡No pares la grabación! Di con naturalidad <i>«Espera, me he equivocado: no fue en el 65 sino en el 68»</i> o <i>«Perdón, no era Juan sino Pedro»</i>. La aplicación se encarga de que la Inteligencia Artificial corrija el error automáticamente y deje el texto limpio.<br>
    • <b>2. Si te acuerdas de algo desordenado:</b> Cuéntalo cuando te venga a la mente, aunque haya ocurrido antes o después. La aplicación se encarga de que cada recuerdo quede colocado en su momento cronológico exacto de tu vida.
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
      <h2 class="modal-title">✨ Tu Biografía Lista para Gemini, Word y NotebookLM</h2>
      <button class="btn-outline" onclick="closeModal('generateModal')">✕</button>
    </div>
    <div style="background:#F0FDF4; border:1px solid #86EFAC; border-radius:10px; padding:14px 18px; margin-bottom:16px; font-size:0.95rem; color:#166534; line-height:1.5;">
      <b>📋 Pasos para completar tu obra:</b><br>
      1. Pulsa en <b>«📋 Copiar todo»</b>.<br>
      2. Abre <b>Google Gemini</b> en tu navegador y pulsa <b>Pegar</b> (Ctrl + V) y Enviar.<br>
      3. Lee tu historia redactada. Si quieres añadir un detalle, escríbelo en la conversación (ej: <i>«En el capítulo 3 añade mi Seat 600...»</i>).<br>
      4. Copia el resultado final de Gemini, abre <b>Microsoft Word</b> en tu ordenador y pulsa <b>Pegar</b> para guardarlo como documento (.docx) o imprimirlo con fotos.
    </div>
    <div id="biographyOutputText" class="modal-content"></div>
    <div class="modal-actions">
      <button class="btn-outline" onclick="downloadTextFile()">⬇️ Descargar texto (.txt)</button>
      <button class="btn-primary" onclick="copyBiographyText()">📋 Copiar todo</button>
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
    try {
      const parsed = JSON.parse(saved);
      if (Array.isArray(parsed) && parsed.length > 0) {
        topics = parsed;
      } else {
        topics = JSON.parse(JSON.stringify(DEFAULT_TOPICS));
      }
    } catch(e) {
      topics = JSON.parse(JSON.stringify(DEFAULT_TOPICS));
    }
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
  if (!container) return;
  container.innerHTML = "";
  
  topics.forEach((t, index) => {
    const card = document.createElement("div");
    card.className = "chapter-card" + (t.audioData ? " recorded" : "");
    card.id = "card-" + t.id;
    
    const statusHtml = t.audioData 
      ? '<span class="status-badge badge-recorded">🟢 Grabado</span>' 
      : '<span class="status-badge badge-pending">⚪ Pendiente</span>';

    let audioPlayerHtml = "";
    if (t.audioData) {
      audioPlayerHtml = '<div style="display:flex; align-items:center; gap:12px; margin-top:14px; flex-wrap:wrap; padding:12px; background:#EFF6FF; border:1px solid #BFDBFE; border-radius:10px;">'
        + '<span style="font-weight:700; color:var(--primary); font-size:0.95rem;">🔊 Tu recuerdo grabado:</span>'
        + '<audio controls src="' + t.audioData + '"></audio>'
        + '<button class="btn-outline btn-sm" style="background:white; font-weight:700;" onclick="downloadSingleAudio(' + t.id + ')">💾 Guardar archivo de audio (.webm)</button>'
        + '</div>';
    }

    card.innerHTML = '<div class="card-header">'
      + '<div class="card-title">📖 ' + t.title + '</div>'
      + '<div class="header-actions">'
      + statusHtml
      + '<button class="btn-outline btn-sm" title="Subir orden del tema" onclick="moveTopic(' + index + ', -1)">⬆️ Subir</button>'
      + '<button class="btn-outline btn-sm" title="Bajar orden del tema" onclick="moveTopic(' + index + ', 1)">⬇️ Bajar</button>'
      + '<button class="btn-outline btn-sm" style="color:var(--danger); border-color:#FECACA;" title="Quitar este tema de la lista" onclick="deleteTopicBlock(' + t.id + ')">✖ Quitar tema</button>'
      + '</div>'
      + '</div>'
      + '<div class="prompt-hint">' + t.hint + '</div>'
      + '<textarea class="notes-input" placeholder="Apunta aquí nombres, fechas o recuerdos antes de hablar (opcional)..." onchange="updateNotes(' + t.id + ', this.value)">' + (t.notes || "") + '</textarea>'
      + '<div class="record-actions">'
      + '<button id="rec-btn-' + t.id + '" class="rec-btn" onclick="toggleRecord(' + t.id + ')">🎙️ GRABAR RECUERDO</button>'
      + '<span id="timer-' + t.id + '" class="timer" style="display:none;">00:00</span>'
      + (t.audioData ? '<button class="btn-outline" onclick="repeatRecord(' + t.id + ')">🔄 Volver a grabar</button>' : "")
      + (t.audioData || t.notes ? '<button class="btn-outline" style="color:#B91C1C; border-color:#FCA5A5;" onclick="clearTopicContentOnly(' + t.id + ')">🗑️ Borrar grabación (dejar en blanco)</button>' : "")
      + '</div>'
      + audioPlayerHtml;
      
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
        const base64Audio = reader.result;
        const topic = topics.find(x => x.id === id);
        if (topic) {
          topic.audioData = base64Audio;
          saveState();
          renderTopics();
        }
      };
      reader.readAsDataURL(blob);
      stream.getTracks().forEach(track => track.stop());
    };

    mediaRecorder.start();
    recordingTopicId = id;
    
    const btn = document.getElementById('rec-btn-' + id);
    if (btn) {
      btn.innerText = "⏹️ DETENER Y GUARDAR";
      btn.classList.add("recording");
    }
    
    const timer = document.getElementById('timer-' + id);
    if (timer) {
      timer.style.display = "inline";
      recordingSeconds = 0;
      timer.innerText = "00:00";
    }
    
    timerInterval = setInterval(() => {
      recordingSeconds++;
      const m = String(Math.floor(recordingSeconds / 60)).padStart(2, '0');
      const s = String(recordingSeconds % 60).padStart(2, '0');
      if (timer) timer.innerText = m + ':' + s;
    }, 1000);

  } catch (err) {
    alert("No se pudo acceder al micrófono. Por favor comprueba los permisos en tu navegador.");
    console.error(err);
  }
}

function stopRecording() {
  if (mediaRecorder && mediaRecorder.state !== "inactive") {
    mediaRecorder.stop();
  }
  clearInterval(timerInterval);
  recordingTopicId = null;
  renderTopics();
}

function repeatRecord(id) {
  if (confirm("¿Quieres volver a grabar este recuerdo? La grabación anterior se sustituirá por la nueva.")) {
    toggleRecord(id);
  }
}

// 1. Borrar únicamente el contenido grabado y notas (dejar el capítulo en blanco)
function clearTopicContentOnly(id) {
  const t = topics.find(x => x.id === id);
  if (!t) return;
  if (confirm("¿Deseas borrar la grabación y notas de este tema?\n\nEl capítulo permanecerá en tu lista para que puedas volver a grabarlo.")) {
    t.audioData = null;
    t.notes = "";
    saveState();
    renderTopics();
  }
}

// 2. Eliminar el bloque o capítulo completo de la lista
function deleteTopicBlock(id) {
  const t = topics.find(x => x.id === id);
  if (!t) return;
  if (confirm("¿Quieres quitar este tema por completo de tu biografía?")) {
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
  const ok = confirm("⚠️ ATENCIÓN MODO AULA:\n\n¿Deseas BORRAR todas tus grabaciones y textos de este ordenador?\n\nHaz esto SIEMPRE al terminar tu clase si el ordenador es compartido, para que nadie más escuche tu vida privada.\n\n¿Confirmas el borrado total?");
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
  a.setAttribute("download", "Mi_Biografia_Sesion_" + new Date().toISOString().slice(0,10) + ".json");
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
        alert("✅ Tu biografía se ha cargado correctamente desde tu archivo.");
      } else {
        alert("El archivo no tiene el formato correcto.");
      }
    } catch(err) {
      alert("Error al leer el archivo de copia de seguridad.");
    }
  };
  reader.readAsText(file);
}

function downloadSingleAudio(id) {
  const t = topics.find(x => x.id === id);
  if (!t || !t.audioData) return;
  const a = document.createElement("a");
  a.href = t.audioData;
  a.download = "Recuerdo_" + t.title.replace(/[^a-zA-Z0-9]/g, '_') + ".webm";
  document.body.appendChild(a);
  a.click();
  a.remove();
}

// Generación de Biografía
function generateBiographyModal() {
  let fullPrompt = "Actúa como un biógrafo literario y escritor sensible profesional. A continuación te entrego las memorias y reflexiones recopiladas a lo largo de mi vida, organizadas por etapas y temas.\n\n";
  fullPrompt += "🧠 REGLAS DE REDACCIÓN Y EDICIÓN:\n";
  fullPrompt += "1. AUTO-CORRECCIÓN: Si en mis relatos digo frases como 'espera, me he equivocado', 'perdón, no fue en ese año sino en...', o 'quería decir...', interpreta la rectificación automáticamente. Elimina el error y deja únicamente el dato corregido en el texto final.\n";
  fullPrompt += "2. REORDENACIÓN CRONOLÓGICA: Si cuento anécdotas desordenadas (por ejemplo, menciono un recuerdo de mi infancia mientras hablaba de mi trabajo), ubica cada suceso en su momento vital correspondiente para que la historia fluya en un orden temporal perfecto y natural.\n";
  fullPrompt += "3. TONO Y ESTILO: Redacta un libro biográfico cálido, elegante y emotivo, dividido en capítulos hermosos, manteniendo mi voz auténtica y destacando las lecciones de vida y valores.\n";
  fullPrompt += "4. FORMATO: Deja el texto impecable para copiarlo y pegarlo en Microsoft Word para guardarlo en el ordenador e imprimirlo en papel, y para usarlo en NotebookLM para generar un podcast familiar.\n\n";
  fullPrompt += "ESTE ES EL MATERIAL Y LOS CAPÍTULOS DE MI VIDA:\n";
  fullPrompt += "========================================================\n\n";

  topics.forEach((t, i) => {
    fullPrompt += "CAPÍTULO " + (i+1) + ": " + t.title.toUpperCase() + "\n";
    fullPrompt += "• Pregunta guía: " + t.hint + "\n";
    if (t.notes) fullPrompt += "• Notas y recuerdos del autor: " + t.notes + "\n";
    if (t.audioData) fullPrompt += "• [Recuerdo grabado por el autor con su voz - Incluir en este capítulo]\n";
    fullPrompt += "\n";
  });

  fullPrompt += "========================================================\n";
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
  element.setAttribute('download', "Mi_Biografia_para_Gemini_" + new Date().toISOString().slice(0,10) + ".txt");
  document.body.appendChild(element);
  element.click();
  element.remove();
}

// Inicializar de inmediato y al cargar
init();
window.addEventListener("DOMContentLoaded", init);
</script>
</body>
</html>
"""

# ==============================================================================
# 2. GENERADOR DEL ÚNICO DOCUMENTO: MANUAL DE INSTRUCCIONES EN PDF
# ==============================================================================
def create_user_manual_pdf():
    filename = "Manual_de_Instrucciones.pdf"
    file_path = os.path.join(TARGET_DIR, filename)
    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    styles = getSampleStyleSheet()
    
    c_primary = colors.HexColor('#1E3A8A')
    c_body = colors.HexColor('#1E293B')
    c_accent = colors.HexColor('#B45309')
    
    style_main_title = ParagraphStyle(
        'MainTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=c_primary,
        spaceAfter=4
    )
    style_subtitle = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=c_accent,
        spaceAfter=12
    )
    style_h2 = ParagraphStyle(
        'H2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=c_primary,
        spaceBefore=14,
        spaceAfter=6
    )
    style_body = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14.5,
        textColor=c_body,
        spaceAfter=6
    )
    style_tip = ParagraphStyle(
        'Tip',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=13.5,
        textColor=colors.HexColor('#334155')
    )
    
    story = []
    
    # Portada / Encabezado
    story.append(Paragraph("📖 MANUAL DE INSTRUCCIONES: APLICACIÓN «MI BIOGRAFÍA»", style_main_title))
    story.append(Paragraph("Guía práctica de uso: Cómo grabar tus recuerdos en casa, ordenarlos y crear tu libro y podcast familiar", style_subtitle))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=10))
    
    # 1. Qué es la aplicación
    story.append(Paragraph("¿QUÉ ES ESTA APLICACIÓN?", style_h2))
    story.append(Paragraph(
        "Es una herramienta diseñada para que puedas <b>grabar los recuerdos de tu vida tranquilamente desde tu propio ordenador</b>, a tu propio ritmo y sin prisas. No necesitas saber informática avanzada ni escribir textos complicados: solo abres la aplicación en la pantalla, pulsas un botón y hablas.",
        style_body
    ))
    
    # 2. Cómo abrirla
    story.append(Paragraph("1. CÓMO ABRIR LA APLICACIÓN", style_h2))
    story.append(Paragraph(
        "• Haz <b>doble clic</b> sobre el archivo <b>Mi_Biografia.html</b>.<br/>"
        "• Se abrirá automáticamente en tu navegador habitual (Microsoft Edge o Google Chrome). No requiere instalar ningún programa.",
        style_body
    ))
    
    # 3. Los botones de la pantalla
    story.append(Paragraph("2. CÓMO FUNCIONAN LOS BOTONES DE LA PANTALLA", style_h2))
    story.append(Paragraph(
        "• <b>🎙️ GRABAR RECUERDO:</b> Pulsa este botón y habla con calma al micrófono del ordenador contando ese momento de tu vida. Cuando termines, pulsa <b>⏹️ DETENER Y GUARDAR</b>.<br/>"
        "• <b>🔊 Tu recuerdo grabado:</b> En cuanto grabas, aparece el reproductor para escucharlo y el botón <b>💾 Guardar archivo de audio</b> si quieres guardarte ese sonido suelto en tu disco duro.<br/>"
        "• <b>🔄 Volver a grabar:</b> Si no te gusta cómo ha quedado la grabación, pulsa este botón para repetirla.<br/>"
        "• <b>🗑️ Borrar grabación (dejar en blanco):</b> Borra el audio y las notas de esa tarjeta para empezar de cero, pero <b>mantiene el capítulo</b> en la lista.<br/>"
        "• <b>✖ Quitar tema:</b> Elimina la tarjeta por completo si no quieres incluir ese asunto en tu vida.<br/>"
        "• <b>⬆️ Subir / ⬇️ Bajar:</b> Mueve los capítulos hacia arriba o hacia abajo para ordenar tu historia como prefieras.<br/>"
        "• <b>➕ Añadir nuevo tema / capítulo:</b> Te permite crear temas libres que no estén en la lista inicial (tus 30 años de trabajo, un viaje especial, una afición, tus amigos de juventud...).",
        style_body
    ))
    
    # 4. Dos trucos para hablar con tranquilidad
    story.append(Paragraph("3. DOS TRUCOS PARA HABLAR CON TOTAL TRANQUILIDAD", style_h2))
    story.append(Paragraph(
        "• <b>Si te equivocas o dudas al hablar:</b> ¡No pares la grabación! Simplemente di de forma natural: <i>«Espera, me he equivocado: no fue en el año 65 sino en el 68»</i> o <i>«Perdón, no era Juan sino Pedro»</i>. La aplicación está programada para que la Inteligencia Artificial elimine el error automáticamente y deje el texto limpio y perfecto.<br/>"
        "• <b>Si recuerdas una anécdota fuera de orden:</b> Cuéntala en cuanto te acuerdes, aunque haya ocurrido antes o después. La aplicación se encarga de colocar cada suceso en su momento cronológico exacto.",
        style_body
    ))
    
    # Salto de página para lectura cómoda
    story.append(PageBreak())
    
    # 5. Guardar en Microsoft Word
    story.append(Paragraph("4. CÓMO GENERAR TU LIBRO Y GUARDARLO EN MICROSOFT WORD", style_h2))
    story.append(Paragraph(
        "Cuando lleves varios días grabando y sientas que ya tienes tus recuerdos listos:<br/>"
        "<b>1.</b> En la aplicación, pulsa el botón azul grande del final: <b>«✨ GENERAR MI BIOGRAFÍA»</b>.<br/>"
        "<b>2.</b> En la ventana que se abre, pulsa <b>«📋 Copiar todo»</b>.<br/>"
        "<b>3.</b> Abre <b>Google Gemini</b> en tu navegador (<i>gemini.google.com</i>), pulsa <b>Pegar (Ctrl + V)</b> y dale a la flecha de enviar. Gemini redactará tu biografía completa dividida en capítulos cálidos y emotivos.<br/>"
        "<b>4. ¿Quieres añadir algo que se te olvidó?</b> No hace falta volver a grabar: díselo directamente a Gemini en la conversación:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>«Oye, añade en el Capítulo 3 que en 1974 me compré mi primer Seat 600 blanco...»</i><br/>"
        "<b>5. Pasar a Microsoft Word:</b> Copia el texto final redactado por Gemini, abre <b>Microsoft Word</b> en tu ordenador y pulsa <b>Pegar (Ctrl + V)</b>.<br/>"
        "<b>6. Personalizar e imprimir:</b> En Word puedes poner el tamaño de letra que quieras, insertar fotos familiares antiguas escaneadas (<i>Insertar -> Imágenes</i>) y darle a <b>Archivo -> Guardar como</b> para guardarlo en tu PC, o <b>Archivo -> Imprimir</b> para tenerlo en papel encuadernado.",
        style_body
    ))
    
    # 6. El podcast familiar para WhatsApp
    story.append(Paragraph("5. CÓMO CREAR EL PODCAST FAMILIAR PARA WHATSAPP", style_h2))
    story.append(Paragraph(
        "Si quieres además un programa de audio para compartir con tus hijos y nietos:<br/>"
        "• Entra en <b>NotebookLM</b> (<i>notebooklm.google.com</i>) con tu cuenta de Google.<br/>"
        "• Pulsa en <i>«Nuevo Cuaderno»</i>, ponle de título <i>«Mi Biografía»</i> y en Fuentes elige <i>«Texto copiado»</i> para pegar el texto de tu biografía.<br/>"
        "• En la columna derecha pulsa en <b>«Conversación de Audio» (Audio Overview)</b>. Se generará un programa de radio donde dos presentadores conversan con enorme cariño y admiración sobre tu vida.<br/>"
        "• Descarga ese audio y envíalo al grupo de WhatsApp familiar.",
        style_body
    ))
    
    # 7. Modo Casa vs Modo Aula
    story.append(Paragraph("6. PRIVACIDAD: EN CASA VS EN EL AULA", style_h2))
    story.append(Paragraph(
        "• <b>EN TU CASA:</b> Trabajas con total tranquilidad. <b>NO</b> tienes que pulsar el botón rojo de borrar. Tu navegador guardará tus recuerdos de un día para otro para que continúes cuando quieras.<br/>"
        "• <b>EN EL AULA COMPARTIDA:</b> Si usas un ordenador de clase que luego van a usar otras personas, antes de marcharte pulsa el botón verde <b>«💾 Guardar copia en mi Pendrive / PC»</b> para llevarte tus archivos, y luego pulsa el botón rojo <b>«🧹 Borrar todo al salir (Modo Aula)»</b>. Así tus recuerdos íntimos no quedarán guardados en ese ordenador.",
        style_body
    ))
    
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=8))
    story.append(Paragraph("<b>💡 CONSEJO:</b> Grabar tu biografía no es una tarea para hacer en una sola tarde. Disfruta recordando despacio cada etapa, tus maestros, tu primer trabajo y las historias que hicieron única tu vida.", style_tip))
    
    doc.build(story)
    print(f"  ✅ Creado el Manual de Instrucciones: {filename}")
    return file_path

def build_all():
    print("🚀 Generando materiales limpios para '4. Mi_Biografia'...")
    
    # 1. Guardar la App HTML interactiva
    html_path = os.path.join(TARGET_DIR, "Mi_Biografia.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print("  ✅ Creada la aplicación interactiva Mi_Biografia.html")
            
    # 2. Generar el ÚNICO DOCUMENTO: Manual_de_Instrucciones.pdf
    create_user_manual_pdf()
    
    print("🎉 ¡Clase 4. Mi_Biografia: Aplicación + Manual de Instrucciones completados con éxito!")

if __name__ == "__main__":
    build_all()
