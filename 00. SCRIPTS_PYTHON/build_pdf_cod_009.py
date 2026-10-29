#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_009.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-009_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 09)
- 09_COD-009_Taller_Simulador_TRex_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/09_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-009_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/09_COD-009_Taller_Simulador_TRex_3D.pdf"

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
    # Encabezado Oficial
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & SIMULADORES CIENTÍFICOS 3D [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.5, color=accent, spaceAfter=5))

    story.append(Paragraph("<b>[COD-009] Guía Científica • El Tyrannosaurus Rex: Biomecánica Craneal y Escaneo Fósil 3D</b>", style_title))

    # Bloque 1: Explicación didáctica del Simulador
    story.append(Paragraph("🦖 <b>1. ¿Qué vemos en el Simulador 3D y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador paleontológico interactivo sitúa al alumno en una sala de museo virtual ante el <b>cráneo fosilizado real del "
        "Tyrannosaurus Rex ('Sue', espécimen PR2081)</b>, el depredador terrestre más imponente del Cretácico Superior. En pantalla se aprecian "
        "con fidelidad milimétrica las <b>fenestras temporales y anteorbitales</b>: grandes aberturas óseas que aligeraban el enorme peso "
        "de la cabeza (de casi 1,5 metros de longitud) y servían de anclaje a los poderosos músculos aductores de la mandíbula.<br/>"
        "El modelo expone la dentición hipertrofiada con <b>piezas dentales aserradas de hasta 30 cm con raíces profundas</b>, diseñadas para "
        "asestar una fuerza de mordida estimada en más de <b>57.000 Newtons</b> (capaz de fracturar huesos de ceratópsidos y hadrosaurios). "
        "Puedes <b>rotar el cráneo 360°</b> con el ratón sobre su peana de exposición, alternar entre focos de galería y luz neutra de laboratorio, "
        "y hacer zoom sobre las suturas craneales y el canal olfativo.",
        style_body
    ))

    # Bloque 2: Procedencia y Fuentes Científicas Oficiales
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Paleontológico Oficial:</b> La malla tridimensional procede del escaneo fotogramétrico y volumétrico del <b>Field Museum "
        "of Natural History de Chicago</b> y de los archivos de digitalización del <b>American Museum of Natural History (AMNH)</b> de Nueva York.<br/>"
        "• <b>Técnica de Digitalización de Fósiles:</b> Fotogrametría de alta resolución calibrada con luz polarizada cruzada combinada con "
        "<b>tomografía axial computarizada industrial (Industrial CT Scan)</b>. Esta técnica permite registrar microfisuras de fosilización, texturas "
        "de mineralización del hueso y desgaste dental microscópico sin tocar la pieza original.<br/>"
        "• <b>Fidelidad Biomecánica:</b> Las dimensiones reproducen las proporciones anatómicas exactas del espécimen catalogado FMNH PR 2081, "
        "descubierto en la formación Hell Creek (Dakota del Sur), el esqueleto de T-Rex más completo y mejor preservado de la historia."
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

    # Bloque 3: Guía de Exploración & Retos de Conversación con Gemini
    story.append(Paragraph("💬 <b>3. Guía de Exploración en el Aula & Conversación con Gemini</b>", style_section_h))
    story.append(Paragraph(
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«🦖 Abrir T-Rex 3D de Museo ↗»</i>) y utilízalo como museo interactivo mientras "
        "conversas con Gemini (<i>gemini.google.com</i>). Puedes plantearle estas preguntas para investigar en clase:",
        style_body
    ))

    prompts_text = (
        "<b>1. Ventanas Óseas y Ligereza:</b> <i>«Al rotar el cráneo del T-Rex 360° en el simulador veo enormes huecos laterales (fenestras). ¿Por qué la evolución dejó esas ventanas vacías en el cráneo en vez de hacerlo de hueso macizo?»</i><br/>"
        "<b>2. La Fuerza de Mordida:</b> <i>«En la ficha se indica que el T-Rex mordía con más de 50.000 Newtons de fuerza. ¿Cómo evitaba que la mandíbula se rompiera al golpear y triturar los huesos de sus presas?»</i><br/>"
        "<b>3. Fósiles y Tecnología:</b> <i>«¿Cómo consiguen los paleontólogos escanear el interior de huesos fosilizados de hace 66 millones de años con escáneres CT sin dañar la piedra?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Paleontología visual interactiva y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-009 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-009 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
