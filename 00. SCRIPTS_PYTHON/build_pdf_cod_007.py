#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_007.py
Ficha Didáctica Oficial de 1 Página (Letter):
Simulador Científico 3D Oficial: El Sol y la Sonda Parker (NASA Eyes) [COD-007]
Estructura científica estricta: Explicación, Controles 360°, Acreditación Oficial (NASA/JHUAPL/JPL)
y 3 Preguntas de Reflexión para dialogar con Gemini en el aula.
"""

import os
import sys
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/07_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-007_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
ALT_PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-007_Simulador_Sol_Parker_NASA_Eyes.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/07_COD-007_Simulador_Sol_Parker_3D.pdf"

def build_cod_007_taller_3d_pdf(output_path=PDF_PATH):
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
    c_amber = colors.HexColor('#D97706')
    c_dark = colors.HexColor('#0F172A')
    c_slate = colors.HexColor('#334155')

    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.0, leading=9.5,
        textColor=c_amber, alignment=1, spaceAfter=1
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
    story.append(Paragraph("BLOQUE IV: CIENCIA Y SIMULADORES 3D INTERACTIVOS • FÍSICA SOLAR [COD]", style_subhead))
    story.append(HRFlowable(width="100%", thickness=1.2, color=c_amber, spaceAfter=4))

    # Título de la Ficha
    story.append(Paragraph("<b>[COD-007] Simulador 3D Oficial: El Sol y la Sonda Parker (NASA Eyes)</b>", style_title))

    # Sección 1: Explicación Didáctica
    story.append(Paragraph("☀️ <b>Física de la Corona Solar y el Vuelo Récord de Parker:</b>", style_sec_h))
    story.append(Paragraph(
        "Este simulador interactivo permite observar el <b>Sol en tiempo real</b> y la audaz trayectoria de la sonda espacial <b>Parker Solar Probe</b> de la NASA, la primera nave diseñada para 'tocar el Sol' sumergiéndose directamente en su ardiente atmósfera exterior (la corona). "
        "El alumno experimenta visualmente cómo la sonda utiliza asistencias gravitatorias de Venus para frenar y precipitarse a más de <b>690.000 km/h</b> (el objeto más veloz jamás fabricado), soportando temperaturas de 1.400 °C tras su escudo térmico de compuesto de carbono mientras mide el origen del viento solar y las eyecciones de masa coronal.",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Sección 2: Controles 360°
    story.append(Paragraph("🎮 <b>Controles del Visor 3D & Guía de Interacción en el Aula:</b>", style_sec_h))
    ctrl_data = [
        [Paragraph("<b>🖱️ Órbita Alrededor del Astro Rey:</b> Arrastra con el ratón para rotar el Sol 360° y contemplar la corona plasmática y las líneas de campo magnético dinámico.", style_box_text)],
        [Paragraph("<b>🔍 Acercamiento al Escudo de Parker:</b> Usa la rueda del ratón para aproximarte a la nave y ver la orientación de su escudo térmico siempre encarado al Sol.", style_box_text)],
        [Paragraph("<b>🛰️ Observatorio SOHO:</b> Pulsa 'Observatorio SOHO' en la barra inferior para saltar al telescopio que vigila las tormentas solares desde el punto de Lagrange L1.", style_box_text)],
        [Paragraph("<b>🪐 Salto a Mercurio:</b> Descubre Mercurio, el planeta más cercano al Sol, y compara su distancia con la atrevida órbita cercana de la sonda Parker.", style_box_text)],
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
        "• <b>Institución Acreditada:</b> Desarrollado por la <b>NASA Heliophysics Division</b>, el <b>Jet Propulsion Laboratory (JPL)</b> y el Laboratorio de Física Aplicada de Johns Hopkins (JHUAPL).<br/>"
        "• <b>Física Solar Basada en Datos Reales:</b> La órbita elíptica extrema de Parker y la corona solar 3D se calculan a partir de la telemetría viva de vuelo y las observaciones espectrográficas de los observatorios espaciales SDO (Solar Dynamics Observatory) y SOHO."
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
        [Paragraph("<b>Pregunta 1 • El Misterio de la Corona:</b> <i>«Gemini, la superficie del Sol está a unos 5.500 °C, pero su corona exterior alcanza millones de grados. ¿Por qué la atmósfera solar está mucho más caliente que la propia superficie?»</i>", style_box_text)],
        [Paragraph("<b>Pregunta 2 • El Escudo Térmico de Parker:</b> <i>«Gemini, ¿de qué material está hecho el escudo frontal de la sonda Parker para resistir 1.400 °C mientras sus instrumentos científicos permanecen a solo 30 °C a su sombra?»</i>", style_box_text)],
        [Paragraph("<b>Pregunta 3 • Tormentas Solares y la Tierra:</b> <i>«Gemini, al mirar el viento solar en el simulador, ¿cómo afectan las erupciones solares a los satélites GPS, a la red eléctrica y a la formación de auroras boreales en la Tierra?»</i>", style_box_text)],
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

    print(f"✅ PDF COD-007 generado con éxito en: {dest_path}")
    return dest_path

if __name__ == '__main__':
    try:
        build_cod_007_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-007: {e}")
        sys.exit(1)
