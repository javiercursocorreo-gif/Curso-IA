#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_015.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-015_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 15)
- 15_COD-015_Taller_Simulador_James_Webb_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/15_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-015_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/15_COD-015_Taller_Simulador_James_Webb_3D.pdf"

def build_pdf(dest_path):
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    doc = SimpleDocTemplate(
        dest_path,
        pagesize=letter,
        rightMargin=36, leftMargin=36, topMargin=24, bottomMargin=20
    )
    styles = getSampleStyleSheet()

    accent = colors.HexColor('#D97706')

    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.2, leading=10.0,
        textColor=accent, alignment=1, spaceAfter=2
    )
    style_block = ParagraphStyle(
        'BlockStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.5, leading=12.0,
        textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=4
    )
    style_title = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=12.0, leading=14.5,
        textColor=colors.HexColor('#0F172A'), spaceAfter=4
    )
    style_section_h = ParagraphStyle(
        'SectionHStyle', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=9.2, leading=12.0,
        textColor=accent, spaceBefore=4, spaceAfter=3
    )
    style_body = ParagraphStyle(
        'BodyStyle', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=8.0, leading=11.2,
        textColor=colors.HexColor('#1E293B'), spaceAfter=3
    )
    style_box_text = ParagraphStyle(
        'BoxText', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.8, leading=10.8,
        textColor=colors.HexColor('#0F172A')
    )

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & SIMULADORES CIENTÍFICOS 3D [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.5, color=accent, spaceAfter=5))

    story.append(Paragraph("<b>[COD-015] Guía Científica • Telescopio Espacial James Webb (JWST)</b>", style_title))

    # Bloque 1
    story.append(Paragraph("🔭 <b>1. ¿Qué vemos en el Simulador y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador astronómico interactivo reproduce el <b>Telescopio Espacial James Webb (JWST)</b> "
        "en fotografía científica hiperrealista de alta resolución capturada durante su inspección óptica en la sala limpia de la NASA. "
        "En pantalla se analiza el <b>espejo primario de 6,5 metros</b> compuesto por 18 segmentos hexagonales de berilio ultraligero revestidos de oro puro (100 nm), "
        "diseñado para captar la débil radiación infrarroja de las primeras estrellas nacidas tras el Big Bang.<br/>"
        "El simulador permite alternar entre la visión óptica en color natural, el modo de <b>infrarrojo térmico MIRI (falso color)</b> "
        "y el análisis de <b>segmentación hexagonal</b>, explorando los actuadores nanométricos de calibración, el trípode del espejo secundario "
        "y el <b>escudo térmico parasol de 5 capas de Kapton</b> que mantiene los instrumentos a temperaturas criogénicas de -233 °C.",
        style_body
    ))

    # Bloque 2
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Datos</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Espacial Oficial:</b> Astrofotografía científica de alta resolución de la sala limpia (Cleanroom) del "
        "<b>NASA Goddard Space Flight Center (GSFC)</b>, la <b>Agencia Espacial Europea (ESA)</b> y <b>Northrop Grumman Aerospace</b>.<br/>"
        "• <b>Ingeniería Óptica y Espectrometría:</b> Especificaciones de la NASA sobre la reflectancia del oro en longitudes de onda de 0,6 a 28,3 micrómetros "
        "y calibración de frente de onda por interferometría láser.<br/>"
        "• <b>Órbita y Criogenia:</b> Parámetros orbitales en el segundo punto de Lagrange (L2) a 1,5 millones de km de la Tierra, con refrigeración pasiva "
        "a 40 Kelvin y refrigeración activa por ciclo cerrado de helio a 6,7 Kelvin en el detector MIRI."
    )
    t_box = Table([[Paragraph(fuente_text, style_box_text)]], colWidths=[letter[0] - 72])
    t_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFBEB')),
        ('BOX', (0,0), (-1,-1), 1.2, accent),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_box)
    story.append(Spacer(1, 4))

    # Bloque 3
    story.append(Paragraph("💬 <b>3. Guía de Exploración en el Aula & Conversación con Gemini</b>", style_section_h))
    story.append(Paragraph(
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«🔭 Abrir James Webb ↗»</i>) y utilízalo como estación astronómica mientras "
        "conversas con Gemini (<i>gemini.google.com</i>). Puedes hacerle estas preguntas para investigar en clase:",
        style_body
    ))

    prompts_text = (
        "<b>1. El Oro en el Espacio:</b> <i>«En el simulador veo que el espejo del James Webb es de color dorado brillante. ¿Por qué la NASA cubrió los 18 espejos con oro puro en lugar de plata o aluminio, y cuánta cantidad de oro se necesitó en total?»</i><br/>"
        "<b>2. El Frío Extremo en L2:</b> <i>«¿Por qué el telescopio necesita estar a casi -233 °C en el punto de Lagrange L2 para poder 'ver' las galaxias más lejanas en infrarrojo sin deslumbrarse?»</i><br/>"
        "<b>3. El Parasol del Tamaño de una Pista de Tenis:</b> <i>«¿Cómo consiguieron que 5 finas láminas de plástico Kapton bloqueen el calor del Sol haciendo que un lado esté a +85 °C y el otro a -233 °C?»</i>"
    )
    p_box = Table([[Paragraph(prompts_text, style_box_text)]], colWidths=[letter[0] - 72])
    p_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(p_box)

    doc.build(story)
    print(f"✅ PDF Científico [COD-015] James Webb generado: {dest_path}")

def build_cod_015_taller_3d_pdf():
    build_pdf(PDF_PATH)
    os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
    shutil.copy2(PDF_PATH, LOCAL_BACKUP)
    print(f"📁 Copia de respaldo guardada en: {LOCAL_BACKUP}")

if __name__ == '__main__':
    build_cod_015_taller_3d_pdf()
