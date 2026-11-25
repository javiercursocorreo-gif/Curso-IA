#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_arquitectura_soluciones_antigravity.py
Genera la Guía Maestra Técnica y Didáctica:
'SOLUCIONES DE ARQUITECTURA Y GOBERNANZA EN GOOGLE ANTIGRAVITY'
(Jerarquía Monorepo Raíz, Las 4 D del Vibe Coding, Configuración y Parámetros del Motor,
Patrón de Trabajo en Silencio y Entrega de Comando Terminal Final,
Subagentes en Paralelo, Generative UI y Catálogo Evolutivo de Mejoras)

Destino:
CURSO-IA/CLASES/7. MAPA_GESTION_PROYECTO_CON_IA/
Archivos generados:
1. ARQUITECTURA_Y_SOLUCIONES_ANTIGRAVITY.html (y copia de compatibilidad LAS_4D_DEL_CODIGO_IA_Y_NUESTRAS_SOLUCIONES.html)
2. ARQUITECTURA_Y_SOLUCIONES_ANTIGRAVITY.pdf (y copia de compatibilidad LAS_4D_DEL_CODIGO_IA_Y_NUESTRAS_SOLUCIONES.pdf)
3. ARQUITECTURA_Y_SOLUCIONES_ANTIGRAVITY.docx (mediante textutil nativo)
"""

import os
import sys
import subprocess
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

TARGET_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/7. MAPA_GESTION_PROYECTO_CON_IA"
PDF_PATH = os.path.join(TARGET_DIR, "ARQUITECTURA_Y_SOLUCIONES_ANTIGRAVITY.pdf")
HTML_PATH = os.path.join(TARGET_DIR, "ARQUITECTURA_Y_SOLUCIONES_ANTIGRAVITY.html")
DOCX_PATH = os.path.join(TARGET_DIR, "ARQUITECTURA_Y_SOLUCIONES_ANTIGRAVITY.docx")

BKP_PDF_PATH = os.path.join(TARGET_DIR, "LAS_4D_DEL_CODIGO_IA_Y_NUESTRAS_SOLUCIONES.pdf")
BKP_HTML_PATH = os.path.join(TARGET_DIR, "LAS_4D_DEL_CODIGO_IA_Y_NUESTRAS_SOLUCIONES.html")

class NumberedCanvas(canvas.Canvas):
    """Añade numeración de páginas profesional 'Página X de Y' y pie de página."""
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
        
        # Línea separadora de pie
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(36, 32, A4[0] - 36, 32)
        
        # Texto pie de página
        left_text = "CURSO-IA • Monográfico 6: Gestión del Proyecto con IA — Arquitectura y Protocolos de Gobernanza"
        page_text = f"Página {self._pageNumber} de {page_count}"
        
        self.drawString(36, 22, left_text)
        self.drawRightString(A4[0] - 36, 22, page_text)
        self.restoreState()

def compilar_html():
    """Genera la versión HTML exhaustiva con jerarquía monorepo, trabajo en silencio y comando terminal."""
    html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Soluciones de Arquitectura y Gobernanza en Google Antigravity</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; line-height: 1.6; color: #1e293b; max-width: 960px; margin: 40px auto; padding: 0 24px; }
        h1 { color: #0f172a; border-bottom: 2px solid #0284c7; padding-bottom: 12px; font-size: 2.1rem; }
        h2 { color: #0369a1; margin-top: 36px; border-left: 4px solid #0284c7; padding-left: 12px; font-size: 1.4rem; }
        h3 { color: #0f172a; margin-top: 22px; font-size: 1.15rem; }
        .danger-box { background: #fef2f2; border: 1px solid #f87171; border-radius: 8px; padding: 15px 18px; margin: 15px 0; }
        .solution-box { background: #f0fdf4; border: 1px solid #4ade80; border-radius: 8px; padding: 15px 18px; margin: 15px 0; }
        .feature-box { background: #f8fafc; border: 1px solid #38bdf8; border-radius: 8px; padding: 15px 18px; margin: 15px 0; }
        .param-box { background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px 20px; margin: 16px 0; }
        .quote-box { background: #f8fafc; border-left: 4px solid #64748b; padding: 14px 20px; font-style: italic; margin: 20px 0; font-size: 1.05rem; }
        .tree-box { background: #0f172a; color: #38bdf8; padding: 16px 20px; border-radius: 8px; font-family: ui-monospace, Menlo, Monaco, "Cascadia Mono", monospace; font-size: 0.88rem; line-height: 1.5; margin: 15px 0; overflow-x: auto; }
        .code-banner { background: #1e293b; color: #f8fafc; padding: 14px 18px; border-radius: 6px; font-family: ui-monospace, Menlo, Monaco, monospace; font-size: 0.85rem; line-height: 1.45; margin: 12px 0; border-left: 4px solid #38bdf8; }
        table { width: 100%; border-collapse: collapse; margin: 25px 0; font-size: 0.92rem; }
        th, td { border: 1px solid #cbd5e1; padding: 10px 14px; text-align: left; }
        th { background: #f1f5f9; color: #0f172a; font-weight: bold; }
        code { background: #e2e8f0; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 0.9em; }
        .badge { display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; margin-bottom: 6px; }
        .badge-danger { background: #fee2e2; color: #b91c1c; }
        .badge-solution { background: #dcfce7; color: #15803d; }
        .badge-feature { background: #e0f2fe; color: #0369a1; }
        .badge-param { background: #f1f5f9; color: #475569; }
    </style>
</head>
<body>
    <h1>Soluciones de Arquitectura y Gobernanza en Google Antigravity</h1>
    <p><strong>Ecosistema Formativo y Personal • Monográfico 6: Gestión del Proyecto con IA</strong><br>
    <em>Guía maestra de blindaje agéntico, prevención del 'Vibe Coding', orquestación concurrente, calibración de parámetros y catálogo evolutivo de mejoras.</em></p>

    <div class="quote-box">
        «El verdadero peligro no es que la inteligencia artificial escriba código, sino que el humano pierda el gobierno sobre la arquitectura. El código se delega; el rigor, la jerarquía de ficheros, la memoria y la verificación jamás.»<br>
        <strong>— Marco de Gobernanza Agéntica en Google Antigravity</strong>
    </div>

    <h2>1. Jerarquía de Carpetas y Arquitectura de Raíz Única (Monorepo Workspace)</h2>
    <p>Para evitar de raíz el problema clásico de permisos, fragmentación y pérdida de contexto entre carpetas dispersas, todo el ecosistema formativo, técnico, musical y de seguimiento está estructurado bajo una <strong>única carpeta raíz (Monorepo Workspace)</strong> en macOS iCloud Drive: <code>/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/</code>.</p>
    
    <p>Al situar la raíz de Antigravity en este directorio padre, <strong>el agente opera permanentemente dentro del mismo espacio de trabajo reconocido</strong>, lo que permite el acceso universal a todos los módulos sin necesidad de solicitar permisos especiales de <em>Non-Workspace File Access</em> ni disparar ventanas de confirmación.</p>

    <div class="tree-box">
📁 CLASES DE TECNOLOGÍA/ [RAÍZ ÚNICA DEL WORKSPACE EN ANTIGRAVITY]
├── 📄 AGENTS.md (Protocolo de Oro, Cero-Submits, Reglas de Ejecución y Estándares)
├── 📄 GEMINI.md (Espejo Canónico y Directivas Operativas de Modelos)
├── 📄 ESTADO_GLOBAL_PROYECTOS.md (Inventario Técnico Centralizado y Memoria Viva)
│
├── 📁 CURSO-IA/ (Inteligencia Artificial para Seniors 65+)
│   ├── 📁 CLASES/ (Fichas, Prompts, Monográficos 1 a 6 y Mapas de Sesión)
│   │   ├── 📁 2. INTRODUCCION_NLM/ (NotebookLM, Talleres y Libros)
│   │   ├── 📁 6. NASA_Y_EXPLORACION_ESPACIAL_CON_IA/ (NASA Eyes 3D, Fobos/Deimos)
│   │   └── 📁 7. MAPA_GESTION_PROYECTO_CON_IA/ (Gobernanza, Vibe Coding, 4D, Antigravity)
│   └── 📁 00. SCRIPTS_PYTHON/ (Compiladores nativos de PDFs, comprobadores y utilidades)
│
├── 📁 CURSO-ROBOTICA-V2/ (Robótica, Mecatrónica y Androides)
│   ├── 📁 BLOQUE-1 a 6/ (Teoría reducida a 14 slides adaptada a seniors)
│   ├── 📁 3.PRACTICAS/ (Simulaciones y laboratorios en Babylon.js oficial)
│   └── 📁 SCRIPTS/ (Automatización de presentaciones PPTX y exportadores)
│
├── 📁 CURSO-ROBOTICA-IA-COMUN/ (Infraestructura y Métricas Compartidas)
│   └── 📁 SEGUIMIENTO DEL CALENDARIO/ (BITACORA_SEGUIMIENTO_CLASES.md, generador Excel nativo)
│
├── 📁 CURSO_MUSICA/ (Web MIDI, Banco Maestro MSB 33 y Korg EK-50)
│   ├── 📁 PARTITURAS/ (Carruseles de partituras depuradas)
│   └── 📁 SCRIPTS/ (Generadores de sonido HUD y reglas de 8 instrumentos únicos)
│
└── 📁 IA TEMAS VARIOS/ (Gestión Personal, Salud y Utilidades Administrativas)
    ├── 📁 ASISTENTE PERSONAL/
    ├── 📁 SEGUMINENTO MEDICINAS JAVI/ (Informes médicos nativos de 1 página)
    └── 📁 ESPALDA/ (Seguimiento clínico y tablas de ejercicios)
    </div>

    <h2>2. Contexto: El Fenómeno del 'Vibe Coding' y la Necesidad de Gobernanza</h2>
    <p>En la era del desarrollo con modelos generativos avanzados (ChatGPT, Claude, Gemini, Antigravity), programar se ha convertido en un flujo acelerado. Es posible generar cientos o miles de líneas de código en minutos simplemente transmitiendo intenciones ("vibe coding").</p>
    <p>Sin embargo, la velocidad desprovista de arquitectura desemboca en una trampa crítica: <strong>la falsa ilusión de perfección</strong>. Un modelo generativo optimiza probabilísticamente para la respuesta inmediata del turno actual, perdiendo de vista el ciclo de vida del repositorio. Sin salvaguardas explícitas, el código resultante acumula silenciosamente cuatro patologías conocidas como <strong>Las 4 D del peligro de la IA</strong> (<em>Duplicación</em>, <em>Drift</em>, <em>Deluge</em> y <em>Deception</em>).</p>

    <h2>3. Patología 1: DUPLICACIÓN (Duplication)</h2>
    <div class="danger-box">
        <span class="badge badge-danger">El Peligro en la IA</span><br>
        <strong>⚠️ Reinvención constante de la rueda:</strong> Al solicitar una nueva funcionalidad, el agente tiende por impulso probabilístico a reescribir funciones de utilidad, estilos y lógica que ya existían en otros archivos del proyecto. Esto fragmenta la base de código, multiplica los puntos de fallo y hace inmanejable el mantenimiento futuro.
    </div>
    <div class="solution-box">
        <span class="badge badge-solution">Soluciones en la Arquitectura</span><br>
        <strong>🛡️ Gobernanza Antigravity:</strong>
        <ul>
            <li><strong>Documento Vivo Centralizado (<code>ESTADO_GLOBAL_PROYECTOS.md</code>):</strong> Memoria técnica compartida y relevo obligatorio. Antes de codificar, el agente debe comprobar utilidades existentes para reutilizarlas sin duplicar.</li>
            <li><strong>Librerías Base Reutilizables y Scripts Maestros:</strong> Estandarización en módulos centrales (ej. generadores de bitácora y scripts batch) en lugar de dispersar código repetido.</li>
            <li><strong>Curaduría y Desduplicación Estricta:</strong> Aplicada por ejemplo en el módulo musical Korg EK-50 con la <em>Regla de los 8 Sonidos Únicos</em>, purgando cabeceras y eliminando botones redundantes.</li>
        </ul>
    </div>

    <h2>4. Patología 2: DRIFT (Desviación / Deriva de Contexto)</h2>
    <div class="danger-box">
        <span class="badge badge-danger">El Peligro en la IA</span><br>
        <strong>⚠️ Ceguera de contexto y olvido progresivo:</strong> A medida que la conversación acumula miles de tokens, el modelo sufre fatiga cognitiva. Se aleja sutilmente de las reglas fundacionales, altera estructuras de carpetas acordadas, inventa abreviaturas o relaja los estándares de calidad.
    </div>
    <div class="solution-box">
        <span class="badge badge-solution">Soluciones en la Arquitectura</span><br>
        <strong>🛡️ Gobernanza Antigravity:</strong>
        <ul>
            <li><strong>Protocolo Elephant-Goldfish:</strong> El <em>Elefante</em> (coordinador) mantiene la memoria histórica y planifica; el <em>Goldfish</em> (subagente efímero) nace con mente virgen para auditar el código contra una lista de control estricta y se destruye inmediatamente sin dejar procesos residuales.</li>
            <li><strong>Catálogos Canónicos Estrictos:</strong> Prohibición absoluta de abreviaturas inventadas. En NASA Eyes se exige el ID exacto (<code>sc_roman_space_telescope</code>, nunca <code>sc_roman</code>); en Korg EK-50, Banco Maestro MSB 33 y numeración formal de 3 dígitos (<code>029 Harmonica</code>).</li>
            <li><strong>Doble Contador Correlativo de Comandos:</strong> Mantenimiento estricto de dos contadores independientes (Contador General <code>[COMANDO XX]</code> y Contador Música <code>[COMANDO MÚSICA XX]</code>) para asegurar la trazabilidad cronológica.</li>
        </ul>
    </div>

    <h2>5. Patología 3: DELUGE (Diluvio de Código y Sobre-Ingeniería)</h2>
    <div class="danger-box">
        <span class="badge badge-danger">El Peligro en la IA</span><br>
        <strong>⚠️ Inflación y dependencias innecesarias:</strong> Propensión del modelo a 'vomitar' cientos de líneas de código superfluo, proponiendo frameworks pesados, dependencias de terceros (<code>npm</code>, librerías <code>pip</code> ajenas) o arquitecturas mastodónticas para resolver problemas que se solucionan con pocas líneas nativas.
    </div>
    <div class="solution-box">
        <span class="badge badge-solution">Soluciones en la Arquitectura</span><br>
        <strong>🛡️ Gobernanza Antigravity:</strong>
        <ul>
            <li><strong>Regla de Cero Herramientas Nuevas ni Instalaciones Externas:</strong> Prohibición radical de instalar paquetes de terceros. Se opera exclusivamente con herramientas nativas de macOS y Python estándar (<code>urllib</code>, <code>xml</code>, AppleScript).</li>
            <li><strong>Diferenciación Clara de Motores 3D:</strong> Prohibición de Babylon.js en simuladores anatómicos/médicos de IA (donde se exige Three.js limpio o Canvas fotográfico hiperrealista) mientras se reserva y mantiene Babylon.js al 100% como motor oficial en Robótica (aprovechando sus shaders y física Havok).</li>
            <li><strong>La Triple Salvaguarda Pedagógica (+65):</strong> Cero código intermedio para los alumnos senior. Se entregan micro-aplicaciones autónomas de 1 página que funcionan al 100% con doble clic en cualquier navegador sin servidor ni dependencias.</li>
        </ul>
    </div>

    <h2>6. Patología 4: DECEPTION (Engaño / Ilusión de Funcionamiento)</h2>
    <div class="danger-box">
        <span class="badge badge-danger">El Peligro en la IA</span><br>
        <strong>⚠️ Simulaciones huecas y enlaces ciegos:</strong> El código compila y la interfaz luce profesional, pero internamente es un cascarón vacío: datos estáticos inventados, APIs bloqueadas por seguridad o sondas históricas orbitando la Tierra en lugar de su planeta destino por omitir el parámetro temporal.
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

    <h2>7. Análisis Exhaustivo de Configuración y Parámetros del Motor Antigravity</h2>
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
            <li><strong>Aislamiento de Recursos:</strong> En modo estándar (<code>BypassSandbox: false</code>), el agente tiene permisos plenos de lectura y escritura dentro de la carpeta raíz del proyecto y directorios temporales, pero no puede acceder a otras carpetas privadas del Mac ni modificar configuraciones de red del sistema anfitrión.</li>
            <li><strong>Eliminación de Fricción:</strong> Permite auto-aprobar comandos sin intervención del usuario, garantizando el cumplimiento estricto del <em>Protocolo de Cero Submits</em>.</li>
        </ul>
    </div>

    <div class="param-box">
        <span class="badge badge-param">Parámetro 3</span>
        <h3>3. Acceso a Archivos Fuera del Workspace (Non-Workspace File Access)</h3>
        <p>Regula la conducta del agente si una instrucción le solicita leer o alterar archivos fuera de la ruta de trabajo inicial.</p>
        <ul>
            <li><strong>Opciones de Motor:</strong> <code>allow</code> (acceso libre), <code>ask</code> (preguntar al usuario con popup), <code>deny</code> (bloqueo absoluto).</li>
            <li><strong>Nuestra Solución por Diseño:</strong> Gracias a nuestra <em>Arquitectura de Raíz Única</em> en <code>CLASES DE TECNOLOGÍA/</code>, <strong>el 100% de los proyectos, bitácoras y asignaturas cuelgan de la misma raíz</strong>. El agente jamás necesita salir del workspace, eliminando alertas de seguridad por cruce de carpetas.</li>
        </ul>
    </div>

    <div class="param-box">
        <span class="badge badge-param">Parámetro 4</span>
        <h3>4. Acceso a Internet y Lista Blanca de Navegación (Internet Access & Browser Allowlist)</h3>
        <p>Controla la capacidad del agente para realizar peticiones de red y abrir sesiones automatizadas en el navegador.</p>
        <ul>
            <li><strong>Nivel de Red:</strong> Configurado en modo lectura y consulta de repositorios científicos (NASA, USGS, Wikimedia Commons) para obtener datos reales.</li>
            <li><strong>Prevención de Invasión en Navegadores:</strong> Se restringe el control invasivo del navegador local mediante Chrome DevTools (que exige puertos de depuración y dispara diálogos de seguridad en macOS), favoreciendo en su lugar micro-aplicaciones locales autónomas en HTML5.</li>
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
            <li><strong>Persistencia de Estándares:</strong> Es aquí donde quedan blindados los compromisos innegociables: Cero-Submits, Cuadro de Mando Matutino, Doble Contador Correlativo, Estándar de Fichas Largas y Despliegue Automático a GitHub.</li>
        </ul>
    </div>

    <h2>8. El Patrón Operativo Maestro: Trabajo en Silencio y Comando Terminal Final</h2>
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
            <li><strong>Fase 2: Entrega del Comando Único al Final (Lado Usuario):</strong> Una vez terminada y verificada la tarea, el agente no le pide al usuario que ejecute múltiples pasos sueltos. Entrega un <strong>único bloque bash autocontenido</strong>, rigurosamente numerado (ej. <code>[COMANDO 201]</code>) y protegido con cabecera y pie visibles mediante <code>echo</code>.</li>
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
            <li><strong>Trazabilidad y Control Humano Real:</strong> Aunque la IA trabaja sola, <em>el usuario retiene la soberanía final de ejecución</em>. El comando en la terminal externa le muestra con total claridad qué se está aplicando en el sistema operativo y cuándo concluye de forma exitosa.</li>
            <li><strong>Cero Fallos de Despliegue en GitHub:</strong> Al empaquetar <code>git add</code>, <code>git commit</code> y <code>git push origin main</code> dentro del comando terminal, se garantiza que jamás quede un cambio local desincronizado con GitHub Pages o Classroom.</li>
            <li><strong>Historial Cronológico Limpio:</strong> Al pegar el comando en la terminal externa del Mac, el historial de la shell refleja de manera idéntica y reproducible la secuencia histórica de hitos registrados en <code>ESTADO_GLOBAL_PROYECTOS.md</code>.</li>
        </ul>
    </div>

    <h2>9. Nueva Arquitectura Concurrente: Subagentes Efímeros en Paralelo</h2>
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

    <h2>10. Nueva Arquitectura Visual: Generative UI en Antigravity</h2>
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

    <h2>11. Catálogo Evolutivo de Mejoras del Ecosistema</h2>
    <p>Este documento constituye el inventario vivo de todas las mejoras de gobernanza, comportamiento y arquitectura implementadas en nuestra configuración de IA:</p>
    <table>
        <thead>
            <tr>
                <th>Hito / Mejora</th>
                <th>Ámbito</th>
                <th>Impacto y Beneficio Operativo</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Monorepo Raíz Única</strong></td>
                <td>Estructura Workspace</td>
                <td>Todas las asignaturas y carpetas bajo <code>CLASES DE TECNOLOGÍA/</code> para cero bloqueos de permisos.</td>
            </tr>
            <tr>
                <td><strong>Trabajo en Silencio & Terminal</strong></td>
                <td>Metodología Agéntica</td>
                <td>Ejecución desatendida sin charla ni popups; entrega de bloque bash único numerado al final.</td>
            </tr>
            <tr>
                <td><strong>Protocolo de Oro Cero-Submits</strong></td>
                <td>Flujo de Trabajo</td>
                <td>Eliminación total de ventanas emergentes de aprobación durante la sesión en el editor.</td>
            </tr>
            <tr>
                <td><strong>Cuadro de Mando Matutino</strong></td>
                <td>Seguimiento Diario</td>
                <td>Recordatorio obligatorio de tareas activas al arrancar cada jornada de trabajo.</td>
            </tr>
            <tr>
                <td><strong>Formato Estricto [COMANDO XX]</strong></td>
                <td>Terminal Externa</td>
                <td>Comandos correlativos numerados con títulos visibles por <code>echo</code> inicial y final.</td>
            </tr>
            <tr>
                <td><strong>Arquitectura Elephant-Goldfish</strong></td>
                <td>Memoria / Contexto</td>
                <td>Prevención de drift mediante agentes efímeros con mente limpia y destrucción inmediata.</td>
            </tr>
            <tr>
                <td><strong>Subagentes en Paralelo</strong></td>
                <td>Alta Concurrencia</td>
                <td>Ejecución concurrente de tareas pesadas en segundo plano sin saturar el hilo principal.</td>
            </tr>
            <tr>
                <td><strong>Generative UI Nativo</strong></td>
                <td>Experiencia Visual</td>
                <td>Widgets y cuadros de mando interactivos embebidos sin exponer código intermedio.</td>
            </tr>
            <tr>
                <td><strong>Estándar de Maquetación Larga</strong></td>
                <td>Didáctica / Senior</td>
                <td>Títulos mayores en página nueva, tipografía de 14 pt y desglose individual botón a botón.</td>
            </tr>
            <tr>
                <td><strong>Despliegue Continuo a GitHub</strong></td>
                <td>Publicación</td>
                <td>Sincronización automática de cada cambio con GitHub Pages y Google Classroom.</td>
            </tr>
        </tbody>
    </table>

    <h2>12. Matriz Resumen de Gobernanza y Soluciones de Arquitectura</h2>
    <table>
        <thead>
            <tr>
                <th>Pilar de Arquitectura</th>
                <th>Riesgo / Desafío</th>
                <th>Solución de Gobernanza en Antigravity</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>1. Estructura Raíz</strong></td>
                <td>Dispersión de carpetas y bloqueos de seguridad.</td>
                <td>Monorepo raíz en <code>CLASES DE TECNOLOGÍA</code> para unificación total de permisos.</td>
            </tr>
            <tr>
                <td><strong>2. Flujo Operativo</strong></td>
                <td>Interrupciones continuas y pérdida de control.</td>
                <td>Trabajo 100% silencioso en Sandbox y entrega de comando terminal único numerado.</td>
            </tr>
            <tr>
                <td><strong>3. Duplicación</strong></td>
                <td>Reinvención de utilidades y código redundante.</td>
                <td>Documento vivo <code>ESTADO_GLOBAL_PROYECTOS.md</code> y módulos maestros compartidos.</td>
            </tr>
            <tr>
                <td><strong>4. Drift</strong></td>
                <td>Pérdida de arquitectura y abreviaturas inventadas.</td>
                <td>Arquitectura Elephant-Goldfish, catálogos canónicos y doble contador correlativo.</td>
            </tr>
            <tr>
                <td><strong>5. Deluge</strong></td>
                <td>Sobre-ingeniería, dependencias y frameworks pesados.</td>
                <td>Regla de cero herramientas nuevas, código nativo estándar y micro-apps de 1 archivo.</td>
            </tr>
            <tr>
                <td><strong>6. Deception</strong></td>
                <td>Ilusión de funcionamiento, APIs ciegas y datos falsos.</td>
                <td>Autocomprobación obligatoria, calibración temporal UTC y copias BKP garantizadas.</td>
            </tr>
            <tr>
                <td><strong>7. Parámetros Motor</strong></td>
                <td>Ventanas molestas de submit y fallos de permisos.</td>
                <td>Calibración estricta en <code>proceed-in-sandbox</code> y reglas canónicas en <code>AGENTS.md</code>.</td>
            </tr>
            <tr>
                <td><strong>8. Concurrencia</strong></td>
                <td>Fatiga cognitiva y bloqueo en tareas intensivas.</td>
                <td>Subagentes paralelos efímeros con ciclo de vida atómico y autodestrucción.</td>
            </tr>
            <tr>
                <td><strong>9. Visualización</strong></td>
                <td>Sobrecarga de código fuente y fricción en el usuario.</td>
                <td>Generative UI: micro-aplicaciones y widgets interactivos embebidos en el chat.</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(BKP_HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ HTML generado: {HTML_PATH}", flush=True)

    # Conversión nativa a DOCX con textutil
    try:
        subprocess.run(["textutil", "-convert", "docx", HTML_PATH, "-output", DOCX_PATH], check=True)
        print(f"✅ DOCX generado: {DOCX_PATH}", flush=True)
    except Exception as e:
        print(f"⚠️ Aviso generando DOCX: {e}", flush=True)

def compilar_pdf_reportlab():
    """Compila el documento PDF profesional completo con maquetación estricta y sin solapes."""
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=42
    )

    PAGE_WIDTH = A4[0] - 72  # 523.27 pt

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#475569'),
        spaceAfter=8
    )

    quote_style = ParagraphStyle(
        'QuoteStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#334155'),
        backColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#64748B'),
        borderWidth=1,
        borderPadding=6,
        spaceAfter=8
    )

    h1_style = ParagraphStyle(
        'Heading1Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13.5,
        textColor=colors.HexColor('#0369A1'),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    h2_sub_style = ParagraphStyle(
        'Heading2Sub',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=4,
        spaceAfter=2,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#1E293B'),
        spaceAfter=4
    )

    tree_style = ParagraphStyle(
        'TreeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=6.8,
        leading=8.8,
        textColor=colors.HexColor('#0284C7'),
        backColor=colors.HexColor('#F1F5F9'),
        borderColor=colors.HexColor('#CBD5E1'),
        borderWidth=0.8,
        borderPadding=6,
        spaceAfter=6
    )

    code_banner_style = ParagraphStyle(
        'CodeBannerStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7,
        leading=9.2,
        textColor=colors.HexColor('#F8FAFC'),
        backColor=colors.HexColor('#1E293B'),
        borderColor=colors.HexColor('#38BDF8'),
        borderWidth=1,
        borderPadding=5,
        spaceAfter=5
    )

    danger_title = ParagraphStyle(
        'DangerTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#B91C1C'),
        spaceAfter=2
    )

    danger_body = ParagraphStyle(
        'DangerBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor('#7F1D1D')
    )

    sol_title = ParagraphStyle(
        'SolTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#15803D'),
        spaceAfter=2
    )

    sol_body = ParagraphStyle(
        'SolBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor('#14532D')
    )

    feat_title = ParagraphStyle(
        'FeatTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#0369A1'),
        spaceAfter=2
    )

    feat_body = ParagraphStyle(
        'FeatBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor('#0F172A')
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#0F172A'),
        alignment=0
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.2,
        textColor=colors.HexColor('#334155')
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=9.2,
        textColor=colors.HexColor('#0F172A')
    )

    story = []

    # Encabezado principal
    story.append(Paragraph("Soluciones de Arquitectura y Gobernanza en Google Antigravity", title_style))
    story.append(Paragraph("<b>Ecosistema Formativo y Personal • Monográfico 6: Gestión del Proyecto con IA</b><br/>Guía maestra de blindaje agéntico, prevención del 'Vibe Coding', orquestación concurrente, calibración de parámetros y catálogo evolutivo de mejoras.", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0284C7"), spaceAfter=6, spaceBefore=0))

    story.append(Paragraph("«El verdadero peligro no es que la inteligencia artificial escriba código, sino que el humano pierda el gobierno sobre la arquitectura. El código se delega; el rigor, la jerarquía de ficheros, la memoria y la verificación jamás.» — <b>Marco de Gobernanza Agéntica en Antigravity</b>", quote_style))

    # 1. Jerarquía Monorepo Raíz Única
    tree_text = """CLASES DE TECNOLOGÍA/ [RAÍZ ÚNICA DEL WORKSPACE EN ANTIGRAVITY]
