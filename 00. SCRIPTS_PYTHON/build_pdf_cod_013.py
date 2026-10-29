#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_013.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-013_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 13)
- 13_COD-013_Taller_Simulador_ADN_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/13_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-013_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/13_COD-013_Taller_Simulador_ADN_3D.pdf"

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

    accent = colors.HexColor('#059669')

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

    story.append(Paragraph("<b>[COD-013] Guía Científica • La Doble Hélice de ADN 3D: Genética Molecular y Estructura PDB</b>", style_title))

    # Bloque 1: Explicación didáctica del Simulador
    story.append(Paragraph("🧬 <b>1. ¿Qué vemos en el Simulador 3D y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador de biología molecular interactivo reproduce la estructura espacial en <b>doble hélice dextrógira del ácido desoxirribonucleico "
        "(ADN forma B)</b>, la molécula portadora de las instrucciones genéticas de la vida. En pantalla se distinguen los dos componentes "
        "estructurales esenciales: los <b>esqueletos exteriores fosfato-azúcar (desoxirribosa)</b> dispuestos de forma antiparalela (5' a 3' y 3' a 5') "
        "y los peldaños interiores constituidos por <b>pares de bases nitrogenadas complementarias</b>.<br/>"
        "La complementariedad química sigue la regla estricta de apareamiento mediante <b>puentes de hidrógeno</b>: la <b>Adenina (A)</b> se empareja "
        "con la <b>Timina (T)</b> a través de dos puentes de hidrógeno, y la <b>Guanina (G)</b> se enlaza con la <b>Citosina (C)</b> mediante tres enlaces "
        "más resistentes. Puedes <b>rotar la molécula 360°</b> con el ratón, examinar el <b>surco mayor y surco menor</b> donde se acoplan las proteínas "
        "reguladoras, y regular la velocidad de torsión helicoidal.",
        style_body
    ))

    # Bloque 2: Procedencia y Fuentes Científicas Oficiales
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Bioinformático Oficial:</b> Las coordenadas atómicas tridimensionales proceden del <b>Protein Data Bank (RCSB PDB, entrada "
        "canónica 1BNA)</b> y del <i>National Center for Biotechnology Information (NCBI)</i> de la Biblioteca Nacional de Medicina (NIH).<br/>"
        "• <b>Técnica de Resolución Estructural:</b> Geometría atómica determinada mediante <b>difracción de rayos X en monocristal a resolución de 1,9 Å "
        "(angstroms)</b>, continuadora directa del descubrimiento de Rosalind Franklin, James Watson y Francis Crick.<br/>"
        "• <b>Física Molecular y Escala Atómica:</b> Las esferas y enlaces PBR respetan los radios de Van der Waals de cada átomo (carbono, nitrógeno, "
        "oxígeno, fósforo e hidrógeno) y las distancias de enlace covalente calculadas mediante mecánica cuántica molecular."
    )
    t_box = Table([[Paragraph(fuente_text, style_box_text)]], colWidths=[letter[0] - 72])
    t_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ECFDF5')),
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
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«🧬 Abrir Simulador ADN 3D ↗»</i>) y utilízalo como laboratorio molecular mientras "
        "conversas con Gemini (<i>gemini.google.com</i>). Puedes plantearle estas preguntas para investigar en clase:",
        style_body
    ))

    prompts_text = (
        "<b>1. Complementariedad Estricta:</b> <i>«En el simulador veo que las bases siempre van emparejadas (A con T y G con C). ¿Por qué nunca se unen A con G o T con C y qué ocurriría en nuestro organismo si fallase este emparejamiento?»</i><br/>"
        "<b>2. Envejecimiento y Telómeros:</b> <i>«¿Qué ocurre en los extremos de nuestras hebras de ADN (los telómeros) con el paso de los años y cómo influye esto en la salud celular y longevidad en personas mayores de 60 años?»</i><br/>"
        "<b>3. Epigenética y Hábitos:</b> <i>«¿Es verdad que el ejercicio diario, el descanso reparador y una mente activa pueden modificar cómo se expresan nuestros genes a través de la epigenética sin alterar la secuencia de ADN?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Genética visual interactiva y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-013 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-013 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
