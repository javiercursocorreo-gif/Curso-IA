#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_004.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-004_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 04 del Curso de IA (Simulador 3D del Ojo Humano, Córnea, Cristalino y Retina).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/04_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-004_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/04_COD-004_Taller_Simulador_Ojo_Humano_3D.pdf"

def build_cod_004_taller_3d_pdf(output_path=PDF_PATH):
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
        textColor=colors.HexColor('#0F766E'), alignment=1, spaceAfter=1
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
        textColor=colors.HexColor('#0D9488'), spaceBefore=3, spaceAfter=2
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
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#0F766E'), spaceAfter=4))

    story.append(Paragraph("<b>[COD-004] Taller: Crea tu propio simulador 3D del ojo humano y la visión</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • Óptica y Anatomía Ocular con Gemini:</b>", style_section_h))
    story.append(Paragraph(
        "En esta sesión pedirás a la Inteligencia Artificial generar el código completo para construir un modelo anatómico tridimensional interactivo del <b>globo ocular humano</b> con corte sagital, capas ópticas y refracción de luz. "
        "<b>Sin saber programar:</b> pedirás el código a Gemini con el prompt maestro, lo probarás en el <b>Taller de Pruebas</b> y comprobarás cómo la córnea, el iris, el cristalino y la retina se visualizan con rotación 360°.",
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
                   "En el mapa de la Sesión 04, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b> "
                   "Pega el código con <b>Ctrl+V</b> (o Cmd+V en Mac) y haz clic en <b>«▶️ Ejecutar Creación»</b>. ¡Tu ojo 3D rotará y podrás explorarlo en 360° con el ratón!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Descubre la Demo completa:</b> "
                   "Pulsa el botón <b>«👁️ Ojo Humano 3D»</b> en el taller (o <b>«👁️ Ver Simulador Ojo Humano ↗»</b> en el mapa) para ver la refracción de rayos luminosos.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0FDFA')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0F766E')),
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
        "<i>\"Genera el código de programación (HTML y JavaScript con Three.js) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un simulador 3D anatómico del ojo humano y la visión con fuentes biomédicas oficiales.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código para que yo pulse directamente «Copiar código» y lo pegue con Ctrl+V en mi simulador.<br/>"
        "2. Incluye en la cabecera las librerías oficiales de Three.js y OrbitControls:<br/>"
        "&lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js&quot;&gt;&lt;/script&gt;<br/>"
        "&lt;script src=&quot;https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Modela el globo ocular con su esclerótica blanca vascularizada, una córnea transparente convexa en el polo anterior, un iris fotográfico circular pigmentado con pupila central y un cristalino biconvexo translúcido interior sobre fondo oscuro (#060913).<br/>"
        "4. Configura controles orbitales 360°, zoom suave con la rueda del ratón y un modo de corte sagital o transparencia que permita ver la retina interior y el nacimiento del nervio óptico posterior.<br/>"
        "5. Añade botones para trazar la trayectoria de rayos de luz que convergen en la fóvea central de la retina.<br/>"
        "6. Escribe exclusivamente el bloque de código para que al copiarlo a mi simulador genere el Ojo Humano 3D inmediatamente.\"</i>"
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
        "<i>«Añade un deslizador para simular cómo se dilata y contrae la pupila según la intensidad de la luz»</i> o "
        "<i>«Muestra cómo cambia el enfoque de objetos cercanos y lejanos modificando la curvatura del cristalino (acomodación ocular)»</i>. "
        "Vuelve a copiar el código, pégalo en tu Taller y ¡mira cómo tu ojo responde en directo!",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Apartado Técnico al final
    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos hiperrealistas y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de los datos anatómicos oculares:</b> Proceden del <b>National Eye Institute (NEI)</b> y de los repositorios de tomografía de coherencia óptica (OCT) del <b>NIH (National Institutes of Health, EE. UU.)</b>, con mediciones micrométricas de espesores corneales, índice de refracción del humor acuoso (n=1.336) y curvatura anatómica de la fóvea retiniana.<br/>"
        "• <b>Cómo se ha montado el objeto en la Demo y en el Taller:</b> En el motor <b>Three.js</b>, las distintas mallas se ensamblan con materiales MeshPhysicalMaterial con transmisión de luz real (fresnel, roughness dieléctrico y refracción), permitiendo ver a través de la córnea hacia las estructuras internas del ojo con iluminación de laboratorio."
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
    print(f"✅ PDF COD-004 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try:
        build_cod_004_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-004: {e}")
        sys.exit(1)
