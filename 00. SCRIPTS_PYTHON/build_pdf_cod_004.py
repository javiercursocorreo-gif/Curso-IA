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
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/04_COD-004_Taller_Simulador_Ojo_Humano_3D.pdf"

def build_cod_004_taller_3d_pdf(output_path=PDF_PATH):
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
        textColor=colors.HexColor('#0284C7'), alignment=1, spaceAfter=1
    )
    style_block = ParagraphStyle(
        'BlockStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.8,
        textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=4
    )
    style_title = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=11.8, leading=14.2,
        textColor=colors.HexColor('#0F172A'), spaceAfter=3
    )
    style_section_h = ParagraphStyle(
        'SectionHStyle', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=8.8, leading=11.2,
        textColor=colors.HexColor('#0369A1'), spaceBefore=3, spaceAfter=2
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
        fontName='Helvetica', fontSize=7.5, leading=9.9,
        textColor=colors.HexColor('#0F172A')
    )

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & TALLER DE CÓDIGO CON GEMINI [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#0284C7'), spaceAfter=4))

    story.append(Paragraph("<b>[COD-004] Taller: Crea tu propio simulador del ojo humano</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • Óptica y Anatomía de la Visión con Inteligencia Artificial:</b>", style_section_h))
    story.append(Paragraph(
        "En este taller ordenarás a Gemini programar en Three.js un <b>simulador 3D interactivo del ojo humano</b> con física de luz en tiempo real. "
        "<b>Sin saber programar:</b> pedirás el código a Gemini con el prompt maestro, lo probarás en el taller pulsando <b>«▶️ Ejecutar Creación»</b> y explorarás el <b>reflejo fotomotor</b> (la pupila contrayéndose con la luz). ¡Y al pulsar el botón <b>«👁️ Ojo Humano 3D»</b> (o la Demo del mapa) descubrirás la versión completa con guía lateral de los 3 botones, colores humanos reales del iris y corte sagital del cristalino!",
        style_body
    ))

    # Apartado Técnico: Origen de las Texturas Hiperrealistas y Montaje del Objeto 3D
    story.append(Paragraph("🔬 <b>¿De dónde proceden las texturas hiperrealistas y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de la referencia anatómica y textura hiperrealista del iris:</b> Basado en las proporciones del <b>Visible Human Project del NIH 3D (National Institutes of Health, EE. UU., <i>eye.glb</i>)</b> y en fotografías clínicas de lámpara de hendidura oftalmológica. A diferencia de una foto estática pegada (que se deformaría al contraer la pupila), la textura hiperrealista del iris se sintetiza dinámicamente en un <b>lienzo biomédico de alta resolución (<i>Canvas 2D de 1024×1024 px</i>)</b> con pigmentación humana real de melanina/lipocromo (castaño, azul grisáceo, verde oliva y avellana), <b>64 criptas estromales de Fuchs</b>, <b>720 fibras trabeculares curvas de colágeno</b> y capilares episclerales.<br/>"
        "• <b>Cómo se ha montado el objeto en la Demo y en el Taller:</b> En el motor <b>Three.js (WebGL PBR)</b> se ensamblan 4 piezas concéntricas: <b>(1)</b> la esfera esclero-iridiana con corrección matemática de proyección equirectangular 2:1 (para que el iris sea 100% redondo y sin aberración ovalada) y relieve <i>bumpMap</i>; <b>(2)</b> el domo corneal transparente orientado en <i>+Z</i> con un único foco de linterna oftálmica; <b>(3)</b> la lente biconvexa interna del <b>cristalino</b> (visible al activar el botón de Corte Sagital) y <b>(4)</b> el nervio óptico posterior."
    )
    tech_table = Table([[Paragraph(tech_text, style_task)]], colWidths=[letter[0] - 72])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ECFDF5')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#059669')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(tech_table)
    story.append(Spacer(1, 3))

    # Lista de Tareas (Checklist Guiado)
    story.append(Paragraph("📋 <b>Lista de Tareas del Alumno (Paso a Paso en 2 Pestañas):</b>", style_section_h))
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> "
                   "Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> inferior, pégalo en el chat y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b> "
                   "En la respuesta de Gemini, haz clic en el botón <b>«Copiar código»</b> situado en la esquina superior derecha del bloque.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b> "
                   "En el mapa de la Sesión 04, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b> "
                   "Pega el código con <b>Ctrl+V</b> (o Cmd+V en Mac) en el cuadro izquierdo y pulsa <b>«▶️ Ejecutar Creación»</b> para probar tu globo ocular 3D.", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Explora la Demo avanzada («👁️ Ojo Humano 3D»):</b> "
                   "Pulsa <b>«👁️ Ojo Humano 3D»</b> en el taller (o <b>«👁️ Ver Simulador Ojo Humano 3D ↗»</b> en el mapa) con cuadro explicativo izquierdo, linterna y corte sagital.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0284C7')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_table)
    story.append(Spacer(1, 3))

    # Recuadro de Prompt Maestro
    story.append(Paragraph("🧠 <b>Prompt Maestro para Copiar y Pegar en Gemini:</b>", style_section_h))
    prompt_text = (
        "<b>Copia exactamente este texto en Gemini:</b><br/>"
        "<i>\"Genera el código de programación completo en un único archivo (HTML, CSS y JavaScript con Three.js) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador interactivo 3D del Globo Ocular Humano y su Cristalino.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega todo en un único bloque de código para que yo pulse directamente «Copiar código» y lo pegue con Ctrl+V en mi taller interactivo.<br/>"
        "2. Carga Three.js y OrbitControls desde CDN oficial (cdnjs) en la cabecera.<br/>"
        "3. Modela el globo ocular en 3D con materiales realistas: esclerótica blanca con microvasos, córnea transparente e iris circular con textura estromal y pupila central.<br/>"
        "4. Añade un control deslizante (slider) de 'Intensidad de Luz' para simular el reflejo fotomotor pupilar: al subir la luz la pupila se contrae (miosis), y al bajarla se dilata (midriasis).<br/>"
        "5. Incluye un botón para alternar 'Corte Sagital / Ver Cristalino' que vuelva translúcida la esclerótica y muestre en el interior la lente biconvexa del cristalino.<br/>"
        "6. Permite rotar el ojo en 3D libremente con el ratón mediante OrbitControls y aplica un diseño moderno oscuro con tarjeta explicativa.<br/>"
        "7. Escribe exclusivamente el bloque de código sin explicaciones previas ni posteriores para que funcione de inmediato al pegarlo.\"</i>"
    )
    p_table = Table([[Paragraph(prompt_text, style_prompt)]], colWidths=[letter[0] - 72])
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

    # Desafío Extra
    story.append(Paragraph("🌟 <b>El Reto Extra (Para Alumnos Curiosos):</b>", style_section_h))
    story.append(Paragraph(
        "👉 <b>¡Pídele a Gemini que personalice tu simulador!</b> En la misma conversación dile: "
        "<i>«Añade botones para cambiar el color del iris entre castaño, azul grisáceo, verde oliva y avellana»</i> o "
        "<i>«Haz que el ojo siga suavemente la posición del ratón cuando pase por encima del visor»</i>. "
        "Copia el código actualizado, pégalo en el Taller y observa el resultado en tiempo real.",
        style_body
    ))

    doc.build(story)
    if dest_path != LOCAL_BACKUP:
        try:
            import shutil
            os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
            shutil.copy2(dest_path, LOCAL_BACKUP)
        except Exception:
            pass
    print(f"✅ PDF COD-004 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try:
        build_cod_004_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-004: {e}")
        sys.exit(1)
