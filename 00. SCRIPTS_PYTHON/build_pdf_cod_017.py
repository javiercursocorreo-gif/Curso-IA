#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_017.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-017_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 17)
- 17_COD-017_Taller_Simulador_Tutankamon_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/17_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-017_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/17_COD-017_Taller_Simulador_Tutankamon_3D.pdf"

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
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & SIMULADORES CIENTÍFICOS 3D [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.5, color=accent, spaceAfter=5))

    story.append(Paragraph("<b>[COD-017] Guía Científica • Máscara Funeraria de Tutankamón (KV62)</b>", style_title))

    # Bloque 1
    story.append(Paragraph("👑 <b>1. ¿Qué vemos en el Simulador y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador arqueológico interactivo reproduce la <b>Máscara Funeraria del faraón Tutankamón</b> (c. 1323 a.C., Dinastía XVIII) "
        "en fotografía macro de altísima resolución desde el Museo Egipcio de El Cairo. La obra maestra pesa <b>10,23 kg de oro macizo</b> de 24 quilates "
        "y reproduce el rostro sereno y divinizado del monarca.<br/>"
        "En pantalla se examinan los detalles canónicos: el <b>tocado Nemes</b> a franjas alternas de oro y pasta azul de lapislázuli; el <b>Ureo real</b> "
        "en la frente (la diosa cobra Wadjet y la diosa buitre Nejbet); los ojos esculpidos en <b>cuarzo blanco y obsidiana volcánica</b> perfilados con kohl negro; "
        "la <b>barba osiríaca trenzada</b> de 2,5 kg; y el <b>collar Usekh</b> de once hileras. Puedes alternar la <b>luz rasante</b> para ver las huellas de cincel y la <b>radiografía de rayos X</b>.",
        style_body
    ))

    # Bloque 2
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de la Arqueometría</b>", style_section_h))
    fuente_text = (
        "• <b>Registro Museográfico Oficial:</b> Archivo oficial del <b>Museo Egipcio de El Cairo (Registro General JE 60672)</b> y los diarios de excavación "
        "originales de <b>Howard Carter (1925, tumba KV62 del Valle de los Reyes)</b> custodiados en el Griffith Institute de Oxford.<br/>"
        "• <b>Estudios Arqueométricos y Metalografía:</b> Datos de composición elemental por fluorescencia de rayos X (XRF) y tomografía computarizada (CT) "
        "realizados por el <b>Ministerio de Antigüedades de Egipto</b> y The Metropolitan Museum of Art (Met).<br/>"
        "• <b>Orfebrería Dinástica:</b> Constatación de la técnica de batido en frío y ensamblaje de dos láminas de oro de diferente pureza (23,5k rostro, 18,4k cuello)."
    )
    t_box = Table([[Paragraph(fuente_text, style_box_text)]], colWidths=[letter[0] - 72])
    t_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FEFCE8')),
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
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«👑 Abrir Máscara Tutankamón ↗»</i>) y utilízalo como museo arqueológico mientras "
        "conversas con Gemini (<i>gemini.google.com</i>). Puedes hacerle estas preguntas para investigar en clase:",
        style_body
    ))

    prompts_text = (
        "<b>1. El Misterio de las Dos Láminas de Oro:</b> <i>«Al examinar la radiografía en el simulador se ve una unión en el cuello. ¿Por qué el rostro tiene un oro más puro y rojizo que el tocado Nemes? ¿Perteneció la máscara originalmente a la reina Nefertiti?»</i><br/>"
        "<b>2. La Mirada Eterna:</b> <i>«¿Por qué los antiguos egipcios usaron obsidiana negra y cuarzo para los ojos en lugar de pintarlos simplemente con pigmentos?»</i><br/>"
        "<b>3. La Piedra de Afganistán:</b> <i>«¿Cómo consiguieron los egipcios hace 3.300 años toneladas de lapislázuli si las minas más cercanas estaban en las montañas de Afganistán a más de 4.000 kilómetros?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Arqueología del Antiguo Egipto y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-017 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-017 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
