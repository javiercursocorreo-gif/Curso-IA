#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_003.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-003_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 03)
- 03_COD-003_Taller_Simulador_Pompeya_HD.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/03_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-003_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/03_COD-003_Taller_Simulador_Pompeya_HD.pdf"

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

    accent = colors.HexColor('#B45309') # Tono terracota arqueológico

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

    story.append(Paragraph("<b>[COD-003] Guía Arqueológica • Reconstrucción 3D de Pompeya y Ruinas del 79 d.C.</b>", style_title))

    # Bloque 1: Explicación didáctica del Simulador
    story.append(Paragraph("🏛️ <b>1. ¿Qué vemos en el Simulador 3D y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador arqueológico interactivo permite realizar una <b>comparativa temporal deslizante directa</b> entre las ruinas excavadas "
        "de la ciudad romana de Pompeya y su <b>reconstrucción arquitectónica tridimensional fidedigna en el año 79 d.C.</b>, momentos antes de la catastrófica "
        "erupción pliniana del monte Vesubio.<br/>"
        "Al deslizar el control central en pantalla, el alumno puede observar la transformación de una <b>domus romana señorial</b>: el <i>atrium</i> con su "
        "estanque central de recogida pluvial (<i>impluvium</i>) y apertura cenital (<i>compluvium</i>), las columnas de orden corintio con estuco original, "
        "los pavimentos de mosaico geométrico con teselas de mármol y las paredes decoradas con frescos policromados del IV estilo pompeyano. El simulador "
        "permite hacer <b>zoom de alta definición</b> sobre los detalles constructivos, contrastando la degradación del tiempo y el colapso volcánico con el "
        "esplendor del urbanismo clásico romano.",
        style_body
    ))

    # Bloque 2: Procedencia y Fuentes Científicas Oficiales
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D</b>", style_section_h))
    fuente_text = (
        "• <b>Institución Arqueológica Oficial:</b> Los levantamientos fotogramétricos y datos topográficos proceden de las excavaciones oficiales del "
        "<b>Parco Archeologico di Pompei</b> (Ministero della Cultura de Italia) y del archivo de digitalización de patrimonio mundial de la <b>UNESCO</b>.<br/>"
        "• <b>Técnicas de Escaneado Científico:</b> La comparativa utiliza levantamientos de <b>láser escáner terrestre LiDAR y fotogrametría aérea con drones</b> "
        "realizados por el consorcio internacional <b>CyArk (Cyber-Archaeology)</b>. Los modelos digitales reproducen con precisión de milímetros las cotas "
        "reales de los muros de toba volcánica y ladrillo romano (<i>opus latericium</i>).<br/>"
        "• <b>Reconstrucción Histórica Validada:</b> La restitución 3D de la techumbre, estucos y policromías fue diseñada bajo la dirección de arqueólogos clásicos "
        "especializados en arquitectura romana del siglo I, garantizando rigor histórico en la iluminación natural y en los pigmentos de rojo cinabrio y azul egipcio."
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
        "Abre el simulador en tu pantalla (en el mapa de la clase pulsa <i>«🏛️ Ver Simulador Pompeya 3D»</i>) y utilízalo como ventana arqueológica mientras "
        "le haces preguntas a Gemini (<i>gemini.google.com</i>):",
        style_body
    ))

    prompts_text = (
        "<b>1. Arquitectura Doméstica:</b> <i>«Estoy mirando una domus pompeyana reconstruida en 3D. ¿Qué función tenían el impluvium y el compluvium en el suministro de agua de la casa?»</i><br/>"
        "<b>2. Vida Cotidiana:</b> <i>«¿Cómo era la iluminación y la ventilación de las habitaciones interiores (cubícula) de una vivienda en el año 79 d.C.?»</i><br/>"
        "<b>3. Geología y Arqueología:</b> <i>«¿Por qué la ceniza y el lapilli del Vesubio conservaron los frescos y mosaicos durante casi dos mil años en lugar de destruirlos?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Arqueología virtual y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-003 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-003 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
