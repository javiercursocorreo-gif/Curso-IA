#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_001.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-001_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 01 del Curso de IA.
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/01_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-001_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")

def build_cod_001_taller_3d_pdf(output_path=PDF_PATH):
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
        rightMargin=42, leftMargin=42, topMargin=34, bottomMargin=32
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

    story.append(Paragraph("<b>[COD-001] Taller Práctico: ¡Construye tu Propio Simulador 3D con Gemini!</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • De Espectador a Creador con IA:</b>", style_section_h))
    story.append(Paragraph(
        "En el ítem anterior (#09) has observado el corazón humano latiendo en 3D con sonido real de fonendoscopio. "
        "Ahora vas a ser tú quien ordene a la Inteligencia Artificial generar el código necesario para construir ese mismo corazón. "
        "<b>No necesitas saber programar:</b> pedirás el código a Gemini con el prompt maestro, lo copiarás en tu <b>Taller de Pruebas</b> y comprobarás cómo cobra vida en tu pantalla.",
        style_body
    ))

    # Lista de Tareas (Checklist Guiado)
    story.append(Paragraph("📋 <b>Lista de Tareas del Alumno (Paso a Paso en 2 Pestañas):</b>", style_section_h))
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b><br/>"
                   "Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> del recuadro inferior, pégalo en el chat y pulsa Enviar. Gemini redactará en segundos el bloque de código para tu simulador.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b><br/>"
                   "En la respuesta de Gemini, haz clic en el icono o botón <b>«Copiar código»</b> situado en la esquina superior del bloque.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b><br/>"
                   "En el mapa del curso, pulsa el botón <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b> (o abre <i>PROBADOR_CODIGO_IA.html</i>). ¡Todo funciona en la memoria del navegador!", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega el código y pulsa «Ejecutar Creación»:</b><br/>"
                   "En el Taller, pulsa el botón <b>«📋 Pegar de Gemini»</b> (o Ctrl+V) y haz clic en <b>«▶️ Ejecutar Creación»</b>. ¡El simulador generará tu corazón 3D latiendo con sonido y podrás rotarlo en 360°!", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 84])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0284C7')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_table)
    story.append(Spacer(1, 4))

    # Recuadro de Prompt Maestro
    story.append(Paragraph("🧠 <b>Prompt Maestro para Copiar y Pegar en Gemini:</b>", style_section_h))
    prompt_text = (
        "<b>Copia exactamente este texto en Gemini:</b><br/><br/>"
        "<i>\"Genera el código de programación (HTML y JavaScript con Babylon.js) que voy a copiar y pegar en el Taller de Pruebas de mi curso para que genere un corazón humano 3D latiendo.<br/><br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código para que yo pulse directamente «Copiar código» y lo pegue en mi simulador.<br/>"
        "2. El código debe cargar la geometría 3D del corazón de nuestro curso desde esta dirección web:<br/>"
        "<b>https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/heart.glb</b><br/>"
        "3. Centra el modelo con cámara orbital 360° para rotarlo con el ratón y fondo azul noche (#070b14).<br/>"
        "4. Incluye un control de ritmo de 40 a 160 BPM que haga latir el corazón rítmicamente.<br/>"
        "5. Conecta el sonido de fonendoscopio real sincronizado desde:<br/>"
        "<b>https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/heartbeat.mp3</b><br/>"
        "6. Escribe exclusivamente el código para que al copiarlo a mi simulador genere el corazón interactivo.\"</i>"
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
        "<i>«Modifica el código para que las luces tengan un brillo verde futurista»</i> o "
        "<i>«Añade un contador en pantalla que cuente cuántas veces ha latido el corazón»</i>. "
        "Vuelve a copiar el código, pégalo en tu Taller y ¡mira cómo cambia tu corazón en directo!",
        style_body
    ))

    doc.build(story)
    print(f"✅ PDF COD-001 generado con éxito en: {output_path}")

if __name__ == '__main__':
    try:
        build_cod_001_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-001: {e}")
        sys.exit(1)

