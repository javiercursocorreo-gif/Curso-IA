#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_arquitectura_soluciones_antigravity.py
Genera la Guía Maestra Técnica y Didáctica Definitiva (Versión Enciclopédica Completa y Calibrada):
'GUÍA DE ARQUITECTURA, INSTALACIÓN Y GOBERNANZA EN GOOGLE ANTIGRAVITY'
(Edición Íntegra Extensa: 5 Fases reestructuradas, enfoque general y didáctico, Mac o PC universal,
Fase 4 unificada en Fase 3, Plantilla Universal en 1 Clic para todos y Kit de Alumnos vertical sin terminal de instalación)

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
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(36, 32, A4[0] - 36, 32)
        left_text = "Ecosistema Tecnológico • Guía Maestra de Arquitectura, Instalación y Gobernanza en Antigravity"
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
        h3 { color: #0f172a; margin-top: 22px; font-size: 1.15rem; }
        .toc-box { background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 20px 24px; margin: 25px 0; }
        .toc-title { font-weight: 800; font-size: 1.15rem; color: #0f172a; margin-bottom: 12px; border-bottom: 1px solid #cbd5e1; padding-bottom: 6px; }
        .toc-list { list-style: none; padding-left: 0; }
        .toc-list li { margin-bottom: 6px; font-size: 0.92rem; }
        .toc-list ul { list-style: none; padding-left: 20px; margin-top: 4px; }
        .toc-list ul li { font-size: 0.88rem; color: #475569; }
        .toc-link { color: #0284c7; text-decoration: none; font-weight: 600; }
        .toc-link:hover { text-decoration: underline; }
        .phase-header { background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #fff; padding: 12px 18px; border-radius: 8px; margin-top: 40px; margin-bottom: 15px; font-size: 1.25rem; font-weight: 700; letter-spacing: 0.5px; }
        .danger-box { background: #fef2f2; border: 1px solid #f87171; border-radius: 8px; padding: 15px 18px; margin: 15px 0; }
        .solution-box { background: #f0fdf4; border: 1px solid #4ade80; border-radius: 8px; padding: 15px 18px; margin: 15px 0; }
        .feature-box { background: #f8fafc; border: 1px solid #38bdf8; border-radius: 8px; padding: 15px 18px; margin: 15px 0; }
        .param-box { background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px 20px; margin: 16px 0; }
        .box-profesor { background: #f0f9ff; border: 2px solid #0284c7; border-radius: 8px; padding: 18px 20px; margin: 20px 0; }
        .box-alumno { background: #f0fdf4; border: 2px solid #16a34a; border-radius: 8px; padding: 18px 20px; margin: 20px 0; }
        .quote-box { background: #f8fafc; border-left: 4px solid #64748b; padding: 14px 20px; font-style: italic; margin: 20px 0; font-size: 1.05rem; }
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
        .badge-param { background: #f1f5f9; color: #475569; }
        .step-item { background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 12px 16px; margin: 10px 0; }
        .step-num { font-weight: 800; color: #16a34a; font-size: 1rem; margin-right: 6px; }
    </style>
</head>
<body>
    <h1>Guía de Arquitectura, Instalación y Gobernanza en Google Antigravity</h1>
    <p><strong>Manual Maestro y Fuente Única de la Verdad (Ecosistema Completo y Kit de Inicio para Alumnos)</strong><br>
    <em>Desde la descarga del IDE y configuración del motor hasta la gobernanza agéntica y el trabajo desatendido en silencio en Mac o PC.</em></p>

    <div class="quote-box">
        «El verdadero peligro no es que la inteligencia artificial escriba código, sino que el humano pierda el gobierno sobre la arquitectura. El código se delega; el rigor, la jerarquía de ficheros, la memoria y la verificación jamás.»<br>
        <strong>— Marco de Gobernanza Agéntica en Google Antigravity</strong>
    </div>

    <!-- ÍNDICE GENERAL -->
    <div class="toc-box">
        <div class="toc-title">📑 ÍNDICE GENERAL DEL DOCUMENTO</div>
        <ul class="toc-list">
            <li><strong><a class="toc-link" href="#fase0">FASE 0: DESCARGA E INSTALACIÓN (PARTIR DE CERO EN WINDOWS Y MAC)</a></strong>
                <ul>
                    <li>0.1 La Web Oficial y Selección Correcta del Instalador (Evitar la trampa del CLI)</li>
                    <li>0.2 Antigravity Desktop vs. Antigravity IDE (Por qué elegir el IDE)</li>
                    <li>0.3 Inicio de Sesión: El Consejo de Oro de la Cuenta de Google Gemini</li>
                    <li>0.4 Tabla Comparativa de Instalación Paso a Paso (Windows y macOS)</li>
                </ul>
            </li>
            <li><strong><a class="toc-link" href="#fase1">FASE 1: FUNDAMENTOS Y ARQUITECTURA DEL ESPACIO DE TRABAJO</a></strong>
                <ul>
                    <li>1.1 De la Ilusión del 'Vibe Coding' a la Gobernanza Real</li>
                    <li>1.2 Las 4 D del Peligro de la IA y Nuestras Soluciones (Duplicación, Drift, Deluge, Deception)</li>
                    <li>1.3 Arquitectura Monorepo de Raíz Única: Cero Bloqueos de Permisos</li>
                </ul>
            </li>
            <li><strong><a class="toc-link" href="#fase2">FASE 2: CONFIGURACIÓN BASE DEL MOTOR (SETTINGS DE ANTIGRAVITY)</a></strong>
                <ul>
                    <li>2.1 Análisis Exhaustivo de Parámetros del Motor (Execution Policy, Sandbox, Layout, Sleep)</li>
                    <li>2.2 Primacía Jerárquica de AGENTS.md sobre la Interfaz Visual</li>
                </ul>
            </li>
            <li><strong><a class="toc-link" href="#fase3">FASE 3: EL NÚCLEO DE PROTOCOLOS DE GOBERNANZA Y CAPACIDADES AGÉNTICAS (AGENTS.MD)</a></strong>
                <ul>
                    <li>3.1 Protocolo de Oro: Cero-Submits Absoluto</li>
                    <li>3.2 El Patrón Operativo Maestro: Trabajo en Silencio y Uso de la Consola (¿Cuándo, Cómo y Por Qué?)</li>
                    <li>3.3 Protocolo Cognitivo Elephant-Goldfish (Memoria vs. Auditoría Virgen)</li>
                    <li>3.4 Contador Correlativo de Comandos y Trazabilidad Cronológica</li>
                    <li>3.5 La Triple Salvaguarda Pedagógica (+65) y Cero Código Intermedio</li>
                    <li>3.6 Orquestación Concurrente: Subagentes Efímeros en Paralelo (invoke_subagent / kill)</li>
                    <li>3.7 Visualización Directa y Paneles Vivos: Generative UI en Antigravity (&lt;agent-embed&gt;)</li>
                    <li>3.8 Pipeline de Despliegue Continuo: GitHub como BKP Blindado y Servidor Web Global (GitHub Pages)</li>
                    <li>3.9 Arquitectura Modular de Skills (SKILL.md): Automatización sin Prompts Largos</li>
                </ul>
            </li>
            <li><strong><a class="toc-link" href="#fase4">FASE 4: PUESTA EN MARCHA DEL ESPACIO DE TRABAJO (PLANTILLA EN 1 CLIC)</a></strong>
                <ul>
                    <li>4.1 La Solución Definitiva: Plantilla Universal en 1 Clic (WORKSPACE-ANTIGRAVITY-PLANTILLA.zip)</li>
                    <li>4.2 Instalación Paso a Paso en tu Ordenador (Windows y macOS)</li>
                    <li>4.3 Catálogo Evolutivo de Mejoras del Ecosistema</li>
                </ul>
            </li>
        </ul>
    </div>

    <!-- FASE 0 -->
    <div id="fase0" class="phase-header">FASE 0: DESCARGA E INSTALACIÓN (PARTIR DE CERO EN WINDOWS Y MAC)</div>

    <h2>0.1 La Web Oficial y Selección Correcta del Instalador (Evitar la trampa del CLI)</h2>
    <p>Para empezar desde cero con Google Antigravity en tu ordenador (Mac o PC), acudimos a la web oficial: <strong><code>antigravity.google</code></strong>. Al pulsar el botón de descarga principal, la plataforma muestra distintas opciones y pestañas que pueden confundir al usuario novato:</p>
    <ul>
        <li><strong>Cuidado con "Apple Antigravity CLI":</strong> Por defecto, si el sistema detecta macOS o si se pulsa sin mirar, puede ofrecer la versión de consola pura (CLI). <em>Esta no es la versión que queremos</em>; la CLI no tiene interfaz visual y está pensada solo para scripts de servidor.</li>
        <li><strong>Cambio de Pestaña según tu Sistema Operativo:</strong> Si estás en un ordenador con <strong>Windows</strong> o con <strong>Linux</strong>, es obligatorio fijarse en las pestañas superiores de la página de descarga y hacer clic en la pestaña <strong>"Windows"</strong> (o "Linux") para que se descargue el instalador ejecutable <code>.exe</code> adecuado.</li>
    </ul>

    <h2>0.2 Antigravity Desktop vs. Antigravity IDE (Por qué elegir el IDE)</h2>
    <p>Google ofrece dos interfaces para interactuar con la plataforma en tu ordenador (Mac o PC):</p>
    <ul>
        <li><strong>Antigravity Desktop (App de Escritorio):</strong> Es una aplicación visual muy básica, orientada casi exclusivamente a chatear. <em>Inconveniente:</em> Oculta el árbol de carpetas, no muestra las diferencias exactas de código (diffs rojos/verdes) y no tiene consola de ejecución integrada, quedándose corta de inmediato.</li>
        <li><strong>Antigravity IDE (Entorno Integrado basado en VS Code - NUESTRA ELECCIÓN OFICIAL):</strong> Es la herramienta profesional definitiva. En una única pantalla integra el explorador de archivos a la izquierda, el editor de código central, la terminal de comandos abajo y el copiloto de IA a la derecha.</li>
    </ul>

    <div class="solution-box">
        <strong>💡 Recomendación Oficial del Curso:</strong> Instala siempre <strong>Antigravity IDE</strong>. Aunque seas principiante, verás en tiempo real cómo la IA crea tus carpetas y archivos en el disco, teniendo el 100% del control visual de lo que ocurre en tu ordenador (Mac o PC).
    </div>

    <h2>0.3 Inicio de Sesión: El Consejo de Oro de la Cuenta de Google Gemini</h2>
    <p>Una vez descargada e instalada la aplicación en tu ordenador (sea ejecutando el <code>.exe</code> en Windows o arrastrando el <code>.dmg</code> a Aplicaciones en Mac), al abrir Antigravity por primera vez te pedirá iniciar sesión:</p>
    <div class="solution-box">
        <strong>💡 Consejo Crucial de Rendimiento:</strong> Al pulsar en <em>"Continuar con Google"</em>, <strong>inicia sesión con la cuenta de Google con la que ya pagues una suscripción de Gemini (Google One AI Premium o Gemini Advanced)</strong> si dispones de ella. Al vincular una cuenta de pago, Antigravity te otorgará una cuota de uso, velocidad de respuesta y límites de tokens drásticamente superiores para trabajar con modelos avanzados (Gemini Pro) sin interrupciones.
    </div>

    <h2>0.4 Tabla Comparativa de Instalación Paso a Paso</h2>
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
    <div id="fase1" class="phase-header">FASE 1: FUNDAMENTOS Y ARQUITECTURA DEL ESPACIO DE TRABAJO</div>

    <h2>1.1 De la Ilusión del 'Vibe Coding' a la Gobernanza Real</h2>
    <p>En la era del desarrollo con modelos generativos avanzados, programar parece haberse convertido en un ejercicio casi instantáneo. Con solo describir intenciones en lenguaje natural ("vibe coding"), es posible generar cientos de líneas de código en minutos.</p>
    <p>Sin embargo, la velocidad desprovista de arquitectura desemboca en una trampa crítica: <strong>la falsa ilusión de perfección</strong>. Un modelo generativo optimiza probabilísticamente para la respuesta inmediata del turno actual, perdiendo de vista el ciclo de vida del repositorio. Sin salvaguardas explícitas, el código resultante acumula silenciosamente cuatro patologías conocidas como <strong>Las 4 D del peligro de la IA</strong>.</p>

    <h2>1.2 Las 4 D del Peligro de la IA y Nuestras Soluciones de Gobernanza</h2>

    <div class="danger-box">
        <span class="badge badge-danger">1. DUPLICACIÓN (Duplication)</span><br>
        <strong>⚠️ El Peligro en la IA:</strong> Al solicitar una nueva funcionalidad, el agente tiende por impulso probabilístico a reescribir funciones de utilidad, estilos y lógica que ya existían en otros archivos del proyecto. Esto fragmenta la base de código, multiplica los puntos de fallo y hace inmanejable el mantenimiento futuro.
    </div>
    <div class="solution-box">
        <span class="badge badge-solution">Soluciones en la Arquitectura</span><br>
        <strong>🛡️ Gobernanza Antigravity:</strong>
        <ul>
            <li><strong>Documento Vivo Centralizado (<code>ESTADO_GLOBAL_PROYECTOS.md</code>):</strong> Memoria técnica compartida y relevo obligatorio. Antes de codificar, el agente debe comprobar utilidades existentes para reutilizarlas sin duplicar.</li>
            <li><strong>Librerías Base Reutilizables y Scripts Maestros:</strong> Estandarización en módulos centrales (ej. generadores de bitácora y scripts batch) en lugar de dispersar código repetido.</li>
            <li><strong>Curaduría y Desduplicación Estricta:</strong> Como en el sistema de generación de fichas didácticas y mapas interactivos, donde se auditan previamente los componentes HUD, botones de navegación y estilos visuales para reutilizar siempre el estándar común y prohibir la creación de elementos redundantes o duplicados.</li>
        </ul>
    </div>

    <div class="danger-box">
        <span class="badge badge-danger">2. DRIFT (Desviación / Deriva de Contexto)</span><br>
        <strong>⚠️ El Peligro en la IA:</strong> A medida que la conversación acumula miles de tokens, el modelo sufre fatiga cognitiva ("ceguera de contexto"). Se aleja sutilmente de las reglas fundacionales, altera estructuras de carpetas acordadas, inventa abreviaturas o relaja los estándares de calidad.
    </div>
    <div class="solution-box">
        <span class="badge badge-solution">Soluciones en la Arquitectura</span><br>
        <strong>🛡️ Gobernanza Antigravity:</strong>
        <ul>
            <li><strong>Protocolo Elephant-Goldfish:</strong> El <em>Elefante</em> (coordinador) mantiene la memoria histórica y planifica; el <em>Goldfish</em> (subagente efímero) nace con mente virgen para auditar el código contra una lista de control estricta y se destruye inmediatamente sin dejar procesos residuales.</li>
            <li><strong>Catálogos Canónicos Estrictos:</strong> Prohibición absoluta de abreviaturas inventadas. En NASA Eyes se exige el ID exacto (<code>sc_roman_space_telescope</code>, nunca <code>sc_roman</code>); en simuladores científicos, identificadores formales contrastados en bases de datos abiertas.</li>
            <li><strong>Contador Correlativo de Comandos y Trazabilidad:</strong> Mantenimiento estricto de una numeración secuencial de comandos (<code>[COMANDO XX]</code>) para anclar cada avance en la bitácora técnica sin saltos ni desviaciones.</li>
        </ul>
    </div>

    <div class="danger-box">
        <span class="badge badge-danger">3. DELUGE (Diluvio de Código y Sobre-Ingeniería)</span><br>
        <strong>⚠️ El Peligro en la IA:</strong> Propensión del modelo a 'vomitar' cientos de líneas de código superfluo, proponiendo frameworks pesados, dependencias de terceros (<code>npm</code>, librerías <code>pip</code> ajenas) o arquitecturas mastodónticas para resolver problemas que se solucionan con pocas líneas nativas.
    </div>
    <div class="solution-box">
        <span class="badge badge-solution">Soluciones en la Arquitectura</span><br>
        <strong>🛡️ Gobernanza Antigravity:</strong>
        <ul>
            <li><strong>Regla de Cero Herramientas Nuevas ni Instalaciones Externas:</strong> Prohibición radical de instalar paquetes de terceros. Se opera exclusivamente con herramientas nativas del sistema operativo (Mac o PC) y Python estándar (<code>urllib</code>, <code>xml</code>, scripts nativos).</li>
            <li><strong>Diferenciación Clara de Motores 3D:</strong> Prohibición de Babylon.js en simuladores anatómicos/médicos de IA (donde se exige Three.js limpio o Canvas fotográfico hiperrealista) mientras se reserva y mantiene Babylon.js al 100% como motor oficial en Robótica (aprovechando sus shaders y física Havok).</li>
            <li><strong>La Triple Salvaguarda Pedagógica (+65):</strong> Cero código intermedio para los alumnos senior. Se entregan micro-aplicaciones autónomas de 1 página que funcionan al 100% con doble clic en cualquier navegador sin servidor ni dependencias.</li>
        </ul>
    </div>

    <div class="danger-box">
        <span class="badge badge-danger">4. DECEPTION (Engaño / Ilusión de Funcionamiento)</span><br>
        <strong>⚠️ El Peligro en la IA:</strong> El código compila y la interfaz luce profesional, pero internamente es un cascarón vacío: datos estáticos inventados, APIs bloqueadas por seguridad o sondas históricas orbitando la Tierra en lugar de su planeta destino por omitir el parámetro temporal.
    </div>
    <div class="solution-box">
        <span class="badge badge-solution">Soluciones en la Arquitectura</span><br>
        <strong>🛡️ Gobernanza Antigravity:</strong>
        <ul>
            <li><strong>Obligación de Autocomprobación Previa y Poda Temprana:</strong> Si un activo, telemetría o malla 3D no existe o no se mueve en el motor real, no se maquilla ni se inventa: se poda de raíz y se sustituye de inmediato por un activo 100% verificado.</li>
            <li><strong>Calibración Temporal de Sondas Históricas:</strong> Inyección obligatoria de marcas temporales UTC (<code>time=YYYY-MM-DD...</code>) para ubicar las sondas en su fecha activa y planeta real.</li>
            <li><strong>Blindaje ante Restricciones del Navegador:</strong> Supresión de enlaces directos a WhatsApp (<code>api.whatsapp.com</code>) bloqueados por la política COOP de Safari, adoptando la publicación nativa en Gemini Canvas.</li>
            <li><strong>Copia de Respaldo Garantizada (BKP Oficial):</strong> Botón de respaldo local probado en cada mapa interactivo para asegurar que el 100% de los alumnos disfrute de la experiencia completa sin atascos de red.</li>
        </ul>
    </div>

    <h2>1.3 Arquitectura Monorepo de Raíz Única: Cero Bloqueos de Permisos</h2>
    <p>Para erradicar de raíz el problema clásico de permisos, fragmentación y pérdida de contexto entre carpetas dispersas, todo el ecosistema está estructurado bajo una <strong>única carpeta raíz (Monorepo Workspace)</strong>.</p>
    <p>Al situar la raíz de Antigravity en este directorio padre en tu ordenador (Mac o PC), <strong>el agente opera permanentemente dentro del mismo espacio de trabajo reconocido</strong>, lo que permite el acceso universal a todos los submódulos sin necesidad de solicitar permisos especiales de <em>Non-Workspace File Access</em> ni disparar ventanas de confirmación.</p>

    <!-- FASE 2 -->
    <div id="fase2" class="phase-header">FASE 2: CONFIGURACIÓN BASE DEL MOTOR (SETTINGS DE ANTIGRAVITY)</div>

    <h2>2.1 Análisis Exhaustivo de Configuración y Parámetros del Motor Antigravity</h2>
    <p>A diferencia de interfaces conversacionales estándar, Google Antigravity es un entorno de desarrollo agéntico gobernado por parámetros técnicos explícitos. A continuación se desglosan en detalle los parámetros analizados en el vídeo, su funcionamiento interno y la calibración aplicada en nuestro ecosistema:</p>

    <div class="param-box">
        <span class="badge badge-param">Parámetro 1</span>
        <h3>1. Política de Ejecución de Terminal (Tool Execution Policy)</h3>
        <p>Determina el grado de autonomía y el nivel de intervención humana requerido cada vez que el agente debe ejecutar un comando en la shell (ej. crear carpetas, ejecutar scripts, compilar o comprobar archivos).</p>
        <ul>
            <li><strong>Modo Estricto (<code>strict</code> / <code>request-review</code>):</strong> El agente detiene su turno ante cada comando unitario y abre una ventana emergente en pantalla solicitando la aprobación explícita del usuario (botón "Submit" / "Approve").</li>
            <li><strong>Modo Decisión del Agente (<code>agent-decides</code>):</strong> El modelo clasifica el riesgo de cada instrucción: ejecuta automáticamente comandos de solo lectura pero se frena ante modificaciones de ficheros.</li>
            <li><strong>Modo Turbo / YOLO (<code>always-proceed</code>):</strong> Autonomía absoluta sin pausas ni revisiones intermedias, ejecutando cualquier instrucción directamente sobre el sistema.</li>
            <li><strong>Modo Sandbox Protegido (<code>proceed-in-sandbox</code> - NUESTRO ESTÁNDAR OFICIAL):</strong> El agente ejecuta tareas de forma 100% desatendida y silenciosa mientras trabaje dentro del Sandbox aislado del proyecto. Si una orden solicita saltar el sandbox (<code>BypassSandbox: true</code>), el sistema operativo activa de inmediato el freno de seguridad y lanza la confirmación humana.</li>
        </ul>
    </div>

    <div class="param-box">
        <span class="badge badge-param">Parámetro 2</span>
        <h3>2. Modo Sandbox y Aislamiento de Procesos (Terminal Sandbox)</h3>
        <p>Define la jaula de seguridad y contención en la que corren los procesos del asistente.</p>
        <ul>
            <li><strong>Aislamiento de Recursos:</strong> En modo estándar (<code>BypassSandbox: false</code>), el agente tiene permisos plenos de lectura y escritura dentro de la carpeta raíz del proyecto y directorios temporales, pero no puede acceder a otras carpetas privadas del Mac o PC ni modificar configuraciones de red del sistema anfitrión.</li>
            <li><strong>Eliminación de Fricción:</strong> Permite auto-aprobar comandos sin intervención del usuario, garantizando el cumplimiento estricto del <em>Protocolo de Cero Submits</em>.</li>
        </ul>
    </div>

    <div class="param-box">
        <span class="badge badge-param">Parámetro 3</span>
        <h3>3. Acceso a Archivos Fuera del Workspace (Non-Workspace File Access)</h3>
        <p>Regula la conducta del agente si una instrucción le solicita leer o alterar archivos fuera de la ruta de trabajo inicial.</p>
        <ul>
            <li><strong>Opciones de Motor:</strong> <code>allow</code> (acceso libre), <code>ask</code> (preguntar al usuario con popup), <code>deny</code> (bloqueo absoluto).</li>
            <li><strong>Nuestra Solución por Diseño:</strong> Gracias a nuestra <em>Arquitectura de Raíz Única</em>, <strong>el 100% de los proyectos cuelgan de la misma raíz</strong>. El agente jamás necesita salir del workspace, eliminando alertas de seguridad por cruce de carpetas.</li>
        </ul>
    </div>

    <div class="param-box">
        <span class="badge badge-param">Parámetro 4</span>
        <h3>4. Acceso a Internet y Lista Blanca de Navegación (Internet Access & Browser Allowlist)</h3>
        <p>Controla la capacidad del agente para realizar peticiones de red y abrir sesiones automatizadas en el navegador.</p>
        <ul>
            <li><strong>Nivel de Red:</strong> Configurado en modo lectura y consulta de repositorios científicos (NASA, USGS, Wikimedia Commons) para obtener datos reales.</li>
            <li><strong>Prevención de Invasión en Navegadores:</strong> Se restringe el control invasivo del navegador local mediante Chrome DevTools (que exige puertos de depuración y dispara diálogos de seguridad en macOS o Windows), favoreciendo en su lugar micro-aplicaciones locales autónomas en HTML5.</li>
        </ul>
    </div>

    <div class="param-box">
        <span class="badge badge-param">Parámetro 5</span>
        <h3>5. Selección de Modelo y Enrutamiento Inteligente (Model Selection)</h3>
        <p>Permite alternar entre los distintos motores neuronales de la familia Gemini según la carga cognitiva requerida.</p>
        <ul>
            <li><strong>Gemini Pro (Coordinador / Elefante):</strong> Diseñado para razonamiento profundo, visión holística del calendario, planificación de lotes y mantenimiento de la arquitectura sin derivas.</li>
            <li><strong>Gemini Flash (Subagentes / Goldfish):</strong> Modelo ligero de bajísima latencia para subagentes paralelos asignados a tareas atómicas (comprobar sintaxis, auditar límites de páginas o verificar enlaces) en fracciones de segundo.</li>
        </ul>
    </div>

    <div class="param-box">
        <span class="badge badge-param">Parámetro 6</span>
        <h3>6. Jerarquía de Reglas del Proyecto (AGENTS.md y GEMINI.md)</h3>
        <p>El núcleo de gobernanza que subordina el comportamiento de la IA a las instrucciones formales del usuario.</p>
        <ul>
            <li><strong>Prioridad Jerárquica:</strong> Las reglas ubicadas en los archivos <code>AGENTS.md</code> y <code>GEMINI.md</code> de la raíz del workspace tienen <strong>prioridad absoluta</strong> sobre cualquier configuración general de la aplicación.</li>
            <li><strong>Persistencia de Estándares:</strong> Es aquí donde quedan blindados los compromisos innegociables: Cero-Submits, Cuadro de Mando Matutino, Contador Correlativo, Estándar de Fichas Largas y Despliegue Automático a GitHub.</li>
        </ul>
    </div>

    <!-- FASE 3 -->
    <div id="fase3" class="phase-header">FASE 3: EL NÚCLEO DE PROTOCOLOS DE GOBERNANZA Y CAPACIDADES AGÉNTICAS (AGENTS.MD)</div>

    <h2>3.1 Protocolo de Oro: Cero-Submits Absoluto</h2>
    <p>Prohibición radical de ventanas emergentes de confirmación interactiva en el editor (<code>RequestFeedback: false</code>). El asistente trabaja de manera 100% desatendida sin detener la ejecución en botones de aprobación intermedia.</p>

    <h2>3.2 El Patrón Operativo Maestro: Trabajo en Silencio y Uso de la Consola</h2>
    <p>Uno de los mayores hallazgos metodológicos de nuestro ecosistema es la articulación del <strong>flujo de trabajo 100% desatendido</strong>: el agente realiza todo el esfuerzo técnico de forma silenciosa e invisible dentro del entorno y, únicamente al concluir con éxito, entrega al usuario un <strong>bloque de comando único numerado para la terminal externa</strong>.</p>

    <div class="feature-box">
        <span class="badge badge-feature">Metodología de Ejecución</span><br>
        <strong>¿En qué momento se usa, cómo opera y por qué se diseñó esta arquitectura?</strong>
        <br><br>
        <h3>1. ¿En qué momento se usa?</h3>
        <p>Se aplica de forma obligatoria en <strong>todas las tareas operativas del sistema</strong>: creación y edición de fichas didácticas, actualización de la bitácora y calendario escolar, reescritura de scripts en Python, modificación de mapas HTML interactivos, sincronizaciones masivas y publicaciones en GitHub Pages / Google Classroom.</p>

        <h3>2. ¿Cómo lo usamos? (Mecánica Técnica en Dos Fases)</h3>
        <ul>
            <li><strong>Fase 1: Trabajo en Silencio en el Sandbox (Lado Asistente):</strong> El agente utiliza sus herramientas internas nativas de edición (<code>read_file</code>, <code>edit_file</code>, <code>write_file</code>) y comandos atómicos dentro del Sandbox (<code>BypassSandbox: false</code>). Procesa los archivos, compila los PDFs, actualiza la bitácora y verifica sintaxis <em>sin emitir charlas intermedias, sin explicaciones redundantes y sin solicitar autorizaciones</em> (<code>RequestFeedback: false</code>). El usuario nunca ve ventanas de «Submit» ni tiene que pulsar botones de aprobación durante la sesión.</li>
            <li><strong>Fase 2: Entrega del Comando Único al Final (Lado Usuario):</strong> Una vez terminada y verificada la tarea, el agente no le pide al usuario que ejecute múltiples pasos sueltos. Entrega un <strong>único bloque bash autocontenido</strong>, rigurosamente numerado (ej. <code>[COMANDO 208]</code>) y protegido con cabecera y pie visibles mediante <code>echo</code>.</li>
        </ul>

        <div class="code-banner">
### [INICIO COMANDO XX: TÍTULO DEL COMANDO]
echo "========================================================"
echo "=== [INICIO COMANDO XX: TÍTULO DEL COMANDO] ==="
echo "========================================================"
... (instrucciones desatendidas: git, verificación, despliegue) ...
echo "========================================================"
echo "=== [FIN COMANDO XX: TÍTULO DEL COMANDO] (EXITOSO) ==="
echo "========================================================"
### [FIN COMANDO XX: TÍTULO DEL COMANDO]
        </div>

        <h3>3. ¿Por qué lo usamos? (Beneficios de Gobernanza y Control Humano)</h3>
        <ul>
            <li><strong>Eliminación Absoluta de la Fricción Cognitiva:</strong> Evita que el usuario tenga que autorizar 15 o 20 ventanas emergentes por tarea. La IA hace el trabajo pesado y el usuario mantiene la paz mental.</li>
            <li><strong>Trazabilidad y Control Humano Real:</strong> Aunque la IA trabaja sola, <em>el usuario retiene la soberanía final de ejecución</em>. El comando en la terminal externa de su ordenador (Mac o PC) le muestra con total claridad qué se está aplicando en el sistema operativo y cuándo concluye de forma exitosa.</li>
            <li><strong>Cero Fallos de Despliegue en GitHub:</strong> Al empaquetar <code>git add</code>, <code>git commit</code> y <code>git push origin main</code> dentro del comando terminal, se garantiza que jamás quede un cambio local desincronizado con GitHub Pages o Classroom.</li>
            <li><strong>Historial Cronológico Limpio:</strong> Al pegar el comando en la terminal externa del ordenador (Mac o PC), el historial de la shell refleja de manera idéntica y reproducible la secuencia histórica de hitos registrados en <code>ESTADO_GLOBAL_PROYECTOS.md</code>.</li>
        </ul>
    </div>

    <h2>3.3 Protocolo Cognitivo Elephant-Goldfish</h2>
    <p>Separación de roles para evitar la saturación de contexto: el <strong>Elefante</strong> (agente coordinador) mantiene la visión histórica, el calendario y los estándares; el <strong>Goldfish</strong> (subagente efímero) nace con mente limpia para auditar código contra una lista de control estricta y se autodestruye de inmediato sin dejar procesos residuales.</p>

    <h2>3.4 Contador Correlativo de Comandos y Trazabilidad Cronológica</h2>
    <p>Mantenimiento estricto de una numeración secuencial de comandos (<code>[COMANDO XX]</code>) para anclar cada avance en la bitácora técnica sin saltos, colisiones ni pérdidas de trazabilidad.</p>

    <h2>3.5 La Triple Salvaguarda Pedagógica (+65) y Cero Código Intermedio</h2>
    <p>Prohibición tajante de exponer al alumno senior a código fuente (HTML, JavaScript, Three.js). Los prompts generan aplicaciones interactivas en modo Canvas / Vista Previa directa, respaldadas por un botón BKP local probado en cada mapa.</p>

    <h2>3.6 Orquestación Concurrente: Subagentes Efímeros en Paralelo</h2>
    <div class="feature-box">
        <span class="badge badge-feature">Alta Concurrencia y Mente Limpia</span><br>
        <strong>⚡ Multiplicador de Velocidad y Cero Proceso Residual:</strong>
        <p>A medida que los proyectos crecen en complejidad, realizar tareas pesadas dentro de la misma conversación del agente coordinador genera saturación cognitiva. La solución adoptada es la delegación en <strong>subagentes paralelos efímeros</strong>:</p>
        <ul>
            <li><strong>Lanzamiento Atómico (<code>invoke_subagent</code>):</strong> Se despliegan múltiples agentes independientes en paralelo, cada uno acotado a un objetivo específico y con un contexto 100% limpio (aislamiento de fallos).</li>
            <li><strong>Destrucción Inmediata (<code>manage_subagents: kill</code>):</strong> Una vez verificado el resultado, el subagente se destruye de inmediato. Cero consumo de memoria residual, cero archivos zombi en disco.</li>
            <li><strong>Autonomía Silenciosa:</strong> Trabajan de forma desatendida respetando escrupulosamente el <em>Protocolo de Cero Submits</em>, entregando únicamente datos consolidados al agente principal.</li>
        </ul>
    </div>

    <h2>3.7 Visualización Directa y Paneles Vivos: Generative UI en Antigravity</h2>
    <div class="feature-box">
        <span class="badge badge-feature">Visualización Directa y Paneles Vivos</span><br>
        <strong>🎨 Interfaces Nativas sin Fricción ni Código Intermedio:</strong>
        <p>El paradigma tradicional de interacción con IA obliga al usuario a leer largos informes de texto o inspeccionar bloques de código. Con <strong>Generative UI</strong>, Antigravity renderiza directamente componentes e interfaces interactivas funcionales en el chat y en el panel lateral:</p>
        <ul>
            <li><strong>Incrustación Dinámica (<code>&lt;agent-embed&gt;</code>):</strong> El asistente genera artefactos HTML interactivos autónomos que se visualizan directamente integrados en la conversación mediante la etiqueta nativa de Antigravity.</li>
            <li><strong>Diseño Estándar y Accesible:</strong> Interfaces estilizadas con Tailwind CSS y tokens semánticos nativos (<code>var(--foreground)</code>, <code>var(--card)</code>, <code>var(--primary)</code>), con soporte perfecto tanto para modo claro como oscuro.</li>
            <li><strong>Cuadros de Mando y Previsualizaciones Vivas:</strong> Permite supervisar el avance de tareas pendientes, bitácoras de calendario y prototipos interactivos en tiempo real con cero fricción y cero ventanas de confirmación.</li>
        </ul>
    </div>

    <h2>3.8 Pipeline de Despliegue Continuo: GitHub como BKP Blindado y Servidor Web Global (GitHub Pages)</h2>
    <div class="feature-box">
        <span class="badge badge-feature">Copia de Seguridad en la Nube y Servidor Web Instantáneo</span><br>
        <strong>🌐 La Doble Función Estratégica de GitHub en Nuestro Ecosistema:</strong>
        <p>En el flujo de trabajo tradicional, los archivos se quedan atrapados en el disco duro del ordenador. En nuestra arquitectura, cada bloque ejecutable termina obligatoriamente con la subida a GitHub (<code>git push origin main</code>), cumpliendo dos funciones vitales simultáneas:</p>
        <ul>
            <li><strong>1. Respaldo Automático e Inmutable (BKP en la Nube):</strong> Cada línea de código, cada PDF generado y cada simulación interactiva queda archivada en un historial cronológico commit a commit. Si el ordenador local falla, se rompe el disco o se borra un archivo por accidente, el proyecto íntegro con meses de trabajo se recupera al 100% en segundos simplemente clonando el repositorio. Cero riesgo de pérdida de datos.</li>
            <li><strong>2. Servidor Web Global Instantáneo (GitHub Pages):</strong> GitHub no actúa como un mero disco duro pasivo. Mediante el servicio gratuito <strong>GitHub Pages</strong>, transforma de forma automática todo el repositorio en un <strong>servidor web de producción accesible desde cualquier lugar del mundo</strong>. Cada archivo HTML interactivo, simulador 3D, visor fotográfico cinemático o cuadro de mando de Classroom cuenta con una URL pública inmediata.</li>
            <li><strong>Acceso Multi-Dispositivo Universal (Alumnos y Profesor):</strong> El profesor puede abrir los recursos en la pantalla del aula y los alumnos pueden interactuar con ellos desde su iPad, tablet Android, iPhone o PC personal sin necesidad de configurar servidores locales (Apache, Nginx), sin abrir puertos de red y sin pagar hosting web alguno.</li>
            <li><strong>Inyección Anti-Caché para Actualizaciones en Tiempo Real (<code>?v=...</code>):</strong> Para solucionar el clásico problema de que el navegador del alumno o del aula retenga en memoria caché la versión antigua de un documento o simulación, el sistema inyecta automáticamente un parámetro forzador de versión fresca (ej. <code>?v=20261125b</code>). Esto obliga a los navegadores (Safari, Chrome) a descargar la versión recién corregida al primer clic sin exigir a los alumnos mayores que sepan vaciar la caché de su navegador.</li>
        </ul>
    </div>

    <h2>3.9 Arquitectura Modular de Skills (SKILL.md): Automatización sin Prompts Largos</h2>
    <div class="feature-box">
        <span class="badge badge-feature">Especialización por Tarea (Adiós a Repetir Prompts)</span><br>
        <strong>🧩 Gobernanza Global (<code>AGENTS.md</code>) vs. Skills Modulares (<code>SKILL.md</code>):</strong>
        <p>Mientras <code>AGENTS.md</code> fija las reglas permanentes de todo el espacio de trabajo (cero-submits, tono, despliegue), los <strong>Skills</strong> encapsulan procedimientos especializados bajo demanda en archivos <code>SKILL.md</code> (globales o por carpeta en <code>.agent/skills/</code>), evitando escribir prompts largos repetitivos y eliminando el olvido de restricciones (<em>Drift</em>).</p>
        <ul>
            <li><strong>Anatomía Oficial de 4 Bloques:</strong> Todo Skill maestro se estructura en: <strong>1) Rol y Objetivo</strong> (misión exacta), <strong>2) Restricciones Negativas (<em>Never Do</em>)</strong> (prohibiciones tajantes para evitar relleno o alucinaciones), <strong>3) Estructura de Entrada</strong> (qué archivos o datos espera) y <strong>4) Formato de Entrega</strong> (tabla, PDF, HTML o salida validada).</li>
            <li><strong>Catálogo Previsto de Skills Generales del Ecosistema:</strong> <code>ficha-senior</code> (maquetación pedagógica +65 sin código), <code>despliegue-seguro</code> (anti-caché, commit y verificación en <code>CURSO-IA</code>), <code>nasa-eyes-calibrado</code> (catálogo orbital 3D y HUD de 380px) y <code>sincronizador-copilot</code> (réplica automática hacia la guía corporativa).</li>
        </ul>
    </div>

    <!-- FASE 4 -->
    <div id="fase4" class="phase-header">FASE 4: PUESTA EN MARCHA DEL ESPACIO DE TRABAJO (PLANTILLA EN 1 CLIC)</div>

    <div class="box-alumno">
        <span class="badge badge-alumno">🟢 MÉTODO OFICIAL Y UNIVERSAL (PROFESOR Y ALUMNOS)</span>
        <h2>4.1 La Solución Definitiva: Plantilla Universal en 1 Clic</h2>
        <p>Tanto para el profesor como para los alumnos, la forma más limpia, rápida y 100% libre de errores para empezar en cualquier ordenador (Windows o Mac) es utilizar el archivo <strong><code>WORKSPACE-ANTIGRAVITY-PLANTILLA.zip</code></strong>.</p>
        <p>Nos olvidamos de comandos técnicos y consolas de instalación: este paquete comprimido <strong>ya incluye todo configurado por dentro</strong> (la estructura de carpetas, las reglas maestras de <code>AGENTS.md</code> y el archivo invisible <code>.agents/settings.json</code> con el Sandbox protegido preactivado). Solo hay que descomprimirlo y abrir la carpeta.</p>

        <h2>4.2 Instalación Paso a Paso en tu Ordenador (Windows y Mac)</h2>

        <h3>Si usas Windows:</h3>
        <div class="step-item">
            <span class="step-num">Paso 1:</span> Ve a tu explorador de archivos y <strong>copia</strong> el archivo <code>WORKSPACE-ANTIGRAVITY-PLANTILLA.zip</code> en tu carpeta <strong>Documentos</strong> (o en <code>C:\</code>).
        </div>
        <div class="step-item">
            <span class="step-num">Paso 2:</span> Haz clic derecho sobre el archivo ZIP allí mismo y pulsa <strong>"Extraer todo..."</strong>. Al descomprimirlo en ese destino, te quedará tu carpeta lista: <code>Documentos\WORKSPACE-ANTIGRAVITY\</code>.
        </div>
        <div class="step-item">
            <span class="step-num">Paso 3:</span> Abre <strong>Google Antigravity IDE</strong>, pulsa en el menú superior <strong>File &gt; Open Folder...</strong> (Abrir Carpeta...) y selecciona la carpeta descomprimida.
        </div>

        <h3>Si usas Mac:</h3>
        <div class="step-item">
            <span class="step-num">Paso 1:</span> Abre el Finder y <strong>copia</strong> el archivo <code>WORKSPACE-ANTIGRAVITY-PLANTILLA.zip</code> en tu carpeta <strong>Documentos</strong> (o en tu carpeta de usuario).
        </div>
        <div class="step-item">
            <span class="step-num">Paso 2:</span> Haz doble clic sobre el archivo ZIP allí mismo para descomprimirlo. Te quedará tu carpeta lista: <code>Documentos/WORKSPACE-ANTIGRAVITY/</code>.
        </div>
        <div class="step-item">
            <span class="step-num">Paso 3:</span> Abre <strong>Google Antigravity IDE</strong>, pulsa en el menú superior <strong>File &gt; Open Folder...</strong> (Abrir Carpeta...) y selecciona la carpeta descomprimida.
        </div>

        <div class="solution-box" style="margin-top: 15px;">
            <strong>🎉 ¡Y ya está todo instalado!</strong> No necesitas abrir ninguna consola ni ejecutar comandos para la instalación. Una vez abierta la carpeta en Antigravity IDE, la IA ya conoce las reglas de trabajo y puedes empezar a chatear directamente con ella.
        </div>
    </div>

    <h2>4.3 Catálogo Evolutivo de Mejoras del Ecosistema</h2>
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
                <td><strong>Índice General Estructurado</strong></td>
                <td>Navegación / Doc</td>
                <td>Índice jerárquico al inicio del documento con mantenimiento obligatorio ante cada nueva mejora.</td>
            </tr>
            <tr>
                <td><strong>Fase 0: Instalación desde Cero</strong></td>
                <td>Didáctica / Setup</td>
                <td>Guía de descarga en antigravity.google con selección de pestañas (Apple vs Windows/Linux), aviso contra CLI e inicio con Gemini.</td>
            </tr>
            <tr>
                <td><strong>Guía Única Señalizada</strong></td>
                <td>Gobernanza</td>
                <td>Fuente única de la verdad con Bloque Maestro (Profesor) y Bloque Alumno (Kit de Inicio).</td>
            </tr>
            <tr>
                <td><strong>Plantilla ZIP en 1 Clic</strong></td>
                <td>Despliegue</td>
                <td>Copia directa a Documentos y extracción en destino en vertical sin rutas perdidas.</td>
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
    print("✅ HTML generado con Índice General exhaustivo y 5 Fases calibradas.", flush=True)

    try:
        subprocess.run(["textutil", "-convert", "docx", HTML_NOBLE, "-output", DOCX_NOBLE], check=True)
        shutil.copyfile(DOCX_NOBLE, DOCX_MONO)
        print("✅ DOCX generado y sincronizado.", flush=True)
    except Exception as e:
        print(f"⚠️ Aviso DOCX: {e}", flush=True)

def compilar_pdf_reportlab():
    """Genera la versión PDF ÍNTEGRA y EXTENSA sin resumir ni comprimir en ReportLab."""
    doc = SimpleDocTemplate(
        PDF_NOBLE,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=34,
        bottomMargin=38
    )

    PAGE_WIDTH = A4[0] - 72

    styles = getSampleStyleSheet()

    c_navy = colors.HexColor('#0F172A')
    c_blue = colors.HexColor('#0284C7')
    c_dark_blue = colors.HexColor('#0369A1')
    c_slate = colors.HexColor('#475569')

    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=15, leading=19, textColor=c_navy, alignment=0, spaceAfter=3)
    subtitle_style = ParagraphStyle('DocSubtitle', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=c_slate, spaceAfter=8)
    
    phase_style = ParagraphStyle('PhaseStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.5, leading=13, textColor=colors.HexColor('#FFFFFF'), backColor=c_blue, borderPadding=4, spaceBefore=10, spaceAfter=6, keepWithNext=True)
    h1_style = ParagraphStyle('H1', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=9, leading=12.5, textColor=c_dark_blue, spaceBefore=7, spaceAfter=3, keepWithNext=True)
    h2_style = ParagraphStyle('H2', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.2, leading=11.5, textColor=c_navy, spaceBefore=5, spaceAfter=2, keepWithNext=True)
    
    body_style = ParagraphStyle('Body', parent=styles['Normal'], fontName='Helvetica', fontSize=7.6, leading=11, textColor=colors.HexColor('#1E293B'), spaceAfter=4)
    bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], fontName='Helvetica', fontSize=7.4, leading=10.5, textColor=colors.HexColor('#1E293B'), leftIndent=12, spaceAfter=2.5)

    code_banner_style = ParagraphStyle('CodeBanner', parent=styles['Normal'], fontName='Courier', fontSize=6.5, leading=8.5, textColor=colors.HexColor('#F8FAFC'), backColor=colors.HexColor('#1E293B'), borderColor=colors.HexColor('#38BDF8'), borderWidth=1, borderPadding=4, spaceAfter=4)

    toc_title = ParagraphStyle('TT', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=c_navy, spaceAfter=4)
    toc_phase = ParagraphStyle('TP', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.6, leading=10, textColor=c_dark_blue, spaceBefore=2)
    toc_sub = ParagraphStyle('TS', parent=styles['Normal'], fontName='Helvetica', fontSize=7.1, leading=9.5, textColor=c_slate, leftIndent=10)

    danger_title = ParagraphStyle('DT', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, leading=10.5, textColor=colors.HexColor('#B91C1C'), spaceAfter=2)
    danger_body = ParagraphStyle('DB', parent=styles['Normal'], fontName='Helvetica', fontSize=7.4, leading=10.5, textColor=colors.HexColor('#7F1D1D'))
    sol_title = ParagraphStyle('ST', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, leading=10.5, textColor=colors.HexColor('#15803D'), spaceAfter=2)
    sol_body = ParagraphStyle('SB', parent=styles['Normal'], fontName='Helvetica', fontSize=7.4, leading=10.5, textColor=colors.HexColor('#14532D'), leftIndent=8, spaceAfter=2)

    feat_title = ParagraphStyle('FT', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.2, leading=11, textColor=c_dark_blue, spaceAfter=2)
    feat_body = ParagraphStyle('FB', parent=styles['Normal'], fontName='Helvetica', fontSize=7.4, leading=10.5, textColor=colors.HexColor('#0F172A'), spaceAfter=3)

    param_title = ParagraphStyle('PT', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.2, leading=11, textColor=colors.HexColor('#0F172A'), spaceAfter=2)
    param_body = ParagraphStyle('PB', parent=styles['Normal'], fontName='Helvetica', fontSize=7.4, leading=10.5, textColor=colors.HexColor('#334155'), spaceAfter=2)

    table_header = ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7, leading=9.5, textColor=c_navy)
    table_cell = ParagraphStyle('TC', parent=styles['Normal'], fontName='Helvetica', fontSize=6.8, leading=9.2, textColor=colors.HexColor('#334155'))
    table_cell_bold = ParagraphStyle('TCB', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=6.8, leading=9.2, textColor=c_navy)

    story = []

    # PORTADA Y CABECERA
    story.append(Paragraph("Guía de Arquitectura, Instalación y Gobernanza en Google Antigravity", title_style))
    story.append(Paragraph("<b>Manual Maestro y Fuente Única de la Verdad (Ecosistema Completo y Kit de Inicio para Alumnos)</b><br/>Desde la descarga del IDE y configuración del motor hasta la gobernanza agéntica y el trabajo desatendido en silencio en Mac o PC.", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_blue, spaceBefore=0, spaceAfter=6))

    # CITA
    p_quote = [
        Paragraph("«El verdadero peligro no es que la inteligencia artificial escriba código, sino que el humano pierda el gobierno sobre la arquitectura. El código se delega; el rigor, la jerarquía de ficheros, la memoria y la verificación jamás.»<br/><b>— Marco de Gobernanza Agéntica en Google Antigravity</b>", ParagraphStyle('QC', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=7.5, leading=10.5, textColor=colors.HexColor('#334155')))
    ]
    t_quote = Table([[p_quote]], colWidths=[PAGE_WIDTH])
    t_quote.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_quote)
    story.append(Spacer(1, 6))

    # ÍNDICE GENERAL DETALLADO (TOC)
    p_toc = [
        Paragraph("📑 ÍNDICE GENERAL DEL DOCUMENTO", toc_title),
        Paragraph("<b>FASE 0: DESCARGA E INSTALACIÓN (PARTIR DE CERO EN WINDOWS Y MAC)</b>", toc_phase),
        Paragraph("0.1 La Web Oficial y Selección Correcta del Instalador (Evitar la trampa del CLI)", toc_sub),
        Paragraph("0.2 Antigravity Desktop vs. Antigravity IDE (Por qué elegir el IDE)", toc_sub),
        Paragraph("0.3 Inicio de Sesión: El Consejo de Oro de la Cuenta de Google Gemini", toc_sub),
        Paragraph("0.4 Tabla Comparativa de Instalación Paso a Paso (Windows y macOS)", toc_sub),
        Spacer(1, 2),
        Paragraph("<b>FASE 1: FUNDAMENTOS Y ARQUITECTURA DEL ESPACIO DE TRABAJO</b>", toc_phase),
        Paragraph("1.1 De la Ilusión del 'Vibe Coding' a la Gobernanza Real", toc_sub),
        Paragraph("1.2 Las 4 D del Peligro de la IA y Nuestras Soluciones (Duplicación, Drift, Deluge, Deception)", toc_sub),
        Paragraph("1.3 Arquitectura Monorepo de Raíz Única: Cero Bloqueos de Permisos", toc_sub),
        Spacer(1, 2),
        Paragraph("<b>FASE 2: CONFIGURACIÓN BASE DEL MOTOR (SETTINGS DE ANTIGRAVITY)</b>", toc_phase),
        Paragraph("2.1 Análisis Exhaustivo de Parámetros del Motor (Execution Policy, Sandbox, Layout, Sleep)", toc_sub),
        Paragraph("2.2 Primacía Jerárquica de AGENTS.md sobre la Interfaz Visual", toc_sub),
        Spacer(1, 2),
        Paragraph("<b>FASE 3: EL NÚCLEO DE PROTOCOLOS DE GOBERNANZA Y CAPACIDADES AGÉNTICAS (AGENTS.MD)</b>", toc_phase),
        Paragraph("3.1 Protocolo de Oro: Cero-Submits Absoluto", toc_sub),
        Paragraph("3.2 El Patrón Operativo Maestro: Trabajo en Silencio y Uso de la Consola (¿Cuándo, Cómo y Por Qué?)", toc_sub),
        Paragraph("3.3 Protocolo Cognitivo Elephant-Goldfish (Memoria vs. Auditoría Virgen)", toc_sub),
        Paragraph("3.4 Contador Correlativo de Comandos y Trazabilidad Cronológica", toc_sub),
        Paragraph("3.5 La Triple Salvaguarda Pedagógica (+65) y Cero Código Intermedio", toc_sub),
        Paragraph("3.6 Orquestación Concurrente: Subagentes Efímeros en Paralelo (invoke_subagent / kill)", toc_sub),
        Paragraph("3.7 Visualización Directa y Paneles Vivos: Generative UI en Antigravity (<agent-embed>)", toc_sub),
        Paragraph("3.8 Pipeline de Despliegue Continuo: GitHub como BKP Blindado y Servidor Web Global (GitHub Pages)", toc_sub),
        Paragraph("3.9 Arquitectura Modular de Skills (SKILL.md): Automatización sin Prompts Largos", toc_sub),
        Spacer(1, 2),
        Paragraph("<b>FASE 4: PUESTA EN MARCHA DEL ESPACIO DE TRABAJO (PLANTILLA EN 1 CLIC)</b>", toc_phase),
        Paragraph("4.1 La Solución Definitiva: Plantilla Universal en 1 Clic (WORKSPACE-ANTIGRAVITY-PLANTILLA.zip)", toc_sub),
        Paragraph("4.2 Instalación Paso a Paso en tu Ordenador (Windows y macOS)", toc_sub),
        Paragraph("4.3 Catálogo Evolutivo de Mejoras del Ecosistema", toc_sub)
    ]
    t_toc = Table([[p_toc]], colWidths=[PAGE_WIDTH])
    t_toc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_toc)
    story.append(Spacer(1, 8))

    # FASE 0: DESCARGA E INSTALACIÓN
    story.append(Paragraph("FASE 0: DESCARGA E INSTALACIÓN (PARTIR DE CERO EN WINDOWS Y MAC)", phase_style))
    story.append(Paragraph("0.1 La Web Oficial y Selección Correcta del Instalador (Evitar la trampa del CLI)", h1_style))
    story.append(Paragraph("Para empezar desde cero con Google Antigravity en tu ordenador (Mac o PC), acudimos a la web oficial: <b><code>antigravity.google</code></b>. Al pulsar el botón de descarga principal, la plataforma muestra distintas opciones y pestañas que pueden confundir al usuario novato:", body_style))
    story.append(Paragraph("• <b>Cuidado con 'Apple Antigravity CLI':</b> Por defecto, si el sistema detecta macOS o si se pulsa sin mirar, puede ofrecer la versión de consola pura (CLI). <i>Esta no es la versión que queremos</i>; la CLI no tiene interfaz visual y está pensada solo para scripts de servidor.", bullet_style))
    story.append(Paragraph("• <b>Cambio de Pestaña según tu Sistema Operativo:</b> Si estás en un ordenador con <b>Windows</b> o con <b>Linux</b>, es obligatorio fijarse en las pestañas superiores de la página de descarga y hacer clic en la pestaña <b>'Windows'</b> (o 'Linux') para que se descargue el instalador ejecutable <code>.exe</code> adecuado.", bullet_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("0.2 Antigravity Desktop vs. Antigravity IDE (Por qué elegir el IDE)", h1_style))
    story.append(Paragraph("Google ofrece dos interfaces para interactuar con la plataforma en tu ordenador (Mac o PC):", body_style))
    story.append(Paragraph("• <b>Antigravity Desktop (App de Escritorio):</b> Es una aplicación visual muy básica, orientada casi exclusivamente a chatear. <i>Inconveniente:</i> Oculta el árbol de carpetas, no muestra las diferencias exactas de código (diffs rojos/verdes) y no tiene consola de ejecución integrada, quedándose corta de inmediato.", bullet_style))
    story.append(Paragraph("• <b>Antigravity IDE (Entorno Integrado basado en VS Code - NUESTRA ELECCIÓN OFICIAL):</b> Es la herramienta profesional definitiva. En una única pantalla integra el explorador de archivos a la izquierda, el editor de código central, la terminal de comandos abajo y el copiloto de IA a la derecha.", bullet_style))
    
    p_rec = [
        Paragraph("💡 <b>Recomendación Oficial del Curso:</b> Instala siempre <b>Antigravity IDE</b>. Aunque seas principiante, verás en tiempo real cómo la IA crea tus carpetas y archivos en el disco, teniendo el 100% del control visual de lo que ocurre en tu ordenador (Mac o PC).", sol_body)
    ]
    t_rec = Table([[p_rec]], colWidths=[PAGE_WIDTH])
    t_rec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0FDF4')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#4ADE80')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_rec)
    story.append(Spacer(1, 4))

    story.append(Paragraph("0.3 Inicio de Sesión: El Consejo de Oro de la Cuenta de Google Gemini", h1_style))
    story.append(Paragraph("Una vez descargada e instalada la aplicación en tu ordenador (sea ejecutando el <code>.exe</code> en Windows o arrastrando el <code>.dmg</code> a Aplicaciones en Mac), al abrir Antigravity por primera vez te pedirá iniciar sesión:", body_style))
    
    p_gemini = [
        Paragraph("💡 <b>Consejo Crucial de Rendimiento:</b> Al pulsar en <i>'Continuar con Google'</i>, <b>inicia sesión con la cuenta de Google con la que ya pagues una suscripción de Gemini (Google One AI Premium o Gemini Advanced)</b> si dispones de ella. Al vincular una cuenta de pago, Antigravity te otorgará una cuota de uso, velocidad de respuesta y límites de tokens drásticamente superiores para trabajar con modelos avanzados (Gemini Pro) sin interrupciones.", sol_body)
    ]
    t_gemini = Table([[p_gemini]], colWidths=[PAGE_WIDTH])
    t_gemini.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0FDF4')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#4ADE80')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_gemini)
    story.append(Spacer(1, 4))

    story.append(Paragraph("0.4 Tabla Comparativa de Instalación Paso a Paso", h1_style))
    table_inst_data = [
        [Paragraph("Sistema Operativo", table_header), Paragraph("Instalador", table_header), Paragraph("Pasos de Instalación", table_header)],
        [Paragraph("<b>Windows 10 / 11</b>", table_cell_bold), Paragraph("<code>.exe</code> (x64)", table_cell), Paragraph("1. Ejecuta el archivo descargado.<br/>2. Sigue el asistente ('Siguiente', 'Instalar').<br/>3. Abre <b>Google Antigravity</b> e inicia sesión con tu cuenta de Google.", table_cell)],
        [Paragraph("<b>macOS (Apple Silicon / Intel)</b>", table_cell_bold), Paragraph("<code>.dmg</code> (Universal)", table_cell), Paragraph("1. Abre el archivo <code>.dmg</code> descargado.<br/>2. Arrastra el icono de Antigravity a <b>Aplicaciones</b>.<br/>3. Abre la app desde Spotlight o Launchpad e inicia sesión.", table_cell)]
    ]
    t_inst = Table(table_inst_data, colWidths=[110, 85, 328.27])
    t_inst.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_inst)
    story.append(Spacer(1, 8))

    # FASE 1: FUNDAMENTOS Y ARQUITECTURA
    story.append(Paragraph("FASE 1: FUNDAMENTOS Y ARQUITECTURA DEL ESPACIO DE TRABAJO", phase_style))
    story.append(Paragraph("1.1 De la Ilusión del 'Vibe Coding' a la Gobernanza Real", h1_style))
    story.append(Paragraph("En la era del desarrollo con modelos generativos avanzados, programar parece haberse convertido en un ejercicio casi instantáneo. Con solo describir intenciones en lenguaje natural ('vibe coding'), es posible generar cientos de líneas de código en minutos. Sin embargo, la velocidad desprovista de arquitectura desemboca en una trampa crítica: <b>la falsa ilusión de perfección</b>. Un modelo generativo optimiza probabilísticamente para la respuesta inmediata del turno actual, perdiendo de vista el ciclo de vida del repositorio. Sin salvaguardas explícitas, el código resultante acumula silenciosamente cuatro patologías conocidas como <b>Las 4 D del peligro de la IA</b>.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("1.2 Las 4 D del Peligro de la IA y Nuestras Soluciones de Gobernanza", h1_style))

    def make_detailed_4d_box(num_str, title_str, danger_text, sol_bullets):
        p_danger = [
            Paragraph(f"⚠️ {num_str} PELIGRO DE LA IA: {title_str.upper()}", danger_title),
            Paragraph(danger_text, danger_body)
        ]
        t_danger = Table([[p_danger]], colWidths=[PAGE_WIDTH])
        t_danger.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FEF2F2")),
            ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#F87171")),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ]))

        p_sol = [Paragraph("🛡️ NUESTRAS SOLUCIONES DE GOBERNANZA EN ANTIGRAVITY:", sol_title)]
        for b in sol_bullets:
            p_sol.append(Paragraph(f"• {b}", sol_body))
        t_sol = Table([[p_sol]], colWidths=[PAGE_WIDTH])
        t_sol.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0FDF4")),
            ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#4ADE80")),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ]))
        return KeepTogether([t_danger, Spacer(1, 2), t_sol, Spacer(1, 4)])

    story.append(make_detailed_4d_box(
        "1.", "DUPLICACIÓN (Duplication)",
        "Al solicitar una nueva funcionalidad, el modelo tiende por impulso probabilístico a reescribir funciones de utilidad, estilos y lógica que ya existían en otros archivos del proyecto. Esto fragmenta la base de código, multiplica los puntos de fallo y hace inmanejable el mantenimiento futuro.",
        [
            "<b>Documento Vivo Centralizado (ESTADO_GLOBAL_PROYECTOS.md):</b> Memoria técnica compartida y relevo obligatorio. Antes de codificar, el agente consulta este inventario para identificar y reutilizar utilidades existentes sin duplicar.",
            "<b>Librerías Base Reutilizables y Scripts Maestros:</b> Estandarización en módulos centrales (ej. generadores de bitácora y scripts batch) en lugar de dispersar código repetido.",
            "<b>Curaduría y Desduplicación Estricta:</b> Como en el sistema de generación de fichas didácticas y mapas interactivos, donde se auditan previamente los componentes HUD, botones de navegación y estilos visuales para reutilizar siempre el estándar común y prohibir la creación de elementos redundantes o duplicados."
        ]
    ))

    story.append(make_detailed_4d_box(
        "2.", "DRIFT (Desviación / Deriva de Contexto)",
        "A medida que la conversación acumula miles de tokens, el modelo sufre fatiga cognitiva ('ceguera de contexto'). Se aleja sutilmente de las reglas fundacionales, altera estructuras de carpetas acordadas, inventa abreviaturas o relaja los estándares de calidad.",
        [
            "<b>Protocolo Elephant-Goldfish:</b> El 'Elefante' (coordinador) mantiene la memoria histórica y planifica; el 'Goldfish' (subagente efímero) nace con mente virgen para auditar el código contra una lista de control estricta y se destruye inmediatamente sin dejar procesos residuales.",
            "<b>Catálogos Canónicos Estrictos:</b> Prohibición absoluta de abreviaturas inventadas. En NASA Eyes se exige el ID exacto (<code>sc_roman_space_telescope</code>, nunca <code>sc_roman</code>); en simuladores científicos, identificadores formales contrastados en bases de datos abiertas.",
            "<b>Contador Correlativo de Comandos y Trazabilidad:</b> Mantenimiento estricto de una numeración secuencial de comandos (<code>[COMANDO XX]</code>) para anclar cada avance en la bitácora técnica sin saltos ni desviaciones."
        ]
    ))

    story.append(make_detailed_4d_box(
        "3.", "DELUGE (Diluvio de Código y Sobre-Ingeniería)",
        "Propensión del modelo a 'vomitar' cientos de líneas de código superfluo, proponiendo frameworks pesados, dependencias de terceros (npm, librerías pip ajenas) o arquitecturas mastodónticas para resolver problemas que se solucionan con pocas líneas nativas.",
        [
            "<b>Regla de Cero Herramientas Nuevas ni Instalaciones Externas:</b> Prohibición radical de instalar paquetes de terceros. Se opera exclusivamente con herramientas nativas del sistema operativo (Mac o PC) y Python estándar (<code>urllib</code>, <code>xml</code>, scripts nativos).",
            "<b>Diferenciación Clara de Motores 3D:</b> Prohibición de Babylon.js en simuladores anatómicos/médicos de IA (donde se exige Three.js limpio o Canvas fotográfico hiperrealista) mientras se reserva y mantiene Babylon.js al 100% como motor oficial en Robótica (aprovechando sus shaders y física Havok).",
            "<b>La Triple Salvaguarda Pedagógica (+65):</b> Cero código intermedio para los alumnos senior. Se entregan micro-aplicaciones autónomas de 1 página que funcionan al 100% con doble clic en cualquier navegador sin servidor ni dependencias."
        ]
    ))

    story.append(make_detailed_4d_box(
        "4.", "DECEPTION (Engaño / Ilusión de Funcionamiento)",
        "El código compila y la interfaz luce profesional, pero internamente es un cascarón vacío: datos estáticos inventados, APIs bloqueadas por seguridad o sondas históricas orbitando la Tierra en lugar de su planeta destino por omitir el parámetro temporal.",
        [
            "<b>Obligación de Autocomprobación Previa y Poda Temprana:</b> Si un activo, telemetría o malla 3D no existe o no se mueve en el motor real, no se maquilla ni se inventa: se poda de raíz y se sustituye de inmediato por un activo 100% verificado.",
            "<b>Calibración Temporal de Sondas Históricas:</b> Inyección obligatoria de marcas temporales UTC (<code>time=YYYY-MM-DD...</code>) para ubicar las sondas en su fecha activa y planeta real.",
            "<b>Blindaje ante Restricciones del Navegador:</b> Supresión de enlaces directos a WhatsApp (<code>api.whatsapp.com</code>) bloqueados por la política COOP de Safari, adoptando la publicación nativa en Gemini Canvas.",
            "<b>Copia de Respaldo Garantizada (BKP Oficial):</b> Botón de respaldo local probado en cada mapa interactivo para asegurar que el 100% de los alumnos disfrute de la experiencia completa sin atascos de red."
        ]
    ))

    story.append(Paragraph("1.3 Arquitectura Monorepo de Raíz Única: Cero Bloqueos de Permisos", h1_style))
    story.append(Paragraph("Para erradicar de raíz el problema clásico de permisos, fragmentación y pérdida de contexto entre carpetas dispersas, todo el ecosistema está estructurado bajo una <b>única carpeta raíz (Monorepo Workspace)</b>. Al situar la raíz de Antigravity en este directorio padre en tu ordenador (Mac o PC), <b>el agente opera permanentemente dentro del mismo espacio de trabajo reconocido</b>, lo que permite el acceso universal a todos los submódulos sin necesidad de solicitar permisos especiales de <i>Non-Workspace File Access</i> ni disparar ventanas de confirmación.", body_style))
    story.append(Spacer(1, 8))

    # FASE 2: CONFIGURACIÓN BASE DEL MOTOR
    story.append(Paragraph("FASE 2: CONFIGURACIÓN BASE DEL MOTOR (SETTINGS DE ANTIGRAVITY)", phase_style))
    story.append(Paragraph("2.1 Análisis Exhaustivo de Parámetros del Motor", h1_style))
    story.append(Paragraph("A diferencia de interfaces conversacionales estándar, Google Antigravity es un entorno de desarrollo agéntico gobernado por parámetros técnicos explícitos:", body_style))

    def make_param_card(num_str, title_str, text_str):
        p_card = [
            Paragraph(f"⚙️ <b>{num_str} {title_str}</b>", param_title),
            Paragraph(text_str, param_body)
        ]
        t_card = Table([[p_card]], colWidths=[PAGE_WIDTH])
        t_card.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
            ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#CBD5E1')),
            ('TOPPADDING', (0,0), (-1,-1), 2.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ]))
        return KeepTogether([t_card, Spacer(1, 2.5)])

    story.append(make_param_card(
        "Parámetro 1:", "Política de Ejecución de Terminal (Tool Execution Policy)",
        "Determina el nivel de autonomía requerido ante cada comando. Nuestro estándar es <code>proceed-in-sandbox</code>: el agente ejecuta tareas de forma 100% desatendida y silenciosa mientras trabaje dentro del Sandbox aislado del proyecto. Si una orden solicita saltar el sandbox (<code>BypassSandbox: true</code>), el sistema operativo activa de inmediato el freno de seguridad y lanza la confirmación humana."
    ))

    story.append(make_param_card(
        "Parámetro 2:", "Modo Sandbox y Aislamiento de Procesos (Terminal Sandbox)",
        "Define la jaula de contención. En modo estándar (<code>BypassSandbox: false</code>), el agente tiene permisos plenos de lectura y escritura dentro de la carpeta raíz del proyecto y directorios temporales, pero no puede acceder a otras carpetas privadas del Mac o PC ni alterar la red. Esto permite auto-aprobar comandos sin intervención del usuario, garantizando Cero-Submits."
    ))

    story.append(make_param_card(
        "Parámetro 3:", "Acceso a Archivos Fuera del Workspace (Non-Workspace File Access)",
        "Regula si el agente puede leer o alterar archivos fuera de la ruta inicial (<code>allow</code>, <code>ask</code>, <code>deny</code>). Gracias a nuestra Arquitectura de Raíz Única, el 100% de los proyectos cuelgan del mismo árbol padre: el agente jamás necesita salir del workspace, eliminando alertas de cruce de carpetas."
    ))

    story.append(make_param_card(
        "Parámetro 4:", "Acceso a Internet y Lista Blanca de Navegación (Internet Access)",
        "Controla las peticiones de red. Configurado en modo lectura y consulta de repositorios científicos (NASA, USGS, Wikimedia Commons) para obtener datos reales, restringiendo el control invasivo mediante Chrome DevTools que dispara alertas en macOS o Windows."
    ))

    story.append(make_param_card(
        "Parámetro 5:", "Selección de Modelo y Enrutamiento Inteligente (Model Selection)",
        "Permite alternar entre motores neuronales: <b>Gemini Pro</b> para el Elefante (coordinador con visión holística, razonamiento profundo y arquitectura) y <b>Gemini Flash</b> para subagentes rápidos (Goldfish para tareas atómicas y auditorías instantáneas)."
    ))

    story.append(make_param_card(
        "Parámetro 6:", "Jerarquía de Reglas del Proyecto (AGENTS.md y GEMINI.md)",
        "Las reglas ubicadas en los archivos <code>AGENTS.md</code> y <code>GEMINI.md</code> de la raíz del workspace tienen <b>prioridad jerárquica absoluta</b> sobre cualquier menú visual de la aplicación. Aquí residen los compromisos innegociables: Cero-Submits, Cuadro Matutino, Contador Correlativo y Despliegue a GitHub."
    ))
    story.append(Spacer(1, 6))

    # FASE 3: EL NÚCLEO DE PROTOCOLOS Y CAPACIDADES AGÉNTICAS
    story.append(Paragraph("FASE 3: EL NÚCLEO DE PROTOCOLOS DE GOBERNANZA Y CAPACIDADES AGÉNTICAS (AGENTS.MD)", phase_style))
    story.append(Paragraph("3.1 Protocolo de Oro: Cero-Submits Absoluto", h1_style))
    story.append(Paragraph("Prohibición radical de ventanas emergentes de confirmación interactiva en el editor (<code>RequestFeedback: false</code>). El asistente trabaja de manera 100% desatendida sin detener la ejecución en botones de aprobación intermedia.", body_style))

    story.append(Paragraph("3.2 El Patrón Operativo Maestro: Trabajo en Silencio y Uso de la Consola", h1_style))
    story.append(Paragraph("Uno de los mayores hallazgos metodológicos de nuestro ecosistema es la articulación del <b>flujo de trabajo 100% desatendido</b>: el agente realiza todo el esfuerzo técnico de forma silenciosa e invisible dentro del entorno y, únicamente al concluir con éxito, entrega al usuario un <b>bloque de comando único numerado para la terminal externa</b>.", body_style))

    p_feat_silence = [
        Paragraph("<b>¿EN QUÉ MOMENTO SE USA, CÓMO OPERA Y POR QUÉ SE DISEÑÓ ESTA ARQUITECTURA?</b>", feat_title),
        Spacer(1, 2),
        Paragraph("<b>1. ¿En qué momento se usa?</b> Se aplica de forma obligatoria en todas las tareas operativas del sistema: creación y edición de fichas didácticas, actualización de bitácoras, reescritura de scripts en Python, modificación de mapas HTML y despliegues.", feat_body),
        Paragraph("<b>2. ¿Cómo lo usamos? (Mecánica Técnica en Dos Fases):</b>", feat_body),
        Paragraph("• <i>Fase 1: Trabajo en Silencio en el Sandbox (Lado Asistente):</i> Edición con herramientas nativas (<code>read_file</code>, <code>edit_file</code>, <code>write_file</code>) y comandos atómicos dentro del Sandbox (<code>BypassSandbox: false</code>). Cero charlas intermedias, cero explicaciones redundantes y cero ventanas de 'Submit'.", feat_body),
        Paragraph("• <i>Fase 2: Entrega del Comando Único al Final (Lado Usuario):</i> Un único bloque bash numerado (ej. <code>[COMANDO 208]</code>) protegido con cabecera y pie visibles mediante <code>echo</code> y sincronización automática con GitHub.", feat_body),
        Paragraph("<b>3. ¿Por qué lo usamos? (Beneficios de Gobernanza y Control Humano):</b>", feat_body),
        Paragraph("• <i>Eliminación de Fricción Cognitiva:</i> La IA hace el trabajo pesado sin obligar al usuario a autorizar 20 ventanas intermedias.", feat_body),
        Paragraph("• <i>Soberanía y Control Humano Real:</i> El usuario retiene el poder de ejecución en la terminal externa de su ordenador (Mac o PC).", feat_body),
        Paragraph("• <i>Cero Fallos de Despliegue en GitHub:</i> <code>git add</code>, <code>git commit</code> y <code>git push origin main</code> se ejecutan siempre de forma blindada.", feat_body),
        Paragraph("• <i>Historial Cronológico Limpio:</i> La terminal del ordenador (Mac o PC) refleja la secuencia exacta de hitos registrados en la bitácora.", feat_body)
    ]
    t_feat_silence = Table([[p_feat_silence]], colWidths=[PAGE_WIDTH])
    t_feat_silence.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#38BDF8')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(KeepTogether([t_feat_silence, Spacer(1, 4)]))

    story.append(Paragraph("3.3 Protocolo Cognitivo Elephant-Goldfish", h1_style))
    story.append(Paragraph("Separación de roles para evitar la saturación de contexto: el <b>Elefante</b> (agente coordinador) mantiene la visión histórica, el calendario y los estándares; el <b>Goldfish</b> (subagente efímero) nace con mente limpia para auditar código contra una lista de control estricta y se autodestruye de inmediato sin dejar procesos residuales.", body_style))

    story.append(Paragraph("3.4 Contador Correlativo de Comandos y Trazabilidad Cronológica", h1_style))
    story.append(Paragraph("Mantenimiento estricto de una numeración secuencial de comandos (<code>[COMANDO XX]</code>) para anclar cada avance en la bitácora técnica sin saltos, colisiones ni pérdidas de trazabilidad.", body_style))

    story.append(Paragraph("3.5 La Triple Salvaguarda Pedagógica (+65) y Cero Código Intermedio", h1_style))
    story.append(Paragraph("Prohibición tajante de exponer al alumno senior a código fuente (HTML, JavaScript, Three.js). Los prompts generan aplicaciones interactivas en modo Canvas / Vista Previa directa, respaldadas por un botón BKP local probado en cada mapa.", body_style))

    story.append(Paragraph("3.6 Orquestación Concurrente: Subagentes Efímeros en Paralelo", h1_style))
    story.append(Paragraph("A medida que los proyectos crecen en complejidad, realizar tareas pesadas dentro de la misma conversación genera saturación cognitiva. La solución adoptada es la delegación en <b>subagentes paralelos efímeros</b> (<code>invoke_subagent</code>): se despliegan múltiples agentes independientes en paralelo con contexto 100% limpio y, tras verificar el resultado, se destruyen de inmediato (<code>manage_subagents: kill</code>) garantizando cero procesos zombi ni consumo residual de memoria.", body_style))

    story.append(Paragraph("3.7 Visualización Directa y Paneles Vivos: Generative UI en Antigravity", h1_style))
    story.append(Paragraph("Con <b>Generative UI</b>, Antigravity renderiza directamente componentes interactivos funcionales en el chat y en el panel lateral mediante <code>&lt;agent-embed src=\"...\"&gt;</code>, utilizando Tailwind CSS y tokens semánticos nativos (<code>var(--foreground)</code>, <code>var(--card)</code>, <code>var(--primary)</code>) con total adaptabilidad a temas claros y oscuros sin requerir ventanas de confirmación.", body_style))

    story.append(Paragraph("3.8 Pipeline de Despliegue Continuo: GitHub como BKP Blindado y Servidor Web Global (GitHub Pages)", h1_style))
    story.append(Paragraph("En nuestro flujo de trabajo, cada bloque ejecutable concluye obligatoriamente con la subida a GitHub (<code>git push origin main</code>), cumpliendo dos funciones vitales simultáneas: <b>1) Respaldo Automático e Inmutable (BKP en la Nube):</b> cada archivo, PDF y simulación interactiva queda archivado con historial commit a commit; ante cualquier fallo local o rotura de disco, el proyecto íntegro se restaura al 100% en segundos sin riesgo de pérdida. <b>2) Servidor Web Global Instantáneo (GitHub Pages):</b> mediante GitHub Pages, todo el repositorio se transforma de forma gratuita en un servidor web de producción donde cada archivo HTML interactivo o simulación 3D dispone de una URL pública inmediata, permitiendo que el profesor y los alumnos (+65) abran los recursos desde iPad, tablet o cualquier ordenador sin instalar servidores locales (Apache/Nginx) ni pagar hosting. Además, la inyección automática de parámetros anti-caché (<code>?v=...</code>) garantiza que los navegadores descarguen siempre la versión recién modificada al primer clic.", body_style))

    story.append(Paragraph("3.9 Arquitectura Modular de Skills (SKILL.md): Automatización sin Prompts Largos", h1_style))
    story.append(Paragraph("Mientras <code>AGENTS.md</code> fija las reglas globales permanentes del espacio de trabajo, los <b>Skills</b> encapsulan procedimientos especializados bajo demanda en archivos <code>SKILL.md</code> (<code>.agent/skills/</code>), eliminando la fatiga de escribir prompts largos y el olvido de restricciones (<i>Drift</i>). Cada Skill sigue una anatomía de 4 bloques: <b>1) Rol y Objetivo</b>, <b>2) Restricciones Negativas (<i>Never Do</i>)</b>, <b>3) Estructura de Entrada</b> y <b>4) Formato de Entrega</b>. Nuestro catálogo general previsto incluye <code>ficha-senior</code> (maquetación +65), <code>despliegue-seguro</code> (anti-caché y push), <code>nasa-eyes-calibrado</code> (mallas orbitales 3D) y <code>sincronizador-copilot</code> (réplica continua hacia la guía corporativa).", body_style))
    story.append(Spacer(1, 6))

    # FASE 4: PUESTA EN MARCHA DEL ESPACIO DE TRABAJO (PLANTILLA EN 1 CLIC)
    story.append(Paragraph("FASE 4: PUESTA EN MARCHA DEL ESPACIO DE TRABAJO (PLANTILLA EN 1 CLIC)", phase_style))

    p_kit_intro = [
        Paragraph("🟢 <b>MÉTODO OFICIAL Y UNIVERSAL (PROFESOR Y ALUMNOS)</b>", ParagraphStyle('UKIT', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11.5, textColor=colors.HexColor('#16A34A'))),
        Paragraph("<b>4.1 La Solución Definitiva: Plantilla Universal en 1 Clic</b>", h2_style),
        Paragraph("Tanto para el profesor como para los alumnos, la forma más limpia, rápida y 100% libre de errores para empezar en cualquier ordenador (Windows o Mac) es utilizar el archivo <b><code>WORKSPACE-ANTIGRAVITY-PLANTILLA.zip</code></b>.<br/>Nos olvidamos de comandos técnicos y consolas de instalación: este paquete comprimido <b>ya incluye todo configurado por dentro</b> (la estructura de carpetas, las reglas maestras de <code>AGENTS.md</code> y el archivo invisible <code>.agents/settings.json</code> con el Sandbox protegido preactivado). Solo hay que descomprimirlo y abrir la carpeta.", feat_body),
        Spacer(1, 2),
        Paragraph("<b>4.2 Instalación Paso a Paso en tu Ordenador (Windows y Mac)</b>", h2_style),
        Spacer(1, 1),
        Paragraph("<b>• SI USAS WINDOWS:</b>", ParagraphStyle('W1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.6, leading=10.5, textColor=colors.HexColor('#15803D'))),
        Paragraph("<b>Paso 1:</b> Ve a tu explorador de archivos y copia el ZIP descargado en tu carpeta <b>Documentos</b> (o en <code>C:\\</code>).", bullet_style),
        Paragraph("<b>Paso 2:</b> Clic derecho sobre el ZIP allí mismo y pulsa 'Extraer todo...'. Te quedará tu carpeta lista: <code>Documentos\\WORKSPACE-ANTIGRAVITY\\</code>.", bullet_style),
        Paragraph("<b>Paso 3:</b> Abre <b>Google Antigravity IDE</b>, pulsa en <b>File &gt; Open Folder...</b> y selecciona esa carpeta descomprimida.", bullet_style),
        Spacer(1, 2),
        Paragraph("<b>• SI USAS MAC:</b>", ParagraphStyle('M1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.6, leading=10.5, textColor=colors.HexColor('#15803D'))),
        Paragraph("<b>Paso 1:</b> Abre el Finder y copia el ZIP descargado en tu carpeta <b>Documentos</b> (o tu carpeta de usuario).", bullet_style),
        Paragraph("<b>Paso 2:</b> Doble clic sobre el ZIP allí mismo para descomprimirlo. Te quedará tu carpeta lista: <code>Documentos/WORKSPACE-ANTIGRAVITY/</code>.", bullet_style),
        Paragraph("<b>Paso 3:</b> Abre <b>Google Antigravity IDE</b>, pulsa en <b>File &gt; Open Folder...</b> y selecciona esa carpeta descomprimida.", bullet_style),
        Spacer(1, 3),
        Paragraph("🎉 <b>¡Y ya está todo instalado!</b> No necesitas abrir ninguna consola ni ejecutar comandos para la instalación. Una vez abierta la carpeta en Antigravity IDE, ya puedes empezar a chatear con la IA.", ParagraphStyle('Done', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.4, leading=10.5, textColor=colors.HexColor('#166534')))
    ]
    t_kit = Table([[p_kit_intro]], colWidths=[PAGE_WIDTH])
    t_kit.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0FDF4')),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#16A34A')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(KeepTogether([t_kit, Spacer(1, 5)]))

    # CATÁLOGO EVOLUTIVO
    story.append(Paragraph("4.3 Catálogo Evolutivo de Mejoras del Ecosistema", h1_style))
    table_cat_data = [
        [Paragraph("Hito / Versión", table_header), Paragraph("Ámbito", table_header), Paragraph("Impacto y Beneficio Operativo", table_header)],
        [Paragraph("<b>Índice General Estructurado</b>", table_cell_bold), Paragraph("Navegación / Doc", table_cell), Paragraph("Mantenimiento obligatorio de índice jerárquico al inicio del documento.", table_cell)],
        [Paragraph("<b>Fase 0: Setup desde Cero</b>", table_cell_bold), Paragraph("Setup / IDE", table_cell), Paragraph("Descarga en antigravity.google con pestañas Windows/Linux, alerta CLI e inicio Gemini.", table_cell)],
        [Paragraph("<b>Guía Única Señalizada</b>", table_cell_bold), Paragraph("Gobernanza", table_cell), Paragraph("Fuente única de la verdad con Bloque Maestro (Profesor) y Bloque Alumno (Kit).", table_cell)],
        [Paragraph("<b>Plantilla ZIP en 1 Clic</b>", table_cell_bold), Paragraph("Despliegue", table_cell), Paragraph("Copia directa a Documentos y extracción en destino en vertical sin rutas perdidas.", table_cell)],
        [Paragraph("<b>Monorepo Raíz Única</b>", table_cell_bold), Paragraph("Workspace", table_cell), Paragraph("Todas las áreas bajo una misma raíz para cero bloqueos de permisos.", table_cell)],
        [Paragraph("<b>Trabajo en Silencio</b>", table_cell_bold), Paragraph("Metodología", table_cell), Paragraph("Ejecución silenciosa en sandbox y entrega de bloque bash único al final.", table_cell)],
        [Paragraph("<b>Cero-Submits</b>", table_cell_bold), Paragraph("Flujo", table_cell), Paragraph("Cero ventanas emergentes de aprobación en el editor durante la sesión.", table_cell)],
        [Paragraph("<b>Elephant-Goldfish</b>", table_cell_bold), Paragraph("Memoria", table_cell), Paragraph("Auditoría con mente virgen y destrucción inmediata sin fugas de memoria.", table_cell)],
        [Paragraph("<b>Subagentes Paralelos</b>", table_cell_bold), Paragraph("Concurrencia", table_cell), Paragraph("Ejecución paralela para tareas pesadas sin saturar el hilo principal.", table_cell)],
        [Paragraph("<b>Generative UI Nativo</b>", table_cell_bold), Paragraph("Visualización", table_cell), Paragraph("Widgets y cuadros de mando interactivos embebidos sin exponer código.", table_cell)]
    ]
    t_cat = Table(table_cat_data, colWidths=[115, 90, 318.27])
    t_cat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_cat)

    doc.build(story, canvasmaker=NumberedCanvas)
    
    shutil.copyfile(PDF_NOBLE, PDF_MONO)
    shutil.copyfile(PDF_NOBLE, BKP_PDF_MONO)
    print("✅ PDF generado y sincronizado con versión íntegra extensa y 5 Fases calibradas.", flush=True)

if __name__ == "__main__":
    compilar_html()
    compilar_pdf_reportlab()
