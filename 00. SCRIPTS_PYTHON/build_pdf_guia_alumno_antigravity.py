#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_guia_alumno_antigravity.py
Genera la Guía Didáctica Oficial del Alumno (adaptada 100% a portátiles Windows):
GUIA_ALUMNO_ANTIGRAVITY_Y_CONTROL_FICHEROS.pdf y .docx
dentro de:
CURSO-IA/CLASES/7. MAPA_GESTION_PROYECTO_CON_IA/

Contenido Pedagógico:
- Checklist de instalación en Windows con hipervínculo directo a https://antigravity.google/
- El secreto de la Carpeta Raíz Única en Documentos (MI_TALLER_IA) para evitar ventanas de aprobación ("Submits").
- Directivas de gobernanza (AGENTS.md y GEMINI.md): no las crea el alumno a mano, se las pide a la IA en su primer mensaje.
- Qué es la Terminal en Windows (PowerShell / cmd / terminal integrada) y por qué la IA da comandos preparados.
- Casuística práctica con archivos que los alumnos sí pueden abrir y ver en Windows (.docx de Word y .html para Chrome/Edge):
  1. Creación masiva: 3 carpetas temáticas con documentos Word (.docx).
  2. Modificación quirúrgica de recetas en Word (.docx) sin borrar nada.
  3. Borrado selectivo seguro dentro de la carpeta raíz.
  4. Mover y renombrar archivos entre carpetas.
  5. Creación de simuladores web (.html) que se abren con doble clic en Chrome/Edge.
