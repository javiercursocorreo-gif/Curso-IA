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

    accent = colors.HexColor('#B45309')

    style_header = ParagraphStyle('HeaderStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.2, leading=10.0, textColor=accent, alignment=1, spaceAfter=2)
    style_block = ParagraphStyle('BlockStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.5, leading=12.0, textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=4)
    style_title = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=12.0, leading=14.5, textColor=colors.HexColor('#0F172A'), spaceAfter=4)
    style_section_h = ParagraphStyle('SectionHStyle', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=9.2, leading=12.0, textColor=accent, spaceBefore=4, spaceAfter=3)
    style_body = ParagraphStyle('BodyStyle', parent=styles['BodyText'], fontName='Helvetica', fontSize=8.0, leading=11.2, textColor=colors.HexColor('#1E293B'), spaceAfter=3)
    style_box_text = ParagraphStyle('BoxText', parent=styles['Normal'], fontName='Helvetica', fontSize=7.8, leading=10.8, textColor=colors.HexColor('#0F172A'))

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & SIMULADORES CIENTÍFICOS 3D [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.5, color=accent, spaceAfter=5))

    story.append(Paragraph("<b>[COD-015] Guía Científica • El Telescopio Espacial James Webb (JWST) en el Punto L2</b>", style_title))

    # Bloque 1
    story.append(Paragraph("🔭 <b>1. ¿Qué vemos en el Simulador y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador reproduce la anatomía y funcionamiento del <b>Telescopio Espacial James Webb (JWST)</b> de la NASA, la ESA y la CSA, "
        "el observatorio astronómico más avanzado de la historia humana, situado a <b>1,5 millones de kilómetros</b> de la Tierra en el punto gravitatorio de Lagrange L2.<br/>"
        "En pantalla se explora el colosal <b>espejo primario de 6,5 metros</b> formado por 18 hexágonos de berilio recubiertos con <b>oro puro de 100 nm</b> "
        "(diseñado para reflejar la luz infrarroja térmica), el <b>parasol térmico de 5 capas de Kapton</b> del tamaño de una pista de tenis y el módulo de cámaras científicas.<br/>"
        "El simulador permite alternar entre la visión humana en <b>Luz Visible</b> y la <b>Revelación Infrarroja (NIRCam / MIRI)</b> en nebulosas como los <i>Pilares de la Creación</i>, "
        "demostrando cómo el polvo estelar opaco se vuelve transparente revelando miles de estrellas recién nacidas.",
        style_body
    ))

    # Bloque 2
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas del Telescopio</b>", style_section_h))
    fuente_text = (
        "• <b>Misión y Operaciones Oficiales:</b> Datos de telemetría y especificaciones de vuelo del <b>Space Telescope Science Institute (STScI)</b>, "
        "el centro <b>NASA Goddard Space Flight Center</b> y la <b>Agencia Espacial Europea (ESA)</b>.<br/>"
        "• <b>Instrumentación Criogénica:</b> Espectros infrarrojos de la cámara <b>NIRCam</b> (0,6 a 5 micras) y el detector <b>MIRI</b> de infrarrojo medio, "
        "refrigerado a <b>7 Kelvin (-266 °C)</b> para captar el calor primordial del universo temprano.<br/>"
        "• <b>Acreditación Científica:</b> Lanzado el 25 de diciembre de 2021 a bordo del cohete Ariane 5 de Arianespace desde la Guayana Francesa."
    )
    t_box = Table([[Paragraph(fuente_text, style_box_text)]], colWidths=[letter[0] - 72])
    t_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FEF3C7')),
        ('BOX', (0,0), (-1,-1), 1, accent),
        ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_box)
    story.append(Spacer(1, 4))

    # Bloque 3
    story.append(Paragraph("💬 <b>3. Guía de Exploración en el Aula & Conversación con Gemini</b>", style_section_h))
    story.append(Paragraph(
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«🔭 Abrir Telescopio James Webb 3D ↗»</i>) y dialoga con Gemini (<i>gemini.google.com</i>) con estas preguntas:",
        style_body
    ))

    prompts_text = (
        "<b>1. El Misterio del Oro:</b> <i>«En el simulador observo que los 18 espejos hexagonales del James Webb brillan en color dorado. ¿Por qué los científicos eligieron oro puro en vez de aluminio o plata para reflejar la luz del espacio profundo?»</i><br/>"
        "<b>2. Viaje en el Tiempo:</b> <i>«¿Por qué los astrónomos afirman que mirar a través de los detectores infrarrojos del James Webb es literalmente viajar 13.500 millones de años atrás en el tiempo, hasta los primeros instantes del Big Bang?»</i><br/>"
        "<b>3. El Escudo de Dos Caras:</b> <i>«El simulador indica que en el lado del parasol que da al Sol hace +85 °C y en el lado de los espejos hace -233 °C. ¿Cómo logran 5 láminas de plástico tan finas como un cabello aislar una diferencia de más de 300 grados?»</i>"
    )
    p_box = Table([[Paragraph(prompts_text, style_box_text)]], colWidths=[letter[0] - 72])
    p_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#64748B')),
        ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(p_box)
    story.append(Spacer(1, 4))

    story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor('#CBD5E1'), spaceAfter=3))
    style_footer = ParagraphStyle('FooterStyle', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=7.0, leading=8.5, textColor=colors.HexColor('#64748B'), alignment=1)
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Astronomía espacial interactiva y agilidad mental con Inteligencia Artificial.", style_footer))
    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-015 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-015 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
