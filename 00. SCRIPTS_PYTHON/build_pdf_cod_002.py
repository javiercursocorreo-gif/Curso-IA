#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_002.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-002_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 02 del Curso de IA (Simulador del Latido Cardíaco Humano en 3D).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/02_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-002_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")

def build_cod_002_taller_3d_pdf(output_path=PDF_PATH):
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
        textColor=colors.HexColor('#E11D48'), alignment=1, spaceAfter=2
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
        textColor=colors.HexColor('#BE123C'), spaceBefore=4, spaceAfter=3
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
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#E11D48'), spaceAfter=5))

    story.append(Paragraph("<b>[COD-002] Construye tu Simulador del Latido Cardíaco Humano en 3D</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • De Espectador a Creador con IA:</b>", style_section_h))
    story.append(Paragraph(
        "En esta práctica vas a ordenar a la Inteligencia Artificial generar el código necesario para construir tu propio simulador 3D del corazón humano latiendo en tiempo real con su ciclo mecánico de sístole y diástole.<br/>"
        "<b>No necesitas saber programar:</b> pedirás el código a Gemini con el prompt maestro, lo copiarás en tu <b>Taller de Pruebas</b> y comprobarás cómo el corazón late ante tus ojos.",
        style_body
    ))

    # Lista de Tareas (Checklist Guiado)
    story.append(Paragraph("📋 <b>Lista de Tareas del Alumno (Paso a Paso en 2 Pestañas):</b>", style_section_h))
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b><br/>"
                   "Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> del recuadro inferior, pégalo en el chat y pulsa Enviar. Gemini redactará en segundos el bloque de código para tu corazón 3D.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b><br/>"
                   "En la respuesta de Gemini, haz clic en el icono o botón <b>«Copiar código»</b> situado en la esquina superior del bloque.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b><br/>"
                   "En el mapa del curso, pulsa el botón <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>. ¡Todo funciona en la memoria del navegador!", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b><br/>"
                   "En el Taller, pega el código pulsando <b>Ctrl+V</b> (o Cmd+V en Mac) en el cuadro de texto y haz clic en <b>«▶️ Ejecutar Creación»</b>. ¡El corazón 3D empezará a latir y podrás rotarlo en 360° con el ratón!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Prueba el simulador médico con audio real:</b><br/>"
                   "Para ver el modelo anatómico completo con sonido acústico de fonendoscopio y control de BPM, pulsa el botón <b>«🫀 Probar Corazón 3D + Audio»</b>.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 84])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFF1F2')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#E11D48')),
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
        "<i>\"Genera el código de programación (HTML y JavaScript con Babylon.js) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un corazón humano 3D latiendo.<br/><br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código para que yo pulse directamente «Copiar código» y lo pegue con Ctrl+V en mi simulador.<br/>"
        "2. Incluye en la cabecera los scripts del motor Babylon.js y el modelo del corazón:<br/>"
        "&lt;script src=&quot;https://cdn.babylonjs.com/babylon.js&quot;&gt;&lt;/script&gt;<br/>"
        "&lt;script src=&quot;https://cdn.babylonjs.com/loaders/babylonjs.loaders.min.js&quot;&gt;&lt;/script&gt;<br/>"
        "&lt;script src=&quot;https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/heart_b64.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Carga el modelo 3D con SceneLoader.AppendUsingAsync(window.HEART_GLB_B64, ...) y céntralo con cámara orbital 360° e iluminación sobre fondo azul oscuro (#070b14).<br/>"
        "4. En el bucle de animación antes de renderizar la escena, programa el latido cardíaco aplicando un escalado suave que simule la contracción de la sístole y la relajación de la diástole.<br/>"
        "5. Escribe exclusivamente el bloque de código para que al copiarlo a mi simulador genere el corazón latiendo.\"</i>"
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
        "👉 <b>¡Pídele a Gemini que modifique tu código!</b> En la misma conversación dile: "
        "<i>«Modifica el código para que el latido sea más rápido como si hiciéramos ejercicio (a 120 latidos por minuto)»</i> o "
        "<i>«Añade una luz roja brillante que se encienda cada vez que el corazón se contrae»</i>. "
        "Vuelve a copiar el código, pégalo en tu Taller y ¡mira cómo cambia tu corazón en directo!",
        style_body
    ))

    doc.build(story)
    print(f"✅ PDF COD-002 generado con éxito en: {output_path}")

if __name__ == '__main__':
    try:
        build_cod_002_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-002: {e}")
        sys.exit(1)

