#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_indice_10_simulaciones_3d.py
Genera el PDF del Catálogo Maestro de las 10 Grandes Simulaciones Interactivas 3D Intercaladas
(Anatomía Humana / Historia / Espacio / Mecánica / Paleontología / Acústica).
"""

import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT_DIR, "SIMULADORES_INTERACTIVOS", "02_INDICES_Y_CATALOGOS")
PDF_PATH = os.path.join(OUT_DIR, "INDICE_10_SIMULACIONES_INTERACTIVAS_3D.pdf")

def build_pdf():
    try:
        from reportlab.lib.pagesizes import A4, landscape
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    except ImportError:
        print("❌ Falta reportlab. Instálalo con: pip3 install reportlab")
        sys.exit(1)

    os.makedirs(OUT_DIR, exist_ok=True)
    # Formato horizontal A4 para albergar con máxima legibilidad la tabla de 10 simulaciones
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=landscape(A4),
        leftMargin=32, rightMargin=32,
        topMargin=28, bottomMargin=26
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Heading1"],
        fontSize=17,
        leading=21,
        textColor=colors.HexColor("#0f172a"),
        alignment=1,
        fontName="Helvetica-Bold"
    )

    sub_style = ParagraphStyle(
        "SubStyle",
        parent=styles["Normal"],
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#475569"),
        alignment=1,
        fontName="Helvetica-Oblique"
    )

    h2_style = ParagraphStyle(
        "H2Style",
        parent=styles["Heading2"],
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#0369a1"),
        fontName="Helvetica-Bold",
        spaceBefore=4, spaceAfter=3
    )

    intro_style = ParagraphStyle(
        "IntroStyle",
        parent=styles["Normal"],
        fontSize=8.5,
        leading=11.5,
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

    tc_sesion = ParagraphStyle(
        "TCSesion",
        parent=styles["Normal"],
        fontSize=8.2,
        leading=10.5,
        textColor=colors.HexColor("#0f172a"),
        fontName="Helvetica-Bold",
        alignment=1
    )

    tc_theme = ParagraphStyle(
        "TCTheme",
        parent=styles["Normal"],
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#0284c7"),
        fontName="Helvetica-Bold"
    )

    tc_model = ParagraphStyle(
        "TCModel",
        parent=styles["Normal"],
        fontSize=8.2,
        leading=11,
        textColor=colors.HexColor("#0f172a"),
        fontName="Helvetica-Bold"
    )

    tc_exp = ParagraphStyle(
        "TCExp",
        parent=styles["Normal"],
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor("#334155"),
        fontName="Helvetica"
    )

    tc_btn = ParagraphStyle(
        "TCBtn",
        parent=styles["Normal"],
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor("#047857"),
        fontName="Helvetica-Bold"
    )

    tc_status = ParagraphStyle(
        "TCStatus",
        parent=styles["Normal"],
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#475569"),
        fontName="Helvetica-Oblique",
        alignment=1
    )

    elements = []

    # Encabezado
    elements.append(Paragraph("🌌 CATÁLOGO MAESTRO: 10 GRANDES SIMULACIONES INTERACTIVAS 3D INTERCALADAS", title_style))
    elements.append(Spacer(1, 2))
    elements.append(Paragraph("Plan Didáctico Intercalado: Alternancia de Anatomía Biomédica, Historia, Exploración Espacial, Mecánica y Paleontología", sub_style))
    elements.append(Spacer(1, 6))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0284c7"), spaceAfter=6))

    # Introducción Didáctica
    intro_p = (
        "<b>Metodología de Intercalación Temática:</b> Para evitar la fatiga cognitiva y mantener la fascinación visual permanente en el alumnado senior (60+), "
        "el bloque de creación de simuladores con IA <b>[COD]</b> alterna una sesión de <i>Anatomía y Salud Humana</i> (fotorrealismo biomédico con pulso, respiración o reflejo a la luz) "
        "con una sesión de <i>Grandes Hitos de la Humanidad</i> (arqueología milenaria, ingeniería espacial de la NASA, biomecánica mecánica o fósiles prehistóricos). "
        "Cada experiencia incluye arquitectura de <b>Doble Botón</b>: Taller Interactivo de Pruebas de Código generado con Gemini y acceso directo al Simulador Terminado."
    )
    elements.append(Paragraph(intro_p, intro_style))
    elements.append(Spacer(1, 6))

    # Tabla Maestra de las 10 Simulaciones
    headers = [
        Paragraph("Sesión", table_header_style),
        Paragraph("Universo / Temática", table_header_style),
        Paragraph("Modelo Aprobado (PBR 4K)", table_header_style),
        Paragraph("Experiencia Visual e Interactiva", table_header_style),
        Paragraph("Botón 2 • Simulador Terminado", table_header_style),
        Paragraph("Estado en Aula", table_header_style)
    ]

    rows = [
        [
            Paragraph("<b>01</b><br/><font color='#64748B'>[COD-001]</font>", tc_sesion),
            Paragraph("🫁 Salud & Respiración", tc_theme),
            Paragraph("Árbol Traqueobronquial & Pulmones", tc_model),
            Paragraph("Estructura traqueal fractal, ventilación alveolar biofísica rítmica y audio respiratorio.", tc_exp),
            Paragraph("🫁 Ver Simulador Pulmones 3D ↗", tc_btn),
            Paragraph("✅ <b>Activo en S01</b>", tc_status)
        ],
        [
            Paragraph("<b>02</b><br/><font color='#64748B'>[COD-002]</font>", tc_sesion),
            Paragraph("❤️ Salud & Cardiología", tc_theme),
            Paragraph("Corazón Humano con Fonendoscopio", tc_model),
            Paragraph("Fotogrametría PBR 4K miocardio, ecuación Wiggers (sístole/diástole), slider BPM y fonendoscopio acústico.", tc_exp),
            Paragraph("🫀 Ver Simulador Corazón 3D ↗", tc_btn),
            Paragraph("✅ <b>Activo en S02</b>", tc_status)
        ],
        [
            Paragraph("<b>03</b><br/><font color='#64748B'>[COD-003]</font>", tc_sesion),
            Paragraph("🏛️ Historia & Arqueología", tc_theme),
            Paragraph("Tesoro de Pompeya (Foro & Ruinas CyArk)", tc_model),
            Paragraph("Arqueología digital HD, comparador de viaje en el tiempo (ruinas vs. reconstrucción imperial), iluminación cinematográfica.", tc_exp),
            Paragraph("🏛️ Ver Tesoro Arqueológico 3D ↗", tc_btn),
            Paragraph("🚀 <b>Activo en S03</b>", tc_status)
        ],
        [
            Paragraph("<b>04</b><br/><font color='#64748B'>[COD-004]</font>", tc_sesion),
            Paragraph("👁️ Salud & Óptica", tc_theme),
            Paragraph("Globo Ocular Humano & Cristalino", tc_model),
            Paragraph("Córnea de cristal reflectante, iris 4K, pupila interactiva con reflejo fotomotor (miosis/midriasis por slider) y seguimiento ocular.", tc_exp),
            Paragraph("👁️ Ver Simulador Ojo Humano 3D ↗", tc_btn),
            Paragraph("📅 Plan S04", tc_status)
        ],
        [
            Paragraph("<b>05</b><br/><font color='#64748B'>[COD-005]</font>", tc_sesion),
            Paragraph("🚀 Espacio & Exploración", tc_theme),
            Paragraph("Módulo Lunar Apolo 11 (NASA)", tc_model),
            Paragraph("Estructura aeroespacial PBR, láminas de foil térmico dorado 4K, toberas de descenso y control de empuje orbital.", tc_exp),
            Paragraph("🚀 Ver Módulo Lunar 3D ↗", tc_btn),
            Paragraph("📅 Plan S05", tc_status)
        ],
        [
            Paragraph("<b>06</b><br/><font color='#64748B'>[COD-006]</font>", tc_sesion),
            Paragraph("🧠 Salud & Neurociencia", tc_theme),
            Paragraph("Cerebro Humano & Red Sináptica", tc_model),
            Paragraph("Resonancia magnética médica cortical, vías neuronales, pulsos lumínicos bioeléctricos y selector de lóbulos cerebrales.", tc_exp),
            Paragraph("🧠 Ver Simulador Cerebro 3D ↗", tc_btn),
            Paragraph("📅 Plan S06", tc_status)
        ],
        [
            Paragraph("<b>07</b><br/><font color='#64748B'>[COD-007]</font>", tc_sesion),
            Paragraph("⚙️ Mecánica & Automoción", tc_theme),
            Paragraph("Motor de 4 Tiempos en Sección Abierta", tc_model),
            Paragraph("Cilindro, pistón, cigüeñal y válvulas sincronizadas; ciclo térmico en corte transversal y control continuo de RPM con audio.", tc_exp),
            Paragraph("⚙️ Ver Motor Mecánico 3D ↗", tc_btn),
            Paragraph("📅 Plan S07", tc_status)
        ],
        [
            Paragraph("<b>08</b><br/><font color='#64748B'>[COD-008]</font>", tc_sesion),
            Paragraph("🦖 Paleontología & Evolución", tc_theme),
            Paragraph("Cráneo Fósil de Tiranosaurio Rex", tc_model),
            Paragraph("Fotogrametría fósil de museo, porosidad mineralizada 4K, bisagra mandibular interactiva con apertura/cierre de fauces.", tc_exp),
            Paragraph("🦖 Ver Fósil T-Rex 3D ↗", tc_btn),
            Paragraph("📅 Plan S08", tc_status)
        ],
        [
            Paragraph("<b>09</b><br/><font color='#64748B'>[COD-009]</font>", tc_sesion),
            Paragraph("🦷 Salud & Odontología", tc_theme),
            Paragraph("Molar Humano en Sección Anatómica", tc_model),
            Paragraph("Esmalte lúcido, dentina, pulpa vascularizada y terminaciones nerviosas; despiece tridimensional por capas clínicas.", tc_exp),
            Paragraph("🦷 Ver Molar Anatómico 3D ↗", tc_btn),
            Paragraph("📅 Plan S09", tc_status)
        ],
        [
            Paragraph("<b>10</b><br/><font color='#64748B'>[COD-010]</font>", tc_sesion),
            Paragraph("🎻 Acústica & Arte Musical", tc_theme),
            Paragraph("Violín Stradivarius & Resonancia Acústica", tc_model),
            Paragraph("Madera de arce noble barnizada PBR 4K, simulación de cuerdas en vibración física armónica y ondas de presión acústica.", tc_exp),
            Paragraph("🎻 Ver Acústica Stradivarius 3D ↗", tc_btn),
            Paragraph("📅 Plan S10", tc_status)
        ]
    ]

    table_data = [headers] + rows

    # Ancho total útil en A4 Landscape: 841.89 - 64 = 777.89 pt
    col_widths = [54, 98, 142, 275, 138, 70]
    t = Table(table_data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f172a")),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#f8fafc"), colors.HexColor("#ffffff")]),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))

    elements.append(t)
    elements.append(Spacer(1, 6))

    # Pie explicativo
    footer_text = (
        "<b>Estándar Técnico Compartido:</b> Todos los simuladores operan en el navegador sin descargas pesadas ni plugins externos, "
        "compatibles con WebGL / Babylon.js / Three.js, y garantizan una experiencia pedagógica fluida en equipos estándar."
    )
    elements.append(Paragraph(footer_text, intro_style))

    doc.build(elements)
    print(f"✅ PDF del Catálogo Maestro de 10 Simulaciones generado con éxito en: {PDF_PATH} ({os.path.getsize(PDF_PATH)} bytes)")

if __name__ == "__main__":
    build_pdf()

