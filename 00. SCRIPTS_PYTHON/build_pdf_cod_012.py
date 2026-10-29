#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_012.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-012_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 12)
- 12_COD-012_Taller_Simulador_Helix_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/12_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-012_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/12_COD-012_Taller_Simulador_Helix_3D.pdf"

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

    story.append(Paragraph("<b>[COD-012] Guía Científica • La Nebulosa Helix 3D: Astrofísica de una Enana Blanca (NASA)</b>", style_title))

    # Bloque 1: Explicación didáctica del Simulador
    story.append(Paragraph("🌌 <b>1. ¿Qué vemos en el Simulador 3D y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador astronómico interactivo reproduce la estructura tridimensional de la <b>Nebulosa planetaria Helix (NGC 7293)</b>, "
        "conocida como el 'Ojo de Dios', ubicada a 650 años luz en la constelación de Acuario. En pantalla se contempla el destino cósmico "
        "final que le aguarda a estrellas de masa media como nuestro Sol: tras agotar su combustible nuclear de hidrógeno y helio, el núcleo "
        "estelar colapsa en una <b>enana blanca central ultradensa y ardiente</b> (a más de 120.000 K de temperatura superficial).<br/>"
        "La estrella moribunda expulsa sus capas gaseosas exteriores, creando una envoltura toroidal de <b>hidrógeno molecular, oxígeno ionizado "
        "(azul-verdoso) y nitrógeno/hidrógeno alfa (rojo brillante)</b> que se expande a más de 40 km/s por el medio interestelar. En el anillo "
        "interno se aprecian los espectaculares <b>nudos cometarios</b> (gotas gaseosas densas con colas de evaporación apuntando en dirección opuesta "
        "al núcleo). Puedes <b>rotar la nebulosa 360°</b> para comprobar su verdadera geometría cilíndrica tridimensional.",
        style_body
    ))

    # Bloque 2: Procedencia y Fuentes Científicas Oficiales
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Astronómico Oficial:</b> Los datos multiespectrales proceden del archivo unificado de la <b>NASA, ESA y Space Telescope "
        "Science Institute (STScI)</b>, compilados a partir de observaciones directas en espectro visible e infrarrojo.<br/>"
        "• <b>Instrumentación Espacial de Vanguardia:</b> Mosaico volumétrico calibrado combinando imágenes ópticas del <b>Telescopio Espacial Hubble "
        "(cámara ACS)</b>, datos infrarrojos del <b>Telescopio Espacial Spitzer (IRAC/MIPS)</b> y cartografía térmica del telescopio <b>VISTA del "
        "Observatorio Europeo Austral (ESO)</b> en Cerro Paranal (Chile).<br/>"
        "• <b>Física Espectral:</b> La paleta cromática traduce con rigor las longitudes de onda de emisión atómica: verde azulado para el doblemente "
        "ionizado [O III] a 500,7 nm y rojo profundo para el hidrógeno H-alfa a 656,3 nm y [N II]."
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
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«🌌 Abrir Nebulosa Helix 3D ↗»</i>) y utilízalo como observatorio espacial mientras "
        "dialogas con Gemini (<i>gemini.google.com</i>). Puedes plantearle estas preguntas para reflexionar en clase:",
        style_body
    ))

    prompts_text = (
        "<b>1. El Futuro de Nuestro Sol:</b> <i>«Al rotar la Nebulosa Helix en 3D veo la diminuta estrella enana blanca en el centro. ¿Es este el destino final que le espera a nuestro propio Sol dentro de unos 5.000 millones de años?»</i><br/>"
        "<b>2. La Forma Real de la Nebulosa:</b> <i>«Desde la Tierra parece un anillo o un ojo plano, pero en el simulador 3D se aprecia que es un cilindro o reloj de arena apuntando hacia nosotros. ¿Por qué la perspectiva engaña en astronomía?»</i><br/>"
        "<b>3. El Reciclaje Cósmico:</b> <i>«¿Qué ocurrirá con todo ese gas de oxígeno, carbono y nitrógeno expulsado por la estrella moribunda cuando se mezcle con nubes moleculares en la galaxia?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Astronomía visual interactiva y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-012 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-012 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
