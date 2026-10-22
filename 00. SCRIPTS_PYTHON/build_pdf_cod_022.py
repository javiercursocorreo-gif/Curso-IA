#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_022.py
Ficha Didáctica Oficial de 1 Página (Letter):
4. COD-022_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
Sesión 22: Esfera de Dyson & Megaestructuras Kardashev 3D
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/22_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-022_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/22_COD-022_Taller_Simulador_Esfera_Dyson_3D.pdf"

def build_cod_022_taller_3d_pdf(output_path=PDF_PATH):
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

    style_header = ParagraphStyle('HStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.0, textColor=colors.HexColor('#D97706'), alignment=1, spaceAfter=1)
    style_block = ParagraphStyle('BStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.8, textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=4)
    style_title = ParagraphStyle('TStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=11.6, leading=14.0, textColor=colors.HexColor('#0F172A'), spaceAfter=3)
    style_section_h = ParagraphStyle('SecStyle', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=8.8, leading=11.2, textColor=colors.HexColor('#B45309'), spaceBefore=3, spaceAfter=2)
    style_body = ParagraphStyle('BodyStyle', parent=styles['BodyText'], fontName='Helvetica', fontSize=7.8, leading=10.4, textColor=colors.HexColor('#1E293B'), spaceAfter=2)
    style_task = ParagraphStyle('TaskStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=7.6, leading=10.0, textColor=colors.HexColor('#0F172A'))
    style_prompt = ParagraphStyle('PromptStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=7.3, leading=9.7, textColor=colors.HexColor('#0F172A'))

    story = [
        Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header),
        Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & TALLER DE CÓDIGO CON GEMINI [COD]", style_block),
        HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#D97706'), spaceAfter=4),
        Paragraph("<b>[COD-022] Taller: Crea tu propio simulador 3D de la Esfera de Dyson & Enjambre Kardashev</b>", style_title),
        Paragraph("💡 <b>Misión Didáctica • Megaestructuras de Captura Solar y Búsqueda SETI con Gemini:</b>", style_section_h),
        Paragraph("En este taller ordenarás a Gemini modelar un simulador 3D de una <b>Esfera de Dyson</b>: un enjambre de satélites colectores solares a 1 Unidad Astronómica capaz de capturar los <b>3.828 × 10^26 Watts</b> emitidos por una estrella central (civilización Kardashev Tipo II). <b>No requieres saber programar:</b> copia el prompt maestro, pégalo en tu Taller y contempla la megaestructura con anillos orbitales y corona solar.", style_body)
    ]

    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> Abre Gemini (<i>gemini.google.com</i>). Copia el Prompt Maestro inferior, pégalo y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado:</b> Pulsa <b>«Copiar código»</b> en la esquina superior del bloque HTML de Gemini.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller de Pruebas (Pestaña 2):</b> En el mapa de la Sesión 22, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y ejecuta:</b> Pega el código con <b>Ctrl+V</b> y pulsa <b>«▶️ Ejecutar Creación»</b>. ¡Tu Esfera de Dyson 3D cobrará vida!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Prueba la Demo Oficial:</b> Pulsa <b>«☀️ Abrir Esfera de Dyson 3D ↗»</b> en el mapa para inspeccionar los rayos colectores y la firma infrarroja.", style_task)]
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFBEB')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#F59E0B')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5), ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7), ('RIGHTPADDING', (0,0), (-1,-1), 7)
    ]))
    story.append(t_table)
    story.append(Spacer(1, 3))

    story.append(Paragraph("🧠 <b>Prompt Maestro para Copiar y Pegar en Gemini:</b>", style_section_h))
    prompt_text = (
        "<b>Copia exactamente este texto en Gemini:</b><br/>"
        "<i>\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un visor interactivo 3D de la Esfera de Dyson y Enjambre Kardashev Tipo II.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.<br/>"
        "2. Incluye en la cabecera el script con los datos astrofísicos reales:<br/>"
        "&lt;script src=&quot;https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/dyson_sphere_b64.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Modela con Babylon.js una estrella central luminosa con partículas de corona solar y 4 anillos orbitales keplerianos con colectores hexagonales PBR.<br/>"
        "4. Incluye botones para activar/pausar el enjambre, rayos colectores de energía, comparar Kardashev Tipo I vs Tipo II y ver la firma infrarroja térmica a 300 K.<br/>"
        "5. Aplica un diseño en modo oscuro (#04060e) con acentos dorados (#f59e0b), tipografía grande (16-18px), balance energético en KPIs y síntesis de voz.<br/>"
        "6. Escribe exclusivamente el código funcional.\"</i>"
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
    story.append(Paragraph("👉 <b>¡Pídele a Gemini que modifique tu código!</b> En la misma conversación dile: <i>«Añade una estimación de cuántos hogares terrestres se podrían abastecer durante un año con 1 segundo de energía capturada»</i>. ¡Copia el código y compruébalo en tu Taller!", style_body))
    story.append(Spacer(1, 2))

    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de la teoría astrofísica (<i>Freeman Dyson / Escala Kardashev</i>):</b> La captura de 3.828 × 10^26 Watts a 1 UA se basa en la potencia total radiada por el Sol según la Ley de Stefan-Boltzmann.<br/>"
        "• <b>Montaje en Babylon.js:</b> Los parámetros se cargan desde <i>dyson_sphere_b64.js</i>. Babylon.js proyecta anillos keplerianos con cilindros hexagonales PBR contrarrotantes para evitar colisiones orbitales reales."
    )
    tech_table = Table([[Paragraph(tech_text, style_task)]], colWidths=[letter[0] - 72])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFBEB')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#D97706')),
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
    print(f"✅ PDF COD-022 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try: build_cod_022_taller_3d_pdf()
    except Exception as e: print(f"❌ Error al generar PDF COD-022: {e}"); sys.exit(1)

