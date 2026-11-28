#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de la ficha didáctica senior (+65):
4B. NLM-003_Mini_Curso_Interactivo_Pompeya.pdf
Inicia con la URL de YouTube de Pompeya como fuente en NotebookLM
y entrega los 5 prompts para generar los 5 artefactos del mini-curso en Studio.
"""
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

BASE = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF"
OUT_PDF = os.path.join(BASE, "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/03_Sesion/4B. NLM-003_Mini_Curso_Interactivo_Pompeya.pdf")

YOUTUBE_URL = "https://youtu.be/0lw0_3WM5XY?si=3uYWRZdrQqyrOmFX"


def make_box(title, body_html, bg_hex, border_hex, styles, width=17.4 * cm):
    content = [
        Paragraph(f"<b>{title}</b>", styles["BoxTitle"]),
        Spacer(1, 3),
        Paragraph(body_html, styles["BoxBody"]),
    ]
    t = Table([[content]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(bg_hex)),
        ("BOX", (0, 0), (-1, -1), 1.1, colors.HexColor(border_hex)),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 11),
    ]))
    return t


def make_artifact_card(num_badge, title, where_text, prompt_text, bg_hex, border_hex, styles):
    content = [
        Paragraph(f"<b>{num_badge} · {title}</b>", styles["CardTitle"]),
        Spacer(1, 2),
        Paragraph(f"<b>Dónde pulsar:</b> {where_text}", styles["WhereText"]),
        Spacer(1, 4),
        Paragraph(f"<b>Prompt para copiar y pegar:</b><br/><i>«{prompt_text}»</i>", styles["PromptText"]),
    ]
    t = Table([[content]], colWidths=[17.4 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(bg_hex)),
        ("BOX", (0, 0), (-1, -1), 1.0, colors.HexColor(border_hex)),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 11),
    ]))
    return t


def build():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="Kicker", fontName="Helvetica-Bold", fontSize=8.5, leading=11,
        textColor=colors.HexColor("#0369A1")
    ))
    styles.add(ParagraphStyle(
        name="MainTitle", fontName="Helvetica-Bold", fontSize=15.5, leading=19,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="SubTitle", fontName="Helvetica", fontSize=9.6, leading=13,
        textColor=colors.HexColor("#475569")
    ))
    styles.add(ParagraphStyle(
        name="SectionHead", fontName="Helvetica-Bold", fontSize=11.5, leading=14.5,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="BoxTitle", fontName="Helvetica-Bold", fontSize=10.2, leading=13.5,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="BoxBody", fontName="Helvetica", fontSize=9.4, leading=13.2,
        textColor=colors.HexColor("#1E293B")
    ))
    styles.add(ParagraphStyle(
        name="CardTitle", fontName="Helvetica-Bold", fontSize=10.2, leading=13.2,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="WhereText", fontName="Helvetica", fontSize=8.9, leading=12.2,
        textColor=colors.HexColor("#334155")
    ))
    styles.add(ParagraphStyle(
        name="PromptText", fontName="Helvetica", fontSize=9.3, leading=12.8,
        textColor=colors.HexColor("#0F172A")
    ))

    doc = SimpleDocTemplate(
        OUT_PDF, pagesize=A4,
        leftMargin=1.8 * cm, rightMargin=1.8 * cm,
        topMargin=1.4 * cm, bottomMargin=1.4 * cm
    )

    story = []

    # Cabecera
    header_box = Table([[
        [
            Paragraph("SESIÓN 03 · ÍTEM #08B [NLM-003] · MINI-CURSO INTERACTIVO EN NOTEBOOKLM", styles["Kicker"]),
            Spacer(1, 3),
            Paragraph("Pompeya: Crea tu Propio Curso Interactivo en NotebookLM", styles["MainTitle"]),
            Spacer(1, 3),
            Paragraph(
                "Convierte un documental de YouTube sobre Pompeya y la erupción del Vesubio en 5 artefactos interactivos "
                "(Audio, Vídeo, Mapa Mental + Cronología, Cuestionario y Presentación) para explorarlos por separado.",
                styles["SubTitle"]
            ),
        ]
    ]], colWidths=[17.4 * cm])
    header_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F0F9FF")),
        ("BOX", (0, 0), (-1, -1), 1.3, colors.HexColor("#0284C7")),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 11),
    ]))
    story.append(header_box)
    story.append(Spacer(1, 10))

    # Paso Inicial: Fuente de YouTube
    fuente_html = (
        "1. Abre <b>https://notebooklm.google.com</b> con tu cuenta de Google y pulsa <b>«+ Crear cuaderno»</b>.<br/>"
        "2. En la ventana <b>Añadir fuentes</b>, elige la opción <b>YouTube</b> (vídeo).<br/>"
        "3. Copia y pega exactamente esta dirección del documental <i>«Pompeya: La Ciudad que desapareció por la Erupción del volcán Vesubio»</i> y pulsa <b>Insertar</b>:<br/><br/>"
        f"<b><font color='#0369A1'>{YOUTUBE_URL}</font></b><br/><br/>"
        "<i>Comprueba en el panel izquierdo (Fuentes) que aparece el vídeo con su casilla marcada antes de empezar.</i>"
    )
    story.append(make_box(
        "PASO INICIAL · CARGA LA FUENTE DE YOUTUBE EN NOTEBOOKLM",
        fuente_html, "#FEF3C7", "#D97706", styles
    ))
    story.append(Spacer(1, 11))

    story.append(Paragraph("LOS 5 PROMPTS PARA GENERAR LOS 5 ARTEFACTOS DEL CURSO (EN STUDIO)", styles["SectionHead"]))
    story.append(Spacer(1, 6))

    # Artefacto 1
    story.append(make_artifact_card(
        "ARTEFACTO 1",
        "Resumen de Audio (Programa de Radio / Pódcast en español)",
        "Panel derecho <b>Studio</b> → botón <b>Resumen de Audio</b> → icono <b>Personalizar (lápiz)</b>.",
        "Crea una conversación amena y pausada en español, como un programa de radio cultural para adultos mayores, "
        "explicando cómo era la vida diaria en Pompeya antes del año 79 d.C. y cómo ocurrió la erupción del Vesubio "
        "según el vídeo. Usa un tono cercano, claro y sin tecnicismos.",
        "#F8FAFC", "#0284C7", styles
    ))
    story.append(Spacer(1, 8))

    # Artefacto 2
    story.append(make_artifact_card(
        "ARTEFACTO 2",
        "Resumen de Vídeo (Documental Narrado Paso a Paso)",
        "Panel derecho <b>Studio</b> → botón <b>Resumen de Vídeo</b> → <b>Personalizar</b>.",
        "Genera un resumen visual claro y ordenado en español sobre el documental de Pompeya: comienza mostrando la "
        "ciudad romana viva, explica las señales previas del volcán Vesubio, la erupción y cómo la ceniza conservó "
        "las casas, frescos y calles como una cápsula del tiempo.",
        "#F8FAFC", "#7C3AED", styles
    ))
    story.append(Spacer(1, 8))

    # Artefacto 3
    story.append(make_artifact_card(
        "ARTEFACTO 3",
        "Mapa Mental Interactivo + Cronología del Desastre",
        "Panel <b>Studio</b> → pulsa <b>Mapa Mental</b> (1 clic) y después escribe este prompt en el <b>Chat central</b> (pulsa <i>Guardar en nota</i>).",
        "A partir exclusivamente del vídeo, organiza una cronología sencilla paso a paso de la erupción del Vesubio "
        "y de los hallazgos arqueológicos en Pompeya, con títulos claros y frases cortas fáciles de leer.",
        "#F0FDF4", "#16A34A", styles
    ))
    story.append(Spacer(1, 8))

    # Artefacto 4
    story.append(make_artifact_card(
        "ARTEFACTO 4",
        "Tarjetas Didácticas (Flashcards) y Cuestionario (Quiz)",
        "Panel derecho <b>Studio</b> → botón <b>Tarjetas didácticas</b> (y luego <b>Cuestionario</b>) → <b>Personalizar</b>.",
        "Crea un repaso ameno en español con preguntas claras sobre la vida cotidiana en Pompeya, el volcán Vesubio "
        "y los descubrimientos arqueológicos del vídeo. Incluye pistas sencillas y explica brevemente cada respuesta.",
        "#FFF7ED", "#EA580C", styles
    ))
    story.append(Spacer(1, 8))

    # Artefacto 5
    story.append(make_artifact_card(
        "ARTEFACTO 5",
        "Presentación Visual / Infografía Resumen",
        "Panel derecho <b>Studio</b> → botón <b>Presentación</b> (o <b>Infografía</b>) → <b>Personalizar</b>.",
        "Diseña una presentación visual limpia y muy legible en español titulada «Pompeya: Vida, Erupción y Legado», "
        "con letra grande, pocos textos por diapositiva y comparando la ciudad viva antes del año 79 d.C. con lo que "
        "hoy podemos visitar en las ruinas.",
        "#FDF2F8", "#DB2777", styles
    ))
    story.append(Spacer(1, 9))

    # Consejo final
    story.append(make_box(
        "CONSEJO DE CLASE · CÓMO VER LOS 5 ARTEFACTOS POR SEPARADO",
        "Cada vez que pulses un botón en <b>Studio</b>, NotebookLM guardará ese artefacto en tu lista de la derecha "
        "con su propio icono. Puedes abrirlos y disfrutarlos <b>uno a uno por separado</b> (escuchar el pódcast, ver el "
        "vídeo, navegar por el mapa mental, jugar al cuestionario y pasar las diapositivas).",
        "#EFF6FF", "#2563EB", styles
    ))

    doc.build(story)
    print(f"✅ Generado PDF NLM-003 Pompeya: {OUT_PDF}")


if __name__ == "__main__":
    build()
