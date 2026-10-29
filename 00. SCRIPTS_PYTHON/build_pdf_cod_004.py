#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_004.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-004_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 04)
- 04_COD-004_Taller_Simulador_Ojo_Humano_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/04_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-004_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/04_COD-004_Taller_Simulador_Ojo_Humano_3D.pdf"

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

    accent = colors.HexColor('#0F766E') # Tono teal/esmeralda óptico

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

    story.append(Paragraph("<b>[COD-004] Guía Biomédica • El Globo Ocular Humano: Óptica, Cristalino y Retina 3D</b>", style_title))

    # Bloque 1: Explicación didáctica del Simulador
    story.append(Paragraph("👁️ <b>1. ¿Qué vemos en el Simulador 3D y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador biofísico interactivo modela el <b>sistema dióptrico y óptico del ojo humano</b> en tiempo real. "
        "En pantalla se representa el recorrido de los haces luminosos desde el exterior hasta su enfoque nítido sobre la fóvea en la retina, "
        "atravesando sucesivamente las cuatro estructuras refringentes fundamentales: la <b>córnea</b> (lente convergente fija más potente), el <b>humor acuoso</b> "
        "en la cámara anterior, el <b>cristalino</b> (lente elástica biconvexa responsable de la acomodación) y el <b>humor vítreo</b>.<br/>"
        "El simulador reproduce dinámicamente dos respuestas fisiológicas clave: el <b>reflejo fotomotor</b> de la pupila (contracción o <i>miosis</i> con luz intensa "
        "y dilatación o <i>midriasis</i> en penumbra) y la <b>acomodación visual</b> (aumento de la curvatura del cristalino para enfocar objetos cercanos frente al "
        "enfoque en el infinito). Puedes <b>rotar el globo ocular 360°</b>, seguir el movimiento del cursor, ajustar la iluminación ambiental y activar el "
        "<b>corte transversal sagital</b> para observar el nervio óptico y la mácula lútea.",
        style_body
    ))

    # Bloque 2: Procedencia y Fuentes Científicas Oficiales
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Oftalmológico Oficial:</b> Los parámetros anatómicos y ópticos proceden del <b>National Eye Institute (NEI)</b> dependiente de los NIH, "
        "así como de los estándares biométricos del <i>European Vision Institute</i>.<br/>"
        "• <b>Adquisición de Datos y Texturas Biomédicas:</b> Las mallas 3D y mapas de refracción se obtuvieron a partir de <b>tomografía de coherencia óptica (OCT) "
        "de polo anterior y posterior</b>, combinada con topografía corneal computerizada. Las texturas PBR 4K del iris humano reproducen con fidelidad microscópica "
        "el estroma anterior, las criptas de Fuchs y el esfínter pupilar.<br/>"
        "• <b>Modelado Óptico Basado en Física:</b> Las ecuaciones de refracción aplicadas siguen el <b>modelo de ojo esquemático de Gullstrand</b>, con índices de "
        "refracción reales (córnea n=1.376, cristalino n=1.406, vítreo n=1.336), garantizando una convergencia focal científicamente rigurosa."
    )
    t_box = Table([[Paragraph(fuente_text, style_box_text)]], colWidths=[letter[0] - 72])
    t_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#CCFBF1')),
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
        "Abre el simulador en tu pantalla (en el mapa pulsa <i>«👁️ Ver Simulador Ojo Humano 3D»</i>) y hazle estas preguntas a Gemini (<i>gemini.google.com</i>) "
        "para comprender cómo cuidamos nuestra vista con el paso de los años:",
        style_body
    ))

    prompts_text = (
        "<b>1. Acomodación y Presbicia:</b> <i>«Estoy mirando un modelo 3D del ojo humano. ¿Por qué con la edad el cristalino pierde flexibilidad y aparece la vista cansada o presbicia?»</i><br/>"
        "<b>2. Óptica y Refracción:</b> <i>«¿Cuál es la diferencia óptica entre la miopía y la hipermetropía en relación al punto exacto donde se enfocan los rayos en la retina?»</i><br/>"
        "<b>3. Protección Ocular:</b> <i>«¿Por qué el iris reacciona cerrando la pupila en milisegundos cuando salimos a una calle muy soleada?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Salud visual y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-004 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-004 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
