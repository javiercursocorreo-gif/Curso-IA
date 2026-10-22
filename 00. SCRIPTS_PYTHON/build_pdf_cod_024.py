#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_024.py
Ficha Didáctica Oficial de 1 Página (Letter):
4. COD-024_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
Sesión 24: Las 11 Dimensiones del Universo & Calabi-Yau 3D (Teoría M y Supercuerdas)
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/24_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-024_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/24_COD-024_Taller_Simulador_11_Dimensiones_3D.pdf"

def build_cod_024_taller_3d_pdf(output_path=PDF_PATH):
    dest_path = output_path
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "wb") as _: pass
    except Exception:
        dest_path = LOCAL_BACKUP
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    doc = SimpleDocTemplate(dest_path, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=22, bottomMargin=20)
    styles = getSampleStyleSheet()

    style_header = ParagraphStyle('HStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.0, textColor=colors.HexColor('#7C3AED'), alignment=1, spaceAfter=1)
    style_block = ParagraphStyle('BStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.8, textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=4)
    style_title = ParagraphStyle('TStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=11.6, leading=14.0, textColor=colors.HexColor('#0F172A'), spaceAfter=3)
    style_section_h = ParagraphStyle('SecStyle', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=8.8, leading=11.2, textColor=colors.HexColor('#6D28D9'), spaceBefore=3, spaceAfter=2)
    style_body = ParagraphStyle('BodyStyle', parent=styles['BodyText'], fontName='Helvetica', fontSize=7.8, leading=10.4, textColor=colors.HexColor('#1E293B'), spaceAfter=2)
    style_task = ParagraphStyle('TaskStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=7.6, leading=10.0, textColor=colors.HexColor('#0F172A'))
    style_prompt = ParagraphStyle('PromptStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=7.3, leading=9.7, textColor=colors.HexColor('#0F172A'))

    story = [
        Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header),
        Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & TALLER DE CÓDIGO CON GEMINI [COD]", style_block),
        HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#7C3AED'), spaceAfter=4),
        Paragraph("<b>[COD-024] Taller: Crea tu propio simulador 3D de las 11 Dimensiones del Universo</b>", style_title),
        Paragraph("💡 <b>Misión Didáctica • Variedad de Calabi-Yau, Supercuerdas y Teoría M con Gemini:</b>", style_section_h),
        Paragraph("En este taller ordenarás a Gemini construir un simulador hiperdimensional en 3D de la <b>Variedad de Calabi-Yau</b> y las <b>11 dimensiones de la Teoría M</b> (Edward Witten, CERN). Comprenderás cómo 6 dimensiones adicionales microscópicas enrolladas en la escala de Planck (10^-35 m) hacen vibrar las cuerdas que dan origen a todas las fuerzas y partículas del cosmos. <b>No requieres saber programar:</b> copia el prompt y ejecútalo.", style_body)
    ]

    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> Abre Gemini (<i>gemini.google.com</i>). Copia el Prompt Maestro inferior, pégalo y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado:</b> Pulsa <b>«Copiar código»</b> en la esquina superior del bloque HTML de Gemini.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller de Pruebas (Pestaña 2):</b> En el mapa de la Sesión 24, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y ejecuta:</b> Pega el código con <b>Ctrl+V</b> y pulsa <b>«▶️ Ejecutar Creación»</b>. ¡La superficie hiperdimensional girará en 4D!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Prueba la Demo Oficial:</b> Pulsa <b>«🌀 Abrir 11 Dimensiones 3D ↗»</b> en el mapa para explorar las cuerdas vibrantes y la holonomía SU(3).", style_task)]
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F5F3FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#A855F7')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5), ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7), ('RIGHTPADDING', (0,0), (-1,-1), 7)
    ]))
    story.append(t_table)
    story.append(Spacer(1, 3))

    story.append(Paragraph("🧠 <b>Prompt Maestro para Copiar y Pegar en Gemini:</b>", style_section_h))
    prompt_text = (
        "<b>Copia exactamente este texto en Gemini:</b><br/>"
        "<i>\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un visor interactivo 3D de las 11 Dimensiones del Universo y la Variedad de Calabi-Yau con datos de física teórica del CERN.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.<br/>"
        "2. Incluye en la cabecera el script con los datos dimensionales reales:<br/>"
        "&lt;script src=&quot;https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/dimensions11_calabiyau_b64.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Modela con Babylon.js una sección tridimensional paramétrica de la Variedad de Calabi-Yau mediante un toroide cruzado con material PBR violeta semitransparente (#c084fc), giro hiperdimensional en 4D y 12 supercuerdas microscópicas oscilantes.<br/>"
        "4. Incluye botones para alternar entre la vista 3D Macroscópica, 4D Espacio-Tiempo, 6D Calabi-Yau y 11D Teoría M.<br/>"
        "5. Aplica un diseño en modo oscuro (#03040c) con tipografía grande (16-18px), datos matemáticos en KPIs (SU(3), Euler -6) y síntesis de voz.<br/>"
        "6. Escribe exclusivamente el código sin texto explicativo.\"</i>"
    )
    p_table = Table([[Paragraph(prompt_text, style_prompt)]], colWidths=[letter[0] - 72])
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#64748B')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5), ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7), ('RIGHTPADDING', (0,0), (-1,-1), 7)
    ]))
    story.append(p_table)
    story.append(Spacer(1, 3))

    story.append(Paragraph("🌟 <b>El Reto Extra (Para Alumnos Curiosos):</b>", style_section_h))
    story.append(Paragraph("👉 <b>¡Pídele a Gemini que modifique tu código!</b> En la misma conversación dile: <i>«Añade una metáfora explicativa sencilla: ¿cómo se enrolla una manguera de jardín vista desde muy lejos (parece una línea 1D) versus vista de cerca (es un tubo 3D)?»</i>. ¡Copia el código y compruébalo en tu Taller!", style_body))
    story.append(Spacer(1, 2))

    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de la geometría compleja (<i>CERN / Edward Witten</i>):</b> Las variedades de Calabi-Yau son espacios compactos con curvatura de Ricci plana y holonomía SU(3) que preservan la supersimetría en 4D.<br/>"
        "• <b>Montaje en Babylon.js:</b> Los parámetros se extraen de <i>dimensions11_calabiyau_b64.js</i>. Babylon.js genera una cinta tridimensional continua (MeshBuilder.CreateRibbon) mediante proyecciones paramétricas de funciones trigonométricas armónicas compuestas."
    )
    tech_table = Table([[Paragraph(tech_text, style_task)]], colWidths=[letter[0] - 72])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F5F3FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#7C3AED')),
        ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 7), ('RIGHTPADDING', (0,0), (-1,-1), 7)
    ]))
    story.append(tech_table)

    doc.build(story)
    if dest_path != LOCAL_BACKUP:
        try:
            import shutil
            os.makedirs(os.path.dirname(LOCAL_BACKUP), exist_ok=True)
            shutil.copy2(dest_path, LOCAL_BACKUP)
        except Exception: pass
    print(f"✅ PDF COD-024 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try: build_cod_024_taller_3d_pdf()
    except Exception as e: print(f"❌ Error al generar PDF COD-024: {e}"); sys.exit(1)

