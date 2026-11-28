#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_info_009_ai_studio_voz.py
Genera la Ficha Didáctica Oficial en PDF (1 página Letter):
INFO-009: Voces Realistas y Diálogos Gratis con Google AI Studio
"""

import os
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

BASE_DIR = "/Users/externo/Library/Mobile Documents/com~apple~CloudDocs/PERSONAL/CLASES DE TECNOLOGÍA/CURSO-IA"
TARGET_DIR = os.path.join(
    BASE_DIR,
    "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/15. [INFO] BLOQUE_15_INFOGRAFIAS_Y_NOVEDADES_IA/Lote_01_al_20"
)
MONO_DIR = os.path.join(
    BASE_DIR,
    "CLASES/EXPORTACION_FICHAS_CLASSROOM_PDF/105. [MONOGRAFICOS] CUADERNOS_Y_TALLERES_ESPECIALES"
)
PDF_NAME = "INFO-009_Generador_Voz_Realista_Google_AI_Studio.pdf"
PDF_PATH = os.path.join(TARGET_DIR, PDF_NAME)
PDF_MONO = os.path.join(MONO_DIR, PDF_NAME)


def build_pdf():
    os.makedirs(TARGET_DIR, exist_ok=True)
    os.makedirs(MONO_DIR, exist_ok=True)

    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=28,
        bottomMargin=24
    )
    W = letter[0] - 72
    styles = getSampleStyleSheet()

    h_tag = ParagraphStyle('HTag', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=colors.HexColor('#93C5FD'))
    h_title = ParagraphStyle('HTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=14.5, leading=17.5, textColor=colors.white)
    h_sub = ParagraphStyle('HSub', parent=styles['Normal'], fontName='Helvetica', fontSize=9.2, leading=12, textColor=colors.HexColor('#E2E8F0'))

    sec_title = ParagraphStyle('SecTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10.5, leading=13, textColor=colors.HexColor('#0F172A'), spaceBefore=6, spaceAfter=3)
    body = ParagraphStyle('Body', parent=styles['Normal'], fontName='Helvetica', fontSize=9.2, leading=12.6, textColor=colors.HexColor('#1E293B'))
    bullet = ParagraphStyle('Bullet', parent=styles['Normal'], fontName='Helvetica', fontSize=9.0, leading=12.2, textColor=colors.HexColor('#1E293B'), leftIndent=10)
    prompt_lbl = ParagraphStyle('PLbl', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.8, leading=11.5, textColor=colors.HexColor('#1D4ED8'))
    prompt_txt = ParagraphStyle('PTxt', parent=styles['Normal'], fontName='Helvetica', fontSize=8.7, leading=11.8, textColor=colors.HexColor('#0F172A'))

    story = []

    # Cabecera azul marino
    t_head = Table([[
        [
            Paragraph("INFO-009  |  NOVEDADES DE IA PARA MAYORES (+65)  |  HERRAMIENTA GRATUITA EN NAVEGADOR", h_tag),
            Paragraph("Voces Realistas y Diálogos Gratis con Google AI Studio", h_title),
            Paragraph("Convierte cuentos, recuerdos o diálogos familiares en audio humano natural sin instalar nada", h_sub)
        ]
    ]], colWidths=[W])
    t_head.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#0F172A')),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('ROUNDEDCORNERS', [6, 6, 6, 6]),
    ]))
    story.append(t_head)
    story.append(Spacer(1, 6))

    # 1. Qué es
    story.append(Paragraph("1. ¿Qué es y para qué nos sirve en clase?", sec_title))
    story.append(Paragraph(
        "Google AI Studio incluye un generador oficial y gratuito de texto a voz (<b>aistudio.google.com/generate-speech</b>). "
        "A diferencia de las voces robóticas antiguas, esta herramienta añade <b>entonación humana, pausas y respiración natural</b>, "
        "permitiendo incluso crear conversaciones realistas entre <b>dos personas distintas</b> para narrar cuentos a los nietos, "
        "dar voz a recuerdos de tu biografía o acompañar fotografías históricas.", body
    ))
    story.append(Spacer(1, 4))

    # 2. Paso a paso en 4 clics
    story.append(Paragraph("2. Cómo usarlo paso a paso (4 clics, sin instalar nada)", sec_title))
    steps = [
        "<b>Paso 1 (Entrar):</b> Abre <b>https://aistudio.google.com/generate-speech</b> e inicia sesión con tu cuenta de Google.",
        "<b>Paso 2 (Elegir modo):</b> Pulsa en <b>«Crear nuevo diálogo»</b> (puedes elegir <b>1 voz</b> para narración o <b>2 voces</b> para conversación). <i>Truco: si sale en inglés, clic derecho → Traducir al español.</i>",
        "<b>Paso 3 (Personalizar voz):</b> Filtra por idioma (<b>Español</b>), género y estilo (ej. <i>Amigable</i> o <i>Cuentacuentos cálido</i>). En <b>Expresión</b> puedes activar matices reales como la respiración del locutor.",
        "<b>Paso 4 (Generar y descargar):</b> Pega tu texto, pulsa generar, escucha el resultado y descárgalo listo para enviar por WhatsApp o integrarlo con música de Google Flow."
    ]
    t_steps = Table([[[Paragraph(f"• {s}", bullet) for s in steps]]], colWidths=[W])
    t_steps.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8FAFC')),
        ('BOX', (0, 0), (-1, -1), 0.8, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_steps)
    story.append(Spacer(1, 5))

    # 3. Dos pruebas prácticas listas para copiar
    story.append(Paragraph("3. Textos de prueba listos para copiar y escuchar", sec_title))

    t_p1 = Table([[
        [
            Paragraph("🎙️ PRUEBA A (1 VOZ — CUENTO O RECUERDO EN TONO CÁLIDO Y AMIGABLE):", prompt_lbl),
            Spacer(1, 2),
            Paragraph("«Había una vez un relojero en Madrid que guardaba los recuerdos del barrio en pequeñas cajas de música. Cada tarde, al caer el sol sobre la Puerta de Alcalá, abría una caja distinta para escuchar las risas de los abuelos y contarles una historia nueva a sus nietos.»", prompt_txt)
        ]
    ]], colWidths=[W])
    t_p1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#EFF6FF')),
        ('BOX', (0, 0), (-1, -1), 0.9, colors.HexColor('#3B82F6')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_p1)
    story.append(Spacer(1, 4))

    t_p2 = Table([[
        [
            Paragraph("🗣️ PRUEBA B (DIÁLOGO A 2 VOCES — ABUELO Y NIETA):", prompt_lbl),
            Spacer(1, 2),
            Paragraph(
                "<b>Voz 1 (Abuelo):</b> ¿Sabes cómo sonaban las calles de Madrid cuando construyeron el Palacio de Cibeles?<br/>"
                "<b>Voz 2 (Nieta):</b> ¡Cuéntamelo, abuelo! ¿Había ya coches o todavía pasaban tranvías y organillos?<br/>"
                "<b>Voz 1 (Abuelo):</b> Pasaban tranvías amarillos y carros de madera, y todo el mundo se saludaba por su nombre.",
                prompt_txt
            )
        ]
    ]], colWidths=[W])
    t_p2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F0FDF4')),
        ('BOX', (0, 0), (-1, -1), 0.9, colors.HexColor('#22C55E')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_p2)
    story.append(Spacer(1, 5))

    # 4. 3 Preguntas de reflexión en el aula
    story.append(Paragraph("4. Tres preguntas clave para comentar en el aula", sec_title))
    q_list = [
        "1. ¿Qué diferencia notas al activar un <b>Estilo</b> (como <i>Amigable</i>) y la <b>Expresión</b> frente a una voz plana de GPS?",
        "2. ¿Qué precauciones debemos tener si escuchamos audios muy realistas por WhatsApp de supuestos familiares o bancos?",
        "3. ¿Cómo combinarías este audio narrado con la música de época de <b>Google Flow Music</b> (<code>labs.google/flow</code>) para crear una postal sonora?"
    ]
    t_q = Table([[[Paragraph(q, bullet) for q in q_list]]], colWidths=[W])
    t_q.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#FFFBEB')),
        ('BOX', (0, 0), (-1, -1), 0.8, colors.HexColor('#F59E0B')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t_q)

    doc.build(story)
    shutil.copyfile(PDF_PATH, PDF_MONO)
    print(f"PDF generado y copiado: {PDF_PATH} y {PDF_MONO}")


if __name__ == "__main__":
    build_pdf()