- Comando final de terminal con títulos visibles mediante echo.
"""

import os
import sys
import subprocess

TARGET_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/7. MAPA_GESTION_PROYECTO_CON_IA"
HTML_PATH = os.path.join(TARGET_DIR, "GUIA_ALUMNO_ANTIGRAVITY_Y_CONTROL_FICHEROS.html")
DOCX_PATH = os.path.join(TARGET_DIR, "GUIA_ALUMNO_ANTIGRAVITY_Y_CONTROL_FICHEROS.docx")
PDF_PATH = os.path.join(TARGET_DIR, "GUIA_ALUMNO_ANTIGRAVITY_Y_CONTROL_FICHEROS.pdf")

def compilar_docx_nativo():
    """Genera versión Word DOCX usando el motor oficial textutil."""
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
    """Genera el PDF oficial de alta resolución con ReportLab adaptado a Windows."""
    print("2. Compilando PDF oficial con ReportLab (Enfoque Windows)...", flush=True)
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
            topMargin=30,
            bottomMargin=30
        )

        styles = getSampleStyleSheet()

        c_navy = colors.HexColor('#0F172A')
        c_blue = colors.HexColor('#0284C7')
        c_slate = colors.HexColor('#475569')
        c_dark = colors.HexColor('#1E293B')
        c_card_bg = colors.HexColor('#F8FAFC')
        c_box_border = colors.HexColor('#CBD5E1')

        title_style = ParagraphStyle(
            'DocTitle', parent=styles['Heading1'],
            fontName='Helvetica-Bold', fontSize=14.5, leading=18,
            textColor=c_navy, alignment=1, spaceAfter=2
        )
        sub_style = ParagraphStyle(
            'DocSub', parent=styles['Normal'],
            fontName='Helvetica-Oblique', fontSize=8.5, leading=12,
            textColor=c_slate, alignment=1, spaceAfter=6
        )
        h1_style = ParagraphStyle(
            'SecH1', parent=styles['Heading2'],
            fontName='Helvetica-Bold', fontSize=10.5, leading=13.5,
            textColor=c_blue, spaceBefore=7, spaceAfter=2
        )
        h2_style = ParagraphStyle(
            'SecH2', parent=styles['Heading3'],
            fontName='Helvetica-Bold', fontSize=9, leading=12,
            textColor=c_navy, spaceBefore=4, spaceAfter=2
        )
        body_style = ParagraphStyle(
            'Body', parent=styles['Normal'],
            fontName='Helvetica', fontSize=8, leading=11,
            textColor=c_dark, spaceAfter=2
        )
        body_bold = ParagraphStyle(
            'BodyBold', parent=body_style,
            fontName='Helvetica-Bold'
        )
        prompt_style = ParagraphStyle(
            'PromptStyle', parent=styles['Normal'],
            fontName='Helvetica-Oblique', fontSize=8, leading=11,
            textColor=colors.HexColor('#0369A1')
        )
        badge_style = ParagraphStyle(
            'BadgeStyle', parent=styles['Normal'],
            fontName='Helvetica-Bold', fontSize=7, leading=9,
            textColor=colors.white, alignment=1
        )

        def make_callout(text, bg_hex='#F0F9FF', border_hex='#38BDF8', pad=5):
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

        # ENCABEZADO
        story.append(Paragraph("GUÍA DIDÁCTICA Y CHECKLIST: TU PRIMER DÍA CON ANTIGRAVITY EN WINDOWS", title_style))
        story.append(Paragraph("Puesta en Marcha 'Cero-Submits', Terminal en Windows y Creación de Documentos Word (.docx) & Web (.html) &bull; Clase 7", sub_style))
        story.append(HRFlowable(width="100%", thickness=1.5, color=c_blue, spaceAfter=5))

        # HERO CALLOUT
        intro_html = (
            "<b>🎯 ¿QUÉ CAMBIA HOY EN TU FORMA DE USAR LA IA?</b> "
            "Hasta hoy utilizabas <i>chatbots</i> en el navegador donde la IA solo te daba texto en una ventanita que debías copiar a mano. "
            "En esta clase damos el salto al <b>Agente Autónomo (Google Antigravity)</b> en tu portátil con <b>Windows</b>: "
            "una IA capaz de crear carpetas, redactar documentos de Word (<code>.docx</code>) que abres con doble clic, "
            "programar páginas web (<code>.html</code>) para ver en Chrome o Edge y corregir errores mientras tú solo le hablas en español."
        )
        story.append(make_callout(intro_html, '#F0FDF4', '#34D399', 5))
        story.append(Spacer(1, 4))

        # BLOQUE 1: CHECKLIST DE INSTALACIÓN WINDOWS
        story.append(Paragraph("BLOQUE 1: CHECKLIST DE PUESTA EN MARCHA EN WINDOWS & PROTOCOLO 'CERO SUBMITS'", h1_style))

        chk_data = [
            [
                Paragraph("<b>PASO (WINDOWS)</b>", body_bold),
                Paragraph("<b>ACCIÓN PASO A PASO DEL ALUMNO</b>", body_bold),
                Paragraph("<b>POR QUÉ ES VITAL (EL SECRETO TÉCNICO)</b>", body_bold)
            ],
            [
                Paragraph("<b>1. Descarga e Instalación</b>", body_style),
                Paragraph(
                    "Entra en la web oficial: <a href='https://antigravity.google/' color='#0284C7'><b><u>https://antigravity.google/</u></b></a>.<br/>"
                    "Descarga el archivo <code>Antigravity-Setup.exe</code> en tu carpeta de <i>Descargas</i>, haz doble clic y sigue el instalador (<i>Siguiente &gt; Instalar &gt; Finalizar</i>).",
                    body_style
                ),
                Paragraph("Instala el agente en tu Windows creando acceso directo en el Escritorio y Menú Inicio.", body_style)
            ],
            [
                Paragraph("<b>2. Carpeta Raíz Única<br/>(En Documentos)</b>", body_style),
                Paragraph(
                    "Abre el <i>Explorador de Archivos</i> de Windows (carpeta amarilla), entra en <b>Documentos</b> y crea la carpeta <code>MI_TALLER_IA</code>.<br/>"
                    "En Antigravity, pulsa <b>File &gt; Open Folder</b> (o <i>Archivo &gt; Abrir Carpeta</i>) y selecciona <code>MI_TALLER_IA</code>.",
                    body_style
                ),
                Paragraph(
                    "<b>¡REGLA DE ORO ANTI-SUBMITS!</b> Si abres archivos sueltos del Escritorio o Descargas, Windows bloqueará a la IA pidiendo confirmación constante. "
                    "Al usar <b>una sola carpeta raíz</b>, todo lo que ocurra dentro queda <b>100% preautorizado</b> y la IA trabaja de corrido sin detenerse.",
                    body_style
                )
            ],
            [
                Paragraph("<b>3. Reglas Maestras<br/>(AGENTS.md / GEMINI.md)</b>", body_style),
                Paragraph(
                    "<b>Tú NO las creas a mano.</b> En tu primer mensaje en el chat le dices a la IA:<br/>"
                    "<i>«Antigravity, crea en mi carpeta raíz los archivos AGENTS.md y GEMINI.md con mis reglas: responde en español claro para personas mayores, trabaja en silencio sin pedir confirmaciones intermedias y mantén estos archivos actualizados.»</i>",
                    body_style
                ),
                Paragraph("Antigravity crea los archivos de gobernanza en segundos y los actualiza según vayas pidiéndole nuevos proyectos.", body_style)
            ],
            [
                Paragraph("<b>4. ¿Qué es la Terminal y Cómo se Abre?</b>", body_style),
                Paragraph(
                    "Es la ventanita de comandos directa de Windows. Para abrirla:<br/>"
                    "• <b>Forma recomendada:</b> En Antigravity, ve al menú superior <b>Terminal &gt; New Terminal</b> (o pulsa <code>Ctrl + Shift + `</code>). Se abre abajo en tu carpeta.<br/>"
                    "• (Alternativa): Pulsa tecla Windows, escribe <code>cmd</code> o <code>PowerShell</code> y pulsa Enter.",
                    body_style
                ),
                Paragraph("Sirve para arrancar servidores web locales o sincronizar proyectos con un solo comando sin tocar configuraciones difíciles.", body_style)
            ],
        ]
        chk_table = Table(chk_data, colWidths=[105, 218, 200])
        chk_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E2E8F0')),
            ('GRID', (0,0), (-1,-1), 0.5, c_box_border),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
            ('BACKGROUND', (0,2), (-1,2), colors.HexColor('#FEF3C7')), # highlight golden rule
        ]))
        story.append(chk_table)
        story.append(Spacer(1, 4))

        # BLOQUE 2: CASUÍSTICA CON ARCHIVOS FAMILIARES (WORD DOCX Y WEB HTML)
        story.append(Paragraph("BLOQUE 2: CASUÍSTICA CON ARCHIVOS QUE PUEDES ABRIR EN WINDOWS (WORD Y NAVEGADOR)", h1_style))
        story.append(Paragraph("En lugar de formatos técnicos que Windows no reconoce, le pedimos a Antigravity documentos de <b>Word (.docx)</b> y páginas web (<b>.html</b>) con doble clic:", body_style))
        story.append(Spacer(1, 2))

        casos = [
            (
                "CASO 1: Creación Masiva (3 Carpetas Temáticas + Documentos de Word .docx)",
                "«Antigravity, dentro de mi espacio de trabajo crea tres carpetas: 1. PLANES_DE_VIAJE, 2. RECETAS_SALUDABLES y 3. ASTRONOMIA_NASA. Dentro de cada una, crea un documento de Word (.docx) con un título elegante, una breve introducción y una lista con tres ideas para empezar.»",
                "Crea las 3 carpetas y dentro los archivos (ej: <code>1. PLANES_DE_VIAJE/itinerario.docx</code>). Vas al Explorador de Windows, haces <b>doble clic y se abre en Microsoft Word</b> formateado y listo.",
                "#059669", "DOCUMENTOS WORD"
            ),
            (
                "CASO 2: Modificación y Ampliación de un Documento de Word sin Borrar",
                "«Antigravity, abre el documento RECETAS_SALUDABLES/menu_semanal.docx y añade al final una receta tradicional de Gazpacho Andaluz con ingredientes para 4 personas y pasos de preparación.»",
                "El agente lee el documento, localiza el final e inserta la receta. <b>La clave:</b> no sobreescribe ni destruye lo que ya tenías; añade la información respetando todo el contenido previo.",
                "#0284C7", "EDICIÓN QUIRÚRGICA"
            ),
            (
                "CASO 3: Borrado Selectivo y Seguro de un Archivo Innecesario",
                "«Antigravity, dentro de la carpeta PLANES_DE_VIAJE, elimina el archivo borrador_antiguo.docx que ya no me sirve.»",
                "Elimina únicamente ese archivo. Gracias a la restricción de la carpeta raíz, la IA no puede tocar tus fotos personales, tus descargas ni el sistema de Windows. Tu equipo está 100% protegido.",
                "#DC2626", "SEGURIDAD TOTAL"
            ),
            (
                "CASO 4: Mover y Renombrar Archivos entre Carpetas Diferentes",
                "«Antigravity, traslada el archivo misiones_espaciales.docx de ASTRONOMIA_NASA a una nueva subcarpeta llamada ASTRONOMIA_NASA/SONDAS_HISTORICAS y renómbralo como 01_apolo_y_voyager.docx.»",
                "Crea la subcarpeta de destino en Windows, copia el archivo con su nuevo nombre y elimina el archivo anterior para no dejar duplicados confusos.",
                "#D97706", "REORGANIZACIÓN"
            ),
            (
                "CASO 5: Creación de Simuladores y Páginas Web (.html) con Doble Clic",
                "«Antigravity, dentro de ASTRONOMIA_NASA crea un visor interactivo visor_solar.html conectado a NASA Eyes, con botones para cambiar de planeta y tarjetas informativas con datos científicos.»",
                "Escribe el código web completo. Cuando termine, vas al Explorador de Windows y haces <b>doble clic: se abrirá en Google Chrome o Microsoft Edge</b> funcionando como una app profesional.",
                "#0EA5E9", "APP WEB INTERACTIVA"
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
                ('TOPPADDING', (0,0), (-1,-1), 2.5),
                ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
                ('LEFTPADDING', (0,0), (-1,-1), 5),
                ('RIGHTPADDING', (0,0), (-1,-1), 5),
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ]))
            story.append(KeepTogether([c_table, Spacer(1, 2.5)]))

        story.append(Spacer(1, 2))

        # BLOQUE 3: COMANDO DE TERMINAL EN WINDOWS
        story.append(Paragraph("BLOQUE 3: ¿POR QUÉ LA IA TE DA UN COMANDO DE TERMINAL AL FINAL?", h1_style))
        cmd_box_text = (
            "<b>¿Por qué la IA te entrega un comando de terminal al terminar?</b><br/>"
            "Para tareas del sistema como poner en marcha un <b>servidor web local</b> (para ver tus simuladores en el navegador o en la tablet) "
            "o publicar proyectos en GitHub. Para no marearte con 10 clics técnicos por los menús de Windows, "
            "la IA te redacta una sola orden que hace todo al pulsar Enter.<br/>"
            "<b>Cómo usarlo en 3 segundos:</b> En Antigravity, ve a <b>Terminal &gt; New Terminal</b> (o pulsa <code>Ctrl + Shift + `</code>), "
            "pega el comando con <b>Ctrl + V</b> y pulsa <b>Enter</b>. Verás en letras claras cuándo se inicia y cuándo concluye de forma exitosa."
        )
        story.append(make_callout(cmd_box_text, '#F8FAFC', '#94A3B8', 4.5))

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

def compilar_pdf_word():
    """Genera PDF mediante Microsoft Word nativo como alternativa."""
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

def main():
    print("🚀 Compilando Guía Didáctica Oficial del Alumno (Clase 7 - Enfoque Windows)...")
    compilar_docx_nativo()
    ok = compilar_pdf_reportlab()
    if not ok:
        compilar_pdf_word()
    print("🎉 ¡Proceso finalizado!")

if __name__ == '__main__':
    main()
