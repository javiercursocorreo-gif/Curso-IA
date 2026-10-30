#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_014.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-014_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 14)
- 14_COD-014_Taller_Simulador_Jupiter_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/14_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-014_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/14_COD-014_Taller_Simulador_Jupiter_3D.pdf"

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

    accent = colors.HexColor('#6D28D9')

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
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & SIMULADORES CIENTÍFICOS 3D [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.5, color=accent, spaceAfter=5))

    story.append(Paragraph("<b>[COD-014] Guía Científica • Júpiter y sus Auroras Ultravioletas 3D (NASA)</b>", style_title))

    # Bloque 1
    story.append(Paragraph("🪐 <b>1. ¿Qué vemos en el Simulador 3D y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador de astrofísica planetaria interactivo reproduce el <b>globo del gigante gaseoso Júpiter y sus colosales auroras ultravioletas</b> "
        "polares en tiempo real. En pantalla se distinguen las bandas atmosféricas zonales y cinturones de nubes de amoníaco y agua, junto con la "
        "<b>Gran Mancha Roja</b> (la mayor tormenta anticiclónica del sistema solar, activa desde hace más de tres siglos y con un diámetro mayor que la Tierra).<br/>"
        "En los polos norte y sur se proyectan los <b>óvalos aurorales permanentes</b> generados por la potente magnetosfera joviana (20.000 veces más intensa que "
        "la terrestre). A diferencia de las auroras de la Tierra, las de Júpiter están alimentadas ininterrumpidamente por el <b>toro de plasma de la luna Ío</b>, "
        "cuyos volcanes expulsan una tonelada de dióxido de azufre por segundo hacia el campo magnético. Puedes <b>rotar el planeta 360°</b> con el ratón, "
        "regular el espectro ultravioleta/rayos X y observar el punto brillante que conecta magnéticamente a Ío con la atmósfera joviana.",
        style_body
    ))

    # Bloque 2
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Planetario Oficial:</b> La cartografía atmosférica procede del <b>Planetary Data System (PDS) de la NASA</b>, a partir de mosaicos "
        "cilíndricos calibrados de la sonda espacial <b>NASA Cassini (Imaging Science Subsystem)</b> durante su sobrevuelo de asistencia gravitatoria.<br/>"
        "• <b>Espectrometría Ultravioleta:</b> Los óvalos aurorales polares se basan en observaciones multiespectrales del <b>Telescopio Espacial Hubble "
        "(cámara STIS - Space Telescope Imaging Spectrograph)</b> y de la misión orbital polar <b>NASA Juno</b>.<br/>"
        "• <b>Física Magnetosférica:</b> El modelo reproduce las líneas de inducción magnética dipolar y los toroides de partículas cargadas que colisionan "
        "con los átomos de hidrógeno a velocidades relativistas en la termosfera joviana."
    )
    t_box = Table([[Paragraph(fuente_text, style_box_text)]], colWidths=[letter[0] - 72])
    t_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F5F3FF')),
        ('BOX', (0,0), (-1,-1), 1.2, accent),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_box)
    story.append(Spacer(1, 4))

    # Bloque 3
    story.append(Paragraph("💬 <b>3. Guía de Exploración en el Aula & Conversación con Gemini</b>", style_section_h))
    story.append(Paragraph(
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«🪐 Abrir Auroras Júpiter ↗»</i>) y utilízalo como observatorio astronómico mientras "
        "conversas con Gemini (<i>gemini.google.com</i>). Puedes hacerle estas preguntas para investigar en clase:",
        style_body
    ))

    prompts_text = (
        "<b>1. Auroras Eternas:</b> <i>«Al rotar Júpiter en el simulador veo los anillos luminosos en ambos polos. ¿Por qué las auroras de Júpiter nunca se apagan mientras que en la Tierra solo ocurren tras tormentas solares?»</i><br/>"
        "<b>2. La Luna Ío y el Azufre:</b> <i>«¿Cómo consiguen los volcanes de la pequeña luna Ío inyectar material en el campo magnético de Júpiter a cientos de miles de kilómetros de distancia?»</i><br/>"
        "<b>3. La Gran Mancha Roja:</b> <i>«¿Por qué la Gran Mancha Roja ha resistido más de 300 años sin desvanecerse a diferencia de los huracanes de nuestro planeta que mueren en pocos días?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Astrofísica visual interactiva y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-014 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-014 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
