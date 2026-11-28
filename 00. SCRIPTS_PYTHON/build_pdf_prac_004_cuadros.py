#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de la ficha didáctica senior (+65):
PRAC-004: Diseña y Visualiza tu Pared de Cuadros con Marcos IKEA (4 Pasos en Gemini).
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
        Spacer(1, 2),
        Paragraph(prompt_text, styles["PromptBody"]),
    ]
    t = Table([[content]], colWidths=[17.4 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(bg_hex)),
        ("BOX", (0, 0), (-1, -1), 1.0, colors.HexColor(border_hex)),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
    ]))
    return t


def build():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="Kicker", fontName="Helvetica-Bold", fontSize=8.2, leading=10.5,
        textColor=colors.HexColor("#0369A1")
    ))
    styles.add(ParagraphStyle(
        name="MainTitle", fontName="Helvetica-Bold", fontSize=14.8, leading=18,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="SubTitle", fontName="Helvetica", fontSize=9.0, leading=12,
        textColor=colors.HexColor("#475569")
    ))
    styles.add(ParagraphStyle(
        name="BodySenior", fontName="Helvetica", fontSize=8.8, leading=12,
        textColor=colors.HexColor("#1E293B")
    ))
    styles.add(ParagraphStyle(
        name="PromptTitle", fontName="Helvetica-Bold", fontSize=9.2, leading=11.5,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="PromptBody", fontName="Helvetica", fontSize=8.6, leading=11.8,
        textColor=colors.HexColor("#1E293B")
    ))

    doc = SimpleDocTemplate(
        S04_PDF, pagesize=A4,
        leftMargin=1.8 * cm, rightMargin=1.8 * cm,
        topMargin=1.1 * cm, bottomMargin=1.1 * cm
    )

    story = []
    header_box = Table([[
        [
            Paragraph("SESIÓN 04 · ÍTEM #06 [PRAC-004] · TALLER PRÁCTICO DE VIDA REAL", styles["Kicker"]),
            Spacer(1, 1),
            Paragraph("Diseña y Visualiza tu Pared de Cuadros con Marcos IKEA", styles["MainTitle"]),
            Spacer(1, 1),
            Paragraph("Crea la foto del salón con Gemini y prueba combinaciones reales de marcos IKEA en 4 pasos sin hacer un solo agujero.", styles["SubTitle"]),
        ]
    ]], colWidths=[17.4 * cm])
    header_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F0F9FF")),
        ("BOX", (0, 0), (-1, -1), 1.2, colors.HexColor("#0284C7")),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
    ]))
    story.append(header_box)
    story.append(Spacer(1, 6))

    if os.path.exists(SAMPLE_IMG):
        img = RLImage(SAMPLE_IMG, width=8.6 * cm, height=6.45 * cm)
        side_txt = [
            Paragraph("<b>🎯 Objetivo del Taller en Clase</b>", styles["PromptTitle"]),
            Spacer(1, 3),
            Paragraph(
                "No necesitas traer una foto de tu casa: en el <b>Paso 1</b> le pediremos a <b>Gemini</b> que invente "
                "un salón luminoso con una <b>pared grande y vacía</b> (295 × 150 cm). Después calcularemos 3 diseños IKEA, "
                "los superpondremos a escala y los rellenaremos con marcos reales (<i>IKEA RÖDALM</i>).",
                styles["BodySenior"]
            ),
            Spacer(1, 4),
            Paragraph("<b>💡 Si quieres probarlo en casa después:</b>", styles["PromptTitle"]),
            Paragraph("Sáltate el Paso 1, haz una foto de frente a la pared de tu salón, mide el hueco libre y empieza directo en el Paso 2.", styles["BodySenior"]),
        ]
        t_intro = Table([[img, side_txt]], colWidths=[8.8 * cm, 8.6 * cm])
        t_intro.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ]))
        story.append(t_intro)
        story.append(Spacer(1, 6))

    # Paso 1: Generar foto del salón
    story.append(make_prompt_box(
        "PASO 1 · Genera una foto de salón con una pared grande y vacía (Copia y pega en Gemini)",
        "<i>«Genera una fotografía fotorrealista, de frente y a la altura de los ojos, de un salón comedor moderno y luminoso "
        "con luz natural. Debe tener una <b>pared central grande, lisa y completamente vacía</b> (de unos 3 metros de ancho "
        "por 1,5 metros de alto libres) en tono blanco cálido, sin ningún cuadro ni póster colgado. Debajo coloca una mesa "
        "redonda de madera o un aparador bajo, y a un lado un radiador blanco o unas baldas.»</i>",
        "#F5F3FF", "#7C3AED", styles
    ))
    story.append(Spacer(1, 5))

    # Paso 2: 3 combinaciones IKEA
    story.append(make_prompt_box(
        "PASO 2 · Pide 3 combinaciones con medidas reales de IKEA (En el mismo chat)",
        "<i>«Para esa pared libre de <b>295 cm de ancho x 150 cm de alto</b>, diseña <b>3 combinaciones distintas</b> de "
        "galería usando exclusivamente medidas estándar de marcos que se venden en IKEA (13x18, 21x30, 30x40, 40x50 y "
        "50x70 cm). Dibújame las 3 plantillas en blanco y negro indicando la medida de cada marco y el total de cada conjunto.»</i>",
        "#FFFBEB", "#F59E0B", styles
    ))
    story.append(Spacer(1, 5))

    # Paso 3: Superposición a escala
    story.append(make_prompt_box(
        "PASO 3 · Superpón la plantilla elegida sobre la foto del salón",
        "<i>«Toma la foto del salón del Paso 1 y superpón la plantilla número <b>[1, 2 o 3]</b> centrada en la pared vacía, "
        "<b>respetando estrictamente la escala real</b> frente a la mesa y el resto del mobiliario, sin cambiar nada de la habitación.»</i>",
        "#F0FDF4", "#16A34A", styles
    ))
    story.append(Spacer(1, 5))

    # Paso 4: Acabado RÖDALM + fotos
    story.append(make_prompt_box(
        "PASO 4 · Rellena con marcos reales de IKEA (RÖDALM) y fotos en blanco y negro o color",
        "<i>«Ahora rellena esos cuadros con <b>fotografías artísticas en blanco y negro</b> (o en color cálido), montadas "
        "con paspartú blanco y marco negro mate fino estilo <b>IKEA RÖDALM</b> "
        "(https://www.ikea.com/es/es/p/rodalm-marco-negro-20548918/), manteniendo sombras suaves naturales sobre la pared.»</i>",
        "#EFF6FF", "#2563EB", styles
    ))
    story.append(Spacer(1, 6))

    # Preguntas
    q_box = Table([[
        [
            Paragraph("<b>💬 3 Preguntas Clave para Comentar en Clase</b>", styles["PromptTitle"]),
            Spacer(1, 2),
            Paragraph("<b>1.</b> ¿Qué combinación te convence más por equilibrio: llenar casi toda la pared o dejar aire a los lados?", styles["BodySenior"]),
            Paragraph("<b>2.</b> Si cambiamos de marcos negros a madera natural o a láminas en color, ¿qué sensación transmite el salón?", styles["BodySenior"]),
            Paragraph("<b>3.</b> ¿Qué medidas exactas de marcos IKEA tendrías que apuntar en tu lista de la compra tras ver la simulación?", styles["BodySenior"]),
        ]
    ]], colWidths=[17.4 * cm])
    q_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
        ("BOX", (0, 0), (-1, -1), 0.9, colors.HexColor("#94A3B8")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
    ]))
    story.append(q_box)

    doc.build(story)
    shutil.copyfile(S04_PDF, BLQ_PDF)
    shutil.copyfile(S04_PDF, BLQ_PDF_ALT)
    print("✅ Generado PDF PRAC-004 (4 pasos):", S04_PDF)


if __name__ == "__main__":
    build()
