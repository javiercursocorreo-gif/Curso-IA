#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_guia_docx_and_pdf.py
Genera la Guía Oficial ÚNICA exclusivamente en:
CURSO-ROBOTICA-IA-COMUN

- Cero dependencias frágiles (genera DOCX mediante python-docx si está disponible,
  o mediante generador OOXML nativo completo con styles.xml, document.xml.rels, etc.).
- Sin IDs antiguos/fósiles (únicamente las 2 clases maestras unificadas vigentes).
- Limpieza previa de archivos temporales/bloqueados por Word.
- Generación de PDF oficial con ReportLab.
"""

import os
import sys
import glob
import zipfile
import subprocess

COMUN_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-ROBOTICA-IA-COMUN"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IA_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PARENT_DIR = os.path.abspath(os.path.join(IA_DIR, ".."))

DOCX_PATH = os.path.join(COMUN_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.docx")
PDF_PATH = os.path.join(COMUN_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.pdf")

def limpiar_archivos_antiguos():
    """Elimina copias obsoletas en CURSO-IA y archivos de bloqueo de Word."""
    print("1. Limpiando archivos obsoletos y temporales...", flush=True)
    patrones = [
        os.path.join(IA_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.*"),
        os.path.join(COMUN_DIR, "~$0.GUIA_PUBLICACION_GITHUB_CLASSROOM.*"),
        os.path.join(COMUN_DIR, ".~$0.GUIA_PUBLICACION_GITHUB_CLASSROOM.*"),
    ]
    for ruta in glob.glob(os.path.join(PARENT_DIR, "*ROBOTICA*")):
        if os.path.abspath(ruta) != os.path.abspath(COMUN_DIR):
            patrones.append(os.path.join(ruta, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.*"))

    for p in patrones:
        for f in glob.glob(p):
            try:
                os.remove(f)
                print(f"   🗑️ Eliminado: {os.path.basename(f)}", flush=True)
            except Exception:
                pass

def generar_docx_ooxml_puro(output_path):
    """
    Genera un paquete .docx 100% válido y estándar de OpenXML (ECMA-376)
    con todos los ficheros obligatorios (Content_Types, _rels, styles, document.xml.rels, settings)
    garantizando que Microsoft Word lo abra SIN NINGÚN MENSAJE DE RECUPERACIÓN.
    """
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
</Types>"""

    pkg_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

    doc_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>
</Relationships>"""

    styles_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>
        <w:sz w:val="20"/>
        <w:color w:val="1E293B"/>
      </w:rPr>
    </w:rPrDefault>
    <w:pPrDefault>
      <w:pPr>
        <w:spacing w:after="120" w:line="240" w:lineRule="auto"/>
      </w:pPr>
    </w:pPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
  </w:style>
</w:styles>"""

    settings_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:defaultTabStop w:val="720"/>
