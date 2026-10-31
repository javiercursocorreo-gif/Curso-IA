#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_004.py
Ficha Didáctica Oficial de 1 Página (Letter):
Simulador Científico 3D Oficial: La Tierra y el Clima en Vivo (NASA Eyes on the Earth) [COD-004]
Estructura científica estricta: Explicación, Controles 360°, Acreditación Oficial (NASA Earth/JPL)
y 3 Preguntas de Reflexión para dialogar con Gemini en el aula.
"""

import os
import sys
import shutil

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/04_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-004_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
ALT_PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-004_Simulador_Tierra_Clima_NASA_Eyes.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/04_COD-004_Simulador_Tierra_Clima_3D.pdf"

def build_cod_004_taller_3d_pdf(output_path=PDF_PATH):
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
    c_blue = colors.HexColor('#0369A1')
    c_dark = colors.HexColor('#0F172A')
    c_slate = colors.HexColor('#334155')

    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.0, leading=9.5,
        textColor=c_blue, alignment=1, spaceAfter=1
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

    story = []

    # Cabecera Oficial
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA Y SIMULADORES 3D INTERACTIVOS • CIENCIAS DE LA TIERRA [COD]", style_subhead))
    story.append(HRFlowable(width="100%", thickness=1.2, color=c_primary, spaceAfter=4))

    # Título de la Ficha
    story.append(Paragraph("<b>[COD-004] Simulador 3D Oficial: La Tierra y el Clima en Vivo (NASA Eyes on the Earth)</b>", style_title))

    # Sección 1: Explicación Didáctica
    story.append(Paragraph("🌍 <b>Signos Vitales del Planeta y Observación en Tiempo Real:</b>", style_sec_h))
    story.append(Paragraph(
        "A través de <b>NASA Eyes on the Earth</b>, el alumno accede a una visión global en directo de la biosfera terrestre monitorizada por más de 20 satélites en órbita activa. "
        "El visor permite rastrear los 'signos vitales' del planeta: concentraciones globales de dióxido de carbono (CO₂) medidas por el satélite OCO-2, la evolución de la capa de ozono polar con el instrumento OMI, anomalías térmicas en la superficie marina y variaciones milimétricas en el nivel medio del mar mediante radares altimétricos como Jason y Sentinel-6 Michael Freilich.",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Sección 2: Controles 360°
    story.append(Paragraph("🎮 <b>Controles del Visor 3D & Guía de Interacción en el Aula:</b>", style_sec_h))
    ctrl_data = [
        [Paragraph("<b>🖱️ Rotación Global 360°:</b> Arrastra con el ratón para rotar el globo terráqueo e inspeccionar cualquier continente, cordillera o cuenca oceánica.", style_box_text)],
        [Paragraph("<b>🔍 Acercamiento Continuo:</b> Usa la rueda del ratón para descender desde la vista espacial global hasta los valles y costas con resolución fotográfica.", style_box_text)],
        [Paragraph("<b>🛰️ Selector de Capas Climáticas:</b> Usa los botones inferiores para alternar entre el mapa de CO₂, temperatura superficial, nivel del mar y ozono.", style_box_text)],
        [Paragraph("<b>📡 Satélites en Órbita Viva:</b> Pulsa en 'Satélites en Órbita' para ver la posición física en tiempo real de cada nave espacial que orbita sobre nuestras cabezas.", style_box_text)],
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
        "• <b>Institución Acreditada:</b> Desarrollado por la <b>NASA Earth Science Division</b> y el <b>Jet Propulsion Laboratory (JPL)</b>.<br/>"
        "• <b>Datos Satelitales Certificados:</b> Las capas visuales proceden de telemetría directa calibrada diariamente por misiones orbitales (Aqua, Terra, GRACE-FO, OCO-2 y Sentinel). No contiene proyecciones artísticas simuladas: cada gradiente de color refleja mediciones físicas reales de radiometría y espectrometría."
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
        [Paragraph("<b>Pregunta 1 • El Ciclo del CO₂:</b> <i>«Gemini, observando la capa de CO₂ en NASA Earth veo zonas con tonos rojos más intensos en el hemisferio norte. ¿Por qué cambia la concentración de dióxido de carbono entre las estaciones del año según la vegetación?»</i>", style_box_text)],
        [Paragraph("<b>Pregunta 2 • El Nivel del Mar:</b> <i>«Gemini, en el simulador veo la capa de nivel del mar con el satélite Sentinel-6. ¿Cómo consigue un satélite en el espacio medir la altura del agua en la Tierra con precisión de milímetros?»</i>", style_box_text)],
        [Paragraph("<b>Pregunta 3 • La Capa de Ozono:</b> <i>«Gemini, al mirar el polo sur en NASA Eyes veo el mapa de ozono. ¿Cómo ha evolucionado el agujero de la capa de ozono antártica gracias al Protocolo de Montreal y cómo nos protege?»</i>", style_box_text)],
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

    print(f"✅ PDF COD-004 generado con éxito en: {dest_path}")
    return dest_path

if __name__ == '__main__':
    try:
        build_cod_004_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-004: {e}")
        sys.exit(1)
