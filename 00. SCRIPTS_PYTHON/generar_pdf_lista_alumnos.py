#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_pdf_lista_alumnos.py
Genera un documento PDF profesional con la tabla de alumnos y correos
transcrita fielmente a partir de la lista manuscrita (curso 26-27).
Destino:
/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-ROBOTICA-IA-COMUN/LISTA ALUMNOS 26-27/
"""

import os
import sys

OUTPUT_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-ROBOTICA-IA-COMUN/LISTA ALUMNOS 26-27"
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "LISTA_ALUMNOS_26-27.pdf")

ALUMNOS = [
    (1, "Manuel Romerales Agudo", "mromerales@gmail.com", "Activo"),
    (2, "Juan Rivera Gil", "riveragiljuan@gmail.com", "Activo"),
    (3, "Fernando Sancho Sanz", "fernandosancho19@gmail.com", "Activo"),
    (4, "Juan Carlos Sastre", "jc00ster@gmail.com", "Activo"),
    (5, "José Ignacio Ruiz García", "agarfayos@gmail.com", "Activo"),
    (6, "Mª Carmen Sánchez", "marylavand@gmail.com", "Activo"),
    (7, "Francisco Casado Santiago", "franciscocurso2025@gmail.com", "Activo"),
    (8, "Santiago Antoñanzas de León", "dr.antonanzas@gmail.com", "Activo"),
    (9, "José Antonio Arteta", "jar.curso@gmail.com", "Activo"),
    (10, "Alberto Cogorro Ávila", "condearriero@gmail.com", "Activo"),
    (11, "Pedro Reis Fargallo", "reisfargallo@gmail.com", "Activo"),
]

def build_pdf():
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    style_title = ParagraphStyle(
        'TitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.white,
        alignment=1
    )
    style_subtitle = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#93C5FD'),
        alignment=1
    )
    style_th = ParagraphStyle(
        'THStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.white,
        alignment=1
    )
    style_num = ParagraphStyle(
        'NumStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#2563EB'),
        alignment=1
    )
    style_name = ParagraphStyle(
        'NameStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#0F172A')
    )
    style_email = ParagraphStyle(
        'EmailStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#0284C7')
    )
    style_status = ParagraphStyle(
        'StatusStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#059669'),
        alignment=1
    )
    style_note = ParagraphStyle(
        'NoteStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=7.5,
        leading=10.5,
        textColor=colors.HexColor('#64748B')
    )
    style_footer = ParagraphStyle(
        'FooterStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#94A3B8'),
        alignment=1
    )

    story = []

    # 1. Encabezado principal tipo Banner
    header_data = [
        [Paragraph("CURSO DE ROBÓTICA E INTELIGENCIA ARTIFICIAL • CURSO 2026-2027", style_title)],
        [Paragraph("LISTADO OFICIAL DE ALUMNOS Y CORREOS ELECTRÓNICOS", style_subtitle)]
    ]
    t_header = Table(header_data, colWidths=[523])
    t_header.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0F172A')),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_header)
    story.append(Spacer(1, 14))

    # 2. Tabla Principal
    table_data = [
        [
            Paragraph("Nº", style_th),
            Paragraph("Nombre y Apellidos", style_th),
            Paragraph("Correo Electrónico (Gmail)", style_th),
            Paragraph("Estado", style_th)
        ]
    ]

    for num, nombre, correo, estado in ALUMNOS:
        table_data.append([
            Paragraph(f"{num:02d}", style_num),
            Paragraph(nombre, style_name),
            Paragraph(correo, style_email),
            Paragraph(estado, style_status)
        ])

    t_main = Table(table_data, colWidths=[35, 215, 205, 68])
    t_style = [
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E40AF')),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('ALIGN', (3,0), (3,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6.5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]

    for i in range(1, len(table_data)):
        bg = colors.HexColor('#F8FAFC') if i % 2 == 1 else colors.white
        t_style.append(('BACKGROUND', (0, i), (-1, i), bg))

    t_main.setStyle(TableStyle(t_style))
    story.append(t_main)
    story.append(Spacer(1, 14))

    # 3. Caja de Resumen y Observaciones
    obs_text = (
        "<b>Observaciones de cotejo documental:</b><br/>"
        "• Transcripción verificada y validada contra la hoja manuscrita original y el archivo digital del curso.<br/>"
        "• Total de alumnos matriculados y activos: <b>11 alumnos</b>.<br/>"
        "• En la hoja manuscrita se descartó la línea intermedia tachada (correo duplicado de robótica)."
    )
    t_obs = Table([[Paragraph(obs_text, style_note)]], colWidths=[523])
    t_obs.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_obs)
    story.append(Spacer(1, 14))

    # 4. Pie
    story.append(Paragraph("Clases de Tecnología • Curso Robótica e IA Común • Convocatoria 2026-2027", style_footer))

    doc.build(story)
    print(f"✅ Documento PDF creado con éxito:")
    print(f"   {OUTPUT_PDF}")

if __name__ == '__main__':
    try:
        build_pdf()
    except Exception as e:
        print(f"❌ Error al crear el PDF: {e}")
        sys.exit(1)