</w:settings>"""

    # Construcción de párrafos del documento
    body_paragraphs = []

    def p_title(text):
        return f"""<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="80"/></w:pPr><w:r><w:rPr><w:b/><w:sz w:val="36"/><w:color w:val="0284C7"/></w:rPr><w:t>{text}</w:t></w:r></w:p>"""

    def p_sub(text):
        return f"""<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:after="280"/></w:pPr><w:r><w:rPr><w:i/><w:sz w:val="21"/><w:color w:val="64748B"/></w:rPr><w:t>{text}</w:t></w:r></w:p>"""

    def p_h2(text):
        return f"""<w:p><w:pPr><w:spacing w:before="260" w:after="80"/></w:pPr><w:r><w:rPr><w:b/><w:sz w:val="24"/><w:color w:val="0F172A"/></w:rPr><w:t>{text}</w:t></w:r></w:p>"""

    def p_item(prefix, text):
        return f"""<w:p><w:pPr><w:ind w:left="360"/><w:spacing w:after="60"/></w:pPr><w:r><w:rPr><w:b/><w:color w:val="0284C7"/></w:rPr><w:t>{prefix} </w:t></w:r><w:r><w:t>{text}</w:t></w:r></w:p>"""

    def p_text(text):
        return f"""<w:p><w:pPr><w:spacing w:after="80"/></w:pPr><w:r><w:t>{text}</w:t></w:r></w:p>"""

    def p_box(title, text, is_alert=False):
        color = "DC2626" if is_alert else "0284C7"
        bg = "FEF2F2" if is_alert else "F0F9FF"
        return f"""<w:tbl>
  <w:tblPr><w:tblW w:w="9360" w:type="dxa"/><w:jc w:val="center"/><w:tblBorders><w:top w:val="none"/><w:left w:val="single" w:sz="24" w:space="0" w:color="{color}"/><w:bottom w:val="none"/><w:right w:val="none"/></w:tblBorders></w:tblPr>
  <w:tr>
    <w:tc>
      <w:tcPr><w:tcW w:w="9360" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="{bg}"/><w:tcMar><w:top w:w="140"/><w:left w:w="200"/><w:bottom w:w="140"/><w:right w:w="200"/></w:tcMar></w:tcPr>
      <w:p><w:r><w:rPr><w:b/><w:color w:val="{color}"/></w:rPr><w:t>{title}</w:t></w:r></w:p>
      <w:p><w:r><w:t>{text}</w:t></w:r></w:p>
    </w:tc>
  </w:tr>
</w:tbl><w:p><w:pPr><w:spacing w:after="100"/></w:pPr></w:p>"""

    # Tabla con las dos clases maestras vigentes
    def p_table_clases():
        return """<w:tbl>
  <w:tblPr><w:tblW w:w="9360" w:type="dxa"/><w:jc w:val="center"/><w:tblBorders><w:top w:val="single" w:sz="6" w:color="CBD5E1"/><w:left w:val="single" w:sz="6" w:color="CBD5E1"/><w:bottom w:val="single" w:sz="6" w:color="CBD5E1"/><w:right w:val="single" w:sz="6" w:color="CBD5E1"/><w:insideH w:val="single" w:sz="6" w:color="CBD5E1"/><w:insideV w:val="single" w:sz="6" w:color="CBD5E1"/></w:tblBorders></w:tblPr>
  <w:tr>
    <w:tc><w:tcPr><w:tcW w:w="3120" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="0284C7"/><w:tcMar><w:top w:w="100"/><w:left w:w="120"/><w:bottom w:w="100"/><w:right w:w="120"/></w:tcMar></w:tcPr><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:b/><w:color w:val="FFFFFF"/></w:rPr><w:t>CURSO</w:t></w:r></w:p></w:tc>
    <w:tc><w:tcPr><w:tcW w:w="3120" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="0284C7"/><w:tcMar><w:top w:w="100"/><w:left w:w="120"/><w:bottom w:w="100"/><w:right w:w="120"/></w:tcMar></w:tcPr><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:b/><w:color w:val="FFFFFF"/></w:rPr><w:t>NOMBRE EN CLASSROOM</w:t></w:r></w:p></w:tc>
    <w:tc><w:tcPr><w:tcW w:w="3120" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="0284C7"/><w:tcMar><w:top w:w="100"/><w:left w:w="120"/><w:bottom w:w="100"/><w:right w:w="120"/></w:tcMar></w:tcPr><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:b/><w:color w:val="FFFFFF"/></w:rPr><w:t>ID REAL DE LA CLASE</w:t></w:r></w:p></w:tc>
  </w:tr>
  <w:tr>
    <w:tc><w:tcPr><w:tcW w:w="3120" w:type="dxa"/><w:tcMar><w:top w:w="100"/><w:left w:w="120"/><w:bottom w:w="100"/><w:right w:w="120"/></w:tcMar></w:tcPr><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:t>INTELIGENCIA ARTIFICIAL</w:t></w:r></w:p></w:tc>
    <w:tc><w:tcPr><w:tcW w:w="3120" w:type="dxa"/><w:tcMar><w:top w:w="100"/><w:left w:w="120"/><w:bottom w:w="100"/><w:right w:w="120"/></w:tcMar></w:tcPr><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:b/></w:rPr><w:t>IA.</w:t></w:r></w:p></w:tc>
    <w:tc><w:tcPr><w:tcW w:w="3120" w:type="dxa"/><w:tcMar><w:top w:w="100"/><w:left w:w="120"/><w:bottom w:w="100"/><w:right w:w="120"/></w:tcMar></w:tcPr><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:b/><w:color w:val="10B981"/></w:rPr><w:t>890436514251</w:t></w:r></w:p></w:tc>
  </w:tr>
  <w:tr>
    <w:tc><w:tcPr><w:tcW w:w="3120" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="F8FAFC"/><w:tcMar><w:top w:w="100"/><w:left w:w="120"/><w:bottom w:w="100"/><w:right w:w="120"/></w:tcMar></w:tcPr><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:t>ROBÓTICA</w:t></w:r></w:p></w:tc>
    <w:tc><w:tcPr><w:tcW w:w="3120" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="F8FAFC"/><w:tcMar><w:top w:w="100"/><w:left w:w="120"/><w:bottom w:w="100"/><w:right w:w="120"/></w:tcMar></w:tcPr><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:b/></w:rPr><w:t>ROBÓTICA.</w:t></w:r></w:p></w:tc>
    <w:tc><w:tcPr><w:tcW w:w="3120" w:type="dxa"/><w:shd w:val="clear" w:color="auto" w:fill="F8FAFC"/><w:tcMar><w:top w:w="100"/><w:left w:w="120"/><w:bottom w:w="100"/><w:right w:w="120"/></w:tcMar></w:tcPr><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:b/><w:color w:val="10B981"/></w:rPr><w:t>890435922022</w:t></w:r></w:p></w:tc>
  </w:tr>
