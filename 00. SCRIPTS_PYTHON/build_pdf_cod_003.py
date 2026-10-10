#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_003.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-003_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 03 del Curso de IA (Simulador Arqueológico de Pompeya: Ruinas vs. Reconstrucción Romana).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/03_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-003_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")

def build_cod_003_taller_3d_pdf(output_path=PDF_PATH):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    if os.path.exists(output_path):
        try: os.remove(output_path)
        except Exception: pass

    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=40, leftMargin=40, topMargin=28, bottomMargin=26
    )
    styles = getSampleStyleSheet()
    
    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.5,
        textColor=colors.HexColor('#D97706'), alignment=1, spaceAfter=2
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
        textColor=colors.HexColor('#B45309'), spaceBefore=4, spaceAfter=3
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
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#D97706'), spaceAfter=5))

    story.append(Paragraph("<b>[COD-003] Construye tu Simulador de Viaje en el Tiempo a Pompeya</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • Arqueología Digital con Inteligencia Artificial:</b>", style_section_h))
    story.append(Paragraph(
        "Tras explorar el corazón y los pulmones en las sesiones anteriores, cambiamos de temática hacia los grandes hitos de la civilización: <b>la arqueología digital</b>.<br/>"
        "En este taller ordenarás a Gemini crear un <b>visor interactivo de viaje en el tiempo</b> para deslizar un cursor entre las ruinas actuales de Pompeya y su reconstrucción romana en el año 79 d.C.<br/>"
        "<b>No necesitas conocimientos de programación:</b> le pedirás el código a Gemini con el prompt maestro, lo probarás en tu <b>Taller de Pruebas</b> y contemplarás el templo romano ante tus ojos.",
        style_body
    ))

    # Lista de Tareas (Checklist Guiado)
    story.append(Paragraph("📋 <b>Lista de Tareas del Alumno (Paso a Paso en 2 Pestañas):</b>", style_section_h))
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b><br/>"
                   "Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> del recuadro inferior, pégalo en el chat y pulsa Enviar. Gemini redactará en segundos el código del visor arqueológico interactivo.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b><br/>"
                   "En la respuesta de Gemini, haz clic en el icono o botón <b>«Copiar código»</b> situado en la esquina superior derecha del bloque.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b><br/>"
                   "En el mapa del curso de la Sesión 03, pulsa el botón <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>. ¡Se ejecuta al instante en el navegador!", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b><br/>"
                   "Pega el código pulsando <b>Ctrl+V</b> (o Cmd+V en Mac) en el recuadro izquierdo y pulsa <b>«▶️ Ejecutar Creación»</b>. ¡Arrastra el control deslizante central para viajar 2.000 años atrás en el tiempo!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Comprueba el simulador arqueológico completo:</b><br/>"
                   "Para ver el modelo oficial con fotos reales en alta resolución del archivo CyArk y filtros de piedra antigua, pulsa el botón <b>«🏛️ Ver Tesoro Arqueológico 3D ↗»</b> en el mapa de la clase.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 84])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFBEB')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#D97706')),
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
        "<i>\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un visor interactivo de Pompeya (Antes y Después).<br/><br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código para que yo pulse directamente «Copiar código» y lo pegue con Ctrl+V en mi simulador.<br/>"
        "2. Incluye en la cabecera el script con las fotografías reales del archivo arqueológico:<br/>"
        "&lt;script src=&quot;https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/pompeii_photos_b64.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Crea un contenedor visual con dos capas fotográficas superpuestas que utilicen window.POMPEII_RUINS_B64 (ruinas actuales) y window.POMPEII_RECON_B64 (templo reconstruido).<br/>"
        "4. Programa una barra divisoria deslizante interactiva con ratón o slider que permita al usuario comparar visualmente las columnas en ruinas con su aspecto monumental romano original.<br/>"
        "5. Aplica un diseño moderno oscuro con tipografía clara y un indicador que muestre 'Año 79 d.C. vs. Año 2026'.<br/>"
        "6. Escribe exclusivamente el bloque de código para que al copiarlo a mi simulador funcione inmediatamente.\"</i>"
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
        "👉 <b>¡Pídele a Gemini que modifique tu simulador!</b> En la misma conversación de chat dile: "
        "<i>«Añade un botón que aplique un filtro de color sepia antiguo simulando una fotografía de expedición del siglo XIX»</i> o "
        "<i>«Añade una etiqueta que explique qué templo romano estamos observando al pulsar un botón»</i>. "
        "Vuelve a copiar el código resultante, pégalo en el Taller y comprueba las novedades al instante.",
        style_body
    ))

    doc.build(story)
    print(f"✅ PDF COD-003 generado con éxito en: {output_path}")

if __name__ == '__main__':
    try:
        build_cod_003_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-003: {e}")
        sys.exit(1)

