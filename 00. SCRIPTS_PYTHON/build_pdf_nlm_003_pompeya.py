#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de la ficha didáctica senior (+65):
4B. NLM-003_Mini_Curso_Interactivo_Pompeya.pdf
Inicia con la URL de YouTube de Pompeya como fuente en NotebookLM
y entrega los 5 prompts exactos para generar los 5 artefactos interactivos del curso
(Curso animado, Mapa histórico Auto-Play, Línea temporal, Juego 3D/Arcade y Duelo RPG).
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
        Spacer(1, 2),
        Paragraph(body_html, styles["BoxBody"]),
    ]
    t = Table([[content]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(bg_hex)),
        ("BOX", (0, 0), (-1, -1), 1.1, colors.HexColor(border_hex)),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    return t


def make_artifact_card(num_badge, title, prompt_html, bg_hex, border_hex, styles):
    content = [
        Paragraph(f"<b>{num_badge} · {title}</b>", styles["CardTitle"]),
        Spacer(1, 3),
        Paragraph(prompt_html, styles["PromptText"]),
    ]
    t = Table([[content]], colWidths=[17.4 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(bg_hex)),
        ("BOX", (0, 0), (-1, -1), 1.0, colors.HexColor(border_hex)),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    return t


def build():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="Kicker", fontName="Helvetica-Bold", fontSize=8.3, leading=10.5,
        textColor=colors.HexColor("#0369A1")
    ))
    styles.add(ParagraphStyle(
        name="MainTitle", fontName="Helvetica-Bold", fontSize=14.8, leading=18,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="SubTitle", fontName="Helvetica", fontSize=9.1, leading=12.2,
        textColor=colors.HexColor("#475569")
    ))
    styles.add(ParagraphStyle(
        name="SectionHead", fontName="Helvetica-Bold", fontSize=10.8, leading=13.5,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="BoxTitle", fontName="Helvetica-Bold", fontSize=9.8, leading=12.8,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="BoxBody", fontName="Helvetica", fontSize=8.9, leading=12.2,
        textColor=colors.HexColor("#1E293B")
    ))
    styles.add(ParagraphStyle(
        name="CardTitle", fontName="Helvetica-Bold", fontSize=9.8, leading=12.5,
        textColor=colors.HexColor("#0F172A")
    ))
    styles.add(ParagraphStyle(
        name="PromptText", fontName="Helvetica", fontSize=8.7, leading=11.9,
        textColor=colors.HexColor("#0F172A")
    ))

    doc = SimpleDocTemplate(
        OUT_PDF, pagesize=A4,
        leftMargin=1.8 * cm, rightMargin=1.8 * cm,
        topMargin=1.2 * cm, bottomMargin=1.2 * cm
    )

    story = []

    # Cabecera
    header_box = Table([[
        [
            Paragraph("SESIÓN 03 · ÍTEM #08B [NLM-003] · CURSO INTERACTIVO CON ARTEFACTOS", styles["Kicker"]),
            Spacer(1, 2),
            Paragraph("Pompeya: Crea un Curso Interactivo en Gemini Notebook", styles["MainTitle"]),
            Spacer(1, 2),
            Paragraph(
                "Carga el documental de YouTube como fuente en NotebookLM y envía estos 5 prompts en el chat "
                "(uno a uno) para generar 5 artefactos interactivos con animación: Curso, Mapa, Línea Temporal, Juego y Duelo RPG.",
                styles["SubTitle"]
            ),
        ]
    ]], colWidths=[17.4 * cm])
    header_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F0F9FF")),
        ("BOX", (0, 0), (-1, -1), 1.3, colors.HexColor("#0284C7")),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(header_box)
    story.append(Spacer(1, 7))

    # Paso Inicial: Fuente de YouTube
    fuente_html = (
        "1. Abre <b>https://notebooklm.google.com</b>, pulsa <b>«+ Crear cuaderno»</b> y ponle de título <b>Pompeya - Curso Interactivo</b>.<br/>"
        "2. En <b>Añadir fuente</b>, elige <b>YouTube</b>, pega exactamente esta URL y pulsa <b>Insertar</b>:<br/>"
        f"<b><font color='#0369A1'>{YOUTUBE_URL}</font></b><br/>"
        "3. Envía los siguientes <b>5 prompts de uno en uno en el chat</b> (en el chat de NotebookLM o desde <b>Gemini</b> vinculando este cuaderno con el botón <b>+ → NotebookLM</b>). Cada prompt creará un <b>artefacto interactivo separado</b> que podrás abrir y ver aparte."
    )
    story.append(make_box(
        "PASO INICIAL · CARGA LA FUENTE DE YOUTUBE",
        fuente_html, "#FEF3C7", "#D97706", styles
    ))
    story.append(Spacer(1, 8))

    story.append(Paragraph("LOS 5 PROMPTS PARA CREAR LOS 5 ARTEFACTOS DEL CURSO (UNO POR MENSAJE)", styles["SectionHead"]))
    story.append(Spacer(1, 5))

    # Prompt 1: Curso Interactivo con Simuladores en Movimiento
    story.append(make_artifact_card(
        "ARTEFACTO 1",
        "Curso Interactivo con Simuladores en Movimiento",
        "<i>«A partir de las fuentes cargadas en este cuaderno, créame un artefacto interactivo tipo curso completo dividido en 3 bloques progresivos sobre Pompeya y la erupción del Vesubio.<br/>"
        "Requisitos obligatorios:<br/>"
        "1. Incluye en cada bloque un simulador visual animado en movimiento (en tiempo real, que el usuario pueda manipular con botones o deslizadores, no texto estático).<br/>"
        "2. Al final de cada bloque, añade un mini-cuestionario autocorregible que explique por qué cada respuesta es correcta o incorrecta.<br/>"
        "3. Usa tipografía grande, clara y botones visuales cómodos para proyectar en clase.»</i>",
        "#F8FAFC", "#0284C7", styles
    ))
    story.append(Spacer(1, 6))

    # Prompt 2: Mapa Histórico Animado
    story.append(make_artifact_card(
        "ARTEFACTO 2",
        "Mapa Histórico Animado (▶ Auto-Play)",
        "<i>«Créame un mapa histórico interactivo y animado basado en las fuentes de este cuaderno sobre Pompeya, el monte Vesubio y el golfo de Nápoles.<br/>"
        "Requisitos obligatorios:<br/>"
        "1. Las capas de color de cada fase (ciudad viva, lluvia de ceniza, flujos piroclásticos y área sepultada) deben adaptarse estrictamente a la geografía, el relieve y las líneas de costa reales (no uses rectángulos genéricos).<br/>"
        "2. Añade una línea de tiempo inferior con un botón de \"Reproducir / Auto-Play\" que anime la evolución paso a paso de forma continua, además de botones manuales para cada fase.<br/>"
        "3. Incluye un interruptor para activar o desactivar las fronteras actuales superpuestas y puntos clicables con explicación breve en cada lugar clave.»</i>",
        "#F8FAFC", "#7C3AED", styles
    ))
    story.append(Spacer(1, 6))

    # Prompt 3: Línea Temporal Interactiva con Filtros
    story.append(make_artifact_card(
        "ARTEFACTO 3",
        "Línea Temporal Interactiva con Filtros",
        "<i>«Créame una línea temporal interactiva a partir de las fuentes de este cuaderno sobre Pompeya y la erupción del Vesubio.<br/>"
        "Requisitos obligatorios:<br/>"
        "1. Permite alternar entre vista horizontal y vista vertical.<br/>"
        "2. Añade botones de filtro arriba por categorías (Todos, Vida en Pompeya, Erupción del Vesubio, Hallazgos Arqueológicos).<br/>"
        "3. Al hacer clic en cada fecha o hito, debe desplegarse una tarjeta visual clara con su explicación y su importancia histórica.»</i>",
        "#F0FDF4", "#16A34A", styles
    ))
    story.append(Spacer(1, 6))

    # Prompt 4: Juego Formativo en Movimiento
    story.append(make_artifact_card(
        "ARTEFACTO 4",
        "Juego Formativo en Movimiento (Arcade / 3D por Niveles)",
        "<i>«Diseña un juego educativo interactivo y en movimiento (a 60 fps, estilo arcade o 3D) basado en los conceptos clave de las fuentes de este cuaderno sobre Pompeya y el Vesubio.<br/>"
        "Requisitos obligatorios:<br/>"
        "1. El jugador debe moverse, esquivar obstáculos (rocas volcánicas y nubes de ceniza) o rescatar objetos históricos en tiempo real usando teclado o botones táctiles grandes en pantalla.<br/>"
        "2. Organízalo en 4 niveles de dificultad progresiva que integren los conceptos reales del vídeo.<br/>"
        "3. Muestra puntuación, vidas y un breve dato educativo cada vez que se supera un nivel.»</i>",
        "#FFF7ED", "#EA580C", styles
    ))
    story.append(Spacer(1, 6))

    # Prompt 5: Examen Gamificado Tipo Duelo RPG
    story.append(make_artifact_card(
        "ARTEFACTO 5",
        "Examen Gamificado Tipo Duelo RPG (2 Jugadores / Equipos en Clase)",
        "<i>«Créame un examen interactivo tipo duelo RPG por turnos para 2 jugadores o 2 equipos en el aula sobre las fuentes de este cuaderno (Pompeya y el Vesubio).<br/>"
        "Requisitos obligatorios:<br/>"
        "1. Pantalla inicial para escribir el nombre de los 2 equipos y elegir la duración de la partida (corta, media o larga).<br/>"
        "2. Durante el duelo: barras de vida/energía animadas, temporizador de cuenta atrás en cada turno y preguntas tipo test sacadas exclusivamente del vídeo.<br/>"
        "3. Si el equipo acierta, resta energía al rival; si falla o se agota el tiempo, pierde energía propia. Tras cada pregunta, muestra siempre la explicación correcta.»</i>",
        "#FDF2F8", "#DB2777", styles
    ))

    doc.build(story)
    print(f"✅ Generado PDF NLM-003 Pompeya (5 Artefactos Curso): {OUT_PDF}")


if __name__ == "__main__":
    build()