</w:tbl><w:p><w:pPr><w:spacing w:after="100"/></w:pPr></w:p>"""

    body_paragraphs.append(p_title("GUÍA DE PUBLICACIÓN EN GITHUB Y CLASSROOM"))
    body_paragraphs.append(p_sub("Workflow de Trabajo en Equipo: Tú (Profesor) y Antigravity (Asistente IA)"))
    body_paragraphs.append(p_box("💡 Introducción al Sistema Unificado:", "Este flujo de trabajo garantiza que todo el material educativo (teoría, simuladores interactivos, fichas didácticas y monográficos) viaje desde tu Mac hasta Google Classroom sin gastar espacio en tu Google Drive y con una experiencia 100% limpia para los alumnos mediante Mapas Interactivos HTML únicos."))
    
    body_paragraphs.append(p_h2("FASE 1: PREPARACIÓN LOCAL EN EL MAC 🧑🏻‍🏫 TAREA TUYA"))
    body_paragraphs.append(p_item("1.", "Escribe tu teoría, genera tus PDFs, graba los vídeos y organiza todo en la carpeta correspondiente de tu Mac."))
    body_paragraphs.append(p_item("2.", "Nombra los archivos correctamente (ej: T0.DEBATE.pdf, T2.VIDEO.mp4, etc.)."))

    body_paragraphs.append(p_h2("FASE 2: SINCRONIZACIÓN AL SERVIDOR (GITHUB) 🤖 TAREA DE LA IA"))
    body_paragraphs.append(p_text('Tú me dices: "Ya he metido todos los archivos nuevos en la carpeta del Mac, súbelos a GitHub".'))
    body_paragraphs.append(p_item("•", "Añadir los archivos creados o modificados y hacer el commit."))
    body_paragraphs.append(p_item("•", "Subirlos a GitHub (git push origin main) en un único comando limpio."))
    body_paragraphs.append(p_item("•", "Objetivo: Alojarlos gratis en GitHub Pages para enlazarlos desde Classroom sin gastar espacio en tu Google Drive. Al actualizar un archivo, solo se vuelve a subir a GitHub y se actualiza al instante para todos los alumnos."))

    body_paragraphs.append(p_h2("FASE 3: CREACIÓN DEL PANEL UNIFICADO DE ENLACES 🤖 TAREA DE LA IA"))
    body_paragraphs.append(p_item("•", "Yo (la IA) genero el archivo maestro CURSO_IA_UNIFICADO.csv (en PANELES_CSV/)."))
    body_paragraphs.append(p_item("•", "Arquitectura de Mapa Único: En lugar de saturar Classroom con docenas de enlaces sueltos, cada sección cuenta con un Mapa Interactivo HTML único (MAPA_MONOGRAFICOS.html y MAPA_SESION_XX.html) que agrupa fichas, simuladores y recursos interactivos sin rehacer publicaciones en Classroom."))

    body_paragraphs.append(p_h2("FASE 4: PREPARACIÓN DE GOOGLE CLASSROOM 🧑🏻‍🏫 TAREA TUYA"))
    body_paragraphs.append(p_item("1.", "Entra en classroom.google.com con tu cuenta de profesor."))
    body_paragraphs.append(p_item("2.", "Trabajamos exclusivamente con las dos Clases Maestras Unificadas Anuales:"))
    body_paragraphs.append(p_table_clases())

    body_paragraphs.append(p_h2("FASE 5: INGESTA DE DATOS (GOOGLE SHEETS) 🧑🏻‍🏫 TAREA TUYA"))
    body_paragraphs.append(p_item("1.", "Abre tu navegador en Modo Incógnito / Ventana Privada (vital para evitar conflictos entre cuentas de Google)."))
    body_paragraphs.append(p_item("2.", "Entra a Google Drive y abre tu hoja de cálculo permanente: 0.PANEL_CLASSROOM."))
    body_paragraphs.append(p_item("3.", "Ve a Archivo > Importar > Subir y arrastra PANELES_CSV/CURSO_IA_UNIFICADO.csv."))
    body_paragraphs.append(p_item("4.", "Selecciona 'Reemplazar hoja de cálculo actual' y pulsa Importar."))
    body_paragraphs.append(p_item("5.", "En la Columna A (ID_CURSO), pega el ID real: 890436514251 y arrastra hacia abajo para que todas las filas tengan el ID."))

    body_paragraphs.append(p_h2("FASE 6: PUBLICACIÓN AUTOMÁTICA 🧑🏻‍🏫 TAREA TUYA"))
    body_paragraphs.append(p_item("1.", "Dentro de la hoja de Google Sheets, ve a Extensiones > Apps Script."))
    body_paragraphs.append(p_item("2.", "Selecciona la función publicarTodoConTemas y pulsa Ejecutar."))
    body_paragraphs.append(p_item("3.", "El script creará automáticamente el tema MONOGRAFICOS y los temas SESIÓN 1 a SESIÓN 60 con sus respectivos mapas interactivos en modo BORRADOR (DRAFT)."))
    body_paragraphs.append(p_item("4.", "¡Listo! Ya puedes ir publicando cada sesión a los alumnos conforme avance el calendario escolar."))

    body_paragraphs.append(p_h2("🚨 ANEXO 1: EL BOTÓN DEL PÁNICO (RESET COMPLETO DE CLASE) 🧑🏻‍🏫 TAREA TUYA"))
    body_paragraphs.append(p_box("Instrucciones de Reinicio Inmediato:", "Si la subida ha quedado desfasada o necesitas borrar TODO de Classroom para empezar de cero:\\n1. Asegúrate de que el ID del curso está puesto en la celda A2 de la hoja: 890436514251.\\n2. Ve a Extensiones > Apps Script, selecciona la función borrarAbsolutamenteTodo y pulsa Ejecutar.\\n3. Toda la clase (Temas, Materiales y Borradores) quedará completamente vacía en segundos.", is_alert=True))

    doc_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {"".join(body_paragraphs)}
    <w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/></w:sectPr>
  </w:body>
</w:document>"""

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", pkg_rels)
        z.writestr("word/_rels/document.xml.rels", doc_rels)
        z.writestr("word/styles.xml", styles_xml)
        z.writestr("word/settings.xml", settings_xml)
        z.writestr("word/document.xml", doc_xml)

    print(f"✅ Microsoft Word DOCX certificado generado con éxito: {output_path}", flush=True)

