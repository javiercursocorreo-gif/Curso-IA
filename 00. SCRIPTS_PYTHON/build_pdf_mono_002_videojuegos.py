#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_mono_002_videojuegos.py
Genera la Ficha Didáctica Oficial del Monográfico 02 (Letter/A4):
MONO-002_Crea_Videojuegos_para_tus_Nietos_con_IA.pdf
para el Curso de IA para Adultos Mayores (60+).
Enfoque: El Prompt Maestro Universal, Diálogo con Gemini y Descarga de Archivo.
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
OUTPUT_DIR_CLASSROOM = os.path.join(BASE_DIR, "CLASES", "MONO_002_VIDEOJUEGOS")
os.makedirs(OUTPUT_DIR_CLASSROOM, exist_ok=True)

PDF_FILENAME = "MONO-002_Crea_Videojuegos_para_tus_Nietos_con_IA.pdf"
DEST_PATH = os.path.join(OUTPUT_DIR_CLASSROOM, PDF_FILENAME)

def build_pdf():
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    doc = SimpleDocTemplate(
        DEST_PATH,
        pagesize=letter,
        rightMargin=36, leftMargin=36, topMargin=22, bottomMargin=20
    )
    styles = getSampleStyleSheet()

    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.0,
        textColor=colors.HexColor('#6366F1'), alignment=1, spaceAfter=1
    )
    style_block = ParagraphStyle(
        'BlockStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.5,
        textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=3
    )
    style_title = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=11.5, leading=14.0,
        textColor=colors.HexColor('#0F172A'), spaceAfter=3
    )
    style_section_h = ParagraphStyle(
        'SectionHStyle', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=8.6, leading=11.0,
        textColor=colors.HexColor('#4338CA'), spaceBefore=3, spaceAfter=2
    )
    style_body = ParagraphStyle(
        'BodyStyle', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=7.8, leading=10.4,
        textColor=colors.HexColor('#1E293B'), spaceAfter=2
    )
    style_task = ParagraphStyle(
        'TaskStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.4, leading=9.6,
        textColor=colors.HexColor('#0F172A')
    )
    style_prompt = ParagraphStyle(
        'PromptStyle', parent=styles['Normal'],
        fontName='Courier', fontSize=6.8, leading=8.6,
        textColor=colors.HexColor('#0F172A')
    )

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("MONOGRÁFICOS ESPECIALES & CUADERNOS DE TALLER PRÁCTICO [MONO-002]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#6366F1'), spaceAfter=4))

    story.append(Paragraph("<b>[MONO-002] Crea Videojuegos con IA para tus Nietos: El Prompt Maestro y Creación en Gemini</b>", style_title))

    story.append(Paragraph("🎮 <b>Tú eres el Director Creativo y Gemini es tu Programador:</b>", style_section_h))
    story.append(Paragraph(
        "A petición de los alumnos de clase tras la sesión de robótica, en este taller aprendemos a crear videojuegos infantiles únicos y totalmente a medida con Inteligencia Artificial. "
        "No necesitas saber nada de código: el secreto consiste en guiar a Gemini con un <b>Prompt Maestro estructurado</b>, "
        "probar el juego en pantalla y pedirle mejoras hablando en español natural hasta que quede perfecto.",
        style_body
    ))

    # El Método en 4 Pasos
    story.append(Paragraph("📋 <b>El Método del Taller en 4 Pasos:</b>", style_section_h))
    steps_rows = [
        [Paragraph("<b>1. Diseña tu Idea y Rellena los [Corchetes]:</b> Abre la app del taller y define el nombre de tu nieto, la mecánica que imaginas (naves, comecocos, carreras, laberinto...) y tu mensaje de victoria.", style_task)],
        [Paragraph("<b>2. Copia tu Prompt Maestro a Gemini:</b> Entra en <i>gemini.google.com</i>, pega el texto y pulsa Enviar. La IA generará el juego completo e interactivo.", style_task)],
        [Paragraph("<b>3. Pruébalo y Habla con Gemini:</b> Juega directamente en pantalla. Pídele cambios como a un programador: <i>«Haz que vaya más lento»</i>, <i>«Añade música al ganar»</i> o <i>«Pon botones más grandes»</i>.", style_task)],
        [Paragraph("<b>4. Descárgalo y Guárdalo en tu PC:</b> Pulsa el botón <i>Descargar</i> en Gemini o usa el probador del curso para guardarlo como archivo <i>.html</i> y jugarlo siempre sin internet.", style_task)],
    ]
    st_table = Table(steps_rows, colWidths=[letter[0] - 72])
    st_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EEF2FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#6366F1')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(st_table)
    story.append(Spacer(1, 3))

    # El Prompt Maestro con Corchetes
    story.append(Paragraph("📝 <b>El Prompt Maestro Universal para Gemini (Rellena los [Corchetes]):</b>", style_section_h))

    prompt_content = (
        "Actúa como programador senior experto en videojuegos educativos para niños. Crea un juego completo, jugable al 100% y sin fallos, en UN ÚNICO ARCHIVO HTML autónomo (con CSS y JavaScript embebido) para mi nieto/a llamado <b>[NOMBRE DE TU NIETO/A]</b>.<br/><br/>"
        "<b>DATOS DEL JUEGO:</b><br/>"
        "• <b>MECÁNICA / TIPO DE JUEGO:</b> [ej. Nave espacial esquivando meteoritos / Perrito atrapando manzanas / Coche de carreras / Laberinto del tesoro / Comecocos en la granja...]<br/>"
        "• <b>PROTAGONISTA Y ELEMENTOS:</b> [ej. Nave 🚀, asteroides 🪨 y estrellas ⭐]<br/>"
        "• <b>OBJETIVO PARA GANAR:</b> [ej. Conseguir 10 puntos sin chocar con los obstáculos]<br/>"
        "• <b>MENSAJE DE VICTORIA DEL ABUELO:</b> \"[ej. ¡Eres un auténtico campeón! El abuelo te quiere con locura]\"<br/><br/>"
        "<b>REGLAS DE INGENIERÍA:</b><br/>"
        "1. <b>Controles duales:</b> Funciona con flechas del teclado (⬆️⬇️⬅️➡️ y WASD) y muestra una botonera táctil en cruz en pantalla.<br/>"
        "2. <b>Instrucciones en pantalla:</b> Cabecera clara explicando «🎯 CÓMO JUGAR: Objetivo...» y controles para que niños y abuelos lo entiendan de inmediato.<br/>"
        "3. <b>Estilo visual:</b> Fondo azul noche o colorido con contraste (prohibido fondo negro #000000). Usa emojis para los gráficos sin imágenes externas.<br/>"
        "4. <b>Pantalla de victoria:</b> Fanfarria sonora alegre (Web Audio API nativo), cartel gigante de felicitación y botón grande «¡Jugar Otra Vez!».<br/>"
        "5. Entrega exclusivamente el código completo dentro de un bloque HTML (desde &lt;!DOCTYPE html&gt; hasta &lt;/html&gt;)."
    )

    p_table = Table([[Paragraph(prompt_content, style_prompt)]], colWidths=[letter[0] - 72])
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#6366F1')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(p_table)
    story.append(Spacer(1, 3))

    # Ideas y Diálogo
    story.append(Paragraph("💡 <b>Ideas para tu Juego y Cómo Mejorarlo con Gemini:</b>", style_section_h))
    ideas_text = (
        "• <b>Ideas que encantan a los niños:</b> 🚀 <i>La Misión Espacial</i> (esquivar cometas), 🏎️ <i>El Circuito de Carreras</i> (esquivar charcos y sumar copas), 🏰 <i>El Laberinto</i> (buscar la llave dorada y abrir el cofre), 🐶 <i>La Merienda</i> (atrapar fresas o galletas), 🧠 <i>Trivial Familiar</i> (5 preguntas divertidas sobre anécdotas de los abuelos).<br/>"
        "• <b>Cómo afinar el juego hablando con Gemini:</b> Si algo no te convence, no reprogrames nada: dile a Gemini frases como <i>«Haz que los objetos caigan un poco más despacio para un niño de 6 años»</i>, <i>«Cambia el coche por una nave espacial»</i> o <i>«Ponle un sonido de campana cada vez que sume puntos»</i>."
    )
    story.append(Paragraph(ideas_text, style_body))
    story.append(Spacer(1, 2))

    # Cómo Guardarlo en el Ordenador
    story.append(Paragraph("💾 <b>Cómo Guardar el Archivo en tu Ordenador para Jugar Siempre:</b>", style_section_h))
    save_text = (
        "• <b>Método 1 (Directo desde Gemini):</b> En el bloque de código de Gemini pulsa el icono de <b>Descargar</b> (o cópialo).<br/>"
        "• <b>Método 2 (Con la App del Curso):</b> Abre el <i>Estudio de Videojuegos</i> en el mapa del curso, ve a la pestaña <b>«2. Probador Libre»</b>, pega el código y pulsa <b>«Guardar Archivo en mi Ordenador»</b>. "
        "Se descargará directamente el archivo <i>Juego_Para_Mi_Nieto.html</i> a tu carpeta de Descargas.<br/>"
        "• <b>A jugar:</b> Haz doble clic sobre el archivo y se abrirá en pantalla completa en Safari o Chrome, listo para jugar en familia sin necesidad de conexión a internet."
    )
    s_table = Table([[Paragraph(save_text, style_task)]], colWidths=[letter[0] - 72])
    s_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F5F3FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#8B5CF6')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(s_table)

    doc.build(story)
    print(f"✅ Ficha Didáctica PDF Oficial MONO-002 generada en:\n   {DEST_PATH}")

if __name__ == '__main__':
    build_pdf()
