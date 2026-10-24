#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_mono_002_videojuegos.py
Genera la Ficha Didáctica Oficial del Monográfico 02 (Letter/A4):
MONO-002_Crea_Videojuegos_para_tus_Nietos_con_IA.pdf
para el Curso de IA para Adultos Mayores (60+).
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
        fontName='Helvetica', fontSize=7.5, leading=9.8,
        textColor=colors.HexColor('#0F172A')
    )
    style_prompt = ParagraphStyle(
        'PromptStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.2, leading=9.3,
        textColor=colors.HexColor('#0F172A')
    )

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("MONOGRÁFICOS ESPECIALES & CUADERNOS DE TALLER PRÁCTICO [MONO-002]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#6366F1'), spaceAfter=4))

    story.append(Paragraph("<b>[MONO-002] Taller Especial: Crea Videojuegos para tus Nietos con IA (El Estudio Creativo)</b>", style_title))

    story.append(Paragraph("🎮 <b>El Regalo Más Mágico: Un Videojuego Diseñado por su Abuelo:</b>", style_section_h))
    story.append(Paragraph(
        "A petición de los alumnos de clase, en este taller especial descubrimos cómo convertirnos en directores de videojuegos para nuestros nietos. "
        "No necesitas saber nada de programación: mediante nuestro <b>Cuestionario Creativo</b> eliges el nombre de tu nieto, sus aficiones favoritas "
        "y el tipo de reto que le gusta. Puedes generar el juego personalizado de inmediato en 1 clic (100% garantizado) o usar la Inteligencia Artificial (Gemini) para crear variaciones.",
        style_body
    ))

    # El Método en 3 Pasos
    story.append(Paragraph("📋 <b>El Método Sencillo con Doble Salvaguarda en el Aula:</b>", style_section_h))
    steps_rows = [
        [Paragraph("<b>1. Responde al Cuestionario Creativo:</b> Abre la aplicación del taller y elige el protagonista, el tipo de juego y el premio.", style_task)],
        [Paragraph("<b>2. Pulsa «¡Crear mi Juego al Instante!» (100% Garantizado):</b> Tu juego personalizado se genera y arranca en 1 segundo en el navegador sin depender de la variabilidad de Gemini.", style_task)],
        [Paragraph("<b>3. O Experimenta con Gemini (Modo IA):</b> Si quieres explorar más, copia el <i>Prompt Maestro</i> a Gemini (<i>gemini.google.com</i>), pega el código en el Probador y descárgalo.", style_task)],
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

    # Los 4 Modelos Clásicos de Juego
    story.append(Paragraph("🌟 <b>Los 4 Tipos de Juegos que Puedes Crear:</b>", style_section_h))

    ex_rows = [
        [Paragraph("<b>🍎 Modelo 1 • Atrapa las Cosas que Caen (Cesta Móvil):</b> "
                   "Caen fresas, estrellas o balones desde arriba. El nieto mueve una cesta o personaje con las flechas o con el dedo en la tablet para atraparlos sumando puntos.<br/>"
                   "<i>Ideal para: Niños de 4 a 8 años. Reflejos rápidos, colores vivos y marcador de récord.</i>", style_prompt)],
        [Paragraph("<b>🏰 Modelo 2 • El Laberinto de Aventura y Tesoros:</b> "
                   "Un personaje (perrito, explorador o astronauta) recorre un mapa con pasillos sorteando obstáculos hasta encontrar la llave que abre el cofre secreto.<br/>"
                   "<i>Ideal para: Niños de 6 a 12 años. Fomenta la orientación espacial y la resolución de problemas con calma.</i>", style_prompt)],
        [Paragraph("<b>🐛 Modelo 3 • La Oruga Glotona (Estilo Serpiente Clásica):</b> "
                   "Una simpática oruga va comiendo frutas y creciendo en la pantalla sin chocar contra los bordes. El juego más adictivo y clásico de la historia.<br/>"
                   "<i>Ideal para: Toda la familia. Cada fruta suma puntos y la oruga cambia de colores divertidos.</i>", style_prompt)],
        [Paragraph("<b>🃏 Modelo 4 • Parejas de Memoria (Memory Familiar):</b> "
                   "12 cartas boca abajo en cuadrícula. El jugador levanta dos cartas buscando la pareja gemela (animales, coches o balones).<br/>"
                   "<i>Ideal para: Jugar abuelo y nieto por turnos en el mismo ordenador, entrenando la memoria visual y la agilidad mental.</i>", style_prompt)],
    ]

    p_table = Table(ex_rows, colWidths=[letter[0] - 72])
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#94A3B8')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(p_table)
    story.append(Spacer(1, 3))

    # La Caja de Herramientas del Taller
    story.append(Paragraph("🛠️ <b>Tu Caja de Herramientas para Este Monográfico:</b>", style_section_h))
    extra_text = (
        "• <b>Instrucciones Claras en Pantalla:</b> Cada juego generado muestra en su cabecera un recuadro vistoso con el <i>Objetivo</i> y los <i>Controles</i> para que niños y abuelos sepan exactamente cómo jugar sin perderse.<br/>"
        "• <b>La Aplicación del Taller (El Estudio Creativo):</b> Entra en la app interactiva en el cuadro de mandos del curso. "
        "Allí tienes el generador 100% directo, el generador de prompts y el <i>Probador en Vivo</i> con guía de juego integrada.<br/>"
        "• <b>Cómo llevárselo a casa:</b> En el Probador pulsa <b>«Guardar Archivo en mi Ordenador»</b>. Se descargará el archivo <i>Juego_Para_Mi_Nieto.html</i> en tu carpeta de Descargas para jugar offline."
    )
    e_table = Table([[Paragraph(extra_text, style_task)]], colWidths=[letter[0] - 72])
    e_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F5F3FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#6366F1')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(e_table)

    doc.build(story)
    print(f"✅ Ficha Didáctica PDF Oficial MONO-002 generada en:\n   {DEST_PATH}")

if __name__ == '__main__':
    build_pdf()

