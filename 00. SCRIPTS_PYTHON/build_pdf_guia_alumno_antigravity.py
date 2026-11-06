#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_guia_alumno_antigravity.py
Genera la Guía Didáctica Oficial del Alumno:
GUIA_ALUMNO_ANTIGRAVITY_Y_CONTROL_FICHEROS.pdf y .docx
dentro de:
CURSO-IA/CLASES/6. NASA_Y_EXPLORACION_ESPACIAL_CON_IA/

Contenido:
- Checklist completo de instalación y puesta en marcha de Antigravity.
- El secreto de la Carpeta Raíz Única para evitar ventanas de aprobación ("Submits").
- Directivas de gobernanza (AGENTS.md y GEMINI.md) para trabajo silencioso y desatendido.
- Casuística práctica de manipulación de archivos y carpetas mediante lenguaje natural:
  1. Crear 3 carpetas temáticas y un archivo en cada una.
  2. Modificar y ampliar un archivo existente (edit_file).
  3. Borrar selectivamente un archivo en otra carpeta.
  4. Mover y renombrar archivos entre carpetas.
  5. Búsqueda y consolidación semántica.
  6. Creación de visores y aplicaciones interactivas HTML.
- El comando final de terminal con títulos visibles mediante echo.
"""

import os
import sys
import subprocess

TARGET_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/6. NASA_Y_EXPLORACION_ESPACIAL_CON_IA"
HTML_PATH = os.path.join(TARGET_DIR, "GUIA_ALUMNO_ANTIGRAVITY_Y_CONTROL_FICHEROS.html")
DOCX_PATH = os.path.join(TARGET_DIR, "GUIA_ALUMNO_ANTIGRAVITY_Y_CONTROL_FICHEROS.docx")
PDF_PATH = os.path.join(TARGET_DIR, "GUIA_ALUMNO_ANTIGRAVITY_Y_CONTROL_FICHEROS.pdf")

def compilar_docx_nativo():
    """Genera versión Word DOCX usando el motor oficial de macOS textutil."""
    print("1. Compilando Microsoft Word DOCX nativo con textutil...", flush=True)
    if os.path.isfile(HTML_PATH):
        cmd = [
            "/usr/bin/textutil",
            "-convert", "docx",
            "-output", DOCX_PATH,
            HTML_PATH
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"   ✅ DOCX generado con éxito: {DOCX_PATH}", flush=True)
        else:
            print(f"   ⚠️ textutil warning: {res.stderr}", flush=True)
    else:
        print("   ⚠️ HTML_PATH no encontrado para textutil.", flush=True)

def compilar_pdf_reportlab():
    """Genera el PDF oficial de alta resolución con ReportLab."""
    print("2. Compilando PDF oficial con ReportLab...", flush=True)
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import (
            SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
        )
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib import colors

        PAGE_WIDTH = A4[0] - 72 # 523.27 pt ancho útil

        doc = SimpleDocTemplate(
            PDF_PATH,
            pagesize=A4,
            rightMargin=36,
            leftMargin=36,
            topMargin=32,
            bottomMargin=32
        )

        styles = getSampleStyleSheet()

        c_navy = colors.HexColor('#0F172A')
        c_blue = colors.HexColor('#0284C7')
        c_slate = colors.HexColor('#475569')
        c_dark = colors.HexColor('#1E293B')
        c_green = colors.HexColor('#059669')
        c_amber = colors.HexColor('#D97706')
        c_red = colors.HexColor('#DC2626')
        c_card_bg = colors.HexColor('#F8FAFC')
        c_box_border = colors.HexColor('#CBD5E1')

        title_style = ParagraphStyle(
            'DocTitle', parent=styles['Heading1'],
            fontName='Helvetica-Bold', fontSize=15, leading=19,
            textColor=c_navy, alignment=1, spaceAfter=3
        )
        sub_style = ParagraphStyle(
            'DocSub', parent=styles['Normal'],
            fontName='Helvetica-Oblique', fontSize=9, leading=13,
            textColor=c_slate, alignment=1, spaceAfter=8
        )
        h1_style = ParagraphStyle(
            'SecH1', parent=styles['Heading2'],
            fontName='Helvetica-Bold', fontSize=11, leading=14,
            textColor=c_blue, spaceBefore=8, spaceAfter=3
        )
        h2_style = ParagraphStyle(
            'SecH2', parent=styles['Heading3'],
            fontName='Helvetica-Bold', fontSize=9.5, leading=12.5,
            textColor=c_navy, spaceBefore=6, spaceAfter=2
        )
        body_style = ParagraphStyle(
            'Body', parent=styles['Normal'],
            fontName='Helvetica', fontSize=8.2, leading=11.5,
            textColor=c_dark, spaceAfter=3
        )
        body_bold = ParagraphStyle(
            'BodyBold', parent=body_style,
            fontName='Helvetica-Bold'
        )
        prompt_style = ParagraphStyle(
            'PromptStyle', parent=styles['Normal'],
            fontName='Helvetica-Oblique', fontSize=8.2, leading=11.2,
            textColor=colors.HexColor('#0369A1')
        )
        code_style = ParagraphStyle(
            'CodeStyle', parent=styles['Normal'],
            fontName='Courier', fontSize=7.6, leading=10.2,
            textColor=colors.HexColor('#0F172A')
        )
        badge_style = ParagraphStyle(
            'BadgeStyle', parent=styles['Normal'],
            fontName='Helvetica-Bold', fontSize=7.2, leading=9.5,
            textColor=colors.white, alignment=1
        )

        def make_callout(text, bg_hex='#F0F9FF', border_hex='#38BDF8', pad=6):
            p = Paragraph(text, body_style)
            t = Table([[p]], colWidths=[PAGE_WIDTH])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg_hex)),
                ('BOX', (0,0), (-1,-1), 1, colors.HexColor(border_hex)),
                ('TOPPADDING', (0,0), (-1,-1), pad),
                ('BOTTOMPADDING', (0,0), (-1,-1), pad),
                ('LEFTPADDING', (0,0), (-1,-1), 8),
                ('RIGHTPADDING', (0,0), (-1,-1), 8),
            ]))
            return t

        story = []

        # ENCABEZADO PRINCIPAL
        story.append(Paragraph("GUÍA DIDÁCTICA Y CHECKLIST: TU PRIMER DÍA CON ANTIGRAVITY", title_style))
        story.append(Paragraph("De la Puesta en Marcha 'Cero-Submits' a la Manipulación Total de Ficheros por Diálogo Natural &bull; Monográfico 7 (NASA e IA)", sub_style))
        story.append(HRFlowable(width="100%", thickness=1.5, color=c_blue, spaceAfter=6))

        # INTRODUCCIÓN GENERAL
        intro_html = (
            "<b>🎯 OBJETIVO PARA EL ALUMNO:</b> En este taller aprendes a trabajar con <b>Antigravity</b>, "
            "el entorno agéntico de Google DeepMind. A diferencia de un chatbot tradicional (que solo habla en una ventanita), "
            "un <b>Agente Autónomo</b> puede crear carpetas, escribir documentos, corregir errores y construir simuladores "
            "reales en tu ordenador mientras tú solo le das instrucciones en español normal. "
            "Sigue esta checklist paso a paso para dominarlo con total seguridad y cero interrupciones."
        )
        story.append(make_callout(intro_html, '#F0FDF4', '#34D399', 6))
        story.append(Spacer(1, 5))

        # BLOQUE 1: CHECKLIST DE INSTALACIÓN Y CONFIGURACIÓN
        story.append(Paragraph("BLOQUE 1: CHECKLIST DE INSTALACIÓN Y REGLA DE ORO 'CERO SUBMITS'", h1_style))

        chk_data = [
            [
                Paragraph("<b>PASO</b>", body_bold),
                Paragraph("<b>ACCIÓN DEL ALUMNO</b>", body_bold),
                Paragraph("<b>POR QUÉ ES VITAL (EL SECRETO TÉCNICO)</b>", body_bold)
            ],
            [
                Paragraph("<b>1. Descarga e Instalación</b>", body_style),
                Paragraph("Descarga Antigravity y arrástralo a tu carpeta de <i>Aplicaciones</i> en macOS.", body_style),
                Paragraph("Queda instalado en el sistema con acceso a las herramientas estándar (Python, AppleScript).", body_style)
            ],
            [
                Paragraph("<b>2. Carpeta Raíz Única<br/>(Workspace)</b>", body_style),
                Paragraph("<b>CREA UNA SOLA CARPETA</b> para todo el proyecto (ej: <code>TALLER_IA</code>) y ábrela en Antigravity con <i>'Open Folder'</i>.", body_style),
                Paragraph("<b>¡LA CLAVE ANTISUBMITS!</b> Si abres archivos sueltos desde Descargas o Escritorio, macOS pedirá permisos a cada segundo. Al usar una sola carpeta raíz, <b>todo queda preautorizado</b> dentro de ella.", body_style)
            ],
            [
                Paragraph("<b>3. Reglas Maestras<br/>(AGENTS.md / GEMINI.md)</b>", body_style),
                Paragraph("Crea en la raíz los archivos <code>AGENTS.md</code> y <code>GEMINI.md</code> indicando trabajar en silencio.", body_style),
                Paragraph("Son las <i>Leyes del Agente</i>: le ordenan no detenerse a pedir confirmación para cada acción intermedia (<code>RequestFeedback: false</code>) y trabajar de corrido.", body_style)
            ],
            [
                Paragraph("<b>4. Flujo Silencioso y Comando Final</b>", body_style),
                Paragraph("Hablas con el agente, él trabaja en silencio y al terminar te da un bloque final de terminal limpio.", body_style),
                Paragraph("Títulos visibles en terminal (<code>echo</code>) para que copies y pegues con total control sin escribir código complejo.", body_style)
            ],
        ]
        chk_table = Table(chk_data, colWidths=[110, 213, 200])
        chk_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E2E8F0')),
            ('GRID', (0,0), (-1,-1), 0.5, c_box_border),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ('BACKGROUND', (0,2), (-1,2), colors.HexColor('#FEF3C7')), # highlight golden rule
        ]))
        story.append(chk_table)
        story.append(Spacer(1, 6))

        # BLOQUE 2: CASUÍSTICA PRÁCTICA DE FICHEROS
        story.append(Paragraph("BLOQUE 2: CASUÍSTICA COMPLETA DE MANIPULACIÓN DE ARCHIVOS POR LENGUAJE NATURAL", h1_style))
        story.append(Paragraph("Así es como tú (el Director) le hablas a Antigravity para que gestione todo tu disco duro sin tocar la terminal:", body_style))
        story.append(Spacer(1, 3))

        casos = [
            (
                "CASO 1: Creación de Estructura Inicial (3 Carpetas Temáticas + 1 Fichero en cada una)",
                "«Antigravity, organiza mi espacio de trabajo creando tres carpetas: 1. PLANES_DE_VIAJE, 2. RECETAS_SALUDABLES y 3. ASTRONOMIA_NASA. Dentro de cada una, crea un archivo inicial en Markdown (.md) con un título, una breve introducción y 3 ideas clave.»",
                "Usa <code>write_file</code>. Crea automáticamente los directorios y los ficheros formateados (ej: <code>1. PLANES_DE_VIAJE/itinerario.md</code>, etc.). No tienes que hacer <code>mkdir</code> ni crear carpetas a mano.",
                "#059669", "CREACIÓN MASIVA"
            ),
            (
                "CASO 2: Modificación y Ampliación Quirúrgica de un Fichero Existente",
                "«Antigravity, abre el archivo RECETAS_SALUDABLES/menu_semanal.md y añade al final una receta tradicional de Gazpacho Andaluz con ingredientes para 4 personas y pasos de preparación.»",
                "Usa <code>read_file</code> para examinar el documento y <code>edit_file</code> para insertar el nuevo bloque exactamente donde corresponde, respetando todo lo que ya habías escrito sin borrar nada.",
                "#0284C7", "EDICIÓN QUIRÚRGICA"
            ),
            (
                "CASO 3: Borrado Selectivo y Seguro de un Fichero en otra Carpeta",
                "«Antigravity, dentro de la carpeta PLANES_DE_VIAJE, elimina el archivo notas_antiguas.txt que ya no utilizo.»",
                "Elimina únicamente el fichero solicitado. Gracias al blindaje de la carpeta raíz, el agente NUNCA puede tocar nada fuera de tu proyecto (tus fotos, correos o sistema operativo están 100% a salvo).",
                "#DC2626", "BORRADO PRECISO"
            ),
            (
                "CASO 4: Mover y Renombrar Archivos entre Carpetas",
                "«Antigravity, traslada el archivo misiones.md de ASTRONOMIA_NASA a una nueva subcarpeta llamada SONDAS_HISTORICAS y renómbralo como 01_apolo_y_voyager.md.»",
                "Crea la subcarpeta de destino, escribe el contenido con el nuevo nombre y elimina el archivo de origen para mantener el disco limpio y ordenado sin ficheros duplicados.",
                "#D97706", "REORGANIZACIÓN"
            ),
            (
                "CASO 5: Búsqueda y Consolidación Semántica en Todo el Proyecto",
                "«Antigravity, revisa todos los archivos de mis carpetas, busca dónde he hablado de 'ingredientes saludables' o 'frutas' y crea en la raíz un archivo RESUMEN_NUTRICIONAL.md con un índice consolidado.»",
                "Lee todos los archivos, localiza las coincidencias por contexto y genera un documento resumen con enlaces a cada archivo de origen.",
                "#7C3AED", "ANÁLISIS GLOBAL"
            ),
            (
                "CASO 6: Generación de Simuladores y Aplicaciones Web (HTML5 + Three.js / Canvas)",
                "«Antigravity, dentro de ASTRONOMIA_NASA genera una aplicación web visor_solar.html con iframe conectado a NASA Eyes, barra de 11 planetas y tarjeta HUD lateral con datos astronómicos.»",
                "Genera el código web completo y funcional al 100%. Solo tienes que hacer doble clic en el archivo para verlo funcionar en tu navegador Safari o Chrome al instante.",
                "#0EA5E9", "APP WEB COMPLETA"
            ),
        ]

        for num_tit, prompt_txt, accion_txt, badge_col, badge_label in casos:
            c_data = [
                [
                    Paragraph(f"<b>{num_tit}</b>", h2_style),
                    Paragraph(f"<font color='{badge_col}'><b>[{badge_label}]</b></font>", badge_style)
                ],
                [
                    Paragraph(f"<b>🗣️ Lo que tú le dices (Prompt):</b><br/>{prompt_txt}", prompt_style),
                    Paragraph(f"<b>⚙️ Lo que Antigravity hace por dentro:</b><br/>{accion_txt}", body_style)
                ]
            ]
            c_table = Table(c_data, colWidths=[270, 253])
            c_table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), c_card_bg),
                ('GRID', (0,0), (-1,-1), 0.5, c_box_border),
                ('TOPPADDING', (0,0), (-1,-1), 3),
                ('BOTTOMPADDING', (0,0), (-1,-1), 3),
                ('LEFTPADDING', (0,0), (-1,-1), 6),
                ('RIGHTPADDING', (0,0), (-1,-1), 6),
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ]))
            story.append(KeepTogether([c_table, Spacer(1, 3)]))

        story.append(Spacer(1, 3))

        # BLOQUE 3: EL COMANDO DE TERMINAL FINAL
        story.append(Paragraph("BLOQUE 3: EL COMANDO EXTERNO DE TERMINAL (CUÁNDO Y CÓMO COPIARLO)", h1_style))
        cmd_box_text = (
            "<b>¿Por qué el agente te entrega un comando de terminal al final?</b><br/>"
            "Para acciones globales del sistema que requieren conexión externa (subir a <b>GitHub Pages</b>, "
            "activar un servidor Wi-Fi local en el puerto 8888 para ver resultados en el iPad, o refrescar cachés).<br/>"
            "<b>El Estándar Oficial:</b> El comando siempre viene en un único bloque con <code>echo</code> de inicio y fin. "
            "Tú solo tienes que abrir la aplicación <b>Terminal</b> de tu Mac, pegar el bloque entero con <b>Cmd + V</b> y pulsar <b>Enter</b>. "
            "Verás en pantalla exactamente qué tarea se inicia y cuándo concluye de forma exitosa."
        )
        story.append(make_callout(cmd_box_text, '#F8FAFC', '#94A3B8', 5))

        doc.build(story)
        print(f"   ✅ PDF oficial generado exitosamente: {PDF_PATH}", flush=True)
        return True
    except ImportError:
        print("   ⚠️ ReportLab no está disponible en este entorno sandbox. Se compilará en terminal externa.", flush=True)
        return False
    except Exception as e:
        print(f"   ❌ Error al generar PDF con ReportLab: {e}", flush=True)
        import traceback
        traceback.print_exc()
        return False

def main():
    print("🚀 Compilando Guía Didáctica Oficial del Alumno (Monográfico 7)...")
    compilar_docx_nativo()
    ok = compilar_pdf_reportlab()
    if not ok:
        compilar_pdf_word()
    print("🎉 ¡Proceso finalizado!")

def compilar_pdf_word():
    """Genera PDF mediante Microsoft Word nativo en macOS como alternativa."""
    print("3. Compilando PDF mediante Microsoft Word nativo...", flush=True)
    osa = f'''
    set docxPath to POSIX file "{DOCX_PATH}" as text
    set pdfPath to POSIX file "{PDF_PATH}" as text
    tell application "Microsoft Word"
        set origDoc to open file name docxPath
        save as origDoc file name pdfPath file format format PDF
        close origDoc saving no
    end tell
    '''
    res = subprocess.run(["osascript", "-e", osa], capture_output=True, text=True)
    if res.returncode == 0 and os.path.isfile(PDF_PATH):
        print(f"   ✅ PDF generado con éxito vía Microsoft Word: {PDF_PATH}", flush=True)
        return True
    else:
        print(f"   ⚠️ Word export notice: {res.stderr.strip()}", flush=True)
        return False

if __name__ == '__main__':
    main()
