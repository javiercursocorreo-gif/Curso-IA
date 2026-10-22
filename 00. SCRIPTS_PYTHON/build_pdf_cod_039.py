#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_039.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-039_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 39 del Curso de IA (Taller: Crea tu propio simulador de iridiscencia óptica y nanocristales).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/39_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-039_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/039_COD-039_Taller_Simulador_3D.pdf"

def build_cod_039_taller_3d_pdf(output_path=PDF_PATH):
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
        textColor=colors.HexColor('#0891B2'), alignment=1, spaceAfter=1
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
        textColor=colors.HexColor('#0891B2'), spaceBefore=3, spaceAfter=2
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
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#0891B2'), spaceAfter=4))

    story.append(Paragraph("<b>[COD-039] Taller: Crea tu propio simulador de iridiscencia óptica y nanocristales</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • De Espectador a Creador con IA:</b>", style_section_h))
    story.append(Paragraph("En esta sesión ordenarás a Gemini construir en Babylon.js el simulador óptico de la mariposa Morpho peleides en 3D: desde la silueta alar macroscópica hasta la microestructura SEM a 20.000 aumentos de sus nano-lamelas en árbol de Navidad. Comprobarás que el azul cobalto brillante no tiene una sola molécula de pigmento: es interferencia constructiva pura de la Ley de Bragg.", style_body))

    # Lista de Tareas
    story.append(Paragraph("📋 <b>Lista de Tareas del Alumno (Paso a Paso en 2 Pestañas):</b>", style_section_h))
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> inferior, pégalo en el chat y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b> En la respuesta de Gemini, haz clic en el botón <b>«Copiar código»</b> situado en la esquina superior del bloque.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b> En el mapa de la Sesión 39, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b> Pega el código con <b>Ctrl+V</b> (o Cmd+V) y haz clic en <b>«▶️ Ejecutar Creación»</b>. ¡Tu simulación 3D cobrará vida al instante!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Descubre la Demo Oficial Terminada:</b> Pulsa el botón <b>«🦋 Ver Mariposa Morpho 3D ↗»</b> en el taller o mapa para comparar tu resultado con la versión oficial con audio.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0891B2')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_table)
    story.append(Spacer(1, 3))

    # Recuadro Prompt Maestro
    story.append(Paragraph("🧠 <b>Prompt Maestro para Copiar y Pegar en Gemini:</b>", style_section_h))
    prompt_html = "<b>Copia exactamente este texto en Gemini:</b><br/><i>&quot;Genera el código de programación (HTML y JavaScript con Babylon.js) para construir un simulador 3D del Mimetismo Óptico, Nanocristales e Iridiscencia de la Mariposa Morpho.<br/>Requisitos del código:<br/>1. Entrega el programa completo en un bloque único de código para copiarlo y ejecutarlo en el taller.<br/>2. Carga Babylon.js desde CDN oficial y el archivo tridimensional de nanocristales iridescence_b64.js.<br/>3. Renderiza en 3D la mariposa Morpho y un corte microscópico de sus nano-lamelas escalonadas en árbol de Navidad con material PBR iridiscente.<br/>4. Añade un control deslizante de Ángulo de Incidencia de la Luz (0° a 80°) y un selector del Índice de Refracción del Medio circundante n (aire n=1.00, agua n=1.33, acetona n=1.36).<br/>5. Muestra en tiempo real la longitud de onda reflejada pico (nm) y cómo el ala pasa de azul cobalto a verde o pierde el color al sumergirse en solventes.<br/>6. Escribe exclusivamente el bloque de código.&quot;</i>"
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
        "<i>«Añade un botón de Inmersión en Solvente Líquido que llene los huecos de aire de las nano-lamelas con acetona, alterando el índice de refracción y apagando instantáneamente el color azul del ala ante los ojos del alumno».</i>. Vuelve a copiar el código, pégalo en tu Taller y ¡comprueba la evolución de tu modelo en directo!",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Apartado Técnico
    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos hiperrealistas y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de los datos científicos y repositorio oficial:</b> Natural History Museum London • Microscopía Electrónica de Barrido (SEM 20.000x) • Ley Óptica de Bragg-Snell.<br/>"
        "• <b>Montaje en Babylon.js y fidelidad biológica:</b> La óptica estructural modela la interferencia en multicapas dieléctricas mediante la ecuación de Bragg-Snell (mλ = 2d √(n² - sin²θ)), demostrando cómo las crestas de cutícula separadas a d ≈ 205 nm producen interferencia constructiva en λ = 450 nm (azul visible) sin requerir ningún cromóforo químico. El modelo está codificado en Base64 (<i>iridescence_b64.js</i>) para carga instantánea 100% offline sin errores de red."
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
    print(f"✅ PDF COD-039 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try:
        build_cod_039_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-039: {e}")
        sys.exit(1)
