#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_indice_modelos_3d.py
Genera el PDF del Catálogo e Índice de Modelos Anatómicos 3D (NIH 3D / Sketchfab)
para el repositorio de SIMULADORES_INTERACTIVOS.
"""

import os
import sys

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
except ImportError:
    print("❌ Falta reportlab. Instálalo con: pip3 install reportlab")
    sys.exit(1)

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS", "02_INDICES_Y_CATALOGOS")
PDF_PATH = os.path.join(OUT_DIR, "INDICE_MODELOS_ANATOMICOS_3D_NIH.pdf")

def build_pdf():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=A4,
        leftMargin=36, rightMargin=36,
        topMargin=36, bottomMargin=36
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Heading1"],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0f172a"),
        alignment=1,
        fontName="Helvetica-Bold"
    )

    sub_style = ParagraphStyle(
        "SubStyle",
        parent=styles["Normal"],
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#475569"),
        alignment=1,
        fontName="Helvetica-Oblique"
    )

    h2_style = ParagraphStyle(
        "H2Style",
        parent=styles["Heading2"],
        fontSize=12,
        leading=15,
        textColor=colors.HexColor("#0369a1"),
        fontName="Helvetica-Bold"
    )

    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["Normal"],
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#1e293b"),
        fontName="Helvetica"
    )

    table_header_style = ParagraphStyle(
        "THStyle",
        parent=styles["Normal"],
        fontSize=8.5,
        leading=11,
        textColor=colors.white,
        fontName="Helvetica-Bold",
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        "TCStyle",
        parent=styles["Normal"],
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#1e293b"),
        fontName="Helvetica"
    )

    elements = []

    elements.append(Paragraph("🏛️ CATÁLOGO DE MODELOS ANATÓMICOS 3D FOTOGRAMÉTRICOS", title_style))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("Repositorio NIH 3D Medical & Colección de Simuladores Interactivos para el Aula", sub_style))
    elements.append(Spacer(1, 10))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0284c7"), spaceAfter=10))

    elements.append(Paragraph("1. ¿Qué son los modelos NIH 3D y cómo se complementan con el código web?", h2_style))
    elements.append(Paragraph(
        "El <b>NIH 3D Medical Repository</b> (National Institutes of Health de EE.UU.) y plataformas científicas abiertas publican escaneos reales por TAC, resonancia magnética y fotogrametría médica. "
        "El archivo 3D (.GLB/.OBJ) aporta la <b>escultura anatómica exacta y sus texturas fotográficas</b>, mientras que el <b>código JavaScript / IA</b> aporta el motor interactivo: iluminación cinematográfica, exploración 360°, dinámica fisiológica (ritmo cardíaco, ventilación diafragmática) y audio biofísico en tiempo real.",
        body_style
    ))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("2. Índice de Modelos Anatómicos Aprobados (Estándar de Oro PBR 4K)", h2_style))
    elements.append(Paragraph(
        "<i>Filtro de Calidad Estricto: Solo se incluyen modelos que cuentan con texturas fotográficas PBR (Albedo, Normal Map, Roughness) y dinámica biomédica programada en código, garantizando el mismo impacto fotorrealista que el Corazón Humano [COD-002].</i>",
        body_style
    ))
    elements.append(Spacer(1, 6))

    data = [
        [
            Paragraph("Modelo Aprobado", table_header_style),
            Paragraph("Textura PBR / Estructura", table_header_style),
            Paragraph("Dinámica / Fisiología Interactiva", table_header_style),
            Paragraph("Sesión / Asignación", table_header_style)
        ],
        [
            Paragraph("<b>❤️ Corazón Humano</b>", table_cell_style),
            Paragraph("Malla fotogramétrica 4K con relieve de arterias coronarias y miocardio húmedo.", table_cell_style),
            Paragraph("Ecuación biomecánica Wiggers (sístole/diástole), slider BPM y fonendoscopio acústico.", table_cell_style),
            Paragraph("Sesión 02 [COD-002]<br/><b>Activo en Curso</b>", table_cell_style)
        ],
        [
            Paragraph("<b>🫁 Árbol Traqueobronquial</b>", table_cell_style),
            Paragraph("Estructura traqueal y ramificación bronquial fractal de alta resolución.", table_cell_style),
            Paragraph("Ventilación pulmonar, flujo acústico biológico y control de respiraciones/min.", table_cell_style),
            Paragraph("Sesión 01 [COD-001]<br/><b>Activo en Curso</b>", table_cell_style)
        ],
        [
            Paragraph("<b>👁️ Globo Ocular Humano</b>", table_cell_style),
            Paragraph("Córnea reflectante translúcida, iris fotográfico 4K ultra-detallado y esclera vascularizada.", table_cell_style),
            Paragraph("Reflejo pupilar a la luz (miosis/midriasis interactiva con slider) y seguimiento de mirada al cursor.", table_cell_style),
            Paragraph("Sesión 04 [COD-004]<br/><i>(Óptica & Visión)</i>", table_cell_style)
        ],
        [
            Paragraph("<b>🧠 Cerebro Humano</b>", table_cell_style),
            Paragraph("Escáner de resonancia médica con circunvoluciones, surcos y vascularización cortical real.", table_cell_style),
            Paragraph("Pulsos sinápticos lumínicos por vías neuronales y visualización de áreas funcionales por capas.", table_cell_style),
            Paragraph("Sesión 06 [COD-006]<br/><i>(Neurociencia & IA)</i>", table_cell_style)
        ],
        [
            Paragraph("<b>🦷 Molar en Sección Anatómica</b>", table_cell_style),
            Paragraph("Textura fotográfica PBR de esmalte brillante, dentina, pulpa vascularizada y hueso alveolar.", table_cell_style),
            Paragraph("Corte transversal interactivo, exploración de capas internas y simulación de densidad.", table_cell_style),
            Paragraph("Monográfico Salud<br/><i>(Biomedicina)</i>", table_cell_style)
        ],
        [
            Paragraph("<b>💀 Cráneo y Estructura Ósea</b>", table_cell_style),
            Paragraph("Fotogrametría de museo con porosidad ósea, suturas craneales y desgaste natural hiperrealista.", table_cell_style),
            Paragraph("Articulación temporomandibular suave y vistas de rayos X / transparencia selectiva.", table_cell_style),
            Paragraph("Monográfico Anatomía<br/><i>(Osteología)</i>", table_cell_style)
        ]
    ]

    t = Table(data, colWidths=[95, 155, 185, 85])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f172a")),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#f8fafc"), colors.HexColor("#ffffff")]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))

    elements.append(t)
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("3. Repositorios Médicos Oficiales Recomendados", h2_style))
    elements.append(Paragraph(
        "• <b>NIH 3D Print Exchange (National Institutes of Health):</b> <i>3d.nih.gov</i> — Modelos científicos de tomografía y resonancia.<br/>"
        "• <b>Sketchfab Medical & Anatomy (CC-BY):</b> <i>sketchfab.com/categories/science-technology/medical-anatomy</i> — Modelos con texturas fotográficas 4K (fuente del modelo cardíaco del Dr. Neshallads).<br/>"
        "• <b>Visible Human Project (NLM):</b> Archivo público de criosecciones milimétricas del cuerpo humano completo.",
        body_style
    ))

    doc.build(elements)
    print(f"✅ PDF creado con éxito en: {PDF_PATH} ({os.path.getsize(PDF_PATH)} bytes)")

if __name__ == "__main__":
    build_pdf()
