#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cod_013.py
Genera la Ficha Didáctica Oficial de 1 Página (Letter/A4):
4. COD-013_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf
para la Sesión 13 del Curso de IA (Simulador 3D: Doble Hélice de ADN • Genética Molecular y Cristalografía PDB).
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/13_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "4. COD-013_Taller_Crea_tu_Propio_Simulador_3D_con_Gemini.pdf")
LOCAL_BACKUP = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/SIMULADORES_INTERACTIVOS/02_INDICES_Y_CATALOGOS/13_COD-013_Taller_Simulador_ADN_3D.pdf"

def build_cod_013_taller_3d_pdf(output_path=PDF_PATH):
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
        textColor=colors.HexColor('#059669'), alignment=1, spaceAfter=1
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
        textColor=colors.HexColor('#047857'), spaceBefore=3, spaceAfter=2
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
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#059669'), spaceAfter=4))

    story.append(Paragraph("<b>[COD-013] Taller: Crea tu propio simulador 3D de la Doble Hélice de ADN</b>", style_title))

    story.append(Paragraph("💡 <b>Misión Didáctica • Genética Molecular, Código de la Vida y Cristalografía PDB:</b>", style_section_h))
    story.append(Paragraph(
        "En este taller pedirás a Gemini desarrollar un visor 3D dextrógiro de la molécula de <b>ADN (Ácido Desoxirribonucleico)</b>. "
        "<b>No requieres saber programar:</b> copiarás el prompt maestro en Gemini, pegarás el código generado en tu <b>Taller de Pruebas</b> y contemplarás la arquitectura biológica: el esqueleto externo de azúcar y fosfato y las cuatro bases nitrogenadas (Adenina, Timina, Citosina y Guanina) unidas por puentes de hidrógeno.",
        style_body
    ))

    # Lista de Tareas
    task_rows = [
        [Paragraph("<b>✅ Tarea 1 • Pídele el código a Gemini (Pestaña 1):</b> "
                   "Abre Gemini (<i>gemini.google.com</i>). Copia el <b>Prompt Maestro</b> inferior, pégalo en el chat y pulsa Enviar.", style_task)],
        [Paragraph("<b>✅ Tarea 2 • Copia el código generado por la IA:</b> "
                   "En la respuesta de Gemini, pulsa <b>«Copiar código»</b> en la esquina superior del bloque.", style_task)],
        [Paragraph("<b>✅ Tarea 3 • Abre el Taller Oficial de Pruebas (Pestaña 2):</b> "
                   "En el mapa de la Sesión 13, pulsa <b>«🚀 Abrir Taller Interactivo de Pruebas ↗»</b>.", style_task)],
        [Paragraph("<b>✅ Tarea 4 • Pega con Ctrl+V y pulsa «Ejecutar Creación»:</b> "
                   "Pega el código con <b>Ctrl+V</b> (o Cmd+V) y pulsa <b>«▶️ Ejecutar Creación»</b>. ¡Tu ADN girará en 3D en pantalla!", style_task)],
        [Paragraph("<b>✅ Tarea 5 • Descubre la Demo genética completa:</b> "
                   "Pulsa <b>«🧬 Doble Hélice ADN 3D»</b> en el taller (o <b>«🧬 Abrir Simulador ADN ↗»</b> en el mapa) para probar los filtros de pares de bases.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[letter[0] - 72])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ECFDF5')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#059669')),
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
        "<i>\"Genera el código de programación (HTML, CSS y JavaScript con Babylon.js) que voy a copiar y pegar en el Taller de Pruebas de mi curso para crear un visor molecular 3D de la Doble Hélice de ADN (B-DNA) basado en cristalografía del Protein Data Bank.<br/>"
        "Requisitos del código:<br/>"
        "1. Entrega el programa en un único bloque de código listo para pulsar directamente «Copiar código» y pegarlo con Ctrl+V.<br/>"
        "2. Incluye en la cabecera los scripts del motor Babylon.js y el conjunto de datos cristalográficos reales:<br/>"
        "&lt;script src=&quot;https://cdn.babylonjs.com/babylon.js&quot;&gt;&lt;/script&gt;<br/>"
        "&lt;script src=&quot;https://cdn.babylonjs.com/loaders/babylonjs.loaders.min.js&quot;&gt;&lt;/script&gt;<br/>"
        "&lt;script src=&quot;https://javiercursocorreo-gif.github.io/Curso-IA/SIMULADORES_INTERACTIVOS/03_ASSETS_3D_Y_DATOS/dna_helix_b64.js&quot;&gt;&lt;/script&gt;<br/>"
        "3. Prohibido inventar gráficos en canvas 2D o esquemas planos: construye en Babylon.js con cilindros y esferas PBR la estructura atómica de la doble hélice dextrógira basada en window.DNA_HELIX_PDB_DATA, con 10 pares de bases por vuelta (paso de 3.4 nm), hebras de fosfato-azúcar antiparalelas y colores diferenciados para A (rojo), T (azul), C (verde) y G (amarillo) sobre fondo oscuro (#030a10) con cámara orbital ArcRotateCamera 360°.<br/>"
        "4. En el bucle de renderizado añade rotación axial continua y botones para destacar los enlaces de hidrógeno en A-T (2 puentes) y G-C (3 puentes).<br/>"
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
        "<i>«Añade una tarjeta histórica en homenaje a la científica Rosalind Franklin y su Foto 51 de difracción de rayos X»</i> o "
        "<i>«Coloca una animación de desenrollado para mostrar cómo se replica el ADN durante la división celular»</i>. "
        "Vuelve a copiar el código en el Taller y ¡observa la magia de la herencia biológica!",
        style_body
    ))
    story.append(Spacer(1, 2))

    # Apartado Técnico al final
    story.append(Paragraph("🔬 <b>¿De dónde proceden los modelos hiperrealistas y cómo se ha montado el objeto 3D?</b>", style_section_h))
    tech_text = (
        "• <b>Origen de los datos cristalográficos (<i>Protein Data Bank / PDB</i>):</b> Las coordenadas atómicas de distancias intermoleculares (0.34 nm entre peldaños, 2.0 nm de diámetro helicoidal) proceden del repositorio científico internacional <b>RCSB PDB (ID: 1BNA)</b>.<br/>"
        "• <b>Cómo se ha montado el objeto en la Demo y en el Taller:</b> Los datos atómicos se empaquetan en <i>dna_helix_b64.js</i>. Babylon.js genera las curvas helicoidales senoidales y las esferas de nucleótidos con materiales PBR reflectantes."
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
    print(f"✅ PDF COD-013 generado con éxito en: {dest_path}")

if __name__ == '__main__':
    try:
        build_cod_013_taller_3d_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF COD-013: {e}")
        sys.exit(1)

