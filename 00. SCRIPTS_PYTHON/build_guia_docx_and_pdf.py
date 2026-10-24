#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_guia_docx_and_pdf.py
Genera la Guía de Publicación Oficial en:
1. Microsoft Word (.docx) 100% estándar usando la librería oficial python-docx
2. Documento PDF de alta legibilidad usando ReportLab
3. Formato HTML compatible con navegadores y editores

Garantiza apertura inmediata en Word sin errores de 'no se puede abrir' o 'texto no legible'.
"""

import os
import sys
import subprocess

COMUN_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-ROBOTICA-IA-COMUN"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IA_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

# Asegurar python-docx
try:
    import docx
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml import parse_xml, OxmlElement
    from docx.oxml.ns import nsdecls, qn
except ImportError:
    print("⏳ Instalando python-docx para garantizar compatibilidad nativa con Word...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx", "-q"])
    import docx
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml import parse_xml, OxmlElement
    from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def create_word_docx(output_path):
    doc = docx.Document()
    
    # Márgenes de página (2 cm)
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Título principal
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = p_title.add_run("GUÍA DE PUBLICACIÓN EN GITHUB Y CLASSROOM")
    run_title.font.name = "Arial"
    run_title.font.size = Pt(20)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(2, 132, 199) # Azul #0284C7

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = p_sub.add_run("Workflow de Trabajo en Equipo: Tú (Profesor) y Antigravity (Asistente IA)")
    run_sub.font.name = "Arial"
    run_sub.font.size = Pt(11)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(100, 116, 139)

    doc.add_paragraph() # Espacio

    # Caja Introductoria
    tbl_intro = doc.add_table(rows=1, cols=1)
    tbl_intro.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_intro = tbl_intro.cell(0, 0)
    set_cell_background(cell_intro, "F0F9FF")
    p_intro = cell_intro.paragraphs[0]
    p_intro.paragraph_format.space_before = Pt(6)
    p_intro.paragraph_format.space_after = Pt(6)
    p_intro.paragraph_format.left_indent = Inches(0.2)
    p_intro.paragraph_format.right_indent = Inches(0.2)
    
    r_intro_bold = p_intro.add_run("💡 Introducción al Sistema Unificado:\n")
    r_intro_bold.bold = True
    r_intro_bold.font.color.rgb = RGBColor(3, 105, 161)
    r_intro_text = p_intro.add_run(
        "Este flujo de trabajo garantiza que todo el material educativo (teoría, simuladores interactivos, "
        "fichas didácticas y monográficos) viaje desde tu Mac hasta Google Classroom sin gastar espacio en tu Google Drive "
        "y con una experiencia 100% limpia para los alumnos mediante Mapas Interactivos HTML únicos."
    )
    r_intro_text.font.size = Pt(10)

    doc.add_paragraph()

    def add_section_header(text, icon=""):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(f"{icon} {text}")
        run.font.name = "Arial"
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.color.rgb = RGBColor(15, 23, 42)
        # Línea inferior decorativa
        return p

    def add_bullet(text, bold_prefix="", level=0):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        if bold_prefix:
            r_b = p.add_run(bold_prefix + " ")
            r_b.bold = True
            r_b.font.color.rgb = RGBColor(30, 41, 59)
        r_t = p.add_run(text)
        r_t.font.size = Pt(10)
        return p

    # FASE 1
    add_section_header("FASE 1: PREPARACIÓN LOCAL EN EL MAC 🧑🏻‍🏫 TAREA TUYA")
    add_bullet("Escribe tu teoría, genera tus PDFs, graba los vídeos y organiza todo en la carpeta correspondiente de tu Mac.", "1.")
    add_bullet("Nombra los archivos correctamente (ej: T0.DEBATE.pdf, T2.VIDEO.mp4, etc.).", "2.")

    # FASE 2
    add_section_header("FASE 2: SINCRONIZACIÓN AL SERVIDOR (GITHUB) 🤖 TAREA DE LA IA")
    p_f2 = doc.add_paragraph()
    r_f2 = p_f2.add_run("Tú me dices: ")
    r_f2_q = p_f2.add_run('"Ya he metido todos los archivos nuevos en la carpeta del Mac, súbelos a GitHub".')
    r_f2_q.italic = True
    add_bullet("Añadir los archivos creados o modificados y hacer el commit.", "•")
    add_bullet("Subirlos a GitHub (git push origin main) en un único comando limpio.", "•")
    add_bullet("Objetivo: Alojarlos gratis en GitHub Pages para que Google Classroom pueda enlazarlos sin gastar espacio en tu Google Drive. Al editar un archivo, solo se resube a GitHub y se actualiza al instante para todos los alumnos.", "•")

    # FASE 3
    add_section_header("FASE 3: CREACIÓN DEL PANEL UNIFICADO DE ENLACES 🤖 TAREA DE LA IA")
    add_bullet("Yo (la IA) genero el archivo maestro CURSO_IA_UNIFICADO.csv (en PANELES_CSV/).", "•")
    add_bullet("Arquitectura de Mapa Único: En lugar de saturar Classroom con docenas de enlaces sueltos, cada sección cuenta con un Mapa Interactivo HTML único (MAPA_MONOGRAFICOS.html y MAPA_SESION_XX.html) que agrupa fichas, simuladores y recursos interactivos sin rehacer publicaciones en Classroom.", "•")

    # FASE 4
    add_section_header("FASE 4: PREPARACIÓN DE GOOGLE CLASSROOM 🧑🏻‍🏫 TAREA TUYA")
    add_bullet("Entra en classroom.google.com con tu cuenta de profesor.", "1.")
    add_bullet("Trabajamos exclusivamente con las Clases Maestras Unificadas Anuales:", "2.")
    
    # Tabla de IDs vigentes
    tbl_ids = doc.add_table(rows=3, cols=3)
    tbl_ids.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["CURSO", "NOMBRE EN CLASSROOM", "ID REAL DE LA CLASE"]
    for c_idx, h in enumerate(headers):
        cell = tbl_ids.cell(0, c_idx)
        set_cell_background(cell, "0284C7")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

    datos_clases = [
        ("INTELIGENCIA ARTIFICIAL", "IA.", "890436514251"),
        ("ROBÓTICA", "ROBÓTICA.", "890435922022")
    ]
    for r_idx, (curso, nombre, id_real) in enumerate(datos_clases, start=1):
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate([curso, nombre, id_real]):
            cell = tbl_ids.cell(r_idx, c_idx)
            set_cell_background(cell, bg)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.size = Pt(9.5)
            if c_idx == 2:
                r.bold = True
                r.font.color.rgb = RGBColor(16, 185, 129)

    doc.add_paragraph()

    # FASE 5
    add_section_header("FASE 5: INGESTA DE DATOS (GOOGLE SHEETS) 🧑🏻‍🏫 TAREA TUYA")
    add_bullet("Abre tu navegador en Modo Incógnito / Ventana Privada (vital para evitar conflictos entre cuentas de Google).", "1.")
    add_bullet("Entra a Google Drive y abre tu hoja de cálculo permanente: 0.PANEL_CLASSROOM.", "2.")
    add_bullet("Ve a Archivo > Importar > Subir y arrastra PANELES_CSV/CURSO_IA_UNIFICADO.csv.", "3.")
    add_bullet("Selecciona 'Reemplazar hoja de cálculo actual' y pulsa Importar.", "4.")
    add_bullet("En la Columna A (ID_CURSO), pega el ID real: 890436514251 y arrastra hacia abajo para que todas las filas tengan el ID.", "5.")

    # FASE 6
    add_section_header("FASE 6: PUBLICACIÓN AUTOMÁTICA 🧑🏻‍🏫 TAREA TUYA")
    add_bullet("Dentro de la hoja de Google Sheets, ve a Extensiones > Apps Script.", "1.")
    add_bullet("Selecciona la función publicarTodoConTemas y pulsa Ejecutar.", "2.")
    add_bullet("El script creará automáticamente el tema MONOGRAFICOS y los temas SESIÓN 1 a SESIÓN 60 con sus respectivos mapas interactivos en modo BORRADOR (DRAFT).", "3.")
    add_bullet("¡Listo! Ya puedes ir publicando cada sesión a los alumnos conforme avance el calendario.", "4.")

    doc.add_paragraph()

    # ANEXO 1: EL BOTÓN DEL PÁNICO
    tbl_panic = doc.add_table(rows=1, cols=1)
    tbl_panic.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_panic = tbl_panic.cell(0, 0)
    set_cell_background(cell_panic, "FEF2F2")
    p_panic = cell_panic.paragraphs[0]
    p_panic.paragraph_format.space_before = Pt(6)
    p_panic.paragraph_format.space_after = Pt(6)
    p_panic.paragraph_format.left_indent = Inches(0.2)
    p_panic.paragraph_format.right_indent = Inches(0.2)
    
    r_p_title = p_panic.add_run("🚨 ANEXO 1: EL BOTÓN DEL PÁNICO (RESET COMPLETO DE CLASE)\n")
    r_p_title.bold = True
    r_p_title.font.color.rgb = RGBColor(220, 38, 38)
    r_p_text = p_panic.add_run(
        "Si la subida ha quedado desfasada o necesitas borrar TODO de Classroom para empezar de cero:\n"
        "1. Asegúrate de que el ID del curso está puesto en la celda A2 de la hoja: 890436514251.\n"
        "2. Ve a Extensiones > Apps Script, selecciona la función borrarAbsolutamenteTodo y pulsa Ejecutar.\n"
        "3. Toda la clase (Temas, Materiales y Borradores) quedará completamente vacía en segundos."
    )
    r_p_text.font.size = Pt(9.5)

    doc.add_paragraph()

    # ANEXO 2: LISTADO DE FÓSILES
    add_section_header("📋 ANEXO 2: HISTORIAL DE CLASES ANTERIORES (ARCHIVADAS / FÓSILES)")
    fosiles = [
        ("IA.MONOGRÁFICOS", "877999132773"),
        ("IA1 (Sesiones 01 a 15)", "826134766630"),
        ("IA2 (Sesiones 16 a 30)", "877174620039"),
        ("IA3 (Sesiones 31 a 45)", "877172188045"),
        ("IA4 (Sesiones 46 a 60)", "826136245220"),
        ("IA.ÍNDICE", "877993104492"),
        ("ROB+IA. Introducción", "876317836453"),
        ("ROB1 a ROB7 (Bloques 1 a 7)", "876316970006 al 869853775914"),
    ]
    for nombre, id_f in fosiles:
        add_bullet(f"{nombre}  --->  ID HISTÓRICO: {id_f}", "•")

    # Guardar DOCX
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc.save(output_path)
    print(f"✅ Microsoft Word DOCX certificado generado con éxito: {output_path}")

def create_pdf(output_path):
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=40, leftMargin=40, topMargin=30, bottomMargin=30
    )
    styles = getSampleStyleSheet()

    style_title = ParagraphStyle(
        'DocTitle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=18, leading=22,
        textColor=colors.HexColor('#0284C7'), alignment=1, spaceAfter=4
    )
    style_sub = ParagraphStyle(
        'DocSub', parent=styles['Normal'],
        fontName='Helvetica-Oblique', fontSize=10, leading=13,
        textColor=colors.HexColor('#64748B'), alignment=1, spaceAfter=14
    )
    style_h2 = ParagraphStyle(
        'DocH2', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=12, leading=15,
        textColor=colors.HexColor('#0F172A'), spaceBefore=12, spaceAfter=4
    )
    style_body = ParagraphStyle(
        'DocBody', parent=styles['Normal'],
        fontName='Helvetica', fontSize=9, leading=12.5,
        textColor=colors.HexColor('#1E293B'), spaceAfter=4
    )
    style_alert = ParagraphStyle(
        'DocAlert', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5, leading=11.5,
        textColor=colors.HexColor('#991B1B')
    )

    story = [
        Paragraph("GUÍA DE PUBLICACIÓN EN GITHUB Y CLASSROOM", style_title),
        Paragraph("Workflow de Trabajo en Equipo: Tú (Profesor) y Antigravity (Asistente IA)", style_sub),
        HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284C7'), spaceAfter=10),
        
        # Info Box
        Table([[Paragraph("<b>💡 INTRODUCCIÓN AL SISTEMA UNIFICADO:</b><br/>Este flujo de trabajo garantiza que todo el material educativo viaje desde tu Mac hasta Google Classroom sin coste de almacenamiento en Google Drive mediante <b>Mapas Interactivos HTML únicos</b>.", style_body)]],
              colWidths=[530], style=[
                  ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
                  ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#BAE6FD')),
                  ('TOPPADDING', (0,0), (-1,-1), 8),
                  ('BOTTOMPADDING', (0,0), (-1,-1), 8),
                  ('LEFTPADDING', (0,0), (-1,-1), 12),
                  ('RIGHTPADDING', (0,0), (-1,-1), 12),
              ]),
        Spacer(1, 10),

        Paragraph("FASE 1: PREPARACIÓN LOCAL EN EL MAC 🧑🏻‍🏫 TAREA TUYA", style_h2),
        Paragraph("1. Escribe tu teoría, genera tus PDFs, graba los vídeos y organiza todo en la carpeta correspondiente de tu Mac.", style_body),
        Paragraph("2. Nombra los archivos correctamente (ej: <code>T0.DEBATE.pdf</code>, <code>T2.VIDEO.mp4</code>, etc.).", style_body),

        Paragraph("FASE 2: SINCRONIZACIÓN AL SERVIDOR (GITHUB) 🤖 TAREA DE LA IA", style_h2),
        Paragraph("Tú me dices: <i>'Ya he metido todos los archivos nuevos en la carpeta del Mac, súbelos a GitHub'</i>.", style_body),
        Paragraph("Yo (la IA) me encargo de añadir los archivos, hacer el commit y subirlos a la nube (<code>git push</code>) en un único comando limpio.", style_body),
        Paragraph("<b>Objetivo:</b> Alojarlos gratis en GitHub Pages para enlazarlos desde Classroom sin gastar espacio en tu Google Drive.", style_body),

        Paragraph("FASE 3: CREACIÓN DEL PANEL UNIFICADO DE ENLACES 🤖 TAREA DE LA IA", style_h2),
        Paragraph("Yo (la IA) escaneo las carpetas y genero el archivo maestro <b><code>CURSO_IA_UNIFICADO.csv</code></b> (en <code>PANELES_CSV/</code>).", style_body),
        Paragraph("<b>Arquitectura de Mapa Único:</b> En lugar de saturar Classroom con docenas de enlaces sueltos, cada sección cuenta con un <b>Mapa Interactivo HTML único</b> (<code>MAPA_MONOGRAFICOS.html</code> y <code>MAPA_SESION_XX.html</code>).", style_body),

        Paragraph("FASE 4: PREPARACIÓN DE GOOGLE CLASSROOM 🧑🏻‍🏫 TAREA TUYA", style_h2),
        Paragraph("Entra en <code>classroom.google.com</code> con tu cuenta de profesor. Trabajamos con las <b>Clases Maestras Unificadas Anuales</b>:", style_body),
        Spacer(1, 4),
        Table([
            [Paragraph("<b>CURSO</b>", style_body), Paragraph("<b>NOMBRE EN CLASSROOM</b>", style_body), Paragraph("<b>ID REAL DE LA CLASE</b>", style_body)],
            [Paragraph("INTELIGENCIA ARTIFICIAL", style_body), Paragraph("<b>IA.</b>", style_body), Paragraph("<b>890436514251</b>", style_body)],
            [Paragraph("ROBÓTICA", style_body), Paragraph("<b>ROBÓTICA.</b>", style_body), Paragraph("<b>890435922022</b>", style_body)],
        ], colWidths=[180, 170, 180], style=[
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0284C7')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
            ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#F8FAFC')),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ]),
        Spacer(1, 10),

        Paragraph("FASE 5: INGESTA DE DATOS (GOOGLE SHEETS) 🧑🏻‍🏫 TAREA TUYA", style_h2),
        Paragraph("1. Abre tu navegador en <b>Modo Incógnito / Ventana Privada</b> (evita conflictos entre cuentas de Google).", style_body),
        Paragraph("2. Entra a Google Drive y abre tu hoja permanente: <b><code>0.PANEL_CLASSROOM</code></b>.", style_body),
        Paragraph("3. Ve a <b>Archivo > Importar > Subir</b> y arrastra <b><code>PANELES_CSV/CURSO_IA_UNIFICADO.csv</code></b>.", style_body),
        Paragraph("4. Selecciona <b>Reemplazar hoja de cálculo actual</b> y pulsa Importar.", style_body),
        Paragraph("5. En la <b>Columna A (<code>ID_CURSO</code>)</b>, pega el ID <b><code>890436514251</code></b> y arrástralo hacia abajo.", style_body),

        Paragraph("FASE 6: PUBLICACIÓN AUTOMÁTICA 🧑🏻‍🏫 TAREA TUYA", style_h2),
        Paragraph("1. En la hoja de Google Sheets, ve a <b>Extensiones > Apps Script</b>.", style_body),
        Paragraph("2. Selecciona la función <b><code>publicarTodoConTemas</code></b> y pulsa <b>Ejecutar</b>.", style_body),
        Paragraph("3. El script creará automáticamente el tema <code>MONOGRAFICOS</code> y los temas <code>SESIÓN 1</code> a <code>SESIÓN 60</code> con sus mapas interactivos en modo BORRADOR (DRAFT).", style_body),

        Spacer(1, 10),
        # Alert Box
        Table([[Paragraph("<b>🚨 ANEXO 1: EL BOTÓN DEL PÁNICO (RESET COMPLETO DE CLASE)</b><br/>"
                          "Si necesitas borrar TODO de Classroom para empezar de cero:<br/>"
                          "1. Asegúrate de que el ID está puesto en la celda <b>A2</b> de la hoja: <b>890436514251</b>.<br/>"
                          "2. En Apps Script, selecciona la función <b><code>borrarAbsolutamenteTodo</code></b> y pulsa <b>Ejecutar</b>.<br/>"
                          "3. Toda la clase quedará completamente limpia en segundos.", style_alert)]],
              colWidths=[530], style=[
                  ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FEF2F2')),
                  ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#FCA5A5')),
                  ('TOPPADDING', (0,0), (-1,-1), 8),
                  ('BOTTOMPADDING', (0,0), (-1,-1), 8),
                  ('LEFTPADDING', (0,0), (-1,-1), 12),
                  ('RIGHTPADDING', (0,0), (-1,-1), 12),
              ]),
    ]
    doc.build(story)
    print(f"✅ Guía en PDF generada con éxito: {output_path}")

def main():
    dest_docx_comun = os.path.join(COMUN_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.docx")
    dest_docx_ia = os.path.join(IA_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.docx")
    dest_pdf_comun = os.path.join(COMUN_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.pdf")
    dest_pdf_ia = os.path.join(IA_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.pdf")

    create_word_docx(dest_docx_comun)
    create_word_docx(dest_docx_ia)
    create_pdf(dest_pdf_comun)
    create_pdf(dest_pdf_ia)

if __name__ == "__main__":
    main()