├── AGENTS.md (Protocolo de Oro, Cero-Submits, Reglas de Ejecución y Estándares)
├── GEMINI.md (Espejo Canónico y Directivas Operativas de Modelos)
├── ESTADO_GLOBAL_PROYECTOS.md (Inventario Técnico Centralizado y Memoria Viva)
├── CURSO-IA/ (Inteligencia Artificial para Seniors 65+ | Monográficos 1 a 6)
│   ├── CLASES/ (Fichas, Prompts, NASA Eyes 3D, Gestión de Proyectos con IA)
│   └── 00. SCRIPTS_PYTHON/ (Compiladores nativos de PDFs y comprobadores)
├── CURSO-ROBOTICA-V2/ (Robótica, Mecatrónica y Androides | 14 slides)
├── CURSO-ROBOTICA-IA-COMUN/ (Infraestructura, Calendario y Bitácora Oficial)
├── CURSO_MUSICA/ (Web MIDI, Banco Maestro MSB 33 y Korg EK-50)
└── IA TEMAS VARIOS/ (Gestión Personal, Salud y Utilidades Administrativas)"""

    story.append(KeepTogether([
        Paragraph("1. Jerarquía de Carpetas y Arquitectura de Raíz Única (Monorepo Workspace)", h1_style),
        Paragraph("Para evitar de raíz el problema clásico de permisos, fragmentación y pérdida de contexto entre carpetas dispersas, todo el ecosistema formativo, técnico, musical y de seguimiento está estructurado bajo una <b>única carpeta raíz (Monorepo Workspace)</b> en macOS iCloud Drive: <code>/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/</code>. Al situar la raíz de Antigravity en este directorio padre, el agente opera permanentemente dentro del mismo espacio de trabajo reconocido, garantizando acceso universal sin solicitar permisos especiales de <i>Non-Workspace File Access</i> ni disparar alertas de seguridad.", body_style),
        Paragraph(tree_text.replace('\n', '<br/>').replace(' ', '&nbsp;'), tree_style),
        Spacer(1, 4)
    ]))

    # 2. Contexto
    story.append(Paragraph("2. Contexto: El Fenómeno del 'Vibe Coding' y la Necesidad de Gobernanza", h1_style))
    story.append(Paragraph("En la era del desarrollo con modelos generativos avanzados, programar se ha convertido en un flujo acelerado ('vibe coding'). Sin embargo, esta velocidad encierra una trampa crítica: la falsa ilusión de perfección. Sin salvaguardas explícitas, el código acumula silenciosamente cuatro patologías fundamentales conocidas como <b>Las 4 D del peligro de la IA</b> (<i>Duplicación</i>, <i>Drift</i>, <i>Deluge</i> y <i>Deception</i>).", body_style))

    def make_section_box(num_str, title_str, danger_text, solution_bullets):
        c_danger_bg = colors.HexColor("#FEF2F2")
        c_danger_border = colors.HexColor("#F87171")
        c_sol_bg = colors.HexColor("#F0FDF4")
        c_sol_border = colors.HexColor("#4ADE80")

        elements = [
            Paragraph(f"{num_str} Patología: {title_str}", h1_style),
            Spacer(1, 2)
        ]

        p_danger = [
            Paragraph("⚠️ EL PELIGRO EN LA IA:", danger_title),
            Paragraph(danger_text, danger_body)
        ]
        t_danger = Table([[p_danger]], colWidths=[PAGE_WIDTH])
        t_danger.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), c_danger_bg),
            ('BOX', (0,0), (-1,-1), 0.8, c_danger_border),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        elements.append(t_danger)
        elements.append(Spacer(1, 4))

        p_sol = [
            Paragraph("🛡️ NUESTRAS SOLUCIONES EN LA ARQUITECTURA:", sol_title),
            Spacer(1, 1)
        ]
        for bullet in solution_bullets:
            p_sol.append(Paragraph(f"• {bullet}", sol_body))
            p_sol.append(Spacer(1, 1))

        t_sol = Table([[p_sol]], colWidths=[PAGE_WIDTH])
        t_sol.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), c_sol_bg),
            ('BOX', (0,0), (-1,-1), 0.8, c_sol_border),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        elements.append(t_sol)
        elements.append(Spacer(1, 5))
        return KeepTogether(elements)

    # 3. DUPLICACIÓN
    story.append(make_section_box(
        "3.", "DUPLICACIÓN (Duplication)",
        "Cuando se solicita una nueva tarea, el modelo tiende a reescribir funciones de utilidad, estilos y lógica que ya existían previamente en otros archivos del repositorio. Esto fragmenta la base de código, multiplica los puntos de fallo y convierte el mantenimiento en una pesadilla.",
        [
            "<b>Documento Vivo Centralizado (ESTADO_GLOBAL_PROYECTOS.md):</b> Inventario permanente que el agente consulta de forma obligatoria antes de codificar para identificar scripts, directivas y estados preexistentes sin duplicar.",
            "<b>Librerías Base Reutilizables y Scripts Maestros:</b> Estandarización en módulos centrales (ej. generadores de bitácora y scripts batch) en lugar de dispersar código repetido.",
            "<b>Curaduría y Desduplicación Estricta:</b> Aplicada por ejemplo en el módulo musical Korg EK-50 con la <i>Regla de los 8 Sonidos Únicos</i>, purgando sistemáticamente cualquier botón redundante."
        ]
    ))

    # 4. DRIFT
    story.append(make_section_box(
        "4.", "DRIFT (Desviación / Deriva de Contexto)",
        "A medida que la sesión acumula miles de tokens, el modelo sufre de 'ceguera de contexto'. Pierde el hilo de las directivas fundacionales, olvida estándares acordados, altera jerarquías de carpetas o inventa abreviaturas que rompen la arquitectura original.",
        [
            "<b>Arquitectura Elephant-Goldfish:</b> El 'Elefante' (coordinador) mantiene la memoria histórica y planifica; el 'Goldfish' (subagente efímero) nace con mente virgen para auditar el código contra una lista de control estricta y se destruye inmediatamente sin dejar procesos residuales.",
            "<b>Catálogos Canónicos Estrictos:</b> Prohibición absoluta de abreviaturas inventadas. En NASA Eyes se exige el ID exacto (<code>sc_roman_space_telescope</code>, nunca <code>sc_roman</code>); en Korg EK-50, Banco Maestro MSB 33 y numeración formal de 3 dígitos (<code>029 Harmonica</code>).",
            "<b>Doble Contador Correlativo de Comandos:</b> Control cronológico estricto entre el Contador General (<code>[COMANDO XX]</code>) y el Contador Música (<code>[COMANDO MÚSICA XX]</code>) para anclar cada avance sin desviaciones."
        ]
    ))

    # 5. DELUGE
    story.append(make_section_box(
        "5.", "DELUGE (Diluvio de Código y Sobre-Ingeniería)",
        "La propensión de la IA a inflar el proyecto ('vomitar' cientos de líneas innecesarias), agregando frameworks pesados, dependencias externas superfluas (npm, librerías pip ajenas) y arquitecturas complejas que luego se rompen por obsolescencia.",
        [
            "<b>Regla de Cero Herramientas Nuevas ni Instalaciones Externas:</b> Prohibición tajante de instalar paquetes de terceros. Se opera exclusivamente con herramientas nativas de macOS y Python estándar (<code>urllib</code>, <code>xml</code>, AppleScript).",
            "<b>Diferenciación Clara de Motores 3D:</b> Prohibición de Babylon.js en simuladores anatómicos/médicos de IA (donde se exige Three.js limpio o Canvas fotográfico hiperrealista) mientras se reserva y mantiene Babylon.js al 100% como motor oficial en Robótica (aprovechando sus shaders y física Havok).",
            "<b>La Triple Salvaguarda Pedagógica y Cero Código Intermedio (+65):</b> Los alumnos senior no manipulan código fuente; reciben micro-aplicaciones autónomas de 1 página que funcionan al 100% con doble clic en cualquier navegador sin servidor ni dependencias."
        ]
    ))

    # 6. DECEPTION
    story.append(make_section_box(
        "6.", "DECEPTION (Engaño / Ilusión de Funcionamiento)",
        "El fallo más peligroso y sutil: el código compila y la interfaz luce atractiva, pero por dentro es una simulación hueca (datos estáticos falsos, llamadas a APIs bloqueadas o sondas espaciales que orbitan la Tierra en lugar de Venus por omisión de parámetros temporales).",
        [
            "<b>Obligación de Autocomprobación Previa y Poda Temprana:</b> Si un enlace, telemetría o malla 3D no existe o no se mueve en el motor real, no se maquilla ni se inventa: se poda de inmediato y se sustituye por un activo 100% verificado.",
            "<b>Calibración Temporal Obligatoria:</b> Inyección de marcas temporales UTC (<code>time=YYYY-MM-DD...</code>) en misiones históricas para situar las naves en su destino real y no en el despegue.",
            "<b>Blindaje ante Políticas de Seguridad del Navegador:</b> Eliminación de enlaces directos a WhatsApp bloqueados por COOP en Safari, adoptando la publicación nativa en Gemini Canvas.",
            "<b>Copia de Respaldo Oficial BKP Garantizada al 100%:</b> Cada simulador cuenta en el mapa con su botón oficial BKP probado, garantizando el funcionamiento en el aula sin depender de la red ni de la IA en tiempo real."
        ]
    ))

    # 7. PARÁMETROS DEL MOTOR ANTIGRAVITY (DETALLADO)
    def make_param_box(num_str, title_str, desc_text, bullets):
        elements = [
            Paragraph(f"{num_str} {title_str}", h1_style),
            Paragraph(desc_text, body_style),
            Spacer(1, 1)
        ]
        p_bullets = []
        for b in bullets:
            p_bullets.append(Paragraph(f"• {b}", feat_body))
            p_bullets.append(Spacer(1, 1))

        t_box = Table([[p_bullets]], colWidths=[PAGE_WIDTH])
        t_box.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
            ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#94A3B8")),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        elements.append(t_box)
        elements.append(Spacer(1, 5))
        return KeepTogether(elements)

    story.append(Paragraph("7. Análisis Exhaustivo de Configuración y Parámetros del Motor Antigravity", h1_style))
    story.append(Paragraph("A diferencia de entornos conversacionales cerrados, Antigravity es un sistema operativo agéntico parametrizable. A continuación se desglosan los parámetros centrales analizados, su funcionamiento interno y la calibración aplicada:", body_style))

    story.append(make_param_box(
        "7.1.", "Política de Ejecución de Terminal (Tool Execution Policy)",
        "Controla el nivel de autonomía y la necesidad de aprobaciones humanas ante cada comando en terminal:",
        [
            "<b>strict / request-review:</b> Pausa ante cada comando de terminal o cambio de fichero, abriendo una ventana de aprobación obligatoria (Submit / Approve).",
            "<b>agent-decides:</b> El modelo evalúa la criticidad de la acción; ejecuta automáticamente lecturas pero pide autorización ante ediciones.",
            "<b>always-proceed (Modo Turbo / YOLO):</b> Autonomía absoluta sin pausas ni revisiones intermedias, ejecutando directamente en la máquina.",
            "<b>proceed-in-sandbox (NUESTRA CALIBRACIÓN OFICIAL):</b> Ejecución 100% desatendida y silenciosa siempre que el comando opere dentro del Sandbox del proyecto. Si por error se solicita <code>BypassSandbox: true</code>, el sistema lanza la confirmación humana de seguridad."
        ]
    ))

    story.append(make_param_box(
        "7.2.", "Modo Sandbox y Aislamiento de Procesos (Terminal Sandbox)",
        "Define el contenedor de seguridad donde operan los procesos del agente:",
        [
            "<b>Aislamiento de Recursos:</b> En <code>BypassSandbox: false</code>, el agente dispone de lectura/escritura total dentro de la carpeta raíz y temporales (/tmp), pero no puede acceder a carpetas privadas del Mac ni alterar binarios del sistema.",
            "<b>Auto-aprobación del Sistema:</b> Permite la ejecución de comandos limpios y atómicos sin interrupciones, cumpliendo el Protocolo de Cero Submits."
        ]
    ))

    story.append(make_param_box(
        "7.3.", "Acceso Fuera del Workspace (Non-Workspace File Access)",
        "Determina el comportamiento cuando una orden solicita acceder a carpetas externas al proyecto:",
        [
            "<b>Opciones:</b> <code>allow</code> (libre), <code>ask</code> (preguntar con ventana emergente), <code>deny</code> (bloqueo total).",
            "<b>Solución Monorepo Raíz:</b> Al estar todo el ecosistema (IA, Robótica, Música, Calendario y Salud) contenido bajo <code>CLASES DE TECNOLOGÍA/</code>, el agente opera siempre dentro del workspace, eliminando al 100% los bloqueos por cruce de carpetas."
        ]
    ))

    story.append(make_param_box(
        "7.4.", "Política de Acceso a Internet y Lista Blanca (Internet Access & Browser Allowlist)",
        "Regula las peticiones de red y la automatización de navegadores:",
        [
            "<b>Consultas Abiertas a Ciencia Real:</b> Acceso autorizado a repositorios de ciencia acreditada (NASA, Wikimedia Commons, NIH) para recopilar mallas y telemetría real.",
            "<b>Restricción de Navegador Invasivo:</b> Se evita la manipulación interactiva de instancias locales de Chrome (que requieren puertos de depuración y generan alertas de seguridad en macOS), prefiriendo micro-apps HTML5 autónomas."
        ]
    ))

    story.append(make_param_box(
        "7.5.", "Selección y Enrutamiento de Modelos (Model Selection & Routing)",
        "Asignación estratégica de modelos neuronales según la complejidad de la tarea:",
        [
            "<b>Gemini Pro (Coordinador / Elefante):</b> Empleado para razonamiento arquitectónico, planificación global de bimestres y supervisión de las 4 D.",
            "<b>Gemini Flash (Subagentes / Goldfish):</b> Modelo de bajísima latencia para subagentes paralelos efímeros que realizan auditorías sintácticas o verificaciones en pocos segundos."
        ]
    ))

    story.append(make_param_box(
        "7.6.", "Jerarquía y Prioridad de Reglas del Proyecto (AGENTS.md / GEMINI.md)",
        "El núcleo de gobernanza que subordina el motor de IA a las directivas del usuario:",
        [
            "<b>Prioridad Absoluta:</b> Los archivos <code>AGENTS.md</code> y <code>GEMINI.md</code> ubicados en la raíz del workspace tienen precedencia total sobre las configuraciones globales de la aplicación.",
            "<b>Persistencia de Estándares:</b> Garantiza la aplicación inquebrantable de Cero-Submits, Cuadro de Mando Diario, Doble Contador y Estándar de Fichas Largas."
        ]
    ))

    # 8. PATRÓN MAESTRO: TRABAJO EN SILENCIO Y COMANDO TERMINAL FINAL
    banner_snippet = """### [INICIO COMANDO XX: TÍTULO DEL COMANDO]
