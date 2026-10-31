#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_005.py
Ficha Didáctica Oficial de 1 Página (Letter):
Simulador Científico 3D Oficial: Estación Espacial Internacional (ISS) (NASA Eyes) [COD-005]
Estructura científica estricta: Explicación, Controles 360°, Acreditación Oficial (NASA/JPL)
y 3 Preguntas de Reflexión para dialogar con Gemini en el aula.
"""

import os
import sys
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/05_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-005_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
ALT_PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-005_Simulador_ISS_NASA_Eyes.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/05_COD-005_Simulador_ISS_3D.pdf"

def build_cod_005_taller_3d_pdf(output_path=PDF_PATH):
    dest_path = output_path
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    except Exception:
        dest_path = LOCAL_BACKUP
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    doc = SimpleDocTemplate(
        dest_path,
        pagesize=letter,
        rightMargin=36, leftMargin=36, topMargin=22, bottomMargin=20
    )
    styles = getSampleStyleSheet()

    c_primary = colors.HexColor('#0284C7')
    c_blue = colors.HexColor('#0369A1')
    c_dark = colors.HexColor('#0F172A')
    c_slate = colors.HexColor('#334155')

    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.0, leading=9.5,
        textColor=c_blue, alignment=1, spaceAfter=1
    )
    style_subhead = ParagraphStyle(
        'SubheadStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.5, leading=11.5,
        textColor=c_dark, alignment=1, spaceAfter=3
    )
    style_title = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=11.5, leading=14.0,
        textColor=c_dark, spaceAfter=3
    )
    style_sec_h = ParagraphStyle(
        'SecHStyle', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=8.8, leading=11.0,
        textColor=c_primary, spaceBefore=2, spaceAfter=2
    )
    style_body = ParagraphStyle(
        'BodyStyle', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=8.1, leading=10.6,
        textColor=c_slate, spaceAfter=2
    )
    style_box_text = ParagraphStyle(
        'BoxTextStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.7, leading=10.1,
        textColor=c_dark
    )

    story = []

    # Cabecera Oficial
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA Y SIMULADORES 3D INTERACTIVOS • EXPLORACIÓN ESPACIAL [COD]", style_subhead))
    story.append(HRFlowable(width="100%", thickness=1.2, color=c_primary, spaceAfter=4))

    # Título de la Ficha
    story.append(Paragraph("<b>[COD-005] Simulador 3D Oficial: Estación Espacial Internacional (ISS) en Tiempo Real</b>", style_title))

    # Sección 1: Explicación Didáctica
    story.append(Paragraph("🛰️ <b>El Mayor Laboratorio Científico Fuera de la Tierra:</b>", style_sec_h))
    story.append(Paragraph(
        "La <b>Estación Espacial Internacional (ISS)</b> es la mayor estructura construida por la humanidad en el espacio: mide 109 metros de largo (el tamaño de un campo de fútbol) y orbita la Tierra a 400 kilómetros de altitud a una velocidad de <b>27.600 km/h</b>. "
        "A través de este simulador oficial de NASA Eyes, el alumno puede inspeccionar en 360° los 8 colosales paneles solares de silicio que generan 120 kilovatios de electricidad, la viga maestra de celosía integrada y los módulos presurizados donde los astronautas viven en microgravedad permanente, realizando experimentos biomédicos y de ciencia de materiales.",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Sección 2: Controles 360°
    story.append(Paragraph("🎮 <b>Controles del Visor 3D & Guía de Interacción en el Aula:</b>", style_sec_h))
    ctrl_data = [
        [Paragraph("<b>🖱️ Inspección Exterior 360°:</b> Haz clic izquierdo y arrastra para rotar la estación y observar los módulos Columbus (Europa), Kibo (Japón), Destiny (EE.UU.) y Zvezda (Rusia).", style_box_text)],
        [Paragraph("<b>🔍 Zoom de Detalle Tecnológico:</b> Usa la rueda del ratón para aproximarte a las escotillas de acoplamiento de las cápsulas Crew Dragon o a la Cúpula de observación.", style_box_text)],
        [Paragraph("<b>🌍 Salto a la Tierra en Órbita:</b> Pulsa el botón 'Tierra desde Órbita' en la botonera inferior para contemplar la curvatura del planeta exactamente como la ven los tripulantes.", style_box_text)],
        [Paragraph("<b>🔭 Telescopio Hubble:</b> Salta con un clic a inspeccionar el telescopio Hubble que orbita a 540 km de altitud en la misma región orbital.", style_box_text)],
    ]
    t_ctrl = Table(ctrl_data, colWidths=[letter[0] - 72])
    t_ctrl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#94A3B8')),
        ('TOPPADDING', (0,0), (-1,-1), 2.0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.0),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_ctrl)
    story.append(Spacer(1, 2))

    # Sección 3: Procedencia Oficial
    story.append(Paragraph("🏛️ <b>Procedencia Institucional y Calidad Científica de los Datos:</b>", style_sec_h))
    prov_text = (
        "• <b>Institución Acreditada:</b> Desarrollado por el <b>Jet Propulsion Laboratory (JPL) de la NASA</b> en colaboración con el Centro Espacial Johnson (JSC Houston).<br/>"
        "• <b>Modelo de Ingeniería 1:1:</b> La geometría de la ISS procede directamente de los archivos CAD de ingeniería de la NASA y la ESA. La posición y orientación de la estación se calculan mediante datos telemétricos y vectores de estado NORAD en tiempo real, reflejando su vuelo auténtico sobre la superficie terrestre."
    )
    t_prov = Table([[Paragraph(prov_text, style_box_text)]], colWidths=[letter[0] - 72])
    t_prov.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ECFDF5')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#10B981')),
        ('TOPPADDING', (0,0), (-1,-1), 3.0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.0),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_prov)
    story.append(Spacer(1, 2))

    # Sección 4: Preguntas para Gemini
    story.append(Paragraph("💬 <b>Guía de Exploración en el Aula & Preguntas para Dialogar con Gemini:</b>", style_sec_h))
    q_data = [
        [Paragraph("<b>Pregunta 1 • Vida en Microgravedad:</b> <i>«Gemini, observando la ISS en NASA Eyes a 400 km de altura, ¿por qué los astronautas flotan en su interior? ¿Es porque no hay gravedad o porque la estación está en una caída libre continua alrededor de la Tierra?»</i>", style_box_text)],
        [Paragraph("<b>Pregunta 2 • Amaneceres cada 90 Minutos:</b> <i>«Gemini, si la ISS viaja a 27.600 km/h y tarda solo 90 minutos en dar una vuelta completa a la Tierra, ¿cuántos amaneceres y puestas de sol ven los astronautas cada 24 horas y cómo logran dormir?»</i>", style_box_text)],
        [Paragraph("<b>Pregunta 3 • Radiación y Blindaje:</b> <i>«Gemini, al mirar los módulos presurizados de la estación, ¿cómo se protegen los tripulantes del impacto de micrometeoritos y de la intensa radiación cósmica fuera de la atmósfera?»</i>", style_box_text)],
    ]
    t_q = Table(q_data, colWidths=[letter[0] - 72])
    t_q.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EFF6FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#3B82F6')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_q)

    doc.build(story)

    # Duplicar con nombre alternativo y respaldo local
    try:
        shutil.copy2(dest_path, ALT_PDF_PATH)
        os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
        shutil.copy2(dest_path, LOCAL_BACKUP)
    except Exception:
        pass

    print(f"✅ PDF COD-005 generado con éxito en: {dest_path}")
    return dest_path

# Alias para compatibilidad con compiladores
def build_pure_python_cod_005(dest=PDF_PATH):
    return build_cod_005_taller_3d_pdf(dest)

if __name__ == '__main__':
    try:
        build_cod_005_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-005: {e}")
        sys.exit(1)