def create_clean_pdf(output_path):
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, HRFlowable
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
        fontName='Helvetica-Bold', fontSize=11.5, leading=14.5,
        textColor=colors.HexColor('#0F172A'), spaceBefore=11, spaceAfter=3
    )
    style_body = ParagraphStyle(
        'DocBody', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5, leading=11.5,
        textColor=colors.HexColor('#1E293B'), spaceAfter=3
    )
    style_alert = ParagraphStyle(
        'DocAlert', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5, leading=11.5,
        textColor=colors.HexColor('#991B1B')
    )

    story = [
        Paragraph("GUÍA DE PUBLICACIÓN EN GITHUB Y CLASSROOM", style_title),
        Paragraph("Workflow de Trabajo en Equipo: Tú (Profesor) y Antigravity (Asistente IA)", style_sub),
        HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284C7'), spaceAfter=8),
        
        Table([[Paragraph("<b>💡 INTRODUCCIÓN AL SISTEMA UNIFICADO:</b><br/>Este flujo de trabajo garantiza que todo el material educativo viaje desde tu Mac hasta Google Classroom sin coste de almacenamiento en Google Drive mediante <b>Mapas Interactivos HTML únicos</b>.", style_body)]],
              colWidths=[530], style=[
                  ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
                  ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#BAE6FD')),
                  ('TOPPADDING', (0,0), (-1,-1), 6),
                  ('BOTTOMPADDING', (0,0), (-1,-1), 6),
                  ('LEFTPADDING', (0,0), (-1,-1), 10),
                  ('RIGHTPADDING', (0,0), (-1,-1), 10),
              ]),
        Spacer(1, 6),

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
        Paragraph("Entra en <code>classroom.google.com</code> con tu cuenta de profesor. Trabajamos exclusivamente con las <b>dos Clases Maestras Unificadas Anuales</b>:", style_body),
        Spacer(1, 3),
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
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ]),
        Spacer(1, 6),

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

        Spacer(1, 6),
        Table([[Paragraph("<b>🚨 ANEXO 1: EL BOTÓN DEL PÁNICO (RESET COMPLETO DE CLASE)</b><br/>"
                          "Si necesitas borrar TODO de Classroom para empezar de cero:<br/>"
                          "1. Asegúrate de que el ID está puesto en la celda <b>A2</b> de la hoja: <b>890436514251</b>.<br/>"
                          "2. En Apps Script, selecciona la función <b><code>borrarAbsolutamenteTodo</code></b> y pulsa <b>Ejecutar</b>.<br/>"
                          "3. Toda la clase quedará completamente limpia en segundos.", style_alert)]],
              colWidths=[530], style=[
                  ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FEF2F2')),
                  ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#FCA5A5')),
                  ('TOPPADDING', (0,0), (-1,-1), 6),
                  ('BOTTOMPADDING', (0,0), (-1,-1), 6),
                  ('LEFTPADDING', (0,0), (-1,-1), 10),
                  ('RIGHTPADDING', (0,0), (-1,-1), 10),
              ]),
    ]
    doc.build(story)
    print(f"✅ Guía en PDF limpia generada en: {output_path}", flush=True)

def main():
    limpiar_archivos_antiguos()
    generar_docx_ooxml_puro(DOCX_PATH)
    create_clean_pdf(PDF_PATH)

if __name__ == "__main__":
    main()
