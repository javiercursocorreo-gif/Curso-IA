#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_007.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-007_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 07 del Curso de IA (Simulador 3D: Atlas de la Luna NASA LRO y Cráteres LOLA).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/07_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-007_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/07_COD-007_Taller_Simulador_Luna_3D.pdf"

def build_cod_007_taller_3d_pdf(output_path=PDF_PATH):
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
        textColor=colors.HexColor('#0284C7'), alignment=1, spaceAfter=1
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
        textColor=colors.HexColor('#0369A1'), spaceBefore=3, spaceAfter=2
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
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#0284C7'), spaceAfter=4))

    story.append(Paragraph("<b>[COD-007] Taller: Crea tu propio simulador 3D del Atlas de la Luna (NASA LRO)</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • Astronomía Lunar Interactiva con Gemini:</b>", style_section_h))
    story.append(Paragraph(
        "En esta sesión ordenarás a la Inteligencia Artificial construir un globo lunar tridimensional interactivo con relieve real basado en la misión espacial <b>NASA LRO (Lunar Reconnaissance Orbiter)</b>. "
        "<b>Sin saber programar:</b> pedirás el código a Gemini con el prompt maestro, lo probarás en el <b>Taller de Pruebas</b> y contemplarás los mares basálticos, los cráteres Tycho y Copérnico, y el sitio exacto de alunizaje del Apolo 11 en <i>Mare Tranquillitatis</i>.",
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
                   "En el mapa de la Sesión 07, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b> "
                   "Pega el código con <b>Ctrl+V</b> (o Cmd+V en Mac) y haz clic en <b>«▶️ Ejecutar Creación»</b>. ¡Tu Luna 3D girará y podrás rotarla 360° con el ratón!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Descubre la Demo completa de la NASA:</b> "
                   "Pulsa el botón <b>«🌕 Atlas Lunar 3D»</b> en el taller (o <b>«🌕 Abrir Atlas Lunar 3D ↗»</b> en el mapa) para explorar las fases lunares y los cráteres.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0284C7')),
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
        "<i>\"Genera el código de programación (HTML y JavaScript con Babylon.js) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador 3D del Atlas de la Luna con texturas satelitales oficiales de la NASA.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código para que yo pulse directamente «Copiar código» y lo pegue con Ctrl+V en mi simulador.<br/>"
        "2. Incluye en la cabecera los scripts del motor Babylon.js:<br/>"
        "&lt;script src=&quot;https://cdn.babylonjs.com/babylon.js&quot;&gt;&lt;/script&gt;<br/>"
        "&lt;script src=&quot;https://cdn.babylonjs.com/loaders/babylonjs.loaders.min.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Crea una esfera 3D suave de radio 2.2 que represente la Luna y aplícale la textura fotográfica satelital real de la NASA libre de CORS: https://cdn.jsdelivr.net/gh/mrdoob/three.js@dev/examples/textures/planets/moon_1024.jpg como diffuseTexture (new BABYLON.Texture('https://cdn.jsdelivr.net/gh/mrdoob/three.js@dev/examples/textures/planets/moon_1024.jpg', scene)) con rugosidad mate 0.9 sin relieves invertidos sobre fondo espacial negro con estrellas.<br/>"
        "4. Configura una cámara orbital ArcRotateCamera con rotación 360°, zoom suave con la rueda del ratón y una luz direccional lateral intensa que simule la iluminación del Sol proyectando sombras alargadas sobre los cráteres (simulación de fases lunares).<br/>"
        "5. Añade una rotación axial lenta automática y marcadores luminosos en Mare Tranquillitatis (Apolo 11, 1969) y en el Cráter Tycho.<br/>"
        "6. Escribe exclusivamente el bloque de código para que al copiarlo a mi simulador genere el Atlas Lunar 3D inmediatamente.\"</i>"
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
        "<i>«Añade un deslizador para cambiar la posición del Sol y ver cómo cambia de Luna Llena a Cuarto Creciente»</i> o "
        "<i>«Coloca una banderita conmemorativa en las coordenadas del Apolo 11»</i>. "
        "Vuelve a copiar el código, pégalo en tu Taller y ¡mira cómo tu Luna responde en directo!",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Apartado Técnico al final
    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos hiperrealistas y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de los datos lunares científicos (<i>NASA LRO / LOLA</i>):</b> Los mapas de relieve altimétrico y las texturas de superficie proceden de los satélites <b>Lunar Reconnaissance Orbiter (LRO)</b> de la NASA y del altímetro láser <b>LOLA (Lunar Orbiter Laser Altimeter)</b>, con resolución métrica global de cráteres, cordilleras y mares basálticos.<br/>"
        "• <b>Cómo se ha montado el objeto en la Demo y en el Taller:</b> En el motor <b>Babylon.js</b>, la superficie se modela con shaders PBR físicos donde la incidencia de la luz solar rasante genera micro-sombras automáticas sobre las paredes de los cráteres, emulando la visión real de los telescopios astronómicos terrestres y naves orbitales."
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
    print(f"✅ PDF COD-007 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try:
        build_cod_007_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-007: {e}")
        sys.exit(1)

