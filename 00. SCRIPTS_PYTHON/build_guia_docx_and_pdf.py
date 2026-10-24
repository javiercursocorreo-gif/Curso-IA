#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_guia_docx_and_pdf.py
Genera la Guía Oficial ÚNICA exclusivamente en:
CURSO-ROBOTICA-IA-COMUN

Utiliza el motor nativo de macOS (/usr/bin/textutil) para compilar el .docx
a partir del HTML limpio, garantizando 100% de compatibilidad binaria con
Microsoft Word para Mac sin ningún diálogo de error ni recuperación.
Genera también la versión PDF oficial con ReportLab.
"""

import os
import sys
import glob
import subprocess

COMUN_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-ROBOTICA-IA-COMUN"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IA_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
PARENT_DIR = os.path.abspath(os.path.join(IA_DIR, ".."))

HTML_PATH = os.path.join(COMUN_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.html")
DOCX_PATH = os.path.join(COMUN_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.docx")
PDF_PATH = os.path.join(COMUN_DIR, "0.GUIA_PUBLICACION_GITHUB_CLASSROOM.pdf")

def limpiar_archivos_antiguos():
    """Elimina copias obsoletas en CURSO-IA y archivos de bloqueo."""
    print("1. Limpiando copias redundantes en cursos satélite...", flush=True)
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

def compilar_docx_nativo():
    """Compila el archivo HTML a DOCX usando el motor oficial de macOS textutil."""
    print("2. Compilando Microsoft Word DOCX nativo con textutil...", flush=True)
    cmd = [
        "/usr/bin/textutil",
        "-convert", "docx",
        "-output", DOCX_PATH,
        HTML_PATH
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"✅ Microsoft Word DOCX generado con éxito: {DOCX_PATH}", flush=True)
    else:
        print(f"⚠️ Error en textutil: {res.stderr}", flush=True)

def compilar_pdf():
    """Genera la versión PDF de alta legibilidad con ReportLab."""
    print("3. Compilando PDF oficial con ReportLab...", flush=True)
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    os.makedirs(os.path.dirname(PDF_PATH), exist_ok=True)
    doc = SimpleDocTemplate(
        PDF_PATH,
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
    print(f"✅ Guía en PDF limpia generada en: {PDF_PATH}", flush=True)

def main():
    limpiar_archivos_antiguos()
    compilar_docx_nativo()
    compilar_pdf()

if __name__ == "__main__":
    main()
