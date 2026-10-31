#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_016.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-016_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 16)
- 16_COD-016_Taller_Simulador_Higado_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/16_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-016_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/16_COD-016_Taller_Simulador_Higado_3D.pdf"

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

    accent = colors.HexColor('#BE123C')

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

    story.append(Paragraph("<b>[COD-016] Guía Científica • Hígado Humano y Sistema Hepatobiliar Real</b>", style_title))

    # Bloque 1
    story.append(Paragraph("🩺 <b>1. ¿Qué vemos en el Simulador y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este laboratorio biomédico interactivo reproduce la <b>anatomía quirúrgica del hígado humano y las vías biliares</b> "
        "a partir de disecciones y tomografías computarizadas de alta fidelidad. En pantalla se exploran el <b>lóbulo derecho voluminoso</b> (65-70% de la masa), "
        "el <b>lóbulo izquierdo afilado</b>, la <b>vesícula biliar</b> en su fosa cística y la <b>tríada portal</b> (vena porta, arteria hepática propia y colédoco).<br/>"
        "El simulador reproduce la <b>doble circulación hepática</b>: el 75% del flujo sanguíneo procede de la vena porta (transportando nutrientes absorbidos del intestino) "
        "y el 25% de la arteria hepática (sangre oxigenada). Permite activar las líneas divisorias de la <b>segmentación de Couinaud (Segmentos I a VIII)</b>, "
        "fundamentales para la cirugía de resección y trasplante de hígado sin hemorragia masiva.",
        style_body
    ))

    # Bloque 2
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes Médicas</b>", style_section_h))
    fuente_text = (
        "• <b>Repositorio Anatómico Oficial:</b> Cortes fotográficos criomicrotómicos y modelos 3D procedentes del <b>Visible Human Project de la "
        "U.S. National Library of Medicine (NLM)</b> y el <b>NIH 3D Print Exchange</b>.<br/>"
        "• <b>Clínica y Hemodinámica:</b> Parámetros fisiológicos y tasas de depuración basadas en las guías canónicas de la <b>American Association "
        "for the Study of Liver Diseases (AASLD)</b> y el <i>Tratado de Cirugía Hepática de Bismuth y Couinaud</i>.<br/>"
        "• <b>Microarquitectura Lobulillar:</b> Representación precisa del drenaje hacia la vena cava inferior a través de las tres venas suprahepáticas."
    )
    t_box = Table([[Paragraph(fuente_text, style_box_text)]], colWidths=[letter[0] - 72])
    t_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFF1F2')),
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
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«🩺 Abrir Hígado ↗»</i>) y utilízalo como atlas médico mientras "
        "conversas con Gemini (<i>gemini.google.com</i>). Puedes hacerle estas preguntas para investigar en clase:",
        style_body
    ))

    prompts_text = (
        "<b>1. La Doble Circulación:</b> <i>«Al activar el realce vascular en el simulador veo la vena porta azul y la arteria hepática roja. ¿Por qué el hígado necesita recibir sangre por dos vías distintas a la vez?»</i><br/>"
        "<b>2. La Vesícula Biliar:</b> <i>«¿Por qué cuando a una persona le operan y le extirpan la vesícula biliar por tener piedras (cálculos) puede seguir viviendo con total normalidad?»</i><br/>"
        "<b>3. La Regeneración Hepática:</b> <i>«¿Cómo es posible que si a un donante vivo le extirpan el 60% de su hígado para un trasplante, el órgano vuelva a crecer a su tamaño normal en pocas semanas?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Anatomía médica interactiva y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-016 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-016 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
