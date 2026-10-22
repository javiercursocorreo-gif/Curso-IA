#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_018.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-018_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 18 del Curso de IA (Simulador 3D: Neurona Piramidal Cortical y Sinapsis • NeuroMorpho.Org y NIH).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/18_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-018_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/18_COD-018_Taller_Simulador_Neurona_3D.pdf"

def build_cod_018_taller_3d_pdf(output_path=PDF_PATH):
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
        fontName='Helvetica', fontSize=7.4, leading=9.8,
        textColor=colors.HexColor('#0F172A')
    )

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & TALLER DE CÓDIGO CON GEMINI [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#0284C7'), spaceAfter=4))

    story.append(Paragraph("<b>[COD-018] Taller: Crea tu propio simulador 3D de la Neurona Piramidal</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • Neurobiología, Sinapsis Eléctrica y Neuroplasticidad con Gemini:</b>", style_section_h))
    story.append(Paragraph(
        "En este taller ordenarás a Gemini crear un simulador 3D interactivo de una <b>Neurona Piramidal Cortical</b> y su mecanismo de transmisión sináptica. "
        "<b>No requieres saber programar:</b> pegarás el prompt maestro en Gemini, copiarás el código en tu <b>Taller de Pruebas</b> y contemplarás la unidad viva del pensamiento: soma piramidal, dendritas basales y apicales con espinas, axón mielinizado con nódulos de Ranvier y disparo del impulso eléctrico a 120 m/s.",
        style_body
    ))

    # Lista de Tareas
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> "
                   "Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> inferior, pégalo en el chat y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b> "
                   "En la respuesta de Gemini, pulsa <b>«Copiar código»</b> en la esquina superior del bloque.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b> "
                   "En el mapa de la Sesión 18, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b> "
                   "Pega el código con <b>Ctrl+V</b> (o Cmd+V) y pulsa <b>«▶️ Ejecutar Creación»</b>. ¡Tu neurona se iluminará con impulsos eléctricos!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Descubre la Demo cerebral completa:</b> "
                   "Pulsa <b>«🧠 Neurona Piramidal 3D»</b> en el taller (o <b>«🧠 Abrir Neurona 3D ↗»</b> en el mapa) para probar el potencial de acción.", style_task)],
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
        "<i>\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador 3D de una Neurona Piramidal de la corteza cerebral humana con datos de NeuroMorpho.Org y el NIH.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.<br/>"
        "2. Incluye en la cabecera el script con los datos morfológicos reales:<br/>"
        "&lt;script src=&quot;https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/neuron_b64.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Modela con Babylon.js el cuerpo piramidal (soma), el árbol dendrítico apical ramificado, las dendritas basales, el axón con vainas de mielina doradas y nódulos de Ranvier.<br/>"
        "4. Incluye un botón para simular el disparo de un potencial de acción que recorra el axón como un pulso bioluminiscente cian a 120 m/s.<br/>"
        "5. Aplica un diseño neurobiológico en modo oscuro (#030712) con tipografía accesible y contrastes cuidados.<br/>"
        "6. Escribe exclusivamente el bloque de código funcional.\"</i>"
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
        "👉 <b>¡Pídele a Gemini que modifique tu código!</b> En la misma conversación dile: "
        "<i>«Añade una tarjeta que explique cómo el aprendizaje continuo y la lectura crean nuevas sinapsis (neuroplasticidad) a cualquier edad»</i> o "
        "<i>«Coloca una vista ampliada de la hendidura sináptica liberando neurotransmisores»</i>. "
        "Vuelve a copiar el código, pégalo en tu Taller y ¡mira a tu cerebro en acción!",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Apartado Técnico al final
    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos hiperrealistas y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de las reconstrucciones neuronales (<i>NeuroMorpho.Org / NIH Human Brain</i>):</b> La morfometría celular tridimensional procede de reconstrucciones de <b>microscopía confocal y trazado de neuronas piramidades de la capa V del neocórtex humano</b>.<br/>"
        "• <b>Cómo se ha montado el objeto en la Demo y en el Taller:</b> Los datos anatómicos se almacenan en <i>neuron_b64.js</i>. Babylon.js utiliza tubos extruidos y shaders emisivos que transmiten ondas luminosas continuas a lo largo de la trayectoria axonal."
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

    doc.build(story)
    if dest_path != LOCAL_BACKUP:
        try:
            import shutil
            os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
            shutil.copy2(dest_path, LOCAL_BACKUP)
        except Exception:
            pass
    print(f"✅ PDF COD-018 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try:
        build_cod_018_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-018: {e}")
        sys.exit(1)

