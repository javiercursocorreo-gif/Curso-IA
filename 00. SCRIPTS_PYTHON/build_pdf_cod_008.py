#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_008.py
Genera la Ficha Didáctica Científica Oficial de 1 Página:
- 4. COD-008_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf (Sesión 08)
- 08_COD-008_Taller_Simulador_Motor_3D.pdf (Catálogo Central)
"""

import os
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/08_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-008_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/08_COD-008_Taller_Simulador_Motor_3D.pdf"

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

    story.append(Paragraph("<b>[COD-008] Guía Científica • El Motor Bóxer 3D: Cinemática, Presión y Termografía CAD</b>", style_title))

    # Bloque 1: Explicación didáctica del Simulador
    story.append(Paragraph("⚙️ <b>1. ¿Qué vemos en el Simulador 3D y qué fenómeno reproduce?</b>", style_section_h))
    story.append(Paragraph(
        "Este simulador de ingeniería mecánica interactivo reproduce con fidelidad cinemática el <b>funcionamiento interno de un motor térmico "
        "bóxer de dos cilindros opuestos horizontalmente (180°)</b>. En pantalla se aprecia la transformación continua del movimiento lineal "
        "alternativo de los <b>pistones de aluminio forjado</b> en movimiento rotativo del <b>cigüeñal equilibrado</b> mediante las <b>bielas "
        "de transmisión de acero cromo-níquel</b>.<br/>"
        "El simulador cuenta con <b>tres modos de inspección visual en tiempo real</b>: <i>Metálico Real</i> (renderizado PBR industrial con "
        "reflejos de mecanizado), <i>Termografía</i> (mapa de calor por gradiente de color que reproduce la temperatura de culata que alcanza "
        "los 420 °C durante la combustión) y <i>Rayos X</i> (transparencia estructural para examinar el juego biela-manivela interno). Puedes "
        "<b>rotar el motor 360°</b> con el ratón, regular el tacómetro de <b>300 a 4.500 RPM</b> y monitorizar la telemetría con velocidad angular, "
        "presión máxima en cámara (hasta 68 bar) y esfuerzo en biela (kN).",
        style_body
    ))

    # Bloque 2: Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D
    story.append(Paragraph("🔬 <b>2. Procedencia Oficial y Fuentes Científicas de las Imágenes y Escaneo 3D</b>", style_section_h))
    fuente_text = (
        "• <b>Archivos Técnicos de Ingeniería Mecánica:</b> Las cotas dimensionales y tolerancias cinemáticas proceden de planos normalizados "
        "según los estándares de la <b>Society of Automotive Engineers (SAE) y normativas ISO</b> para motores de combustión de cilindros opuestos "
        "empleados en aviación ligera y automoción clásica.<br/>"
        "• <b>Propiedades de Aleaciones Industriales:</b> Las texturas PBR y comportamientos térmicos replican especificaciones metalúrgicas reales: "
        "aleación de aluminio forjado 2618 (pistones resistentes a dilatación extrema) y acero forjado 4340 cromo-molibdeno-níquel para bielas de alta fatiga.<br/>"
        "• <b>Simulación Física y Dinámica de Fluidos:</b> Las curvas de telemetría calculan la velocidad angular precisa en función del régimen "
        "seleccionado, simulando el empuje volumétrico de expansión y la disipación térmica del bloque refrigerado por aire."
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
        "Abre el simulador en tu navegador (en el mapa pulsa <i>«⚙️ Abrir Motor Bóxer 3D ↗»</i>) y utilízalo como banco de pruebas interactivo mientras "
        "dialogas con Gemini (<i>gemini.google.com</i>). Puedes plantearle estas preguntas para reflexionar en clase:",
        style_body
    ))

    prompts_text = (
        "<b>1. Equilibrio del Motor Bóxer:</b> <i>«En el simulador veo que los dos pistones se mueven en sentidos opuestos a la vez. ¿Por qué los motores bóxer tienen un equilibrado natural tan suave y apenas producen vibraciones en comparación con un motor en línea?»</i><br/>"
        "<b>2. Cinemática y Mecanismos:</b> <i>«Al activar el modo Rayos X contemplo cómo la biela oscila al girar el cigüeñal. ¿Cómo consigue este mecanismo biela-manivela convertir la fuerza explosiva en giro para las ruedas?»</i><br/>"
        "<b>3. Rendimiento y Calor:</b> <i>«En el modo Termografía veo la culata a más de 400 °C. ¿Qué porcentaje del combustible se transforma en movimiento útil y cuánto se pierde en calor y fricción?»</i>"
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
    story.append(Paragraph("Material didáctico adaptado pedagógicamente para personas mayores (60+). Ingeniería visual interactiva y agilidad mental con Inteligencia Artificial.", style_footer))

    doc.build(story)

def main():
    build_pdf(LOCAL_BACKUP)
    print(f"✅ Ficha COD-008 generada en catálogo: {LOCAL_BACKUP}")
    try:
        shutil.copy2(LOCAL_BACKUP, PDF_PATH)
        print(f"✅ Ficha COD-008 sincronizada en sesión: {PDF_PATH}")
    except Exception as e:
        print(f"⚠️ Nota de copia: {e}")

if __name__ == "__main__":
    main()
