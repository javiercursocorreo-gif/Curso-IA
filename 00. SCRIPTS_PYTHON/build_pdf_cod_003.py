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
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/03_COD-003_Taller_Simulador_Pompeya_HD.pdf"

def build_cod_003_taller_3d_pdf(output_path=PDF_PATH):
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
        textColor=colors.HexColor('#D97706'), alignment=1, spaceAfter=1
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
        textColor=colors.HexColor('#B45309'), spaceBefore=3, spaceAfter=2
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
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#D97706'), spaceAfter=4))

    story.append(Paragraph("<b>[COD-003] Taller: Crea tu propio simulador de las ruinas de Pompeya</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • Arqueología Digital con Inteligencia Artificial:</b>", style_section_h))
    story.append(Paragraph(
        "En este taller ordenarás a Gemini crear un <b>visor interactivo de las ruinas reales de Pompeya</b> para contemplar en alta definición el Templo de Apolo tal como se conserva hoy en día. "
        "<b>Sin saber programar:</b> pedirás el código a Gemini con el prompt maestro, lo probarás pulsando <b>«▶️ Ejecutar Creación»</b> y verás las ruinas romanas. ¡Y la gran sorpresa llegará al pulsar el botón <b>«🏛️ Pompeya HD»</b>, donde se revelará la reconstrucción del año 79 d.C. con la cortina deslizante de viaje en el tiempo!",
        style_body
    ))

    # Apartado Técnico: Origen de las Imágenes Hiperrealistas y Montaje del Objeto
    story.append(Paragraph("🔬 <b>¿De dónde proceden las imágenes hiperrealistas y cómo se ha montado el visor?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de las fotografías hiperrealistas (<i>pompeii_ruins_hd.jpg y pompeii_reconstructed_hd.jpg</i>):</b> La imagen de las ruinas actuales procede del archivo patrimonial de <b>Wikimedia Commons / Parque Arqueológico de Pompeya (Italia)</b>, mostrando el <b>Templo de Apolo</b> real con su columnata corintia, el altar y el monte Vesubio al fondo. La imagen hiperrealista del año 79 d.C. se ha creado mediante <b>restauración arqueológica por IA generativa y composición digital alineada píxel a píxel</b> (manteniendo exactamente la perspectiva de cada columna, estatua de bronce, entablamento policromado y pavimento del foro).<br/>"
        "• <b>Cómo se ha montado el objeto en el Taller y en la Demo:</b> Ambas fotografías en alta resolución se han codificado en Base64 dentro de <i>pompeii_photos_b64.js</i>. En el <b>Taller</b>, el código de Gemini carga <i>window.POMPEII_RUINS_B64</i> en un visor arqueológico documental. En la <b>Demo («🏛️ Pompeya HD»)</b>, las dos capas fotográficas se superponen con registro geométrico exacto y una máscara dinámica (<i>clip-path</i>) gobernada por un deslizador para barrer en tiempo real entre las ruinas actuales y el esplendor imperial romano."
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
                   "En el mapa de la Sesión 03, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b> "
                   "Pega el código con <b>Ctrl+V</b> (o Cmd+V en Mac) en el cuadro izquierdo y pulsa <b>«▶️ Ejecutar Creación»</b> para ver las ruinas reales.", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Descubre la sorpresa con «🏛️ Pompeya HD»:</b> "
                   "Pulsa el botón <b>«🏛️ Pompeya HD»</b> en el taller (o <b>«🏛️ Ver Tesoro Arqueológico 3D ↗»</b> en el mapa) para deslizar la cortina del tiempo al año 79 d.C.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFBEB')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#D97706')),
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
        "<i>\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un visor interactivo de las Ruinas de Pompeya (Templo de Apolo).<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código para que yo pulse directamente «Copiar código» y lo pegue con Ctrl+V en mi simulador.<br/>"
        "2. Incluye en la cabecera el script con las fotografías reales del archivo arqueológico:<br/>"
        "&lt;script src=&quot;https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/pompeii_photos_b64.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Crea un visor arqueológico elegante que muestre la fotografía real en alta resolución de las ruinas actuales utilizando window.POMPEII_RUINS_B64.<br/>"
        "4. No incluyas barras deslizantes (slider): muestra únicamente las ruinas de piedra con un marco arqueológico refinado, título histórico y una tarjeta informativa con datos del Templo de Apolo.<br/>"
        "5. Aplica un diseño moderno oscuro con tipografía clara y botones interactivos para explorar detalles o alternar modos de nitidez.<br/>"
        "6. Escribe exclusivamente el bloque de código para que al copiarlo a mi simulador funcione inmediatamente.\"</i>"
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
        "👉 <b>¡Pídele a Gemini que modifique tu simulador!</b> En la misma conversación dile: "
        "<i>«Añade un botón que aplique un filtro de color sepia antiguo simulando una fotografía de expedición del siglo XIX»</i> o "
        "<i>«Añade una lupa o zoom suave al pasar el ratón por las columnas del Templo de Apolo»</i>. "
        "Copia el nuevo código, pégalo en el Taller y comprueba las novedades al instante.",
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
    print(f"✅ PDF COD-003 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try:
        build_cod_003_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-003: {e}")
        sys.exit(1)
