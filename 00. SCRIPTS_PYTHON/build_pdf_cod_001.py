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
        "En el ítem anterior (#09) has explorado el corazón humano latiendo en 3D con sonido real de fonendoscopio. "
        "¿Te gustaría ser tú quien construya y programe ese mismo simulador desde cero con Inteligencia Artificial? "
        "<b>No necesitas saber programar ni escribir código:</b> solo tienes que pedirle a Gemini lo que quieres mediante un prompt claro y probar tu creación en el <b>Taller de Pruebas del Curso</b> en tu navegador.",
        style_body
    ))

    # Lista de Tareas (Checklist Guiado)
    story.append(Paragraph("📋 <b>Lista de Tareas del Alumno (Paso a Paso en 2 Pestañas):</b>", style_section_h))
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el programa a Gemini (Pestaña 1):</b><br/>"
                   "Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> del recuadro inferior, pégalo en el chat y pulsa Enviar. Observa cómo la IA redacta en segundos todo el código HTML y 3D en Babylon.js.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b><br/>"
                   "En la respuesta de Gemini, ve a la esquina superior derecha del bloque de código y haz clic en el icono <b>«Copiar código»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b><br/>"
                   "Abre en tu navegador la pestaña del Taller de Pruebas: pulsa el botón <b>«🚀 Abrir Taller ↗»</b> del cuadro de mando (o abre <i>PROBADOR_CODIGO_IA.html</i>). ¡Cero archivos en el disco duro, todo funciona en la memoria!", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega y Ejecuta tu Creación:</b><br/>"
                   "En el Taller, pulsa el botón <b>«📋 Pegar de Gemini»</b> (o Ctrl+V) y a continuación pulsa el botón azul <b>«▶️ Ejecutar Creación»</b>. ¡Tu propio corazón 3D empezará a latir en pantalla al instante! Puedes girarlo en 360° con el ratón.", style_task)],
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
        "<i>\"Actúa como desarrollador web 3D especializado en educación interactiva.<br/>"
        "Crea un visor web en un único archivo HTML utilizando Babylon.js (vía CDN).<br/>"
        "Carga el modelo 3D anatómico del corazón desde la nube oficial de nuestro curso en esta URL:<br/>"
        "<b>https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/heart.glb</b><br/><br/>"
        "Requisitos obligatorios:<br/>"
        "1. Carga el modelo con BABYLON.SceneLoader.ImportMesh, céntralo y añade cámara orbital 360°.<br/>"
        "2. Fondo azul noche (#070b14) con iluminación médica de estudio.<br/>"
        "3. Panel flotante con deslizador de 40 a 160 BPM que haga latir el corazón rítmicamente.<br/>"
        "4. Incluye un botón para activar el sonido de fonendoscopio real usando este audio:<br/>"
        "<b>https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/heartbeat.mp3</b><br/>"
        "5. Entrega todo el código completo en un único bloque HTML listo para probar.\"</i>"
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
        "<i>«Ahora cambia las luces para que tenga un brillo verde futurista»</i> o "
        "<i>«Añade un contador en pantalla que cuente cuántas veces ha latido el corazón»</i>. "
        "Vuelve a copiar el código, pégalo en tu Taller y ¡mira cómo la IA adapta el programa a tus órdenes!",
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

