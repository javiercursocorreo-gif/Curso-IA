#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_014.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-014_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 14 del Curso de IA (Simulador 3D: Auroras Ultravioletas de Júpiter • NASA Cassini y Hubble).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/14_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-014_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/14_COD-014_Taller_Simulador_Jupiter_3D.pdf"

def build_cod_014_taller_3d_pdf(output_path=PDF_PATH):
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
        textColor=colors.HexColor('#7C3AED'), alignment=1, spaceAfter=1
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
        textColor=colors.HexColor('#6D28D9'), spaceBefore=3, spaceAfter=2
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
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#7C3AED'), spaceAfter=4))

    story.append(Paragraph("<b>[COD-014] Taller: Crea tu propio simulador 3D de Júpiter y sus Auroras</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • Ciencias Planetarias, Magnetosferas y Misiones NASA con Gemini:</b>", style_section_h))
    story.append(Paragraph(
        "En este taller ordenarás a Gemini crear un simulador 3D del planeta <b>Júpiter</b> y sus espectaculares <b>auroras polares ultravioletas</b>. "
        "<b>No requieres saber programar:</b> copiarás el prompt maestro en Gemini, pegarás el código generado en tu <b>Taller de Pruebas</b> y contemplarás el gigante joviano con sus cinturones de nubes, la Gran Mancha Roja y los anillos de plasma auroral alimentados por el volcán Ío.",
        style_body
    ))

    # Lista de Tareas
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> "
                   "Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> inferior, pégalo en el chat y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b> "
                   "En la respuesta de Gemini, pulsa <b>«Copiar código»</b> en la esquina superior del bloque.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b> "
                   "En el mapa de la Sesión 14, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b> "
                   "Pega el código con <b>Ctrl+V</b> (o Cmd+V) y pulsa <b>«▶️ Ejecutar Creación»</b>. ¡Tu planeta Júpiter se mostrará con auroras brillantes!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Descubre la Demo planetaria completa:</b> "
                   "Pulsa <b>«🪐 Júpiter & Auroras 3D»</b> en el taller (o <b>«🪐 Abrir Auroras Júpiter ↗»</b> en el mapa) para probar los puntos interactivos.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FAF5FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#8B5CF6')),
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
        "<i>\"Genera el código de programación (HTML, CSS y JavaScript con Babylon.js) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador 3D de Júpiter y sus auroras boreales ultravioletas con texturas de la NASA.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.<br/>"
        "2. Incluye en la cabecera los scripts del motor Babylon.js y los datos de emisión auroral en Base64:<br/>"
        "&lt;script src=&quot;https://cdn.babylonjs.com/babylon.js&quot;&gt;&lt;/script&gt;<br/>"
        "&lt;script src=&quot;https://cdn.babylonjs.com/loaders/babylonjs.loaders.min.js&quot;&gt;&lt;/script&gt;<br/>"
        "&lt;script src=&quot;https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/jupiter_aurora_b64.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Prohibido inventar texturas o cuadrículas en canvas 2D: crea una esfera planetaria 3D suave y aplícale directamente la textura fotográfica real de Júpiter libre de CORS: https://cdn.jsdelivr.net/gh/mrdoob/three.js@dev/examples/textures/planets/jupiter.jpg como diffuseTexture (new BABYLON.Texture('https://cdn.jsdelivr.net/gh/mrdoob/three.js@dev/examples/textures/planets/jupiter.jpg', scene)), mostrando la Gran Mancha Roja y bandas atmosféricas sobre fondo espacial oscuro.<br/>"
        "4. Superpón en los polos anillos luminosos de emisión auroral ultravioleta (cian/violeta) con brillo emisivo que reaccionen a la rotación orbital ArcRotateCamera 360°.<br/>"
        "5. Escribe exclusivamente el bloque de código para que al copiarlo a mi simulador funcione inmediatamente.\"</i>"
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
        "<i>«Añade una tarjeta que compare el tamaño de la Gran Mancha Roja con la Tierra entera»</i> o "
        "<i>«Coloca una opción para activar un destello pulsante en las auroras según el viento solar»</i>. "
        "Vuelve a copiar el código, pégalo en tu Taller y ¡mira a Júpiter en plena actividad magnética!",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Apartado Técnico al final
    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos hiperrealistas y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de los datos jovianos (<i>NASA JPL Cassini & Hubble STScI</i>):</b> Las bandas nubosas y espectros ultravioletas provienen de las cámaras multiespectrales de la sonda <b>Cassini (sobrevuelo del año 2000)</b> y del espectrógrafo espacial STIS del <b>Telescopio Espacial Hubble</b>.<br/>"
        "• <b>Cómo se ha montado el objeto en la Demo y en el Taller:</b> Los datos planetarios se integran en <i>jupiter_aurora_b64.js</i>. Babylon.js utiliza texturas cilíndricas jovianas y mallas de disco con shaders emisivos brillantes en los polos magnéticos."
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
    print(f"✅ PDF COD-014 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try:
        build_cod_014_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-014: {e}")
        sys.exit(1)

