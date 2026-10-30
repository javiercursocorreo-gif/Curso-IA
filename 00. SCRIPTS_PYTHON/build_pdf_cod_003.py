#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_003.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-003_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 03 del Curso de IA (Simulador Arqueológico Pompeya HD y Reconstrucción del 79 d.C.).
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
        textColor=colors.HexColor('#B45309'), alignment=1, spaceAfter=1
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
        textColor=colors.HexColor('#92400E'), spaceBefore=3, spaceAfter=2
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
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#B45309'), spaceAfter=4))

    story.append(Paragraph("<b>[COD-003] Taller: Crea tu simulador de Pompeya HD y Reconstrucción del 79 d.C.</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • Arqueología e Historia Visual con Gemini:</b>", style_section_h))
    story.append(Paragraph(
        "En esta sesión pedirás a la Inteligencia Artificial construir un visor interactivo de comparación temporal deslizante entre las ruinas excavadas de la ciudad romana de <b>Pompeya</b> y su reconstrucción arqueológica en el año 79 d.C. "
        "<b>Sin saber programar:</b> pedirás el código a Gemini con el prompt maestro, lo probarás en el <b>Taller de Pruebas</b> y comprobarás cómo un deslizador central revela los frescos policromados y mosaicos originales sobre las ruinas.",
        style_body
    ))

    # Lista de Tareas (Checklist Guiado)
    story.append(Paragraph("📋 <b>Lista de Tareas del Alumno (Paso a Paso en 2 Pestañas):</b>", style_section_h))
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> "
                   "Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> inferior, pégalo en el chat y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b> "
                   "En la respuesta de Gemini, haz clic en el botón <b>«Copiar código»</b> situado en la esquina superior del bloque.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b> "
                   "En el mapa de la Sesión 03, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b> "
                   "Pega el código con <b>Ctrl+V</b> (o Cmd+V en Mac) y haz clic en <b>«▶️ Ejecutar Creación»</b>. ¡Desliza el control para viajar al año 79 d.C.!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Descubre la Demo completa:</b> "
                   "Pulsa el botón <b>«🏛️ Pompeya HD»</b> en el taller (o <b>«🏛️ Ver Simulador Pompeya HD ↗»</b> en el mapa) para inspeccionar la Domus romana.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FEF3C7')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#B45309')),
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
        "<i>\"Genera el código de programación (HTML y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un visor comparativo interactivo de Pompeya HD con fotografías arqueológicas oficiales.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código para que yo pulse directamente «Copiar código» y lo pegue con Ctrl+V en mi simulador.<br/>"
        "2. Incluye en la cabecera el script oficial con las fotografías de alta resolución en Base64:<br/>"
        "&lt;script src=&quot;https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/pompeii_photos_b64.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Crea un visor interactivo de doble capa superpuesta con las imágenes oficiales: fondo con las ruinas reales (window.POMPEII_RUINS_B64) y capa superior con la reconstrucción fidedigna del 79 d.C. (window.POMPEII_RECON_B64).<br/>"
        "4. Añade un deslizador divisor central (before/after slider) que el alumno pueda arrastrar con el ratón de izquierda a derecha, revelando en tiempo real las columnas con estuco, el impluvium y los frescos romanos sobre las ruinas.<br/>"
        "5. Incorpora un selector de zoom interactivo y fichas explicativas de los elementos arquitectónicos de la Domus romana.<br/>"
        "6. Escribe exclusivamente el bloque de código para que al copiarlo a mi simulador genere el visor de Pompeya HD inmediatamente.\"</i>"
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
        "<i>«Añade una lupa de aumento al pasar el ratón para inspeccionar el mosaico del suelo»</i> o "
        "<i>«Coloca un botón que reproduzca el sonido ambiental de una calle romana con fuentes de agua»</i>. "
        "Vuelve a copiar el código, pégalo en tu Taller y ¡mira cómo tu visor cobra vida en directo!",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Apartado Técnico al final
    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos hiperrealistas y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de las fotografías y levantamientos arqueológicos (<i>pompeii_photos_b64.js</i>):</b> Proceden de los archivos oficiales del <b>Parco Archeologico di Pompei (Ministero della Cultura, Italia)</b> y de los programas de digitalización patrimonial de la <b>UNESCO</b>, con ortofotografías gigapíxel de la Domus de los Menandro y la Casa de los Vettii.<br/>"
        "• <b>Cómo se ha montado el objeto en la Demo y en el Taller:</b> Las imágenes de alta definición se empaquetan en Base64 para garantizar carga offline instantánea sin latencia. Un canvas interactivo de composición bicapa calcula el recorte geométrico (`clip-path`) en tiempo real al mover el ratón, permitiendo la comparación arqueológica fluida a 60 fps."
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
    print(f"✅ PDF COD-003 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try:
        build_cod_003_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-003: {e}")
        sys.exit(1)
