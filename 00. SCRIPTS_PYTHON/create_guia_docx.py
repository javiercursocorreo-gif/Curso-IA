#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
create_guia_docx.py
Genera 0.GUIA_PUBLICACION_GITHUB_CLASSROOM.docx y .rtf
en CURSO-ROBOTICA-IA-COMUN y CURSO-IA para que Microsoft Word
lo abra perfectamente sin errores de formato.
"""

import os
import sys
import zipfile

COMUN_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-ROBOTICA-IA-COMUN"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IA_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

DOCX_CONTENT = [
    ("TITLE", "GUÍA DE PUBLICACIÓN EN GITHUB Y CLASSROOM (Workflow de Trabajo en Equipo)"),
    ("SUBTITLE", "Flujo de trabajo para Tú (el Profesor) y Antigravity (tu asistente IA)"),
    ("HEADING", "FASE 1: PREPARACIÓN LOCAL EN EL MAC 🧑🏻‍🏫 TAREA TUYA"),
    ("BODY", "1. Escribe tu teoría, genera tus PDFs, graba los vídeos y organiza todo en la carpeta correspondiente de tu Mac."),
    ("BODY", "2. Nombra los archivos correctamente (ej: T0.DEBATE.pdf, T2.VIDEO.mp4, etc.)."),
    ("HEADING", "FASE 2: SINCRONIZACIÓN AL SERVIDOR (GITHUB) 🤖 TAREA DE LA IA"),
    ("BODY", "Tú me dices: 'Ya he metido todos los archivos nuevos en la carpeta del Mac, súbelos a GitHub'."),
    ("BODY", "Yo (la IA) me encargo de: Añadir los archivos, hacer el commit y enviarlos a la nube (git push) mediante el bloque de comandos correlativo."),
    ("BODY", "Objetivo: Alojarlos gratis en internet para que Google Classroom pueda enlazarlos sin gastar espacio en tu Google Drive. Si algún día editas un PDF que ya subimos, solo tienes que pedirme que lo vuelva a subir y se actualizará automáticamente para todos tus alumnos sin tocar Classroom."),
    ("HEADING", "FASE 3: CREACIÓN DEL PANEL UNIFICADO DE ENLACES 🤖 TAREA DE LA IA"),
    ("BODY", "Tú me dices: 'Genera el CSV unificado con los enlaces actualizados'."),
    ("BODY", "Yo (la IA) me encargo de escanear las carpetas y generar el archivo maestro CURSO_IA_UNIFICADO.csv (dentro de PANELES_CSV/)."),
    ("BODY", "Arquitectura de Mapa Único: En lugar de saturar Classroom con docenas de enlaces sueltos, cada sección cuenta con un Mapa Interactivo HTML único (MAPA_MONOGRAFICOS.html para todos los monográficos y MAPA_SESION_XX.html para cada sesión), que dan acceso dinámico a todos los materiales, talleres interactivos y fichas sin rehacer publicaciones en Classroom."),
    ("HEADING", "FASE 4: PREPARACIÓN DE GOOGLE CLASSROOM 🧑🏻‍🏫 TAREA TUYA"),
    ("BODY", "1. Entra en classroom.google.com con tu cuenta de profesor."),
    ("BODY", "2. Trabajamos con las Clases Maestras Unificadas Anuales:"),
    ("BODY", "   • CLASE DE IA (Curso Completo Anual): IA. ---> ID REAL: 890436514251"),
    ("BODY", "   • CLASE DE ROBÓTICA (Curso Completo Anual): ROBÓTICA. ---> ID REAL: 890435922022"),
    ("HEADING", "FASE 5: INGESTA DE DATOS (GOOGLE SHEETS) 🧑🏻‍🏫 TAREA TUYA"),
    ("BODY", "1. Abre tu navegador en Modo Incógnito / Ventana Privada (vital para evitar conflictos entre cuentas de Google)."),
    ("BODY", "2. Entra a Google Drive y abre tu hoja permanente: 0.PANEL_CLASSROOM."),
    ("BODY", "3. Ve a Archivo > Importar > Subir y arrastra el archivo maestro CURSO_IA_UNIFICADO.csv (de PANELES_CSV/)."),
    ("BODY", "4. Selecciona Reemplazar hoja de cálculo actual y pulsa Importar."),
    ("BODY", "5. En la Columna A (ID_CURSO), pega el ID real de la clase (890436514251) y arrastra el número hacia abajo para todas las filas."),
    ("HEADING", "FASE 6: PUBLICACIÓN AUTOMÁTICA 🧑🏻‍🏫 TAREA TUYA"),
    ("BODY", "1. Dentro de la hoja, ve a Extensiones > Apps Script."),
    ("BODY", "2. Selecciona la función publicarTodoConTemas y pulsa Ejecutar."),
    ("BODY", "3. El script creará automáticamente los Temas en Classroom (MONOGRAFICOS y SESIÓN 1 a 60) y cargará todos los mapas interactivos en modo BORRADOR (DRAFT)."),
    ("BODY", "4. ¡Listo! Ya puedes ir publicándolos a los alumnos según avance el calendario escolar."),
    ("HEADING", "🚨 ANEXO 1: EL BOTÓN DEL PÁNICO (RESET COMPLETO DE CLASE) 🧑🏻‍🏫 TAREA TUYA"),
    ("BODY", "Si necesitas borrar TODO de Classroom para empezar de cero:"),
    ("BODY", "1. Asegúrate de que el ID de la clase está puesto en la celda A2 de la hoja (ej: 890436514251)."),
    ("BODY", "2. Ve a Extensiones > Apps Script, selecciona la función borrarAbsolutamenteTodo y pulsa Ejecutar."),
    ("BODY", "3. Toda la clase (Temas, Materiales y Borradores) quedará borrada en segundos."),
    ("HEADING", "📋 ANEXO 2: LISTADO MAESTRO DE IDs DE TUS CLASES"),
    ("BODY", "CLASES MAESTRAS VIGENTES (MODELO UNIFICADO ANUAL):"),
    ("BODY", "  • IA (Curso Completo Anual) ---> ID REAL: 890436514251"),
    ("BODY", "  • ROBÓTICA (Curso Completo Anual) ---> ID REAL: 890435922022"),
    ("BODY", "HISTORIAL DE CLASES Y LOTES ANTERIORES (ARCHIVADAS / FÓSILES):"),
    ("BODY", "  • IA.MONOGRÁFICOS: ID REAL 877999132773"),
    ("BODY", "  • IA1 (Sesiones 01 a 15): ID REAL 826134766630"),
    ("BODY", "  • IA2 (Sesiones 16 a 30): ID REAL 877174620039"),
    ("BODY", "  • IA3 (Sesiones 31 a 45): ID REAL 877172188045"),
    ("BODY", "  • IA4 (Sesiones 46 a 60): ID REAL 826136245220"),
    ("BODY", "  • IA.ÍNDICE: ID REAL 877993104492"),
    ("BODY", "  • ROB+IA. Introducción: ID REAL 876317836453"),
    ("BODY", "  • Bloques Robótica 1 a 7: IDs 876316970006 al 869853775914"),
    ("HEADING", "⚙️ ANEXO 3: EL CÓDIGO MAESTRO DE APPS SCRIPT (Copia de Seguridad)"),
    ("BODY", "Consulta el código íntegro de dimeMisIDs(), publicarTodoConTemas() y borrarAbsolutamenteTodo() en el archivo .md y en la hoja de Google Sheets.")
]

def make_docx(output_path):
    # Generar un .docx 100% estándar y válido mediante paquete zip OOXML
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>"""

    rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

    # Construir párrafos XML
    p_xml = []
    for item_type, text in DOCX_CONTENT:
        safe_text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        if item_type == "TITLE":
            p_xml.append(f"""<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:before="240" w:after="120"/></w:pPr><w:r><w:rPr><w:b/><w:color w:val="0284C7"/><w:sz w:val="36"/></w:rPr><w:t>{safe_text}</w:t></w:r></w:p>""")
        elif item_type == "SUBTITLE":
            p_xml.append(f"""<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:after="240"/></w:pPr><w:r><w:rPr><w:i/><w:color w:val="64748B"/><w:sz w:val="22"/></w:rPr><w:t>{safe_text}</w:t></w:r></w:p>""")
        elif item_type == "HEADING":
            p_xml.append(f"""<w:p><w:pPr><w:spacing w:before="240" w:after="80"/></w:pPr><w:r><w:rPr><w:b/><w:color w:val="0F172A"/><w:sz w:val="26"/></w:rPr><w:t>{safe_text}</w:t></w:r></w:p>""")
        else:
            p_xml.append(f"""<w:p><w:pPr><w:spacing w:after="80"/></w:pPr><w:r><w:rPr><w:sz w:val="22"/></w:rPr><w:t>{safe_text}</w:t></w:r></w:p>""")

    body_xml = "".join(p_xml)
    document_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {body_xml}
    <w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/></w:sectPr>
  </w:body>
