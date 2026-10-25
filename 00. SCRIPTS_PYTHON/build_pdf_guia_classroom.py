#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_guia_classroom.py
Compila la Guía Oficial de Publicación en GitHub y Google Classroom a PDF:
0.GUIA_PUBLICACION_GITHUB_CLASSROOM.pdf
Versión simplificada y limpia: sin cursos archivados ni código extenso.
"""

import os
import sys

TARGET_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-ROBOTICA-IA-COMUN/5.GUIAS_Y_METODOLOGIA"
PDF_PATH = os.path.join(TARGET_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.pdf")

def generate_pdf():
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    )
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    PAGE_WIDTH = A4[0] - 72 # 523.27 pt ancho util

    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=15, leading=19,
        textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'DocSub', parent=styles['Normal'],
        fontName='Helvetica-Oblique', fontSize=9.5, leading=13,
        textColor=colors.HexColor('#475569'), alignment=1, spaceAfter=12
    )
    h2_style = ParagraphStyle(
        'H2Style', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=11, leading=14,
        textColor=colors.HexColor('#0284C7'), spaceBefore=10, spaceAfter=4
    )
    body_style = ParagraphStyle(
        'BodyDark', parent=styles['Normal'],
        fontName='Helvetica', fontSize=9, leading=13,
        textColor=colors.HexColor('#1E293B'), spaceAfter=4
    )
    body_bold = ParagraphStyle(
        'BodyBold', parent=body_style,
        fontName='Helvetica-Bold'
    )
    callout_style = ParagraphStyle(
        'Callout', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.8, leading=12.5,
        textColor=colors.HexColor('#0F172A')
    )

    story = []

    # Encabezado
    story.append(Paragraph("GUIA DE PUBLICACION EN GITHUB Y GOOGLE CLASSROOM", title_style))
    story.append(Paragraph("Workflow Oficial de Trabajo en Equipo &bull; Profesor (Tu) &amp; Asistente IA (Antigravity)", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284C7'), spaceAfter=10))

    # Introduccion
    intro_text = (
        "<b>INTRODUCCION AL SISTEMA:</b><br/>"
        "Este flujo de trabajo esta disenado para un equipo de dos: <b>Tu (el Profesor)</b> y <b>Yo (Antigravity, tu asistente IA)</b>. "
        "Permite que todo el contenido viaje desde tu Mac hasta Google Classroom de forma ordenada, sin desfases de cache y sin tocar codigo."
    )
    intro_table = Table([[Paragraph(intro_text, callout_style)]], colWidths=[PAGE_WIDTH])
    intro_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#38BDF8')),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(intro_table)
    story.append(Spacer(1, 8))

    # FASE 1
    story.append(Paragraph("FASE 1: PREPARACION LOCAL EN EL MAC [TAREA DEL PROFESOR]", h2_style))
    story.append(Paragraph("1. Escribe tu teoria, genera tus PDFs, graba los videos y organiza todo en la carpeta correspondiente de tu Mac.", body_style))
    story.append(Paragraph("2. Nombra los archivos correctamente (ej: <code>T0.DEBATE.pdf</code>, <code>T2.VIDEO.mp4</code>, etc.).", body_style))
    story.append(Spacer(1, 5))

    # FASE 2
    story.append(Paragraph("FASE 2: SINCRONIZACION AL SERVIDOR (GITHUB) [TAREA DE LA IA]", h2_style))
    story.append(Paragraph("Tu me dices: <i>«Ya he metido todos los archivos nuevos en la carpeta del Mac, subelos a GitHub»</i>.", body_style))
    story.append(Paragraph("Yo (la IA) me encargo de anadir los archivos, hacer el commit y enviarlos a la nube (<code>git push origin main</code>) para alojarlos en GitHub Pages sin gastar espacio en tu Google Drive.", body_style))
    story.append(Spacer(1, 5))

    # FASE 3
    story.append(Paragraph("FASE 3: CREACION DEL PANEL UNIFICADO DE ENLACES [TAREA DE LA IA]", h2_style))
    story.append(Paragraph("Tu me dices: <i>«Genera el CSV unificado con los enlaces actualizados»</i>.", body_style))
    story.append(Paragraph("Yo (la IA) me encargo de generar el archivo maestro <b><code>PANELES_CSV/CURSO_IA_UNIFICADO.csv</code></b> con los mapas interactivos de sesiones y monograficos.", body_style))
    story.append(Spacer(1, 5))

    # FASE 4 - TABLA DESTACADA DE IDs
    story.append(Paragraph("FASE 4: PREPARACION DE GOOGLE CLASSROOM [TAREA DEL PROFESOR]", h2_style))
    story.append(Paragraph("Entra en <code>classroom.google.com</code> con tu cuenta de profesor. Trabajamos con las <b>Clases Maestras Unificadas Anuales</b>:", body_style))

    id_data = [
        [Paragraph("<b>CLASE MAESTRA UNIFICADA</b>", body_bold), Paragraph("<b>IDENTIFICADOR REAL (ID CLASSROOM)</b>", body_bold), Paragraph("<b>ESTADO</b>", body_bold)],
        [Paragraph("<b>CURSO DE IA (Curso Completo Anual)</b>", body_style), Paragraph("<font size=11 color='#B91C1C'><b>890436514251</b></font>", body_style), Paragraph("<font color='#059669'><b>ACTIVO (VIGENTE)</b></font>", body_style)],
        [Paragraph("<b>CURSO DE ROBOTICA (Curso Completo Anual)</b>", body_style), Paragraph("<font size=11 color='#0284C7'><b>890435922022</b></font>", body_style), Paragraph("<font color='#059669'><b>ACTIVO (VIGENTE)</b></font>", body_style)],
    ]
    id_table = Table(id_data, colWidths=[203, 180, 140])
    id_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E2E8F0')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#FEF2F2')),
        ('BACKGROUND', (0,2), (-1,2), colors.HexColor('#F0FDF4')),
        ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#94A3B8')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(id_table)
    story.append(Spacer(1, 8))

    # FASE 5
    story.append(Paragraph("FASE 5: INGESTA DE DATOS (GOOGLE SHEETS) [TAREA DEL PROFESOR]", h2_style))
    story.append(Paragraph("1. Abre tu navegador en <b>Modo Incognito / Ventana Privada</b> (evita conflictos entre cuentas de Google).", body_style))
    story.append(Paragraph("2. Entra a Google Drive y abre tu hoja permanente: <b><code>0.PANEL_CLASSROOM</code></b>.", body_style))
    story.append(Paragraph("3. Ve a <b>Archivo &gt; Importar &gt; Subir</b> y arrastra: <b><code>PANELES_CSV/CURSO_IA_UNIFICADO.csv</code></b>.", body_style))
    story.append(Paragraph("4. Selecciona <b>«Reemplazar hoja de calculo actual»</b> y pulsa <b>Importar</b>.", body_style))
    story.append(Paragraph("5. En la <b>Columna A (<code>ID_CURSO</code>)</b>, introduce el identificador de la clase:", body_style))
    story.append(Paragraph("   &bull; Para el curso de IA: <b><font size=10 color='#B91C1C'>890436514251</font></b> (arrastra hacia abajo para rellenar todas las filas).", body_style))
    story.append(Spacer(1, 5))

    # FASE 6
    story.append(Paragraph("FASE 6: PUBLICACION AUTOMATICA [TAREA DEL PROFESOR]", h2_style))
    story.append(Paragraph("1. En la hoja Google Sheets, ve a <b>Extensiones &gt; Apps Script</b>.", body_style))
    story.append(Paragraph("2. Selecciona la funcion <b><code>publicarTodoConTemas</code></b> y pulsa <b>Ejecutar</b>.", body_style))
    story.append(Paragraph("3. El script creara automaticamente los Temas (<code>MONOGRAFICOS</code> y <code>SESION 1</code> a <code>SESION 60</code>) y cargara los materiales en modo <b>BORRADOR (DRAFT)</b> para que los publiques a tu ritmo.", body_style))
    story.append(Spacer(1, 8))

    # ANEXO
    story.append(Paragraph("ANEXO: EL BOTON DEL PANICO (RESET COMPLETO DE CLASE)", h2_style))
    story.append(Paragraph("Si necesitas limpiar por completo la clase de Classroom para empezar de cero:", body_style))
    story.append(Paragraph("1. Escribe el ID del curso en la celda <b>A2</b> de la hoja (ej: <code>890436514251</code>).", body_style))
    story.append(Paragraph("2. En Apps Script, ejecuta la funcion <b><code>borrarAbsolutamenteTodo</code></b>.", body_style))
    story.append(Paragraph("3. Toda la clase (temas, materiales y borradores) quedara reseteada por completo en pocos segundos.", body_style))

    doc.build(story)
    print(f"✅ PDF generado exitosamente en: {PDF_PATH}")

if __name__ == '__main__':
    try:
        generate_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
