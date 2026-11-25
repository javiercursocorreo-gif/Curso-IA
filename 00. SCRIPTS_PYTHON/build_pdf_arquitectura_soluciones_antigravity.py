#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_arquitectura_soluciones_antigravity.py
Genera la Guía Maestra Técnica y Didáctica Definitiva (Fuente Única de la Verdad):
'GUÍA DE ARQUITECTURA, INSTALACIÓN Y GOBERNANZA EN GOOGLE ANTIGRAVITY'
(Estructurada en 6 Fases desde CERO:
 Fase 0: Descarga e Instalación en Windows y Mac (Por qué elegir el IDE)
 Fase 1: Fundamentos y Arquitectura Monorepo
 Fase 2: Configuración del Motor (Settings)
 Fase 3: Protocolos de Comportamiento (AGENTS.md)
 Fase 4: Capacidades Avanzadas (Subagentes y UI)
 Fase 5: Puesta en Marcha con Doble Bloque: Maestro del Profesor y Kit Alumnos)

Destinos sincronizados:
1. 00. ARQUITECTURA SISTEMA CON IA/
2. CURSO-IA/CLASES/7. MAPA_GESTION_PROYECTO_CON_IA/
"""

import os
import sys
import subprocess
import shutil
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

ROOT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA"
NOBLE_DIR = os.path.join(ROOT_DIR, "00. ARQUITECTURA SISTEMA CON IA")
MONO_DIR = os.path.join(ROOT_DIR, "CURSO-IA/CLASES/7. MAPA_GESTION_PROYECTO_CON_IA")

os.makedirs(NOBLE_DIR, exist_ok=True)
os.makedirs(MONO_DIR, exist_ok=True)

PDF_NOBLE = os.path.join(NOBLE_DIR, "ARQUITECTURA_Y_SOLUCIONES_ANTIGRAVITY.pdf")
HTML_NOBLE = os.path.join(NOBLE_DIR, "ARQUITECTURA_Y_SOLUCIONES_ANTIGRAVITY.html")
DOCX_NOBLE = os.path.join(NOBLE_DIR, "ARQUITECTURA_Y_SOLUCIONES_ANTIGRAVITY.docx")

PDF_MONO = os.path.join(MONO_DIR, "ARQUITECTURA_Y_SOLUCIONES_ANTIGRAVITY.pdf")
HTML_MONO = os.path.join(MONO_DIR, "ARQUITECTURA_Y_SOLUCIONES_ANTIGRAVITY.html")
DOCX_MONO = os.path.join(MONO_DIR, "ARQUITECTURA_Y_SOLUCIONES_ANTIGRAVITY.docx")
BKP_PDF_MONO = os.path.join(MONO_DIR, "LAS_4D_DEL_CODIGO_IA_Y_NUESTRAS_SOLUCIONES.pdf")
BKP_HTML_MONO = os.path.join(MONO_DIR, "LAS_4D_DEL_CODIGO_IA_Y_NUESTRAS_SOLUCIONES.html")

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(36, 32, A4[0] - 36, 32)
        left_text = "Ecosistema Tecnológico • Arquitectura y Gobernanza en Google Antigravity"
        page_text = f"Página {self._pageNumber} de {page_count}"
        self.drawString(36, 22, left_text)
        self.drawRightString(A4[0] - 36, 22, page_text)
        self.restoreState()

def compilar_html():
    html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Guía de Arquitectura, Instalación y Gobernanza en Google Antigravity</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; line-height: 1.6; color: #1e293b; max-width: 980px; margin: 40px auto; padding: 0 24px; }
        h1 { color: #0f172a; border-bottom: 2px solid #0284c7; padding-bottom: 12px; font-size: 2.1rem; }
        h2 { color: #0369a1; margin-top: 36px; border-left: 4px solid #0284c7; padding-left: 12px; font-size: 1.35rem; }
        h3 { color: #0f172a; margin-top: 20px; font-size: 1.12rem; }
        .phase-header { background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #fff; padding: 12px 18px; border-radius: 8px; margin-top: 40px; margin-bottom: 15px; font-size: 1.25rem; font-weight: 700; letter-spacing: 0.5px; }
        .danger-box { background: #fef2f2; border: 1px solid #f87171; border-radius: 8px; padding: 15px 18px; margin: 15px 0; }
        .solution-box { background: #f0fdf4; border: 1px solid #4ade80; border-radius: 8px; padding: 15px 18px; margin: 15px 0; }
        .feature-box { background: #f8fafc; border: 1px solid #38bdf8; border-radius: 8px; padding: 15px 18px; margin: 15px 0; }
        .box-profesor { background: #f0f9ff; border: 2px solid #0284c7; border-radius: 8px; padding: 18px 20px; margin: 20px 0; }
        .box-alumno { background: #f0fdf4; border: 2px solid #16a34a; border-radius: 8px; padding: 18px 20px; margin: 20px 0; }
        .quote-box { background: #f8fafc; border-left: 4px solid #64748b; padding: 14px 20px; font-style: italic; margin: 20px 0; font-size: 1.05rem; }
        .tree-box { background: #0f172a; color: #38bdf8; padding: 16px 20px; border-radius: 8px; font-family: ui-monospace, Menlo, Monaco, monospace; font-size: 0.86rem; line-height: 1.45; margin: 15px 0; overflow-x: auto; }
        .code-banner { background: #1e293b; color: #f8fafc; padding: 14px 18px; border-radius: 6px; font-family: ui-monospace, Menlo, Monaco, monospace; font-size: 0.84rem; line-height: 1.45; margin: 12px 0; border-left: 4px solid #38bdf8; overflow-x: auto; }
        table { width: 100%; border-collapse: collapse; margin: 25px 0; font-size: 0.92rem; }
        th, td { border: 1px solid #cbd5e1; padding: 10px 14px; text-align: left; }
        th { background: #f1f5f9; color: #0f172a; font-weight: bold; }
        code { background: #e2e8f0; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 0.9em; }
        .badge { display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; margin-bottom: 6px; }
        .badge-profesor { background: #0284c7; color: #fff; }
        .badge-alumno { background: #16a34a; color: #fff; }
        .badge-danger { background: #fee2e2; color: #b91c1c; }
        .badge-solution { background: #dcfce7; color: #15803d; }
    </style>
</head>
<body>
    <h1>Guía de Arquitectura, Instalación y Gobernanza en Google Antigravity</h1>
    <p><strong>Manual Maestro y Fuente Única de la Verdad (Ecosistema Completo y Kit de Inicio para Alumnos)</strong><br>
    <em>Desde la descarga de la herramienta y configuración del motor hasta la gobernanza agéntica profesional y el trabajo desatendido en silencio.</em></p>

    <div class="quote-box">
        «El verdadero peligro no es que la inteligencia artificial escriba código, sino que el humano pierda el gobierno sobre la arquitectura. El código se delega; el rigor, la jerarquía de ficheros, la memoria y la verificación jamás.»<br>
        <strong>— Marco de Gobernanza Agéntica en Google Antigravity</strong>
    </div>

    <!-- FASE 0 -->
    <div class="phase-header">FASE 0: DESCARGA E INSTALACIÓN (PARTIR DE CERO EN WINDOWS Y MAC)</div>

    <h2>0.1 ¿Qué Versión Descargar? La Diferencia Crítica: Desktop vs. IDE</h2>
    <p>Al acceder a la web oficial de descarga de Google Antigravity, la plataforma presenta distintas opciones:</p>
    <ul>
        <li><strong>Antigravity Desktop (App de Escritorio):</strong> Es una aplicación visual muy básica, orientada casi exclusivamente a chatear. <em>Inconveniente:</em> Oculta el árbol de carpetas, no muestra las diferencias exactas de código (diffs rojos/verdes) y no tiene consola de ejecución integrada, quedándose corta de inmediato.</li>
        <li><strong>Antigravity IDE (Entorno Integrado basado en VS Code - NUESTRA ELECCIÓN OFICIAL):</strong> Es la herramienta profesional definitiva. En una única pantalla integra el explorador de archivos a la izquierda, el editor de código central, la terminal de comandos abajo y el copiloto de IA a la derecha.</li>
    </ul>

    <div class="solution-box">
        <strong>💡 Recomendación Oficial del Curso:</strong> Instala siempre <strong>Antigravity IDE</strong>. Aunque seas principiante, verás en tiempo real cómo la IA crea tus carpetas y archivos en el disco, teniendo el 100% del control visual de lo que ocurre en tu ordenador.
    </div>

    <h2>0.2 Proceso de Instalación Paso a Paso</h2>
    <table>
        <thead>
            <tr>
                <th>Sistema Operativo</th>
                <th>Enlace / Instalador</th>
                <th>Pasos de Instalación</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Windows 10 / 11</strong></td>
                <td>Descargar el instalador <code>.exe</code> (versión Windows x64)</td>
                <td>1. Ejecuta el archivo descargado.<br>2. Sigue el asistente ("Siguiente", "Instalar").<br>3. Al terminar, abre <strong>Google Antigravity</strong> e inicia sesión con tu cuenta de Google.</td>
            </tr>
            <tr>
                <td><strong>macOS (Apple Silicon / Intel)</strong></td>
                <td>Descargar el instalador <code>.dmg</code> (versión Mac Universal o Apple Silicon)</td>
                <td>1. Abre el archivo <code>.dmg</code>.<br>2. Arrastra el icono de Antigravity a la carpeta <strong>Aplicaciones</strong>.<br>3. Abre la app desde Spotlight o Launchpad e inicia sesión con tu cuenta de Google.</td>
            </tr>
        </tbody>
    </table>

    <!-- FASE 1 -->
    <div class="phase-header">FASE 1: FUNDAMENTOS Y ARQUITECTURA DEL ESPACIO DE TRABAJO</div>

    <h2>1.1 De la Ilusión del 'Vibe Coding' a la Gobernanza Real (Las 4 D)</h2>
    <p>Generar código mediante lenguaje natural sin arquitectura acumula silenciosamente cuatro patologías críticas conocidas como <strong>Las 4 D del peligro de la IA</strong>:</p>

    <div class="danger-box">
        <span class="badge badge-danger">1. Duplicación</span>: Reinvención constante de funciones y utilidades en archivos dispersos.<br>
        <span class="badge badge-solution">Solución</span>: <code>ESTADO_GLOBAL_PROYECTOS.md</code> como inventario técnico centralizado previo obligatorio.
    </div>

    <div class="danger-box">
        <span class="badge badge-danger">2. Drift (Deriva)</span>: Ceguera de contexto en sesiones largas, pérdida de arquitectura y abreviaturas inventadas.<br>
        <span class="badge badge-solution">Solución</span>: Arquitectura <em>Elephant-Goldfish</em>, catálogos canónicos exactos (NASA Eyes) y doble contador correlativo.
    </div>

    <div class="danger-box">
        <span class="badge badge-danger">3. Deluge (Diluvio)</span>: Inflación de dependencias externas superfluas (npm, frameworks pesados) para tareas simples.<br>
        <span class="badge badge-solution">Solución</span>: Regla de cero herramientas nuevas, uso de herramientas nativas del sistema operativo y micro-apps atómicas.
    </div>

    <div class="danger-box">
        <span class="badge badge-danger">4. Deception (Engaño)</span>: Código que compila pero oculta datos falsos, APIs bloqueadas o activos inertes.<br>
        <span class="badge badge-solution">Solución</span>: Autocomprobación previa obligatoria, marcas temporales UTC en sondas históricas y copias BKP garantizadas.
    </div>

    <h2>1.2 Arquitectura Monorepo de Raíz Única: Cero Barreras de Permisos</h2>
    <p>Para erradicar de raíz las alertas y bloqueos por cruce de carpetas (<em>Non-Workspace File Access</em>), la arquitectura agéntica exige situar la raíz de Antigravity en una <strong>única carpeta superior</strong>. Todo lo que cuelga de esa raíz se encuentra dentro del mismo espacio de trabajo seguro.</p>

    <!-- FASE 2 -->
    <div class="phase-header">FASE 2: CONFIGURACIÓN BASE DEL MOTOR (SETTINGS DE ANTIGRAVITY)</div>

    <h2>2.1 Checklist Exhaustiva de Parámetros Calibrados</h2>
    <table>
        <thead>
            <tr>
                <th>Parámetro</th>
                <th>Valor Recomendado</th>
                <th>Justificación Técnica y Operativa</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Interface Layout</strong></td>
                <td><code>Software Engineering</code></td>
                <td>Habilita terminales, consola git, explorador completo y visores de diffs necesarios para desarrollo real.</td>
            </tr>
            <tr>
                <td><strong>Tool Execution Policy</strong></td>
                <td><code>proceed-in-sandbox</code></td>
                <td>Autonomía desatendida total mientras se opere dentro del Sandbox seguro del proyecto. Frena llamadas invasivas.</td>
            </tr>
            <tr>
                <td><strong>Terminal Sandbox</strong></td>
                <td><code>Enabled (true)</code></td>
                <td>Contención estricta: lectura/escritura en la raíz y /tmp; cero riesgo de alterar binarios del sistema anfitrión.</td>
            </tr>
            <tr>
                <td><strong>Application: Prevent Sleep</strong></td>
                <td><code>Enabled (true)</code></td>
                <td>Evita la suspensión del equipo durante tareas largas en lote (compilaciones masivas y exportaciones).</td>
            </tr>
            <tr>
                <td><strong>Message Execution</strong></td>
                <td><code>Queue Message</code></td>
                <td>Encola las nuevas instrucciones durante un turno, garantizando ejecuciones atómicas sin cortes a mitad.</td>
            </tr>
            <tr>
                <td><strong>Model Selection</strong></td>
                <td><code>Pro / Flash</code></td>
                <td>Gemini Pro para el Elefante (coordinador arquitectónico); Gemini Flash para subagentes rápidos de auditoría.</td>
            </tr>
        </tbody>
    </table>

    <h2>2.2 Primacía de AGENTS.md</h2>
    <p>En Antigravity, los archivos <code>AGENTS.md</code> y <code>GEMINI.md</code> situados en la raíz del workspace tienen <strong>precedencia jerárquica absoluta</strong> sobre cualquier menú visual de la aplicación, blindando las normas de trabajo.</p>

    <!-- FASE 3 -->
    <div class="phase-header">FASE 3: EL NÚCLEO DE PROTOCOLOS DE COMPORTAMIENTO (AGENTS.MD)</div>

    <h2>3.1 Protocolo de Oro: Cero-Submits Absoluto</h2>
    <p>Prohibición total de ventanas emergentes de confirmación interactiva en el editor (<code>RequestFeedback: false</code>). La IA trabaja desatendida de principio a fin.</p>

    <h2>3.2 El Patrón Operativo Maestro: Trabajo en Silencio y Comando Terminal Final</h2>
    <div class="feature-box">
        <strong>Mecánica en Dos Fases:</strong>
        <ul>
            <li><strong>Fase 1 (Silencio en Sandbox):</strong> El agente utiliza sus herramientas internas (<code>read_file</code>, <code>edit_file</code>, <code>write_file</code>) para editar, auditar y compilar archivos sin emitir charlas ni popups durante el turno.</li>
            <li><strong>Fase 2 (Comando Único al Final):</strong> Al concluir con éxito, entrega un único bloque bash numerado (ej. <code>[COMANDO XX]</code>) con cabecera y pie visibles por <code>echo</code> para ejecución externa soberana del usuario.</li>
        </ul>
        <p><strong>Beneficio:</strong> Máxima paz mental, cero fricción cognitiva, trazabilidad cronológica en la shell y soberanía humana sobre la ejecución final.</p>
    </div>

    <h2>3.3 Elephant-Goldfish, Doble Contador y Salvaguarda Senior (+65)</h2>
    <p>• <strong>Elephant-Goldfish:</strong> Coordinador con memoria vs. subagentes efímeros limpios con autodestrucción inmediata.<br>
    • <strong>Doble Contador Correlativo:</strong> Control cronológico estricto entre clases y proyectos especializados.<br>
    • <strong>La Triple Salvaguarda Pedagógica (+65):</strong> Cero código intermedio para alumnos senior; aplicaciones en modo Canvas/Vista Previa directa con copia de respaldo oficial BKP en mapas.</p>

    <!-- FASE 4 -->
    <div class="phase-header">FASE 4: CAPACIDADES AVANZADAS DE ÚLTIMA GENERACIÓN</div>

    <h2>4.1 Subagentes en Paralelo, Generative UI y Despliegue Continuo</h2>
    <p>• <strong>Subagentes en Paralelo (<code>invoke_subagent</code>):</strong> Concurrencia masiva para tareas pesadas y cierre inmediato (<code>kill</code>).<br>
    • <strong>Generative UI (<code>&lt;agent-embed&gt;</code>):</strong> Paneles y cuadros de mando interactivos embebidos con Tailwind CSS.<br>
    • <strong>Despliegue Continuo a GitHub:</strong> Cada cambio queda subido a <code>origin/main</code> para reflejarse en GitHub Pages y Classroom al instante.</p>

    <!-- FASE 5 -->
    <div class="phase-header">FASE 5: PUESTA EN MARCHA AUTOMATIZADA (DOBLE BLOQUE SEÑALIZADO)</div>

    <!-- BLOQUE PROFESOR -->
    <div class="box-profesor">
        <span class="badge badge-profesor">📘 PARTE MAESTRA: CASO REAL DE ESTUDIO (ECOSISTEMA DEL PROFESOR)</span>
        <h3>Estructura Real Completa en macOS iCloud Drive</h3>
        <p>Esta es la radiografía real de nuestro entorno de producción. Muestra cómo conviven los módulos de IA, Robótica, Música, Calendario y Salud bajo la misma raíz soberana:</p>

        <div class="tree-box">
📁 CLASES DE TECNOLOGÍA/ [RAÍZ ÚNICA DEL WORKSPACE EN ANTIGRAVITY]
├── 📄 AGENTS.md (Protocolo de Oro, Cero-Submits y Reglas Maestras)
├── 📄 GEMINI.md (Espejo Canónico y Directivas de Modelos)
├── 📄 ESTADO_GLOBAL_PROYECTOS.md (Inventario Técnico Centralizado)
│
├── 📁 00. ARQUITECTURA SISTEMA CON IA/ (Guía Maestra y Plantilla Universal ZIP)
├── 📁 CURSO-IA/ (Monográficos 1 a 6, Talleres y Scripts Python de Compilación)
├── 📁 CURSO-ROBOTICA-V2/ (Teoría a 14 slides, Babylon.js y Prácticas)
├── 📁 CURSO-ROBOTICA-IA-COMUN/ (Calendario y BITACORA_SEGUIMIENTO_CLASES.md)
├── 📁 CURSO_MUSICA/ (Web MIDI, Banco Maestro MSB 33 y Korg EK-50)
└── 📁 IA TEMAS VARIOS/ (Asistente Personal, Medicinas y Ejercicios)
        </div>

        <h3>Supercomando Maestro de Restauración Personal (macOS)</h3>
        <p>Comando que utiliza el profesor para clonar o restaurar el ecosistema completo en cualquier Mac nuevo en 20 segundos:</p>

        <div class="code-banner">
echo "=== [SUPERCOMANDO MAESTRO: ECOSISTEMA COMPLETO] ==="
ROOT_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA"
mkdir -p "$ROOT_DIR/00. ARQUITECTURA SISTEMA CON IA"
mkdir -p "$ROOT_DIR/CURSO-IA/CLASES" "$ROOT_DIR/CURSO-ROBOTICA-V2" "$ROOT_DIR/CURSO_MUSICA"
mkdir -p "$ROOT_DIR/.agents"
cat << 'EOF' > "$ROOT_DIR/.agents/settings.json"
{"layout":"softwareEngineering","toolExecutionPolicy":"proceed-in-sandbox","terminalSandbox":true,"preventSleep":true,"messageExecution":"queue"}
EOF
echo "=== [FIN SUPERCOMANDO MAESTRO] (EXITOSO) ==="
        </div>
    </div>

    <!-- BLOQUE ALUMNO -->
    <div class="box-alumno">
        <span class="badge badge-alumno">🟢 PARTE DEL ALUMNO: GUÍA PASO A PASO PARA MONTARLO EN TU PC</span>
        <h3>Paso 1: ¿Dónde Copiar y Descomprimir este Archivo ZIP? (Windows o Mac)</h3>
        <p>Para no dejar archivos perdidos en la carpeta de Descargas, sigue este orden exacto:</p>
        <ul>
            <li><strong>Si usas Windows:</strong><br>
                1. Ve al explorador y <strong>copia</strong> el archivo <code>WORKSPACE-ANTIGRAVITY-PLANTILLA.zip</code> en tu carpeta <strong>Documentos</strong> (o en <code>C:\</code>).<br>
                2. Haz clic derecho sobre el ZIP allí mismo y pulsa <strong>"Extraer todo..."</strong>.<br>
                3. Al descomprimirlo en ese destino, te quedará tu carpeta lista: <code>Documentos\WORKSPACE-ANTIGRAVITY\</code>.
            </li>
            <li><strong>Si usas Mac:</strong><br>
                1. Abre el Finder y <strong>copia</strong> el archivo <code>WORKSPACE-ANTIGRAVITY-PLANTILLA.zip</code> en tu carpeta <strong>Documentos</strong> (o en tu carpeta de usuario).<br>
                2. Haz doble clic sobre el ZIP allí mismo para descomprimirlo.<br>
                3. Te quedará tu carpeta lista: <code>Documentos/WORKSPACE-ANTIGRAVITY/</code>.
            </li>
        </ul>

        <h3>Paso 2: Abrir la Carpeta en Antigravity IDE</h3>
        <ol>
            <li>Abre <strong>Google Antigravity IDE</strong>.</li>
            <li>En el menú superior pulsa en <strong>File > Open Folder...</strong> (Abrir Carpeta...).</li>
            <li>Selecciona la carpeta que acabas de descomprimir en el Paso 1.</li>
            <li>¡Listo! Tu Antigravity ya tiene las reglas de Cero-Submits y la configuración técnica profesional preactivada.</li>
        </ol>

        <h3>Paso 3: Cómo Usar tu Terminal sin Miedo (El Trabajo en Silencio)</h3>
        <ol>
            <li><strong>Abre tu consola:</strong><br>
                • En Windows: Pulsa la tecla <code>Windows</code>, escribe <strong><code>cmd</code></strong> (o Terminal) y pulsa <code>Enter</code>.<br>
                • En Mac: Pulsa <code>Cmd + Espacio</code>, escribe <strong><code>Terminal</code></strong> y pulsa <code>Enter</code>.
            </li>
            <li><strong>Pídele cosas a la IA en Antigravity:</strong> Trabajarás en el chat normalmente. La IA procesará en silencio sin abrirte popups molestos.</li>
            <li><strong>Ejecuta el Comando Final:</strong> Al terminar, la IA te entregará un bloque de código que empieza por <code>echo</code>. Lo copias, lo pegas en tu ventana negra de la terminal y pulsas <code>Enter</code>. ¡Verás cómo se aplica todo en tu PC con control total!</li>
        </ol>
    </div>

    <h2>5.3 Catálogo Evolutivo de Mejoras del Ecosistema</h2>
    <table>
        <thead>
            <tr>
                <th>Hito / Versión</th>
                <th>Ámbito</th>
                <th>Impacto y Beneficio Operativo</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Fase 0: Instalación desde Cero</strong></td>
                <td>Didáctica / Setup</td>
                <td>Guía de descarga para Windows/Mac explicando por qué elegir Antigravity IDE frente a Desktop.</td>
            </tr>
            <tr>
                <td><strong>Guía Única Señalizada</strong></td>
                <td>Gobernanza</td>
                <td>Fuente única de la verdad con Bloque Maestro (Profesor) y Bloque Alumno (Kit de Inicio).</td>
            </tr>
            <tr>
                <td><strong>Plantilla ZIP en 1 Clic</strong></td>
                <td>Despliegue</td>
                <td>Inicio rápido para Windows/Mac copiando a Documentos y descomprimiendo en destino.</td>
            </tr>
            <tr>
                <td><strong>Monorepo Raíz Única</strong></td>
                <td>Workspace</td>
                <td>Todas las áreas bajo una misma raíz para cero bloqueos de permisos.</td>
            </tr>
            <tr>
                <td><strong>Trabajo en Silencio</strong></td>
                <td>Metodología</td>
                <td>Ejecución silenciosa en sandbox y entrega de bloque bash único al final.</td>
            </tr>
            <tr>
                <td><strong>Cero-Submits</strong></td>
                <td>Flujo de Trabajo</td>
                <td>Eliminación total de ventanas emergentes de aprobación durante la sesión en el editor.</td>
            </tr>
            <tr>
                <td><strong>Elephant-Goldfish</strong></td>
                <td>Memoria</td>
                <td>Auditoría con mente virgen y destrucción inmediata sin fugas de memoria.</td>
            </tr>
            <tr>
                <td><strong>Subagentes Paralelos</strong></td>
                <td>Concurrencia</td>
                <td>Ejecución paralela para tareas pesadas sin saturar el hilo principal.</td>
            </tr>
            <tr>
                <td><strong>Generative UI Nativo</strong></td>
                <td>Visualización</td>
                <td>Widgets y cuadros de mando interactivos embebidos sin exponer código.</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""
    with open(HTML_NOBLE, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(HTML_MONO, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(BKP_HTML_MONO, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("✅ HTML generado con Fase 0 e IDE incorporados.", flush=True)

    try:
        subprocess.run(["textutil", "-convert", "docx", HTML_NOBLE, "-output", DOCX_NOBLE], check=True)
        shutil.copyfile(DOCX_NOBLE, DOCX_MONO)
        print("✅ DOCX generado y sincronizado.", flush=True)
    except Exception as e:
        print(f"⚠️ Aviso DOCX: {e}", flush=True)

def compilar_pdf_reportlab():
    doc = SimpleDocTemplate(
        PDF_NOBLE,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=42
    )

    PAGE_WIDTH = A4[0] - 72

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle('DocTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=14.5, leading=17.5, textColor=colors.HexColor('#0F172A'), spaceAfter=4)
    subtitle_style = ParagraphStyle('DocSubtitle', parent=styles['Normal'], fontName='Helvetica', fontSize=8.2, leading=11, textColor=colors.HexColor('#475569'), spaceAfter=7)
    phase_style = ParagraphStyle('PhaseStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, leading=11.5, textColor=colors.HexColor('#FFFFFF'), backColor=colors.HexColor('#0284C7'), borderPadding=4, spaceBefore=7, spaceAfter=4, keepWithNext=True)
    h1_style = ParagraphStyle('H1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11.5, textColor=colors.HexColor('#0369A1'), spaceBefore=5, spaceAfter=2.5, keepWithNext=True)
    body_style = ParagraphStyle('Body', parent=styles['Normal'], fontName='Helvetica', fontSize=7.4, leading=10.2, textColor=colors.HexColor('#1E293B'), spaceAfter=3.5)
    code_banner_style = ParagraphStyle('CodeBanner', parent=styles['Normal'], fontName='Courier', fontSize=6.2, leading=8.2, textColor=colors.HexColor('#F8FAFC'), backColor=colors.HexColor('#1E293B'), borderColor=colors.HexColor('#38BDF8'), borderWidth=1, borderPadding=3.5, spaceAfter=3.5)

    danger_title = ParagraphStyle('DT', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.6, leading=9.5, textColor=colors.HexColor('#B91C1C'), spaceAfter=1)
    danger_body = ParagraphStyle('DB', parent=styles['Normal'], fontName='Helvetica', fontSize=7, leading=9.2, textColor=colors.HexColor('#7F1D1D'))
    sol_title = ParagraphStyle('ST', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.6, leading=9.5, textColor=colors.HexColor('#15803D'), spaceAfter=1)
    sol_body = ParagraphStyle('SB', parent=styles['Normal'], fontName='Helvetica', fontSize=7, leading=9.2, textColor=colors.HexColor('#14532D'))
    feat_title = ParagraphStyle('FT', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.8, leading=10, textColor=colors.HexColor('#0369A1'), spaceAfter=1.5)
    feat_body = ParagraphStyle('FB', parent=styles['Normal'], fontName='Helvetica', fontSize=7, leading=9.4, textColor=colors.HexColor('#0F172A'))

    table_header = ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=6.8, leading=8.8, textColor=colors.HexColor('#0F172A'))
    table_cell = ParagraphStyle('TC', parent=styles['Normal'], fontName='Helvetica', fontSize=6.6, leading=8.5, textColor=colors.HexColor('#334155'))
    table_cell_bold = ParagraphStyle('TCB', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=6.6, leading=8.5, textColor=colors.HexColor('#0F172A'))

    story = []

    story.append(Paragraph("Guía de Arquitectura, Instalación y Gobernanza en Google Antigravity", title_style))
    story.append(Paragraph("<b>Manual Maestro y Fuente Única de la Verdad (Ecosistema Completo y Kit de Alumnos)</b><br/>Desde la descarga del IDE y configuración del motor hasta la gobernanza agéntica y el trabajo desatendido.", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0284C7"), spaceAfter=5, spaceBefore=0))

    # FASE 0
    story.append(Paragraph("FASE 0: DESCARGA E INSTALACIÓN (PARTIR DE CERO EN WINDOWS Y MAC)", phase_style))
    story.append(Paragraph("0.1 ¿Por qué elegir Antigravity IDE frente a la App de Escritorio?", h1_style))
    story.append(Paragraph("Google ofrece dos opciones: la <b>App de Escritorio</b> (un chat conversacional cerrado que oculta las carpetas y los diffs de código) y el <b>Antigravity IDE</b> (entorno profesional basado en VS Code). <b>Recomendación Oficial:</b> Instalar siempre el IDE para tener en una sola ventana el explorador de archivos a la izquierda, el editor central, la terminal integrada abajo y el chat de IA a la derecha.", body_style))

    table_f0_data = [
        [Paragraph("Sistema Operativo", table_header), Paragraph("Instalador Oficial", table_header), Paragraph("Proceso de Instalación en 3 Pasos", table_header)],
        [Paragraph("<b>Windows 10 / 11</b>", table_cell_bold), Paragraph("Instalador <code>.exe</code> (x64)", table_cell), Paragraph("1. Descargar y ejecutar .exe.<br/>2. Seguir el asistente.<br/>3. Abrir Antigravity e iniciar sesión con Google.", table_cell)],
        [Paragraph("<b>macOS (Apple / Intel)</b>", table_cell_bold), Paragraph("Instalador <code>.dmg</code>", table_cell), Paragraph("1. Abrir .dmg.<br/>2. Arrastrar a /Aplicaciones.<br/>3. Abrir app e iniciar sesión con Google.", table_cell)]
    ]
    t_f0 = Table(table_f0_data, colWidths=[105, 110, 308.27])
    t_f0.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_f0)
    story.append(Spacer(1, 3))

    # FASE 1
    story.append(Paragraph("FASE 1: FUNDAMENTOS Y ARQUITECTURA DEL ESPACIO DE TRABAJO", phase_style))
    story.append(Paragraph("1.1 De la Ilusión del 'Vibe Coding' a la Gobernanza Real (Las 4 D)", h1_style))

    def make_section_box(num_str, title_str, danger_text, sol_text):
        p_danger = [Paragraph(f"⚠️ {num_str} PELIGRO: {title_str.upper()}", danger_title), Paragraph(danger_text, danger_body)]
        t_danger = Table([[p_danger]], colWidths=[PAGE_WIDTH])
        t_danger.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FEF2F2")),
            ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#F87171")),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ]))

        p_sol = [Paragraph("🛡️ SOLUCIÓN DE GOBERNANZA:", sol_title), Paragraph(sol_text, sol_body)]
        t_sol = Table([[p_sol]], colWidths=[PAGE_WIDTH])
        t_sol.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0FDF4")),
            ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#4ADE80")),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ]))
        return KeepTogether([t_danger, Spacer(1, 1.5), t_sol, Spacer(1, 2.5)])

    story.append(make_section_box("1.", "Duplicación", "Reescritura de utilidades y funciones redundantes en archivos dispersos.", "Documento vivo ESTADO_GLOBAL_PROYECTOS.md como inventario técnico previo obligatorio."))
    story.append(make_section_box("2.", "Drift (Deriva)", "Ceguera de contexto en sesiones largas, pérdida de arquitectura y abreviaturas inventadas.", "Arquitectura Elephant-Goldfish, catálogos canónicos exactos (NASA Eyes) y doble contador correlativo."))
    story.append(make_section_box("3.", "Deluge (Diluvio)", "Inflación de dependencias (npm, frameworks pesados) para tareas simples.", "Regla de cero herramientas nuevas, herramientas nativas del sistema operativo y micro-apps atómicas."))
    story.append(make_section_box("4.", "Deception (Engaño)", "Código que compila pero oculta datos falsos, APIs bloqueadas o activos inertes.", "Autocomprobación obligatoria, calibración temporal UTC en sondas históricas y copias BKP garantizadas."))

    story.append(Paragraph("1.2 Arquitectura Monorepo de Raíz Única", h1_style))
    story.append(Paragraph("Para evitar bloqueos por cruce de carpetas y alertas de <i>Non-Workspace File Access</i>, todo el ecosistema cuelga de una <b>única carpeta raíz</b>. Al fijar el workspace en el directorio padre, el agente opera en un entorno reconocido con acceso fluido a todos los submódulos.", body_style))

    # FASE 2
    story.append(Paragraph("FASE 2: CONFIGURACIÓN BASE DEL MOTOR (SETTINGS DE ANTIGRAVITY)", phase_style))
    table_settings_data = [
        [Paragraph("Parámetro", table_header), Paragraph("Valor Calibrado", table_header), Paragraph("Justificación Técnica", table_header)],
        [Paragraph("<b>Interface Layout</b>", table_cell_bold), Paragraph("<code>Software Engineering</code>", table_cell), Paragraph("Consola completa, terminales, linter y git para trabajo técnico integral.", table_cell)],
        [Paragraph("<b>Execution Policy</b>", table_cell_bold), Paragraph("<code>proceed-in-sandbox</code>", table_cell), Paragraph("Autonomía desatendida dentro del Sandbox; frena llamadas externas peligrosas.", table_cell)],
        [Paragraph("<b>Terminal Sandbox</b>", table_cell_bold), Paragraph("<code>Enabled (true)</code>", table_cell), Paragraph("Aislamiento seguro: lectura/escritura en raíz y /tmp; cero riesgo en el Mac.", table_cell)],
        [Paragraph("<b>Prevent Sleep</b>", table_cell_bold), Paragraph("<code>Enabled (true)</code>", table_cell), Paragraph("Evita suspensión del Mac en procesos por lotes (compilaciones y PPTX).", table_cell)],
        [Paragraph("<b>Message Execution</b>", table_cell_bold), Paragraph("<code>Queue Message</code>", table_cell), Paragraph("Encola mensajes durante el turno para ejecuciones atómicas sin cortes.", table_cell)],
        [Paragraph("<b>Model Selection</b>", table_cell_bold), Paragraph("<code>Pro / Flash</code>", table_cell), Paragraph("Pro para el Elefante (coordinador); Flash para subagentes rápidos (Goldfish).", table_cell)]
    ]
    t_set = Table(table_settings_data, colWidths=[110, 115, 298.27])
    t_set.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 1.8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_set)
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>Primacía de AGENTS.md:</b> Las directivas en <code>AGENTS.md</code> y <code>GEMINI.md</code> en la raíz del workspace tienen precedencia absoluta sobre los menús de la aplicación.", body_style))

    # FASE 3
    story.append(Paragraph("FASE 3: EL NÚCLEO DE PROTOCOLOS DE COMPORTAMIENTO (AGENTS.MD)", phase_style))
    story.append(Paragraph("3.1 Cero-Submits y Patrón de Trabajo en Silencio", h1_style))
    p_sil_text = "<b>• Protocolo de Oro Cero-Submits:</b> Prohibido abrir ventanas emergentes de confirmación interactiva (RequestFeedback: false).<br/><b>• Fase 1 (Silencio en Sandbox):</b> El agente procesa, edita y compila archivos en segundo plano sin emitir charlas ni popups intermedios.<br/><b>• Fase 2 (Comando Único al Final):</b> Al concluir con éxito, entrega un único bloque bash numerado (ej. <code>[COMANDO XX]</code>) con cabecera y pie visibles por <code>echo</code> y sincronización automática con GitHub (<code>git push origin main</code>)."
    t_sil_box = Table([[Paragraph(p_sil_text, feat_body)]], colWidths=[PAGE_WIDTH])
    t_sil_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0FDF4")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#22C55E")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(KeepTogether([t_sil_box, Spacer(1, 2.5)]))

    story.append(Paragraph("3.2 Elephant-Goldfish, Doble Contador y Salvaguarda Senior (+65)", h1_style))
    story.append(Paragraph("• <b>Elephant-Goldfish:</b> Coordinador con memoria vs. subagentes efímeros limpios con autodestrucción inmediata.<br/>• <b>Doble Contador Correlativo:</b> Contador General de Clases y Contador de Música independientes.<br/>• <b>La Triple Salvaguarda Pedagógica (+65):</b> Cero código intermedio para alumnos senior; aplicaciones en modo Canvas/Vista Previa directa con copia de respaldo oficial BKP en mapas.", body_style))

    # FASE 4
    story.append(Paragraph("FASE 4: CAPACIDADES AVANZADAS DE ÚLTIMA GENERACIÓN", phase_style))
    story.append(Paragraph("4.1 Subagentes Paralelos, Generative UI y Despliegue Continuo", h1_style))
    story.append(Paragraph("• <b>Subagentes en Paralelo (<code>invoke_subagent</code>):</b> Concurrencia masiva para tareas pesadas y cierre inmediato (<code>kill</code>).<br/>• <b>Generative UI (<code>&lt;agent-embed&gt;</code>):</b> Paneles y cuadros de mando interactivos embebidos con Tailwind CSS.<br/>• <b>Despliegue Continuo a GitHub:</b> Cada cambio queda subido a <code>origin/main</code> para reflejarse en GitHub Pages y Classroom al instante.", body_style))

    # FASE 5
    story.append(Paragraph("FASE 5: PUESTA EN MARCHA AUTOMATIZADA (DOBLE BLOQUE SEÑALIZADO)", phase_style))

    # BLOQUE PROFESOR
    p_prof = [
        Paragraph("📘 PARTE MAESTRA: CASO REAL DE ESTUDIO (ECOSISTEMA DEL PROFESOR)", feat_title),
        Paragraph("<b>Estructura Real Completa en iCloud Drive:</b> <code>CLASES DE TECNOLOGÍA/</code> unifica CURSO-IA, CURSO-ROBOTICA-V2, CURSO_MUSICA, SEGUIMIENTO DEL CALENDARIO y temas de salud.<br/><b>Supercomando Maestro Personal (macOS):</b>", feat_body),
        Paragraph("echo '=== [SUPERCOMANDO MAESTRO: ECOSISTEMA COMPLETO] ==='<br/>ROOT_DIR=\"$HOME/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA\"<br/>mkdir -p \"$ROOT_DIR/00. ARQUITECTURA SISTEMA CON IA\" \"$ROOT_DIR/CURSO-IA/CLASES\" \"$ROOT_DIR/CURSO-ROBOTICA-V2\"<br/>cat &lt;&lt; 'EOF' &gt; \"$ROOT_DIR/.agents/settings.json\"<br/>{\"layout\":\"softwareEngineering\",\"toolExecutionPolicy\":\"proceed-in-sandbox\",\"terminalSandbox\":true,\"preventSleep\":true}<br/>EOF<br/>echo '=== [FIN SUPERCOMANDO MAESTRO] (EXITOSO) ==='", code_banner_style)
    ]
    t_prof = Table([[p_prof]], colWidths=[PAGE_WIDTH])
    t_prof.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0F9FF")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#0284C7")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(KeepTogether([t_prof, Spacer(1, 3)]))

    # BLOQUE ALUMNO
    p_alum = [
        Paragraph("🟢 PARTE DEL ALUMNO: GUÍA PASO A PASO PARA MONTARLO EN TU PC (WINDOWS / MAC)", feat_title),
        Paragraph("<b>1. Dónde Copiar y Descomprimir:</b> Copia <code>WORKSPACE-ANTIGRAVITY-PLANTILLA.zip</code> en tu carpeta <b>Documentos</b> (o C:\\ en Windows) y descomprímelo allí mismo para que te quede <code>Documentos\\WORKSPACE-ANTIGRAVITY\\</code>.<br/><b>2. Abrir en Antigravity IDE:</b> Pulsa <i>File &gt; Open Folder...</i> y selecciona esa carpeta.<br/><b>3. Usar la Terminal sin Miedo:</b> Abre tu consola (CMD en Windows / Terminal en Mac). Pídele cosas a la IA en el chat y, cuando termine en silencio, copia el bloque <code>echo</code> que te entregue, pégalo en la terminal y pulsa Enter para aplicar los cambios con control total.", feat_body)
    ]
    t_alum = Table([[p_alum]], colWidths=[PAGE_WIDTH])
    t_alum.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0FDF4")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#16A34A")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(KeepTogether([t_alum, Spacer(1, 3)]))

    # Catálogo
    table_cat_data = [
        [Paragraph("Hito / Versión", table_header), Paragraph("Ámbito", table_header), Paragraph("Impacto y Beneficio Operativo", table_header)],
        [Paragraph("<b>Fase 0: Instalación desde Cero</b>", table_cell_bold), Paragraph("Setup / IDE", table_cell), Paragraph("Descarga para Windows/Mac argumentando la superioridad del IDE frente a Desktop.", table_cell)],
        [Paragraph("<b>Guía Única Señalizada</b>", table_cell_bold), Paragraph("Gobernanza", table_cell), Paragraph("Fuente única de la verdad con Bloque Maestro (Profesor) y Bloque Alumno (Kit).", table_cell)],
        [Paragraph("<b>Plantilla ZIP en 1 Clic</b>", table_cell_bold), Paragraph("Despliegue", table_cell), Paragraph("Copia directa a Documentos y extracción en destino sin rutas perdidas.", table_cell)],
        [Paragraph("<b>Monorepo Raíz Única</b>", table_cell_bold), Paragraph("Workspace", table_cell), Paragraph("Todas las áreas bajo una misma raíz para cero bloqueos de permisos.", table_cell)],
        [Paragraph("<b>Trabajo en Silencio</b>", table_cell_bold), Paragraph("Metodología", table_cell), Paragraph("Ejecución silenciosa en sandbox y entrega de bloque bash único al final.", table_cell)],
        [Paragraph("<b>Cero-Submits</b>", table_cell_bold), Paragraph("Flujo", table_cell), Paragraph("Cero ventanas emergentes de aprobación en el editor durante la sesión.", table_cell)],
        [Paragraph("<b>Elephant-Goldfish</b>", table_cell_bold), Paragraph("Memoria", table_cell), Paragraph("Auditoría con mente virgen y destrucción inmediata sin fugas de memoria.", table_cell)]
    ]
    t_cat = Table(table_cat_data, colWidths=[120, 95, 308.27])
    t_cat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 1.8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_cat)

    doc.build(story, canvasmaker=NumberedCanvas)
    
    shutil.copyfile(PDF_NOBLE, PDF_MONO)
    shutil.copyfile(PDF_NOBLE, BKP_PDF_MONO)
    print("✅ PDF generado y sincronizado con Fase 0 e IDE.", flush=True)

if __name__ == "__main__":
    compilar_html()
    compilar_pdf_reportlab()
