#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_016.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-016_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 16 del Curso de IA (Simulador 3D: Hígado Humano y Sistema Hepatobiliar • NIH 3D Print Exchange).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/16_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-016_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/16_COD-016_Taller_Simulador_Higado_3D.pdf"

def build_cod_016_taller_3d_pdf(output_path=PDF_PATH):
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
        textColor=colors.HexColor('#BE123C'), alignment=1, spaceAfter=1
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
        textColor=colors.HexColor('#9F1239'), spaceBefore=3, spaceAfter=2
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
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#BE123C'), spaceAfter=4))

    story.append(Paragraph("<b>[COD-016] Taller: Crea tu propio simulador 3D del Hígado Humano</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • Anatomía Quirúrgica, Sistema Hepatobiliar y Salud con Gemini:</b>", style_section_h))
    story.append(Paragraph(
        "En este taller pedirás a Gemini desarrollar un simulador 3D clínico del <b>Hígado Humano</b> y el <b>Sistema Hepatobiliar</b>. "
        "<b>No requieres saber programar:</b> copiarás el prompt maestro en Gemini, pegarás el código generado en tu <b>Taller de Pruebas</b> y contemplarás el laboratorio químico del organismo: lóbulo derecho e izquierdo, vesícula biliar, árbol biliar verde, vena porta y vena cava inferior.",
        style_body
    ))

    # Lista de Tareas
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> "
                   "Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> inferior, pégalo en el chat y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b> "
                   "En la respuesta de Gemini, pulsa <b>«Copiar código»</b> en la esquina superior del bloque.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b> "
                   "En el mapa de la Sesión 16, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b> "
                   "Pega el código con <b>Ctrl+V</b> (o Cmd+V) y pulsa <b>«▶️ Ejecutar Creación»</b>. ¡Tu hígado 3D se mostrará con controles interactivos!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Descubre la Demo quirúrgica completa:</b> "
                   "Pulsa <b>«🩺 Hígado & Vía Biliar 3D»</b> en el taller (o <b>«🩺 Abrir Simulador Hígado ↗»</b> en el mapa) para probar los 8 segmentos de Couinaud.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFF1F2')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#F43F5E')),
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
        "<i>\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador 3D del Hígado Humano y el Sistema Hepatobiliar con datos médicos del NIH 3D Print Exchange.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.<br/>"
        "2. Incluye en la cabecera el script con los datos anatómicos reales:<br/>"
        "&lt;script src=&quot;https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/liver_b64.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Crea un modelo 3D con Babylon.js que represente el parénquima hepático con sus lóbulos derecho e izquierdo, la vesícula biliar verde, la vena porta azul, la arteria hepática y la vena cava inferior.<br/>"
        "4. Incluye botones para ilustrar la segmentación quirúrgica de Couinaud (I a VIII) y la filtración de 1.5 litros de sangre por minuto.<br/>"
        "5. Aplica un diseño clínico en modo oscuro (#060913) con tipografía accesible y contrastes cuidados.<br/>"
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
        "<i>«Añade una tarjeta con consejos para cuidar el hígado graso y moderar fármacos después de los 60 años»</i> o "
        "<i>«Coloca una animación de flujo biliar desde los canalículos hasta el duodeno»</i>. "
        "Vuelve a copiar el código, pégalo en tu Taller y ¡comprueba la capacidad regenerativa del hígado!",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Apartado Técnico al final
    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos hiperrealistas y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de los datos médicos (<i>NIH 3D Print Exchange / TC Clínico</i>):</b> Las mallas anatómicas derivan de <b>tomografías computarizadas (TC) abdominales contrastadas</b> del repositorio biomédico oficial de los Institutos Nacionales de la Salud de EE.UU. (NIH 3D).<br/>"
        "• <b>Cómo se ha montado el objeto en la Demo y en el Taller:</b> Los datos morfológicos se compilan en <i>liver_b64.js</i>. Babylon.js aplica materiales PBR con tono rojo-violáceo hepático y dispersión de luz subsuperficial orgánica."
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
    print(f"✅ PDF COD-016 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try:
        build_cod_016_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-016: {e}")
        sys.exit(1)

