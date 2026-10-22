#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_037.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-037_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 37 del Curso de IA (Taller: Crea tu propio simulador de la piel humana y capas tisulares).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/37_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-037_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/037_COD-037_Taller_Simulador_3D.pdf"

def build_cod_037_taller_3d_pdf(output_path=PDF_PATH):
    dest_path = output_path
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "wb") as _:
            pass
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

    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.0,
        textColor=colors.HexColor('#E11D48'), alignment=1, spaceAfter=1
    )
    style_block = ParagraphStyle(
        'BlockStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.8,
        textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=4
    )
    style_title = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=11.5, leading=14.0,
        textColor=colors.HexColor('#0F172A'), spaceAfter=3
    )
    style_section_h = ParagraphStyle(
        'SectionHStyle', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=8.8, leading=11.2,
        textColor=colors.HexColor('#E11D48'), spaceBefore=3, spaceAfter=2
    )
    style_body = ParagraphStyle(
        'BodyStyle', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=7.9, leading=10.5,
        textColor=colors.HexColor('#1E293B'), spaceAfter=2
    )
    style_task = ParagraphStyle(
        'TaskStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.7, leading=10.1,
        textColor=colors.HexColor('#0F172A')
    )
    style_prompt = ParagraphStyle(
        'PromptStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.3, leading=9.6,
        textColor=colors.HexColor('#0F172A')
    )

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & TALLER DE CÓDIGO CON GEMINI [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#E11D48'), spaceAfter=4))

    story.append(Paragraph("<b>[COD-037] Taller: Crea tu propio simulador de la piel humana y capas tisulares</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • De Espectador a Creador con IA:</b>", style_section_h))
    story.append(Paragraph("En esta sesión crearás con Gemini un bloque histológico 3D de la piel humana: Epidermis, Dermis e Hipodermis con sus folículos pilosos, glándulas sebáceas, músculo erector del pelo y asas capilares. Simularás en directo las respuestas de termorregulación: vasodilatación, sudoración ecrina y el reflejo pilomotor de la piel de gallina ante el frío.", style_body))

    # Lista de Tareas
    story.append(Paragraph("📋 <b>Lista de Tareas del Alumno (Paso a Paso en 2 Pestañas):</b>", style_section_h))
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> inferior, pégalo en el chat y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b> En la respuesta de Gemini, haz clic en el botón <b>«Copiar código»</b> situado en la esquina superior del bloque.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b> En el mapa de la Sesión 37, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b> Pega el código con <b>Ctrl+V</b> (o Cmd+V) y haz clic en <b>«▶️ Ejecutar Creación»</b>. ¡Tu simulación 3D cobrará vida al instante!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Descubre la Demo Oficial Terminada:</b> Pulsa el botón <b>«🔬 Ver Piel Humana 3D ↗»</b> en el taller o mapa para comparar tu resultado con la versión oficial con audio.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#E11D48')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_table)
    story.append(Spacer(1, 3))

    # Recuadro Prompt Maestro
    story.append(Paragraph("🧠 <b>Prompt Maestro para Copiar y Pegar en Gemini:</b>", style_section_h))
    prompt_html = "<b>Copia exactamente este texto en Gemini:</b><br/><i>&quot;Genera el código de programación (HTML y JavaScript con Babylon.js) para construir un simulador interactivo 3D de la Piel Humana, Capas Tisulares y Termorregulación.<br/>Requisitos del código:<br/>1. Entrega el código en un único bloque autocontenido listo para copiar y probar.<br/>2. Enlaza Babylon.js desde CDN oficial y el modelo histológico tridimensional skin_b64.js.<br/>3. Renderiza en 3D un bloque cúbico con la Epidermis queratinizada, la Dermis papilar/reticular vascularizada y la Hipodermis adiposa con folículo piloso.<br/>4. Añade controles deslizantes para la Temperatura Ambiental (-10°C a +45°C), la Actividad Metabólica (W) y el Índice de Radiación UV.<br/>5. Programa botones interactivos para activar Vasodilatación, Vasoconstricción, Reflejo Pilomotor (Piel de gallina) y Tasa de Sudoración ecrina.<br/>6. Escribe exclusivamente el código sin textos adicionales.&quot;</i>"
    p_table = Table([[Paragraph(prompt_html, style_prompt)]], colWidths=[letter[0] - 72])
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#64748B')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(p_table)
    story.append(Spacer(1, 3))

    # Reto Extra
    story.append(Paragraph("🌟 <b>El Reto Extra (Para Alumnos Curiosos):</b>", style_section_h))
    story.append(Paragraph(
        "👉 <b>¡Pídele a Gemini que modifique tu código!</b> En la misma conversación dile: "
        "<i>«Añade al simulador una visualización termográfica por colores donde el tejido cambie de azul gélido (vasoconstricción a 0°C) a rojo ardiente (vasodilatación a 40°C) para disipar calor corporal».</i>. Vuelve a copiar el código, pégalo en tu Taller y ¡comprueba la evolución de tu modelo en directo!",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Apartado Técnico
    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos hiperrealistas y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de los datos científicos y repositorio oficial:</b> NIH Visible Human Project • Histología Dermatológica de Wheater & Gartner.<br/>"
        "• <b>Montaje en Babylon.js y fidelidad biológica:</b> El modelo 3D representa con rigor microanatómico los 5 estratos epidérmicos, las papilas dérmicas con asas capilares y la inervación simpática del músculo liso erector del pelo, aplicando las ecuaciones termodinámicas del balance térmico humano de Gagge y Stolwijk para el cálculo de la temperatura cutánea media. El modelo está codificado en Base64 (<i>skin_b64.js</i>) para carga instantánea 100% offline sin errores de red."
    )
    tech_table = Table([[Paragraph(tech_text, style_task)]], colWidths=[letter[0] - 72])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0FDF4')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#16A34A')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(tech_table)

    doc.build(story)
    if dest_path != LOCAL_BACKUP:
        try:
            import shutil
            os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
            shutil.copy2(dest_path, LOCAL_BACKUP)
        except Exception:
            pass
    print(f"✅ PDF COD-037 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try:
        build_cod_037_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-037: {e}")
        sys.exit(1)