echo "========================================================"
echo "=== [INICIO COMANDO XX: TÍTULO DEL COMANDO] ==="
echo "========================================================"
... (instrucciones desatendidas: git, verificación, despliegue) ...
echo "========================================================"
echo "=== [FIN COMANDO XX: TÍTULO DEL COMANDO] (EXITOSO) ==="
echo "========================================================"
### [FIN COMANDO XX: TÍTULO DEL COMANDO]"""

    p_silence = [
        Paragraph("<b>¿En qué momento se usa, cómo opera y por qué se diseñó esta arquitectura?</b>", feat_title),
        Spacer(1, 2),
        Paragraph("<b>1. ¿En qué momento se usa?</b> Se aplica obligatoriamente en todas las tareas operativas: maquetación de fichas, reescritura de scripts, edición de mapas interactivos, actualización de calendarios y despliegues en GitHub.", feat_body),
        Spacer(1, 2),
        Paragraph("<b>2. ¿Cómo lo usamos? (Mecánica en Dos Fases):</b>", feat_body),
        Paragraph("• <i>Fase 1 (Trabajo Silencioso en Sandbox):</i> El agente usa herramientas internas (read_file, edit_file, write_file) procesando archivos y compilando sin emitir charlas intermedias ni requerir botones interactivos (RequestFeedback: false, Cero Submits).", feat_body),
        Paragraph("• <i>Fase 2 (Entrega del Comando Único al Final):</i> Al concluir con éxito, el agente entrega un único bloque bash correlativo y numerado con cabecera y pie visibles por <code>echo</code> para ejecución externa desatendida.", feat_body),
        Spacer(1, 2),
        Paragraph(banner_snippet.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_banner_style),
        Spacer(1, 2),
        Paragraph("<b>3. ¿Por qué lo usamos? (Beneficios de Gobernanza):</b>", feat_body),
        Paragraph("• <i>Cero Fricción Cognitiva:</i> Elimina 15-20 popups por tarea; la IA absorbe el esfuerzo sin interrumpir.", feat_body),
        Paragraph("• <i>Soberanía y Control Humano:</i> El usuario retiene el control final viendo en su terminal qué se ejecuta y cuándo concluye.", feat_body),
        Paragraph("• <i>Despliegue GitHub Blindado:</i> Integra commit y push automáticos, garantizando que nada quede huérfano en local.", feat_body),
        Paragraph("• <i>Trazabilidad Cronológica:</i> La shell externa reproduce con exactitud la serie histórica de <code>ESTADO_GLOBAL_PROYECTOS.md</code>.", feat_body)
    ]
    t_silence = Table([[p_silence]], colWidths=[PAGE_WIDTH])
    t_silence.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0FDF4")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#22C55E")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(KeepTogether([
        Paragraph("8. El Patrón Operativo Maestro: Trabajo en Silencio y Comando Terminal Final", h1_style),
        Paragraph("La clave de la colaboración entre humano e IA en nuestro sistema es la separación estricta entre <b>procesamiento silencioso interno</b> y <b>ejecución soberana externa</b>:", body_style),
        Spacer(1, 2),
        t_silence,
        Spacer(1, 5)
    ]))

    # 9. SUBAGENTES EN PARALELO
    p_feat_sub = [
        Paragraph("⚡ ALTA CONCURRENCIA Y AISLAMIENTO TOTAL:", feat_title),
        Paragraph("Para evitar la saturación de contexto en sesiones complejas, Antigravity adopta la orquestación de subagentes paralelos efímeros (<code>invoke_subagent</code>):", feat_body),
        Spacer(1, 2),
        Paragraph("• <b>Mente Limpia y Cero Sesgo:</b> Cada subagente se lanza con un prompt atómico específico, sin arrastrar historiales extensos.", feat_body),
        Paragraph("• <b>Autodestrucción Inmediata (kill):</b> Al concluir la tarea (auditoría, compilación de PDF o verificación), el subagente se destruye liberando memoria y evitando procesos zombi.", feat_body),
        Paragraph("• <b>Protocolo Cero-Submits:</b> Ejecución 100% desatendida y silenciosa, reportando únicamente el resultado consolidado al coordinador.", feat_body)
    ]
    t_feat_sub = Table([[p_feat_sub]], colWidths=[PAGE_WIDTH])
    t_feat_sub.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0F9FF")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#38BDF8")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(KeepTogether([
        Paragraph("9. Nueva Arquitectura Concurrente: Subagentes Efímeros en Paralelo", h1_style),
        Spacer(1, 2),
        t_feat_sub,
        Spacer(1, 5)
    ]))

    # 10. GENERATIVE UI
    p_feat_ui = [
        Paragraph("🎨 VISUALIZACIÓN DIRECTA SIN CÓDIGO INTERMEDIO:", feat_title),
        Paragraph("Antigravity revoluciona la interacción humana mediante Generative UI embebido (<code>&lt;agent-embed&gt;</code>):", feat_body),
        Spacer(1, 2),
        Paragraph("• <b>Renderizado Nativo en el Chat y Panel Lateral:</b> Widgets interactivos autónomos que muestran cuadros de mando, calendarios y simuladores sin obligar al usuario a abrir consolas.", feat_body),
        Paragraph("• <b>Tailwind CSS & Tokens Antigravity:</b> Estilizado modular que respeta el tema claro/oscuro del sistema mediante variables semánticas.", feat_body),
        Paragraph("• <b>Cero Fricción para Alumnos Senior:</b> En lugar de código fuente, los alumnos visualizan y manipulan controles visuales enriquecidos al primer clic.", feat_body)
    ]
    t_feat_ui = Table([[p_feat_ui]], colWidths=[PAGE_WIDTH])
    t_feat_ui.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FAF5FF")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#C084FC")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(KeepTogether([
        Paragraph("10. Nueva Arquitectura Visual: Generative UI en Antigravity", h1_style),
        Spacer(1, 2),
        t_feat_ui,
        Spacer(1, 5)
    ]))

    # 11. CATÁLOGO EVOLUTIVO DE MEJORAS
    story.append(KeepTogether([
        Paragraph("11. Catálogo Evolutivo de Mejoras del Ecosistema", h1_style),
        Spacer(1, 2)
    ]))
    table_cat_data = [
        [Paragraph("Mejora / Protocolo", table_header), Paragraph("Ámbito Operativo", table_header), Paragraph("Impacto y Beneficio en la Configuración", table_header)],
        [Paragraph("<b>Monorepo Raíz Única</b>", table_cell_bold), Paragraph("Estructura Workspace", table_cell), Paragraph("Todas las áreas bajo <code>CLASES DE TECNOLOGÍA/</code> para cero bloqueos de permisos.", table_cell)],
        [Paragraph("<b>Trabajo en Silencio & Terminal</b>", table_cell_bold), Paragraph("Metodología Agéntica", table_cell), Paragraph("Ejecución desatendida sin charla ni popups; entrega de bloque bash único numerado al final.", table_cell)],
        [Paragraph("<b>Protocolo Cero-Submits</b>", table_cell_bold), Paragraph("Flujo de Trabajo", table_cell), Paragraph("Cero ventanas emergentes de aprobación. Ejecución 100% desatendida en editor.", table_cell)],
        [Paragraph("<b>Cuadro de Mando Matutino</b>", table_cell_bold), Paragraph("Seguimiento Diario", table_cell), Paragraph("Recordatorio de tareas activas al arrancar cada jornada.", table_cell)],
        [Paragraph("<b>Formato Estricto [COMANDO XX]</b>", table_cell_bold), Paragraph("Terminal Externa", table_cell), Paragraph("Comandos correlativos con títulos visibles por <code>echo</code> inicial/final.", table_cell)],
        [Paragraph("<b>Elephant-Goldfish</b>", table_cell_bold), Paragraph("Memoria / Contexto", table_cell), Paragraph("Auditoría con mente virgen y destrucción inmediata sin fugas de memoria.", table_cell)],
        [Paragraph("<b>Subagentes en Paralelo</b>", table_cell_bold), Paragraph("Alta Concurrencia", table_cell), Paragraph("Múltiples agentes en segundo plano para tareas pesadas sin saturación.", table_cell)],
        [Paragraph("<b>Generative UI Nativo</b>", table_cell_bold), Paragraph("Visualización", table_cell), Paragraph("Widgets y cuadros de mando interactivos embebidos sin exponer código.", table_cell)],
        [Paragraph("<b>Estándar Fichas Largas</b>", table_cell_bold), Paragraph("Didáctica (+65)", table_cell), Paragraph("Títulos en página nueva (14 pt) y desglose individual botón a botón.", table_cell)],
        [Paragraph("<b>Despliegue GitHub Auto</b>", table_cell_bold), Paragraph("Publicación", table_cell), Paragraph("Sincronización inmediata con GitHub Pages y Google Classroom en cada lote.", table_cell)]
    ]
    t_cat = Table(table_cat_data, colWidths=[120, 105, 298.27])
    t_cat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_cat)
    story.append(Spacer(1, 6))

    # 12. MATRIZ RESUMEN
    story.append(KeepTogether([
        Paragraph("12. Matriz Resumen de Gobernanza y Soluciones de Arquitectura", h1_style),
        Spacer(1, 2)
    ]))
    table_mat_data = [
        [Paragraph("Pilar de Arquitectura", table_header), Paragraph("Riesgo / Desafío", table_header), Paragraph("Solución de Gobernanza en Antigravity", table_header)],
        [Paragraph("<b>1. Estructura Raíz</b>", table_cell_bold), Paragraph("Dispersión de carpetas y bloqueos de seguridad.", table_cell), Paragraph("Monorepo raíz en <code>CLASES DE TECNOLOGÍA</code> para unificación total de permisos.", table_cell)],
        [Paragraph("<b>2. Flujo Operativo</b>", table_cell_bold), Paragraph("Interrupciones continuas y pérdida de control.", table_cell), Paragraph("Trabajo 100% silencioso en Sandbox y entrega de comando terminal único numerado.", table_cell)],
        [Paragraph("<b>3. Duplicación</b>", table_cell_bold), Paragraph("Reinvención de utilidades y código redundante.", table_cell), Paragraph("Documento vivo <code>ESTADO_GLOBAL_PROYECTOS.md</code> y módulos maestros compartidos.", table_cell)],
        [Paragraph("<b>4. Drift</b>", table_cell_bold), Paragraph("Pérdida de arquitectura y abreviaturas inventadas.", table_cell), Paragraph("Arquitectura Elephant-Goldfish, catálogos canónicos y doble contador correlativo.", table_cell)],
        [Paragraph("<b>5. Deluge</b>", table_cell_bold), Paragraph("Sobre-ingeniería, dependencias y frameworks pesados.", table_cell), Paragraph("Regla de cero herramientas nuevas, código nativo estándar y micro-apps atómicas.", table_cell)],
        [Paragraph("<b>6. Deception</b>", table_cell_bold), Paragraph("Ilusión de funcionamiento, APIs ciegas y datos falsos.", table_cell), Paragraph("Autocomprobación obligatoria, calibración temporal UTC y copias BKP garantizadas.", table_cell)],
        [Paragraph("<b>7. Parámetros Motor</b>", table_cell_bold), Paragraph("Ventanas molestas de submit y fallos de permisos.", table_cell), Paragraph("Calibración estricta en <code>proceed-in-sandbox</code> y reglas canónicas en <code>AGENTS.md</code>.", table_cell)],
        [Paragraph("<b>8. Concurrencia</b>", table_cell_bold), Paragraph("Fatiga cognitiva y bloqueo en tareas intensivas.", table_cell), Paragraph("Subagentes paralelos efímeros con ciclo de vida atómico y autodestrucción.", table_cell)],
        [Paragraph("<b>9. Visualización</b>", table_cell_bold), Paragraph("Sobrecarga de código fuente y fricción en el usuario.", table_cell), Paragraph("Generative UI: micro-aplicaciones y widgets interactivos embebidos.", table_cell)]
    ]
    t_mat = Table(table_mat_data, colWidths=[110, 190, 223.27])
    t_mat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_mat)

    doc.build(story, canvasmaker=NumberedCanvas)
    
    import shutil
    shutil.copyfile(PDF_PATH, BKP_PDF_PATH)
    print(f"✅ PDF generado con éxito: {PDF_PATH} (y copia en {BKP_PDF_PATH})", flush=True)

if __name__ == "__main__":
    compilar_html()
    compilar_pdf_reportlab()
