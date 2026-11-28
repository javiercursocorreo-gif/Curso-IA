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
        name="MainTitle", fontName="Helvetica-Bold", fontSize=15.5, leading=19,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="SubTitle", fontName="Helvetica", fontSize=9.5, leading=13,
        textColor=colors.HexColor("#475569")
    ))
    styles.add(ParagraphStyle(
        name="BodySenior", fontName="Helvetica", fontSize=9.5, leading=13,
        textColor=colors.HexColor("#1E293B")
    ))
    styles.add(ParagraphStyle(
        name="PromptTitle", fontName="Helvetica-Bold", fontSize=9.8, leading=12.5,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="PromptBody", fontName="Helvetica", fontSize=9.0, leading=12.5,
        textColor=colors.HexColor("#1E293B")
    ))

    doc = SimpleDocTemplate(
        S04_PDF, pagesize=A4,
        leftMargin=1.8 * cm, rightMargin=1.8 * cm,
        topMargin=1.4 * cm, bottomMargin=1.4 * cm
    )

    story = []
    # Cabecera
    header_box = Table([[
        [
            Paragraph("SESIÓN 04 · ÍTEM #06 [PRAC-004] · TALLER PRÁCTICO DE VIDA REAL", styles["Kicker"]),
            Spacer(1, 2),
            Paragraph("Diseña y Visualiza tu Pared de Cuadros con Marcos IKEA", styles["MainTitle"]),
            Spacer(1, 2),
            Paragraph("Cómo probar combinaciones a escala real sobre una foto de tu salón antes de hacer un solo agujero.", styles["SubTitle"]),
        ]
    ]], colWidths=[17.4 * cm])
    header_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F0F9FF")),
        ("BOX", (0, 0), (-1, -1), 1.2, colors.HexColor("#0284C7")),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(header_box)
    story.append(Spacer(1, 8))

    # Ejemplo visual + resumen
    if os.path.exists(SAMPLE_IMG):
        img = RLImage(SAMPLE_IMG, width=10.5 * cm, height=7.88 * cm)
        side_txt = [
            Paragraph("<b>🎯 Objetivo del Taller</b>", styles["PromptTitle"]),
            Spacer(1, 4),
            Paragraph(
                "En lugar de imaginar cómo quedarán los cuadros, usaremos <b>Gemini</b> en <b>3 pasos</b>: "
                "1) calcular 3 diseños con medidas reales de IKEA, 2) superponer el diseño elegido sobre la "
                "foto de tu pared y 3) rellenarlo con marcos reales (ej. <i>IKEA RÖDALM negro</i>) y fotos.",
                styles["BodySenior"]
            ),
            Spacer(1, 6),
            Paragraph("<b>📏 Qué necesitas tener a mano:</b>", styles["PromptTitle"]),
            Paragraph("• El <b>ancho y alto</b> libres de tu pared (ej. 295 × 150 cm).", styles["BodySenior"]),
            Paragraph("• Una <b>foto de frente</b> de la pared de tu salón.", styles["BodySenior"]),
            Paragraph("• El <b>modelo o enlace</b> del marco que te guste (ej. IKEA RÖDALM).", styles["BodySenior"]),
        ]
        t_intro = Table([[img, side_txt]], colWidths=[10.7 * cm, 6.7 * cm])
        t_intro.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ]))
        story.append(t_intro)
        story.append(Spacer(1, 8))

    # Paso 1
    story.append(make_prompt_box(
        "PASO 1 · Pide 3 combinaciones con medidas reales de IKEA (Copia y pega en Gemini)",
        "<i>«Quiero decorar una pared libre de mi salón que mide <b>[295 cm de ancho x 150 cm de alto]</b>. "
        "Diseña <b>3 combinaciones distintas</b> de composición de galería usando exclusivamente medidas estándar de marcos "
        "que se venden en IKEA (13x18, 21x30, 30x40, 40x50 y 50x70 cm). Dibújame las 3 plantillas en blanco y negro "
        "indicando las medidas de cada marco y el ancho y alto total de cada conjunto.»</i>",
        "#FFFBEB", "#F59E0B", styles
    ))
    story.append(Spacer(1, 6))

    # Paso 2
    story.append(make_prompt_box(
        "PASO 2 · Superpón la plantilla elegida sobre tu foto real (Sube la foto de tu salón + la plantilla)",
        "<i>«Te adjunto la foto real de mi salón y la plantilla de medidas que más me gusta del paso anterior. "
        "Haz una superposición realista colocando esos cuadros centrados en el hueco de la pared, <b>respetando "
        "estrictamente la escala real</b> frente a los muebles, el radiador y la puerta, y sin modificar nada de mi habitación.»</i>",
        "#F0FDF4", "#16A34A", styles
    ))
    story.append(Spacer(1, 6))

    # Paso 3
    story.append(make_prompt_box(
        "PASO 3 · Rellena con marcos reales de IKEA y tus fotos favoritas",
        "<i>«Ahora rellena cada uno de esos cuadros con <b>fotografías artísticas en blanco y negro</b> (o en color cálido, "
        "o ilustraciones botánicas), montadas con paspartú blanco y marco negro mate fino estilo <b>IKEA RÖDALM</b> "
        "(https://www.ikea.com/es/es/p/rodalm-marco-negro-20548918/), manteniendo sombras naturales sobre la pared.»</i>",
        "#EFF6FF", "#2563EB", styles
    ))
    story.append(Spacer(1, 8))

    # Preguntas de diálogo en clase
    q_box = Table([[
        [
            Paragraph("<b>💬 3 Preguntas Clave para Comentar en Clase</b>", styles["PromptTitle"]),
            Spacer(1, 3),
            Paragraph("<b>1.</b> ¿Qué opción te convence más por proporción: llenar casi toda la pared o dejar aire a los lados?", styles["BodySenior"]),
            Paragraph("<b>2.</b> Si cambiamos de marcos negros a madera natural o a fotos en color, ¿cambia la sensación de amplitud?", styles["BodySenior"]),
            Paragraph("<b>3.</b> ¿Qué medidas exactas de marcos IKEA tendrías que apuntar en tu lista de la compra tras ver la simulación?", styles["BodySenior"]),
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
    print("✅ Generado PDF PRAC-004 en Sesión 04 y Bloque 03 [PRAC]:", S04_PDF)


if __name__ == "__main__":
    build()
