#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de la ficha didáctica senior (+65):
PRAC-004: Diseña y Visualiza tu Pared de Cuadros con Marcos IKEA (3 Pasos en Gemini).
"""
import os
import shutil
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Image as RLImage
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

BASE = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF"
S04_PDF = os.path.join(BASE, "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/04_Sesion/3. PRAC-004_Decoracion_Pared_Cuadros_IKEA.pdf")
BLQ_PDF = os.path.join(BASE, "03. [PRAC] BLOQUE_3_TALLERES_DE_PROMPTS_PRACTICOS/Lote_01_al_20/3. PRAC-004_Decoracion_Pared_Cuadros_IKEA.pdf")
BLQ_PDF_ALT = os.path.join(BASE, "03. [PRAC] BLOQUE_3_TALLERES_DE_PROMPTS_PRACTICOS/Lote_01_al_20/PRAC-004_Decoracion_Pared_Cuadros_IKEA.pdf")
SAMPLE_IMG = os.path.join(BASE, "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/04_Sesion/SALON_EJEMPLO_PRAC_004.jpg")


def make_prompt_box(title, prompt_text, bg_hex, border_hex, styles):
    content = [
        Paragraph(f"<b>{title}</b>", styles["PromptTitle"]),
        Spacer(1, 3),
        Paragraph(prompt_text, styles["PromptBody"]),
    ]
    t = Table([[content]], colWidths=[17.4 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(bg_hex)),
        ("BOX", (0, 0), (-1, -1), 1.0, colors.HexColor(border_hex)),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    return t


def build():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="Kicker", fontName="Helvetica-Bold", fontSize=8.5, leading=11,
        textColor=colors.HexColor("#0369A1")
    ))
    styles.add(ParagraphStyle(
        name="MainTitle", fontName="Helvetica-Bold", fontSize=15.2, leading=18.5,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="SubTitle", fontName="Helvetica", fontSize=9.3, leading=12.5,
        textColor=colors.HexColor("#475569")
    ))
    styles.add(ParagraphStyle(
        name="BodySenior", fontName="Helvetica", fontSize=9.2, leading=12.8,
        textColor=colors.HexColor("#1E293B")
    ))
    styles.add(ParagraphStyle(
        name="PromptTitle", fontName="Helvetica-Bold", fontSize=9.5, leading=12,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="PromptBody", fontName="Helvetica", fontSize=8.9, leading=12.4,
        textColor=colors.HexColor("#1E293B")
    ))

    doc = SimpleDocTemplate(
        S04_PDF, pagesize=A4,
        leftMargin=1.8 * cm, rightMargin=1.8 * cm,
        topMargin=1.3 * cm, bottomMargin=1.3 * cm
    )

    story = []
    header_box = Table([[
        [
            Paragraph("SESIÓN 04 · ÍTEM #06 [PRAC-004] · TALLER PRÁCTICO DE VIDA REAL", styles["Kicker"]),
            Spacer(1, 2),
            Paragraph("Diseña y Visualiza tu Pared de Cuadros con Marcos IKEA", styles["MainTitle"]),
            Spacer(1, 2),
            Paragraph("Genera un salón con Gemini, diseña 3 plantillas IKEA y compara las 3 composiciones reales con marco en solo 3 pasos.", styles["SubTitle"]),
        ]
    ]], colWidths=[17.4 * cm])
    header_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F0F9FF")),
        ("BOX", (0, 0), (-1, -1), 1.2, colors.HexColor("#0284C7")),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(header_box)
    story.append(Spacer(1, 8))

    if os.path.exists(SAMPLE_IMG):
        img = RLImage(SAMPLE_IMG, width=9.6 * cm, height=7.2 * cm)
        side_txt = [
            Paragraph("<b>🎯 Objetivo del Taller (Solo 3 Prompts)</b>", styles["PromptTitle"]),
            Spacer(1, 4),
            Paragraph(
                "1) <b>Gemini</b> crea la foto de un salón con una pared grande vacía. "
                "2) Diseña <b>3 plantillas en blanco</b> con medidas reales de IKEA. "
                "3) Genera <b>3 escenarios</b> usando 3 veces esa misma habitación con las 3 plantillas ya colocadas, "
                "<b>con fotos reales y marcos negros IKEA RÖDALM</b>.",
                styles["BodySenior"]
            ),
            Spacer(1, 6),
            Paragraph("<b>💡 Para probarlo en casa con tu propia pared:</b>", styles["PromptTitle"]),
            Paragraph("Sáltate el Paso 1, sube la foto de frente de tu salón con tus medidas y pasa directo al Paso 2.", styles["BodySenior"]),
        ]
        t_intro = Table([[img, side_txt]], colWidths=[9.8 * cm, 7.6 * cm])
        t_intro.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ]))
        story.append(t_intro)
        story.append(Spacer(1, 8))

    # Paso 1
    story.append(make_prompt_box(
        "PASO 1 · Genera la foto de la habitación con una pared grande y vacía",
        "<i>«Genera una fotografía fotorrealista, de frente y a la altura de los ojos, de un salón comedor moderno y luminoso "
        "con luz natural. Debe tener una <b>pared central grande, lisa y completamente vacía</b> (de unos 3 metros de ancho "
        "por 1,5 metros de alto libres) en tono blanco cálido, sin ningún cuadro ni póster colgado. Debajo coloca una mesa "
        "redonda de madera o un aparador bajo, y a un lado un radiador blanco o unas baldas.»</i>",
        "#F5F3FF", "#7C3AED", styles
    ))
    story.append(Spacer(1, 7))

    # Paso 2
    story.append(make_prompt_box(
        "PASO 2 · Genera 3 plantillas en blanco con medidas reales de IKEA",
        "<i>«Para esa pared libre de <b>295 cm de ancho x 150 cm de alto</b>, diseña <b>3 plantillas en blanco distintas</b> "
        "usando exclusivamente medidas estándar de marcos de IKEA (13x18, 21x30, 30x40, 40x50 y 50x70 cm). "
        "Dibújame los 3 esquemas en blanco y negro indicando las medidas de cada marco y el ancho y alto total de cada conjunto.»</i>",
        "#FFFBEB", "#F59E0B", styles
    ))
    story.append(Spacer(1, 7))

    # Paso 3 (Final: 3 escenarios completos)
    story.append(make_prompt_box(
        "PASO 3 (FINAL) · Genera los 3 escenarios completos con cuadros reales y marco IKEA RÖDALM",
        "<i>«Ahora genera <b>3 imágenes finales distintas</b> usando <b>3 veces exactamente la misma habitación del Paso 1</b> "
        "(sin cambiar muebles, luz ni paredes), colocando en cada una la plantilla 1, la plantilla 2 y la plantilla 3 a escala real. "
        "Cada cuadro debe aparecer ya relleno con <b>fotografías artísticas en blanco y negro</b> (o en color cálido), "
        "montadas con paspartú blanco y marco negro mate fino estilo <b>IKEA RÖDALM</b> "
        "(https://www.ikea.com/es/es/p/rodalm-marco-negro-20548918/) con sombras naturales sobre la pared.»</i>",
        "#F0FDF4", "#16A34A", styles
    ))
    story.append(Spacer(1, 8))

    # Preguntas
    q_box = Table([[
        [
            Paragraph("<b>💬 3 Preguntas Clave para Comentar en Clase</b>", styles["PromptTitle"]),
            Spacer(1, 3),
            Paragraph("<b>1.</b> De los 3 escenarios generados, ¿cuál te convence más por equilibrio entre los muebles y el aire libre?", styles["BodySenior"]),
            Paragraph("<b>2.</b> Si cambiamos las fotos a color o el marco negro por madera natural, ¿cambia la sensación de amplitud?", styles["BodySenior"]),
            Paragraph("<b>3.</b> ¿Qué lista exacta de marcos IKEA tendrías que comprar tras comparar los 3 escenarios?", styles["BodySenior"]),
        ]
    ]], colWidths=[17.4 * cm])
    q_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
        ("BOX", (0, 0), (-1, -1), 0.9, colors.HexColor("#94A3B8")),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(q_box)

    doc.build(story)
    shutil.copyfile(S04_PDF, BLQ_PDF)
    shutil.copyfile(S04_PDF, BLQ_PDF_ALT)
    print("✅ Generado PDF PRAC-004 (3 pasos finales):", S04_PDF)


if __name__ == "__main__":
    build()
