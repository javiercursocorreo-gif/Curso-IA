#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_005.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 5. COD-005_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 05)
- 05_COD-005_Taller_Simulador_Sistema_Solar_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/05_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "5. COD-005_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/05_COD-005_Taller_Simulador_Sistema_Solar_3D.pdf"

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

    accent = colors.HexColor('#D97706') # Tono ámbar/dorado solar

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

    story.append(Paragraph("<b>[COD-005] Guía Astronómica • El Sistema Solar: Dinámica Orbital Planetaria y Kepler 3D</b>", style_title))

    # Bloque 1: Explicación didáctica del Simulador
    story.append(Paragraph("🪐 <b>1. ¿Qué vemos en el Simulador 3D y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este planetario heliocéntrico interactivo 3D reproduce con precisión física el <b>movimiento de traslación y rotación de los 8 planetas</b> "
        "alrededor del Sol, siguiendo las <b>Leyes de Gravitación Universal de Newton</b> y las <b>Leyes del Movimiento Planetario de Kepler</b> (órbitas "
        "elípticas con velocidad orbital inversamente proporcional a la distancia del perihelio).<br/>"
        "El simulador permite contrastar las dos familias planetarias de nuestro sistema: los <b>planetas rocosos interiores</b> (Mercurio, Venus, la Tierra con "
        "su satélite lunar y Marte) y los <b>gigantes gaseosos exteriores</b> (Júpiter con sus bandas atmosféricas ciclónicas, Saturno con su sistema de anillos "
        "de partículas de hielo, Urano y Neptuno). Mediante la botonera interactiva puedes <b>acelerar el tiempo orbital (de 1x a 50x)</b>, activar las trazas "
        "luminosas de las órbitas elípticas, rotar libremente la cámara espacial 360° y hacer zoom a cada planeta para contemplar su rotación axial.",
        style_body
    ))

    # Bloque 2: Procedencia y Fuentes Científicas Oficiales
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D</b>", style_section_h))
    fuente_text = (
        "• <b>Agencia Espacial y Repositorios Oficiales:</b> Todos los datos orbitales y texturas superficiales proceden de la <b>NASA (National Aeronautics and Space Administration)</b> "
        "a través del <b>Jet Propulsion Laboratory (JPL)</b> y el <i>NASA Scientific Visualization Studio</i>.<br/>"
        "• <b>Mosaicos Satelitales y Fotografía Espacial:</b> Los mapas fotográficos esféricos de cada planeta fueron capturados por sondas espaciales emblemáticas: "
        "la misión <b>Cassini-Huygens</b> (mapas de Júpiter y anillos de Saturno), <b>Lunar Reconnaissance Orbiter (LRO)</b> para el relieve lunar, la sonda <b>Mars Global Surveyor</b> "
        "para la topografía marciana y las cámaras WFC3 del <b>Telescopio Espacial Hubble</b>.<br/>"
        "• <b>Parámetros Físicos Rigurosos:</b> Las distancias relativas, excentricidades orbitales y periodos siderales de traslación se sincronizan con las efemérides astronómicas "
        "del <i>Solar System Dynamics Group (SSD)</i> del Instituto Tecnológico de California (Caltech)."
    )
    t_box = Table([[Paragraph(fuente_text, style_box_text)]], colWidths=[letter[0] - 72])
    t_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FEF3C7')),
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
        "Abre el planetario en tu pantalla (en el mapa de la clase pulsa <i>«🪐 Ver Simulador Sistema Solar 3D»</i>) y hazle estas preguntas a Gemini "
        "(<i>gemini.google.com</i>) para explorar los enigmas del cosmos:",
        style_body
    ))

    prompts_text = (
        "<b>1. Leyes de Kepler:</b> <i>«Estoy mirando el simulador del Sistema Solar. ¿Por qué Mercurio se desplaza a tanta velocidad (88 días por vuelta) mientras que Neptuno tarda 165 años terrestres en completar una órbita?»</i><br/>"
        "<b>2. Astronomía y Escalas:</b> <i>«¿Por qué en los libros y simuladores el tamaño de los planetas se agranda respecto a la inmensidad de las distancias espaciales que los separan?»</i><br/>"
        "<b>3. Exploración Espacial:</b> <i>«¿Cómo consiguen las sondas espaciales de la NASA aprovechar la gravedad de planetas como Júpiter para acelerar su viaje hacia los confines del sistema solar?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Astronomía visual y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-005 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-005 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
