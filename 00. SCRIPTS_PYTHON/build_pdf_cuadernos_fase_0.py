#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_cuadernos_fase_0.py
Genera el PDF oficial de 1 SOLA PÁGINA (A4):
0. FASE_0_GUIA_CUADERNOS_GEMINI.pdf
en CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/01_Sesion/
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/01_Sesion"
PDF_PATH = os.path.join(OUTPUT_DIR, "0. FASE_0_GUIA_CUADERNOS_GEMINI.pdf")

ETIQUETAS = [
    ("[COMICS]", "CÓMICS", "Novelas gráficas, narrativa secuencial e historietas con IA."),
    ("[TXT]", "TEXTO", "Cartas formales, consultas, comparativas de compra y recetas de salud."),
    ("[EST]", "ESTILO", "Fotografía fotorrealista, acuarela, grabado, cine negro y texturas 3D."),
    ("[PRAC]", "PRÁCTICA", "Retos paso a paso y desafíos interactivos en clase con Gemini."),
    ("[ARTE]", "ARTE", "Obras maestras de la pinacoteca universal y análisis artístico."),
    ("[FRAC]", "FRACTALES", "Geometría en la naturaleza, biomimética y vídeos en alta definición."),
    ("[INT]", "INTERIOR", "Cortes transversales: arquitectura, monumentos y maquinaria por dentro."),
    ("[FUT]", "FUTURO", "Ciencia ficción, hábitats espaciales y robótica avanzada del mañana."),
    ("[NAT]", "NATURALEZA", "Biomecánica animal, aves del mundo y maravillas del reino natural."),
    ("[NIV]", "NIVELES", "Escalafones del conocimiento y clasificaciones universales (101)."),
    ("[TRUC]", "TRUCOS", "Remedios prácticos del hogar, bricolaje rápido y limpieza ecológica."),
    ("[PAT]", "PATRIMONIO", "Testamentos, herencias, derechos bancarios y vivienda clara 101."),
    ("[MOVIL]", "MÓVIL", "Símbolos de pantalla, salvavidas de configuración y cámara útil."),
    ("[MEM]", "MEMORIA", "Cápsula de recuerdos: lugares de infancia y objetos de época."),
    ("[MEC]", "MECÁNICA", "Engranajes, motores clásicos e inventos tecnológicos históricos.")
]

