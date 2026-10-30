#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_001.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-001_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 01 del Curso de IA (Simulador 3D de los Pulmones y Árbol Bronquial).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/01_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-001_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/01_COD-001_Taller_Simulador_Pulmones_3D.pdf"

def build_cod_001_taller_3d_pdf(output_path=PDF_PATH):
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
        fontName='Helvetica', fontSize=7.5, leading=9.9,
        textColor=colors.HexColor('#0F172A')
    )

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("BLOQUE IV: CIENCIA INTERACTIVA & TALLER DE CÓDIGO CON GEMINI [COD]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#0284C7'), spaceAfter=4))

    story.append(Paragraph("<b>[COD-001] Taller: Crea tu propio simulador de los pulmones</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • De Espectador a Creador con IA:</b>", style_section_h))
    story.append(Paragraph(
        "En esta práctica vas a ordenar a la Inteligencia Artificial generar el código necesario para construir tu propio simulador 3D del aparato respiratorio humano con su árbol bronquial fractal y animación biológica de respiración. "
        "<b>No necesitas saber programar:</b> pedirás el código a Gemini con el prompt maestro, lo copiarás en tu <b>Taller de Pruebas</b> y comprobarás cómo tus pulmones cobran vida en tu pantalla.",
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
                   "En el mapa de la Sesión 01, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b> "
                   "Pega el código con <b>Ctrl+V</b> (o Cmd+V en Mac) y haz clic en <b>«▶️ Ejecutar Creación»</b>. ¡Tus pulmones 3D ventilarán y podrás rotarlos 360°!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Descubre la Demo completa:</b> "
                   "Pulsa el botón <b>«🫁 Pulmones 3D»</b> en el taller (o <b>«🫁 Ver Simulador Pulmones 3D ↗»</b> en el mapa) para ver el modelo médico con control de 8 a 28 RPM.", style_task)],
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
        "<i>\"Genera el código de programación (HTML y JavaScript con Babylon.js) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador 3D hiperrealista del aparato respiratorio humano.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código para que yo pulse directamente «Copiar código» y lo pegue con Ctrl+V en mi simulador.<br/>"
        "2. Incluye en la cabecera los scripts del motor Babylon.js y el modelo anatómico fotogramétrico:<br/>"
        "&lt;script src=&quot;https://cdn.babylonjs.com/babylon.js&quot;&gt;&lt;/script&gt;<br/>"
        "&lt;script src=&quot;https://cdn.babylonjs.com/loaders/babylonjs.loaders.min.js&quot;&gt;&lt;/script&gt;<br/>"
        "&lt;script src=&quot;https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/lungs_b64.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Carga el modelo 3D anatómico real con SceneLoader.ImportMesh('', '', window.LUNGS_GLB_B64, ...) y céntralo con cámara orbital 360° e iluminación de estudio sobre fondo azul noche (#060913).<br/>"
        "4. Detén cualquier animación interna o de morphing del archivo 3D (animationGroups.forEach(ag => ag.stop())) para mantener el árbol traqueobronquial y los pulmones 100% firmes, estables y quietos en el centro (sin vaivén vertical, sin subir ni bajar), permitiendo rotar libremente en 360° con el ratón e incluyendo una rotación suave automática.<br/>"
        "5. Escribe exclusivamente el bloque de código para que al copiarlo a mi simulador genere los pulmones 3D hiperrealistas.\"</i>"
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
        "<i>«Añade una luz de quirófano azul cian que ilumine la tráquea por detrás»</i> o "
        "<i>«Haz que gire lentamente sobre su eje vertical para ver los bronquios desde todos los ángulos»</i>. "
        "Vuelve a copiar el código, pégalo en tu Taller y ¡mira cómo cambia en directo!",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Apartado Técnico al final del todo: Origen de las Imágenes/Modelos Hiperrealistas y Montaje del Objeto 3D
    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos hiperrealistas y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen del modelo anatómico hiperrealista (<i>lungs.glb / lungs_b64.js</i>):</b> Procede del repositorio biomédico oficial <b>NIH 3D Print Exchange (National Institutes of Health, EE. UU.)</b> y <b>BodyParts3D / Anatomography</b> (Instituto DBCLS de Ciencias de la Vida, Japón, bajo licencia abierta <i>Creative Commons</i>), reconstruido mediante <b>tomografía computarizada (TC) médica real</b> de la tráquea, bronquios y lóbulos pulmonares.<br/>"
        "• <b>Cómo se ha montado el objeto en la Demo y en el Taller:</b> El archivo tridimensional <i>.glb</i> (formato <i>glTF 2.0</i> con texturas PBR de tejido mucoso y anillos cartilaginosos) se ha empaquetado en Base64 dentro de <i>lungs_b64.js</i> para evitar bloqueos de seguridad del navegador (CORS). En el motor <b>Babylon.js</b>, se carga la malla 3D con <i>SceneLoader.ImportMesh</i>, se detienen las animaciones internas para mantener el órgano firme, quieto y sin vaivén vertical, permitiendo la exploración científica 360° limpia y centrada con iluminación médica de estudio."
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
    print(f"✅ PDF COD-001 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try:
        build_cod_001_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-001: {e}")
        sys.exit(1)
