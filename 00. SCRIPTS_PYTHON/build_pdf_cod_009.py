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

    story.append(Paragraph("<b>[COD-009] Guía Científica • El Tyrannosaurus Rex: Anatomía Completa, Biomecánica y Fósil 3D</b>", style_title))

    # Bloque 1: Explicación didáctica del Simulador
    story.append(Paragraph("🦖 <b>1. ¿Qué vemos en el Simulador 3D y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador paleontológico interactivo sitúa al alumno en una sala de museo virtual ante el <b>esqueleto fósil completo del "
        "Tyrannosaurus Rex</b>, el superdepredador más imponente del Cretácico Superior. En pantalla se examina la biomecánica corporal integral "
        "de este gigante de más de 12 metros de longitud y 8 toneladas de masa:<br/>"
        "• <b>Cráneo y Potencia de Mordida:</b> Mandíbula articulada con dientes aserrados de hasta 30 cm capaces de ejercer más de 57.000 N, con "
        "órbitas orientadas hacia el frente que le otorgaban una aguda visión estereoscópica tridimensional para calcular distancias de ataque.<br/>"
        "• <b>Cuello y Tronco:</b> Potente curvatura cervical en 'S' para desgarrar presas y robusta caja torácica sostenida por una columna vertebral horizontal.<br/>"
        "• <b>Locomoción Bípeda y Cola de Contrapeso:</b> Extremidades posteriores colosales preparadas para la propulsión, contrapesadas por una "
        "larga cola maciza y musculada que actuaba como timón inercial en giros rápidos.<br/>"
        "Puedes <b>rotar el espécimen 360°</b> con el ratón sobre su pedestal de museo, activar el giradiscos automático y enfocar cada punto anatómico clave.",
        style_body
    ))

    # Bloque 2: Procedencia y Fuentes Científicas Oficiales
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Paleontológico Oficial:</b> La digitalización procede del escaneo volumétrico de especímenes de museo conservados "
        "en los archivos del <b>Field Museum of Natural History de Chicago</b> y de la red de museos de historia natural abiertos (*VR Dinosaur Museum* / AMNH).<br/>"
        "• <b>Técnica de Digitalización Fósil:</b> Reconstrucción tridimensional por <b>fotogrametría de alta precisión calibrada y escaneo láser LiDAR</b> "
        "de los huesos fosilizados reales, ensamblados respetando la postura bípeda y la biomecánica descrita en los estudios tafonómicos modernos.<br/>"
        "• <b>Rigor Paleobiológico:</b> La pose horizontal neutra elimina los mitos obsoletos del siglo XX del T-Rex erguido arrastrando la cola, "
        "reflejando el consenso científico moderno sobre su centro de gravedad y dinámica biomecánica."
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
        "conversas con Gemini (<i>gemini.google.com</i>):",
        style_body
    ))

    prompts_text = (
        "<b>1. Anatomía y Equilibrio:</b> <i>«Al rotar el esqueleto completo del T-Rex 360° en el simulador veo que su cuerpo está en equilibrio horizontal. ¿Por qué la cola era tan larga y pesada y cómo le ayudaba a caminar y girar sin caerse de bruces?»</i><br/>"
        "<b>2. Visión Binocular y Caza:</b> <i>«En el simulador enfoco la cabeza y noto que ambos ojos miran hacia adelante en vez de a los lados como en otros dinosaurios herbívoros. ¿Qué ventaja le daba esta visión binocular al cazar?»</i><br/>"
        "<b>3. Extremidades Anteriores:</b> <i>«A pesar de medir más de 12 metros, los brazos del T-Rex son sorprendentemente pequeños. ¿Tenían alguna función útil o eran restos evolutivos que ya no necesitaba?»</i>"
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
