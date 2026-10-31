#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_019.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-019_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 19)
- 19_COD-019_Taller_Simulador_Saturno_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/19_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-019_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/19_COD-019_Taller_Simulador_Saturno_3D.pdf"

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

    story.append(Paragraph("<b>[COD-019] Guía Científica • Saturno, Hexágono Polar & Anillos PBR</b>", style_title))

    # Bloque 1
    story.append(Paragraph("🪐 <b>1. ¿Qué vemos en el Simulador y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este visor astronómico interactivo de alta resolución reproduce el planeta <b>Saturno y su majestuoso sistema de anillos</b> "
        "con datos e imágenes directas de la sonda espacial <b>Cassini-Huygens (NASA / ESA)</b>. En pantalla se observa el globo gaseoso "
        "achatado polarmente con su inclinación axial real de <b>26.73°</b>, las bandas atmosféricas de nubes de amoníaco, el enigmático "
        "<b>hexágono polar norte</b> (un vórtice atmosférico de 30.000 km de diámetro) y los anillos concéntricos principales (C, B y A), "
        "separados por la imponente <b>División de Cassini</b> (una brecha gravitatoria de 4.800 km de ancho modelada por la luna Mimas).<br/>"
        "El simulador permite interactuar con zoom macro, rotación, contraste espectral y filtros ópticos (luz natural, infrarrojo térmico "
        "y falso color ultravioleta), revelando que los anillos, a pesar de medir casi 300.000 km de ancho, tienen solo entre 10 y 30 metros de espesor.",
        style_body
    ))

    # Bloque 2
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de la Astrofísica</b>", style_section_h))
    fuente_text = (
        "• <b>Misión Espacial Oficial:</b> Mosaicos fotográficos y datos espectrométricos de la sonda <b>NASA / JPL / Space Science Institute Cassini-Huygens</b> "
        "(cámaras ISS Narrow Angle y espectrómetro VIMS) durante su órbita alrededor de Saturno (2004-2017).<br/>"
        "• <b>Física de Anillos y Resonancia Gravitatoria:</b> Parámetros radiales calibrados a partir de las curvas de densidad de ondas espirales "
        "y ocultaciones estelares registradas por la NASA.<br/>"
        "• <b>Composición Física:</b> Partículas de hielo de agua con pureza superior al 99%, con albedos ópticos idénticos a los del sistema saturniano real."
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
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«🪐 Abrir Saturno ↗»</i>) y utilízalo como telescopio espacial mientras "
        "conversas con Gemini (<i>gemini.google.com</i>). Puedes hacerle estas preguntas para investigar en clase:",
        style_body
    ))

    prompts_text = (
        "<b>1. El Misterio del Hexágono Polar:</b> <i>«Al enfocar el polo norte de Saturno en el simulador veo un hexágono geométrico perfecto. ¿Cómo puede formarse una figura geométrica de seis lados en las tormentas de un planeta gaseoso?»</i><br/>"
        "<b>2. El Espesor de los Anillos:</b> <i>«¿Es verdad que si Saturno fuera del tamaño de una pelota de baloncesto, sus anillos serían mil veces más finos que una hoja de papel de fumar?»</i><br/>"
        "<b>3. La Brecha de Cassini:</b> <i>«En el simulador se ve una franja negra entre los anillos A y B. ¿Por qué la luna Mimas barre gravitatoriamente esa zona dejando un hueco vacío de 4.800 kilómetros?»</i>"
    )
    p_box = Table([[Paragraph(prompts_text, style_box_text)]], colWidths=[letter[0] - 72])
    p_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#64748B')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(p_box)
    story.append(Spacer(1, 4))

    story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor('#CBD5E1'), spaceAfter=3))
    style_footer = ParagraphStyle(
        'FooterStyle', parent=styles['Normal'],
        fontName='Helvetica-Oblique', fontSize=7.0, leading=8.5,
        textColor=colors.HexColor('#64748B'), alignment=1
    )
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Astrofísica observacional y exploración planetaria con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-019 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-019 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
