#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_015.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-015_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 15 del Curso de IA (Simulador 3D: El Partenón de Atenas & Proporción Áurea • Acrópolis y Geometría Clásica).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/15_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-015_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/15_COD-015_Taller_Simulador_Partenon_3D.pdf"

def build_cod_015_taller_3d_pdf(output_path=PDF_PATH):
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
        fontName='Helvetica', fontSize=7.4, leading=9.8,
        textColor=colors.HexColor('#0F172A')
    )

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & TALLER DE CÓDIGO CON GEMINI [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#D97706'), spaceAfter=4))

    story.append(Paragraph("<b>[COD-015] Taller: Crea tu propio simulador 3D del Partenón de Atenas</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • Arqueología Clásica, Proporción Áurea (Phi) y Óptica Griega:</b>", style_section_h))
    story.append(Paragraph(
        "En este taller pedirás a Gemini crear una reconstrucción arquitectónica 3D del <b>Partenón de Atenas</b> en la Acrópolis. "
        "<b>No requieres saber programar:</b> pegarás el prompt maestro en Gemini, copiarás el código en tu <b>Taller de Pruebas</b> y contemplarás las correcciones ópticas de los arquitectos Ictino y Calícrates: la curvatura convexa del estilóbato (6.5 y 11 cm), la éntasis de las columnas convergentes a 2.400 m de altura y la superposición de la Proporción Áurea (Phi = 1.618).",
        style_body
    ))

    # Lista de Tareas
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> "
                   "Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> inferior, pégalo en el chat y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b> "
                   "En la respuesta de Gemini, pulsa <b>«Copiar código»</b> en la esquina superior del bloque.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b> "
                   "En el mapa de la Sesión 15, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b> "
                   "Pega el código con <b>Ctrl+V</b> (o Cmd+V) y pulsa <b>«▶️ Ejecutar Creación»</b>. ¡Tu Partenón 3D se mostrará con controles interactivos!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Descubre la Demo arqueológica completa:</b> "
                   "Pulsa <b>«🏛️ Partenón & Proporción Áurea 3D»</b> en el taller (o <b>«🏛️ Abrir Partenón Dorado 3D ↗»</b> en el mapa) para probar los puntos de corrección óptica.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFBEB')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#F59E0B')),
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
        "<i>\"Genera el código de programación (HTML, CSS y JavaScript) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un visor interactivo 3D del Partenón de Atenas con datos arqueológicos reales del levantamiento de la Acrópolis.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.<br/>"
        "2. Incluye en la cabecera el script con los datos arqueológicos reales:<br/>"
        "&lt;script src=&quot;https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/parthenon_b64.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Modela con Babylon.js el templo octástilo dórico en mármol pentélico con 8 columnas frontales y 17 laterales, arquitrabe, friso y frontón triangular.<br/>"
        "4. Incluye botones para ilustrar la Proporción Áurea (Phi = 1.618), la éntasis de las columnas y la curvatura del estilóbato.<br/>"
        "5. Aplica un diseño clásico solemne en modo oscuro (#06070a) con tipografía elegante y controles accesibles.<br/>"
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
        "<i>«Añade una tarjeta que explique la estatua crisoelefantina de Atenea Pártenos de 12 metros de altura esculpida por Fidias en oro y marfil»</i> o "
        "<i>«Muestra la espiral dorada de Fibonacci superpuesta sobre la fachada frontal»</i>. "
        "Vuelve a copiar el código, pégalo en tu Taller y ¡descubre la genialidad de la Grecia Clásica!",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Apartado Técnico al final
    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos hiperrealistas y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de las mediciones arqueológicas (<i>Servicio de Restauración de Monumentos de la Acrópolis - YSMA</i>):</b> Las cotas y curvaturas ópticas derivan del levantamiento milimétrico del <b>Partenón de Atenas (447-432 a.C.)</b> dirigido por arqueólogos e ingenieros del Ministerio de Cultura de Grecia.<br/>"
        "• <b>Cómo se ha montado el objeto en la Demo y en el Taller:</b> Las proporciones reales se compilan en <i>parthenon_b64.js</i>. Babylon.js utiliza materiales PBR con albedo de mármol pentélico envejecido e iluminación solar mediterránea."
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
    print(f"✅ PDF COD-015 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try:
        build_cod_015_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-015: {e}")
        sys.exit(1)

