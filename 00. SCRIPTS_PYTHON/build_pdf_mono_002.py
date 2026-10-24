#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pdf_mono_002.py
Genera la Ficha Didáctica Oficial del Monográfico 02 (Letter/A4):
MONO-002_104_Estilos_Animados_Sin_Programar.pdf
para el Curso de IA para Adultos Mayores (60+).
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
OUTPUT_DIR_104 = os.path.join(BASE_DIR, "104 ESTILO ANIMADOS SIN PROGRAMAR")
OUTPUT_DIR_CLASSROOM = os.path.join(BASE_DIR, "CLASES", "EXPORTACION_FICHAS_CLASSROOM_PDF", "105. [MONOGRAFICOS] CUADERNOS_Y_TALLERES_ESPECIALES", "MONO-002")
os.makedirs(OUTPUT_DIR_104, exist_ok=True)
os.makedirs(OUTPUT_DIR_CLASSROOM, exist_ok=True)

PDF_FILENAME = "MONO-002_104_Estilos_Animados_Sin_Programar.pdf"
DEST_PATH_104 = os.path.join(OUTPUT_DIR_104, PDF_FILENAME)
DEST_PATH_CLASS = os.path.join(OUTPUT_DIR_CLASSROOM, PDF_FILENAME)

def build_mono_002_pdf():
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    doc = SimpleDocTemplate(
        DEST_PATH_104,
        pagesize=letter,
        rightMargin=36, leftMargin=36, topMargin=22, bottomMargin=20
    )
    styles = getSampleStyleSheet()

    style_header = ParagraphStyle(
        'HeaderStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8.0,
        textColor=colors.HexColor('#0284C7'), alignment=1, spaceAfter=1
    )
    style_block = ParagraphStyle(
        'BlockStyle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.5,
        textColor=colors.HexColor('#0F172A'), alignment=1, spaceAfter=3
    )
    style_title = ParagraphStyle(
        'TitleStyle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=11.5, leading=14.0,
        textColor=colors.HexColor('#0F172A'), spaceAfter=3
    )
    style_section_h = ParagraphStyle(
        'SectionHStyle', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=8.6, leading=11.0,
        textColor=colors.HexColor('#0369A1'), spaceBefore=3, spaceAfter=2
    )
    style_body = ParagraphStyle(
        'BodyStyle', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=7.8, leading=10.4,
        textColor=colors.HexColor('#1E293B'), spaceAfter=2
    )
    style_task = ParagraphStyle(
        'TaskStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.5, leading=9.8,
        textColor=colors.HexColor('#0F172A')
    )
    style_prompt = ParagraphStyle(
        'PromptStyle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=7.2, leading=9.3,
        textColor=colors.HexColor('#0F172A')
    )

    story = []
    story.append(Paragraph("CURSO DE INTELIGENCIA ARTIFICIAL Y TECNOLOGÍA PARA ADULTOS MAYORES (60+)", style_header))
    story.append(Paragraph("MONOGRÁFICOS ESPECIALES & CUADERNOS DE TALLER PRÁCTICO [MONO-002]", style_block))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#0284C7'), spaceAfter=4))

    story.append(Paragraph("<b>[MONO-002] Taller Especial: 104 Estilos Animados que puedes pedirle a la IA sin Programar</b>", style_title))

    story.append(Paragraph("💡 <b>La Magia de Crear Animaciones sin Escribir Código:</b>", style_section_h))
    story.append(Paragraph(
        "¿Sabías que puedes pedirle a Gemini o Claude que construya en segundos una animación interactiva con movimiento profesional sin que tengas que saber ni una sola línea de programación? "
        "En este monográfico descubrimos una técnica visual revolucionaria: <b>la caja negra de prompt cerrado</b>. Solo copias el texto, cambias tus datos cotidianos (tu receta, tu reto de salud o tu lista de recuerdos) y la IA te entrega una página web animada lista para abrir con doble clic.",
        style_body
    ))

    # El Método en 3 Pasos
    story.append(Paragraph("📋 <b>El Método Sencillo en 3 Pasos:</b>", style_section_h))
    steps_rows = [
        [Paragraph("<b>1. Elige tu ejercicio:</b> Escoge uno de los 6 estilos preparados abajo o abre el catálogo de 104 estilos para curiosear.", style_task)],
        [Paragraph("<b>2. Copia y cambia [TU CONTENIDO]:</b> Pega el texto en Gemini (<i>gemini.google.com</i>) y pon tus propios ingredientes, cifras o recuerdos.", style_task)],
        [Paragraph("<b>3. Disfruta tu creación:</b> Gemini te entregará el código. Haz clic en «Copiar código», guárdalo en tu ordenador y ¡mira cómo se mueve!", style_task)],
    ]
    st_table = Table(steps_rows, colWidths=[letter[0] - 72])
    st_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0284C7')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(st_table)
    story.append(Spacer(1, 3))

    # Los 6 Ejercicios Prácticos
    story.append(Paragraph("🌟 <b>Los 6 Ejercicios Prácticos Listos para Usar en Clase:</b>", style_section_h))

    ex_rows = [
        [Paragraph("<b>🧾 Ejercicio 1 • Ticket que se imprime (Estilo #010):</b> "
                   "Una impresora de caja va soltando un ticket línea a línea con tu lista de la compra o los pasos de una receta tradicional, sellando el total en rojo.<br/>"
                   "<i>Prompt: «Crea una sola página HTML con animación de ticket de caja registradora. Fondo gris oscuro, papel blanco que baja línea a línea con tipografía de máquina: [TUS INGREDIENTES O GASTOS: concepto e importe]. Al final estampa un sello circular rojo con el TOTAL.»</i>", style_prompt)],
        [Paragraph("<b>🚗 Ejercicio 2 • Velocímetro de Reto de Salud (Estilo #006):</b> "
                   "Un velocímetro con arco rojo, amarillo y verde donde una aguja sube y se clava en tu objetivo de pasos caminados o litros de agua del día.<br/>"
                   "<i>Prompt: «Crea una página HTML con animación de aguja tipo velocímetro con arco verde, amarillo y rojo. La aguja sube desde cero y se clava en el valor real: [INDICADOR: Caminar 6.000 pasos · Objetivo: 6.000 · Conseguido: 6.450]. Si supera el objetivo, destello verde.»</i>", style_prompt)],
        [Paragraph("<b>👥 Ejercicio 3 • De cada 100 personas (Estilo #008):</b> "
                   "100 personitas en cuadrícula que se iluminan como una ola para visualizar proporciones humanas y familiares de forma entrañable.<br/>"
                   "<i>Prompt: «Crea una página HTML con animación de pictograma de 10×10 personitas dibujadas. Las figuras aparecen y se iluminan en color azul intenso según el dato: [De cada 100 abuelos, 82 hacen videollamadas semanales con sus nietos]. Contador numérico que sube.»</i>", style_prompt)],
        [Paragraph("<b>🚦 Ejercicio 4 • Semáforo de Seguridad y Tranquilidad (Estilo #013):</b> "
                   "Tres luces de semáforo que guían con claridad ante llamadas desconocidas (Verde: familia / Amarillo: comercial / Rojo: piden dinero o claves = colgar).<br/>"
                   "<i>Prompt: «Crea una página HTML con animación de semáforo de tres luces grandes y claras: [Verde: Familia conocida · Amarillo: Ofertas comerciales con calma · Rojo: Si piden contraseñas o cuentas bancarias, cuelga de inmediato]. Conclusión grande abajo.»</i>", style_prompt)],
        [Paragraph("<b>↔️ Ejercicio 5 • Comparador Antes y Después (Estilo #002):</b> "
                   "Una barra deslizante interactiva que permite comparar dos recuerdos, fotos de vacaciones de antes y de ahora o la reforma de una habitación.<br/>"
                   "<i>Prompt: «Crea una página HTML con animación interactiva de cortinilla de Antes y Después. Una línea vertical que se desliza y revela dos situaciones: [Antes: La plaza del pueblo en 1970 vs Después: La plaza peatonal en 2026]. Con etiquetas grandes.»</i>", style_prompt)],
        [Paragraph("<b>📅 Ejercicio 6 • Tu Año en Resumen (Estilo #009):</b> "
                   "Tarjetas de colores alegres con números grandes tipo resumen musical que van pasando con transiciones dinámicas para celebrar los grandes hitos familiares.<br/>"
                   "<i>Prompt: «Crea una página HTML con animación tipo resumen anual: pantallas de colores vivos que pasan con transiciones dinámicas. Cada pantalla con una cifra enorme y un recuerdo: [1: 52 domingos en familia · 2: 1 viaje a la playa · 3: 1 nuevo nieto].»</i>", style_prompt)],
    ]

    p_table = Table(ex_rows, colWidths=[letter[0] - 72])
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#64748B')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(p_table)
    story.append(Spacer(1, 3))

    # Catálogo Completo de 104 Estilos
    story.append(Paragraph("📚 <b>¿Quieres más? El Catálogo Completo de 104 Estilos para Casa:</b>", style_section_h))
    extra_text = (
        "• <b>El documento original con dibujos:</b> Tienes a tu disposición el PDF completo <i>«104 Estilos Animados que puedes pedirle a la IA sin Programar»</i> (por Paco Vida / DiarioVida). "
        "En él verás los 104 ejemplos dibujados con sus miniaturas (cronologías de fotos, pizarras de tiza, cartas que se abren, velocímetros y titulares de prensa).<br/>"
        "• <b>Galería interactiva en vivo:</b> Puedes ver las 104 animaciones en movimiento antes de elegir entrando en: <b>diariovida.com/galeria-animaciones-ia</b>."
    )
    e_table = Table([[Paragraph(extra_text, style_task)]], colWidths=[letter[0] - 72])
    e_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ECFDF5')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#059669')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(e_table)

    doc.build(story)

    # Copiar a carpeta Classroom
    import shutil
    try:
        shutil.copy2(DEST_PATH_104, DEST_PATH_CLASS)
    except Exception:
        pass

    print(f"✅ PDF MONO-002 generado con éxito en:\n   {DEST_PATH_104}\n   {DEST_PATH_CLASS}")

if __name__ == '__main__':
    try:
        build_mono_002_pdf()
    except Exception as e:
        print(f"❌ Error al generar PDF MONO-002: {e}")
        sys.exit(1)

