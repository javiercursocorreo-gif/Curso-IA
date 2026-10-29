#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_001.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-001_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 01)
- 01_COD-001_Taller_Simulador_Pulmones_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/01_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-001_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/01_COD-001_Taller_Simulador_Pulmones_3D.pdf"

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

    story.append(Paragraph("<b>[COD-001] Guía Científica • El Sistema Respiratorio Humano y Árbol Bronquial 3D</b>", style_title))

    # Bloque 1: Explicación didáctica del Simulador
    story.append(Paragraph("🫁 <b>1. ¿Qué vemos en el Simulador 3D y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador biomédico interactivo reproduce en tiempo real la <b>mecánica ventilatoria del aparato respiratorio humano</b> "
        "y la arquitectura tridimensional del árbol traqueobronquial. En pantalla se observa el movimiento rítmico de <b>inspiración y espiración</b>: "
        "la expansión fisiológica de los lóbulos pulmonares (tres en el pulmón derecho y dos en el izquierdo para alojar la silueta cardíaca) "
        "y la posterior descompresión elástica del parénquima.<br/>"
        "Al activar la transparencia tisular se aprecia la <b>tráquea cartilaginosa, la carina y la estructura fractal de ramificación bronquial</b> "
        "(desde los bronquios principales primarios hasta las subdivisiones lobares y segmentarias) por donde fluye el oxígeno. Puedes <b>rotar los "
        "pulmones 360°</b> con el ratón, regular la <b>frecuencia respiratoria</b> (de 8 a 28 respiraciones por minuto) y pausar el ciclo para "
        "analizar cada estructura en reposo anatómico.",
        style_body
    ))

    # Bloque 2: Procedencia y Fuentes Científicas Oficiales
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Médico Oficial:</b> El modelo tridimensional procede de los archivos científicos de la <b>Biblioteca Nacional de Medicina "
        "de los Estados Unidos (NIH 3D Print Exchange)</b> y del atlas biomédico abierto <b>Z-Anatomy Open-Source Anatomy Project</b>.<br/>"
        "• <b>Técnica de Adquisición de Datos:</b> Malla anatómica reconstruida a partir de <b>tomografía axial computarizada de tórax de alta "
        "resolución (HRCT)</b>. Los materiales PBR reproducen con fidelidad médica los anillos cartilaginosos traqueales, la textura elástica de la pleura "
        "y las bifurcaciones vasculares de la arteria pulmonar.<br/>"
        "• <b>Morfología Fractal y Superficie Alveolar:</b> El árbol bronquial ilustra el principio biológico de optimización fractal: 23 generaciones "
        "sucesivas de dicotomía que permiten empaquetar una superficie de intercambio gaseoso de más de <b>70 metros cuadrados</b> (el tamaño de una "
        "pista de bádminton) en el reducido volumen torácico humano."
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
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«🫁 Ver Simulador Pulmones 3D»</i>) y utilízalo como laboratorio visual mientras "
        "conversas con Gemini (<i>gemini.google.com</i>). Puedes copiar y hacerle estas preguntas para profundizar en tu aprendizaje:",
        style_body
    ))

    prompts_text = (
        "<b>1. Asimetría Anatómica:</b> <i>«Estoy mirando un modelo 3D de los pulmones humanos. ¿Por qué el pulmón derecho se divide en tres lóbulos mientras que el izquierdo solo tiene dos?»</i><br/>"
        "<b>2. Respiración y Salud en Adultos Mayores:</b> <i>«En el simulador varío la velocidad de respiración entre 10 y 24 RPM. ¿Por qué la respiración diafragmática profunda calma el sistema nervioso y mejora la oxigenación cerebral en personas mayores?»</i><br/>"
        "<b>3. La Maravilla Fractal:</b> <i>«¿Por qué la naturaleza diseñó los bronquios con una geometría fractal de ramificación en lugar de conductos rectos convencionales?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Ciencia visual interactiva y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-001 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-001 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
