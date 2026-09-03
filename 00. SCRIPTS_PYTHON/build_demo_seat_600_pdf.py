# -*- coding: utf-8 -*-
"""
Genera el PDF de demostración para la clase práctica de NotebookLM:
DEMO_HISTORIA_SEAT_600.pdf en CLASES/2. INTRODUCCION_NLM
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import cm

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_PDF = os.path.join(ROOT_DIR, "CLASES", "2. INTRODUCCION_NLM", "DEMO_HISTORIA_SEAT_600.pdf")

def create_demo_pdf():
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

    c_primary = colors.HexColor('#1E293B')
    c_accent = colors.HexColor('#2563EB')
    c_text = colors.HexColor('#334155')

    p_title = ParagraphStyle(
        'MainTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.white,
        alignment=1
    )

    p_sub = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#E2E8F0'),
        alignment=1
    )

    p_h2 = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=c_accent,
        spaceBefore=12,
        spaceAfter=6
    )

    p_body = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10.5,
        leading=15,
        textColor=c_text,
        spaceAfter=8
    )

    p_box = ParagraphStyle(
        'BoxText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#1E3A8A')
    )

    story = []

    # Cabecera
    h1 = Paragraph("DOCUMENTO HISTÓRICO: EL FENÓMENO DEL SEAT 600 EN ESPAÑA", p_title)
    h2 = Paragraph("Crónica divulgativa de la motorización y transformación social (1957 - 1973)", p_sub)
    header_table = Table([[h1], [h2]], colWidths=[17*cm])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_primary),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('PADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 14))

    # Sección 1
    story.append(Paragraph("1. El Nacimiento de un Mito (Junio de 1957)", p_h2))
    story.append(Paragraph(
        "El 27 de junio de 1957 salió de la factoría de la Zona Franca de Barcelona el primer <b>SEAT 600</b> comercializado. "
        "Su precio de lanzamiento fue de <b>65.000 pesetas</b>, lo que equivalía a casi tres años y medio de salario medio de un trabajador de la época. "
        "A pesar de ese coste considerable, el vehículo desató una fiebre popular sin precedentes: en apenas unos meses, la lista de espera "
        "para recibir un 600 superaba los <b>dos años de espera</b>.", p_body
    ))

    # Sección 2
    story.append(Paragraph("2. Características Técnicas Populares", p_h2))
    story.append(Paragraph(
        "Diseñado originalmente por el ingeniero italiano Dante Giacosa y fabricado bajo licencia en España, el coche tenía un motor "
        "trasero de 4 cilindros y apenas <b>633 centímetros cúbicos</b>, que desarrollaba 18 a 21 caballos de potencia. "
        "Su velocidad máxima teórica era de 95 km/h, aunque con el coche cargado rara vez pasaba de 80 km/h en las carreteras nacionales.", p_body
    ))
    story.append(Paragraph(
        "Una de sus señas de identidad más recordadas era la apertura de las puertas hacia atrás (conocidas popularmente como <i>«puertas suicidas»</i> "
        "o <i>«mirabragas»</i>), que se mantuvieron hasta el modelo 600-D en 1963, cuando pasaron a abrir de manera convencional hacia delante.", p_body
    ))

    # Recuadro destacado
    caja = Table([[
        Paragraph(
            "<b>Dato histórico clave:</b> En 1957 apenas circulaban 100.000 automóviles privados en toda España. "
            "Para 1973, cuando cesó su producción tras fabricarse <b>794.406 unidades</b>, el 600 representaba uno de cada cuatro coches que transitaban por el país.",
            p_box
        )
    ]], colWidths=[17*cm])
    caja.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EFF6FF')),
        ('BOX', (0,0), (-1,-1), 1, c_accent),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(caja)
    story.append(Spacer(1, 10))

    # Sección 3
    story.append(Paragraph("3. La Revolución Social y los Viajes Familiares", p_h2))
    story.append(Paragraph(
        "Más allá de la mecánica, el 600 fue el catalizador del turismo familiar de la clase media española. "
        "Por primera vez, las familias de clase trabajadora podían planificar sus vacaciones hacia la costa (Alicante, Valencia, Málaga o Santander). "
        "Los viajes se convertían en auténticas expediciones: se instalaba la baca de metal en el techo cargada de maletas y enseres, "
        "el interior viajaba con cinco o seis personas (incluidos abuelos y niños), y era habitual parar en los arcenes o puertos de montaña "
        "para dejar enfriar el motor y echar agua fresca al radiador.", p_body
    ))
    story.append(Paragraph(
        "El Seat 600 democratizó el fin de semana, la libertad de movimiento y el reencuentro con los pueblos de origen durante las fiestas patronales.", p_body
    ))

    doc.build(story)
    print(f"✅ PDF demo creado: {TARGET_PDF}")

if __name__ == '__main__':
    create_demo_pdf()
