#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_010.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-010_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 10)
- 10_COD-010_Taller_Simulador_Molar_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/10_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-010_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/10_COD-010_Taller_Simulador_Molar_3D.pdf"

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

    story.append(Paragraph("<b>[COD-010] Guía Científica • El Molar Humano 3D: Microtomografía, Esmalte y Pulpa</b>", style_title))

    # Bloque 1: Explicación didáctica del Simulador
    story.append(Paragraph("🦷 <b>1. ¿Qué vemos en el Simulador 3D y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador biomédico interactivo reproduce un <b>primer molar inferior humano en corte sagital y transversal</b>, "
        "permitiendo analizar la compleja arquitectura biológica de las piezas dentales en tiempo real. En pantalla se distinguen las cuatro "
        "capas fundamentales del diente: el <b>esmalte dental</b> (la sustancia más dura y mineralizada del cuerpo humano, 96% hidroxiapatita), "
        "la <b>dentina</b> intermedia (atravesada por millones de microtúbulos sensitivos), la <b>cámara pulpar</b> (que aloja los vasos sanguíneos "
        "nutricios y las terminaciones nerviosas) y los <b>conductos radiculares</b> que descienden hacia las raíces.<br/>"
        "El simulador incorpora <b>modo de sección gradual y rayos X</b> para observar la transición tisular interna. Puedes <b>rotar el molar 360°</b> "
        "con el ratón, separar la mitad coronal para examinar el interior radicular, resaltar los haces vasculonerviosos en color rojo/azul y "
        "comprender la causa del dolor o hipersensibilidad ante estímulos térmicos o mecánicos.",
        style_body
    ))

    # Bloque 2: Procedencia y Fuentes Científicas Oficiales
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Odontológico Oficial:</b> La reconstrucción procede de los atlas biomédicos abiertos del <b>National Institute of Dental "
        "and Craniofacial Research (NIDCR / NIH)</b> de los Estados Unidos y del departamento de morfología dental de la <b>Universidad de Berna</b>.<br/>"
        "• <b>Técnica de Microtomografía (Micro-CT Dental):</b> El volumen 3D no es un modelo sintético poligonal, sino el resultado de un escaneo "
        "mediante <b>microtomografía axial computarizada con resolución de 15 micrómetros</b>. Esta tecnología clínica penetra las capas minerales "
        "para capturar los conductos radiculares accesorios y la morfología del ápice dental real.<br/>"
        "• <b>Fidelidad Tisular PBR:</b> Los materiales replican el índice de refracción del esmalte traslúcido, la opacidad marfil de la dentina y "
        "la vascularización de la pulpa dental según parámetros de microscopía confocal y óptica biomédica."
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
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«🦷 Abrir Simulador Molar Humano ↗»</i>) y utilízalo como laboratorio dental mientras "
        "dialogas con Gemini (<i>gemini.google.com</i>). Puedes plantearle estas preguntas para investigar en clase:",
        style_body
    ))

    prompts_text = (
        "<b>1. Salud Dental en Adultos Mayores:</b> <i>«En el corte sagital del molar 3D veo la cercanía de la pulpa nerviosa a la dentina. ¿Por qué con los años se produce retracción de encías y mayor sensibilidad dental o riesgo de caries en la raíz a partir de los 60 años?»</i><br/>"
        "<b>2. La Dureza del Esmalte:</b> <i>«¿Por qué el esmalte dental es más duro que el propio hueso del esqueleto y qué hace que, una vez dañado o erosionado, el cuerpo humano ya no pueda regenerarlo de forma natural?»</i><br/>"
        "<b>3. Tratamientos y Endodoncia:</b> <i>«Al observar los conductos radiculares que bajan por las raíces en el simulador, ¿en qué consiste exactamente una endodoncia o tratamiento de conductos para salvar una muela enferma?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Salud bucodental y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-010 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-010 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
