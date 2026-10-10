#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_004.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-004_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 04 del Curso de IA (Simulador 3D: Óptica y Anatomía Humana • Globo Ocular y Cristalino).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/04_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-004_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/04_COD-004_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf"

def build_cod_004_taller_3d_pdf(output_path=PDF_PATH):
    dest_path = output_path
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    except Exception:
        dest_path = LOCAL_BACKUP

    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    doc = SimpleDocTemplate(
        dest_path,
        pagesize=letter,
        rightMargin=40, leftMargin=40, topMargin=28, bottomMargin=26
    )
    styles = getSampleStyleSheet()
    
    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.5,
        textColor=colors.HexColor('#0284C7'), alignment=1, spaceAfter=2
    )
    style_block = ParagraphStyle(
        'BlockStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10.5,
        textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=6
    )
    style_title = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=12.5, leading=15.5,
        textColor=colors.HexColor('#0F172A'), spaceAfter=5
    )
    style_section_h = ParagraphStyle(
        'SectionHStyle', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=9.5, leading=12.5,
        textColor=colors.HexColor('#0369A1'), spaceBefore=4, spaceAfter=3
    )
    style_body = ParagraphStyle(
        'BodyStyle', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=8.5, leading=11.8,
        textColor=colors.HexColor('#1E293B'), spaceAfter=4
    )
    style_task = ParagraphStyle(
        'TaskStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.2, leading=11.2,
        textColor=colors.HexColor('#0F172A')
    )
    style_prompt = ParagraphStyle(
        'PromptStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8, leading=11,
        textColor=colors.HexColor('#0F172A')
    )

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & TALLER DE CÓDIGO CON GEMINI [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284C7'), spaceAfter=5))

    story.append(Paragraph("<b>[COD-004] Construye tu Simulador 3D del Globo Ocular Humano y Cristalino</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • Óptica y Anatomía de la Visión con Inteligencia Artificial:</b>", style_section_h))
    story.append(Paragraph(
        "El ojo humano es una de las mayores maravillas biológicas: una cámara fotográfica perfecta con autofoco natural.<br/>"
        "En este taller ordenarás a Gemini programar en Three.js un <b>simulador 3D interactivo del ojo humano</b> con física de luz en tiempo real.<br/>"
        "<b>Aprenderás sin programar:</b> pedirás el código a Gemini con el prompt maestro, lo probarás en el taller pulsando <b>«▶️ Ejecutar Creación»</b> y explorarás el <b>reflejo fotomotor</b> (la pupila contrayéndose con la luz para proteger la retina). ¡Y al pulsar el botón <b>«👁️ Ojo Humano 3D»</b> descubrirás la versión avanzada con vista de corte sagital de rayos X del cristalino, selector de color de iris y seguimiento de mirada!",
        style_body
    ))

    # Lista de Tareas (Checklist Guiado)
    story.append(Paragraph("📋 <b>Lista de Tareas del Alumno (Paso a Paso en 2 Pestañas):</b>", style_section_h))
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b><br/>"
                   "Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> del recuadro inferior, pégalo en el chat y pulsa Enviar. Gemini programará en segundos el simulador del ojo 3D.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b><br/>"
                   "En la respuesta de Gemini, haz clic en el botón <b>«Copiar código»</b> situado en la esquina superior derecha del bloque.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b><br/>"
                   "En el mapa del curso de la Sesión 04, pulsa el botón <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>. ¡Se ejecuta al instante en el navegador!", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b><br/>"
                   "Pega el código con <b>Ctrl+V</b> (o Cmd+V en Mac) en el recuadro izquierdo y pulsa <b>«▶️ Ejecutar Creación»</b>. ¡El globo ocular 3D responderá al ratón y a la luz!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Descubre la anatomía completa con «👁️ Ojo Humano 3D»:</b><br/>"
                   "Pulsa el botón oficial <b>«👁️ Ojo Humano 3D»</b>: ¡activa el modo linterna para ver el reflejo fotomotor (miosis y midriasis), cambia el color del iris y haz un corte de rayos X para ver el cristalino interior!", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 84])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0284C7')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_table)
    story.append(Spacer(1, 4))

    # Recuadro de Prompt Maestro
    story.append(Paragraph("🧠 <b>Prompt Maestro para Copiar y Pegar en Gemini:</b>", style_section_h))
    prompt_text = (
        "<b>Copia exactamente este texto en Gemini:</b><br/><br/>"
        "<i>\"Genera el código de programación completo en un único archivo (HTML, CSS y JavaScript con Three.js) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador interactivo 3D del Globo Ocular Humano y su Cristalino.<br/><br/>"
        "Requisitos del código:<br/>"
        "1. Entrega todo en un único bloque de código para que yo pulse directamente «Copiar código» y lo pegue con Ctrl+V en mi taller interactivo.<br/>"
        "2. Carga Three.js y OrbitControls desde CDN oficial (cdnjs) en la cabecera.<br/>"
        "3. Modela el globo ocular en 3D con materiales realistas: esclerótica blanca con sutiles microvasos, córnea transparente reflectante e iris con textura radial y pupila central.<br/>"
        "4. Añade un control deslizante (slider) de 'Intensidad de Luz' para simular el reflejo fotomotor pupilar: al aumentar la luz la pupila se contrae (miosis), y al disminuirla se dilata (midriasis) con animación suave.<br/>"
        "5. Incluye un botón para alternar 'Corte Sagital / Ver Cristalino' que vuelva translúcida la esclerótica y muestre en el interior la lente biconvexa del cristalino.<br/>"
        "6. Permite rotar el ojo en 3D libremente con el ratón mediante OrbitControls.<br/>"
        "7. Aplica un diseño moderno oscuro con una tarjeta informativa elegante que explique la función del iris, la córnea y el cristalino.<br/>"
        "8. Escribe exclusivamente el bloque de código sin explicaciones previas ni posteriores para que funcione de inmediato al pegarlo.\"</i>"
    )
    p_table = Table([[Paragraph(prompt_text, style_prompt)]], colWidths=[letter[0] - 84])
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#64748B')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(p_table)
    story.append(Spacer(1, 4))

    # Desafío Extra
    story.append(Paragraph("🌟 <b>El Reto Extra (Para Alumnos Curiosos):</b>", style_section_h))
    story.append(Paragraph(
        "👉 <b>¡Pídele a Gemini que personalice tu simulador!</b> En la misma conversación dile: "
        "<i>«Añade 3 botones para alternar el color del iris entre azul, verde y avellana»</i> o "
        "<i>«Haz que el ojo siga suavemente la posición del puntero del ratón por la pantalla simulando el seguimiento ocular humano»</i>. "
        "Vuelve a copiar el código con «Copiar código», pégalo en el Taller y observa el resultado en tiempo real.",
        style_body
    ))

    doc.build(story)
    print(f"✅ PDF COD-004 generado con éxito en: {dest_path}")
    if dest_path != output_path:
        print(f"ℹ️ Nota: Generado en respaldo local ({dest_path}) debido a permisos de sandbox.")

if __name__ == '__main__':
    try:
        build_cod_004_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-004: {e}")
        sys.exit(1)

