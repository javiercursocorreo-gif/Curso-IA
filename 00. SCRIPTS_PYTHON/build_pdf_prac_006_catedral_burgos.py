#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de la ficha didáctica senior (+65):
PRAC-006: Descubre la Catedral de Burgos con «Google Profesor» (Aprendizaje guiado en Gemini).
"""
import os
import shutil
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

BASE = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA/CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF"
S06_PDF = os.path.join(BASE, "100. [SESSIONS] TERNAS_LISTAS_PARA_CLASSROOM/06_Sesion/3. PRAC-006_Google_Profesor_Catedral_de_Burgos.pdf")
BLQ_PDF = os.path.join(BASE, "03. [PRAC] BLOQUE_3_TALLERES_DE_PROMPTS_PRACTICOS/Lote_01_al_20/3. PRAC-006_Google_Profesor_Catedral_de_Burgos.pdf")


def make_box(title, body_html, bg_hex, border_hex, styles):
    content = [
        Paragraph(f"<b>{title}</b>", styles["BoxTitle"]),
        Spacer(1, 3),
        Paragraph(body_html, styles["BoxBody"]),
    ]
    t = Table([[content]], colWidths=[17.4 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(bg_hex)),
        ("BOX", (0, 0), (-1, -1), 1.1, colors.HexColor(border_hex)),
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
        name="MainTitle", fontName="Helvetica-Bold", fontSize=15.0, leading=18.5,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="SubTitle", fontName="Helvetica", fontSize=9.4, leading=12.6,
        textColor=colors.HexColor("#475569")
    ))
    styles.add(ParagraphStyle(
        name="BoxTitle", fontName="Helvetica-Bold", fontSize=10.1, leading=13.2,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="BoxBody", fontName="Helvetica", fontSize=9.2, leading=13.0,
        textColor=colors.HexColor("#1E293B")
    ))

    doc = SimpleDocTemplate(
        S06_PDF, pagesize=A4,
        leftMargin=1.8 * cm, rightMargin=1.8 * cm,
        topMargin=1.4 * cm, bottomMargin=1.4 * cm
    )

    story = []

    # Cabecera
    header_box = Table([[
        [
            Paragraph("SESIÓN 06 · ÍTEM #06 [PRAC-006] · TALLER CON «GOOGLE PROFESOR»", styles["Kicker"]),
            Spacer(1, 2),
            Paragraph("Descifra la Catedral de Burgos con «Google Profesor»", styles["MainTitle"]),
            Spacer(1, 2),
            Paragraph(
                "Aprende a usar el modo «Aprendizaje guiado» (LearnLM) de Gemini para que la IA actúe como un profesor "
                "particular: te explica paso a paso, te hace preguntas y te da pistas sin soltarte todo de golpe.",
                styles["SubTitle"]
            ),
        ]
    ]], colWidths=[17.4 * cm])
    header_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F0F9FF")),
        ("BOX", (0, 0), (-1, -1), 1.3, colors.HexColor("#0284C7")),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 11),
    ]))
    story.append(header_box)
    story.append(Spacer(1, 10))

    # Paso 1: Activar Aprendizaje guiado
    paso1_html = (
        "1. Entra en <b>https://gemini.google.com</b> con tu cuenta de Google.<br/>"
        "2. En la barra inferior donde escribes los mensajes, pulsa el botón <b>Herramientas</b> (o el icono <b>+</b>) "
        "y selecciona <b>«Aprendizaje guiado»</b> (<i>Guided Learning</i>, el modo «Google Profesor»).<br/>"
        "3. Verás que aparece la etiqueta <b>Aprendizaje guiado</b> activada debajo de la caja de texto."
    )
    story.append(make_box(
        "PASO 1 · ACTIVA EL MODO «APRENDIZAJE GUIADO» (GOOGLE PROFESOR)",
        paso1_html, "#FEF3C7", "#D97706", styles
    ))
    story.append(Spacer(1, 10))

    # Paso 2: Prompt para arrancar la tutoría
    paso2_html = (
        "Copia y pega este texto en el chat de Gemini (con <b>Aprendizaje guiado</b> activado) y pulsa Enviar:<br/><br/>"
        "<i>«Quiero que seas mi profesor particular para entender los secretos de la Catedral de Burgos y el arte gótico "
        "en 4 mini-lecciones cortas (1. Cómo se sostienen sus muros altos con arbotantes; 2. La luz de los rosetones y vidrieras; "
        "3. Las agujas caladas de Juan de Colonia; 4. Curiosidades como el Papamoscas).<br/>"
        "Reglas de nuestra clase:<br/>"
        "- Explícame solo la primera lección en 4 o 5 líneas claras y con ejemplos sencillos de la vida diaria.<br/>"
        "- Al terminar cada lección, hazme UNA pregunta amena para comprobar si lo he entendido y espera mi respuesta antes de pasar a la siguiente.<br/>"
        "- Si fallo o dudo, no me des la solución directa: dame primero una pista.»</i>"
    )
    story.append(make_box(
        "PASO 2 · PIDE TU CLASE INTERACTIVA SOBRE LA CATEDRAL DE BURGOS",
        paso2_html, "#F8FAFC", "#0284C7", styles
    ))
    story.append(Spacer(1, 10))

    # Paso 3: Cómo interactuar con el Profesor IA
    paso3_html = (
        "<b>A) Contesta a su pregunta:</b> Escribe tu respuesta con tus propias palabras (no hace falta que sea perfecta). "
        "Verás cómo «Google Profesor» te felicita o te orienta con cariño y pasa a la siguiente lección.<br/><br/>"
        "<b>B) Pon a prueba sus pistas:</b> En una de las preguntas, prueba a escribir:<br/>"
        "<i>«No estoy seguro, ¿me das una pista sencilla?»</i> o <i>«Explícamelo con una comparación de la vida diaria»</i>.<br/><br/>"
        "<b>C) Cierra la clase con un recuerdo:</b> Cuando termines las 4 mini-lecciones, escríbele:<br/>"
        "<i>«Dame un resumen de 3 ideas clave para contárselas a mis nietos cuando visitemos la Catedral de Burgos.»</i>"
    )
    story.append(make_box(
        "PASO 3 · DIALOGA CON TU PROFESOR IA (RESPONDE, PIDE PISTAS Y RESUME)",
        paso3_html, "#F0FDF4", "#16A34A", styles
    ))
    story.append(Spacer(1, 10))

    # Nota pedagógica final
    nota_html = (
        "A diferencia del chat normal (que suelta todo el texto de golpe), <b>Aprendizaje guiado</b> escucha tus respuestas, "
        "detecta qué parte no quedó clara y adapta el ritmo a ti. Puedes usarlo con cualquier tema que siempre hayas querido aprender."
    )
    story.append(make_box(
        "¿POR QUÉ USAR «GOOGLE PROFESOR» EN LUGAR DEL CHAT NORMAL?",
        nota_html, "#EFF6FF", "#2563EB", styles
    ))

    doc.build(story)
    os.makedirs(os.path.dirname(BLQ_PDF), exist_ok=True)
    shutil.copy2(S06_PDF, BLQ_PDF)
    print(f"✅ Generado PDF PRAC-006 Catedral de Burgos: {S06_PDF}")


if __name__ == "__main__":
    build()
