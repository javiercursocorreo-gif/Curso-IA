#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_005.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-005_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 05 del Curso de IA (Simulador 3D del Sistema Solar Kepleriano, NASA y Órbitas Planetarias).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/05_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-005_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/05_COD-005_Taller_Simulador_Sistema_Solar_3D.pdf"

def build_cod_005_taller_3d_pdf(output_path=PDF_PATH):
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

    story.append(Paragraph("<b>[COD-005] Taller: Crea tu simulador 3D del Sistema Solar Kepleriano (NASA)</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • Astronomía Dinámica y Órbitas con Gemini:</b>", style_section_h))
    story.append(Paragraph(
        "En esta sesión pedirás a la Inteligencia Artificial generar el código completo para construir un planetario tridimensional del <b>Sistema Solar</b> con física kepleriana real, el Sol radiante y texturas fotográficas satelitales oficiales de la NASA. "
        "<b>Sin saber programar:</b> pedirás el código a Gemini con el prompt maestro, lo probarás en el <b>Taller de Pruebas</b> y contemplarás los planetas orbitando a su velocidad relativa real con rotación 360°.",
        style_body
    ))

    # Lista de Tareas (Checklist Guiado)
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> "
                   "Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> inferior, pégalo en el chat y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b> "
                   "En la respuesta de Gemini, haz clic en el botón <b>«Copiar código»</b> situado en la esquina superior del bloque.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b> "
                   "En el mapa de la Sesión 05, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b> "
                   "Pega el código con <b>Ctrl+V</b> (o Cmd+V en Mac) y haz clic en <b>«▶️ Ejecutar Creación»</b>. ¡Los planetas orbitarán en 3D en tu pantalla!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Descubre la Demo completa:</b> "
                   "Pulsa el botón <b>«🌌 Sistema Solar 3D»</b> en el taller (o <b>«🌌 Ver Simulador Sistema Solar ↗»</b> en el mapa) para ver el Vórtice Galáctico.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FEF3C7')),
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
        "<i>\"Genera el código de programación (HTML y JavaScript con Three.js) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un planetario 3D del Sistema Solar con texturas satelitales oficiales de la NASA.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código para que yo pulse directamente «Copiar código» y lo pegue con Ctrl+V en mi simulador.<br/>"
        "2. Incluye en la cabecera las librerías oficiales de Three.js y OrbitControls:<br/>"
        "&lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js&quot;&gt;&lt;/script&gt;<br/>"
        "&lt;script src=&quot;https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Crea el Sol central brillante con luz puntual y los planetas orbitando a distancias proporcionales con la 3ª Ley de Kepler sobre fondo espacial negro con estrellas.<br/>"
        "4. Aplica directamente a la Tierra la textura satelital real de la NASA libre de CORS: https://cdn.jsdelivr.net/gh/mrdoob/three.js@dev/examples/textures/planets/earth_atmos_2048.jpg y a la Luna la textura https://cdn.jsdelivr.net/gh/mrdoob/three.js@dev/examples/textures/planets/moon_1024.jpg mediante THREE.TextureLoader.<br/>"
        "5. Configura una cámara orbital con rotación 360°, zoom suave con la rueda del ratón y trazas de las órbitas elípticas en líneas tenues.<br/>"
        "6. Escribe exclusivamente el bloque de código para que al copiarlo a mi simulador genere el Sistema Solar 3D inmediatamente.\"</i>"
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
        "<i>«Añade los anillos de Saturno con inclinación de 27°»</i> o "
        "<i>«Coloca un botón para acelerar el tiempo de órbita y ver a Mercurio dar 4 vueltas completas por cada año terrestre»</i>. "
        "Vuelve a copiar el código, pégalo en tu Taller y ¡mira cómo tu Sistema Solar responde en directo!",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Apartado Técnico al final
    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos hiperrealistas y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de las texturas satelitales y efemérides (<i>NASA JPL / Solar System Dynamics</i>):</b> Los mapas esféricos de superficie proceden de las misiones espaciales <b>NASA Blue Marble (satélites Terra/Aqua)</b>, <b>LRO</b> y <b>Cassini-Huygens</b>, con parámetros orbitales exactos calibrados según la base de datos de efemérides <i>HORIZONS</i> del JPL.<br/>"
        "• <b>Cómo se ha montado el objeto en la Demo y en el Taller:</b> En <b>Three.js</b>, la velocidad angular de cada planeta se calcula en cada fotograma mediante la 3ª Ley de Kepler ($T^2 \\propto a^3$), garantizando que Mercurio orbite 4 veces más rápido que la Tierra y Júpiter complete su órbita en 11.86 años relativos."
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
    print(f"✅ PDF COD-005 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try:
        build_cod_005_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-005: {e}")
        sys.exit(1)
