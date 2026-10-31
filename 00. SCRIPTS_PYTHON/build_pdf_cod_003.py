#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_003.py
Ficha Didáctica Oficial de 1 Página (Letter):
Simulador Científico 3D Oficial: El Sistema Solar en Tiempo Real (NASA Eyes) [COD-003]
Estructura científica estricta: Explicación, Controles 360°, Acreditación Oficial (NASA/JPL)
y 3 Preguntas de Reflexión para dialogar con Gemini en el aula.
"""

import os
import sys
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/03_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-003_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
ALT_PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-003_Simulador_Sistema_Solar_NASA_Eyes.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/03_COD-003_Simulador_Sistema_Solar_3D.pdf"

def build_cod_003_taller_3d_pdf(output_path=PDF_PATH):
    dest_path = output_path
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    except Exception:
        dest_path = LOCAL_BACKUP
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    doc = SimpleDocTemplate(
        dest_path,
        pagesize=letter,
        rightMargin=36, leftMargin=36, topMargin=22, bottomMargin=20
    )
    styles = getSampleStyleSheet()

    c_primary = colors.HexColor('#0284C7')
    c_gold = colors.HexColor('#D97706')
    c_dark = colors.HexColor('#0F172A')
    c_slate = colors.HexColor('#334155')

    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.0, leading=9.5,
        textColor=c_gold, alignment=1, spaceAfter=1
    )
    style_subhead = ParagraphStyle(
        'SubheadStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.5, leading=11.5,
        textColor=c_dark, alignment=1, spaceAfter=3
    )
    style_title = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=11.5, leading=14.0,
        textColor=c_dark, spaceAfter=3
    )
    style_sec_h = ParagraphStyle(
        'SecHStyle', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=8.8, leading=11.0,
        textColor=c_primary, spaceBefore=2, spaceAfter=2
    )
    style_body = ParagraphStyle(
        'BodyStyle', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=8.1, leading=10.6,
        textColor=c_slate, spaceAfter=2
    )
    style_box_text = ParagraphStyle(
        'BoxTextStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.7, leading=10.1,
        textColor=c_dark
    )
    style_q_num = ParagraphStyle(
        'QNumStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=7.8, leading=10.2,
        textColor=c_primary
    )

    story = []

    # Cabecera Oficial
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA Y SIMULADORES 3D INTERACTIVOS • EXPLORACIÓN ESPACIAL [COD]", style_subhead))
    story.append(HRFlowable(width="100%", thickness=1.2, color=c_primary, spaceAfter=4))

    # Título de la Ficha
    story.append(Paragraph("<b>[COD-003] Simulador 3D Oficial: El Sistema Solar en Tiempo Real (NASA Eyes)</b>", style_title))

    # Sección 1: Explicación Didáctica
    story.append(Paragraph("🔭 <b>Fenómeno Científico y Observación en Tiempo Real:</b>", style_sec_h))
    story.append(Paragraph(
        "Este simulador oficial reproduce las <b>posiciones exactas en tiempo real</b> de los 8 planetas, planetas enanos como Plutón y Ceres, más de 120 lunas y sondas interestelares históricas como Voyager 1 y New Horizons. "
        "A través del motor oficial <b>NASA Eyes on the Solar System</b>, el alumno contempla la mecánica celeste kepleriana sin simplificaciones: las velocidades orbitales diferenciales (Mercurio a 47 km/s frente a Neptuno a 5,4 km/s), la inclinación de los planos orbitales y la inmensidad del vacío cósmico a escala astronómica.",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Sección 2: Controles 360°
    story.append(Paragraph("🎮 <b>Controles del Visor 3D & Guía de Interacción en el Aula:</b>", style_sec_h))
    ctrl_data = [
        [Paragraph("<b>🖱️ Giro y Órbita 360°:</b> Haz clic izquierdo y arrastra en cualquier dirección para rotar la perspectiva tridimensional del Sistema Solar desde cualquier ángulo cenital o eclíptico.", style_box_text)],
        [Paragraph("<b>🔍 Zoom Continuo:</b> Usa la rueda del ratón para pasar de la vista panorámica del plano solar al detalle minucioso de la atmósfera de Júpiter o los anillos de Saturno.", style_box_text)],
        [Paragraph("<b>🎯 Enfoque Instantáneo:</b> Haz doble clic sobre cualquier planeta, satélite o nave para fijar la cámara y descender automáticamente hasta su superficie.", style_box_text)],
        [Paragraph("<b>⏱️ Línea de Tiempo:</b> Puedes acelerar los días o retroceder siglos con la barra temporal inferior de NASA Eyes para comprobar conjunciones pasadas o futuras.", style_box_text)],
    ]
    t_ctrl = Table(ctrl_data, colWidths=[letter[0] - 72])
    t_ctrl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#94A3B8')),
        ('TOPPADDING', (0,0), (-1,-1), 2.0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.0),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_ctrl)
    story.append(Spacer(1, 2))

    # Sección 3: Procedencia Oficial
    story.append(Paragraph("🏛️ <b>Procedencia Institucional y Calidad Científica de los Datos:</b>", style_sec_h))
    prov_text = (
        "• <b>Institución Acreditada:</b> Desarrollado por el <b>Jet Propulsion Laboratory (JPL) de la NASA</b> y el <b>California Institute of Technology (Caltech)</b>.<br/>"
        "• <b>Precisión Telemétrica:</b> Las trayectorias se basan en el sistema matemático de efemérides planetarias <b>DE440</b> de JPL, utilizado por los directores de vuelo de la NASA para la navegación real de misiones interplanetarias. Cero dibujos inventados o mallas ficticias: datos 100% científicos y auditables."
    )
    t_prov = Table([[Paragraph(prov_text, style_box_text)]], colWidths=[letter[0] - 72])
    t_prov.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ECFDF5')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#10B981')),
        ('TOPPADDING', (0,0), (-1,-1), 3.0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.0),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_prov)
    story.append(Spacer(1, 2))

    # Sección 4: Preguntas para Gemini
    story.append(Paragraph("💬 <b>Guía de Exploración en el Aula & Preguntas para Dialogar con Gemini:</b>", style_sec_h))
    q_data = [
        [Paragraph("<b>Pregunta 1 • Velocidades Orbitales:</b> <i>«Gemini, observando el simulador de NASA Eyes veo que Mercurio se mueve rapidísimo alrededor del Sol mientras que Saturno y Urano van muy lentos. ¿Por qué ocurre esto según la tercera ley de Kepler y la gravedad solar?»</i>", style_box_text)],
        [Paragraph("<b>Pregunta 2 • El Vacío Espacial:</b> <i>«Gemini, cuando alejo el zoom en NASA Eyes los planetas casi desaparecen y solo se ve oscuridad. ¿Por qué es tan difícil viajar entre mundos y qué distancia real separa a la Tierra de Marte en su punto más cercano?»</i>", style_box_text)],
        [Paragraph("<b>Pregunta 3 • Las Sondas Voyager:</b> <i>«Gemini, pulso en Voyager 1 en el simulador y veo que está lejísimos, fuera del plano de los planetas. ¿Hacia dónde se dirige ahora mismo y qué mensaje lleva grabado en su disco de oro?»</i>", style_box_text)],
    ]
    t_q = Table(q_data, colWidths=[letter[0] - 72])
    t_q.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EFF6FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#3B82F6')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_q)

    doc.build(story)

    # Duplicar con nombre alternativo y respaldo local
    try:
        shutil.copy2(dest_path, ALT_PDF_PATH)
        os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
        shutil.copy2(dest_path, LOCAL_BACKUP)
    except Exception:
        pass

    print(f"✅ PDF COD-003 generado con éxito en: {dest_path}")
    return dest_path

if __name__ == '__main__':
    try:
        build_cod_003_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-003: {e}")
        sys.exit(1)
