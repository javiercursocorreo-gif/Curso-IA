#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_015.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-015_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 15)
- 15_COD-015_Taller_Simulador_Partenon_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/15_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-015_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/15_COD-015_Taller_Simulador_Partenon_3D.pdf"

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

    story.append(Paragraph("<b>[COD-015] Guía Científica • El Partenón de Atenas & Proporción Áurea</b>", style_title))

    # Bloque 1
    story.append(Paragraph("🏛️ <b>1. ¿Qué vemos en el Simulador y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador arqueológico interactivo reproduce el <b>templo dórico del Partenón en la Acrópolis de Atenas</b> (447-432 a.C.) "
        "en fotografía hiperrealista de alta resolución. En pantalla se analiza la aplicación matemática del <b>número áureo (Φ = 1,618)</b> en la fachada octástila "
        "(8 × 17 columnas de mármol pentélico puro), así como las <b>correcciones ópticas</b> magistrales de Ictino y Calícrates.<br/>"
        "El templo carece por completo de líneas rectas: el suelo (estilóbato) está abombado 6 cm en el centro para no parecer hundido; las columnas poseen "
        "un ensanchamiento central de 2 cm (<b>éntasis</b>) a un tercio de su altura; y las columnas de las esquinas son 2,5 cm más gruesas y se inclinan "
        "hacia el interior para contrarrestar la intensa luz del cielo ateniense. Puedes activar la <b>rejilla de la espiral áurea</b> y explorar cada elemento.",
        style_body
    ))

    # Bloque 2
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Arqueológico Oficial:</b> Cartografía fotogramétrica y escaneo láser LiDAR de la <b>Acrópolis de Atenas</b> procedente del archivo "
        "<b>CyArk Heritage Archive</b> y del <b>Ministerio de Cultura y Deportes de Grecia</b>.<br/>"
        "• <b>Geometría y Óptica Clásica:</b> Parámetros métricos basados en los estudios canónicos de Manolis Korres (Jefe de Restauración del Partenón) "
        "y las especificaciones de arquitectura griega clásica del <i>Tratado de Arquitectura de Vitruvio</i>.<br/>"
        "• <b>Proporción Divina:</b> La relación matemática entre el ancho de la fachada y la altura total hasta el vértice del tímpano obedece a la proporción "
        "áurea euclidiana exacta (1 : 1,618033)."
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
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«🏛️ Abrir Partenón ↗»</i>) y utilízalo como observatorio arqueológico mientras "
        "conversas con Gemini (<i>gemini.google.com</i>). Puedes hacerle estas preguntas para investigar en clase:",
        style_body
    ))

    prompts_text = (
        "<b>1. El Secreto del Éntasis:</b> <i>«Al activar los marcadores en el simulador veo el ensanchamiento en las columnas dóricas. ¿Por qué nuestros ojos verían una columna perfectamente cilíndrica como si estuviese estrecha y a punto de quebrarse por el centro?»</i><br/>"
        "<b>2. La Curvatura del Suelo:</b> <i>«¿Cómo consiguieron los canteros griegos tallar miles de bloques de mármol con curvas milimétricas sin tener ordenadores ni láser?»</i><br/>"
        "<b>3. El Número Áureo en la Naturaleza:</b> <i>«¿Qué relación existe entre la proporción áurea que usaron en el Partenón y la forma en que crecen los girasoles o las conchas de nautilus?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Arqueología clásica interactiva y agilidad mental con Inteligencia Artificial.", style_footer))

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
