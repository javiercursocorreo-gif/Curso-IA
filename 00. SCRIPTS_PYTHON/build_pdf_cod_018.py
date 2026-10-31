#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_018.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-018_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 18)
- 18_COD-018_Taller_Simulador_Neurona_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/18_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-018_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/18_COD-018_Taller_Simulador_Neurona_3D.pdf"

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
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & SIMULADORES CIENTÍFICOS 3D [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.5, color=accent, spaceAfter=5))

    story.append(Paragraph("<b>[COD-018] Guía Científica • Neurona Piramidal & Sinapsis Química</b>", style_title))

    # Bloque 1
    story.append(Paragraph("🧠 <b>1. ¿Qué vemos en el Simulador y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este laboratorio neurocientífico interactivo reproduce una <b>neurona piramidal de la corteza cerebral humana</b> "
        "en microscopía láser confocal de fluorescencia multicanal de alta resolución. En pantalla se distinguen el <b>soma triangular</b> (cuerpo con núcleo de ADN), "
        "el <b>árbol dendrítico apical</b> poblado de miles de espinas sinápticas, el <b>cono axónico</b> (zona gatillo) y el <b>axón mielinizado</b>.<br/>"
        "El simulador reproduce la <b>electrofisiología neuronal en tiempo real</b>: el potencial de reposo a -70 mV y el disparo del <b>potencial de acción</b> "
        "(despolarización a +30 mV por entrada masiva de iones Na⁺) que viaja a más de 100 m/s hasta los botones sinápticos terminales, provocando la liberación "
        "cuántica de neurotransmisores (glutamato, GABA, dopamina) a través de la hendidura sináptica de 20 nanómetros.",
        style_body
    ))

    # Bloque 2
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de la Neurobiología</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Neuronal Oficial:</b> Reconstrucción morfométrica tridimensional y escaneo confocal procedente de <b>NeuroMorpho.Org</b> "
        "(Krasnow Institute for Advanced Study) y el <b>NIH National Institute of Neurological Disorders and Stroke (NINDS)</b>.<br/>"
        "• <b>Modelo Biofísico de Membrana:</b> Ecuaciones de Hodgkin-Huxley y parámetros electrofisiológicos calibrados a partir de registros "
        "<i>patch-clamp</i> in vitro de neuronas piramidales de la capa V de la corteza cerebral humana.<br/>"
        "• <b>Inmunofluorescencia:</b> Marcaje biológico real mediante proteína verde fluorescente (GFP para citoesqueleto) y DAPI (para el núcleo celular)."
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

    # Bloque 3
    story.append(Paragraph("💬 <b>3. Guía de Exploración en el Aula & Conversación con Gemini</b>", style_section_h))
    story.append(Paragraph(
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«🧠 Abrir Neurona ↗»</i>) y utilízalo como microscopio virtual mientras "
        "conversas con Gemini (<i>gemini.google.com</i>). Puedes hacerle estas preguntas para investigar en clase:",
        style_body
    ))

    prompts_text = (
        "<b>1. El Impulso Eléctrico:</b> <i>«Al pulsar 'Potencial de Acción' en el simulador veo la chispa eléctrica bajar por el axón. ¿Cómo genera una célula viva electricidad sin tener cables metálicos ni baterías?»</i><br/>"
        "<b>2. Las Espinas de la Memoria:</b> <i>«¿Es verdad que cada vez que aprendemos una palabra nueva o recordamos una canción se forma físicamente una nueva espina en las dendritas de nuestras neuronas?»</i><br/>"
        "<b>3. La Mielina y la Velocidad:</b> <i>«¿Por qué la grasa de mielina que envuelve al axón hace que el pensamiento viaje 100 veces más rápido que en los nervios sin mielina?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Neurociencia interactiva y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-018 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-018 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
