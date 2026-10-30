#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_pdf_cod_015.py - Ficha Científica Oficial de 1 Página"""
import os, shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/15_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-015_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/15_COD-015_Taller_Simulador_Partenon_3D.pdf"

def build_pdf(dest_path):
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    doc = SimpleDocTemplate(dest_path, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=24, bottomMargin=20)
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
    story.append(Paragraph("<b>[COD-015] Guía Científica • El Partenón de Atenas 3D: Arqueometría y Proporción Áurea</b>", style_title))

    story.append(Paragraph("🏛️ <b>1. ¿Qué vemos en el Simulador 3D y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador de arqueología virtual reproduce la reconstrucción arquitectónica del <b>Partenón de la Acrópolis de Atenas</b> "
        "(siglo V a.C., obra cumbre de Ictino, Calícrates y Fidias). En pantalla se contempla la fachada octástila de estilo dórico y la "
        "aplicación de las <b>correcciones ópticas clásicas</b> ideadas para evitar distorsiones visuales: el <b>éntasis</b> "
        "(ligero abombamiento de las columnas de mármol pentélico), la <b>inclinación hacia adentro de las columnas perimetrales</b> "
        "(cuyos ejes convergerían a 2.400 m de altura) y la <b>curvatura convexa del estilóbato</b> (el suelo del templo, elevado en el centro).<br/>"
        "El simulador permite superponer en tiempo real la <b>rejilla de la Proporción Áurea (Phi = 1,618)</b> sobre la fachada, "
        "<b>rotar el templo 360°</b> con el ratón y observar la estructura constructiva sin mortero ni cemento.",
        style_body
    ))

    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Arqueológico Oficial:</b> La planimetría tridimensional procede del archivo de conservación <b>CyArk (Scan 5006 - "
        "Parthenon Acropolis)</b> y de los estudios del <b>Comité para la Conservación de los Monumentos de la Acrópolis (YSMA)</b> de Grecia.<br/>"
        "• <b>Técnica de Escaneo Láser LiDAR:</b> Nube de puntos de alta densidad capturada con <b>escáner láser terrestre milimétrico</b> y "
        "fotogrametría aérea ortorrectificada, registrando las deformaciones sísmicas y la explosión del polvorín de 1687.<br/>"
        "• <b>Arqueometría y Materiales:</b> Las texturas PBR reproducen la pátina cálida del mármol pentélico con inclusiones férricas, que adquiere con los siglos "
        "su característico tono miel dorado al oxidarse con la intemperie."
    )
    t_box = Table([[Paragraph(fuente_text, style_box_text)]], colWidths=[letter[0] - 72])
    t_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFBEB')),
        ('BOX', (0,0), (-1,-1), 1.2, accent),
        ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_box)
    story.append(Spacer(1, 4))

    story.append(Paragraph("💬 <b>3. Guía de Exploración en el Aula & Conversación con Gemini</b>", style_section_h))
    story.append(Paragraph("Abre el simulador en tu navegador (en el mapa pulsa <i>«🏛️ Abrir Partenón Dorado 3D ↗»</i>) y dialoga con Gemini (<i>gemini.google.com</i>):", style_body))
    prompts_text = (
        "<b>1. Las Ilusiones Ópticas:</b> <i>«En el simulador veo que las columnas del Partenón no son rectas sino abombadas e inclinadas. ¿Por qué los arquitectos griegos hicieron esto a propósito para engañar a nuestros ojos?»</i><br/>"
        "<b>2. La Proporción Áurea (Phi):</b> <i>«Al activar la rejilla geométrica en el templo veo la proporción 1,618. ¿Por qué esta relación matemática genera una sensación universal de belleza y equilibrio visual en el cerebro humano?»</i><br/>"
        "<b>3. El Mármol Pentélico:</b> <i>«¿Por qué el mármol de las canteras del monte Pentélico tiene ese tono dorado y cómo consiguieron tallar los tambores de las columnas sin mortero ni cemento?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Arqueología virtual interactiva y agilidad mental con Inteligencia Artificial.", style_footer))
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
