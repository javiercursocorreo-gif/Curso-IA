# -*- coding: utf-8 -*-
"""
Clase Monográfica 4: "4. Mi_Biografia"
Genera:
1. Mi_Biografia.html -> Aplicación web con transcripción por voz en tiempo real,
   sin cajas de texto confusas, sin descargas de .txt inútiles,
   y con reglas anti-invención y anti-cursilería estrictas para Gemini.
2. Manual_de_Instrucciones.pdf -> Manual de usuario sencillo de entender.
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
    .container { max-width: 920px; margin: 0 auto; }

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
    .chapter-card { background: var(--card-bg); border: 2px solid var(--border); border-radius: 14px; padding: 22px; transition: border-color 0.2s; }
    .chapter-card.recorded { border-color: var(--success); background: #F0FDF4; }
    .card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; gap: 10px; flex-wrap: wrap; }
    .card-title { font-size: 1.35rem; font-weight: 700; color: var(--primary); display: flex; align-items: center; gap: 10px; }
    .status-badge { font-size: 0.85rem; font-weight: 700; padding: 4px 10px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.5px; }
    .badge-pending { background: #E2E8F0; color: #475569; }
    .badge-recorded { background: #DCFCE7; color: #166534; }
    .prompt-hint { font-size: 1.05rem; color: var(--text-muted); font-style: italic; margin-bottom: 14px; background: #F8FAFC; padding: 10px 14px; border-left: 4px solid var(--primary); border-radius: 0 8px 8px 0; }

    /* Notas y Transcripción */
    .notes-input { width: 100%; min-height: 75px; font-size: 1.02rem; padding: 12px; border: 1px solid var(--border); border-radius: 8px; margin-bottom: 14px; resize: vertical; line-height: 1.5; background: white; }
    .speech-status { font-size: 0.88rem; color: #0284C7; margin-bottom: 8px; font-weight: 600; display: none; }

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
    .modal-box { background: white; border-radius: 16px; max-width: 600px; width: 100%; max-height: 90vh; overflow-y: auto; padding: 32px 28px; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.2); text-align: center; }
    .modal-actions { display: flex; justify-content: center; gap: 12px; margin-top: 20px; flex-wrap: wrap; }
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
    💡 <b>Tres cosas muy importantes para tu total tranquilidad:</b><br>
    • <b>1. Habla al micrófono:</b> Al pulsar grabar y hablar, tus palabras se transcriben en la pantalla para que veas que el ordenador te escucha.<br>
    • <b>2. Si te equivocas o dudas al hablar:</b> ¡No pares la grabación! Di con naturalidad <i>«Espera, me he equivocado: no fue en el 65 sino en el 68»</i>. La Inteligencia Artificial corregirá el error automáticamente y dejará el texto limpio.<br>
    • <b>3. Si no quieres hablar de algún tema:</b> Déjalo simplemente en blanco. La aplicación lo omitirá y no aparecerá en tu biografía.
  </div>

  <div id="chaptersContainer" class="chapters-list"></div>

  <div class="footer-actions">
    <button class="btn-generate" onclick="generateBiographyModal()">✨ GENERAR MI BIOGRAFÍA</button>
  </div>
</div>

<!-- Modal para Añadir Tema -->
<div id="addTopicModal" class="modal-overlay">
  <div class="modal-box" style="text-align: left;">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
      <h2 style="color:var(--primary);">➕ Añadir Nuevo Tema</h2>
      <button class="btn-outline" onclick="closeModal('addTopicModal')">✕</button>
    </div>
    <label style="font-weight: 700; display: block; margin-bottom: 6px;">Título del tema:</label>
    <input type="text" id="newTopicTitle" placeholder="Ej: Mis 35 años de trabajo en la fábrica" style="width:100%; padding:10px; font-size:1.05rem; border:1px solid var(--border); border-radius:8px; margin-bottom:14px;">
    <label style="font-weight: 700; display: block; margin-bottom: 6px;">Pregunta o recuerdo que te inspire:</label>
    <input type="text" id="newTopicHint" placeholder="Ej: ¿Qué aprendí en mi empleo, qué compañeros recuerdo y cómo cambió el oficio?" style="width:100%; padding:10px; font-size:1.05rem; border:1px solid var(--border); border-radius:8px; margin-bottom:18px;">
    <div style="display:flex; justify-content:flex-end; gap:10px;">
      <button class="btn-outline" onclick="closeModal('addTopicModal')">Cancelar</button>
      <button class="btn-primary" onclick="addNewTopic()">Guardar Tema</button>
    </div>
  </div>
</div>

<!-- Modal de Generar Biografía (Limpio y directo para el alumno) -->
<div id="generateModal" class="modal-overlay">
  <div class="modal-box">
    <div style="font-size: 3.2rem; margin-bottom: 12px;">✅</div>
    <h2 style="font-size: 1.6rem; color: var(--primary); margin-bottom: 10px;">¡Tus recuerdos ya están copiados!</h2>
    <p style="font-size: 1.1rem; color: var(--text-muted); margin-bottom: 24px; line-height: 1.5;">
      Hemos empaquetado tus vivencias para que Gemini las redacte con fidelidad total a lo que has contado.
    </p>

    <div style="display: flex; flex-direction: column; gap: 12px; max-width: 380px; margin: 0 auto 24px;">
      <button class="btn-primary" style="justify-content: center; font-size: 1.15rem; padding: 15px;" onclick="openGeminiTab()">
        🚀 Ir a Google Gemini
      </button>
      <button class="btn-outline" style="justify-content: center; font-size: 0.95rem;" onclick="copyAgain()">
        📋 Volver a copiar
      </button>
    </div>

    <div style="background: #F1F5F9; border-radius: 10px; padding: 14px 18px; font-size: 0.95rem; color: var(--text-main); text-align: left; line-height: 1.5;">
      <b>📌 Qué hacer ahora:</b><br>
      <b>1.</b> Pulsa el botón azul <b>«Ir a Google Gemini»</b>.<br>
      <b>2.</b> En Gemini, haz clic en la casilla de escribir y pulsa <b>Pegar (Ctrl + V)</b> y dale a Enviar.<br>
      <b>3.</b> Gemini redactará tu biografía fiel a tus hechos.<br>
      <b>4.</b> Copia el texto final de Gemini, abre <b>Microsoft Word</b> en tu PC y pulsa <b>Pegar</b> para guardarlo e imprimirlo.
    </div>

    <div style="margin-top: 20px;">
      <button class="btn-outline btn-sm" onclick="closeModal('generateModal')">Cerrar esta ventana</button>
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
let recognition = null;
let lastFullPrompt = "";

// Reconocimiento de voz nativo en navegador
function initSpeechRecognition() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (SpeechRecognition) {
    try {
      recognition = new SpeechRecognition();
      recognition.continuous = true;
      recognition.interimResults = true;
      recognition.lang = 'es-ES';
    } catch(e) {
      console.warn("SpeechRecognition no disponible:", e);
    }
  }
}

// Cargar estado inicial
function init() {
  initSpeechRecognition();
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
  
  topics.forEach((t) => {
    const card = document.createElement("div");
    card.className = "chapter-card" + ((t.audioData || (t.notes && t.notes.trim())) ? " recorded" : "");
    card.id = "card-" + t.id;
    
    const isDone = (t.audioData || (t.notes && t.notes.trim().length > 0));
    const statusHtml = isDone 
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
      + statusHtml
      + '</div>'
      + '<div class="prompt-hint">' + t.hint + '</div>'
      + '<div id="speech-status-' + t.id + '" class="speech-status">🎙️ Escuchando tu voz y escribiendo...</div>'
      + '<textarea id="notes-' + t.id + '" class="notes-input" placeholder="Habla al micrófono y tus palabras aparecerán aquí automáticamente (también puedes escribir o retocar a mano)..." onchange="updateNotes(' + t.id + ', this.value)">' + (t.notes || "") + '</textarea>'
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
    
    // Iniciar transcripción automática de voz a texto
    const txtArea = document.getElementById('notes-' + id);
    const speechStatus = document.getElementById('speech-status-' + id);
    if (speechStatus) speechStatus.style.display = 'block';
    
    const topic = topics.find(x => x.id === id);
    let originalNotes = (topic && topic.notes) ? topic.notes.trim() : "";
    let transcriptAccumulator = "";

    if (recognition) {
      recognition.onresult = (event) => {
        let interim = '';
        let final = '';
        for (let i = event.resultIndex; i < event.results.length; ++i) {
          if (event.results[i].isFinal) {
            final += event.results[i][0].transcript + ' ';
          } else {
            interim += event.results[i][0].transcript;
          }
        }
        transcriptAccumulator += final;
        const fullText = (originalNotes ? originalNotes + "\n" : "") + transcriptAccumulator + interim;
        if (txtArea) txtArea.value = fullText.trim();
        if (topic) {
          topic.notes = ((originalNotes ? originalNotes + "\n" : "") + transcriptAccumulator).trim();
          saveState();
        }
      };
      recognition.onerror = (e) => { console.warn("Error speech recognition:", e); };
      try { recognition.start(); } catch(e) {}
    }

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
  if (recognition) {
    try { recognition.stop(); } catch(e) {}
  }
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

// Borrar únicamente el contenido grabado y notas (dejar el capítulo en blanco)
function clearTopicContentOnly(id) {
  const t = topics.find(x => x.id === id);
  if (!t) return;
  if (confirm("¿Deseas borrar la grabación y notas de este tema?\n\nQuedará en blanco y no se incluirá en tu biografía a menos que vuelvas a grabarlo.")) {
    t.audioData = null;
    t.notes = "";
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

// Generación de Biografía con Reglas Estrictas Anti-Ficción y Anti-Cursilería
function generateBiographyModal() {
  let count = 0;
  let memoriesText = "";

  topics.forEach((t) => {
    const hasNotes = t.notes && t.notes.trim().length > 0;
    if (hasNotes) {
      count++;
      memoriesText += "CAPÍTULO: " + t.title.toUpperCase() + "\n";
      memoriesText += "RELATO Y DATOS REALES APORTADOS POR EL AUTOR:\n";
      memoriesText += t.notes.trim() + "\n\n";
    }
  });

  if (count === 0) {
    alert("Todavía no has grabado ningún recuerdo ni añadido palabras en los temas. Pulsa el botón rojo 'GRABAR RECUERDO' y habla al micrófono antes de generar tu biografía.");
    return;
  }

  let fullPrompt = "Actúa como un biógrafo y redactor profesional, sobrio, respetuoso y profundamente humano. Tu tarea es redactar el libro biográfico real del autor basándote ÚNICA Y EXCLUSIVAMENTE en las memorias y datos que te aporta a continuación.\n\n";
  fullPrompt += "🛑 REGLAS ESTRICTAS DE REDACCIÓN (OBLIGATORIAS):\n";
  fullPrompt += "1. PROHIBIDO TOTALMENTE INVENTAR: No inventes nombres de personas, calles, pueblos, trabajos, anécdotas ni sucesos que el autor no haya contado. Cíñete fielmente a sus palabras y vivencias reales.\n";
  fullPrompt += "2. PROHIBIDO EL TONO CURSI O MELODRAMÁTICO: Prohibido usar clichés vacíos como 'si cierras los ojos', 'en el ocaso de la vida', 'ecos del ayer' o poesías artificiales. Escribe con un lenguaje natural, directo, digno y auténtico, como una persona real contando su historia verdadera a sus hijos y nietos.\n";
  fullPrompt += "3. AUTO-CORRECCIÓN AL HABLAR: Si en el relato el autor duda o dice 'espera, me he equivocado', 'perdón, fue en...', interpreta la rectificación y deja únicamente el dato final correcto.\n";
  fullPrompt += "4. HILO CRONOLÓGICO NATURAL: Organiza los recuerdos aportados en una narración fluida y coherente, respetando la cronología vital del autor.\n";
  fullPrompt += "5. FORMATO: Devuelve el texto estructurado por capítulos con títulos claros, listo para copiar a Microsoft Word.\n\n";
  fullPrompt += "ESTAS SON LAS MEMORIAS REALES QUE TE ENTREGA EL AUTOR:\n";
  fullPrompt += "========================================================\n\n";
  fullPrompt += memoriesText;
  fullPrompt += "========================================================\n";
  fullPrompt += "Redacta ahora la biografía completa del autor siguiendo estrictamente todas las reglas anteriores.";

  lastFullPrompt = fullPrompt;

  // Copiado automático al portapapeles
  navigator.clipboard.writeText(fullPrompt).then(() => {
    document.getElementById("generateModal").classList.add("active");
  }).catch(() => {
    // Si el portapapeles falla por permisos, abrir modal igualmente
    document.getElementById("generateModal").classList.add("active");
  });
}

function openGeminiTab() {
  window.open("https://gemini.google.com", "_blank");
}

function copyAgain() {
  if (lastFullPrompt) {
    navigator.clipboard.writeText(lastFullPrompt).then(() => {
      alert("📋 ¡Copiado de nuevo! Ahora ve a Gemini y pulsa Pegar (Ctrl + V).");
    });
  }
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
    story.append(Paragraph("Guía práctica de uso: Graba tus recuerdos en tu ordenador a tu ritmo y crea tu libro y podcast familiar", style_subtitle))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceAfter=10))
    
    # 1. Qué es la aplicación
    story.append(Paragraph("¿QUÉ ES ESTA APLICACIÓN?", style_h2))
    story.append(Paragraph(
        "Es una herramienta diseñada para que puedas <b>grabar los recuerdos de tu vida tranquilamente desde tu propio ordenador</b>, a tu propio ritmo y sin prisas. No necesitas saber informática avanzada: solo abres la aplicación en la pantalla, pulsas un botón y hablas. La Inteligencia Artificial se encarga de ordenar y redactar todo por ti sin inventar nada.",
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
        "• <b>🎙️ GRABAR RECUERDO:</b> Pulsa este botón y habla con calma al micrófono del ordenador contando ese momento de tu vida. Tus palabras se escribirán en la pantalla mientras hablas. Cuando termines, pulsa <b>⏹️ DETENER Y GUARDAR</b>.<br/>"
        "• <b>🔊 Tu recuerdo grabado:</b> En cuanto grabas, aparece el reproductor para escucharlo y el botón <b>💾 Guardar archivo de audio</b> si quieres guardarte ese sonido suelto en tu disco duro.<br/>"
        "• <b>🔄 Volver a grabar:</b> Si no te gusta cómo ha quedado la grabación, pulsa este botón para repetirla.<br/>"
        "• <b>🗑️ Borrar grabación (dejar en blanco):</b> Borra el audio y las notas de esa tarjeta para empezar de cero.<br/>"
        "• <b>➕ Añadir nuevo tema / capítulo:</b> Te permite añadir temas libres que no estén en la lista inicial (tus 30 años de trabajo, un viaje especial, una afición, tus amigos de juventud...).",
        style_body
    ))
    
    # 4. Los secretos para hablar con tranquilidad
    story.append(Paragraph("3. TRES SECRETOS PARA HABLAR CON TOTAL TRANQUILIDAD", style_h2))
    story.append(Paragraph(
        "• <b>1. Si te equivocas o dudas al hablar:</b> ¡No pares la grabación! Simplemente di de forma natural: <i>«Espera, me he equivocado: no fue en el año 65 sino en el 68»</i> o <i>«Perdón, no era Juan sino Pedro»</i>. La aplicación se encarga de que la Inteligencia Artificial elimine el error automáticamente y deje el texto limpio.<br/>"
        "• <b>2. Si no quieres hablar de algún tema:</b> Déjalo simplemente en blanco. No te preocupes por borrarlo; la aplicación lo ignorará y no aparecerá en tu libro biográfico.<br/>"
        "• <b>3. Orden de tu historia:</b> Habla con total libertad en cualquier orden. La Inteligencia Artificial se encargará de ordenar y mezclar todos tus recuerdos en una narración cronológica fluida y natural, sin inventar nada que tú no hayas contado.",
        style_body
    ))
    
    # Salto de página para lectura cómoda
    story.append(PageBreak())
    
    # 5. Guardar en Microsoft Word
    story.append(Paragraph("4. CÓMO GENERAR TU LIBRO Y GUARDARLO EN MICROSOFT WORD", style_h2))
    story.append(Paragraph(
        "Cuando lleves varios días grabando y sientas que ya tienes tus recuerdos listos:<br/>"
        "<b>1.</b> En la aplicación, pulsa el botón azul grande del final: <b>«✨ GENERAR MI BIOGRAFÍA»</b>. Se copiarán automáticamente tus recuerdos.<br/>"
        "<b>2.</b> En la ventana que aparece, pulsa el botón azul <b>«🚀 Ir a Google Gemini»</b>.<br/>"
        "<b>3.</b> En Gemini, haz clic en la casilla de escribir abajo, pulsa <b>Pegar (Ctrl + V)</b> y dale a la flecha de enviar. Gemini redactará tu biografía completa respetando con total fidelidad los datos reales que has contado.<br/>"
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
