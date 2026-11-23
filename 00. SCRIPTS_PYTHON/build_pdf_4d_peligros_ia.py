#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_4d_peligros_ia.py
Genera la Guía Maestra Técnica y Didáctica:
'LAS 4 D DEL PELIGRO DEL CÓDIGO IA Y CÓMO LAS SOLUCIONAMOS'
(Duplicación, Drift, Deluge y Deception vs. Protocolos de Gobernanza de Antigravity)

Destino:
CURSO-IA/CLASES/7. MAPA_GESTION_PROYECTO_CON_IA/
Archivos generados:
1. LAS_4D_DEL_CODIGO_IA_Y_NUESTRAS_SOLUCIONES.pdf
2. LAS_4D_DEL_CODIGO_IA_Y_NUESTRAS_SOLUCIONES.html
3. LAS_4D_DEL_CODIGO_IA_Y_NUESTRAS_SOLUCIONES.docx (mediante textutil nativo)
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
PDF_PATH = os.path.join(TARGET_DIR, "LAS_4D_DEL_CODIGO_IA_Y_NUESTRAS_SOLUCIONES.pdf")
HTML_PATH = os.path.join(TARGET_DIR, "LAS_4D_DEL_CODIGO_IA_Y_NUESTRAS_SOLUCIONES.html")
DOCX_PATH = os.path.join(TARGET_DIR, "LAS_4D_DEL_CODIGO_IA_Y_NUESTRAS_SOLUCIONES.docx")

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
    """Genera la versión HTML limpia y estilizada para visualización o conversión a DOCX."""
    html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Las 4 D del Peligro del Código IA y Nuestras Soluciones</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; line-height: 1.6; color: #1e293b; max-width: 900px; margin: 40px auto; padding: 0 20px; }
        h1 { color: #0f172a; border-bottom: 2px solid #0284c7; padding-bottom: 10px; }
        h2 { color: #0369a1; margin-top: 30px; border-left: 4px solid #0284c7; padding-left: 12px; }
        h3 { color: #0f172a; margin-top: 20px; }
        .danger-box { background: #fef2f2; border: 1px solid #f87171; border-radius: 8px; padding: 15px; margin: 15px 0; }
        .solution-box { background: #f0fdf4; border: 1px solid #4ade80; border-radius: 8px; padding: 15px; margin: 15px 0; }
        .quote-box { background: #f8fafc; border-left: 4px solid #64748b; padding: 12px 18px; font-style: italic; margin: 20px 0; }
        table { width: 100%; border-collapse: collapse; margin: 25px 0; }
        th, td { border: 1px solid #cbd5e1; padding: 10px 14px; text-align: left; }
        th { background: #f1f5f9; color: #0f172a; font-weight: bold; }
        code { background: #e2e8f0; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 0.9em; }
    </style>
</head>
<body>
    <h1>Las 4 D del Peligro del Código IA y Nuestras Soluciones</h1>
    <p><strong>Ecosistema Formativo y Personal • Monográfico 6: Gestión del Proyecto con IA</strong><br>
    <em>Análisis crítico del fenómeno 'Vibe Coding' y las salvaguardas de gobernanza agéntica.</em></p>

    <div class="quote-box">
        «El verdadero peligro no es que la inteligencia artificial escriba código, sino que dejemos de verificarlo.»<br>
        <strong>— NeroCode (@nerocode)</strong>
    </div>

    <h2>1. Contexto: El Fenómeno del 'Vibe Coding' y la Trampa de la Velocidad</h2>
    <p>En la era actual del desarrollo con modelos de lenguaje avanzados (ChatGPT, Claude, Gemini, Antigravity), programar parece haberse convertido en un ejercicio casi instantáneo. Es posible generar cientos o miles de líneas de código en cuestión de minutos simplemente describiendo una idea.</p>
    <p>Sin embargo, esta velocidad descontrolada esconde una trampa estructural: <strong>la falsa ilusión de perfección</strong>. Un modelo generativo no "entiende" la arquitectura a largo plazo; genera la continuación probabilística más plausible para el prompt inmediato. Sin salvaguardas explícitas, el código resultante acumula silenciosamente cuatro patologías fundamentales conocidas como <strong>Las 4 D del peligro de la IA</strong>: <em>Duplicación</em>, <em>Drift</em>, <em>Deluge</em> y <em>Deception</em>.</p>

    <h2>2. Fallo 1: DUPLICACIÓN (Duplication)</h2>
    <div class="danger-box">
        <strong>⚠️ El Peligro en la IA:</strong> Cuando se solicita una nueva funcionalidad, el impulso inmediato del modelo es volver a programarla desde cero en cada archivo, reescribiendo constantes, funciones de utilidad y clases que ya existían en el repositorio. El resultado es una base de código fragmentada, redundante e imposible de mantener.
    </div>
    <div class="solution-box">
        <strong>🛡️ Nuestras Soluciones en el Ecosistema:</strong>
        <ul>
            <li><strong>Documento Vivo Centralizado (<code>ESTADO_GLOBAL_PROYECTOS.md</code>):</strong> Actúa como memoria central y relevo permanente entre sesiones. La IA está obligada a consultar este inventario antes de codificar para identificar scripts y utilidades preexistentes.</li>
            <li><strong>Librerías Base Reutilizables:</strong> Módulos maestros compartidos como <code>NativePDFWriter</code>, generadores centrales de bitácora y scripts de procesamiento por lotes que centralizan la lógica común.</li>
            <li><strong>Curaduría y Desduplicación Estricta:</strong> Como en el módulo de música Korg EK-50, donde se impone la <em>Regla de los 8 Sonidos Únicos</em>, purgando y comparando las cabeceras HUD para prohibir instrumentos repetidos o redundantes.</li>
        </ul>
    </div>

    <h2>3. Fallo 2: DRIFT (Desviación / Deriva de Contexto)</h2>
    <div class="danger-box">
        <strong>⚠️ El Peligro en la IA:</strong> A medida que la conversación acumula miles de tokens, el modelo sufre fatiga cognitiva y "ceguera de contexto". Se aleja paulatinamente de las instrucciones iniciales, altera la estructura de carpetas, acorta nombres canónicos o inventa abreviaturas que rompen la arquitectura acordada.
    </div>
    <div class="solution-box">
        <strong>🛡️ Nuestras Soluciones en el Ecosistema:</strong>
        <ul>
            <li><strong>Protocolo Elephant-Goldfish (Google Architecture):</strong> Separación de roles: el <em>Elefante</em> (coordinador) mantiene la memoria y planifica; el <em>Goldfish</em> (subagente efímero) nace con mente limpia para auditar el código contra una lista de control estricta y se destruye de inmediato sin dejar procesos zombi.</li>
            <li><strong>Catálogos Canónicos Estrictos:</strong> Prohibición radical de abreviaturas inventadas. En NASA Eyes se exige el ID exacto (<code>sc_roman_space_telescope</code>, nunca <code>sc_roman</code>); en Korg EK-50, Banco Maestro MSB 33 y numeración formal de 3 dígitos (<code>029 Harmonica</code>).</li>
            <li><strong>Doble Contador Correlativo:</strong> Mantenimiento de dos contadores estrictamente independientes (Contador General <code>[COMANDO 181]</code> y Contador Música <code>[COMANDO MÚSICA 181]</code>) para asegurar la trazabilidad cronológica.</li>
        </ul>
    </div>

    <h2>4. Fallo 3: DELUGE (Diluvio de Código y Sobre-Ingeniería)</h2>
    <div class="danger-box">
        <strong>⚠️ El Peligro en la IA:</strong> La tendencia del modelo a inflar el proyecto ("vomitar" código excesivo), sugiriendo frameworks pesados, dependencias de terceros (<code>npm</code>, librerías <code>pip</code> ajenas) o arquitecturas mastodónticas para problemas que se resolvían con unas pocas líneas de código nativo.
    </div>
    <div class="solution-box">
        <strong>🛡️ Nuestras Soluciones en el Ecosistema:</strong>
        <ul>
            <li><strong>Regla de Cero Herramientas Nuevas ni Instalaciones Externas:</strong> Prohibición estricta de instalar paquetes adicionales. Todo se construye con las herramientas nativas preexistentes de macOS y la biblioteca estándar de Python (<code>urllib</code>, <code>xml</code>, AppleScript).</li>
            <li><strong>Diferenciación Clara de Motores 3D:</strong> Prohibición de Babylon.js en simuladores anatómicos/médicos de IA (donde se exige Three.js limpio o Canvas fotográfico hiperrealista) mientras se reserva y mantiene Babylon.js al 100% como motor oficial en Robótica (aprovechando sus shaders y física Havok).</li>
            <li><strong>La Triple Salvaguarda Pedagógica (+65):</strong> Cero código intermedio para el alumno senior. Micro-aplicaciones contenidas en un único archivo <code>.html</code> autónomo que funciona con doble clic sin dependencias.</li>
        </ul>
    </div>

    <h2>5. Fallo 4: DECEPTION (Engaño / Ilusión de Funcionamiento)</h2>
    <div class="danger-box">
        <strong>⚠️ El Peligro en la IA:</strong> Es la patología más traicionera: el código compila y la interfaz se ve impecable, pero por dentro es una simulación hueca (datos estáticos falsos, llamadas a APIs bloqueadas o sondas espaciales orbitando la Tierra en lugar de Venus por omisión de parámetros temporales).
    </div>
    <div class="solution-box">
        <strong>🛡️ Nuestras Soluciones en el Ecosistema:</strong>
        <ul>
            <li><strong>Obligación de Autocomprobación Previa y Poda Temprana:</strong> Si una malla 3D, sonda o telemetría no existe o no se mueve en el motor real, no se maquilla ni se inventa: se poda de raíz y se sustituye de inmediato por un activo 100% verificado.</li>
            <li><strong>Calibración Temporal de Sondas Históricas:</strong> Inyección obligatoria de marcas temporales UTC (<code>time=YYYY-MM-DD...</code>) para ubicar las sondas en su fecha activa y planeta real.</li>
            <li><strong>Blindaje ante Restricciones del Navegador:</strong> Supresión de enlaces directos a WhatsApp (<code>api.whatsapp.com</code>) bloqueados por la política COOP de Safari, adoptando la publicación nativa en Gemini Canvas.</li>
            <li><strong>Copia de Respaldo Garantizada (BKP Oficial):</strong> Botón de respaldo local probado en cada mapa interactivo para asegurar que el 100% de los alumnos disfrute de la experiencia completa sin atascos de red.</li>
        </ul>
    </div>

    <h2>6. Matriz Resumen de Gobernanza</h2>
    <table>
        <thead>
            <tr>
                <th>Peligro de la IA</th>
                <th>Manifestación Crítica</th>
                <th>Protocolo de Gobernanza Aplicado</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>1. Duplicación</strong></td>
                <td>Reescritura de utilidades y funciones redundantes.</td>
                <td>Documento vivo <code>ESTADO_GLOBAL_PROYECTOS.md</code> y librerías base compartidas.</td>
            </tr>
            <tr>
                <td><strong>2. Drift</strong></td>
                <td>Pérdida de arquitectura y abreviaturas inventadas.</td>
                <td>Arquitectura Elephant-Goldfish, catálogos canónicos y doble contador correlativo.</td>
            </tr>
            <tr>
                <td><strong>3. Deluge</strong></td>
                <td>Sobre-ingeniería, dependencias externas e inflación.</td>
                <td>Cero herramientas nuevas, herramientas nativas del sistema y micro-apps atómicas.</td>
            </tr>
            <tr>
                <td><strong>4. Deception</strong></td>
                <td>Ilusión de funcionamiento, enlaces rotos y datos falsos.</td>
                <td>Autocomprobación obligatoria, calibración temporal y copias BKP garantizadas.</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ HTML generado: {HTML_PATH}", flush=True)

    # Convertir a DOCX nativo con textutil
    cmd = ["/usr/bin/textutil", "-convert", "docx", "-output", DOCX_PATH, HTML_PATH]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"✅ DOCX generado con textutil: {DOCX_PATH}", flush=True)
    else:
        print(f"⚠️ textutil warning: {res.stderr}", flush=True)

def compilar_pdf_reportlab():
    """Compila el PDF oficial con diseño editorial elegante en ReportLab."""
    print("Compilando PDF oficial con ReportLab...", flush=True)
    
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=32,
        bottomMargin=38
    )

    PAGE_WIDTH = A4[0] - 72 # 523.27 pt

    styles = getSampleStyleSheet()

    c_navy = colors.HexColor('#0F172A')
    c_blue = colors.HexColor('#0284C7')
    c_dark_blue = colors.HexColor('#0369A1')
    c_slate = colors.HexColor('#475569')
    c_danger_bg = colors.HexColor('#FEF2F2')
    c_danger_border = colors.HexColor('#F87171')
    c_danger_text = colors.HexColor('#991B1B')
    c_sol_bg = colors.HexColor('#F0FDF4')
    c_sol_border = colors.HexColor('#4ADE80')
    c_sol_text = colors.HexColor('#166534')
    c_quote_bg = colors.HexColor('#F8FAFC')

    title_style = ParagraphStyle(
        'DocTitle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=15, leading=19,
        textColor=c_navy, alignment=1, spaceAfter=2
    )
    sub_style = ParagraphStyle(
        'DocSub', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.5, leading=12,
        textColor=c_blue, alignment=1, spaceAfter=8
    )
    h1_style = ParagraphStyle(
        'SecH1', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=10.5, leading=14,
        textColor=c_dark_blue, spaceBefore=8, spaceAfter=3
    )
    body_style = ParagraphStyle(
        'DocBody', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8, leading=11.5,
        textColor=colors.HexColor('#1E293B'), spaceAfter=4
    )
    quote_style = ParagraphStyle(
        'DocQuote', parent=styles['Normal'],
        fontName='Helvetica-Oblique', fontSize=8, leading=11.5,
        textColor=colors.HexColor('#334155'), alignment=1
    )
    danger_title = ParagraphStyle(
        'DangerTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8, leading=11,
        textColor=c_danger_text
    )
    danger_body = ParagraphStyle(
        'DangerBody', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.5, leading=10.5,
        textColor=colors.HexColor('#7F1D1D')
    )
    sol_title = ParagraphStyle(
        'SolTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8, leading=11,
        textColor=c_sol_text
    )
    sol_body = ParagraphStyle(
        'SolBody', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.5, leading=10.5,
        textColor=colors.HexColor('#14532D')
    )
    table_header = ParagraphStyle(
        'TH', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=7.5, leading=10,
        textColor=colors.HexColor('#0F172A'), alignment=1
    )
    table_cell = ParagraphStyle(
        'TC', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7, leading=9.5,
        textColor=colors.HexColor('#1E293B')
    )
    table_cell_bold = ParagraphStyle(
        'TCB', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=7, leading=9.5,
        textColor=colors.HexColor('#0F172A')
    )

    story = []

    # Cabecera
    story.append(Paragraph("LAS 4 D DEL PELIGRO DEL CÓDIGO IA Y NUESTRAS SOLUCIONES", title_style))
    story.append(Paragraph("MONOGRÁFICO 6: GESTIÓN DEL PROYECTO CON IA • ANÁLISIS TÉCNICO Y SALVAGUARDAS DE GOBERNANZA", sub_style))
    story.append(HRFlowable(width="100%", thickness=1, color=c_blue, spaceBefore=0, spaceAfter=6))

    # Cita de apertura
    quote_data = [[
        Paragraph("«El verdadero peligro no es que la inteligencia artificial escriba código, sino que dejemos de verificarlo.»<br/><b>— NeroCode (@nerocode)</b>", quote_style)
    ]]
    t_quote = Table(quote_data, colWidths=[PAGE_WIDTH])
    t_quote.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_quote_bg),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(t_quote)
    story.append(Spacer(1, 6))

    # 1. Contexto
    story.append(Paragraph("1. El Fenómeno del 'Vibe Coding' y la Trampa de la Velocidad en 2026", h1_style))
    story.append(Paragraph(
        "En la actualidad, herramientas como ChatGPT, Claude, Gemini y Antigravity permiten generar aplicaciones completas y redactar miles de líneas de código en minutos. Sin embargo, esta velocidad introduce un sesgo cognitivo crítico: <b>la falsa ilusión de perfección</b>. El modelo genera código estadísticamente verosímil pero carente de visión holística a largo plazo. Sin directivas estrictas de gobernanza, el proyecto degenera inevitablemente en cuatro patologías estructurales: <b>Duplicación</b>, <b>Drift</b>, <b>Deluge</b> y <b>Deception</b>.",
        body_style
    ))
    story.append(Spacer(1, 4))

    def make_section_box(number_str, title_str, danger_text, solution_bullets):
        elements = []
        elements.append(Paragraph(f"{number_str} {title_str}", h1_style))
        
        # Caja de peligro
        p_danger = [
            Paragraph("⚠️ EL PELIGRO EN LA IA:", danger_title),
            Spacer(1, 2),
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
        elements.append(Spacer(1, 3))

        # Caja de solución
        p_sol = [
            Paragraph("🛡️ NUESTRA SOLUCIÓN EN EL ECOSISTEMA AGÉNTICO:", sol_title),
            Spacer(1, 2)
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
        elements.append(Spacer(1, 6))
        return KeepTogether(elements)

    # 2. DUPLICACIÓN
    story.append(make_section_box(
        "2.", "DUPLICACIÓN (Duplication)",
        "Cuando se solicita una nueva tarea, el modelo tiende a reescribir funciones de utilidad, estilos y lógica que ya existían previamente en otros archivos del repositorio. Esto fragmenta la base de código, multiplica los puntos de fallo y convierte el mantenimiento en una pesadilla.",
        [
            "<b>Documento Vivo Centralizado (ESTADO_GLOBAL_PROYECTOS.md):</b> Inventario permanente que el agente consulta de forma obligatoria antes de codificar para identificar scripts, directivas y estados preexistentes sin duplicar.",
            "<b>Librerías Base Reutilizables y Scripts Maestros:</b> Estandarización en módulos centrales (ej. <code>NativePDFWriter</code>, generadores de bitácora y scripts batch) en lugar de dispersar código repetido.",
            "<b>Curaduría y Desduplicación Estricta:</b> Aplicada por ejemplo en el módulo musical Korg EK-50 con la <i>Regla de los 8 Sonidos Únicos</i>, donde el agente compara las filas del HUD y purga sistemáticamente cualquier botón redundante."
        ]
    ))

    # 3. DRIFT
    story.append(make_section_box(
        "3.", "DRIFT (Desviación / Deriva de Contexto)",
        "A medida que la sesión acumula miles de tokens, el modelo sufre de 'ceguera de contexto'. Pierde el hilo de las directivas fundacionales, olvida estándares acordados, altera jerarquías de carpetas o inventa abreviaturas que rompen la arquitectura original.",
        [
            "<b>Arquitectura Elephant-Goldfish (Google Architecture):</b> El 'Elefante' (coordinador) mantiene la memoria histórica y planifica; el 'Goldfish' (subagente efímero) nace con mente virgen para auditar el código contra una lista de control estricta y se destruye inmediatamente sin dejar procesos residuales.",
            "<b>Catálogos Canónicos Estrictos:</b> Prohibición absoluta de abreviaturas inventadas. En NASA Eyes se exige el ID exacto (<code>sc_roman_space_telescope</code>, nunca <code>sc_roman</code>); en Korg EK-50, Banco Maestro MSB 33 y numeración formal de 3 dígitos (<code>029 Harmonica</code>).",
            "<b>Doble Contador Correlativo de Comandos:</b> Control cronológico estricto entre el Contador General (<code>[COMANDO 181]</code>) y el Contador Música (<code>[COMANDO MÚSICA 181]</code>) para anclar cada avance sin desviaciones."
        ]
    ))

    # 4. DELUGE
    story.append(make_section_box(
        "4.", "DELUGE (Diluvio de Código y Sobre-Ingeniería)",
        "La propensión de la IA a inflar el proyecto ('vomitar' cientos de líneas innecesarias), agregando frameworks pesados, dependencias externas superfluas (npm, librerías pip ajenas) y arquitecturas complejas que luego se rompen por obsolescencia.",
        [
            "<b>Regla de Cero Herramientas Nuevas ni Instalaciones Externas:</b> Prohibición tajante de instalar paquetes de terceros. Se opera exclusivamente con herramientas nativas de macOS y Python estándar (<code>urllib</code>, <code>xml</code>, AppleScript).",
            "<b>Diferenciación Clara de Motores 3D:</b> Prohibición de Babylon.js en simuladores anatómicos/médicos de IA (donde se exige Three.js limpio o Canvas fotográfico hiperrealista) mientras se reserva y mantiene Babylon.js al 100% como motor oficial en Robótica (aprovechando sus shaders y física Havok).",
            "<b>La Triple Salvaguarda Pedagógica y Cero Código Intermedio (+65):</b> Los alumnos senior no manipulan código fuente; reciben micro-aplicaciones autónomas de 1 página que funcionan al 100% con doble clic en cualquier navegador sin servidor ni dependencias."
        ]
    ))

    # 5. DECEPTION
    story.append(make_section_box(
        "5.", "DECEPTION (Engaño / Ilusión de Funcionamiento)",
        "El fallo más peligroso y sutil: el código compila y la interfaz luce atractiva, pero por dentro es una simulación hueca (datos estáticos falsos, llamadas a APIs bloqueadas o sondas espaciales que orbitan la Tierra en lugar de Venus por omisión de parámetros temporales).",
        [
            "<b>Obligación de Autocomprobación Previa y Poda Temprana:</b> Si un enlace, telemetría o malla 3D no existe o no se mueve en el motor real, no se maquilla ni se inventa: se poda de inmediato y se sustituye por un activo 100% verificado.",
            "<b>Calibración Temporal Obligatoria:</b> Inyección de marcas temporales UTC (<code>time=YYYY-MM-DD...</code>) en misiones históricas para situar las naves en su destino real y no en el despegue.",
            "<b>Blindaje ante Políticas de Seguridad del Navegador:</b> Eliminación de enlaces directos a WhatsApp bloqueados por COOP en Safari, adoptando la publicación nativa en Gemini Canvas.",
            "<b>Copia de Respaldo Oficial BKP Garantizada al 100%:</b> Cada simulador cuenta en el mapa con su botón oficial BKP probado, garantizando el funcionamiento en el aula sin depender de la red ni de la IA en tiempo real."
        ]
    ))

    # 6. Tabla Resumen
    story.append(Paragraph("6. Matriz Ejecutiva: Patología de la IA vs. Salvaguarda Agéntica", h1_style))
    table_data = [
        [Paragraph("Peligro de la IA (Las 4 D)", table_header), Paragraph("Manifestación Crítica en Código", table_header), Paragraph("Protocolo de Gobernanza Aplicado", table_header)],
        [Paragraph("<b>1. Duplicación</b>", table_cell_bold), Paragraph("Reinvención de utilidades y funciones redundantes.", table_cell), Paragraph("Documento vivo <code>ESTADO_GLOBAL_PROYECTOS.md</code> y módulos compartidos.", table_cell)],
        [Paragraph("<b>2. Drift</b>", table_cell_bold), Paragraph("Pérdida de directivas fundacionales y abreviaturas inventadas.", table_cell), Paragraph("Arquitectura Elephant-Goldfish, catálogos canónicos y doble contador correlativo.", table_cell)],
        [Paragraph("<b>3. Deluge</b>", table_cell_bold), Paragraph("Sobre-ingeniería, frameworks pesados y dependencias rotas.", table_cell), Paragraph("Cero herramientas nuevas, librerías estándar nativas y micro-apps atómicas.", table_cell)],
        [Paragraph("<b>4. Deception</b>", table_cell_bold), Paragraph("Ilusión de funcionamiento, APIs bloqueadas y datos falsos.", table_cell), Paragraph("Autocomprobación obligatoria, calibración temporal y copias BKP garantizadas.", table_cell)]
    ]
    t_matriz = Table(table_data, colWidths=[110, 190, 223.27])
    t_matriz.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_matriz)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"✅ PDF generado con éxito: {PDF_PATH}", flush=True)

if __name__ == "__main__":
    compilar_html()
    compilar_pdf_reportlab()