</w:document>"""

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/document.xml", document_xml)
    print(f"✅ Archivo Word DOCX generado con éxito: {output_path}")

def make_rtf(output_path):
    rtf_lines = [
        r"{\rtf1\ansi\deff0",
        r"{\fonttbl{\f0\fnil\fcharset0 Arial;}}",
        r"{\colortbl ;\red2\green132\blue199;\red15\green23\blue42;\red100\green116\blue139;}",
    ]
    for item_type, text in DOCX_CONTENT:
        safe_text = text.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")
        if item_type == "TITLE":
            rtf_lines.append(r"\pard\qc\sa200\b\fs32\cf1 " + safe_text + r"\par")
        elif item_type == "SUBTITLE":
            rtf_lines.append(r"\pard\qc\sa240\i\fs20\cf3 " + safe_text + r"\par")
        elif item_type == "HEADING":
            rtf_lines.append(r"\pard\ql\sb200\sa100\b\fs24\cf2 " + safe_text + r"\par")
        else:
            rtf_lines.append(r"\pard\ql\sa80\fs20\cf0 " + safe_text + r"\par")
    rtf_lines.append(r"}")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(rtf_lines))
    print(f"✅ Archivo RTF generado con éxito: {output_path}")

def main():
    targets = [
        os.path.join(COMUN_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.docx"),
        os.path.join(IA_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.docx"),
    ]
    targets_rtf = [
        os.path.join(COMUN_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.rtf"),
        os.path.join(IA_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.rtf"),
    ]

    for t in targets:
        make_docx(t)
    for r in targets_rtf:
        make_rtf(r)

if __name__ == "__main__":
    main()

