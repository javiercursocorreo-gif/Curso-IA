#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_011.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-011_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 11)
- 11_COD-011_Taller_Simulador_Stradivarius_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/11_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-011_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/11_COD-011_Taller_Simulador_Stradivarius_3D.pdf"

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

    accent = colors.HexColor('#B45309')

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

    story.append(Paragraph("<b>[COD-011] Guía Científica • El Violín Stradivarius 3D: Acústica, Luthería y Resonancia</b>", style_title))

    # Bloque 1: Explicación didáctica del Simulador
    story.append(Paragraph("🎻 <b>1. ¿Qué vemos en el Simulador 3D y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador acústico interactivo reproduce con fidelidad milimétrica el célebre <b>Violín Stradivarius 'The Gould' (1693)</b>, "
        "obra maestra del luthier Antonio Stradivari en Cremona (Italia). En pantalla se contempla la estructura anatómica que produce su "
        "inigualable resonancia armónica: la <b>tabla armónica de abeto rojo</b> (tallada con veta densa y regular para maximizar la velocidad de "
        "propagación del sonido), el <b>fondo y aros de arce rizado europeo</b>, las <b>aberturas acústicas en 'f'</b> (diseñadas para proyectar las "
        "frecuencias medias y agudas con pureza cristalina) y el puente de madera tallada que transmite la vibración de las cuatro cuerdas a la caja.<br/>"
        "Puedes <b>rotar el instrumento 360°</b> con el ratón, examinar la curvatura del mástil de ébano y el clavijero, aislar las áreas de resonancia "
        "y apreciar la refracción lumínica del barniz al aceite original, formulado con resinas naturales y minerales de la época barroca.",
        style_body
    ))

    # Bloque 2: Procedencia y Fuentes Científicas Oficiales
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Museístico Oficial:</b> La digitalización 3D procede de la colección de instrumentos históricos del <b>Metropolitan Museum of "
        "Art de Nueva York (The Met Open Access)</b>, que conserva y expone el espécimen original donado por George Gould en 1955.<br/>"
        "• <b>Técnica de Adquisición Fotogramétrica:</b> Malla geométrica tridimensional reconstruida mediante <b>fotogrametría calibrada de ultra-alta "
        "resolución (8K)</b> y microtomografía acústica en colaboración con el <b>Museo del Violino de Cremona</b>. Esta técnica preserva el mapa exacto "
        "de desgaste del barniz y las microondulaciones de la madera sin alterar el instrumento.<br/>"
        "• <b>Física de Materiales Acústicos:</b> La veta de la madera responde a las características de abetos recolectados durante el 'Mínimo de Maunder', "
        "período de frío extremo con anillos de crecimiento excepcionalmente estrechos que otorgan una rigidez y ligereza únicas."
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
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«🎻 Abrir Simulador Violín Stradivarius ↗»</i>) y utilízalo como laboratorio acústico mientras "
        "dialogas con Gemini (<i>gemini.google.com</i>). Puedes plantearle estas preguntas para investigar en clase:",
        style_body
    ))

    prompts_text = (
        "<b>1. El Clima y la Madera:</b> <i>«¿Por qué los científicos afirman que la Pequeña Edad de Hielo en el siglo XVII hizo que los abetos alpinos crecieran con madera tan densa que influyó en el timbre irrepetible de Stradivari?»</i><br/>"
        "<b>2. Acústica de las Efes:</b> <i>«En el simulador observo las aberturas en forma de 'f' a ambos lados del puente. ¿Por qué tienen esa forma curvada en vez de ser orificios redondos como en una guitarra clásica?»</i><br/>"
        "<b>3. El Enigma del Barniz:</b> <i>«¿Qué componentes químicos y minerales contenía el legendario barniz de Cremona y qué papel desempeña en proteger la madera sin ahogar su vibración armónica?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Acústica musical interactiva y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-011 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-011 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
