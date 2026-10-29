#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_007.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-007_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 07)
- 07_COD-007_Taller_Simulador_Luna_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/07_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-007_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/07_COD-007_Taller_Simulador_Luna_3D.pdf"

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

    accent = colors.HexColor('#0284C7')

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
    # Encabezado Oficial
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & SIMULADORES CIENTÍFICOS 3D [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.5, color=accent, spaceAfter=5))

    story.append(Paragraph("<b>[COD-007] Guía Científica • El Atlas Lunar 3D: Topografía y Relieve LOLA (NASA)</b>", style_title))

    # Bloque 1: Explicación didáctica del Simulador
    story.append(Paragraph("🌕 <b>1. ¿Qué vemos en el Simulador 3D y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador astronómico interactivo reproduce el <b>globo tridimensional de la Luna con relieve topográfico real</b> basado "
        "en las mediciones de la misión <b>NASA LRO (Lunar Reconnaissance Orbiter)</b>. En pantalla se distingue con claridad la marcada "
        "asimetría geológica lunar: los oscuros <b>mares basálticos</b> (<i>maria</i>) originados por antiguos impactos rellenados de lava "
        "en la cara visible (<i>Mare Tranquillitatis</i>, <i>Mare Imbrium</i> y <i>Oceanus Procellarum</i>) frente a las escarpadas tierras "
        "altas anortosíticas plagadas de cráteres.<br/>"
        "El simulador cuenta con <b>iluminación solar interactiva y ciclo de fases lunares</b>: al rotar la posición del Sol se proyectan sombras "
        "rasantes alargadas que realzan la profundidad de cráteres icónicos como <b>Tycho</b> (con sus extensas bandas de eyección radial), "
        "<b>Copérnico</b> y <b>Kepler</b>. Puedes <b>rotar la Luna 360°</b> para examinar tanto la Cara Visible como la <b>Cara Oculta</b>, "
        "conmutar entre la textura fotométrica natural y el <b>mapa de relieve LOLA</b>, y localizar el sitio del alunizaje del <b>Apolo 11 (1969)</b>.",
        style_body
    ))

    # Bloque 2: Procedencia y Fuentes Científicas Oficiales
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Astronómico Oficial:</b> Los mapas globales de textura y elevación proceden del <b>Planetary Data System (PDS) de la NASA</b> "
        "y del centro <i>Goddard Space Flight Center</i> mediante los datos abiertos de la sonda <b>Lunar Reconnaissance Orbiter (LRO)</b>.<br/>"
        "• <b>Altimetría Láser LOLA (Lunar Orbiter Laser Altimeter):</b> El relieve topográfico no es artístico, sino el resultado directo de más de "
        "<b>4.000 millones de disparos láser</b> desde la órbita lunar hacia la superficie. La medición del tiempo de rebote calculó cotas con precisión "
        "vertical milimétrica, cartografiando desniveles de hasta 16 km entre la cuenca polar Aitken y las cordilleras lunares.<br/>"
        "• <b>Fotometría Satelital 4K:</b> Mosaico espectral de alta resolución ensamblado por la cámara orbital <i>LROC (LRO Camera)</i>, corregido "
        "fotométricamente para eliminar reflejos espurios y mostrar el albedo fidedigno del regolito lunar."
    )
    t_box = Table([[Paragraph(fuente_text, style_box_text)]], colWidths=[letter[0] - 72])
    t_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1.2, accent),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_box)
    story.append(Spacer(1, 4))

    # Bloque 3: Guía de Exploración & Retos de Conversación con Gemini
    story.append(Paragraph("💬 <b>3. Guía de Exploración en el Aula & Conversación con Gemini</b>", style_section_h))
    story.append(Paragraph(
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«🌕 Abrir Atlas Lunar 3D ↗»</i>) y utilízalo como observatorio interactivo mientras "
        "dialogas con Gemini (<i>gemini.google.com</i>). Puedes formularle estas preguntas para profundizar en clase:",
        style_body
    ))

    prompts_text = (
        "<b>1. La Cara Oculta:</b> <i>«Al rotar la Luna 360° en el simulador veo que la Cara Oculta apenas tiene mares oscuros y está saturada de cráteres. ¿Por qué ambas caras de la Luna son tan distintas geológicamente?»</i><br/>"
        "<b>2. Fases Lunares y Rotación Sincrónica:</b> <i>«En el simulador muevo la luz del Sol y aprecio cómo las sombras rasantes revelan el cráter Tycho. ¿Por qué desde la Tierra siempre vemos la misma cara de la Luna?»</i><br/>"
        "<b>3. Historia Espacial:</b> <i>«¿Por qué la misión Apolo 11 eligió precisamente el Mare Tranquillitatis para el primer alunizaje humano en julio de 1969?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Astronomía visual interactiva y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-007 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-007 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
