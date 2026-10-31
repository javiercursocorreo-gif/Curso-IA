#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_006.py
Ficha Didáctica Oficial de 1 Página (Letter):
Simulador Científico 3D Oficial: La Luna y el Programa Artemisa (NASA Eyes) [COD-006]
Estructura científica estricta: Explicación, Controles 360°, Acreditación Oficial (NASA/LRO/JPL)
y 3 Preguntas de Reflexión para dialogar con Gemini en el aula.
"""

import os
import sys
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/06_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "6. COD-006_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
ALT_PDF_PATH_4 = os.path.join(OUTPUT_DIR, "4. COD-006_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
ALT_PDF_PATH_NAME = os.path.join(OUTPUT_DIR, "4. COD-006_Simulador_Luna_Artemisa_NASA_Eyes.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/06_COD-006_Simulador_Luna_Artemisa_3D.pdf"

def build_cod_006_taller_3d_pdf(output_path=PDF_PATH):
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
    c_orange = colors.HexColor('#EA580C')
    c_dark = colors.HexColor('#0F172A')
    c_slate = colors.HexColor('#334155')

    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.0, leading=9.5,
        textColor=c_orange, alignment=1, spaceAfter=1
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
    story.append(Paragraph("BLOQUE IV: CIENCIA Y SIMULADORES 3D INTERACTIVOS • EXPLORACIÓN LUNAR [COD]", style_subhead))
    story.append(HRFlowable(width="100%", thickness=1.2, color=c_orange, spaceAfter=4))

    # Título de la Ficha
    story.append(Paragraph("<b>[COD-006] Simulador 3D Oficial: La Luna y el Programa Artemisa (NASA Eyes)</b>", style_title))

    # Sección 1: Explicación Didáctica
    story.append(Paragraph("🌕 <b>Topografía Lunar y el Retorno Humano con Artemisa:</b>", style_sec_h))
    story.append(Paragraph(
        "Este simulador sumerge al alumno en la <b>geología y relieve 3D hiperrealista de la Luna</b> a partir de los mapas altimétricos láser del orbitador LRO (Lunar Reconnaissance Orbiter). "
        "Permite explorar los oscuros mares de lava basáltica solidificada, las tierras altas cribadas por impactos de meteoritos y los valles del polo sur lunar (como el cráter Shackleton), donde el sol incide en rasante y el fondo permanece en tinieblas eternas a -240 °C, albergando millones de toneladas de hielo de agua vitales para abastecer la futura base lunar permanente del <b>Programa Artemisa</b> y la nave tripulada <b>Orión</b>.",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Sección 2: Controles 360°
    story.append(Paragraph("🎮 <b>Controles del Visor 3D & Guía de Interacción en el Aula:</b>", style_sec_h))
    ctrl_data = [
        [Paragraph("<b>🖱️ Exploración de la Cara Oculta:</b> Haz clic izquierdo y rota la Luna para descubrir la cara que jamás vemos desde la Tierra, mucho más accidentada y repleta de cráteres.", style_box_text)],
        [Paragraph("<b>🔍 Acercamiento a los Cráteres:</b> Usa la rueda del ratón para descender hacia los cráteres Tycho y Copérnico, apreciando sus impresionantes rayos de eyección blanca.", style_box_text)],
        [Paragraph("<b>🚀 La Nave Artemisa Orión:</b> Pulsa 'Nave Artemisa Orión' en la botonera inferior para volar en paralelo con la cápsula espacial de última generación de la NASA.", style_box_text)],
        [Paragraph("<b>🛰️ Orbitador Lunar LRO:</b> Inspecciona el satélite LRO que lleva más de una década cartografiando cada metro de la corteza lunar con láser.", style_box_text)],
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
        "• <b>Institución Acreditada:</b> Desarrollado por el <b>Jet Propulsion Laboratory (JPL)</b> y el <b>Goddard Space Flight Center (GSFC) de la NASA</b>.<br/>"
        "• <b>Altimetría Láser Real LOLA:</b> El relieve 3D utiliza la cuadrícula topográfica oficial del instrumento LOLA (Lunar Orbiter Laser Altimeter), con millones de puntos de elevación reales. Las trayectorias de la nave Orión y del orbitador LRO se sincronizan con las coordenadas de telemetría de vuelo del Centro Espacial Johnson."
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
        [Paragraph("<b>Pregunta 1 • El Hielo de Agua Lunar:</b> <i>«Gemini, observando el polo sur de la Luna en NASA Eyes, ¿cómo es posible que haya hielo de agua en los cráteres oscuros si la Luna no tiene atmósfera y el sol la calienta a más de 120 °C?»</i>", style_box_text)],
        [Paragraph("<b>Pregunta 2 • Apolo vs. Artemisa:</b> <i>«Gemini, ¿qué diferencias tecnológicas fundamentales existen entre las misiones Apolo de 1969 y el actual programa Artemisa de la NASA para volver a la Luna con astronautas?»</i>", style_box_text)],
        [Paragraph("<b>Pregunta 3 • La Cara Oculta:</b> <i>«Gemini, al rotar la Luna veo que la cara oculta casi no tiene mares oscuros como la cara visible. ¿Por qué las dos caras de la Luna son tan diferentes geológicamente?»</i>", style_box_text)],
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

    # Duplicar con nombres alternativos y respaldo local
    try:
        shutil.copy2(dest_path, ALT_PDF_PATH_4)
        shutil.copy2(dest_path, ALT_PDF_PATH_NAME)
        os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
        shutil.copy2(dest_path, LOCAL_BACKUP)
    except Exception:
        pass

    print(f"✅ PDF COD-006 generado con éxito en: {dest_path}")
    return dest_path

# Alias para compatibilidad con compiladores
def build_pure_python_cod_006(dest=PDF_PATH):
    return build_cod_006_taller_3d_pdf(dest)

if __name__ == '__main__':
    try:
        build_cod_006_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-006: {e}")
        sys.exit(1)