def build_pdf_reportlab():
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=A4,
        leftMargin=32,
        rightMargin=32,
        topMargin=26,
        bottomMargin=22
    )

    styles = getSampleStyleSheet()
    
    # Estilos
    style_header_title = ParagraphStyle(
        'HeaderTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12.5,
        leading=15,
        textColor=colors.white,
        alignment=1
    )
    style_header_sub = ParagraphStyle(
        'HeaderSub',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#7DD3FC'),
        alignment=1
    )
    style_callout_title = ParagraphStyle(
        'CalloutTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#0369A1')
    )
    style_callout_body = ParagraphStyle(
        'CalloutBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor('#334155')
    )
    style_tbl_head = ParagraphStyle(
        'TblHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white,
        alignment=1
    )
    style_tag = ParagraphStyle(
        'TagCol',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=9.5,
        textColor=colors.HexColor('#0284C7'),
        alignment=1
    )
    style_notebook = ParagraphStyle(
        'NotebookCol',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=9.5,
        textColor=colors.HexColor('#047857'),
        alignment=1
    )
    style_desc = ParagraphStyle(
        'DescCol',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#1E293B')
    )
    style_tip_title = ParagraphStyle(
        'TipTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#B45309')
    )
    style_tip_body = ParagraphStyle(
        'TipBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.3,
        leading=9.5,
        textColor=colors.HexColor('#78350F')
    )
    style_footer = ParagraphStyle(
        'FooterStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#64748B'),
        alignment=1
    )

    story = []

    # 1. Cabecera Banner
    header_content = [
        [Paragraph("FASE 0 • GUÍA METODOLÓGICA: TU SISTEMA DE CUADERNOS EN GEMINI", style_header_title)],
        [Paragraph("Organización de prácticas durante las 60 sesiones del Curso de Inteligencia Artificial", style_header_sub)]
    ]
    t_header = Table(header_content, colWidths=[531])
    t_header.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0F172A')),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_header)
    story.append(Spacer(1, 6))

    # 2. Caja Explicativa de Regla de Oro
    callout_html = (
        "<b>¿Por qué usamos Cuadernos? Regla de oro para trabajar en clase:</b><br/>"
        "• <b>1. Evitar el desorden:</b> Si abrimos un chat nuevo para cada práctica, al cabo de semanas quedarán perdidas en el historial.<br/>"
        "• <b>2. Reutilización continua:</b> Con Cuadernos agrupamos por temática. La 1ª vez que ves una etiqueta, creas su cuaderno; en las siguientes sesiones <b>¡lo reutilizas!</b><br/>"
        "• <b>3. Nombres estandarizados:</b> Nombra tu cuaderno exactamente con la palabra de la columna verde para tener todo tu portafolio perfectamente ordenado."
    )
    callout_table = Table([[Paragraph(callout_html, style_callout_body)]], colWidths=[531])
    callout_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0284C7')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(callout_table)
    story.append(Spacer(1, 6))

    # 3. Tabla Principal de 15 Etiquetas y Cuadernos
    table_data = [
        [
            Paragraph("Etiqueta en Clase", style_tbl_head),
            Paragraph("Nombre de tu Cuaderno", style_tbl_head),
            Paragraph("¿Qué guardaremos en este cuaderno?", style_tbl_head)
        ]
    ]

    for tag, nombre, desc in ETIQUETAS:
        table_data.append([
            Paragraph(tag, style_tag),
            Paragraph(nombre, style_notebook),
            Paragraph(desc, style_desc)
        ])

    t_main = Table(table_data, colWidths=[85, 120, 326])
    t_style = [
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0284C7')),
        ('ALIGN', (0,0), (1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]
    # Colores alternos en filas
    for i in range(1, len(table_data)):
        bg = colors.HexColor('#F8FAFC') if i % 2 == 1 else colors.white
        t_style.append(('BACKGROUND', (0, i), (-1, i), bg))

    t_main.setStyle(TableStyle(t_style))
    story.append(t_main)
    story.append(Spacer(1, 6))

    # 4. Caja Inferior de Beneficio y Portafolio
    tip_html = (
        "<b>💡 [CONSEJO] El Gran Beneficio: Tu Portafolio Personal Ordenado</b><br/>"
        "• A lo largo de las 60 sesiones realizarás decenas de prácticas fascinantes con inteligencia artificial.<br/>"
        "• Cuando quieras recuperar una receta o redacción formal, irás directo a tu cuaderno <b>TEXTO</b>.<br/>"
        "• Si quieres admirar tus ilustraciones y cuadros generados, abrirás <b>ESTILO</b> y los tendrás todos juntos.<br/>"
        "• <b>¡Nunca más volverás a perder una práctica valiosa entre cientos de conversaciones dispersas!</b>"
    )
    t_tip = Table([[Paragraph(tip_html, style_tip_body)]], colWidths=[531])
    t_tip.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFBEB')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#F59E0B')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_tip)
    story.append(Spacer(1, 5))

    # 5. Pie de página
    story.append(Paragraph("Curso de Inteligencia Artificial • Fase 0: Guía Metodológica de Cuadernos • Hoja Oficial de Referencia", style_footer))

    doc.build(story)
    print(f"✅ PDF generado con éxito en: {PDF_PATH}")

if __name__ == '__main__':
    try:
        build_pdf_reportlab()
    except Exception as e:
        print(f"❌ Error al generar el PDF: {e}")
        sys.exit(1)
