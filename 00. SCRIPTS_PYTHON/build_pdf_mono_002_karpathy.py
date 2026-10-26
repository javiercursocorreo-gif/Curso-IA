#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_mono_002_karpathy.py
Genera la Ficha Didáctica Oficial del Alumno (A4):
MONO-002_Los_4_Trucos_de_Prompting_de_Karpathy.pdf
Para el Monográfico de Prompting Avanzado (Técnicas Karpathy).
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
OUTPUT_DIR = os.path.join(BASE_DIR, "CLASES", "MONO_002_PROMPTING_KARPATHY")
PDF_PATH = os.path.join(OUTPUT_DIR, "MONO-002_Los_4_Trucos_de_Prompting_de_Karpathy.pdf")

def build_mono_002_pdf(output_path=PDF_PATH):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    )
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    PAGE_WIDTH = A4[0] - 72 # 523.27 pt

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=36, leftMargin=36, topMargin=24, bottomMargin=22
    )
    styles = getSampleStyleSheet()

    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.0,
        textColor=colors.HexColor('#0284C7'), alignment=1, spaceAfter=2
    )
    style_block = ParagraphStyle(
        'BlockStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.5,
        textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=4
    )
    style_title = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=12.0, leading=15.0,
        textColor=colors.HexColor('#0F172A'), spaceAfter=4
    )
    style_section_h = ParagraphStyle(
        'SectionHStyle', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=8.8, leading=11.5,
        textColor=colors.HexColor('#0369A1'), spaceBefore=4, spaceAfter=2
    )
    style_body = ParagraphStyle(
        'BodyStyle', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=8.0, leading=11.0,
        textColor=colors.HexColor('#1E293B'), spaceAfter=3
    )
    style_task = ParagraphStyle(
        'TaskStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.6, leading=10.2,
        textColor=colors.HexColor('#1E293B')
    )
    style_prompt = ParagraphStyle(
        'PromptStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.3, leading=9.8,
        textColor=colors.HexColor('#0F172A')
    )

    story = []

    # Cabecera
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL &bull; MONOGRAFICOS ESPECIALES", style_header))
    story.append(Paragraph("TALLER PRACTICO: DOMINA EL PROMPTING SIN MUROS DE TEXTO", style_block))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#0284C7'), spaceAfter=4))

    # Titulo
    story.append(Paragraph("<b>[MONO-002] Los 4 Super-Trucos de Prompting de Andrej Karpathy</b>", style_title))

    # Mision
    story.append(Paragraph("<b>Mision Didactica &bull; De Sufrir Muros de Texto a Controlar la IA con Precision:</b>", style_section_h))
    story.append(Paragraph(
        "Muchos usuarios se frustran porque la IA responde con 6 parrafos interminables llenos de rodeos y lenguaje abstracto. "
        "En este taller aprenderas los <b>4 trucos maestros revelados por Andrej Karpathy</b> (cofundador de OpenAI) para exigirle a Gemini "
        "instrucciones directas estilo manual aeronautico, diagramas visuales en 50 milisegundos, aplicaciones interactivas en tu navegador y explicaciones de documental.",
        style_body
    ))

    # Checklist de tareas
    story.append(Paragraph("<b>Lista de Tareas del Alumno (Paso a Paso en Pantalla):</b>", style_section_h))
    task_rows = [
        [Paragraph("<b>[Paso 1] Abre el Estudio Interactivo de Prompting:</b> Abre en tu navegador el archivo oficial <i>ESTUDIO_PROMPTING_KARPATHY.html</i> para probar en directo los 4 modos de Karpathy.", style_task)],
        [Paragraph("<b>[Paso 2] Prueba el Filtro ASD-STE100 (Cero Paja):</b> Selecciona el Truco 1, copia el prompt maestro y pegalo en Gemini. Comprueba como la respuesta se reduce a ordenes directas de menos de 20 palabras.", style_task)],
        [Paragraph("<b>[Paso 3] Pide un Diagrama Visual Directo en el Chat:</b> Activa el Truco 2. Pídele a Gemini que dibuje un esquema visual en arte de texto con cajas [ ], rombos y flechas para verlo directamente en la conversación sin usar ningún visor.", style_task)],
        [Paragraph("<b>[Paso 4] Crea y Ejecuta tu Micro-App HTML:</b> Activa el Truco 3. Pide a Gemini el código de una calculadora o temporizador y, en el siguiente mensaje, dile: <i>«¡Ejecuta este código en pantalla!»</i> para probarla directamente en el chat, o guárdala como <i>.html</i> en tu Mac.", style_task)],
        [Paragraph("<b>[Paso 5] Modo Documental 3Blue1Brown:</b> Activa el Truco 4 y pidele a Gemini que te explique como viaja el GPS como si fuera un guion cinematografico con 3 analogias visuales.", style_task)],
    ]
    t_table = Table(task_rows, colWidths=[PAGE_WIDTH])
    t_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0284C7')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_table)
    story.append(Spacer(1, 4))

    # Recuadro Prompt Maestro
    story.append(Paragraph("<b>Prompt Maestro Comodin para Copiar y Pegar en Gemini / ChatGPT:</b>", style_section_h))
    prompt_text = (
        "<b>Copia este prompt maestro comodin para ordenar a la IA que deje de dar rodeos:</b><br/>"
        "<i>\"Actua como un redactor tecnico bajo el estandar aeronautico 80% ASD-STE100.<br/>"
        "Responde a mi consulta siguiendo estas 4 reglas obligatorias:<br/>"
        "1. Maximo 20 palabras por instruccion y uso estricto del modo imperativo ('Haz esto', no 'Se recomienda').<br/>"
        "2. Cero rodeos, cero saludos y cero textos de relleno o introducciones obvias.<br/>"
        "3. Si el proceso tiene fases, incluye un diagrama de flujo esquematico antes del texto.<br/>"
        "4. Si involucra calculos o formulas, entrega el codigo de una mini-aplicacion interactiva en un unico archivo HTML con modo oscuro y botones accesibles para usarla en mi navegador.<br/>"
        "Mi consulta es: [Escribe aqui lo que necesitas resolver]\"</i>"
    )
    p_table = Table([[Paragraph(prompt_text, style_prompt)]], colWidths=[PAGE_WIDTH])
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFBEB')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#D97706')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(p_table)
    story.append(Spacer(1, 4))

    # Tabla Resumen de los 4 Trucos
    story.append(Paragraph("<b>Ficha Tecnica de los 4 Trucos de Karpathy:</b>", style_section_h))
    summary_data = [
        [Paragraph("<b>TRUCO MAESTRO</b>", style_task), Paragraph("<b>REGLA OPERATIVA DE PROMPT</b>", style_task), Paragraph("<b>BENEFICIO PARA EL ALUMNO</b>", style_task)],
        [
            Paragraph("<b>1. Filtro ASD-STE100</b>", style_task),
            Paragraph("Pide <i>«80% ASD-STE100, frases &lt;20 palabras y modo imperativo»</i>.", style_task),
            Paragraph("Elimina el 100% de la palabreria inutil y ofrece ordenes claras.", style_task)
        ],
        [
            Paragraph("<b>2. Diagramas Visuales</b>", style_task),
            Paragraph("Pide <i>«Dibuja un diagrama en arte de texto con cajas [ ], rombos y flechas | y v»</i>.", style_task),
            Paragraph("Esquema visual dibujado directamente en el chat en 50 milisegundos sin visores.", style_task)
        ],
        [
            Paragraph("<b>3. Micro-Apps HTML</b>", style_task),
            Paragraph("Pide la app y luego dile en el paso 2: <i>«¡Ejecuta este código en pantalla!»</i>.", style_task),
            Paragraph("Prueba la herramienta interactiva directamente en el chat de Gemini o en tu Mac.", style_task)
        ],
        [
            Paragraph("<b>4. Modo 3Blue1Brown</b>", style_task),
            Paragraph("Pide <i>«Guion divulgativo con 1 enigma inicial y 3 analogias visuales»</i>.", style_task),
            Paragraph("Hace comprensible cualquier tema cientifico o tecnologico complejo.", style_task)
        ],
    ]
    s_table = Table(summary_data, colWidths=[120, 210, 193])
    s_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E2E8F0')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#94A3B8')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(s_table)

    doc.build(story)
    print(f"✅ PDF MONO-002 generado con éxito en: {output_path}")

if __name__ == '__main__':
    try:
        build_mono_002_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF MONO-002: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
