# -*- coding: utf-8 -*-
"""
Genera el PDF de demostración histórica/intelectual para NotebookLM:
DEMO_HISTORIA_APOLO_11.pdf en CLASES/2. INTRODUCCION_NLM
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import cm

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_PDF = os.path.join(ROOT_DIR, "CLASES", "2. INTRODUCCION_NLM", "DEMO_HISTORIA_APOLO_11.pdf")

def create_apollo_pdf():
    os.makedirs(os.path.dirname(TARGET_PDF), exist_ok=True)
    if os.path.exists(TARGET_PDF):
        try: os.remove(TARGET_PDF)
        except Exception: pass

    doc = SimpleDocTemplate(
        TARGET_PDF,
        pagesize=A4,
        leftMargin=2*cm,
        rightMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    styles = getSampleStyleSheet()

    c_primary = colors.HexColor('#0B0F19')   # Azul noche espacial
    c_accent = colors.HexColor('#38BDF8')    # Azul cian estelar
    c_text = colors.HexColor('#334155')

    p_title = ParagraphStyle(
        'MainTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=17,
        leading=21,
        textColor=colors.white,
        alignment=1
    )

    p_sub = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#BAE6FD'),
        alignment=1
    )

    p_h2 = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12.5,
        leading=16,
        textColor=colors.HexColor('#0369A1'),
        spaceBefore=12,
        spaceAfter=5
    )

    p_body = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14.5,
        textColor=c_text,
        spaceAfter=8
    )

    p_box = ParagraphStyle(
        'BoxText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor('#0C4A6E')
    )

    story = []

    # Cabecera
    h1 = Paragraph("DOCUMENTO HISTÓRICO: EL PROYECTO APOLO 11 Y LA CONQUISTA LUNAR", p_title)
    h2 = Paragraph("Crónica científica de la mayor hazaña tecnológica del siglo XX (20 de julio de 1969)", p_sub)
    header_table = Table([[h1], [h2]], colWidths=[17*cm])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_primary),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('PADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 14))

    # Sección 1
    story.append(Paragraph("1. La Cumbre del Desafío Espacial (1961 - 1969)", p_h2))
    story.append(Paragraph(
        "En mayo de 1961, el presidente John F. Kennedy lanzó el compromiso histórico de enviar un ser humano a la Luna y devolverlo sano "
        "a la Tierra antes de que terminara la década. Lo que en su momento parecía ciencia ficción se convirtió en una movilización técnica "
        "sin precedentes: más de <b>400.000 científicos, ingenieros y técnicos</b>, y cerca de 20.000 empresas e instituciones colaboraron "
        "para hacer realidad el programa Apolo de la NASA.", p_body
    ))

    # Sección 2
    story.append(Paragraph("2. El Saturno V y el Milagro de la Computación Primitiva", p_h2))
    story.append(Paragraph(
        "El cohete colosal <b>Saturno V</b>, diseñado por el equipo de Wernher von Braun, medía 111 metros de altura y generaba una fuerza "
        "de empuje de 34,5 millones de newtons al despegar. Sin embargo, el aspecto más asombroso reside en la tecnología de a bordo: "
        "el <i>Apollo Guidance Computer (AGC)</i>, el ordenador de navegación que alunizó el módulo espacial, contaba con apenas <b>4 kilobytes de memoria RAM</b> "
        "y 72 kilobytes de memoria ROM tejida a mano con hilos magnéticos. Un teléfono inteligente moderno tiene millones de veces más capacidad de cálculo.", p_body
    ))

    # Recuadro destacado: El Papel Decisivo de España
    caja_espana = Table([[
        Paragraph(
            "<b>El papel clave de España (Fresnedillas de la Oliva, Madrid):</b><br/>"
            "Durante el momento crítico del alunizaje, la Luna estaba situada en la vertical de la Península Ibérica. "
            "La estación espacial de la NASA en <b>Fresnedillas de la Oliva (Madrid)</b> fue la que mantuvo el contacto directo y escuchó "
            "antes que nadie en el mundo la célebre frase de Neil Armstrong: <i>«Houston, aquí Base Tranquilidad. El Águila ha alunizado»</i>. "
            "El ingeniero español Carlos González Pintado y su equipo fueron condecorados por la NASA por su labor decisiva en las comunicaciones.",
            p_box
        )
    ]], colWidths=[17*cm])
    caja_espana.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F9FF')),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#0284C7')),
        ('PADDING', (0,0), (-1,-1), 9),
    ]))
    story.append(caja_espana)
    story.append(Spacer(1, 10))

    # Sección 3
    story.append(Paragraph("3. Las 21 Horas en la Superficie Lunar y el Impacto Humano", p_h2))
    story.append(Paragraph(
        "A las 20:17 UTC del 20 de julio de 1969, el módulo lunar <i>Eagle</i> se posó en el Mar de la Tranquilidad con apenas 25 segundos "
        "de combustible sobrante. Seis horas después, Armstrong descendió por la escalerilla y pronunció las palabras que definieron una época: "
        "<i>«Un pequeño paso para el hombre, un gran salto para la humanidad»</i>. "
        "Junto a Buzz Aldrin, recogieron 21,5 kilos de rocas y polvo lunar, mientras Michael Collins orbitaba en solitario en el módulo de mando <i>Columbia</i>.", p_body
    ))
    story.append(Paragraph(
        "Más de 650 millones de personas en todo el planeta contemplaron la retransmisión televisiva en directo, convirtiendo la misión "
        "en el primer acontecimiento verdaderamente global de la historia contemporánea.", p_body
    ))

    doc.build(story)
    print(f"✅ PDF Apolo creado: {TARGET_PDF}")

if __name__ == '__main__':
    create_apollo_pdf()
